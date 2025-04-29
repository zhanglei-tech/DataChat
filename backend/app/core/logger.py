import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

# 初始化日志配置

def configure_logger(app):
    """
    日志配置函数
    
    参数:
        app: Flask应用实例
    """
    logger = app.logger
    logger.setLevel(logging.INFO)

    # 创建日志目录
    log_dir = Path(__file__).parent.parent / 'logs'
    log_dir.mkdir(exist_ok=True)

    # 日志格式
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # 文件处理器（自动轮换）
    file_handler = RotatingFileHandler(
        filename=log_dir / 'app.log',
        maxBytes=1024*1024,
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)

    # 控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # 添加处理器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # 返回应用实例的logger
    return logger