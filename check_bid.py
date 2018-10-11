dep = float(input())
procent_profit = 1.80
'''
min_bid = 0
for i in range (1,9):
    min_bid = dep/2**i
    print(min_bid)
min_bid = dep/2**9
summ = 0
win_bid = 0
curr_bid = 0
total_bid = 0
for i in range (1,9):
    curr_bid = min_bid*(2**i)
    total_bid += min_bid*(2**i)
    win_bid = curr_bid*procent_profit
    result_win_bid = win_bid - total_bid

    print(i,":",curr_bid,";",win_bid,":",result_win_bid)
'''
day = 1
save = 8

#while day != 20:
    #bid_count = 5
    #while bid_count != -1:
last_bid = 0
lost_bid = 0
summ = dep
for i  in range(1,save):
     last_bid = summ/procent_profit
     summ -= last_bid
     #print(i,":",last_bid)
     min_win_bid = last_bid*procent_profit - last_bid
last_bid = 0
lost_bid = 0
summ = dep
total_bid = 0
for i  in range(1,save):
     last_bid = (summ + min_win_bid)/procent_profit
     summ -= last_bid
     total_bid += last_bid
     win_bid = last_bid*procent_profit
     result_win_bid = win_bid - last_bid - summ
     print(i,":",last_bid,":",win_bid,":",result_win_bid)
     #dep += result_win_bid
     #bid_count -= 1
print(total_bid)
    #print()



   # day += 1




