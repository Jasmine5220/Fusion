from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    # Applicant-related paths
    path("applicant/applications/submit/", views.submit_application, name="submit_application"),
    path("applicant/applications/", views.view_applications, name="view_applications"),
    path("applicant/applications/details/<int:application_id>/", views.view_application_details_for_applicant, name="view_application_details"),
    path("applicant/drafts/", views.saved_drafts, name="saved_drafts"),

    # PCCAdmin-related paths
    path("pccAdmin/applications/new/", views.new_applications, name="new_applications"),
    path("pccAdmin/applications/review/", views.review_applications, name="review_applications"),
    path("pccAdmin/applications/forward/", views.forward_application, name="forward_applications"),
    path("pccAdmin/applications/reject/", views.reject_application, name="reject_applications"),
    path("pccAdmin/applications/ongoing/", views.ongoing_applications, name="ongoing_applications"),
    path("pccAdmin/applications/past/", views.past_applications, name="past_applications"),

    # Director-related paths
    path("director/applications/new/", views.director_new_applications, name="director_new_applications"), 
    path("director/application/reject", views.director_reject, name="director_reject"),
    path("director/application/accept", views.director_accept, name="director_accept"),
    path("director/reviewedapplications", views.director_reviewed_applications, name="director_reviewed_applications"),
    path("director/active", views.active_applications, name="active_applications"),
    # path("director/final-review/details", views.director_status_view, name="director_status_view"),
    path("director/notifications/", views.director_notifications, name="director_notifications"),

    # Attorney management URLs
    path("pccAdmin/attorneys/", views.get_attorney_list, name="get_attorney_list"),
    path("pccAdmin/attorneys/add/", views.add_attorney, name="add_attorney"),
    path("pccAdmin/attorneys/<int:attorney_id>/remove/", views.remove_attorney, name="remove_attorney"),
    path("pccAdmin/attorneys/<int:attorney_id>/applications/", views.get_attorney_applications, name="get_attorney_applications"),
    path("pccAdmin/attorneys/<int:attorney_id>/update/", views.update_attorney_details, name="update_attorney_details"),

    # Document Management URLs
    path('documents/', views.manage_documents, name='manage_documents'),
    path('pccAdmin/documents/<int:document_id>/delete/', views.delete_document, name='delete_document'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
