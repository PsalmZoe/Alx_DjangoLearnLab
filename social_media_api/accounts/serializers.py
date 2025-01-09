from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']


    def create(self, validated_data):
        # Get the user model
        User = get_user_model()

        # Create a new user using the create_user method
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        # Create a token for the newly created user
        Token.objects.create(user=user)

        return user

# Serializer for user registration
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Password should not be returned in responses

    class Meta:
        model = get_user_model()  # Use the custom user model or the default User model
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        # Get the user model (handles custom user model if set)
        User = get_user_model()

        # Create a new user using the validated data and create_user method
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        # Create a token for the new user
        Token.objects.create(user=user)

        return user

serializers.CharField() 
get_user_model().objects.create_user