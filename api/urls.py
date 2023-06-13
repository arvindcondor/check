from django.urls import path
from api.views import MyApiView

urlpatterns = [
    path('posts', MyApiView.as_view()),
    path('post/<int:id>/', MyApiView.as_view()),
    # path('view/post/', MyApiView.as_view()),

]
