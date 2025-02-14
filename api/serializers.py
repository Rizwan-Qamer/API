from rest_framework import serializers
from .models import Company, Employee

#create serializers here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = "__all__"
        

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"        
          