import datetime
import time

import pandas as pd
from sqlalchemy import text
from sqlalchemy.orm import Session

from . import models, schemas
from .database import execute_query


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.User)
        .order_by(models.User.id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(
        email=user.email, hashed_password=fake_hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Item)
        .order_by(models.Item.id)
        .offset(skip)
        .limit(limit)
        .all()
    )


query = """
SELECT * 
FROM [testdb].[dbo].[Sales] WITH (NOLOCK)
where Order_Priority = 'H' and sales_channel = 'Online' and Region = 'Europe'
    """


def get_sales(db: Session):
    results = db.execute(text(query))
    before_time = time.time()
    records = results.fetchall()
    df = pd.DataFrame(records)
    after_time = time.time()
    print(
        f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}: {len(df)} fetched in {(after_time - before_time) * 1000} ms")
    return len(df)


def get_sales2():
    before_time = time.time()
    results = execute_query(query)
    after_time = time.time()
    print(
        f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}: {len(results)} fetched in {(after_time - before_time) * 1000} ms")
    return len(results)
