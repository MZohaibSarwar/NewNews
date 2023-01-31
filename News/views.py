from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from django.core.paginator import Paginator

from News.models import News, Subscribe, Contact


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_news'] = News.objects.all()
        context['recent_news'] = News.objects.filter(tag='Recent-Posts')
        context['popular_news'] = News.objects.filter(tag='Popular')
        context['most_read_news'] = News.objects.filter(tag='Most-Read')
        context['hot_stuff_news'] = News.objects.filter(tag='Hot-Stuff')
        context['top_of_the_week_news'] = News.objects.filter(tag='Top-of-the-week')
        context['must_read_news'] = News.objects.filter(tag='Must-Read')
        return context


def blog(request, category):
    news1 = News.objects.filter(category=category)
    news2 = News.objects.all().values()
    popular_news = News.objects.filter(tag='Popular')
    template = loader.get_template('blog.html')
    context = {
        'news1': news1,
        'news2': news2,
        'popular_news': popular_news,
    }
    return HttpResponse(template.render(context, request))


def blog2(request):
    news2 = News.objects.all().values()
    paginator = Paginator(news2, 3)
    page_number = request.GET.get('page')
    news3 = paginator.get_page(page_number)
    totalpage = news3.paginator.num_pages
    popular_news = News.objects.filter(tag='Popular')
    template = loader.get_template('blog2.html')
    context = {
        'total_page_list': [n+1 for n in range(totalpage)],
        'news3': news3,
        'news2': news2,
        'popular_news': popular_news,
    }
    return HttpResponse(template.render(context, request))


def article(request, id):
    single_news = News.objects.get(id=id)
    news2 = News.objects.all().values()
    popular_news = News.objects.filter(tag='Popular')
    template = loader.get_template('article.html')
    context = {
        'single_news': single_news,
        'news2': news2,
        'popular_news': popular_news,
    }
    return HttpResponse(template.render(context, request))


def SubscribeView(request):
    if request.method == 'POST':
        subscribe = Subscribe()
        email = request.POST.get('email')
        subscribe.email = email
        subscribe.save()
        return HttpResponse('Thanks for subscribed us!!!')

    mymember3 = News.objects.get(id=5)
    template = loader.get_template('thanks.html')
    context = {
        'mymember3': mymember3,
    }

    return HttpResponse(template.render(context, request))


def ContactView(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        tel = request.POST.get('tel')
        email2 = request.POST.get('email2')
        comment = request.POST.get('comment')
        contact.name = name
        contact.tel = tel
        contact.email2 = email2
        contact.comment = comment
        contact.save()
        return HttpResponse('Thanks for contact us!!!')

    mymember3 = News.objects.get(id=5)
    template = loader.get_template('thanks.html')
    context = {
        'mymember3': mymember3,
    }

    return HttpResponse(template.render(context, request))
