from projects.serializers import PledgeSerializer, ProjectSerializer
from rest_framework import serializers, validators
from .models import CustomUser

# class CustomUserSerializer(serializers.Serializer):
    # id = serializers.ReadOnlyField()
    # username = serializers.CharField(max_length=150)
    # email = serializers.EmailField()
# 
    # def create(self, validated_data):
      	# return CustomUser.objects.create(**validated_data) #validated by serializer??
# 
# class CustomUserSerializer(serializers.ModelSerializer):
# 
    # class Meta:
        # model = CustomUser
        # fields = ('email', 'username', 'password', 'avatar', 'bio')
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
        
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "email", "is_active", "password", "bio", "avatar")

        extra_kwargs = {
            "email": {
                "validators": [validators.UniqueValidator(queryset=CustomUser.objects.all())],
                "allow_blank": False,
                "required": True,
            },
            "password": {"write_only": True},
            "is_active": {"read_only": True},
        }

    def create(self, validated_data):
        user = CustomUser.objects.create(**validated_data)
        user.set_password(validated_data["password"])  # protects password
        user.save()
        return user
    
class CustomUserDetail(CustomUserSerializer):
    # below based on ProjectSerializer approach for owner
    pledges = PledgeSerializer(many=True, source="supporter_pledges", required=False)
    projects = ProjectSerializer(many=True, source="owner_projects", required=False)

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "email",
            "is_active",
            "bio",
            "avatar",
            "pledges",
            "projects",
        )
        read_only_fields = ["id", "pledges", "projects"]

class ChangePasswordSerializer(serializers.Serializer):

    model = CustomUser
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)