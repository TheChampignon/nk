import random
number_of_bets = 1
depo = 3000
initial = 0
initial_persent = 0.10
percent = 1.82
#risk_persent = 0.274
win_lose_percent = 65
random.seed()
#lose_count = 0
#win_count = 0
days = 1
o=0
while o <=100:
    while days <= 10:
        #print("Day: ", days)
        while number_of_bets <= 10:


            initial = depo * initial_persent
            depo -= initial

            number_of_bets += 1
            if number_of_bets > 11:
                break
            win_lose = random.randrange(1, 101, 1)
            if win_lose <= 70:
                sum_of_win = initial * percent
                depo += sum_of_win
            #else:

        days += 1
        number_of_bets = 1

    o += 1
    days = 0
    print(depo)
    depo = 3000
    print()