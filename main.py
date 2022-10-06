# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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
        #print(throws)

    print(
        f'After throwing the dice {num_throws * num_repetitions} times, '
        f'{num_throws} times each {num_repetitions} times, '
        f'you would have won the bet {success}/{num_repetitions} times and lost {fail}/{num_repetitions} times')

    print(f'Your chance of winning should be approximately {success/num_repetitions*100}%')

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
        f'After throwing 2 dices {num_double_throws*num_repetitions} times, '
        f'{num_double_throws} times each {num_repetitions} times, '
        f'you would have won the bet {success}/{num_repetitions} times and lost {fail}/{num_repetitions} times')
    print(f'Your chance of winning should be approximately {success/num_repetitions*100}%')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    statistical_question1()
    statistical_question2()
