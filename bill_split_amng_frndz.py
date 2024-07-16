def bill_split(amount, friends):
    amunt = int(amount)
    frndz = int (friends) 
    subtotal = amunt * 0.2
    total =  (amunt + subtotal)/frndz
    print ('Total Bill Payable By Each: ',total)
amnt = input('Enter billable amount: ')
frnds = input('Enter number of friends: ')
bill_split(amnt,frnds)