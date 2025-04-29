from datetime import datetime
from app.core.database import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    """用户数据模型
    
    Attributes:
        id: 主键ID
        username: 用户名（唯一）
        password_hash: 加密后的密码
        email: 邮箱地址（唯一）
        created_at: 创建时间
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        """密码加密存储"""
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """密码验证"""
        return check_password_hash(self.password_hash, password)

class Role(db.Model):
    """用户角色模型"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(255))