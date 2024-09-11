from django.urls import path
from . import views
from app.views import ProductList,ProductRegister,ProductUpdate,ProductDelete

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('userlogout/',views.userlogout,name="userlogout"),
    path('Productlist/',ProductList.as_view(),name="ProductList"),
    path('ProductRegister/',ProductRegister.as_view(),name="ProductRegister"),
    path('mobilelist/',views.mobilelist,name="mobilelist"),
    path('electronicslist/',views.electronicslist,name="electronicslist"),
    path('showpricerange/',views.showpricerange,name="showpricerange"),
    path('ProductUpdate/<int:pk>',ProductUpdate.as_view(),name="ProductUpdate"),
    path('ProductDelete/<int:pk>',ProductDelete.as_view(),name="ProductDelete"),
    path('shortingbyprice',views.sortingbyprice,name="sortingbyprice"),
    path('sortingbyprice/',views.sortingbyprice,name="sortingbyprice"),
    path('searchproduct/',views.searchproduct,name="searchproduct"),
    path('showcarts/',views.showcarts,name="showcarts"),
    path('updateqty/<int:qv>/<int:productid>',views.updateqty,name="updateqty"),
    path('removecart/<int:productid>',views.removecart,name="removecart"),
    path('addtocart/<int:productid>',views.addtocart,name="addtocart"),
    path('payment/',views.payment,name="payment"),
    path('showorders/',views.showorders,name="showorders"),    
]
