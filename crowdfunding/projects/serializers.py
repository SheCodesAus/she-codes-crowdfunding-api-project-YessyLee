from rest_framework import serializers
from .models import Project, Pledge

class PledgeSerializer(serializers.ModelSerializer):
    class Meta: #define how the model form work
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']
        
class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
<<<<<<< Updated upstream
    owner = serializers.CharField(max_length=200) #removing owner??
=======
    owner = serializers.ReadOnlyField(source="owner_id") #call owner id
>>>>>>> Stashed changes
    
    def create(self, validated_data): #validated data is the dictionary function
        return Project.objects.create(**validated_data) #asterisk is to return the pair key value
    
<<<<<<< Updated upstream
class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
=======
class PledgeSerializer(serializers.ModelSerializer):
    class Meta: #define how the model form work
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']
        read_only_fields = ['id', 'supporter']
>>>>>>> Stashed changes
