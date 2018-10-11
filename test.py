import random


number_of_bets = 1
depo = 350
initial = 0
initial_persent = 0.10
percent = 1.82
risk_persent = 0.40
win_lose_percent = 60
random.seed()
lose_count = 0
win_count = 0
days = 1
o=0
cup = 20000*60
pocket = 0
total_avr = float(0)
bets = 15
day_trade = 20
initial = 35
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

            for i in range(1, bets+1):

                #print()
                #print("number of bets: ", number_of_bets)
                #print('step: ', i)
                #print('initial bet on that step: ', initial)
                number_of_bets += 1
                if number_of_bets > bets:
                    break
                win_lose = random.randrange(1, 101, 1)
                if win_lose <= win_lose_percent:
                    sum_of_win = initial * percent
                    #print('sum that you win when bet: ', sum_of_win)
                    risk = sum_of_win * risk_persent
                    depo += risk
                    sum_of_win -= risk
                    #initial = sum_of_win
                    #print('money that go to depo: ', risk)
                    #print('depo: ', depo)
                    win_count += 1
                    #number_of_bets += 1
                else:
                    #print('U lose')
                    lose_count += 1
                    #number_of_bets += 1
                    break
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