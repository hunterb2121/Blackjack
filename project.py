import random
import sys

from card import Card


def main():
    # print the welcome page
    welcome()
    # create the main deck
    deck = create_deck()
    # create empty lists for the dealer and player's hands
    player_hand = list()
    dealer_hand = list()
    # deal te first hand, print it, then check if the player or dealer had a blackjack or busted
    deck, player_hand, dealer_hand = deal_first_hands(deck, player_hand, dealer_hand)
    print_hand(player_hand, dealer_hand)
    player_blackjack = check_for_blackjack(player_hand)
    dealer_blackjack = check_for_blackjack(dealer_hand)
    player_bust = check_for_bust(player_hand)
    dealer_bust = check_for_bust(dealer_hand)
    # deal with conditions if the player or dealer busted or had a blackjack
    if player_blackjack:
        win(player_hand, dealer_hand)
    if dealer_blackjack and player_blackjack != True:
        lose(player_hand, dealer_hand)
    if player_bust:
        lose(player_hand, dealer_hand)
    if player_bust and dealer_bust:
        tie(player_hand, dealer_hand)
    if player_bust == False and dealer_bust:
        win(player_hand, dealer_hand)
    print(f"Your Current Score: {calculate_score(player_hand)}")
    # main game loop that continues to run until the end of the game
    while True:
        # try to get the player to choose H or S and if not raise a ValueError and make them lose the game
        try:
            print("Hit (H) or Stay (S)")
            h_or_s = input("> ").lower()
            # deal with player choosing to hit
            if h_or_s == "h":
                player_hand, dealer_hand, deck = hit(player_hand, dealer_hand, deck)
                print(f"Your Current Score: {calculate_score(player_hand)}")
            # deal with player choosing to stay
            elif h_or_s == "s":
                player_hand, dealer_hand, deck = dealer_turn(
                    player_hand, dealer_hand, deck
                )
                # deal with the outcomes of the game
                outcomes(player_hand, dealer_hand)
            else:
                raise ValueError
        except ValueError:
            print("Invalid Command. You forfeit the game.")
            lose()


# draw ASCII art of each card in a hand in a row
def draw_card(hand):
    # quit if there is no hand
    if not hand:
        return

    # create a dictionary for each symbol and assign to the proper suit
    suit_symbols = {"Spades": "♠", "Clubs": "♣", "Hearts": "♥", "Diamonds": "♦"}

    # create a list of empty lists to store each string in
    line_lists = [list() for _ in range(7)]

    # go through each card in the hand
    for card in hand:
        # ASCII art
        back_of_card = [
            "┌─────────┐",
            "|    *    |",
            "|    *    |",
            "|    *    |",
            "|    *    |",
            "|    *    |",
            "└─────────┘",
        ]

        front_of_card_not_ten = [
            "┌─────────┐",
            f"| {card.face}       |",
            f"|    {suit_symbols[card.suit]}    |",
            "|         |",
            f"|    {suit_symbols[card.suit]}    |",
            f"|       {card.face} |",
            "└─────────┘",
        ]

        front_of_card_ten = [
            "┌─────────┐",
            f"| {card.face}      |",
            f"|    {suit_symbols[card.suit]}    |",
            "|         |",
            f"|    {suit_symbols[card.suit]}    |",
            f"|      {card.face} |",
            "└─────────┘",
        ]

        # determine which card face is going to be used
        if card.hidden:
            card_face = back_of_card
        elif card.face != "10":
            card_face = front_of_card_not_ten
        else:
            card_face = front_of_card_ten

        # append each line of the card face to the corresponding list
        for i in range(7):
            line_lists[i].append(card_face[i])

    # print each list in the line list
    for line_list in line_lists:
        print("  ".join(line_list))


# print each hand, both player and dealer
def print_hand(player_hand, dealer_hand):
    print("Dealer Hand:")
    draw_card(dealer_hand)
    print("Your Hand:")
    draw_card(player_hand)


# create the initial deck
def create_deck():
    # create an empty list to populate the deck
    deck = list()

    # create lists of suits, faces, and values
    suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
    faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    values = {
        "A": 11,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
    }

    # for each suit and each face create a card that is initially hidden
    for suit in suits:
        for face in faces:
            deck.append(Card(suit, face, values[face], True))

    # return the deck list
    return deck


# function to deal a card
def deal_card(deck):
    # randomly pick a card from the deck
    card = random.choice(deck)
    # remove said card from the deck
    deck = remove_card(deck, card)
    # return the card and deck
    return card, deck


# function to remove cards from th deck
def remove_card(deck, card):
    deck.remove(card)
    return deck


# calculate the score of a hand
def calculate_score(hand):
    # empty variables for total score and number of aces
    total = 0
    aces = 0

    # for each card in the hand add that value to the total
    for card in hand:
        total += card.value
        # if the card is an ace add 1 to the aces variable
        if card.value == 11:
            aces += 1

    # while the score of the hand is over 21 and there are still aces
    while total > 21 and aces:
        # remove 10 from the total to make the ace = 1 and remove one from the aces
        total -= 10
        aces -= 1

    # return the total
    return total


