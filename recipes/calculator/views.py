from django.http import HttpResponse
from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },

    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def cook_book(request):
    context = {'recipe': {}}
    dish = request.path_info[1:-1]
    servings = request.GET.get("servings", 1)

    if servings == 1 or servings == None or not servings.isdecimal():
        context['recipe'] = DATA[dish]
    else:
        servings = int(servings)
        for ingredient, count in DATA[dish].items():
            context['recipe'][ingredient] = count * servings

    return render(request, 'calculator\index.html', context)