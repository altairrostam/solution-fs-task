from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import Email
from .serializers import GetEmailSerializer,PatchEmailSerializer


class EmailList(APIView):
    def get(self, request, format=None):
        try:
            queryset = Email.objects.all()
            queryset = queryset.order_by('-timestamp')
            serializer = GetEmailSerializer(queryset,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValueError as err:
            return Response(str(err), status=status.HTTP_400_BAD_REQUEST)
    def post(self,request):
        try:
            email = Email.objects.create(
                emailId =request.data['email']
            )
            email.save()
            return Response(GetEmailSerializer(Email.objects.get(pk=email.pk)).data, status=status.HTTP_201_CREATED)
        except ValueError as err:
            return Response(str(err), status=status.HTTP_400_BAD_REQUEST)

class EmailDetail(APIView):
    def get_object(self, idEmail):
        try:
            return Email.objects.get(idEmail=idEmail)
        except Email.DoesNotExist:
            raise Http404
    def patch(self,request,idEmail,format=None):
        email = self.get_object(request.data['idEmail'])
        serializer = PatchEmailSerializer(email,
            data={
                "status":request.data['status']
            }
        ,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(GetEmailSerializer(Email.objects.get(pk=idEmail)).data, status=status.HTTP_202_ACCEPTED)


