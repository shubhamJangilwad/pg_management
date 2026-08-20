from fastapi import APIRouter , Depends
from app.database import get_db
from app.schemas.tenant_schema import TenantCreate , TenantResponse
from sqlalchemy.orm import Session
from app.services.auth import get_current_user
from app.services.tenant_service import create_tenant_service , get_tenants_service , get_tenant_by_id_service


Tenants = APIRouter()

@Tenants.post("/create/tenant",response_model=TenantResponse)
def create_tenant(body : TenantCreate,
                current_user = Depends(get_current_user),
                db:Session = Depends(get_db)):

    return create_tenant_service(body,current_user,db)


@Tenants.get("/get/tenants")
def get_tenant(current_user = Depends(get_current_user),
               db:Session = Depends(get_db)):
        return get_tenants_service(current_user,db)


@Tenants.get("/get/tenant/{tenant_id}")
def get_tenant(tenant_id : int,
       current_user = Depends(get_current_user),
       db:Session = Depends(get_db)):
      return get_tenant_by_id_service(tenant_id,current_user,db)