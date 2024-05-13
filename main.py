import time 
def printBox(box):
    print('  0 1 2 ')
    for i in range (0, 3):
        for j in range (0, 3):
            if j == 0:
                print(i, box[i][j], end=' ')
            else:
                print(box[i][j], end=' ')
        print()
winner = "-"
box =  [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]

for k in range (1, 10):
    
    printBox(box)
    if k % 2 == 0:
        sign = "O"
    else: 
        sign = "X"


    possition_x = int(input("Вводи строку:"))
    possition_y = int(input("Вводи столбец:"))

    while box[possition_x][possition_y] != '-':
        print('Вводи коректные значения!')
        possition_x = int(input("Вводи строку:"))
        possition_y = int(input("Вводи столбец:"))

    if box[possition_x][possition_y] == '-':
        box[possition_x][possition_y] = sign

        for i in range(0, 3):
            counter = 0
            for j in range(0, 3):
                if box[i][j] == sign:
                    counter+=1
            if counter == 3:
                winner = sign
                break

        for i in range(0, 3):
            counter = 0
            for j in range(0, 3):
                if box[j][i] == sign:
                    counter+=1
            if counter == 3:
                winner = sign
                break
        counter = 0
        for i in range(0,3):
            
            if box[i][i]== sign:
                counter+=1
            if counter == 3:
                winner = sign
                break
        counter = 0
        for i in range(0,3):
            if box[i][2-i]== sign:
                counter+=1
            if counter == 3:
                winner = sign
                break
            
    
    if winner != '-':
        break
    



if winner == "X":
    print('''##########################################################################''')
    print('''##        X        X     W          W  IIIII  N     N  SSSSS            ##''')
    time.sleep(0.15)
    print('''##          X    X       W          W    I    NN    N  SS   s           ## ''')
    time.sleep(0.15)
    print('''##            XX         W          W    I    N N   N   SSS             ##''')
    time.sleep(0.15)
    print('''##            XX           W   W  W      I    N  N  N     SS            ##''')
    time.sleep(0.15)
    print('''##          X    X         W W  W W      I    N   N N  S   SS           ##''')
    time.sleep(0.15)
    print('''##        X        X       W      W    IIIII  N    NN   SSSS            ##''')
    time.sleep(0.15)
    print('''##########################################################################\n''')
    time.sleep(0.3)
elif winner =="O":
    
    print('''##########################################################################''')      
    print('''##          OOO        W          W    IIIII  N     N  SSSSS            ## ''') 
    time.sleep(0.15)
    print('''##         O   O       W          W      I    NN    N  SS    s          ## ''')
    time.sleep(0.15)
    print('''##         O   O       W          W      I    N N   N   SSS             ## ''')
    time.sleep(0.15)
    print('''##         O   O         W   W  W        I    N  N  N     SS            ## ''')
    time.sleep(0.15)
    print('''##         O   O         W W  W W        I    N   N N     SS            ## ''')
    time.sleep(0.15)
    print('''##          OOO          W      W      IIIII  N    NN   SSSS            ## ''')
    time.sleep(0.15)
    print('''##########################################################################\n''')
    time.sleep(0.3)


printBox(box)


