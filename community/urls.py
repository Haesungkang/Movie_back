from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('', views.article_list_create),
    path('<int:article_pk>/', views.article_detail_update_delete),

    path('<int:article_pk>/comment_list/', views.comment_list),
    path('<int:article_pk>/comments/', views.comment_create),
    path('comments/<int:comment_pk>/', views.comment_detail_update_delete),
    # path('api-token-auth/', obtain_jwt_token),
]