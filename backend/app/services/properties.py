from typing import Any, Dict, List


async def get_properties_list(tenant_id: str) -> List[Dict[str, Any]]:
    """
    Fetches all properties with tenant_id from database.
    """
    try:
        from app.core.database_pool import DatabasePool

        db_pool = DatabasePool()
        await db_pool.initialize()

        if db_pool.session_factory:
            async with await db_pool.get_session() as session:
                from sqlalchemy import text

                query = text("""
                    SELECT *
                    FROM properties 
                    WHERE tenant_id = :tenant_id
                """)

                result = await session.execute(query, {"tenant_id": tenant_id})
                rows = result.mappings().all()
                return [dict(r) for r in rows]
        else:
            raise Exception("Database pool not available")

    except Exception as e:
        print(f"Database error for (tenant: {tenant_id}): {e}")
        return []
