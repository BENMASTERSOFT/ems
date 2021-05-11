from django.shortcuts import render, redirect, HttpResponse
from poll.models import Question, Answer, Choice
from django.http import Http404
from django.contrib.auth.models import User


def index(request):
	questions = Question.objects.all()
	context={
	'title':'Polls',
	'questions':questions,
	}
	return render(request, 'poll/index.html', context)


def details(request,id=None):
	try:
		question = Question.objects.get(id=id)
	except:
		raise Http404

	context={
	'question':question,
	}
	return render(request, 'poll/details.html', context)


def poll(request,id=None):
	if request.method == "GET":
		try:
			question = Question.objects.get(id=id)
		except:
			raise Http404

		context={
		'question':question,
		}
		return render(request, 'poll/poll.html', context)
	if request.method == "POST":
		user_id = User.objects.get(id=1)
		choice= request.POST.get('choice')
		choice_obj=Choice.objects.get(id=choice)
		Answer.objects.create(user=user_id, choice=choice_obj)
	
		
		return HttpResponse("Answer Saved")
