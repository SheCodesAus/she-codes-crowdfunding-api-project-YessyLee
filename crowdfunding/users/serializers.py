from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()

    def create(self, validated_data):
      	return CustomUser.objects.create(**validated_data) #validated by serializer??
# 
# class CustomUserSerializer(serializers.ModelSerializer):
# 
    # class Meta:
        # model = CustomUser
        # fields = ['email', 'username', 'password']
        # extra_kwargs = {'password': {'write_only': True}}
    # 
    # def create(self, validated_data):
        # user = CustomUser(
            # email=validated_data['email'],
            # username=validated_data['username']
        # )
        # user.set_password(validated_data['password'])
        # user.save()
        # return user
# 