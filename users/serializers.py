from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    username = serializers.CharField(read_only=True)
    password = serializers.CharField(write_only=True, required=False)
    old_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ["url", "id", "username", "email", "first_name", "last_name", "password", "old_password"]
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

    def update(self, instance, validated_data):
        try:
            user = instance
            password = validated_data.pop('password', None)
            old_password = validated_data.pop('old_password', None)
            if password is not None and old_password is not None:
                if user.check_password(old_password):
                    user.set_password(password)
                else:
                    raise Exception("Old password is incorrect")
                user.save()
        except Exception as err:
            raise serializers.ValidationError({ 'info': err })
        return super(UserSerializer, self).update(instance, validated_data)
