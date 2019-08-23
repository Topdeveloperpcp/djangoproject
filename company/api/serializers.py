from rest_framework import serializers
from company.models import Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'Name', 'Address', 'Pan_No', 'Regd_No', 'Telephone', 'Mobile', 'Email', 'Web', 'State', 'Country', 'Created_by','Logo')
    def create(self, validated_data):
        return Company.objects.create(**validated_data)  
    def update(self, instance, validated_data):
        instance.Name       = validated_data.get('Name', instance.Name)
        instance.Address    = validated_data.get('Address', instance.Address)
        instance.Pan_No     = validated_data.get('Pan_No', instance.Pan_No)
        instance.Regd_No    = validated_data.get('Regd_No', instance.Regd_No)
        instance.Telephone  = validated_data.get('Telephone', instance.Telephone)
        instance.Mobile     = validated_data.get('Mobile', instance.Mobile)
        instance.Email      = validated_data.get('Email', instance.Email)
        instance.Web        = validated_data.get('Web', instance.Web)
        instance.State      = validated_data.get('State', instance.State)
        instance.Country    = validated_data.get('Country', instance.Country)
        instance.Created_by = validated_data.get('Created_by', instance.Created_by)
        instance.Logo       = validated_data.get('Logo', instance.Logo)

        instance.save()
        return instance  

