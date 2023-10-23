from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from rest_framework import serializers

from django.contrib.auth.hashers import make_password    
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _    
    
from myuser.models import MyUser


class EditUserProfileSerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True, required=False)
    bio = serializers.CharField(write_only=True, required=False)
    college = serializers.CharField(write_only=True, required=False)
    profile_image = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = MyUser
        fields = (
            "name",
            "bio",
            "college",
            "profile_image",
            # "college_entry",
        )
        
        
class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = MyUser
        fields = (
            'email',
            'name',
            'username',
            'password',
            'confirm_password',
            )
        
        extra_kwargs = {
            "password":{'write_only':True},
        }
        
        validators = [
            UniqueTogetherValidator(
                queryset=MyUser.objects.all(),
                fields=['email', 'name']
            )
        ]
        
    def create(self, validated_data):
        del validated_data['confirm_password']
        validated_data['password'] = make_password(validated_data['password'])
        validated_data['is_active'] = True
        return MyUser.objects.create(**validated_data)


    def validate_email(self, email):
        return email
        
        
    def validate_username(self, username):
        if username == 'admin':
            raise serializers.ValidationError('Username can not be admin')
        elif len(username)< 4:
            raise serializers.ValidationError('Username must at least 4 charecter')
        return username
    
    
    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('password mismatch')
        return data
    
    
    

    

class CustomAuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
    
    
    