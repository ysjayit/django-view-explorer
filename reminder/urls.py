from django.urls import path
from .views import ReminderList, ReminderDetail, ReminderCreate, ReminderUpdate, ReminderDelete

urlpatterns = [
    path('reminders/', ReminderList.as_view(), name='reminder-list'),
    path('reminders/<int:pk>', ReminderDetail.as_view(), name='reminder-details'),
    path('reminders/create/', ReminderCreate.as_view(), name='reminder-create'),
    path('reminders/update/<int:pk>', ReminderUpdate.as_view(), name='reminder-update'),
    path('reminders/delete/<int:pk>', ReminderDelete.as_view(), name='reminder-delete'),
]