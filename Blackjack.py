#############################################
#############################################
########DEFINED FUNCTIONS, IMPORT, CARD VALUES LIBRARY, LOGO
logo = """
.------.            _     _            _    _            _    
|H_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|J /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ T|                            _/ |                
      `------'                           |__/           
"""
import random
cards_values = {
    11: "A", 
    1: 1, 
    2: 2, 
    3: 3, 
    4: 4, 
    5: 5, 
    6: 6, 
    7: 7, 
    8: 8, 
    9: 9, 
    10: 10, 
    10: "J", 
    10: "Q", 
    10: "K",
    }
def deal_card():
    """CREATES CARD LIST AND SELECT RANDOM CARD"""
    cards_list = ["11", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"]
    card = random.choice(cards_list)
    return int(card)
def calculate_score(cards):
    """CALCULATES SCORE BASED ON CARD INPUT AND RETURN SCORE"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

##############################################
##############################################
######FIRST HAND STATEMENTS AND FUNCTION CALLS

def play_game():
    def shown_cards(num):
        """CONVERTS PLAYER CARDS FROM NUMBERS TO A,J,Q,K"""
        hand = []
        for num in player_cards:
         hand += str(cards_values[num])
        return hand
    def com_shown_cards(num):
        """CONVERTS COMPUTER CARDS FROM NUMBERS TO A,J,Q,K"""
        hand = []
        for num in computer_cards:
            hand += str(cards_values[num])
        return hand
    print(logo)
    player_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]    
    game_over = False
    player_score = calculate_score(player_cards)
    computer_score = calculate_score(computer_cards)
    if player_score == 0 or computer_score == 0:
        if player_score == 0 and computer_score == 0:
            print(f"Your cards: {shown_cards(player_cards)}, current score: {player_score}")
            print(f"Dealer shows: {computer_cards[1]}")
            print("Double Blackjack! Push game!")
        elif player_score == 0:
            print(f"Your cards: {shown_cards(player_cards)}, current score: {player_score}")
            print(f"Dealer shows: {computer_cards[1]}")
            print("Blackjack! Player wins!")
            game_over = True
        else:
            print(f"Your cards: {shown_cards(player_cards)}, current score: {player_score}")
            print(f"Dealer shows: {computer_cards[1]}")
            print("Blackjack! Dealer wins!")
            game_over = True
    else:
        print(f"Your cards: {shown_cards(player_cards)}, current score: {player_score}")
        print(f"Dealer shows: {computer_cards[1]}")
    ##############################################
    ##############################################
    #####HIT/STAY LOOP WITH GAME OUTCOME##########
    hit_stay = "hit"
    while game_over == False:
        while player_score <= 21 and hit_stay == "hit":
            hit_stay = input("Type hit for another card, or type stay: ")
            if hit_stay == "hit":
                player_cards.append(deal_card())
                player_score = calculate_score(player_cards)
                print(f"Your cards: {shown_cards(player_cards)}, current score: {player_score}")
                print(f"Dealer shows: {computer_cards[1]}")
                if player_score > 21:
                    print("Player busts! Dealer wins!")
                    game_over = True
        while hit_stay == "stay" and computer_score < 17:
            while computer_score < 17:
                print("Dealer hits.")
                computer_cards.append(deal_card())
                computer_score = calculate_score(computer_cards)
                print(f"Dealer shows: {com_shown_cards(computer_cards)}")
                print(f"Your cards: {shown_cards(player_cards)}, current score: {player_score}")
                if computer_score > 21:
                    print(f"Dealer busts with {computer_score}! Player wins!")
                    game_over = True
        if computer_score == player_score:
            print("Player and Dealer tie! Push game!")
            game_over = True
        elif player_score > computer_score and player_score <= 21:
            print("Player wins!")
            game_over = True
        elif computer_score > player_score and computer_score <= 21:
            print(f"Dealer wins! Dealer score: {computer_score}")
            game_over = True
################################################
################################################
#####GAME RESTART###############################
lets_play = input("Would you like to play a game of Blackjack? Type 'y' to play!: ")
if lets_play == "y":
    play_game()
else:
    exit
while input("Type 'y' to play another hand: ") == "y":
    play_game()
