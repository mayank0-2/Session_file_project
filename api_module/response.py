from django.http import JsonResponse


class ResponseFormat() :

    def plusResponse(self, error_code, message, data) :
        result = {
            'error_code' : error_code, 
            'message' : message, 
            'data' : data
        }
        return JsonResponse(result)
