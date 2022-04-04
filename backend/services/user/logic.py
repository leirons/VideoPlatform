from core.auth import AuthHandler

from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import UnmappedInstanceError

from core import config
from loguru import logger

from . import models
from . import schemes


logger.add(config.LOG_FILE, format=config.format, level=config.level, rotation=config.rotation,
           compression=config.compression)

class UserLogic:
    def __init__(self):
        self.auth_handler = AuthHandler()

    def check_none(self):
        pass

    def get_user_by_id(self, db: Session, user_id: int):
        return db.query(models.User).filter(models.User.id == user_id).first()

    def get_user_by_email(self, db: Session, email: str):
        return db.query(models.User).filter(models.User.email == email).first()

    def get_user_by_login(self, db: Session, login: str):
        return db.query(models.User).filter(models.User.login == login).first()

    def get_users(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.User).offset(skip).limit(limit).all()

    def delete_user(self, db: Session, user_id: int):
        record = db.query(models.User).filter(models.User.id == user_id).first()
        try:
            db.delete(record)
            db.commit()
        except UnmappedInstanceError as exc:
            logger.info(f"Не удалось удалить пользователя {user_id}",exc)
            return {'status_code': 404,'detail':"Не удалось удалить пользователя"}
        return {'status_code':200,"detail":"Пользователь удален"}

    def create_user(self, password: str, register_date, db: Session, user: schemes.UserCreate):
        try:
            hashed_password = self.auth_handler.get_passwords_hash(password)
            db_user = models.User(email=user.email, hash_password=hashed_password, login=user.login,
                                  register_date=register_date)
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
        except Exception as exc:
            logger.info("Не удалось создать пользователя",exc)
            return {'status_code':500,"detail":"Не удалось создать пользователя"}
        return {"status_code": 201, "user": db_user}

    def get_all_users(self, db: Session):
        db_user = db.query(models.User).all()
        return db_user

    def check_login_email(self, login: str, email: str, db: Session):
        if self.get_user_by_login(db, login) and self.get_user_by_email(db, email):
            return {"status_code": 403, "detail": 'User with the same login and email exists'}

    def patch_user(self, db: Session, user: schemes.UserPatch, user_id: int):
        try:
            db_user = db.query(models.User).filter(models.User.id == user_id).first()
            res = self.check_login_email(login=user.login, email=user.email, db=db)
            if res.get("status_code") == 403:
                return res
            if user.login is not None:
                db_user.login = user.login
            if user.email is not None:
                db_user.email = user.email
            if user.password is not None:
                hashed_password = self.auth_handler.get_passwords_hash(user.password)
                db_user.hash_password = hashed_password
            db.commit()
            db.refresh(db_user)
        except Exception as exc:
            logger.info("Не удалось сделать patch пользователя",exc)
            return {'status_code': 500,"detail":"Не удалось сделать patch пользователя"}
        return {'status_code':200,"detail":"Операция произведена успешно"}


    def put_user(self, db: Session, user: schemes.UserCreate, user_id: int):
        try:
            hashed_password = self.auth_handler.get_passwords_hash(user.password)
            db_user = db.query(models.User).filter(models.User.id == user_id).first()
            db_user.login = user.login
            db_user.hash_password = hashed_password
            db_user.email = user.email
            db.commit()
            db.refresh(db_user)
        except AttributeError as exc:
            logger.info("Не удалось сделать put пользователя",exc)
            return {'status_code': 500, "detail": "Не удалось сделать put пользователя"}
        return {'status_code': 200, "detail": "Операция произведена успешно"}
