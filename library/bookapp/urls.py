from django.urls import path
from .import views

urlpatterns=[
    path('b1/',views.bookview,name="bookform_url"),
    path('s1/',views.showview,name="show_url"),
    path('u1/<int:id>/',views.updateview,name="update_url"),
    path('d1/<int:id>/',views.deleteview,name="delete_url")
]