from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render
from .models import ChatMessage, Answer, Profile, Job
from .forms1 import QuestionFormSet
from .forms import AnswerForm
from .chat_ai import get_bot_response


#

class AnswerView(generic.FormView):
    template_name = 'recommend_edu//results.html'
    form_class = AnswerForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()

            return redirect('recommend_edu:votes')
        return render(request, self.template_name, {'form': form})


'''
class ProfileView(generic.FormView):
    template_name = 'recommend_edu//detail.html'
    success_url = 'recommend_edu:votes'
    ai_cookie = 'csrftoken'
    form_class = QuestionFormSet

    def get(self, request):
        user_id = self.request.COOKIES.get(self.ai_cookie)
        print('COOKIE:', user_id)
        # Try to get the Person instance if it exists or create a new one
        user, created = Profile.objects.get_or_create(user_id=user_id)
        formset = QuestionFormSet(instance=user)
        return render(request, self.template_name, {'formset': formset})

    def post(self, request):
        user_id = self.request.COOKIES.get(self.ai_cookie)
        # Try to get the Person instance if it exists or create a new one
        user, created = Profile.objects.get_or_create(user_id=user_id)
        formset = QuestionFormSet(request.POST, instance=user)
        if formset.is_valid():
            formset.save()
            return redirect(self.success_url, profile_id=user.id)

        return render(request, self.template_name, {'formset': formset})
'''


class ProfileView(generic.FormView):
    template_name = 'recommend_edu//detail.html'
    success_url = 'recommend_edu:votes'
    ai_cookie = 'csrftoken'
    form_class = QuestionFormSet

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user_id = self.request.COOKIES.get(self.ai_cookie)
        user, create = Profile.objects.get_or_create(user_id=user_id)
        print(user.user_id, user.id, "HELP")

        kwargs.update({'instance': user})
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        # return the URL where you want to redirect after successful form submission
        return self.success_url


class VotesView(generic.ListView):
    template_name = 'recommend_edu//votes.html'
    ai_cookie = 'csrftoken'

    def get(self, request):
        try:
            user_id = self.request.COOKIES.get(self.ai_cookie)
            user, create = Profile.objects.get_or_create(user_id=user_id)
            answer = Answer.objects.get(profile_id=user.id)
            return render(request, self.template_name, {'answer': answer})
        except:
            return render(request, self.template_name, {'answer': 'You need to go true test first)'})


class ChatView(generic.ListView):
    template_name = "recommend_edu//chat.html"
    context_object_name = "chat_history"
    ai_cookie = 'csrftoken'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_id'] = self.request.COOKIES.get(self.ai_cookie)
        return context

    def get_queryset(self):
        user_id = self.request.COOKIES.get(self.ai_cookie)
        return ChatMessage.objects.filter(user_id=user_id).order_by('-timestamp')

    def post(self, request, *args, **kwargs):
        '''
        Analysis for user Profile using pretrained openAi model
        :return: bot-assistant response, for details check chat_ai.py
        '''
        user_message = request.POST.get('user_message')
        user_id = request.COOKIES.get(self.ai_cookie)
        try:
            user = Profile.objects.get(user_id=user_id)

            # IMPORTANT - switch to a Profile information after prediction

            answer = Answer.objects.get(id=user.id)
            bot_response = get_bot_response(user_message, mean_age=answer.mean_age)
        except Exception as e:
            bot_response = get_bot_response(user_message)

        ChatMessage.objects.create(user_id=user_id, user_message=user_message, bot_response=bot_response)
        response = self.get(request, *args, **kwargs)
        response.set_cookie(self.ai_cookie, user_id)
        return response


class IndexView(generic.ListView):
    template_name = "recommend_edu//index.html"
    context_object_name = "main_page"
    ai_cookie = 'csrftoken'

    def get(self, request):
        response = render(request, self.template_name)
        return response
