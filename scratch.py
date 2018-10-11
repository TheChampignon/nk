procent_profit = 0.80
mounth_profit = float(70000)
min_bid_procent = 0.02
anti_lose_coeff = 2.5
day_in_mounth = 29.6

profit_in_day = mounth_profit/day_in_mounth
print("Day profit needed:", profit_in_day)

min_win_bid_requered = profit_in_day/procent_profit
print("Min wining bid needed:",min_win_bid_requered)

dep = min_win_bid_requered * 100
print("Min dep needed:",dep)

for win_bed in range(1,9):
    min_bid = min_win_bid_requered/win_bed
    dep = min_bid * 100
    print("For",win_bed,"bid requered min bid:",min_bid,"; and dep:",dep )

dep = 65000
min_bid = dep/2**8
win_bed = min_bid * procent_profit * 5

print(min_bid, win_bed)

min_bid = dep * min_bid_procent
summ = 0
curr_bid = 0
for i in range (0,12):
    if dep <= summ:
        break
    curr_bid = min_bid + curr_bid
    summ += curr_bid
    win_bed = summ - (summ * procent_profit)
    print(i,":",curr_bid,":",win_bed,":",summ)

