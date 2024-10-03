from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ["url", "id", "username", "email", "first_name", "last_name", "password"]
        # extra_kwargs = {
        #     'password': {'write_only': True, 'required': False}
        # }

    def create(self, validated_data):
        password = validated_data.pop("password", None)
        user = User.objects.create(**validated_data)
        # user = self.Meta.model(**validated_data)
        if password is not None:
            user.set_password(password)
        user.save()
        return user
