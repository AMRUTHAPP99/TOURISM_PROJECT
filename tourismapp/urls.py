from django.urls import path
from tourismapp import views


urlpatterns=[
     path('index_fn/',views.index_fun,name="index_fn"),
     path('add_customerfn/',views.add_customerfn,name="add_customerfn"),
     path('savedata_fn/',views.savedata_fn,name="savedata_fn"),
     path('savedestination_fn/',views.savedestination_fn,name="savedestination_fn"),
     path('displaypage_fn/',views.displaypage_fn,name="displaypage_fn"),

     path('editcustomer_fn/<int:dataid>/',views.editcustomer_fn,name="editcustomer_fn"),
     path('editdest_fn/<int:dataid>/',views.editdest_fn,name="editdest_fn"),
     path('displaydest_fn/',views.displaydest_fn,name="displaydest_fn"),
     path('updatedestination/<int:dataid>/',views.updatedestination,name="updatedestination"),
     path('deletedestination/<int:dataid>/',views.deletedestination,name="deletedestination"),
     path('deletecustomer/<int:dataid>/',views.deletecustomer,name="deletecustomer"),
     path('deletefeed/<int:dataid>/',views.deletefeed,name="deletefeed"),
     path('login_page/',views.login_page,name="login_page"),
     path('admin_login/',views.admin_login,name='admin_login'),
     path('admin_logout/',views.admin_logout,name='admin_logout'),
     path('add_destination/',views.add_destination,name='add_destination'),
     path('viewfeedback/',views.viewfeedback,name='viewfeedback'),
     path('user_details/',views.user_details,name='user_details'),
     path('viewbooking/',views.viewbooking,name='viewbooking'),
     path('addproduct_fn/',views.addproduct_fn,name='addproduct_fn'),
    path('save_addproductdata/',views.save_addproductdata,name='save_addproductdata'),
    path('displayproduct_fn/', views.displayproduct_fn, name='displayproduct_fn'),
    path('editaddproduct_fn/<int:productid>/', views.editaddproduct_fn, name='editaddproduct_fn'),
    path('updateaddproduct/<int:productid>/', views.updateaddproduct, name='updateaddproduct'),
    path('deleteaddproduct/<int:productid>/', views.deleteaddproduct, name='deleteaddproduct'),

]




