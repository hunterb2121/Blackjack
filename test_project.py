from project import Card, calculate_score, check_for_blackjack, check_for_bust, determine_winner

card1 = Card('Spades', '5', 5, False)
card2 = Card('Hearts', '10', 10, False)
card3 = Card('Diamonds', 'A', 11, False)
card4 = Card('Clubs', '6', 6, False)
card5 = Card('Spades', 'K', 10, False)
card6 = Card('Hearts', 'Q', 10, False)
card7 = Card('Diamonds', '2', 2, False)
card8 = Card('Clubs', '6', 6, False)

def test_calculate_score():
    assert(calculate_score([card1, card4])) == 11
    assert(calculate_score([card5, card6])) == 20
    assert(calculate_score([card7, card8, card2, card3])) == 19


def test_check_for_blackjack():
    assert(check_for_blackjack([card1, card2])) == False
    assert(check_for_blackjack([card5, card6, card3])) == True
    assert(check_for_blackjack([card5, card6, card8])) == False


def test_check_for_bust():
    assert(check_for_bust([card1, card2])) == False
    assert(check_for_bust([card5, card6, card3])) == False
    assert(check_for_bust([card5, card6, card8])) == True


def test_determine_winner():
    assert(determine_winner(15, 13)) == 'P'
    assert(determine_winner(13, 15)) == 'D'
    assert(determine_winner(13, 13)) == 'T'