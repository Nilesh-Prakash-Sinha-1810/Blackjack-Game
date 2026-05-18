import random

# Constants
STARTING_WALLET = 100
BLACKJACK = 21

player_wallet = STARTING_WALLET

print("🎰 -------------------------------------------------")
print(f"🎲 Welcome to the Python Casino! You start with ${player_wallet}.")
print("🎰 -------------------------------------------------")


# Create and shuffle a fresh deck
def create_deck():
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck


# Calculate total hand value
def calculate_hand_value(hand):
    value = 0
    aces = 0

    for card in hand:
        rank = card.split(" ")[0]

        if rank in ['Jack', 'Queen', 'King']:
            value += 10
        elif rank == 'Ace':
            aces += 1
            value += 11
        else:
            value += int(rank)

    # Adjust Ace value if player busts
    while value > BLACKJACK and aces > 0:
        value -= 10
        aces -= 1

    return value


while True:
    if player_wallet <= 0:
        print("\n💀 You are broke! The casino always wins. Goodbye!")
        break

    # Create a fresh deck for the round
    deck = create_deck()

    print(f"\n🔀 A fresh deck of {len(deck)} cards has been shuffled and is ready!")

    while True:
        try:
            bet = int(input(f"\n💰 Your balance: ${player_wallet}\nEnter an amount to bet: ").strip())

            if bet <= 0:
                print("⚠️ You have to bet at least $1.")
                continue

            if bet > player_wallet:
                print("❌ Insufficient funds! Please enter a valid amount.")
                continue

            print(f"✅ Bet accepted! You bet ${bet}")
            break

        except ValueError:
            print("⚠️ Please enter a valid number.")

    # Deduct player's bet
    player_wallet -= bet
    print(f"💵 Your remaining balance is ${player_wallet}")

    player_hand = []
    dealer_hand = []

    # Safety check for deck
    if len(deck) < 4:
        deck = create_deck()

    # Initial card dealing
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())

    print("\n🎴 --- THE DEAL --- 🎴")
    print(f"🧑 Your cards: {player_hand} | Total Value: {calculate_hand_value(player_hand)}")
    print(f"🤖 Dealer's visible card: [{dealer_hand[0]}] and one hidden card.")

    while True:
        player_score = calculate_hand_value(player_hand)

        # Natural blackjack detection
        if len(player_hand) == 2 and player_score == BLACKJACK:
            print("🃏 BLACKJACK! 🃏")
            break

        if player_score == BLACKJACK:
            print("🎉 You have 21!")
            break

        choice = input("\nDo you want to [H]it or [S]tand? ").strip().lower()

        if choice == 'h':

            # Safety check for deck
            if len(deck) == 0:
                deck = create_deck()

            new_card = deck.pop()
            player_hand.append(new_card)

            print(f"🃏 You drew: {new_card}")

            player_score = calculate_hand_value(player_hand)
            print(f"🧑 Your cards: {player_hand} | Total Value: {player_score}")

            if player_score > BLACKJACK:
                print("💥 Bust! You went over 21. Dealer wins!")
                break

        elif choice == 's':
            print(f"✋ You stand with a total of {player_score}.")
            break

        else:
            print("⚠️ Invalid choice! Please enter 'H' to hit or 'S' to stand.")

    player_score = calculate_hand_value(player_hand)
    dealer_score = calculate_hand_value(dealer_hand)

    if player_score <= BLACKJACK:
        print("\n🤖 --- DEALER'S TURN --- 🤖")
        print(f"🃏 Dealer reveals hidden card. Full hand: {dealer_hand}")
        print(f"📊 Dealer's starting total: {dealer_score}")

        while dealer_score < 17:

            # Safety check for deck
            if len(deck) == 0:
                deck = create_deck()

            new_card = deck.pop()
            dealer_hand.append(new_card)

            dealer_score = calculate_hand_value(dealer_hand)
            print(f"🤖 Dealer draws: {new_card} | Dealer total: {dealer_score}")

        print("\n🏁 --- FINAL RESULTS --- 🏁")
        print(f"🧑 Your final score: {player_score}")
        print(f"🤖 Dealer's final score: {dealer_score}")

        if dealer_score > BLACKJACK:
            print("🎉 Dealer busted! You win!")
            player_wallet += (bet * 2)

        elif player_score > dealer_score:
            print("🏆 You beat the dealer! You win!")
            player_wallet += (bet * 2)

        elif player_score < dealer_score:
            print("😔 Dealer wins!")

        else:
            print("🤝 It's a tie (Push)! You get your bet back.")
            player_wallet += bet

    else:
        print("\n🏁 --- FINAL RESULTS --- 🏁")
        print("💀 Game over. You busted, so the dealer wins automatically.")

    print(f"\n💰 Your new wallet balance is: ${player_wallet}")

    play_again = input("\n🔁 Do you want to play another round? (y/n): ").strip().lower()

    if play_again.startswith('n'):
        print(f"\n👋 Thanks for playing! You leave the table with ${player_wallet}.")
        break