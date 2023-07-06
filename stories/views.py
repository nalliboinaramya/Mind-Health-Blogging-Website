from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from . models import Post


def showstories(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'stories/storiesdisplay.html',context)


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['caption','story']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

