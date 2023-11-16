from random import randint
import tkinter as tk
import time

gDice = tk.Tk()
gDice.geometry('500x500')
gDice.configure(bg='black')
gDice.title('Get it Twisted')

'''
money = round(float(input('How much do you want to put in? ')),2)

while money > 0:
    try:
        bet = round(float(input('\nHow much do you want to bet?')),2)
        if bet > money:
            print('Your bet cant be grater than your balance!')
            continue
        else:
            money -= bet
    except ValueError:
        print('\nDo you want to quit?')
        q = input('Press "q" to quit')
        if q == 'q':
            break
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    diceModels(d1)
    diceModels(d2)
    if d1 == d2:
        money += bet*2
        print(f'\nCongrats! You won ${bet}! Balance: ${money}')
    else:
        print(f'\nToo bad. You lost ${bet}. Balance: ${money}')
    print('-'*50)1
'''

monLab = tk.Label(gDice, text='How much money would you like to enter?', bg='black', fg='white')
monLab.place(x=100, y=100)

monBox = tk.Entry(gDice, bg='black', fg='white')
monBox.place(x=100, y=150)

betLab = tk.Label(gDice, text='How much do you want to bet?', bg='black', fg='white')
betLab.place(x=100, y=200)

betBox = tk.Entry(gDice, bg='black', fg='white')
betBox.place(x=100, y=250)

money = 0
bet = 0

def conBet():
    bet = betBox.get()
    money = monBox.get()
    global t
    global b
    if money.isnumeric():
        t = int(money)
        monLab.configure(text=(f'Total Balance: ${money}'))
        if bet.isnumeric():
            b = int(bet)
            betLab.configure(text=(f'Current Bet: ${bet}'))
            dicBut.place(x=200, y=300)
        elif bet.isnumeric() == False:
            betLab.configure(text='Invalid bet')
            b = 0
    elif money.isnumeric() == False:    
        monLab.configure(text='Money ammount is invalid')
        t = 0
        if bet.isnumeric() == False:
            betLab.configure(text='Invalid bet')
            b = 0
        elif bet.isnumeric():
            b = int(bet)
            betLab.configure(text=(f'Current Bet: ${bet}'))

def backOut():
    rollBut.destroy()
    monBox.place(x=100, y=150)
    betBox.place(x=100, y=250)
    conBut.place(x=100, y=300)
    #dicBut.pack()

def scrClr():
    global rollBut
    global bacBut
    monBox.destroy()
    betBox.destroy()
    conBut.destroy()
    dicBut.destroy()
    rollBut = tk.Button(gDice, text='Roll Dice', command=diceRoll, bg='black', fg='white')
    rollBut.place(x=200, y=300)
    bacBut = tk.Button(gDice, text='Back Out', command=backOut, bg='black',fg='white')
    bacBut.place(x=200, y=350)

def diceRoll():
    global money
    global t
    global b
    
    d1 = randint(1,6)
    time.sleep(0.03)
    d2 = randint(1,6)
    time.sleep(0.002)
    d3 = randint(1,6)
    time.sleep(0.0001)
    d4 = randint(1,6)
    
    if d1 == d2:
        if d3 != d4:
            t += (b)
            monLab.configure(text=f'Your Total Balance is ${t}')
            betLab.configure(text=f'Congrats! You Won ${(b)}!')
        else:
            monLab.configure(text=f'Your Total Balance is ${t}')
            betLab.configure(text=f"It's a draw! Re-Roll? Bet: ${(b)}")
    elif d3 == d4:
        t -= b
        monLab.configure(text=f'Your Total Balance is ${t}')
        betLab.configure(text=f'Better Luck Next Time! You Lost ${b}')
    else:
        monLab.configure(text=f'Your Total Balance is ${t}')
        betLab.configure(text=f"It's a draw! Re-Roll? Bet: ${(b)}")
    print(d1,d2,d3,d4,t,b,end=', ')


    

conBut = tk.Button(gDice, text='Confirm', command=conBet, bg='black', fg='white')
conBut.place(x=100, y=300)

dicBut = tk.Button(gDice, text='Dice Rolling', command=scrClr, bg='black', fg='white')

gDice.mainloop()

'''

Need to do:
    * Back Out Button
    * Different games
    * Animations/ Pictures
    * Send to start if money = 0
    * 
    

'''
