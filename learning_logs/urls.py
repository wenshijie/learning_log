"""定义learning_logs的url模式"""

from django.urls import path,re_path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    path('topics/',views.topics,name='topics'),
    # 特定主题的详细页面
    path('topics/<int:topic_id>/',views.topic,name = 'topic'),
    path('new_topic/',views.new_topic,name = 'new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry,name='new_entry'),

]
