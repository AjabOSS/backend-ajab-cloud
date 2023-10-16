from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from myuser.models import MyUser

    
class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = MyUser
        fields = (
            'email',
            'first_name',
            'username',
            'password',
            'password2',
            )
        
        extra_kwargs = {
            "password":{'write_only':True},
        }
        
        validators = [
            UniqueTogetherValidator(
                queryset=MyUser.objects.all(),
                fields=['email']
            )
        ]
        
    def create(self, validated_data):
        del validated_data['password2']
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
        if data['password'] != data['password2']:
            raise serializers.ValidationError('password mismatch')
        return data