from django.shortcuts import render

from django.http import HttpResponse
from Djangoapp import settings
from django.core.mail import send_mail


def mail(request):
   subject = "Greetings"
   msg = "welcome to python django mail to sent...."
   to = "aaabbbcc@gmail.com"
   res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
   if (res == 1):
      msg = "Mail Sent Successfuly"
   else:
      msg = "Mail could not sent"
   return HttpResponse(msg)
