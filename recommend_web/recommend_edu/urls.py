from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

app_name = "recommend_edu"
urlpatterns = [
                  path("", views.IndexView.as_view(), name="index"),
                  path("test/", views.QuestionaryView.as_view(), name="detail"),
                  path("chat/", views.ChatView.as_view(), name="chat"),
                  path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
                  path("vote/", views.vote, name="vote"),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
