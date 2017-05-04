from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, QueryDict
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Choice, Question

# Create your views here.


def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'polls/index.html', context)


def answer(request):
    q = Question.objects.all()
    answers = request.POST
    results = {}
    total_correct = 0
    total_questions = len(q)
    ranking = ""
    ranks = [
      (0, "It's zero noon."),
      (1, "Get off my team."),
      (2, "Do you even play this game?"),
      (3, "Dòng zhù, bùxǔ zǒu!"),
      (4, "You must die, die, die a lot."),
      (5, "I've got you in my sights to do better."),
      (6, "At least you tried."),
      (7,  "50%... could be better!"),
      (8,  "Study up!"),
      (9,  "Need more work."),
      (10, "Double digits now."),
      (11, "Experience getting most of them."),
      (12, "Right on target!"),
      (13, "Team captain!"),
      (14, "Seagull"),
    ]

    for key, value in answers.items():
        try:
            if Question.objects.get(pk=key).answer_text == value:
                correctness = 'correct'
                question_text = Question.objects.get(pk=key).question_text
                tup = (question_text, value, correctness)
                results[key] = tup
                total_correct += 1
            else:
                correctness = 'wrong'
                question_text = Question.objects.get(pk=key).question_text
                tup = (question_text, value, correctness)
                results[key] = tup
        except (ValueError):
            pass

    for rank, title in ranks:
        if total_correct == rank:
            ranking = title

    return render(request, 'polls/answer.html', {'results': sorted(results.items()),
        'total_correct': total_correct, 'total_questions': total_questions,
        'ranking': ranking})
