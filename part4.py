'''
Представлен список чисел. Определить элементы списка,
не имеющие повторений. Сформировать итоговый массив чисел,
соответствующих требованию. Элементы вывести
в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
'''

from itertools import permutations
from itertools import repeat
from itertools import combinations
my_list = [8, 5, 4, 5, 8, 5, 3, 5, 4, 2]
new = [el for el in my_list if my_list.count(el)==1]
print(new)