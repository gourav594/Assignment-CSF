# 🎮 Number Guessing Game

A fun and interactive console-based number guessing game built with Python. Test your intuition and logic by guessing the secret number with helpful hints!

## 📝 Description

This is a simple yet engaging number guessing game where players try to guess a randomly generated number within a specific range. The game offers three difficulty levels and provides intelligent hints to guide players toward the correct answer. It's perfect for beginners learning Python and demonstrates fundamental programming concepts.

## ✨ Features

- **Three Difficulty Levels**
  - Easy: Guess between 1-50 with 10 attempts
  - Medium: Guess between 1-100 with 7 attempts
  - Hard: Guess between 1-200 with 5 attempts

- **Intelligent Hint System**
  - Directional hints (Too High/Too Low)
  - Temperature-based proximity hints (Hot/Cold)
  - Visual feedback with emojis

- **Game Statistics**
  - Track total games played
  - Monitor win rate
  - View guess history

- **User-Friendly Interface**
  - Clear instructions
  - Input validation
  - Attempt counter
  - Play again option

## 🚀 Installation and Setup

### Prerequisites
- Python 3.6 or higher installed on your system
- Basic knowledge of running Python scripts

### Steps to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/gourav594-coder/assignment-CSF.git
   Number-guessing-game
   ```

2. **Run the game**
   ```bash
   python game.py
   ```

3. **Start playing!**
   - Follow the on-screen instructions
   - Select your difficulty level
   - Make your guesses and enjoy!

## 🎯 How to Play

1. Launch the game by running `game.py`
2. Choose your preferred difficulty level (1-3)
3. The game will generate a random secret number
4. Enter your guess when prompted
5. Receive hints after each guess:
   - 📈 Too Low / 📉 Too High
   - 🔥 Very Hot / ❄️ Cold (proximity indicators)
6. Keep guessing until you find the number or run out of attempts
7. View your statistics and choose to play again!

## 📸 Screenshots

### Welcome Screen
```
==================================================
     WELCOME TO THE NUMBER GUESSING GAME!
==================================================

How to play:
1. Choose a difficulty level
2. Guess the secret number within the range
3. Get hints after each guess
4. Try to guess in minimum attempts!
```

### Gameplay Example
```
Attempt 3/7 (Remaining: 5)
Enter your guess (1-100): 50

📉 Too High!
☀️ Warm! You're on the right track!
```

### Victory Screen
```
🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
   CONGRATULATIONS! You guessed it right!
   The secret number was: 42
   You won in 5 attempt(s)!
🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
```

## 🛠️ Technology Stack

- **Language**: Python 3.x
- **Libraries**: 
  - `random` - For generating random numbers
  - `os` - For screen clearing functionality

## 📂 Project Structure

```
assignment-CSF/
├── game.py              # Main game file
├── README.md            # Project documentation
├── Gitignore            # Git ignore file
├── overview.md          # Project overview
├── development.md       # Development process
└── improvements.md      # Future improvements
```

## 🎓 Learning Outcomes

This project demonstrates:
- Function-based programming structure
- User input validation
- Conditional logic and loops
- Random number generation
- Basic algorithm design
- Code documentation practices

## 🤝 Contributing

This is an educational project. If you'd like to suggest improvements:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is created for educational purposes as part of the B.Tech CSE coursework at K.R. Mangalam University.

## 👨‍💻 Author

GOURAV

B.Tech CSE (CyberSecurity) - Semester 1  
K.R. Mangalam University

## 🙏 Acknowledgments

- Course: Computer Science Fundamentals & Career Pathways (ETCCCP105)
- Faculty: Dr. Firoz Ahmed
- Assignment: 04 - Tools for Programming, Learning, and Collaboration

---

**Note**: This project was developed using Visual Studio Code and version controlled with Git/GitHub as part of the course requirements.
