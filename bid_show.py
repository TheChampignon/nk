#import random

DEPO = 0
IN_DEPO = 0.4
BETS_IN_DAY = 10
INIT_PERCENT = 0.1
WIN_PERCENT = 1.82
ROUND = 1# None
# первая ставка 10% от депо. При выигрыше, она полностью возвращается в депо, а 82% выигранного продолжает крутиться
# в следующей ставке


def bid_initiate(depo, init_percent=0.1):

    initial_bid = depo * init_percent

    if initial_bid < 30:
        initial_bid = 30

    return round(initial_bid, ROUND)
# W L W L W L W L W L
'''
350 962  2649 7299  + 20118 55456
450 1239 3413 9404  + 25922 71457
580 1596 4397 12117 + 33401 92075
747 2056 5665 15613 + 43038 118642
962 2649 7299 20118 + 55456 152874
'''
# L L L W W W L W W L
'''
350 431 504 590 + 720 843
374 448 524 614 + 749 877
396 466 545 639 + 779 912
415 485 567 665 + 810 949
431 504 590 692 + 843 987


w l w w l l w l l w  w 50/l 50
w l w w l l w l w w  w 60/l 40
l w w l l l w w w l  w 60/l 40
l w l w l l l w w l  w 40/l 60
w w w l l l w l w l  w 50/l 50
l w w l l l w w w l  w 50/l 50
w w l l w w w w w l  w 70/l 30
l w w w l w w l w l  w 60/l 40
350 403 554 576 556 590 734 999
1377
'''
'''
w w l l l l w l w l  w 40/l 60
l l w w w l l w l l  w 40/l 60
l 
350 256 114 
'''


def money_management(depo, win_percent=1.80, in_depo=0.4, bets_in_day=10,
                     fixed_init_bid=0):

    print('Day depo start: ', depo)

    initial_bid = bid_initiate(depo, INIT_PERCENT)
    depo -= initial_bid
    lose_count = 0

    for i in range(1, bets_in_day + 1):

        print()
        print('step: ', i)
        print('initial bet on that step: ', initial_bid)

        win_lose = int(input('Enter your result (WIN = 1, LOSE = 2): '))

        if win_lose == 1:
            print('WIN')

            sum_of_win = initial_bid * win_percent

            print('sum that you win when bet: ', sum_of_win)

            value_to_depo = sum_of_win * in_depo
            depo += value_to_depo
            sum_of_win -= value_to_depo

            if fixed_init_bid == 0:
                initial_bid = round(sum_of_win, ROUND)
                depo += sum_of_win - initial_bid
            if i == bets_in_day:
                depo += initial_bid

            lose_count = 0

            print('money that go to depo: ', value_to_depo+(sum_of_win-initial_bid))
            print('depo: ', depo)

        else:
            print('LOSE')

            if 1 <= lose_count:
                depo -= initial_bid

            print('sum you lose: ', initial_bid)
            print('depo: ', depo)

            initial_bid = bid_initiate(depo, INIT_PERCENT)
            lose_count += 1
    print()
    print()
    print('Thats all duuude! Go rest!')
    return depo

DEPO = float(input('Enter your depo: '))

print('Your depo at the end of daytrade:', money_management(DEPO, WIN_PERCENT, IN_DEPO, BETS_IN_DAY))