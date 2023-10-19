from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from myuser.models import MyUser

    
class UserRegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = MyUser
        fields = (
            'email',
            'name',
            'username',
            'password',
            'password_confirm',
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
        del validated_data['password_confirm']
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
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError('password mismatch')
        return data