from django.contrib import admin
from django.urls import path
from django.urls import path, include
from myapp import views
from myapp.views import Detail, labmemberdetails, formTest, items, placeorder

app_name = 'myapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('myapp.urls')),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('<int:type_no>/', views.detail, name='detail'),
    path('about/<int:year>/<int:month>/', views.about, name='about_with_date'),  # URL with year and month
    path('detail/<int:type_no>/', Detail.as_view(), name='detail'),  # for CBV
    path('team/', labmemberdetails.as_view(), name='team'),
    path('formTest/', views.formTest, name='orderInterest'),
    path('items', views.items, name='items'),
    path('placeorder/', views.placeorder, name='placeorder')
]

