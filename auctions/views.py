from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Category, Listing, Comment, Bid

# index
def index(request):
    activeListings = Listing.objects.filter(isActive=True)
    categories = Category.objects.all()
    return render(request, "auctions/index.html", {
        "listings": activeListings,
        "categories": categories
    })

# listing section
def create_listing(request):
    if request.method == "POST":
        # get data from the form
        title = request.POST["title"]
        resume = request.POST["resume"]
        description = request.POST["description"]
        img = request.POST["img"]
        price = request.POST["price"]
        category = request.POST["category"]
        
        # find out who is the user
        currentUser = request.user
        
        # select category in a list of categories
        category_data = Category.objects.get(categoryName=category)
        
        # create bid object
        bid = Bid(bid=float(price), user=currentUser)
        bid.save()
        
        # create a new listing object
        newListing = Listing(
            title=title,
            resume=resume,
            description=description,
            imageUrl= img,
            price=bid,
            category=category_data,
            owner = currentUser
        )
        
        # insert the object in our database
        newListing.save()
        
        # redirect to index page
        return HttpResponseRedirect(reverse("index"))
    else:
        categories = Category.objects.all()
        return render(request, "auctions/create.html", {
            "categories": categories
        })
    

def listing_page(request, id):
    # get listing, watchlist and comments data
    listing_data = Listing.objects.get(pk=id)
    verify_watchlist = request.user in listing_data.watchlist.all()
    all_comments = Comment.objects.filter(listing=listing_data)
    
    # expected true or false
    is_owner = request.user.username == listing_data.owner.username
    
    return render(request, "auctions/listing.html", {
        "listing": listing_data,
        "verify_watchlist": verify_watchlist,
        "comments": all_comments,
        "isOwner": is_owner
    })


def end_auction(request, id):
    # closing auction
    listing_data = Listing.objects.get(pk=id)
    listing_data.isActive = False
    listing_data.save()
    
    verify_watchlist = request.user in listing_data.watchlist.all()
    all_comments = Comment.objects.filter(listing=listing_data)
    
    is_owner = request.user.username == listing_data.owner.username
    
    return render(request, "auctions/listing.html", {
        "listing": listing_data,
        "verify_watchlist": verify_watchlist,
        "comments": all_comments,
        "isOwner": is_owner,
        "alert": True,
        "message": "Bid successfully closed!"
    })


def new_bid(request, id):
    bid = request.POST["newBid"]
    listing_data = Listing.objects.get(pk=id)
    all_comments = Comment.objects.filter(listing=listing_data)
    verify_watchlist = request.user in listing_data.watchlist.all()
    
    is_owner = request.user.username == listing_data.owner.username
    
    if float(bid) > listing_data.price.bid:
        new_bid = Bid(bid=float(bid), user=request.user)
        new_bid.save()
        
        listing_data.price = new_bid
        listing_data.save()
        
        return render(request, "auctions/listing.html", {
            "listing": listing_data,
            "message": "Bid was updated successfully!",
            "isOwner": is_owner,
            "alert": True,
            "comments": all_comments,
            "verify_watchlist": verify_watchlist
        })

    else:
        return render(request, "auctions/listing.html", {
            "listing": listing_data,
            "message": "Bid update was failed!",
            "isOwner": is_owner,
            "alert": False,
            "comments": all_comments,
            "verify_watchlist": verify_watchlist
        })    

# categories
def categories(request):
    if request.method == "POST":
        category_form = request.POST["category"]
        category_match = Category.objects.get(categoryName=category_form)
        
        activeListings = Listing.objects.filter(isActive=True, category=category_match)
        categories = Category.objects.all()
        
        return render(request, "auctions/index.html", {
            "listings": activeListings,
            "categories": categories
        })
    

# watchlist section
def add_watchlist(request, id):
    listing_data = Listing.objects.get(pk=id)
    current_user = request.user
    listing_data.watchlist.add(current_user)
    
    return HttpResponseRedirect(reverse("listing", args=(listing_data.id,)))


def remove_watchlist(request, id):
    listing_data = Listing.objects.get(pk=id)
    current_user = request.user
    listing_data.watchlist.remove(current_user)
    
    return HttpResponseRedirect(reverse("listing", args=(listing_data.id,)))    


def watchlist_view(request):
    currentUser = request.user
    listings_watchlist = currentUser.userWatchlist.all()
    
    return render(request, "auctions/watchlist.html", {
        "listings": listings_watchlist
    })


# comments section
def new_comment(request, id):
    currentUser = request.user
    listing_data = Listing.objects.get(pk=id)
    message = request.POST["newComment"]
    
    newComment = Comment(
        author = currentUser,
        listing = listing_data,
        message = message
    )
    
    newComment.save()
    
    return HttpResponseRedirect(reverse("listing", args=(listing_data.id,)))


# login, logout and register
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
