from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView 
from .models import Post, Comment, Category
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'discussion/discussion.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    # ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    
# def CategoryListView(request):
#     cat_menu_list = Category.objects.all()
#     return render(request, 'discussion/category_list.html', {'cat_menu_list':cat_menu_list})


class CategoryView(ListView):
    model = Post
    template_name = 'discussion/categories.html'
    context_object_name = 'category_posts'

    def get_queryset(self):
        self.category_name = self.kwargs['cats']
        return Post.objects.filter(category__name__icontains=self.category_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats'] = self.category_name
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'discussion/article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'discussion/add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'discussion/add_comment.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post_id = self.kwargs.get('pk')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article_detail', kwargs={'pk': self.kwargs.get('pk')})


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'discussion/update_post.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class UpdateCommentView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'discussion/update_comment.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdateCommentView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class DeletePostView(DeleteView):
    model = Post
    template_name = 'discussion/delete_post.html'
    success_url = reverse_lazy('discussion')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class DeleteCommentView(DeleteView):
    model = Comment
    template_name = 'discussion/delete_comment.html'
    success_url = reverse_lazy('discussion')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeleteCommentView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
