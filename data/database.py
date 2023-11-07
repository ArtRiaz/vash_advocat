from aiogram import types, Bot
from gino import Gino
import sqlalchemy as sa
from sqlalchemy import (Column, Integer, BigInteger, String,
                        Sequence, TIMESTAMP, Boolean, JSON)
from sqlalchemy import sql
from create_bot import load_config, POSTGRES_URL
from typing import List
import gino

db = Gino()

config = load_config()


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    user_id = Column(BigInteger)
    full_name = Column(String(100))
    username = Column(String(50))
    query: sql.Select

    def __repr__(self):
        return "<User(id='{}', fullname='{}', username='{}')>".format(
            self.id, self.full_name, self.username)


class RegisterUser(db.Model):
    __tablename__ = 'register'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    user_id = Column(BigInteger)
    name = Column(String(100))
    phone = Column(String(100))
    email = Column(String(100))
    coment = Column(String(500))
    register_time = Column(TIMESTAMP)
    query: sql.Select


class DBCommands:

    async def get_user(self, user_id):
        user = await User.query.where(User.user_id == user_id).gino.first()
        return user

    async def add_new_user(self):
        user = types.User.get_current()
        old_user = await self.get_user(user.id)
        if old_user:
            return old_user
        new_user = User()
        new_user.user_id = user.id
        new_user.username = user.username
        new_user.full_name = user.full_name
        await new_user.create()
        return new_user

    async def show_users(self):
        await db.set_bind(POSTGRES_URL)
        users = await User.query.gino.all()

        return users

    async def show_registr_users(self):
        await db.set_bind(POSTGRES_URL)
        users = await RegisterUser.query.gino.all()

        return users

    async def get_all_user_ids(self):
        users = await User.query.gino.all()  # Получаем всех пользователей из таблицы
        user_ids = [user.user_id for user in users]
        return user_ids

    async def empty_cart(self):
        register = await RegisterUser.delete.gino.status()

        return register


async def create_db():
    await db.set_bind(POSTGRES_URL)
    await db.gino.create_all()
