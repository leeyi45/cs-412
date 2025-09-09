"""URLs for the quote apps
"""

from django.urls import path
from .views import about, show_all, quote

urlpatterns = [
  path('', quote),
  path('about/', about),
  path('show_all/', show_all),
  path('quote/', quote)
]
