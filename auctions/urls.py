from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create_listing, name="create"),
    path("categories", views.categories, name="categories"),
    path("listing/<int:id>", views.listing_page, name="listing"), 
    path("addWatchlist/<int:id>", views.add_watchlist, name="addWatchlist"),
    path("removeWatchlist/<int:id>", views.remove_watchlist, name="removeWatchlist"),
    path("watchlist", views.watchlist_view, name="watchlist"),
    path("newComment/<int:id>", views.new_comment, name="newComment"),
    path("newBid/<int:id>", views.new_bid, name="newBid"),
    path("endAuction/<int:id>", views.end_auction, name="endAuction"),
]
