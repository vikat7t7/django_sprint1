from django.http import Http404
from django.shortcuts import render

posts = [
    {
        'id': 0,
        'location': 'Остров отчаянья',
        'date': '30 сентября 1659 года',
        'category': 'travel',
        'text': '''Наш корабль, застигнутый в открытом море
                страшным штормом, потерпел крушение.
                Весь экипаж, кроме меня, утонул; я же,
                несчастный Робинзон Крузо, был выброшен
                полумёртвым на берег этого проклятого острова,
                который назвал островом Отчаяния.''',
    },
    {
        'id': 1,
        'location': 'Остров отчаянья',
        'date': '1 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Проснувшись поутру, я увидел, что наш корабль сняло
                с мели приливом и пригнало гораздо ближе к берегу.
                Это подало мне надежду, что, когда ветер стихнет,
                мне удастся добраться до корабля и запастись едой и
                другими необходимыми вещами. Я немного приободрился,
                хотя печаль о погибших товарищах не покидала меня.
                Мне всё думалось, что, останься мы на корабле, мы
                непременно спаслись бы. Теперь из его обломков мы могли бы
                построить баркас, на котором и выбрались бы из этого
                гиблого места.''',
    },
    {
        'id': 2,
        'location': 'Остров отчаянья',
        'date': '25 октября 1659 года',
        'category': 'not-my-day',
        'text': '''Всю ночь и весь день шёл дождь и дул сильный
                порывистый ветер. 25 октября.  Корабль за ночь разбило
                в щепки; на том месте, где он стоял, торчат какие-то
                жалкие обломки,  да и те видны только во время отлива.
                Весь этот день я хлопотал  около вещей: укрывал и
                укутывал их, чтобы не испортились от дождя.''',
    },
]

# _posts = {post['id']: post for post in posts}


def index(request):
    template = 'blog/index.html'
    context = {'posts': reversed(posts)}
    return render(request, template, context)


def post_detail(request, id):
    template = 'blog/detail.html'
    if not isinstance(id, int):
        raise Http404(f'Параметр id {id} не найден')
    post = next(
        (post for post in posts
         if post['id'] == id),
        None)
    if post is None:
        raise Http404(f'Пост с id {id} не найден')
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    if category_slug is None:
        raise Http404(f'Категория с названием "{category_slug}" не найдена.')
    posts_in_category = [
        post for post in posts
        if post['category'] == category_slug
    ]
    posts_in_category.reverse()
    context = {
        'category_slug': category_slug,
        'posts': posts_in_category,
    }
    return render(request, template, context)
