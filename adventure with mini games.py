import random

# Player stats
player = {
    "health": 100,
    "gold": 50,
    "inventory": []
}

# ---------- Utility ----------
def status():
    print(f"\n❤️ Health: {player['health']} | 💰 Gold: {player['gold']} | 🎒 Inventory: {player['inventory']}")

# ---------- Mini Games ----------
def dice_game():
    print("\n🎲 Dice Betting Game")
    bet = int(input("Enter bet amount: "))
    if bet > player["gold"]:
        print("Not enough gold!")
        return

    player_roll = random.randint(1, 6)
    dealer_roll = random.randint(1, 6)

    print(f"You rolled: {player_roll}")
    print(f"Dealer rolled: {dealer_roll}")

    if player_roll > dealer_roll:
        player["gold"] += bet
        print(f"You won! Gained {bet} gold.")
    else:
        player["gold"] -= bet
        print(f"You lost! Lost {bet} gold.")

def number_guessing_game():
    print("\n🔢 Number Guessing Challenge")
    number = random.randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))

    if guess == number:
        player["gold"] += 20
        print("Correct! You earned 20 gold.")
    else:
        player["health"] -= 10
        print(f"Wrong! The number was {number}. You lost 10 health.")

def rock_paper_scissors():
    print("\n✊✋✌️ Rock Paper Scissors")
    choices = ["rock", "paper", "scissors"]
    user = input("Choose rock/paper/scissors: ").lower()
    computer = random.choice(choices)

    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        player["gold"] += 15
        print("You win! Gained 15 gold.")
    else:
        player["health"] -= 15
        print("You lost! Lost 15 health.")

# ---------- Chapters ----------
def chapter1():
    print("\n🌲 Chapter 1: The Forest")
    choice = input("You meet a merchant. Invest gold? (yes/no): ").lower()

    if choice == "yes":
        result = random.randint(-20, 40)
        player["gold"] += result
        print(f"Investment result: {result} gold")

    if random.choice([True, False]):
        print("A wild wolf appears!")
        number_guessing_game()

def chapter2():
    print("\n🏘️ Chapter 2: The Village")
    print("1. Casino (Dice Game)")
    print("2. Arena (Rock Paper Scissors)")
    print("3. Market (Buy Potion)")

    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        dice_game()
    elif choice == "2":
        rock_paper_scissors()
    elif choice == "3":
        if player["gold"] >= 20:
            player["gold"] -= 20
            player["inventory"].append("Health Potion")
            print("You bought a Health Potion!")
        else:
            print("Not enough gold.")

def chapter3():
    print("\n🏰 Chapter 3: The Castle")
    print("Final Challenge!")

    if "Health Potion" in player["inventory"]:
        use = input("Use Health Potion? (yes/no): ").lower()
        if use == "yes":
            player["health"] += 30
            player["inventory"].remove("Health Potion")
            print("Health restored!")

    rock_paper_scissors()

    if player["health"] > 0:
        reward = 100 + random.randint(0, 50)
        player["gold"] += reward
        print(f"You defeated the castle guardian! Treasure gained: {reward} gold")

# ---------- Main Game ----------
def main():
    print("🎮 Welcome to the Adventure Investment Game!")

    chapter1()
    status()
    if player["health"] <= 0:
        print("Game Over!")
        return

    chapter2()
    status()
    if player["health"] <= 0:
        print("Game Over!")
        return

    chapter3()
    status()

    if player["health"] > 0:
        print("\n🏆 Congratulations! You completed the game successfully!")
    else:
        print("\n💀 You were defeated at the final stage.")

if __name__ == "__main__":
    main()