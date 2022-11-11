from random import randint


def statistical_question1():
    num_throws = 4
    num_repetitions = 20000
    success = 0
    fail = 0
    for r in range(num_repetitions):
        throws = []
        for t in range(num_throws):
            throws.append(randint(1, 6))
        six_not_found = True
        for x in throws:
            if x == 6 and six_not_found:
                success += 1
                six_not_found = False
        if six_not_found:
            fail += 1
        # print(throws)

    print(
        f'After throwing the dice {num_throws * num_repetitions} times, '
        f'{num_throws} times each {num_repetitions} times, '
        f'you would have won the bet {success}/{num_repetitions} times and lost {fail}/{num_repetitions} times')

    print(f'Your chance of winning should be approximately {success / num_repetitions * 100}%')


def statistical_question2():
    num_double_throws = 24
    num_repetitions = 20000
    success = 0
    fail = 0
    for r in range(num_repetitions):
        doublethrows_per_rep = [[0] * 2 for i in range(num_double_throws)]
        for t in range(num_double_throws):
            for u in range(2):
                doublethrows_per_rep[t][u] = randint(1, 6)
        double_throw_not_found = True
        for t2 in range(num_double_throws):
            if doublethrows_per_rep[t2][0] == 6 and doublethrows_per_rep[t2][1] == 6 and double_throw_not_found:
                success += 1
                double_throw_not_found = False
        if double_throw_not_found:
            fail += 1
    print(
        f'After throwing 2 dices {num_double_throws * num_repetitions} times, '
        f'{num_double_throws} times each {num_repetitions} times, '
        f'you would have won the bet {success}/{num_repetitions} times and lost {fail}/{num_repetitions} times')
    print(f'Your chance of winning should be approximately {success / num_repetitions * 100}%')


def roulette_won():
    result = True
    number = randint(0, 36)
    if number <= 18:
        result = False
    return result


def roulette_strategy():
    num_games = 1000000
    balance = 0
    games_won = 0
    games_lost = 0
    bet = 1
    money_spent = 0
    negatives = []
    highest_loss = 0
    for r in range(num_games):
        balance -= bet
        if balance < 0:
            negatives.append(balance)
            if balance < highest_loss:
                highest_loss = balance
        if roulette_won():
            #print(f"won +{bet}")
            games_won += 1
            balance += 2*bet
            bet = 1
        else:
            #print(f"lost -{bet}")
            games_lost += 1
            bet = bet*2

        #print(f'balance: {balance}')
    print(f"spent:{money_spent}")
    print(f"lost: {games_lost}, won:{games_won}")
    print(f'your final balance is {balance}.')
    print(f"negatives: {negatives}")
    print(f"highest loss: {highest_loss}")


def zufallszahlen():
    num_numbers = 25
    smallest_number = 0
    biggest_number = 1000000
    numbers = []
    print("")
    for i in range(num_numbers):
        numbers.append(randint(smallest_number, biggest_number))
        print(numbers[i], end='\t')
        if (i+1)%5 == 0:
            print("")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #statistical_question1()
    #statistical_question2()
    #roulette_strategy()
    zufallszahlen()

