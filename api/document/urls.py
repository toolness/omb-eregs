from django.conf.urls import url

from document.views import TreeView

urlpatterns = [
    url(r'^(?P<policy_id>[0-9]+)(/(?P<identifier>[a-zA-Z0-9_-]+))?',
        TreeView.as_view()),
]
