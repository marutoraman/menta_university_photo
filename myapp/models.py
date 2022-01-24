from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db.models.fields import BLANK_CHOICE_DASH
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail
import ulid

from mysite.const import USER_TYPE

# class PermissionType(models.IntegerChoices):
#     STUDENT = (0,'生徒')
#     MANAGER = (1,'大学職員')


class CustomUserManager(UserManager):
    '''
    Userを作成するための処理
    Userの項目が変更になっているので、こちらも変更の必要がある
    '''    
    
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_user(self, email=None, password=None,user_type=None, **extra_fields):
        '''
        一般ユーザーを作成する処理
        '''
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password,user_type,**extra_fields)
    
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        '''
        管理者ユーザーを作成する処理
        '''
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
    
class StudentUser(models.Model):
    id = models.CharField(max_length=32, default=ulid.new, primary_key=True, editable=False)
    # username = models.CharField(max_length=150,unique=True)
    # permission_type = models.IntegerField(choices=PermissionType.choices,default=PermissionType.STUDENT)
    nickname = models.CharField(_('ニックネーム'), max_length=32, blank=True)
    university_name = models.ForeignKey('University',on_delete=models.CASCADE,null=True,blank=True)
    major_name = models.ForeignKey('Major',on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.nickname
    
    class Meta:
        verbose_name = "学生ユーザー"
        verbose_name_plural = "学生ユーザー"
        db_table = "student_user"
        
class EditUser(models.Model):
    id = models.CharField(max_length=32, default=ulid.new, primary_key=True, editable=False) 
    nickname = models.CharField(_('ニックネーム'), max_length=32, blank=True)
    # username = models.CharField(max_length=150,unique=True)
    university_name = models.ForeignKey('University',on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.nickname
    
    class Meta:
        verbose_name = "editユーザー"
        verbose_name_plural = "editユーザー"
        db_table = "edit_user"
        
class User(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(max_length=32, default=ulid.new, primary_key=True, editable=False)
    email = models.EmailField(_('メールアドレス'), blank=False, unique=True, db_index=True) 
    username = models.CharField(_('ユーザーネーム'), max_length=150, blank=True)
    user_type = models.IntegerField(_('ユーザータイプ'), blank=False,default=0)
    student_user = models.ForeignKey(StudentUser,db_column="student_user_id",blank=True, db_index=True, default=None, null=True, on_delete=models.SET_NULL)
    edit_user = models.ForeignKey(EditUser,db_column="edit_user_id", blank=True, db_index=True, default=None, null=True, on_delete=models.SET_NULL)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    
    objects = CustomUserManager()
    # emailの項目名を指定
    EMAIL_FIELD = 'email'
    # ログイン時にIDになる項目名を指定
    USERNAME_FIELD = 'email'
    # 必須入力とする項目名(USERNAME_FIELDに指定した項目は必ず指定する前提のため指定しない)
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = _('ログイン用共通ユーザー')
        verbose_name_plural = _('ログイン用共通ユーザー')
        db_table = "auth_user"
        
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
        
    def is_student_user(self):
        return self.user_type == USER_TYPE.STUDENT_USER
    
    def is_edit_user(self):
        return self.user_type == USER_TYPE.EDIT_USER


class University(models.Model):
    university_name = models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return self.university_name

class Major(models.Model):
    major_name = models.CharField(max_length=30)
    r_university = models.ForeignKey('University', on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.major_name