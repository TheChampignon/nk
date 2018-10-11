#import random


class MoneyManagement():
    DEPO = 0
    IN_DEPO = 0.4
    BETS_IN_DAY = 10
    INIT_PERCENT = 0.1
    WIN_PERCENT = 1.82
    ROUND = None
    # первая ставка 10% от депо. При выигрыше, она полностью возвращается в депо, а 82% выигранного продолжает крутиться
    # в следующей ставке

    def __init__(self, depo, in_depo, bets_in_day, init_percent, win_percent):
        self.depo = depo
        self.in_depo = in_depo
        self.bets_in_day = bets_in_day
        self.init_percent = init_percent
        self.win_percent = win_percent

    def bid_initiate(self, depo, init_percent=0.1):
        self.initial_bid = self.depo * self.init_percent

        if self.initial_bid < 30:
            self.initial_bid = 30

        return round(self.initial_bid, ROUND)

    def money_management(self, depo, win_percent=1.80, in_depo=0.4, bets_in_day=10, fixed_init_bid=0):

        print('Day depo start: ', depo)

        initial_bid = bid_initiate(depo, INIT_PERCENT)
        depo -= initial_bid
        lose_count = 0

        for i in range(1, bets_in_day + 1):

            print()
            print('step: ', i)
            print('initial bet on that step: ', initial_bid)

            if i > 1:
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