from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings
from .models import *
from .forms.student_user import StudentUserForm
from mysite.const import USER_TYPE


class AccountAdapter(DefaultAccountAdapter):
    '''
    Userアカウントに紐づける処理を定義できるクラス
    '''

    def save_user(self, request, user, form, commit=True):
        '''
        ユーザー登録時に実行される
        ユーザー登録時にstudentユーザーとeditユーザーで異なる処理を実装する
        '''
        # 継承元の処理を行い、ユーザーを作成
        super(AccountAdapter, self).save_user(request, user, form, commit=False)
        user.user_type = int(request.POST.get("user_type", 0))
        print(user.user_type)
        
        # 一般ユーザー個別処理
        if user.user_type == USER_TYPE.STUDENT_USER:
            # studentユーザー用テーブルを作成
            user_attribute = StudentUser()
            user_attribute.save()
            user.student_user = user_attribute
        # editユーザー個別処理
        else:
            user_attribute = EditUser()
            user_attribute.save()
            user.edit_user = user_attribute
        
        user.save()
        
        
    def get_login_redirect_url(self, request):
        '''
        ログイン後のリダイレクト先をUserTypeで振り分ける
        '''
        # user_type=1の場合はeditユーザー用、それ以外はstudentユーザー用のリダイレクトURLを返す
        if request.user.user_type == USER_TYPE.EDIT_USER:
            return settings.LOGIN_REDIRECT_URL_COMPANY
        else:
            return super().get_login_redirect_url(request)