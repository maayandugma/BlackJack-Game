import random, sys, time

HEARTS   = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES   = chr(9824) # Character 9824 is '♠'.
CLUBS    = chr(9827) # Character 9827 is '♣'.

def round(money):

    def GetDeck():
        '''return list of cards'''
        deck = []
        for number in range(2, 11):
            for sign in (HEARTS, DIAMONDS, SPADES, CLUBS):
                deck.append((number, sign))
        for caste in ["A", "J", "Q", "K"]:
            for sign in (HEARTS, DIAMONDS, SPADES, CLUBS):
                deck.append((caste, sign))

        return deck

    def count_player_hand(cards):
        """Returns the value of the cards. Face cards are worth 10, aces are 11 or 1"""
        p_card = []
        numberOfAces = [] #count the 
        for i in range(len(cards)):

            if cards[i][0] == "A":
                p_card.append(11)
                numberOfAces.append("A")

            elif cards[i][0] in ["J", "Q", "K"]:
                p_card.append(10)

            else:
                p_card.append(int(cards[i][0]))
        sum_p_card = sum(p_card)

        # in a case that the sum of the card more than 21 ,change the value of the "ace" to 1
        while sum_p_card > 21 and "A" in numberOfAces:

            if 11 in p_card:
                p_card.remove(11)
                p_card.append(1)
                sum_p_card = sum(p_card)

            else:
                break

        return sum_p_card

    def allow_drawing_card_if_not_burned_or_at_21(player_hand,deck_card):
        """player turn, while sum of player's card less than 21 ,check his move (bet or stay)"""
        player_hit_option = ["H", "h", "HIT", "hit"]

        sum_cards = count_player_hand(player_hand)
        while sum_cards < 21:
            player_move = input("Would you like to HIT or STAY?")
            # add another card to the player
            if player_move in player_hit_option:
                player_hand.append(deck_card.pop())
                sum_cards = count_player_hand(player_hand)
                print(f"player_hand = {player_hand}")
            else:
                break

        return sum_cards

    def dealer_turn(dealer_hand,deck_card):
        sum_dealer_hand = -1
        # add a cards to dealer until the sum of the card will be above than 16
        while sum_dealer_hand < 17 :
            dealer_hand.append(deck_card.pop())
            print(f"dealer_hand ={dealer_hand}")
            time.sleep(1)
            sum_dealer_hand = count_player_hand(dealer_hand)

        return sum_dealer_hand



    def cont_player(money):

        valid_yes_option = ["y", "yes", "YES", "Y"]
        # Check if the player broke
        if money == 0:
            print("You're broke!")
            print("GAME-OVER")
            sys.exit()
        # Check if the player want to continue game
        else:
            continue_game = input("Would you like continue gamble? y / n")
            if continue_game not in valid_yes_option:
                print("Thanks for playing!")
                sys.exit()
            else:
                round(money)

    print('Money:', money)
    # the player enter his bet
    # check if he's bet is integers
    # take player bet
    while True:
        try:
            bet = int(input("Please place your bet:"))
            # check if the bet not exceeding player's balance
            if bet > money:
                print(f"You don't have enough money,you have {money}")
                continue
            else:
                break
        except ValueError:
            print("Invalid input was provided,  please provide integers only!")


    money -= bet
    deck_card = GetDeck()
    random.shuffle(deck_card)
    # Deal cards
    # By Geneva conventions this is how the cards should be dealt
    player_hand = [deck_card.pop(), deck_card.pop()]
    dealer_hand = [deck_card.pop()]

    print(f"dealer hand = {dealer_hand}")
    print(f"player hand = {player_hand}")



    while True:
        # could probably use the count once for each loop iteration
        sum_player_hand = allow_drawing_card_if_not_burned_or_at_21(player_hand,deck_card)
        if sum_player_hand > 21 :
            # round lost scenario
            print("you lost")
            cont_player(money) # check if the player want to continue play
        else:
            sum_dealer_hand = dealer_turn(dealer_hand,deck_card)
            if sum_dealer_hand > 21 :
                print("you win")
                money += 2 * int(bet)
                cont_player(money)

            elif sum_dealer_hand <= 21:
                if sum_dealer_hand > sum_player_hand:
                    print("you lost")
                    cont_player(money)

                elif sum_player_hand == sum_dealer_hand:
                    print("tie")

                    money += int(bet)
                    cont_player(money)

                else:
                    print("you win")
                    money += 2 * int(bet)
                    cont_player(money)




def main():

    money = 5000
    round(money)


main()

