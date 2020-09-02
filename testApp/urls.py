from django.urls import path
from testApp import views

urlpatterns = [
    path('handler404',views.handler404,name = 'handler404'),
    path('handler500',views.handler500,name = 'handler500'),
    path('index',views.index_Veiw, name = 'index'),

]
handler404 =views.handler404
# handler500 = testApp.views.handler500
