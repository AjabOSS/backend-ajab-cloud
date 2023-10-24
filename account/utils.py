from myuser.models import EmailConfirmationToken
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template
import uuid

def send_verification_email(user):
        
    EmailConfirmationToken.objects.filter(user=user).delete()
    evt_obj = EmailConfirmationToken.objects.create(user=user)    
    evt_obj.code = str(uuid.uuid4().hex[:6].upper())

    evt_obj.save()
    if settings.DEBUG:
        print(f"-- email confirmation code for {user.email} : {evt_obj.code}")
    else:
        data = {'t_code': str(evt_obj.code)}
        message = get_template('confimation_email.txt').render(data)
        send_mail(
            subject="کد تایید عجب کلود",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email,],
            fail_silently=False,
            )
        