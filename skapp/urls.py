from django.urls import path
from skapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('about',views.about,name="about"),
    path('contact',views.contactus,name="contact"),
    path('work',views.work,name="work"),

    # Admin urls
    path("login",views.login_page, name="login_page"),
    path('logout',views.logout_btn,name="logout_btn"),
    path('admin_home_page',views.admin_home_page,name="admin_home_page"),
    path('delete_img',views.delete_img,name="delete_img"),
    path('delete_img2',views.delete_img2,name="delete_img2"),
    path('admin_home2',views.home_page2,name="admin_home2"),

    path('about_page',views.about_page,name="about_page"),
    path('delete_about',views.delete_about,name="delete_about"),

    path('work_page',views.work_page,name="work_page"),

# new code
    path('work', views.music_list, name='music_list'),

# my code
    path('delete_work',views.delete_work,name="delete_work"),
    path('contact_page',views.contact_page,name="contact_page"),
    path('delete_contact',views.delete_contact,name="delete_contact"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)