# check a hand for blackjack where the score of the hand is 21
def check_for_blackjack(hand):
    if calculate_score(hand) == 21:
        return True
    else:
        return False


# check a hand for a bust where the score of the hand is over 21
def check_for_bust(hand):
    if calculate_score(hand) > 21:
        return True
    else:
        return False


# determine the winner based off score if no blackjack or bust
def determine_winner(player_score, dealer_score):
    winner = None

    if player_score > dealer_score:
        winner = "P"
    elif player_score < dealer_score:
        winner = "D"
    else:
        winner = "T"

    return winner


# deal the first hand
def deal_first_hands(deck, player_hand, dealer_hand):
    # deal the cards and reassign the deck to update it and remove the old card
    card1, deck = deal_card(deck)
    card2, deck = deal_card(deck)
    card3, deck = deal_card(deck)
    card4, deck = deal_card(deck)
    # set all cards to be visible except the dealer's first card
    card1.hidden = False
    card3.hidden = False
    card4.hidden = False
    # extend the list to add the cards in there
    player_hand.extend([card1, card3])
    dealer_hand.extend([card2, card4])
    # return the updated deck and hands
    return deck, player_hand, dealer_hand


# function to define what happens when the player decides to hit
def hit(player_hand, dealer_hand, deck):
    # get a card, set it to be visible, and append it to the hand
    card, deck = deal_card(deck)
    card.hidden = False
    player_hand.append(card)

    # print the hands out
    print_hand(player_hand, dealer_hand)

    # check for blackjack or bust and if either happens make the player win or lose
    if check_for_blackjack(player_hand):
        win(player_hand, dealer_hand)
    if check_for_bust(player_hand):
        lose(player_hand, dealer_hand)

    # return the hands and deck
    return player_hand, dealer_hand, deck


# function to define the dealers turn (happens when the player chooses to stay with their hand)
def dealer_turn(player_hand, dealer_hand, deck):
    # while the score of the dealer's hand is less than 17 keep drawing cards like how they do in casinos
    while calculate_score(dealer_hand) < 17:
        # get a card, set it to be visible, and append it to the hand
        card, deck = deal_card(deck)
        card.hidden = False
        dealer_hand.append(card)

        # print the hands out
        print_hand(player_hand, dealer_hand)

        # check for blackjack or bust and if either happens make the dealer win or lose
        if check_for_blackjack(dealer_hand):
            lose(player_hand, dealer_hand)
        if check_for_bust(dealer_hand):
            win(player_hand, dealer_hand)

    # return the hands and deck
    return player_hand, dealer_hand, deck


# determine outcomes and choose whether the player wins, loses, or ties based off final scores
def outcomes(player_hand, dealer_hand):
    # get scores for player and dealer hands
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    # set a varable to determine the winner
    winner = determine_winner(player_score, dealer_score)

    # decide outcome based on winner
    if winner == "P":
        win(player_hand, dealer_hand)
    elif winner == "D":
        lose(player_hand, dealer_hand)
    elif winner == "T":
        tie(player_hand, dealer_hand)


# function to print the welcome screen
def welcome():
    print("============================================")
    print("          Welcome to the game of            ")
    print("                 Blackjack                  ")
    print("============================================")


# function for printing the lose screen
def lose(player_hand, dealer_hand):
    # set first dealer card to visible
    for card in dealer_hand:
        card.hidden = False

    # print the final hands and scores
    print_hand(player_hand, dealer_hand)
    print("Player Total: ", calculate_score(player_hand))
    print("Dealer Total: ", calculate_score(dealer_hand))

    # lose graphic
    print("============================================")
    print("                  You Lose                  ")
    print("                  Game Over                 ")
    print("============================================")

    # exit the program after the game
    sys.exit()


# function for printing the win screen
def win(player_hand, dealer_hand):
    # set first dealer card to visible
    for card in dealer_hand:
        card.hidden = False

    # print the final hands and scores
    print_hand(player_hand, dealer_hand)
    print("Player Total: ", calculate_score(player_hand))
    print("Dealer Total: ", calculate_score(dealer_hand))

    # win graphic
    print("============================================")
    print("                   You Win                  ")
    print("                   Congrats                 ")
    print("============================================")

    # exit the program after the game
    sys.exit()


# function for printing the tie screen
def tie(player_hand, dealer_hand):
    # set first dealer card to visible
    for card in dealer_hand:
        card.hidden = False

    # print the final hands and scores
    print_hand(player_hand, dealer_hand)
    print("Player Total: ", calculate_score(player_hand))
    print("Dealer Total: ", calculate_score(dealer_hand))

    # tie graphic
    print("============================================")
    print("                  You Tied                  ")
    print("============================================")

    # exit the program after the game
    sys.exit()


if __name__ == "__main__":
    main()