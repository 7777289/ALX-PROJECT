# from django.contrib import admin
# from .models import Apartment

# admin.site.register(Apartment)

from django.contrib import admin
from .models import Apartment

class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'price', 'owner')
    list_filter = ('owner',) # This line adds the filter

admin.site.register(Apartment, ApartmentAdmin)