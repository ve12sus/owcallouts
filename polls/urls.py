from django.conf.urls import url

from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/answer/
    url(r'^answer/$', views.answer, name='answer'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

