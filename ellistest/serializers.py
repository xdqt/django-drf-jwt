from uuid import uuid4

from django.utils.translation import ugettext as _

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from ellistest.models import User

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER


class TokenSerializer(JSONWebTokenSerializer):
    def __init__(self, *args, **kwargs):
        self.extra = kwargs.get('extra_payload')
        if 'extra_payload' in kwargs:
            kwargs.pop('extra_payload')
        super().__init__(*args, **kwargs)
        

    def validate(self, attrs):
        credentials = {
            self.username_field: attrs.get(self.username_field),
            'password': attrs.get('password')
        }

        # 先校验这个用户存在于我们系统与否
        filter_condition = {self.username_field:attrs.get(self.username_field)}
        
            
        user = User.objects.filter(**filter_condition).first()

        payload = jwt_payload_handler(user)
        
        payload['jti'] = uuid4().hex
        payload.update(self.extra)

        return {
            'token': jwt_encode_handler(payload),
            'user': user
        }