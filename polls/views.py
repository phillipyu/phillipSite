from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import Http404
from django.http import HttpResponse # not necessary if using render, as stated in Django Tutorial 3
# from django.template import loader # not necessary if using render, as stated in Django Tutorial 3

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list} #dictionary mapping template variable names to Python objects
    return render(request, 'polls/index.html', context) # render takes request object as its first argument, a template name as its second argument, and a dictionary as its optional third argument.

""" long version: 
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
    """

# shortened version:
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) #get_object_or_404 is a shortcut: takes a Django model as its first argument and an arbitrary number of keyword arguments
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)