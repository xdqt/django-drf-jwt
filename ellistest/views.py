from rest_framework import status
from rest_framework.response import Response
from datetime import datetime
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_jwt.settings import api_settings
from rest_framework.viewsets import GenericViewSet

from ellistest.models import User

from .serializers import TokenSerializer

jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER

class JSONWebTokenAPIView(ObtainJSONWebToken):
    """
    Base API View that various JWT interactions inherit from.
    """

    serializer_class = TokenSerializer

    def post(self, request, *args, **kwargs):
        # serializer = self.get_serializer(data=request.data)
        serializer = self.get_serializer(
            data=request.data, extra_payload={"id":1,"age":100})
        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token, user, request)
            response = Response(response_data)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.utcnow() +
                              api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                    token,
                                    expires=expiration,
                                    httponly=True)
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    



class ProtectedView(GenericViewSet):
    queryset = User.objects.all()
    def list(self,request):
        payload = jwt_decode_handler(request.auth)
        payload['haha'] = 'haha'
        
        return Response(data=payload,status=status.HTTP_200_OK)
    
    