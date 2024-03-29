from rest_framework.views import APIView
import uuid 
from datetime import datetime, timedelta
from config import Config
from django.http import JsonResponse
from api_module.response import ResponseFormat

session = {}
response = ResponseFormat()

class create_session(APIView):
    def post(self, request):
        defaultSessionTime = int(Config().DEFALUT_SESSION_TIME)
        session_id = str(uuid.uuid4())
        session[session_id] = {
            'files' : [],
            'total_sum' : 0,
            'session_expiry_time' : datetime.now() + timedelta(defaultSessionTime)
        }
        return response.plusResponse(200, "session_created", {"session_id" : session_id})





class delete_session(APIView):
    def post(self, request):
        session_id = request.data.get('session_id')
        if session_id in session:
            del session[session_id]
            return response.plusResponse(200, "session_deleted", {})
        return response.plusResponse(404, "Session_not_found", {})






class verify_and_update_session_data() :
    def is_session_valid(self, session_id) :
        print(session_id)
        if session_id not in session:
            return False
        if session[session_id]['session_expiry_time'] < datetime.now():
            del session[session_id]
            return False
        return True
    
    
    def remove_oldest_file(self, session_id) :
        os.remove(session[session_id]['files'].pop(0)['relative_path'])



    def add_new_file(self, session_id, file, result = 0) :
        session[session_id]['files'].append(file)
        session[session_id]['total_sum'] += result

    def check_if_file_exists(self, session_id, file_name):
        print('sessions' , session)
        print('file_nme', file_name)
        for row in session[session_id]['files']:
            print(row)
            if row['file_name'] == file_name:
                return JsonResponse({'error': 'File already exists in the session'}, status=400)