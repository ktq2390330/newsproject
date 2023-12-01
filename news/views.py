from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,DetailView,DeleteView,FormView
from django.urls import reverse_lazy
from .forms import NewsPostForm,ContactForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import NewsPost
from django.contrib import messages
from django.core.mail import EmailMessage
# Create your views here.
class IndexView(TemplateView):
    template_name='index.html'

@method_decorator(login_required,name='dispatch')
class CreateNewsView(CreateView):
    form_class=NewsPostForm
    template_name='post_news.html'
    success_url=reverse_lazy('news:post_done')

    def form_valid(self, form):
        postdata=form.save(commit=False)
        postdata.user=self.request.user
        postdata.save()
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    template_name='post_success.html'

class IndexView(ListView):
    template_name='index.html'

    queryset=NewsPost.objects.order_by('-posted_at')

    paginate_by=9

class CategoryView(ListView):
    template_name='index.html'
    paginate_by=9
    def get_queryset(self):
        category_id=self.kwargs['category']
        categories=NewsPost.objects.filter(
            category=category_id).order_by('posted_at')
        return categories

class UserView(ListView):
    template_name='index.html'
    paginate_by=9

    def get_queryset(self):

        user_id=self.kwargs['user']
        user_list=NewsPost.objects.filter(
            user=user_id).order_by('posted_at')
        return user_list
    
class DetailView(DetailView):
    template_name='detail.html'
    model=NewsPost

class MypageView(ListView):
    template_name='mypage.html'
    paginate_by=9
    def get_queryset(self):
        queryset=NewsPost.objects.filter(
            user=self.request.user).order_by('posted_at')
        return queryset

class NewsDeleteView(DeleteView):
    model=NewsPost
    template_name='news_delete.html'
    success_url=reverse_lazy('news:mypage')

    def delete(self,request,*args, **kwargs):
        return super().delete(request,*args, **kwargs)

class ContactView(FormView):
    template_name='contact.html'
    form_class=ContactForm
    success_url=reverse_lazy('news:contact')

    def form_valid(self, form):
        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        title=form.cleaned_data['title']
        message=form.cleaned_data['message']
        subject='お問い合わせ:{}'.format(title)

        message=\
            '送信者名:{0}\n メールアドレス:{1}\n タイトル:{2}\n メッセージ:{3}' \
            .format(name,email,title,message)
        
        from_email='oohara.pretest@gmail.com'
        to_list=['oohara.pretest@gmail.com']
        message=EmailMessage(subject=subject,
                            body=message,
                            from_email=from_email,
                            to=to_list,)
        message.send()
        messages.success(
            self.request,'お問い合わせは正常に送信されました。'
        )
        return super().form_valid(form)
    