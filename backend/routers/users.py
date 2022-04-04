import datetime
from typing import List
from core.db import engine, get_db
from sqlalchemy.orm import Session
from services.user import models, schemes
from services.user.logic import UserLogic
from fastapi import APIRouter, Path, Depends, HTTPException


models.Base.metadata.create_all(bind=engine)

router = APIRouter()
logic = UserLogic()


@router.post("/user/", response_model=schemes.User, tags=['User'])
async def create_user(user: schemes.UserCreate, db: Session = Depends(get_db)):
    db_user = logic.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=403, detail="Email already registered")
    res = logic.create_user(db=db, user=user, password=user.password, register_date=datetime.datetime.now())
    if res.get('user'):
        return res['user']
    return res


@router.delete("/user/{user_id}", tags=["User"])
async def delete_user(user_id: int = Path(..., title="Id of user"), db: Session = Depends(get_db)):
    res = logic.delete_user(db, user_id=user_id)
    return res


@router.get("/user/{user_id}", response_model=schemes.User, tags=["User"])
async def get_user(user_id: int = Path(..., title="Id of user"), db: Session = Depends(get_db)):
    db_user = logic.get_user_by_id(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User does not exists")
    return db_user


@router.get("/user-list/", response_model=List[schemes.User], tags=["User"])
async def get_all_user(skip: int = 0, limit: int = 100, db=Depends(get_db)):
    db_user = logic.get_users(db, skip=skip, limit=limit)
    if not db_user:
        return HTTPException(status_code=404, detail="Users does not exists")
    return db_user


@router.patch('/user/{user_id}', tags=['User'])
async def patch_user(user_id: int, user: schemes.UserPatch, db: Session = Depends((get_db))):
    res = logic.patch_user(db=db, user=user, user_id=user_id)
    return res


@router.put('/user/{user_id}', tags=['User'])
async def put_user(user_id: int, user: schemes.UserCreate, db: Session = Depends((get_db))):
    res = logic.put_user(db=db, user=user, user_id=user_id)
    return res
