"""URLs for quotes
"""

import random
from django.http import HttpRequest
from django.shortcuts import render

QUOTES = [
  "The best argument against democracy is a five-minute conversation with the average voter.",
  "Tact is the ability to tell someone to go to hell in such a way that they look forward to the trip.",
  "I am fond of pigs. Dogs look up to us. Cats look down on us. Pigs treat us as equals."
]
IMAGES = [
  "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bc/Sir_Winston_Churchill_-_19086236948.jpg/500px-Sir_Winston_Churchill_-_19086236948.jpg",
  "https://cdn.britannica.com/25/171125-050-94459F61/Winston-Churchill.jpg",
  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTKiWYBgPBMLR_FbmvJnoGvAJsAiWhoFMzjbiT21RHl6bMYVEPjAG6YeJU&s"
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
