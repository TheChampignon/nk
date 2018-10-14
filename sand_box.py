import random

random.seed()

DEPO = 60000                    # размер депозита (депо)
IN_DEPO = 1                     # % от выигрыша, который идет в депо
BETS_IN_DAY = 10                # количество сделок в день
INIT_PERCENT = 1                # процент от депо, который будет ставкой
WIN_RATE = 70                   # процент выйгрышей в выбранной торговой стратегии
WIN_PERCENT = 1.82              # процент выйгрыша предлагаемый торговой платформой
NUMBERS_OF_PROGON = 1           # шаг увеличения переменных IN_DEPO, BETS_IN_DAY, INIT_PERCENT, WIN_RATE для генерации
                                # результатов вычисляется по формуле 100/NUMBERS_OF_PROGON
COUNTMAX = 1000000              # количество вычислей с одним заданным набором параметров
                                # Предложения к обновлению: первая ставка 10% от депо. При выигрыше, она полностью
                                # возвращается в вдепо, а 82% выигранного продолжает крутиться в следующей ставке

                                # функция вычисления первой ставки: берется процент от депо (INIT_PERCENT), если ставка
                                # оказалась меньше 30, то берется в качестве ставки минимальное значение равное 30

def bid_initiate(depo, init_percent=1):

    initial_bid = depo * init_percent * 0.01

    if initial_bid < 30:
        initial_bid = 30

    return initial_bid

                                # функция симуляции торгов с заданными параметрами
                                # fixed_init_bid - переменная-опция если равна 0, то следующая ставка вычисляется из
                                # выйгрыша, если равна 1 то следующая ставка берется по проценту от депо (INIT_PERCENT)

def money_management(depo1, win_percent1=1.82, in_depo1=1, bets_in_day1=5, win_rate1=1, init_percent1=1,
                     fixed_init_bid1=0):

                                # инициация размер первой ставки

    initial_bid = bid_initiate(depo1, init_percent1)
    depo1 -= initial_bid
    lose_count = 0
                                # запуск симуляции торгов каждый проход цикла является одной ставкой коррелирует с
                                # с переменной BETS_IN_DAY

    for i in range(1, bets_in_day1 + 1):

                                # вычисляем вероятность выйгрыша

        win_lose = random.randrange(1, 101, 1)

                                # если вероятность выйгрыша меньше либо равна WIN_RATE, то считается выйгрышем, иначе
                                # проигрышем

        if win_lose <= win_rate1:

                                # высчитываем сумму выйгрыша

            sum_of_win = initial_bid * win_percent1

                                # процент от выйгрыша (IN_DEPO) возвращается в депо

            value_to_depo = sum_of_win * in_depo1 * 0.01
            depo1 += value_to_depo
            sum_of_win -= value_to_depo

                                # остаток будет следующей cтавкой, если fixed_init_bid равна 0 и если равна 1 то
                                # следующая ставка берется по проценту от депо (INIT_PERCENT)

            if fixed_init_bid1 == 0:
                initial_bid = sum_of_win
            else:
                depo1 += sum_of_win
                initial_bid = bid_initiate(depo1, init_percent1)
                depo1 -= initial_bid

            if i == bets_in_day1:
                depo1 += initial_bid

            lose_count = 0

        else:

            if 1 <= lose_count:
                depo1 -= initial_bid

            initial_bid = bid_initiate(depo1, init_percent1)
            lose_count += 1

    return depo1

def min_max_gap (dict1={}):
    min1 = dict1.get(1)
    max1 = dict1.get(1)
    #print(min)
    for key6 in dict1:
        if key6 == 0:
            continue
        #print(dict.get(key6))
        if dict1.get(key6) < min1:
            min1 = dict1.get(key6)
        elif dict1.get(key6) > max1:
            max1 = dict1.get(key6)
    return [min1, max1, (max1 - min1) / 100]

def hist (dict2={}, list=[]):
    min2 = float(list[0])
    max2 = float(list[1])
    gap = float(list[2])
    d3 = {}
    k1 = 1
    val = min2
    count1 = 0
    val_pre = 0
    if gap == 0:
        return [dict2.get(0), min2]
    while val < max2:
        val_pre = val
        val += gap

        for key1 in dict2:
            if key1 == 0:
                continue
            if val_pre <= dict2.get(key1) < val:
                count1 += 1
        d3.update({k1:count1})
        count1 = 0
        k1 += 1
    all_val = 0
    for key2 in d3:
        if d3.get(key2) > 0:
            all_val += d3.get(key2)

    #print(dict, list, d3, all_val)
    procent1 = 0
    while procent1 <= 5:
        key_del = 0
        min_value1 = 0
        for key4 in range(1, 101):
            if d3.get(key4) == None:
                continue
            else:
                min_value1 = d3.get(key4)
                key_del = key4
                break
        for key4 in d3:
            if d3.get(key4) < min_value1:
                min_value1 = d3.get(key4)
                key_del = key4
        if all_val == 0:
            procent1 = 5
        else:
            procent1 += (min_value1/all_val)*100
        if key_del == 0:
            continue
        else:
            del d3[key_del]
    key_value = 0
    for key5 in range(1, 101):
        if d3.get(key5) == None:
            continue
        else:
            key_value = key5
            break
    point = min2 + gap*key_value

    #print(point)
    return [dict2.get(0), point]




def generate_progon (depo2, countmax=100, win_percent2=1.82, bets_in_day2=5, fixed_init_bid2=0, numbers_of_progon=1):
    dict_rezult = {}
    list_temp = []
    d1 = {}
    for i in range(1, 101, numbers_of_progon):
        init_percent2 = i
        for j in range(1, 101, numbers_of_progon):
            in_depo2 = j
            #print(in_depo2)
            count = 0
            d1.update({0: ('IP{0}ID{1}'.format(init_percent2, in_depo2))})
            key0 = 1
            while count < countmax:
                value = money_management(depo2, in_depo1=in_depo2, win_percent1=WIN_RATE, init_percent1=init_percent2,
                                         fixed_init_bid1=fixed_init_bid2)
                d1.update({key0 : value})
                key0 += 1
                count += 1
            #print(d1)
            list_temp = hist(d1, min_max_gap(d1))
            print(list_temp[0])
            if list_temp[1] <= DEPO:
                continue
            else:
                print(list_temp)
                dict_rezult.update({list_temp[0]:list_temp[1]})

    return dict_rezult


dict_rez = generate_progon(DEPO, COUNTMAX, numbers_of_progon=NUMBERS_OF_PROGON)


for key7 in dict_rez:
    if dict_rez.get(key7) != None:
        min_value = dict_rez.get(key7)
        key_rez = key7
        break

for key8 in dict_rez:
    if dict_rez.get(key8) < min_value:
        min_value = dict_rez.get(key8)
        key_rez = key8

print(key_rez)
