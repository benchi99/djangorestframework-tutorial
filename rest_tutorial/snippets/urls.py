from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework import renderers
# from .views import SnippetViewSet, UserViewSet, api_root
from snippets import views

# Creamos un router y registramos los viewsets con él.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# Las URLS de la API ahora las determina el router por sí solo. (¡Qué maravilla!)
urlpatterns = [
    path('', include(router.urls)),
]

""" Tutorial 6
snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = SnippetViewSet.as_view({
    'get': 'highlight',
}, renderer_classes=[renderers.StaticHTMLRenderer])

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = [
    path('', views.api_root),
    # path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/', snippet_list, name='snippet-list'),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
    # path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-remarcado'),
    path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-remarcado'),
    # path('users/', views.UserList.as_view(), name='user-list'),
    path('users/', user_list, name='user-list'),
    # path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    path('users/<int:pk>', user_detail, name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)

"""