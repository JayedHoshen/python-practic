#List values sum and average

def test_fnc(li):
    li_sum = sum(li)
    print("Sum is:",li_sum)
    
    avg = li_sum / (len(li))
    print("Average is:",avg)

my_list = [1,2,3,4,5,6,7,8,9,10]

test_fnc(my_list)
