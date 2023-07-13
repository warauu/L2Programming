text = ''
count = 0
maxInput = 5

while text != '' and count < maxInput:

    #tells user how many inputs are left
    if count < 4:
        print('you have {} seats left'.format(maxInput-count))

    #warns the user that there is only one seat remaining
    else:
        print('**** There is only ONE seat left! ****')

        #Get details
        text = input('name: ')
        count += 1

if count == maxInput:
    print('You have sold all avaliable tickets')
else:
    print('You have sold {} tickets. \n There are {} places remaining'.format(count, maxInput - count))