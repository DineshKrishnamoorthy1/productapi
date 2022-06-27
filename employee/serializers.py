from rest_framework import serializers
from employee.models import employees

class employeeSerializer(serializers.ModelSerializer):

    class Meta:
        model=employees
        fields=('fistname','lastname')
        fields ='__all__'
