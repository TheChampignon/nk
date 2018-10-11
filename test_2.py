import random


DEPO = 350
INIT_PERCENT = 0.1
WIN_PERCENT = 1.82
IN_DEPO = 0.40
WIN_RATE = 60
o=0
CUP = 20000*60
pocket = 0
total_avr = float(0)
BETS_IN_DAY = 15
DAYS_TRADE = 20
initial = 35


def bid_initiate(depo, init_percent=0.1):

    initial_bid = depo * init_percent

    if initial_bid < 30:
        initial_bid = 30

    return initial_bid


def money_management(depo, win_percent=1.80, win_rate=60, in_depo=0.4, bets_in_day=10,
                     fixed_init_bid=0):

    random.seed()

    print('Day depo start: ', depo)

    initial_bid = bid_initiate(depo)
    depo -= initial_bid
    lose_count = 0

    for i in range(1, bets_in_day + 1):

        print()
        print('step: ', i)

        win_lose = random.randrange(1, 101, 1)

        if win_lose <= win_rate:
            print('WIN')
            print('initial bet on that step: ', initial_bid)

            sum_of_win = initial_bid * win_percent

            print('sum that you win when bet: ', sum_of_win)

            value_to_depo = sum_of_win * in_depo
            depo += value_to_depo
            sum_of_win -= value_to_depo

            if fixed_init_bid == 0:
                initial_bid = sum_of_win

            if i == bets_in_day:
                depo += initial_bid

            lose_count = 0

            print('money that go to depo: ', value_to_depo)
            print('depo: ', depo)

        else:
            print('LOSE')
            print('initial bet on that step: ', initial_bid)

            if 1 <= lose_count:
                depo -= initial_bid

            print('sum you lose: ', initial_bid)
            print('depo: ', depo)

            initial_bid = bid_initiate(depo)
            lose_count += 1

            # print('initial bet on that step: ', initial_bid, 'sum you lose ', initial_bid, 'depo: ', depo, end='\n')

    return depo


def days_trade(depo, days=10):

    day = 1

    while day <= days:
        print()
        print()
        print("Day ", day)

        depo = money_management(depo, win_rate=57, bets_in_day=5)

        day += 1

days_trade(DEPO, 5)



'''
while o <=100:
    while days <= day_trade:
        #print("Day: ", days)
        while number_of_bets <= bets:

            if cup < depo:
                vivod = (depo - cup)
                pocket += vivod
                depo -= vivod

            #initial = depo * initial_persent
            #depo -= initial

            
        #print("win count: ", win_count)
        #print("lose count: ", lose_count)

        #print("U results depo: ", depo)
        #print()
        days += 1
        number_of_bets = 1
        win_count = 0
        lose_count = 0

        #print()
    o += 1
    days = 1
    print("pocket: ", pocket, "depo: ", depo, "total summ: ", depo + pocket)
    total_avr += depo+pocket
    depo = 350
    pocket = 0
    print()
print(total_avr/100)
'''