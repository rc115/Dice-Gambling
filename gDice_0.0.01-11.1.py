#import random
import tkinter as tk

gDice = tk.Tk()
gDice.geometry('500x500')
gDice.configure(bg='black')

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
    print('-'*50)
'''

monLab = tk.Label(gDice, text='How much money would you like to enter?', bg='black', fg='white')
monLab.pack()

monBox = tk.Entry(gDice, bg='black', fg='white')
monBox.pack()

betLab = tk.Label(gDice, text='How much do you want to bet?', bg='black', fg='white')
betLab.pack()

betBox = tk.Entry(gDice, bg='black', fg='white')
betBox.pack()

money = 0
bet = 0

mT = False
bT = False

def conBet():
    money = monBox.get()
    bet = betBox.get()
    if money.isnumeric():
        money = int(money)
        monLab.configure(text=(f'Total Balance: ${money}'))
        mT = True
    elif money.isnumeric() == False:    
        monLab.configure(text='Money ammount is invalid')
        mT = False
    if bet.isnumeric():
        bet = int(bet)
        betLab.configure(text=(f'Current Bet: ${bet}'))
        bT = True
    elif bet.isnumeric() == False:
        betLab.configure(text='Invalid bet')
        bT = False

conBut = tk.Button(gDice, text='Confirm', command=conBet, bg='black', fg='white')
conBut.pack()

if mT and bT:
    monLab.delete('all')
    monBox.delete('all')
    betLab.destroy()
    betBox.delete('all')
elif mT == False:
    print('Fix')
elif bT == False:
    print('Fix')


gDice.mainloop()







