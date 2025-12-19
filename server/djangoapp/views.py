# Uncomment the required imports before adding the code

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json
import logging

from .populate import initiate

# Get an instance of a logger
logger = logging.getLogger(__name__)

# -----------------------------
# LOGIN
# -----------------------------
@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']

    user = authenticate(username=username, password=password)
    response = {"userName": username}

    if user is not None:
        login(request, user)
        response["status"] = "Authenticated"
    else:
        response["status"] = "Failed"

    return JsonResponse(response)


# -----------------------------
# LOGOUT
# -----------------------------
@csrf_exempt
def logout_request(request):
    logout(request)
    logger.info("User logged out")
    messages.info(request, "You have successfully logged out.")
    data = {"userName":""}
    return JsonResponse(data)


# -----------------------------
# REGISTRATION
# -----------------------------
@csrf_exempt
def registration(request):
    context = {}

    # Load JSON data from the request body
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']
    username_exist = False
    email_exist = False
    try:
        # Check if user already exists
        User.objects.get(username=username)
        username_exist = True
    except:
        # If not, simply log this is a new user
        logger.debug("{} is new user".format(username))

    # If it is a new user
    if not username_exist:
        # Create user in auth_user table
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,password=password, email=email)
        # Login the user and redirect to list page
        login(request, user)
        data = {"userName":username,"status":"Authenticated"}
        return JsonResponse(data)
    else :
        data = {"userName":username,"error":"Already Registered"}
        return JsonResponse(data)


# -----------------------------
# DEALERSHIPS (HOME PAGE)
# -----------------------------
def get_dealerships(request):
    context = {
        "dealerships": initiate()
    }
    return render(request, "Home.html", context)


# -----------------------------
# DEALER REVIEWS
# -----------------------------
def get_dealer_reviews(request, dealer_id):
    context = {
        "dealer_id": dealer_id,
        "reviews": []  # Reviews loaded via API in frontend
    }
    return render(request, "DealerReviews.html", context)


# -----------------------------
# DEALER DETAILS
# -----------------------------
def get_dealer_details(request, dealer_id):
    context = {
        "dealer_id": dealer_id
    }
    return render(request, "DealerDetails.html", context)


# -----------------------------
# ADD REVIEW
# -----------------------------
def add_review(request):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('djangoapp:login')

        review_data = {
            "user": request.user.username,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "review": request.POST.get("review"),
            "rating": request.POST.get("rating")
        }

        logger.info(f"Review submitted: {review_data}")
        messages.success(request, "Review submitted successfully.")

    return redirect('djangoapp:index')
