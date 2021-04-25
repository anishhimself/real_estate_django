from django.urls import path, include
from . import views

urlpatterns = [
    path('admindashboard', views.index, name="admindashboard"),
    path('users', views.getUsers),
    path('update-user-to-admin/<int:user_id>', views.update_user_to_admin),

    path('listing', views.listing),
    path('deleteListing/<int:l_id>', views.delete_listing),
    path('updateListing/<int:l_id>', views.update_listing),

    path('contact', views.contact),
    path('deleteContact/<int:c_id>', views.delete_contact),
    path('updateContact/<int:c_id>', views.update_contact),

    path('realtor', views.realtor),
    path('deleteRealtor/<int:r_id>', views.delete_realtor),
    path('updateRealtor/<int:r_id>', views.update_realtor),


]