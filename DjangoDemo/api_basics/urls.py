from django.urls import path, include
from .views import article_list, article_detail, ArticleAPIView, ArticleDetailsAPIView, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),

    # function based
    # path('article/', article_list),
    # path('article_detail/<int:id>/', article_detail)

    #classed based
    path('article/', ArticleAPIView.as_view()),
    path('article_detail/<int:id>/', ArticleDetailsAPIView.as_view()),

    # path('generic/article', GenericAPIView.as_view())
    path('generic/article/<int:id>/', GenericAPIView.as_view())

]