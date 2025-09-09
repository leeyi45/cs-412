"""URLs for quotes
"""

import random
from django.http import HttpRequest
from django.shortcuts import render

QUOTES = [
  "I never think about the future"
]
IMAGES = [
  "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Albert_Einstein_1947.jpg/1920px-Albert_Einstein_1947.jpg"
]

def about(req: HttpRequest):
  """The /about route
  An about page with short biographical information about the person whose
  quotes you are displaying, as well as a note about the creator of this web
  application (you).
  """
  return render(req, 'quotes/about.html')

def quote(req: HttpRequest):
  """The /quote route
  Displays a picture of a famous or notable person of your choosing and a quote
  that this person said or wrote. The quote and image is selected at random from
  a list of images/quote.
  """
  index = random.randint(0, len(QUOTES) - 1)
  quote_text = QUOTES[index]
  image_url = IMAGES[index]

  return render(req, 'quotes/quote.html', {
    "quote_text": quote_text,
    "image_url": image_url
  })

def show_all(req: HttpRequest):
  """The /show_all route
  This view will add the entire list of quotes and images to the context data for
  the view.
  """

  return render(req, 'quotes/show_all.html', {
    "data": zip(QUOTES, IMAGES)
  })
