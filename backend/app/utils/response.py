from flask import jsonify
from typing import Union, Dict


def json_response(code: int = 200, message: str = 'success', data: Union[Dict, list] = None):
    """统一API响应格式
    
    Args:
        code: HTTP状态码
        message: 返回消息
        data: 业务数据
    
    Returns:
        Flask响应对象
    """
    response = {
        'code': code,
        'message': message,
        'data': data or {}
    }
    return jsonify(response), code