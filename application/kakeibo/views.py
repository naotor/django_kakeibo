from django.views import generic
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Category, Kakeibo
from .forms import KakeiboForm

from django.db.models import Sum

import calendar

class KakeiboListView(generic.ListView):
    template_name = 'kakeibo/kakeibo_list.html'
    model = Kakeibo

    def queryset(self):
        return Kakeibo.objects.all()


class KakeiboCreateView(generic.CreateView):
    template_name = 'kakeibo/kakeibo_form.html'
    model = Kakeibo
    form_class = KakeiboForm
    success_url = reverse_lazy('kakeibo:create_done')


def create_done(request):
    template_name = 'kakeibo/create_done.html'
    return render(request, template_name)


class KakeiboUpdateView(generic.UpdateView):
    template_name = 'kakeibo/kakeibo_form.html'
    model = Kakeibo
    form_class = KakeiboForm
    success_url = reverse_lazy('kakeibo:update_done')


def update_done(request):
    template_name = 'kakeibo/update_done.html'
    return render(request, template_name)


class KakeiboDeleteView(generic.DeleteView):
    template_name = 'kakeibo/delete_confirm.html'
    model = Kakeibo
    success_url = reverse_lazy('kakeibo:delete_done')


def delete_done(request):
    template_name = 'kakeibo/update_done.html'
    return render(request, template_name)


def show_circle_chart(request):
    template_name = 'kakeibo/show_circle_chart.html'
    category_dict = {}

    # すべての金額の合計を求める
    kakeibo_data = Kakeibo.objects.all()
    total = 0
    for item in kakeibo_data:
        total += item.money

    # すべてのカテゴリ名を取得する
    category_data = Category.objects.all()
    category_list = []
    for item in category_data:
        category_list.append(item.category_name)

    # カテゴリごとの合計金額を求める
    for i, item in enumerate(category_list):
        category_total = Kakeibo.objects.filter(category__category_name=category_list[i])\
            .aggregate(sum=Sum('money'))['sum']

        if category_total != None:
            ratio = int((category_total / total) * 100)
            category_dict[item] = ratio
        else:
            ratio = 0
            category_dict[item] = ratio

    return render(request, template_name, {
        'category_dict': category_dict,
    })


def show_linear_chart(request):
    template_name = 'kakeibo/show_linear_chart.html'
    parameters = {}

    # すべての家計簿データを取得する
    kakeibo_data = Kakeibo.objects.all()

    # すべてのカテゴリ名を取得する
    category_list = []
    category_data = Category.objects.all().order_by('-category_name')
    for item in category_data:
        category_list.append(item.category_name)

    parameters['category_list'] = category_list

    # 家計簿データから日付ラベル(日を除く)を取得する
    date_list = []
    for i in kakeibo_data:
        date_list.append((i.date.strftime('%Y/%m/%d')[:7]))

    # 日付ラベルから重複を除く
    x_label = sorted(set(date_list))
    parameters['x_label'] = x_label

    # 月ごと、かつカテゴリごとの合計金額データセットを取得する
    monthly_sum_data = []
    for i in range(len(x_label)):
        year, month = x_label[i].split("/")
        month_range = calendar.monthrange(int(year), int(month))[1]

        first_date = year + '-' + month + '-' + '01'
        last_date = year + '-' + month + '-' + str(month_range)

        total_of_month = Kakeibo.objects.filter(date__range=(first_date, last_date))
        category_total = total_of_month.values('category').annotate(total_price=Sum('money'))

        for j in range(len(category_total)):
            money = category_total[j]['total_price']
            category = Category.objects.get(pk=category_total[j]['category'])
            monthly_sum_data.append([x_label[i], category.category_name, money])

    # 月ごと、かつカテゴリごとの合計金額データを生成する
    matrix_list = []
    for item_label in x_label:
        for item_category in category_list:
            matrix_list.append([item_label, item_category, 0])

    for yyyy_mm, category, total in monthly_sum_data:
        for i, data in enumerate(matrix_list):
            if data[0] == yyyy_mm and data[1] == category:
                matrix_list[i][2] = total

    parameters['matrix_list'] = matrix_list

    #折れ線グラフのボーダーカラー色を設定する
    border_color_list=['254,97,132,0.8','54,164,235,0.8','0,255,65,0.8','255,241,15,0.8',\
                       '255,94,25,0.8','84,77,203,0.8','204,153,50,0.8','214,216,165,0.8',\
                       '33,30,45,0.8','52,38,89,0.8']
    border_color =[]
    for x,y in zip(category_list, border_color_list):
        border_color.append([x,y])

    parameters['border_color'] = border_color

    #折れ線グラフの背景色を設定する
    background_color_list=['254,97,132,0.5','54,164,235,0.5','0,255,65,0.5','255,241,15,0.5',\
                           '255,94,25,0.5','84,77,203,0.5','204,153,50,0.5','214,216,165,0.5'\
                           '33,30,45,0.5','52,38,89,0.5']
    background_color =[]
    for x,y in zip(category_list, background_color_list):
        background_color.append([x,y])

    parameters['background_color'] = background_color

    return render(request, template_name, parameters)