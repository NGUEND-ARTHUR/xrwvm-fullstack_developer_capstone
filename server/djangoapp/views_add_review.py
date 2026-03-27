from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest

@login_required
@csrf_exempt
def add_review(request, dealer_id):
    if request.method == 'GET':
        # Import CarMake ici pour éviter les imports circulaires
        from djangoapp.models import CarMake
        car_makes = CarMake.objects.all().values_list('name', flat=True)
        return render(request, 'add_review.html', {'dealer_id': dealer_id, 'car_makes': car_makes})
    elif request.method == 'POST':
        from djangoapp.models import DealerReview
        review_text = request.POST.get('review')
        rating = request.POST.get('rating')
        purchased = request.POST.get('purchase') == 'on'
        reviewer = request.user.username if request.user.is_authenticated else 'Anonymous'
        # Save the review
        DealerReview.objects.create(
            dealer_id=dealer_id,
            reviewer=reviewer,
            review=review_text,
            rating=rating,
        )
        return redirect('djangoapp:get_dealer_reviews', dealer_id=dealer_id)
    else:
        return HttpResponseBadRequest('Invalid request method')
