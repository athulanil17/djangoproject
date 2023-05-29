from django.urls import path
from .views import Signupuser, Loginuser, Logout, MedicineList, MedicineDetail,CreateMedicine

urlpatterns = [
    path('signup/', Signupuser.as_view(), name='signup'),
    path('login/', Loginuser.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('medicines/', MedicineList.as_view(), name='medicine-list'),
    path('medicines/create/', CreateMedicine.as_view(), name='create-medicine'),
    path('medicines/<int:pk>/', MedicineDetail.as_view(), name='medicine-detail'),
]
