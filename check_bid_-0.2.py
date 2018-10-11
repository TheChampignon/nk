procent_profit = 1.80
save = 7
cur_count = 1

i = input()
i = i.replace(',','')
i = i.replace(' ','')
dep = float(i)
round_num = 0

def min_bid(summ, save=8):
    summ = round(summ / cur_count, round_num)
    for i in range(1,save):
        last_bid =  round(summ/procent_profit,round_num)
        summ -= last_bid
    min_win_bid = round((last_bid*procent_profit) - last_bid,round_num)
    return min_win_bid
def table_split(summ, min_win_bid, save=8):
    total_bid = 0
    summ = round(summ / cur_count, round_num)
    for i in range(1,save):
        last_bid = round((summ + min_win_bid)/procent_profit,round_num)
        win_bid = round(last_bid*procent_profit,round_num)
        summ -= last_bid
        result_win_bid = round((win_bid - last_bid-summ),round_num)
        print(i,":",last_bid,":",win_bid,":",result_win_bid)
        total_bid += last_bid
    print(round(total_bid,round_num))

table_split(dep,min_bid(dep,save),save)
table_split(dep+min_bid(dep,save),min_bid(dep+min_bid(dep,save),save),save)