"""Модель базы данных"""
from peewee import Model, IntegerField, SqliteDatabase


db = SqliteDatabase("base.db")


class BaseModel(Model):
    """Класс BaseModel для хранения данных"""

    a = IntegerField()
    b = IntegerField()
    c = IntegerField()
    result = IntegerField()

    class Meta:
        """Класс Meta с настройками модели"""
        database = db
