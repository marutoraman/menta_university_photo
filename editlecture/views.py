from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .models import MenuMaster,RegisterMenu,Coma
from .models import University

# Create your views here.
User = get_user_model()


class CreateComa(CreateView):
    pass
    # template_name = 'create_coma.html'
    # model = Coma
    # fields = ['name','start_time','finish_time']
    
    # def form_valid(self, form):
    #     university = University.objects.filter(university_name=self.request.user.university_name).first()
    #     form.instance.r_university = self.request.user.
    #     return super().form_valid(form)
    
    

class ShowClass(TemplateView):
    template_name = 'show_class.html'
    
    def get(self, request, **kwargs):
        user = User.objects.get(id=request.user.id)
        menu = RegisterMenu.objects.filter(user_id=user.id).all().values_list('menu',flat=True)
        menus = list(menu)
        menu_list = []
        for m in menus:
            get_menumaster = MenuMaster.objects.get(id=int(m))
            menu_list.append(get_menumaster)
        context = {
            'weekdays':['Mon','Tue','Wed','Thu','Fry','Sat','Sun'],
            'period':['1','2','3','4','5','6'],
            'menu_list':menu_list
        }
        return self.render_to_response(context)
