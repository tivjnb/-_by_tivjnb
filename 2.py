from itertools import product, permutations
'''
В общем и целом такая сложная программа здесь не всегда нужна, но иногда хреново обычной считается, да и ручками фу
Если её запомнить, то выходит иногда даже быстрее чем руками, а с повышением сложности задания программа всё та же
'''


def f(x, y, z, w):
    return ((x <= y) and (y <= w)) or (z == (x or y))


result = set()  # Для результата
for a in product([0, 1], repeat=7):  # repeat ставим по количеству неизвестных
    # Сюда мы переноси таблицу, вместо пропусков вставляем а-шки
    t = [
        (1, a[0], a[1], 1),
        (1, a[2], a[3], a[4]),
        (a[5], 1, a[6], 1)
    ]
    if len(set(t)) == len(t):  # Необходимо во избежание двух одинаковых строк в таблице
        '''
        Дальше неочевидный кусок, поэтому распишу поподробнее
        Цикл for перебирает все варианты расстановки наших букв
        Первая часть условия это список, состоящий из результатов работы функции, 
        на вход которой подается словарь в формате БУКВА:ЦИФРА 
        Буква из цикла for
        Цифра из t
        zip попарно соединяет их  dict(zip([a,b,c,d], [1,2,3,4])) => {a:1, b:2, c:3, d:4}
        ** нужен для того, чтобы подать переменные поименно, не по порядку
        вторая часть это результаты работы функции из таблицы
        '''
        for per in permutations('xyzw'):
            if [f(**dict(zip(per, r))) for r in t] == [0, 0, 0]:
                result.add(per)  # Результат добавляем в set
print(result)  # Вот и все, программа всегда одинаковая, придумывать ничего не надо
