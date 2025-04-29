import os
from pathlib import Path

class Config:
    """基础配置类
    
    Attributes:
        SQLALCHEMY_DATABASE_URI: 数据库连接字符串
        SQLALCHEMY_TRACK_MODIFICATIONS: 是否跟踪对象修改
        SECRET_KEY: 应用密钥
    """
    BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
    
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{BASE_DIR}/db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # 安全配置
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key')

class DevelopmentConfig(Config):
    """开发环境配置"""
    DEBUG = True

class ProductionConfig(Config):
    """生产环境配置"""
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SECRET_KEY = os.getenv('SECRET_KEY')