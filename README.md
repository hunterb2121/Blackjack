# Blackjack by Hunter Barnes
#### Video Demo: https://www.youtube.com/watch?v=QGyUwDPnzRk
#### Description:

This project is a simple game of Blackjack or 21. The object of the game is to get as close to 21 points as possible without going over. If the dealer gets closer to 21, they win. If you are closer to 21, you win. If you get 21, you win or tie if the dealer also has 21. If you both have the same score, you tie. If you or the dealer goes over 21, you immediately lose.

Each card has a certain value. The number cards all have their face value while each face card is worth 10. The Ace is the only exception. It is worth 11 unless you go over 21 in which case the Ace is counted as 1.

##### Card Values

* Ace: 11 or 1
* K: 10
* Q: 10
* J: 10
* 10: 10
* 9: 9
* 8: 8
* 7: 7
* 6: 6
* 5: 5
* 4: 4
* 3: 3
* 2: 2

I still want to add the ability to play the game again without having to run the program again.

#### Program Structure

There are two files in this program, the main file and the card file. The card file contains a single class for the card object. The main file contains all the game logic. The functions in the main file.

##### card.py

This file contains the Card object which has an initializer function requiring a Suit, Face, Value, and whether the card is hidden from player view or not. Each item has a getter and setter function in case those need to be called in the main file. There is also a string function to define what will output when a card is type cast to a string. This is no longer used and is a remnant of when I didn't include ASCII graphics. I never removed it in case it could come in handy later when adding more to the project.

##### main.py

This is the main program file which contains most of the logic. It requires 2 modules that come with Python - Random and Sys - as well as the Card object from card.py. There are 18 functions in the program including the main function. I'll go into each function in detail in a later section.

Each Function with a small description:
* main() - contains the main game loop
* draw_card(hand) - draw an ASCII depiction of each card in a hand
* print_hand(player_hand, dealer_hand) - print the dealer and player hand
* create_deck() - create a deck with 52 cards in it with Ace, King, Queen, Jack, 2-10
* deal_first_hands(deck, player_hand, dealer_hand) - deal 4 cards by calling the deal_card(deck) function and appending them to each hand
* deal_card(deck) - chose a random card with random.choice(deck) then removing the card by calling remove_card(deck, card)
* remove_card(deck, card) - remove the card from the deck using deck.remove(card) since deck is a list
* calculate_score(hand) - calculate the score by adding the value of each card to total score and accounting for Ace's, changing them from 11 to 1 when the total score hits 21
* check_for_blackjack(hand) - checks if total score is 21 by calling calculate_score(hand) and then returns True otherwise returns False
* check_for_bust(hand) - checks if total score is over 21 by calling calculate_score(hand) and then returns True otherwise returns False
* determine_winner(player_score, dealer_score) - checks if player_score is higher, lower, or the same as the dealer score
* hit(player_hand, dealer_hand, deck) - logic for when a player hits and draws a new card to add to the player_hand then checks for blackjack or bust
* dealer_turn(player_hand, dealer_hand, deck) - draws cards for the dealer until it hits at least 17
* outcomes(player_hand, dealer_hand) - determines the winner by calling calculate_score for the player and dealer then calls determine_winner to figure out who wins then it runs win(), lose(), or tie() to display the end game screen
* welcome() - an ASCII welcome screen
* lose(player_hand, dealer_hand) - prints the scores, then prints an ASCII game over screen, and then exits the program
* win(player_hand, dealer_hand) - prints the scores, then prints an ASCII win screen, and then exits the program
* tie(player_hand, dealer_hand) - prints the scores, then prints an ASCII game over screen, and then exits the program

#### Design Choices

There were a couple of choices I made with the design of the program that should be mentioned.
The first is the choice to move the Card object to a separate file. It was making the main file a little long, and it is normally best practice to keep objects separate from the main file.
The next is the choice of organizing the file. I have organized it with main at top like is best practice, having functions for printing the cards, creating the deck, dealing, and removing cards since they have to do with the cards. Then we go into calculating score, checking for blackjack, checking for bust, and determining the winner since they all have to do with scores and finding the winner. Then, it's to deal the first hand, when the player chooses to hit, the dealer's turn, and the outcomes since they all have to do with player choices and the main game logic. Last are the functions for the printing the beginning and ending screens.

