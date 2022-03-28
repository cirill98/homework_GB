# 1 задание
nums = {'one': "Один",
        'two': "Два",
        'three': "Три",
        'four': "Четыре",
        'five': "Пять",
        'six': "Шесть",
        'seven': "Семь",
        'eight': "Восемь",
        'nine': "Девять",
        'ten': "Десять"
}
def num_translate(num):
    return nums.get(num)
print(num_translate("two"))

# 3 задание
# ("Иван", "Мария", "Петр", "Илья")
def tresaurus(*names):
    out_dict = dict()
    for name in names:
        out_dict.setdefault(name[0], [])
        out_dict[name[0]].append(name)
    return out_dict
print(tresaurus("Иван", "Мария", "Петр", "Илья"))



# 5 задание
import random
a = ["автомобиль", "лес", "огонь", "город", "дом"]
b = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
c = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
def get_jokes(num):
    """Function to return jokes. num (int) - count of jokes """
    joke_list = []
    for i in range(num):
        cur_a = random.choice(a)
        cur_b = random.choice(b)
        cur_c = random.choice(c)
        joke_list.append(f'{cur_a} {cur_b} {cur_c}')
    return joke_list
print(get_jokes(1))
print(get_jokes(2))

def get_jokes_adv(num, repeats=True):
    joke_list = []

    if not repeats:
        if num > min(len(a), len(b), len(c)):
            return 'No way'
        else:
            random.shuffle(a)
            random.shuffle(b)
            random.shuffle(c)
            for i in range(num):
                joke_list.append(f'{a[i]} {b[i]} {c[i]}')

    else:
        for i in range(num):
            cur_a = random.choice(a)
            cur_b = random.choice(b)
            cur_c = random.choice(c)
            joke_list.append(f'{cur_a} {cur_b} {cur_c}')
    return joke_list


print(get_jokes_adv(4, False))
print(get_jokes_adv(5, False))
print(get_jokes_adv(6, False))
