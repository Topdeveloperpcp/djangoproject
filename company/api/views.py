from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from company.models import Company
from .serializers import CompanySerializer

@permission_classes((permissions.AllowAny,))
class CompanyListView(APIView):
    def get(self, request):
        queryset = Company.objects.all()
        serializer_class = CompanySerializer(queryset, many=True)
        return Response({"company": serializer_class.data})

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            company_saved = serializer.save()
        return Response({"success": "Company '{}' created successfully".format(company_saved.Name)})

    def put(self, request, pk):
        saved_company = get_object_or_404(Company.objects.all(), pk=pk) 
        serializer = CompanySerializer(instance=saved_company, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            company_saved = serializer.save()
        return Response({"success": "Company '{}' updated successfully".format(company_saved.Name)})

    def delete(self, request, pk):
        company = get_object_or_404(Company.objects.all(), pk=pk)
        company.delete()
        return Response({"message": "Company with id `{}` has been deleted.".format(pk)},status=204)



class CompanyDetailView(RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
