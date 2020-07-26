from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Questions 


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Questions.objects.order_by('-pub_date')[:5]

 
class DetailsView(generic.DetailView):
    model = Questions
    template_name = 'polls/details.html'
    context_object_name = 'question'


class ResultsView(generic.DetailView):
    model = Questions
    template_name = 'polls/results.html'
    context_object_name = 'question'


def votes(request,id):
        question = get_object_or_404(Questions, pk=id)
        try:
          selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
          return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
        else:
          selected_choice.votes += 1
          selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
          return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))