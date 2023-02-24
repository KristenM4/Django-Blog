from django.shortcuts import render
from django.http import HttpResponseNotFound, Http404
from django.template.loader import render_to_string
import datetime as dt

# Create your views here.
posts = [
    {
    "slug": "trek-through-the-jungle",
    "image": "hiking.jpg",
    "author": Kristen,
    "date": dt.date(2022, 11, 19),
    "title": "Jungle Trekking",
    "excerpt": "An early morning hike through a leafy forest in Selangor. Despite's the state's advanced development and high population, there are still many areas to find respite in nature.",
    "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Rem possimus animi culpa cumque, delectus nemo est! Delectus, sed iure sit, 
        deserunt totam tempore magnam voluptates laboriosam, necessitatibus fuga aliquam vero!

        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Rem possimus animi culpa cumque, delectus nemo est! Delectus, sed iure sit, 
        deserunt totam tempore magnam voluptates laboriosam, necessitatibus fuga aliquam vero!

        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Rem possimus animi culpa cumque, delectus nemo est! Delectus, sed iure sit, 
        deserunt totam tempore magnam voluptates laboriosam, necessitatibus fuga aliquam vero!
    """
    },
    {
    "slug": "programming-in-the-equator",
    "image": "laptop.jpg",
    "author": Kristen,
    "date": dt.date(2022, 12, 28),
    "title": "The Struggles of Equatorial Programming",
    "excerpt": "Living in a tropical country can be like paradise. Good food, warm weather, and friendly locals. But for tech-focused people, the relentlessly hot and humid climate can have some unexpected downsides.",
    "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Rem possimus animi culpa cumque, delectus nemo est! Delectus, sed iure sit, 
        deserunt totam tempore magnam voluptates laboriosam, necessitatibus fuga aliquam vero!

        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Rem possimus animi culpa cumque, delectus nemo est! Delectus, sed iure sit, 
        deserunt totam tempore magnam voluptates laboriosam, necessitatibus fuga aliquam vero!
        
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Rem possimus animi culpa cumque, delectus nemo est! Delectus, sed iure sit, 
        deserunt totam tempore magnam voluptates laboriosam, necessitatibus fuga aliquam vero!
    """
    },
    {
    "slug": "the-elusive-musang",
    "image": "musang.jpg",
    "author": Kristen,
    "date": dt.date(2023, 2, 4),
    "title": "A Glimpse of the Elusive Musang",
    "excerpt": "Also known as the Common Palm Civet, the Musang has adapted well to urban environments. They're an uncommon sight in Malaysian suburbs, and a stark reminder of the region's unique ecosystem.",
    "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Rem possimus animi culpa cumque, delectus nemo est! Delectus, sed iure sit, 
        deserunt totam tempore magnam voluptates laboriosam, necessitatibus fuga aliquam vero!

        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Rem possimus animi culpa cumque, delectus nemo est! Delectus, sed iure sit, 
        deserunt totam tempore magnam voluptates laboriosam, necessitatibus fuga aliquam vero!
        
        Lorem ipsum dolor sit amet consectetur adipisicing elit. 
        Rem possimus animi culpa cumque, delectus nemo est! Delectus, sed iure sit, 
        deserunt totam tempore magnam voluptates laboriosam, necessitatibus fuga aliquam vero!
    """
    }
]

def index(request):
    latest_post = posts[0]
    return render(request, "blog/index.html", {"latest_post": latest_post})


def posts(request):
    all_posts = posts
    return render(request, "blog/posts.html", {"all_posts": all_posts})


def get_post(request, slug):
    for i in posts:
        if slug == i['slug']:
            return render(request, "blog/post.html", {"post": i})
    else:
        error_page = render_to_string("404.html")
        return HttpResponseNotFound(error_page)
