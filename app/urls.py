from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.login_view,name='login'),
    path('1/',views.register,name='register'),
    path('add/',views.add,name='add'),
    path('display/',views.photo_list,name='list'),
    path('<int:photo_id>/update/',views.update,name='edit'),    
    path('<int:photo_id>/delete/',views.delete,name='delete'),
    path('mail/',views.mail_send,name='send_mail'),
    path('setup_mail/',views.mail_setup,name='setup_mail'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
