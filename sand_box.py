import random
import matplotlib.pyplot as plt
import numpy as np


random.seed()

DEPO = 60000
IN_DEPO = 1 # % от выигрыша, который идет в депо
BETS_IN_DAY = 10
INIT_PERCENT = 1 # процент от депо, который является первоначальной ставкой
WIN_RATE = 70
WIN_PERCENT = 1.82
NUMBERS_OF_PROGON = 100

# первая ставка 10% от депо. При выигрыше, она полностью возвращается в вдепо, а 82% выигранного продолжает крутиться
# в следующей ставке


def bid_initiate(depo, init_percent=1):

    initial_bid = depo * init_percent * 0.01

    if initial_bid < 30:
        initial_bid = 30

    return initial_bid


def money_management(depo, win_percent=1.80, in_depo=1, bets_in_day=1, win_rate=1, init_percent=1,
                     fixed_init_bid=0):

    #print('Day depo start: ', depo)

    initial_bid = bid_initiate(depo, init_percent)
    depo -= initial_bid
    lose_count = 0

    for i in range(1, bets_in_day + 1):

        # print()
        # print('step: ', i)
        # print('initial bet on that step: ', initial_bid)

        win_lose = random.randrange(1, 101, 1)

        if win_lose <= win_rate:
            #print('WIN')


            sum_of_win = initial_bid * win_percent

            #print('sum that you win when bet: ', sum_of_win)

            value_to_depo = sum_of_win * in_depo * 0.01
            depo += value_to_depo
            sum_of_win -= value_to_depo

            if fixed_init_bid == 0:
                initial_bid = sum_of_win

            if i == bets_in_day:
                depo += initial_bid

            lose_count = 0

            #print('money that go to depo: ', value_to_depo+(sum_of_win-initial_bid))
            #print('depo: ', depo)

        else:
            #print('LOSE')

            if 1 <= lose_count:
                depo -= initial_bid

            #print('sum you lose: ', initial_bid)
            #print('depo: ', depo)

            initial_bid = bid_initiate(depo, init_percent)
            lose_count += 1
    #print()
    #print()
    #print('Thats all duuude! Go rest!')
    return depo
#d = {}
#key = 1




def generate_progon (numbers_of_progon=1):
    for i in range(10, 101, NUMBERS_OF_PROGON):
        INIT_PERCENT = i
        #print('INIT_PERCENT: ', INIT_PERCENT)
        #d[INIT_PERCENT] = {}
        for j in range(40, 101, NUMBERS_OF_PROGON):
            IN_DEPO = j
            #print('IN_DEPO: ', IN_DEPO)
            #d[INIT_PERCENT][IN_DEPO] = {}
            for k in range(70, 101, NUMBERS_OF_PROGON):
                WIN_RATE = k
                #d[INIT_PERCENT][IN_DEPO][WIN_RATE] = {}
                for l in range (100, 101, NUMBERS_OF_PROGON):
                    BETS_IN_DAY = l
                    #d[INIT_PERCENT][IN_DEPO][WIN_RATE][BETS_IN_DAY] = {}

                    file1 = open('INIT_PERCENT({0})_IN_DEPO({1})_WIN_RATE({2})_BETS_IN_DAY({3})'.format(INIT_PERCENT, IN_DEPO, WIN_RATE, BETS_IN_DAY), 'w')
                    count = 0
                    while count < 1000000:
                        value = money_management(DEPO, in_depo=IN_DEPO, bets_in_day=BETS_IN_DAY, win_rate=WIN_RATE, init_percent=INIT_PERCENT)
                    #if value < 0:
                    #    continue

                        opstr = str(value) + '\n'
                        file1.write(opstr)
                        count += 1
                    file1.close()
                BETS_IN_DAY = 0
            WIN_RATE = 0
        IN_DEPO = 0
#generate_progon(NUMBERS_OF_PROGON)

file1 = open('INIT_PERCENT(10)_IN_DEPO(40)_WIN_RATE(70)_BETS_IN_DAY(100)', 'r')
x = []
for element in file1.readlines():
    x.append(float(element))
num_bins = 100
n, bins, patches = plt.hist(x, num_bins, density=True, facecolor = 'red', alpha = 1)
plt.show()

#np.histogram(x, num_bins)
#n

