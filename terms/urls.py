from django.urls import path

from. import views

urlpatterns = [
    path('', views.AllKeywordsListView.as_view(), name='terms'),
    path('terms', views.KeywordsListView.as_view(), name='keyword-by-page'),
    path('terms/<int:page>', views.KeywordsListView.as_view(),
         name='keyword-by-page'),
    path('keyword.json', views.listing_api, name="keyword-api")
]
