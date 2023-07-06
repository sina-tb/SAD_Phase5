from django.urls import path
from .views import PackageListView, PrerequisitesTypeListView, RecordCreateView

urlpatterns = [
    path('packages/', PackageListView.as_view(), name='package-list'),
    path('packages/<int:package_id>/prerequisites-types/', PrerequisitesTypeListView.as_view(), name='prerequisites-types'),
    path('records/', RecordCreateView.as_view(), name='record-create'),
]
