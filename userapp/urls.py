from django.urls import path
from userapp import views

urlpatterns=[
    path('', views.homepage_fn, name='homepage_fn'),
    path('registration_fn/',views.registration_fn,name='registration_fn'),
    path('saveregistrationdata/',views.saveregistrationdata,name='saveregistrationdata'),
     path('signup_fn/',views.signup_fn,name='signup_fn'),
     path('userlogout/',views.userlogout,name='userlogout'),
    path('contactpage/',views.contactpage,name='contactpage'),
    path('hotelbooking/',views.hotelbooking,name='hotelbooking'),
    path('destination_page/',views.destination_page,name='destination_page'),
    path('singledest_fn/<int:dataid>',views.singledest_fn,name='singledest_fn'),


    path('booking_fn/',views.booking_fn,name='booking_fn'),
    path('savebooking/',views.savebooking,name='savebooking'),
    path('displaybook_fn/',views.displaybook_fn,name='displaybook_fn'),
    path('deletebooking/<int:dataid>/',views.deletebooking,name='deletebooking'),
    path('feedback_fn/',views.feedback_fn,name='feedback_fn'),
    path('savefeedback/',views.savefeedback,name='savefeedback'),
    path('contact_fn/',views.contact_fn,name='contact_fn'),
    path('history_fn/',views.history_fn,name='history_fn'),
    path('about_fn/',views.about_fn,name='about_fn'),
    path('cardpage/',views.cardpage,name='cardpage'),
    path('invoice/',views.invoice,name='invoice'),
    path('save_Checkout/',views.save_Checkout,name='save_Checkout'),
    path('paymentB/',views.paymentB,name='paymentB'),
    path('chatbox/',views.chatbox,name='chatbox'),
    path('updatebooking/',views.updatebooking,name='updatebooking'),
    path('editbooking/<int:dataid>/',views.editbooking,name='editbooking'),
    path('savecontactdata/',views.savecontactdata,name='savecontactdata'),
    path('newfn/<dname>',views.newfn,name='newfn'),

    path('deletehistory/<int:dataid>/', views.deletehistory, name='deletehistory'),

    path('login_page/', views.login_page, name='login_page'),
    path('servicefn/', views.servicefn, name='servicefn'),
    path('search_results/', views.search_results, name='search_results'),






]

