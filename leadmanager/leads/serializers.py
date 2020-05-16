#Serializer to serialize QuerySets to JSON objects
from rest_framework import serializers
from leads.model import Lead

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'