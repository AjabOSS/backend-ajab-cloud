from myuser.models import EmailConfirmationToken
from django.core.mail import send_mail
from django.conf import settings


def send_verification_email(user):
    evt_obj_to_delete = EmailConfirmationToken.objects.filter(user=user)
    if not len(evt_obj_to_delete) == 0:
        for i in evt_obj_to_delete:
            i.delete()
    evt_obj = EmailConfirmationToken.objects.create(user=user)
    if settings.DEBUG:
        print(f"-- email confirmation code for {user.email} : {evt_obj.code}")
    msg = f"""
    کد تایید شما برای تایید ایمیل در عجب کلود :
    
    
    
    
    {evt_obj.code}
    
    
    
    لطفا این کد را در اختیار هیچ کس قرار ندهید.
    اگر نمیدانید برای چه این کد را دریافت کردید 
    این پیام را نادیده بگیرید
    """
    send_mail(
        "کد تایید عجب کلود",
        msg,
        settings.EMAIL_HOST_USER,
        [user.email,],
        fail_silently=False,
        )

