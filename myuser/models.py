from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

from django.db.models.signals import post_save
from django.dispatch import receiver

from uuid import uuid4
from .utils import create_new_ref_number
from random import randint


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError("You have to import Username")
        if not email:
            raise ValueError("You have to import Email")

        user = self.model(
            username = username,
            email = email,
            is_active = True,
            
        )
        user.set_password(make_password(password))
        user.save(using=self._db)
        return user




    def create_superuser(self,  username, email, first_name="", last_name="", password=None):
        user = self.create_user(
            username = username,
            email = email,
            # first_name = first_name,
            # last_name = last_name,
        )
        
        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.is_online = True
        user.is_verifyed  = True
        user.is_email_verified = True
        user.is_onboarded = True
        
        user.set_password(password)
        user.save(using=self._db)
        return user





class MyUser(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, blank=False)



    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)
    is_verified  = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    is_onboarded = models.BooleanField(default=False)
    is_male = models.BooleanField(default=False) # Just for fun
    
    
    ip = models.CharField(max_length=50, blank=True)
    # ip = models.GenericIPAddressField(protocol="both", unpack_ipv4=False)
    profile_image = models.FileField(upload_to=f"images/users/", blank=True, default="media/static/default_profile_image.png")
    bio = models.TextField(blank=True)
    college = models.CharField(max_length=100, blank=True)
    college_entry = models.DateTimeField(auto_now=False, blank=True, null=True)
    rank = models.PositiveIntegerField(default=1)
    saved_branchs = models.ManyToManyField("branch.Branch", related_name="saved_branch", blank=True)
    viewed_branches = models.ManyToManyField("branch.Branch", related_name="viewed_branches", blank=True)
    created_branches = models.ManyToManyField("branch.Branch", related_name="created_branches", blank=True)
    
    
    
    # security_question #TODO dlkcvnmsdljvn
    # links #TODO should add links model for foreign key
    # custom_role #TODO should add custom_role model for foreign key
    # badges #TODO should add badges model for foreign keyw    
    # major = models.CharField(max_length=50) #TODO: should add major model for foreign key
    
    
    
    
    
    

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True


    def __str__(self):
        return f"{self.username} , id:{self.id}"
    
    
    
class EmailConfirmationToken(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    # code = models.IntegerField(default=randint(100000, 999999))
    code = models.CharField(max_length=6, default=create_new_ref_number())
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id) + " " + str(self.code) + " " + str(self.user) 

    

# @receiver(post_save, sender=MyUser)
# def print_only_after_deal_created(sender, instance, created, **kwargs):
#     if created:
        # EmailConfirmationToken.objects.create(user=instance)
        # print(f'New deal with pk: {instance.pk} was created.')