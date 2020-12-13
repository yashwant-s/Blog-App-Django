from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post#to import model form models.py
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.
#dummy data
# posts=[
#       {
#             'author': 'Yashwant',
#             'title': 'Blog Post 1',
#             'content': 'first post content',
#             'date_posted': 'December 10, 2020'    
#       },
#       {
#             'author': 'Jane Doe',
#             'title': 'Blog Post 2',
#             'content': 'Seconf post content',
#             'date_posted': 'December 11, 2020'    

#       }
# ]




def home(request):
      context={'posts': Post.objects.all()}# assigning data from post model
      return render(request, 'blog/home.html', context)#here we write path of the regarding file in template directory

#view for list of all the post
class PostListView(ListView):
      model = Post
      template_name = 'blog/home.html' #<app> / <model>_<viewtype>.html this is what default listview is looking for
      context_object_name = 'posts'
      ordering = ['-date_posted']
      paginate_by = 10

class UserPostListView(ListView):
      model = Post
      template_name = 'blog/user_post.html' #<app> / <model>_<viewtype>.html this is what default listview is looking for
      context_object_name = 'posts'
      paginate_by = 10

      def get_queryset(self):
            user = get_object_or_404(User, username=self.kwargs.get('username'))
            return Post.objects.filter(author = user).order_by('-date_posted')
            

#class view for details of the post
class PostDetailView(DetailView):
      model = Post

#in the create and update view we are not specifying any path for template coz 
#it inherently goes to the post_form.html(which is alos why we did not create two different templates)
#class view to create new post
class PostCreateView(LoginRequiredMixin, CreateView):
      model = Post 
      fields = ['title', 'content']

      def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)

#class view to update the already created post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
      model = Post 
      fields = ['title', 'content']

      def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)

      #here we are checking if the user trying to update is the author of the post
      def test_func(self):
            post = self.get_object()
            if self.request.user == post.author:
                  return True
            else:
                  return False

#class view for delete the post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
      model = Post
      success_url = '/'
      def test_func(self):
            post = self.get_object()
            if self.request.user == post.author:
                  return True
            else:
                  return False
def about(request):
      return render(request, 'blog/about.html')