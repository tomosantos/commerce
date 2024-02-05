from django.contrib import admin

from .models import Category, Listing, User, Comment, Bid

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "resume", "category", "price", "isActive", "owner")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "message", "listing")
    
class BidAdmin(admin.ModelAdmin):
    list_display = ("user", "bid")

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Bid, BidAdmin)