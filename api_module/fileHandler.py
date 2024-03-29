from rest_framework.views import APIView
from api_module.sessionHandler import verify_and_update_session_data
from django.core.files.storage import default_storage
from api_module.response import ResponseFormat

response = ResponseFormat()

class file_handler(APIView) :
    def post(self, request, session_id):
        if not verify_and_update_session_data().is_session_valid(session_id):
            return response.plusResponse(404, "Session_not_found", {})
        for i in range(1, 16) :
            file = request.FILES.get(f'file{i}')
            if file is None :
                break
            print(file, "---------------->file")
            if not file :
                return response.plusResponse(400, "File_not_found", {})
            print(file.name, "---->")

            name_path = f"uploads/{file.name}_session_{session_id}"

            verify_and_update_session_data().check_if_file_exists(session_id, name_path)


            file_path = default_storage.save(name_path, file)
            result = self.calculate_file_content(file_path)
            file_data = {
                "file_name" : file.name,
                "relative_path" : file_path,
            }
            verify_and_update_session_data.add_new_file(session_id, session_id, file_data, result)
        return response.plusResponse(200, "File_uploaded", {"result" : result})


    
    def calculate_file_content(self, file_path) :
        with open(file_path, 'r') as f :
            equation = f.read()
            return eval(equation)