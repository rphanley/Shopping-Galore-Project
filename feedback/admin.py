from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('product', 'user_name', 'date', 'rating',)
    list_filter = ('product', 'date',)
    search_fields = ('product__name', 'details',)

    class Meta:
        model = Feedback


# Register your models here.
admin.site.register(Feedback, FeedbackAdmin)
