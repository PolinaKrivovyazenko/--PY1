src = not False and True or False and not True
# result = True and True or False and False - избавились от отрицаний
# result = True or False - избавились от логического И
# result = True - избавились от логического Или
# TODO расписать упрощение выражения

result = True

print(src == result)
