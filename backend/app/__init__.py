from flask import Flask
from flask_migrate import Migrate
from app.core.config import Config
from app.core.database import db


def create_app(config_class=Config):
    """Flask应用工厂函数
    
    Args:
        config_class: 配置类
    Returns:
        Flask应用实例
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # 初始化数据库
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app, db)

    # 配置日志
    from .core.logger import configure_logger
    configure_logger(app)

    # 注册蓝图
    # 延迟导入蓝图避免循环依赖
    from app.modules.user.routes import user_bp
    app.register_blueprint(user_bp, url_prefix='/api/users')

    return app