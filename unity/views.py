from django.shortcuts import render
from .models import Email
from .serializers import GetEmailSerializer
from datetime import datetime
import calendar

# Create your views here.
def Dashboard(request):

    queryset = Email.objects.all()
    queryset = queryset.order_by('-timestamp')
    serializer = GetEmailSerializer(queryset,many=True)
    emailData = serializer.data
    emailCount = queryset.count()
    
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    emailThisMonthObjects = Email.objects.filter(timestamp__month=currentMonth).count()

    unsubscribedEmail =Email.objects.filter(status=0).count()
    # month = datetime.date(1900, currentMonth, 1).strftime('%B')
    return render(
                request,
                'dashboard.html',
                context={
                    'title':calendar.month_name[currentMonth] +' '+str(currentYear),
                    'emails': emailData,
                    'emailCount':emailCount,
                    'thisMonth':emailThisMonthObjects,
                    'unsubscribed':unsubscribedEmail
                }
            )
def Store(request):
    return render(request,'store.html')
