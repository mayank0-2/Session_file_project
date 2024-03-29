from rest_framework.views import APIView
from api_module.sessionHandler import verify_and_update_session_data
from django.core.files.storage import default_storage

class file_handler(APIView) :
    def post(self, request, session_id):
        if not verify_and_update_session_data.is_session_valid(session_id):
            return response.plusResponse(404, "Session_not_found", {})
        file = request.FILES.get('file')
        if not file :
            return response.plusResponse(400, "File_not_found", {})
        
        file_path = default_storage.save(f"uploads/{file.name}", file)
        result = self.calculate_file_content(file_path)
        file_data = {
            "file_name" : file.name,
            "relative_path" : file_path,
        }
        verify_and_update_session_data.add_new_file(session_id, file_data, result)



    
    def calculate_file_content(file_path) :
        with open(file_path, 'r') as f :
            equation = f.read()
            return eval(equation)