# 🎰 Python Blackjack Game

A terminal-based **Blackjack game built in Python** where players can place bets, manage a wallet, and compete against a dealer using classic Blackjack mechanics.

---

## ✨ Features

- 💰 Wallet system with betting
- 🎴 Fresh shuffled deck every round
- 🃏 Automatic Ace value adjustment (11 → 1)
- 🤖 Dealer AI (draws until 17+)
- 🏆 Win / Lose / Push logic
- 🎯 Natural Blackjack detection
- 🔁 Replay multiple rounds
- 🛡️ Input validation & error handling
- 🎨 Improved terminal UI with emojis

---

## 🃏 Rules

### Objective
Beat the dealer by getting a hand value closer to **21** without going over.

### Card Values

| Card | Value |
|------|------:|
| Number Cards (2–10) | Face Value |
| Jack, Queen, King | 10 |
| Ace | 11 or 1 |

### Ace Logic
Aces are initially counted as **11**, but automatically convert to **1** if the total exceeds **21**.

### Natural Blackjack
If your first **two cards total 21**, the game detects a **Blackjack**.

> Current version uses standard payout (no 3:2 Blackjack bonus).

### Dealer Rules
The dealer:

- Reveals the hidden card after your turn
- Draws cards until reaching **17 or higher**
- Stops at **17+**

### Winning Conditions

You win if:

- Dealer busts (**over 21**)
- Your total is higher than the dealer's

You lose if:

- You bust (**over 21**)
- Dealer has a higher score

### Push (Tie)
If both totals are equal, your bet is returned.

---

## 🎮 Controls

| Key | Action |
|------|--------|
| `H` | Hit |
| `S` | Stand |
| `Y` | Play Again |
| `N` | Exit Game |

---

## ⚙️ Requirements

- Python **3.8+**

Check installed version:

```bash
python --version
```

or

```bash
python3 --version
```

---

## 🚀 Installation & Running

### 1. Clone the Repository

```bash
git clone <https://github.com/Nilesh-Prakash-Sinha-1810/Blackjack-Game.git>
```

### 2. Navigate to the Project Folder

```bash
cd Blackjack-Game
```

### 3. Run the Program

```bash
python BlackJack.py
```

or

```bash
python3 BlackJack.py
```

---

## 📂 Project Structure

```text
Blackjack-Game/
│── BlackJack.py
│── README.md
│── LICENSE
```

---

## 🛡️ Error Handling

The game includes validation for:

- Invalid input
- Negative or zero bets
- Insufficient wallet balance
- Empty deck protection

---

## 🧠 Concepts Used

This project demonstrates:

- Functions
- Loops
- Lists
- Conditional Logic
- Error Handling (`try-except`)
- Input Validation
- Randomization
- Game Logic Design

---

## 🔮 Future Improvements

Planned features:

- [ ] Double Down
- [ ] Split Cards
- [ ] Insurance
- [ ] Statistics Tracking
- [ ] Save Progress
- [ ] GUI Version (Tkinter / PyQt)
- [ ] Multiplayer Mode
- [ ] Sound Effects

---

## 👨‍💻 Solo Developer

### This project is made by a solo developer

# **Nilesh Prakash Sinha**

> This project was created for learning and educational practice while improving Python and programming skills.

---

## 📜 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.
