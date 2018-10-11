procent_profit = 1.80
save = 6
round_num = 0
d={}

save +=1

i = input("Enter Dep value: ")
i = i.replace(',','')
i = i.replace(' ','')
dep = float(i)

def min_bid(summ, save=8):
    summ = round(summ, round_num)
    for i in range(1,save):
        last_bid =  round(summ/procent_profit,round_num)
        summ -= last_bid
    min_win_bid = round((last_bid*procent_profit) - last_bid,round_num)
    return min_win_bid

def table_split(summ, min_win_bid, save=8):
    total_bid = 0
    #summ = round(summ / ass_count, round_num)
    for i in range(1,save):
        last_bid = round((summ + min_win_bid)/procent_profit,round_num)
        win_bid = round(last_bid*procent_profit,round_num)
        summ -= last_bid
        result_win_bid = round((win_bid - last_bid-summ),round_num)
        #print(i,":",last_bid,":",win_bid,":",result_win_bid)
        d.update({save-i:last_bid})
        total_bid += last_bid
    #print(round(total_bid,round_num))

win_count = 0
last_ass_count = 1
step_count = 0
multi = 1
ass_count = -1

table_split(dep,min_bid(dep,save),save)
print(d)

while win_count != "exit":
    for i in range(1,save+1):

        if win_count == ass_count:
            step_count = 0
            win_count = 0
            last_ass_count = 1
            multi = 1
            print("reset")
            break
        step_count = i
        curr_price = d.get(i)
        #if last_ass_count == 1:
        #    multi = 1
        print(curr_price)
        inp = input("Enter assets count: ")
        ass_count = int(inp)

        price = round(((curr_price/multi)*(last_ass_count-win_count))/ass_count,round_num)
        print(price)
        multi *= ass_count
        inp = input("Enter win count: ")
        win_count = int(inp)
        last_ass_count = ass_count
        if win_count == 0:
            last_ass_count = 1
            multi /=ass_count


