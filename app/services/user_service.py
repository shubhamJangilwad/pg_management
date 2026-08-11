from fastapi import HTTPException
from app.models.users import User
from app.services.password import hash_password , verify_password
from app.services.auth import create_access_token



def user_create_service(body,db):
    user_email= db.query(User).filter(body.email == User.email).first()

    if user_email:
        raise HTTPException (
            status_code= 409,
            detail= "Conflict"
        )

    user_phone = db.query(User).filter(body.phone_no == User.phone_no).first()

    if user_phone:
            raise HTTPException (
                status_code= 409,
                detail= "Conflict"
            )
    else:
        try:

            user_create = User(
                full_name = body.full_name,
                email = body.email,
                phone_no = body.phone_no,
                password = hash_password(body.password),
                role = "owner"
            )

            db.add(user_create)
            db.commit()
            db.refresh(user_create)

            return user_create
        except Exception as e:
            db.rollback()
            print(e)


def user_login_service(form_data,db):
     user_email = db.query(User).filter(form_data.username == User.email).first()

     if not user_email:
          raise HTTPException(
               status_code=404,
               detail= "Email not found"
          )

     password_check = verify_password(form_data.password , user_email.password)

     if not password_check:
          raise HTTPException(
               status_code= 401,
               detail= "invalid Email or password"
          )
     else:

        token = create_access_token({
        "user_id": user_email.id,
        "role": user_email.role
    })

        return {
        "access_token": token,
        "token_type": "bearer"
    }
            