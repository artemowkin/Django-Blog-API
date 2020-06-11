from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account import app_settings
from rest_framework import serializers


class SignupSerializer(RegisterSerializer):
    password2 = serializers.CharField(
        write_only=True,
        required=app_settings.SIGNUP_PASSWORD_ENTER_TWICE,
    )

    def validate(self, data):
        if not app_settings.SIGNUP_PASSWORD_ENTER_TWICE:
            return data

        return super().validate(data)
