from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # path for registration

    path('login', views.login_user, name='login'),
    path('logout', views.logout_request, name='logout'),



    # path for all dealers view
    path('getalldealers', views.get_all_dealers, name='get_all_dealers'),
    # path for dealer reviews view
    path('fetchReviews/dealer/<int:dealer_id>', views.get_dealer_reviews, name='get_dealer_reviews'),

    # path for posting a review
    path('postreview/<int:dealer_id>', __import__('djangoapp.views_add_review').views_add_review.add_review, name='add_review'),

    # path for all car makes and models
    path('getallcarmakes/', views.get_all_carmakes, name='get_all_carmakes'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
