def build_response_dict(success, action, message, reason=None):
    response_dict = {}
    if success:
        response_dict['data'] = { action: 'success', 'message': message}
        if reason is not None:
            response_dict['data']['reason'] = reason
    elif not success:
        response_dict['error'] = { action: 'failed', 'message': message}
        if reason is not None:
            response_dict['error']['reason'] = reason
    return response_dict