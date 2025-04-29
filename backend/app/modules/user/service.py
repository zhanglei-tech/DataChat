from models import User, Role
from app.core.database import db
from werkzeug.security import generate_password_hash
from typing import Optional

class UserService:
    """用户服务类
    
    封装用户相关业务逻辑，包括：
    - 用户注册
    - 密码验证
    - 权限管理
    """

    @classmethod
    def create_user(cls, username: str, password: str, email: Optional[str] = None) -> User:
        """创建新用户
        
        Args:
            username: 用户名
            password: 明文密码
            email: 邮箱地址
        
        Returns:
            新用户对象
        """
        if User.query.filter_by(username=username).first():
            raise ValueError('用户名已存在')
        
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @classmethod
    def authenticate(cls, username: str, password: str) -> Optional[User]:
        """用户认证
        
        Args:
            username: 用户名
            password: 明文密码
        
        Returns:
            认证成功返回用户对象，否则返回None
        """
        user = User.query.filter_by(username=username).first()
        if user and user.verify_password(password):
            return user
        return None

    @classmethod
    def assign_role(cls, user_id: int, role_name: str):
        """分配用户角色
        
        Args:
            user_id: 用户ID
            role_name: 角色名称
        """
        user = User.query.get(user_id)
        role = Role.query.filter_by(name=role_name).first()
        
        if not user or not role:
            raise ValueError('用户或角色不存在')
        
        user.roles.append(role)
        db.session.commit()