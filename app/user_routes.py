from fastapi import APIRouter, HTTPException
from typing import List
from .crud import insert_user, get_all_users, update_user, delete_user
from .schemas import UserCreate, UserUpdate


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=dict)
def create_user(user: UserCreate):
    try:
        response = insert_user(
            user.first_name,
            user.last_name,
            user.city,
            user.country,
            user.zip_code
        )
        return response.data[0]  
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[dict])
def read_users():
    return get_all_users()

@router.put("/{user_id}", response_model=dict)
def update_user_route(user_id: int, user: UserUpdate):
    update_data = {k: v for k, v in user.dict().items() if v is not None}

    if not update_data:
        raise HTTPException(status_code=400, detail="No data provided for update")

    try:
        response = update_user(user_id, update_data)

        if not response.data:
            raise HTTPException(status_code=404, detail="User not found")

        return response.data[0]

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/{user_id}", response_model=dict)
def delete_user_route(user_id: int):
    try:
        response = delete_user(user_id)

        if not response.data:
            raise HTTPException(status_code=404, detail="User not found")

        return response.data[0]

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
