from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """SQLAlchemy声明式基类
    提供公共的模型继承基础，支持未来扩展
    """
    pass

# 创建可重用的SQLAlchemy实例
db = SQLAlchemy(model_class=Base)