#### Function Descriptions

1. draw_card(hand)
    * checks if there is a hand and if not returns
    * create a dictionary assigning the suit symbol for each suit
    * create a list of empty lists to hold each line of a card and then holds the same line for the next card in the hand
    * create a for loop for each card in a hand
    * has the ASCII art for each type of card
    * determine the card face that should be used
    * add the line for the card to the appropriate line list
    * print each line list so that the cards in the hand are printed next to each other
2. print_hand(player_hand, dealer_hand)
    * prints the dealer hand by calling draw_card(dealer_hand)
    * prints the player hand by calling draw_card(player_hand)
3. create_deck()
    * create an empty list to populate the deck
    * create a list with suit names
    * create a list for faces
    * create a dictionary to assign faces a certain value
    * go through each suit and each face for each suit and append a new Card with that suit, face, and value, marked as Hidden by defualt, to the deck
    * return the deck
4. deal_card(deck)
    * use random.choice to choose a random card from the deck
    * call the remove_card function to remove the card
    * return the card and deck
5. remove_card(deck, card)
    * remove the card from the deck
    * return the deck
6. calculate_score(hand)
    * create a total and aces variable to count the total score and number of aces
    * for each card in the hand add the value of the card to the total
    * add 1 to aces if the card value is 11
    * while the total is above 21 and there are aces subtract 10 from the total and remove 1 from aces each loop
    * this will make the aces equal to 1 if the total is above 21
    * return total
7. check_for_blackjack(hand)
    * call calculate_score and see if it's 21
    * if it's 21 return True and if not return False
8. check_for_bust(hand)
    * call calculate_score and see if it's above 21
    * if it's over 21 return True and if not return False
9. determine_winner(player_score, dealer_score)
    * set a winner variable set to None
    * check if player_score is greater than dealer_score and return "P" for player win
    * check if player_score is less than dealer_score and return "D" for dealer win
    * check if they are equal and return "T" for a tie
10. deal_first_hands(deck, player_hand, dealer_hand)
    * create four cards and update the deck
    * set all the cards except for the first dealer card to visible
    * extend the player_hand and dealer_hand with their new cards
    * return the updated deck, player_hand, and dealer_hand
11. hit(player_hand, dealer_hand, deck)
    * call deal_card to deal a new card
    * set it to be visible
    * add it to the player_hand
    * call check_for_blackjack and if True call win()
    * call check_for_bust and if True call lose()
    * return the updated player_hand, dealer_hand, and deck
12. dealer_turn(player_hand, dealer_hand, deck)
    * call calculate_score on the dealer_hand and while it's less than 17
    * call deal_card to deal a new card
    * set it to be visible
    * append it to the dealer_hand
    * call check_for_blackjack and if True call lose()
    * call check_for_bust and if True call win()
    * return the updated player_hand, dealer_hand, and deck
13. outcomes(player_hand, dealer_hand)
    * calculate the score of the player_hand and dealer_hand by calling calculate_score
    * find the winner by calling determine_winner
    * call win() if winner is "P", lose() if winner is "D", and tie() if winner is "T"
14. welcome()
    * print the welcome screen
15. lose(player_hand, dealer_hand)
    * set the first dealer_hand to visible
    * call print_hand()
    * print player and dealer totals by calling calculate_score()
    * print the lose graphic
    * call sys.exit() to exit the program
16. win(player_hand, dealer_hand)
    * set the first dealer_hand to visible
    * call print_hand()
    * print player and dealer totals by calling calculate_score()
    * print the win graphic
    * call sys.exit() to exit the program
17. tie(player_hand, dealer_hand)
    * set the first dealer_hand to visible
    * call print_hand()
    * print player and dealer totals by calling calculate_score()
    * print the tie graphic
    * call sys.exit() to exit the program

#### Usage:

You will need Python installed on your system. On CMD for Windows or Terminal for Mac / Linux, navigate to the directory where the project was downloaded. Run the command "Python3 main.py". The program will start and display the welcome screen followed by the cards. You will then have the option to enter "h" or "s" to hit or stay. You will keep hitting until you decide either hit a blackjack, bust, or decide to stay on that turn. When you stay, the dealer will keep drawing cards until they hit at least 17 points, get a blackjack, or bust. You will win if you get a blackjack or your score is greater than the dealers.