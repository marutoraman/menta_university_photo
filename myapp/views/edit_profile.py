from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from ..forms.edit_user import EditUserForm
from mysite.const import USER_TYPE

app_name = "myapp"

@method_decorator(login_required, name="dispatch")
class EditProfileView(TemplateView):
    template_name = f"{app_name}/edit_profile.html"
    
    def get(self, request):
        if not request.user.user_type == USER_TYPE.EDIT_USER:
            return Http404("生徒アカウントは、このページは表示できません")
        form = EditUserForm(instance=request.user.edit_user)
        return self.render_to_response({"form": form})
    
    
    def post(self, request):
        if not request.user.user_type == USER_TYPE.EDIT_USER:
            return Http404("生徒アカウントは、このページは表示できません")
        form = EditUserForm(request.POST, instance=request.user.edit_user)
        if not form.is_valid():
            messages.error(request, "保存に失敗しました")
            for field in form:
                for error in field.errors:
                    messages.error(request, f"{field.label}: {error}")
        else:
            form.save()
            messages.success(request, "保存しました")
            
        return self.render_to_response({"form": form})