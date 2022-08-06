from time import sleep


class SingleCard:
    def __init__(self, card_suite, card_rank):
        self.card_suite = card_suite
        self.card_rank = card_rank


class CardSet:
    def __init__(self, dek: list):
        self.dek = dek

    def drop_random(self):
        from random import randint
        return self.dek.pop(randint(0, len(self.dek) - 1))

    def card_add(self, card_added):
        self.dek.append(card_added)

    def points(self):
        result = 0
        aces_total = 0
        for card in self.dek:
            result += card_points.get(card.card_rank)
            if card.card_rank == 'A':
                aces_total += 1
        for _ in range(aces_total):
            if result > 21:
                result -= 10
            else:
                break
        return result


def print_table(dealer: list, player: list, hidden=True):
    print('\n' * 10)
    print('Dealers hand:')
    print('   ___ ' * len(dealer))
    line_2 = ''
    line_3 = ''
    first_card = True
    for current_card in dealer:
        if hidden and first_card:
            line_2 += '  |   |'
            line_3 += '  |   |'
            first_card = False
        else:
            line_2 += f'  | {current_card.card_rank} |'
            line_3 += f'  | {current_card.card_suite} |'
    print(line_2)
    print(line_3)
    print('  |___|' * len(dealer))
    print('\n' * 3)

    print('Players hand:')
    print('   ___ ' * len(player))
    line_2 = ''
    line_3 = ''
    for current_card in player:
        line_2 += f'  | {current_card.card_rank} |'
        line_3 += f'  | {current_card.card_suite} |'
    print(line_2)
    print(line_3)
    print('  |___|' * len(player))


def one_more_time():
    again = None
    while again not in ['1', '2']:
        print('Continue?')
        again = input('1 - Yes, 2 - No: ')
    return again == '1'


def get_integer():
    idiot = True
    while idiot:
        number = input('Input number: ')
        try:
            number = int(number)
        except:
            pass
        else:
            idiot = False
    else:
        print('Thank you!')
    return number


# Players balance:
print('Input your start balance')
start_balance = get_integer()


# Creating full dek list:
card_suits = ['♣', '♦', '♥', '♠']
card_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
card_points = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10,
               'Q': 10, 'K': 10, 'A': 11}
dek_full = []
for rank in card_ranks:
    for suite in card_suits:
        dek_full.append(SingleCard(suite, rank))

balance = start_balance
one_more_game = True
while one_more_game and balance > 0:
    print('Input bet')
    bet = get_integer()

    current_dek = CardSet(dek_full)
    dealers_hand = CardSet([])
    players_hand = CardSet([])

    for _ in range(2):
        dealers_hand.card_add(current_dek.drop_random())
        players_hand.card_add(current_dek.drop_random())

    print(dealers_hand.points())
    print_table(dealers_hand.dek, players_hand.dek)

    one_more_card = one_more_time()
    while one_more_card and players_hand.points() <= 21:
        players_hand.card_add(current_dek.drop_random())
        print_table(dealers_hand.dek, players_hand.dek)
        if players_hand.points() <= 21:
            one_more_card = one_more_time()

    print_table(dealers_hand.dek, players_hand.dek, False)

    if players_hand.points() > 21:
        print('Bust!')
    else:
        while dealers_hand.points() <= 17 or dealers_hand.points() <= players_hand.points():
            sleep(2.5)
            dealers_hand.card_add(current_dek.drop_random())
            print_table(dealers_hand.dek, players_hand.dek, False)
    print('Players points:', players_hand.points())
    print('Dealers points:', dealers_hand.points())

    if players_hand.points() > 21:
        print('Dealer win!')
        balance -= bet
    elif dealers_hand.points() > 21:
        print('Player win')
        print('Congratulations!')
        balance += bet
    elif players_hand.points() == dealers_hand.points():
        print('Dead heat')
    # elif players_hand.points() > dealers_hand.points():
    #     print('Player win')
    #     print('Congratulations!')
    #     balance += bet
    else:
        print('Dealer win!')
        balance -= bet

    if balance <= 0:
        one_more_game = False
    else:
        print('Current balance =', balance)
        one_more_game = one_more_time()

print('Thank you!')
print('Start balance =', start_balance)
print('Current balance =', balance)
