# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from event.models import Column, Event
from event import form


def index(request):
    home_display_columns = Column.objects.filter(home_display=True)
    nav_display_columns = Column.objects.filter(nav_display=True)
    return render(request, 'event/index.html', {
        'home_display_columns': home_display_columns,
        'nav_display_columns': nav_display_columns,
        'nav_show': 'home',
    })


def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'event/column.html', {'column': column, 'nav_show': column.name, })


def event_detail(request, id, event_slug):
    at_home = True
    event = Event.objects.get(id=id)
    for k in event.column.all():
        print(k)
    if event_slug != event.slug:
        return redirect(event, permanent=True)

    return render(request, 'event/event.html', {'event': event, 'nav_show': event.column.all()[0].name})


def add_event(request):
    if request.method == 'POST':
        print("!")
        name=request.GET['name']
        content=request.GET['content']
        return HttpResponse(content)
    else:
        print("-")
        return render(request, 'event/add_record.html',)


def customers(request):
    customer_list = models.Customer.objects.all()
    paginator = Paginator(customer_list, 3)  # 每页显示2条纪录

    page = request.GET.get('page')  # 获取客户端请求传来的页码

    try:
        customer_list = paginator.page(page)  # 返回用户请求的页码对象
    except PageNotAnInteger:  # 如果请求中的page不是数字,也就是为空的情况下
        customer_list = paginator.page(1)
    except EmptyPage:
        # 如果请求的页码数超出paginator.page_range(),则返回paginator页码对象的最后一页
        customer_list = paginator.page(paginator.num_pages)

    return render(request, 'crm/customers.html', {'customer_list': customer_list})


def customer_detail(request, customer_id):  # 定义customer_detail.html网页的视图函数
    # 这个函数有两个功能:
    # 1.获取该记录的详细信息,用form表单形式展示
    # 2.修改该条纪录,并且保存.
    # 获取时用页面请求用的get方法,修改时请求用的post方法
    customer_obj = models.Customer.objects.get(id=customer_id)
    form = forms.CustomerModelForm()

    return render(request, 'crm/customer_detail.html', {'customer_form': form})  # 默认返回的时候,把form对象作为参数返回给前端页面

