from django.urls import path
from fileprocessing import views

urlpatterns = [
    path("", views.fileupload, name="fileprocessing"),
    path("chunking/<uuid:request_id>", views.chunking, name="chunking"),
    path("restart/<uuid:request_id>", views.restart, name="restart")

]