#Prompt list:
numb_element = int(input('Enter number of element of the list: '))
list_n = []
for i in range(0,numb_element):
    tmp = input('Enter element NO {}: '.format(i+1))
    list_n.append(float(tmp))

#Find number in list nearest to average of all number in list: 
avg = sum(list_n)/len(list_n)
tmp = -1
nearest = []
for numb in list_n:
    if tmp == -1 :
        nearest.append(numb)
        tmp = abs(numb - avg)
    elif abs(numb - avg) < tmp:
        nearest.clear()
        nearest.append(numb)
        tmp = abs(numb - avg)
    elif abs(numb - avg) == tmp:
        nearest.append(numb)

print('Given list is {} \nAverage of the list is: {} \nNumber nearest average of the list is(are): {}'.format(list_n,avg,nearest))