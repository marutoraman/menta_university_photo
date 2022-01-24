from django.urls import path, include
from .views.edit_profile import EditProfileView
from .views.edit_student_profile import EditStudentProfileView, user_university, user_major
from .apis.university import MajorAPIView

app_name = "myapp"
urlpatterns = [
    path("edit_profile", EditProfileView.as_view(), name="edit_profile"),
    path("edit_student_profile", EditStudentProfileView.as_view(), name="edit_student_profile"),
    path('user_university/',user_university,name='user_university'),
    #path('user_major/<int:university_id>',user_major,name='user_major'),
    #path('myapp/user_major/(?P<university_id>[0-9]+)$',user_major,name='user_major'),
    path('api/major', MajorAPIView.as_view(), name='major_api')
]