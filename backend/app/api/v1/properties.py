from typing import Any, Dict, List

from fastapi import APIRouter, Depends

from app.core.auth import authenticate_request as get_current_user
from app.services.cache import get_properties_data

router = APIRouter()

@router.get("/properties/")
async def get_properties(current_user: dict = Depends(get_current_user)) -> List[Dict[str, Any]]:
    tenant_id = getattr(current_user, "tenant_id", "default_tenant") or "default_tenant"

    properties_data = await get_properties_data(tenant_id)

    return properties_data