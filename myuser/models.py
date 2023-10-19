from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractUser




class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError("You have to import Username")
        if not email:
            raise ValueError("You have to import Email")

        user = self.model(
            username = username,
            email = email,
        )
        user.set_password(password)
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
        user.is_email_verifyed = True
        user.is_onboarded = True
        
        user.set_password(password)
        user.save(using=self._db)
        return user





class MyUser(AbstractBaseUser, PermissionsMixin):
    
    # username = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=50, blank=False)



    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)
    is_verifyed  = models.BooleanField(default=False)
    is_email_verifyed = models.BooleanField(default=False)
    is_onboarded = models.BooleanField(default=False)
    is_male = models.BooleanField(default=False) # Just for fun
    
    
    ip = models.CharField(max_length=50, blank=True)
    # ip = models.GenericIPAddressField(protocol="both", unpack_ipv4=False)
    profile_image = models.FileField(upload_to=None, max_length=100, blank=True)
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
        return self.username