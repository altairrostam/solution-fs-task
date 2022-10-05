from rest_framework import serializers
from django.contrib.humanize.templatetags import humanize
from .models import Email

class GetEmailSerializer(serializers.ModelSerializer):
    timestamp = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:
        model=Email
        fields=('id','emailId','timestamp','status')
    def get_timestamp(self, obj):
        return humanize.naturaltime(obj.timestamp)
    def get_status(self,obj):
        return obj.get_status_display()

class PatchEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Email
        fields=['id','emailId','status']