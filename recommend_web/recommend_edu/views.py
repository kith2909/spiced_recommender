from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render
from .models import Choice, Question, ChatMessage, Answer, Person
from .forms import ChoiceForm  # Make sure that the ChoiceForm is imported
from .models import ChatMessage
from .chat_ai import get_bot_response


class ChatView(generic.ListView):
    template_name = "recommend_edu/chat.html"
    context_object_name = "chat_history"
    ai_cookie = 'chat_to_grow'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_id'] = self.request.COOKIES.get(self.ai_cookie)
        return context

    def get_queryset(self):
        user_id = self.request.COOKIES.get(self.ai_cookie)
        return ChatMessage.objects.filter(user_id=user_id).order_by('-timestamp')

    def post(self, request, *args, **kwargs):
        user_message = request.POST.get('user_message')
        bot_response = get_bot_response(user_message)
        user_id = request.COOKIES.get(self.ai_cookie)
        ChatMessage.objects.create(user_id=user_id, user_message=user_message, bot_response=bot_response)
        response = self.get(request, *args, **kwargs)
        response.set_cookie(self.ai_cookie, user_id)
        return response


class IndexView(generic.ListView):
    template_name = "recommend_edu//index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future). NOT USED TEMPORARY
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
               :5
               ]


class AnswerFormView(generic.ListView):
    template_name = 'recommend_edu//detail.html'
    success_url = 'recommend_edu:votes'
    person_id = 1  # For example, we use 1. You might want to set this dynamically

    def get(self, request):
        person = Person.objects.get(id=self.person_id)
        formset = QuestionFormSet(instance=person)
        return render(request, self.template_name, {'formset': formset})

    def post(self, request):
        person = Person.objects.get(id=self.person_id)
        formset = QuestionFormSet(request.POST, instance=person)
        if formset.is_valid():
            formset.save()
            return redirect(self.success_url)
        else:
            return render(request, self.template_name, {'formset': formset})


'''
class QuestionaryView(generic.ListView):
    model = Question
    template_name = "recommend_edu/detail.html"

    def get_queryset(self):
        return Question.objects.order_by('-id')[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ChoiceForm()
        return context


class ResultsView(generic.DetailView):
    model = Question
    template_name = "recommend_edu//results.html"


def vote(request, user_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "recommend_edu/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("recommend_edu:results", args=(question.id,)))
'''
