from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from .models import Review, Comment
from .forms import ReviewForm
from django.urls import reverse


# Create your views here.
def home(request):
    return render(request, 'books/home.html', {})

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('login')

    context = {
        'form' : form
    }
    return render(request, 'books/register.html', context)

def login(request):
    if request.method == 'GET':
        return render(request, 'books/login.html', {})
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
        user = authenticate(username=username, password=password)

        if user:
            return HttpResponseRedirect('forum')
        else:
            return render(request, 'books/login.html', {'error' : 'wrong login or password'})

def forum(request):
    reviews = Review.objects.order_by('-pub_date')[:10]
    context = {'reviews' : reviews}
    return render(request, 'books/forum.html', context)


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('forum')
    else:
        form = ReviewForm()
    return render(request, 'books/add_review.html', {'form' : form})


def add_comment(request):
    if request.method == 'POST':
        review_id = request.POST.get('review_id')
        comment_text = request.POST.get('comment_text')

        comment = Comment.objects.create(review_id=review_id, comment_text=comment_text)

    return HttpResponseRedirect(reverse('forum'))


def comments(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    comments = Comment.objects.filter(review_id=review_id)
    return render(request, 'books/comments.html', {'review': review, 'comments': comments})
