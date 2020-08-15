from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # path('',views.home,name='home'),
    path('', views.post_list,name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
            views.post_details,
            name='post_details')
]