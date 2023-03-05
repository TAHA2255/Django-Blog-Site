from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from .models import post
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    data = {'posts':post.objects.all()}
    return render(request,'myblog/index.html',data)

    
def about(request):
    return render(request,'myblog/about.html',{'title':'ABOUT'})
class PostListView(ListView):
    model = post
    template_name = 'myblog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6
class userListView(ListView):
    model = post
    template_name = 'myblog/userposts.html'
    context_object_name = 'posts'
    #ordering = ['-date_posted']
    paginate_by = 6
    def get_queryset(self):
        user = get_object_or_404(User,username=self.kwargs.get('username'))
        return post.objects.filter(author=user).order_by('-date_posted')
    

class PostDetailView(DetailView):
    model = post   
     #app/model_viewtype.html

class PostCreateView(UserPassesTestMixin,LoginRequiredMixin, CreateView):
    model = post   
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin ,UpdateView):
    model = post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = post
    #template_name = "myblog/post_confrim_delete.html"
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False