import random
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
    print('-'*50)1
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
d1 = 0
d2 = 0

def conBet():
    money = monBox.get()
    bet = betBox.get()
    global t
    global b
    if money.isnumeric():
        t = int(money)
        monLab.configure(text=(f'Total Balance: ${money}'))
    elif money.isnumeric() == False:    
        monLab.configure(text='Money ammount is invalid')
        t = 0
    if bet.isnumeric():
        b = int(bet)
        betLab.configure(text=(f'Current Bet: ${bet}'))
    elif bet.isnumeric() == False:
        betLab.configure(text='Invalid bet')
        b = 0

def scrClr():
    #monBox.destroy()
    #betBox.destroy()
    conBut.destroy()
    nexBut.destroy()
    gamBut = tk.Button(gDice, text='Press to gamba', command=gamba, bg='black', fg='white')
    gamBut.pack()

def gamba():
    global money
    global bet
    money = monBox.get()
    bet = betBox.get()
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    global t
    global b
    if d1 == d2:
        t += (b*2)
        monLab.configure(text=f'Your Total Balance is ${t}')
        betLab.configure(text=f'Congrats! You Won ${(b*2)}!')
    else:
        t -= b
        monLab.configure(text=f'Your Total Balance is ${t}')
        betLab.configure(text=f'Better Luck Next Time! You Lost ${b}')
    print(d1,d2,t,b,end=', ')

conBut = tk.Button(gDice, text='Confirm', command=conBet, bg='black', fg='white')
conBut.pack()

nexBut = tk.Button(gDice, text='Next', command=scrClr, bg='black', fg='white')
nexBut.pack()

gDice.mainloop()







