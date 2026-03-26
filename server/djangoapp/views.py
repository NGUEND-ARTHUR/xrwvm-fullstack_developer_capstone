# Endpoint pour retourner toutes les marques et modèles de voitures
from django.views.decorators.csrf import csrf_exempt
from .models import CarMake, CarModel
from django.views.decorators.http import require_GET
from django.http import JsonResponse

@require_GET
def get_all_carmakes(request):
    if request.method == 'GET':
        makes = CarMake.objects.all()
        data = []
        for make in makes:
            models = make.models.all()
            data.append({
                'id': make.id,
                'name': make.name,
                'description': make.description,
                'models': [
                    {
                        'id': model.id,
                        'name': model.name,
                        'type': model.type,
                        'year': model.year
                    } for model in models
                ]
            })
        return JsonResponse({'car_makes': data}, safe=False)

# Create a `login_request` view to handle sign in request

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

@csrf_exempt
def login_user(request):
    next_url = request.GET.get('next') or request.POST.get('next') or '/'
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next_url)
        else:
            return render(request, "login.html", {"login_error": "Invalid credentials", "next": next_url})
    # GET: show login form
    return render(request, "login.html", {"next": next_url})


# Create a `logout_request` view to handle sign out request
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def logout_request(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({"status": "Logged out"})
    return JsonResponse({"error": "Only POST allowed"}, status=405)

# Create a `registration` view to handle sign up request
# @csrf_exempt
# def registration(request):
# ...

# # Update the `get_dealerships` view to render the index page with
# a list of dealerships
# def get_dealerships(request):
# ...



from .models import DealerReview, Dealer
from django.views.decorators.http import require_GET
from django.shortcuts import render
# Return the home page with dealers listed
def home(request):
    state = request.GET.get("state")
    if state:
        dealers = Dealer.objects.filter(state=state)
    else:
        dealers = Dealer.objects.all()
    all_states = Dealer.objects.values_list('state', flat=True).distinct().order_by('state')
    return render(request, "Home.html", {"dealers": dealers, "all_states": all_states, "selected_state": state})

# Return reviews for a dealer as JSON
from django.shortcuts import get_object_or_404

@require_GET
def get_dealer_reviews(request, dealer_id):
    dealer = get_object_or_404(Dealer, id=dealer_id)
    reviews = DealerReview.objects.filter(dealer_id=dealer_id)
    # If HTML is requested, render template; else, return JSON
    if 'text/html' in request.META.get('HTTP_ACCEPT', ''):
        return render(request, "dealer_details.html", {"dealer": dealer, "reviews": reviews})
    # fallback to JSON for API
    data = [
        {
            "dealer_id": r.dealer_id,
            "reviewer": r.reviewer,
            "review": r.review,
            "rating": r.rating,
            "created_at": r.created_at.isoformat()
        }
        for r in reviews
    ]
    return JsonResponse(data, safe=False)

# Return all dealers as JSON
@require_GET
def get_all_dealers(request):
    dealers = Dealer.objects.all()
    data = [
        {
            "id": d.id,
            "name": d.name,
            "address": d.address,
            "city": d.city,
            "state": d.state,
            "zip_code": d.zip_code
        }
        for d in dealers
    ]
    return JsonResponse(data, safe=False)

# Create a `get_dealer_details` view to render the dealer details
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request):
# ...
