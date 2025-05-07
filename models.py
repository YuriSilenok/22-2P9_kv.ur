"""Модель базы данных"""
from peewee import Model, IntegerField, SqliteDatabase


db = SqliteDatabase("base.db")


class Table(Model):
    """Класс BaseModel для хранения данных"""

    class Meta:
        """Класс Meta с настройками модели"""
        database = db


class Kvur(Table):
    """Класс kvur"""

    a = IntegerField()
    b = IntegerField()
    c = IntegerField()
    result = IntegerField()


if __name__ == "__main__":
    db.create_tables([Kvur])
