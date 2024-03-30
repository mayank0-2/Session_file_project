from functools import wraps
from api_module.response import ResponseFormat

response = ResponseFormat()
def isValidRequest(f) :
    @wraps(f)
    def validate(*args, **kwargs) :
        if request.path == "v1/delete-session" and request.data.get('session_id') in (None, "") :
            return response.plusResponse(400, "Session_id_not_found", {})


        return f(*args, **kwargs)
    return validate