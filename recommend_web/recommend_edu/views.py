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
import pickle
import imblearn
import numpy as np

with open('recommend_edu/supporters/model_preffered.pkl', 'rb') as f:
    model_preferred = pickle.load(f)

with open('recommend_edu/supporters/model_responsibilities.pkl', 'rb') as f:
    model_responsibilities = pickle.load(f)

models = {"Model Preferred Skills": model_preferred,
          "Model trained on responsibilities": model_responsibilities
          }

images_print = {'Program Management': '../../static/img/program_managment.png',
                'Manufacturing & Supply Chain': '../../static/img/Marketing_Communications.png',
                'Technical Solutions': '../../static/img/technical_solution.png',
                'Developer Relations': '../../static/img/line.png',
                'Hardware Engineering': '../../static/img/line.png',
                'Partnerships': '../../static/img/line.png',
                'Product & Customer Support': '../../static/img/line.png',
                'Software Engineering': '../../static/img/software.png',
                'Data Center & Network': '../../static/img/line.png',
                'Business Strategy': '../../static/img/strategy.png',
                'Technical Writing': '../../static/img/line.png',
                'Technical Infrastructure': '../../static/img/line.png',
                'IT & Data Management': '../../static/img/line.png',
                'Marketing & Communications': '../../static/img/Marketing_Communications.png',
                'Network Engineering': '../../static/img/line.png',
                'Sales & Account Management': '../../static/img/line.png',
                'Sales Operations': '../../static/img/line.png',
                'Finance': '../../static/img/line.png',
                'Legal & Government Relations': '../../static/img/line.png',
                'Administrative': '../../static/img/line.png',
                'User Experience & Design': '../../static/img/users_design.png',
                'People Operations': '../../static/img/line.png',
                'Real Estate & Workplace Services': '../../static/img/line.png'}


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
        user_id = self.request.COOKIES.get(self.ai_cookie)
        user, create = Profile.objects.get_or_create(user_id=user_id)
        answer = Answer.objects.latest('id')
        try:
            user.age = answer.mean_age
            user.hobbies = answer.hobbies
            user.location = answer.location
            user.language = answer.lang
            skills = answer.feedback + ', ' + answer.hobbies + ', ' + answer.subjects
            if answer.work_in_team:
                skills += ' communicative, office, management, '
            else:
                skills += ' home office, remote, '

            if answer.logic_1 == 4 and answer.logic_2 == 2:
                skills += ' logic, analytic, good english, '
            else:
                skills += ' sense of humour, '

            if answer.tech_1 == 3 and answer.tech_2 == 2:
                skills += ' technical, data analysis, computer science, '
            else:
                skills += 'Design, creativity, people oriented, '

            if answer.responsible in [2, 5]:
                skills += 'Strong Organization,  team lead, strategy, '
            else:
                skills += 'People, psychology, marketing, '

            user.skills = skills

            for key, model in models.items():
                print(key, model.predict([skills]))

            user.goal = model_preferred.predict([skills])
            user.goal_extra = model_responsibilities.predict([skills])
            user.img = images_print[user.goal[0]]
            user.save()
            return render(request, self.template_name, {'profile': user})

        except:

            return render(request, self.template_name, {'profile': user})


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
        user = Profile.objects.get(user_id=user_id)
        print(user.skills)
        try:
            bot_response = get_bot_response(user_message,
                                            skills=user.skills,
                                            goal=user.goal,
                                            mean_age=user.age,
                                            location=user.location,
                                            lang=user.language)
        except Exception as e:
            print('Exception', e, user_id)
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
