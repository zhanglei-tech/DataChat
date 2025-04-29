import jwt
from datetime import datetime, timedelta
from flask import request, jsonify
from functools import wraps
from app.core.config import Config


def generate_token(user_id):
    """生成JWT访问令牌
    
    Args:
        user_id: 用户ID
    Returns:
        JWT令牌字符串
    """
    payload = {
        'exp': datetime.utcnow() + timedelta(hours=2),
        'iat': datetime.utcnow(),
        'sub': user_id
    }
    return jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')


def decode_token(token):
    """解析验证JWT令牌
    
    Args:
        token: JWT令牌字符串
    Returns:
        用户ID或错误信息
    """
    try:
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return '令牌已过期'
    except jwt.InvalidTokenError:
        return '无效令牌'


def jwt_required(f):  # 无参数装饰器标准实现
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token or not token.startswith('Bearer '):
            return jsonify({'code': 401, 'message': '缺少访问令牌'}), 401
        
        token = token.split(' ')[1]
        user_id = decode_token(token)
        if isinstance(user_id, str):
            return jsonify({'code': 401, 'message': user_id}), 401
        
        return f(*args, **kwargs)
    return decorated_function