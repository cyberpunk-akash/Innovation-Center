from django.shortcuts import render
from . import models
from . import forms

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import Http404
from django.views.generic import ListView,DeleteView,DetailView,CreateView
from django.utils import timezone
from django.contrib import messages
# Create your views here.
# from braces.views import SelectRelatedMixin

from django.contrib.auth import get_user_model
User=get_user_model()

class PostListView(ListView):
    model=models.Post
    template_name='dashboard/dash_list.html'

    def get_queryset(self):
        return models.Post.objects.filter(created_at__lte=timezone.now()).order_by('-created_at')
class StartupPosts(ListView):

    model=models.Post
    template_name='dashboard/startup_post_list.html'

    def get_queryset(self):
        try:
            self.post_user=User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['post_user']=self.post_user
        return context

class PostDetail(DetailView):
    model=models.Post
    template_name="dashboard/dash_detail.html"

    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset.filter(startup_name__username__iexact=self.kwargs.get('username'))

class CreatePost(LoginRequiredMixin,CreateView):
    model=models.Post
    template_name='dashboard/dash_form.html'
    form_class=forms.PostForm

    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.startup_name=self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin,DeleteView):
    model=models.Post
    success_url=reverse_lazy('dashboard:all')
    template_name='dashboard/post_confirm_delete.html'

    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset.filter(startup_name_id=self.request.user.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request,'Post deleted')
        return super().delete(*args,**kwargs)
