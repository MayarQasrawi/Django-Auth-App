from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Profile
from django.contrib.auth import authenticate

# get_user_model() Returns the current active User model,
#  which could be a custom one.
User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("email", "username", "password", "password_confirm")

    def validate(self, attrs):
        if attrs["password"] != attrs["password_confirm"]:
            raise serializers.ValidationError("Passwords don't match")
        return attrs

    def create(self, validated_data):
        validated_data.pop("password_confirm")
        
        user = User.objects.create_user(**validated_data) 
        '''
        1. create_user() automatically hashes the password before saving it to the database.
        2. create_user() can set default fields properly (like is_staff=False, is_superuser=False for a regular user).
        
        note: For creating a superuser, Django provides create_superuser().
        '''
       
        Profile.objects.create(user=user)  # Create profile automatically
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "username", "date_joined")
        read_only_fields = ("id", "date_joined")


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("bio", "phone", "avatar")


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        user = authenticate(request=self.context.get("request"), email=email, password=password)

        if not user:
            raise serializers.ValidationError(_("Invalid email or password"))

        data = super().validate({"username": user.email, "password": password})
        return data


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs

    def save(self, **kwargs):
        from rest_framework_simplejwt.tokens import RefreshToken, TokenError

        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail("bad_token")


