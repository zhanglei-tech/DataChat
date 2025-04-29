from flask import Blueprint, request
from app.core.database import db
from app.modules.user.models import User
from app.modules.user.schemas import UserSchema
from app.utils.response import json_response
from app.utils.auth import jwt_required, generate_token

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    """用户注册接口
    Request Body:
        username: 用户名
        password: 密码
        email: 邮箱（可选）
    """
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user:
        return json_response(code=400, message='用户已存在')

    new_user = User(username=data['username'], email=data.get('email'))
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return json_response(data=UserSchema().dump(new_user))

@user_bp.route('/login', methods=['POST'])
def login():
    """用户登录接口
    Request Body:
        username: 用户名
        password: 密码
    """
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if not user or not user.verify_password(data['password']):
        return json_response(code=401, message='用户名或密码错误')
    
    # 生成JWT令牌
    access_token = generate_token(user.id)
    return json_response(data={'token': access_token})

@user_bp.route('', methods=['GET'])
@jwt_required  # 正确无括号调用
def get_users():
    """获取用户列表（需鉴权）"""
    users = User.query.all()
    return json_response(data=UserSchema(many=True).dump(users))