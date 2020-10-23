from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from notes import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact_us, name='contact_us'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', views.notes_list, name='notes_list'),
    path('notes/<int:pk>', views.notes_details, name='notes_details'),
    path('notes/add/', views.add_note, name='add_note'),
    path('notes/<int:pk>/edit/', views.edit_note, name='edit_note'),
    path('notes/<int:pk>/delete/', views.delete_note, name='delete_note'),
    path('notes/search/', views.search, name='search_result'),
    path('notes/search/', views.search, name='search')
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
