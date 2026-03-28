# 🧪 Critical Mass – AI Agent for Chain Reaction

An AI-powered bot environment for the game **Chain Reaction**, built as a real-world **OpenEnv-style environment** where agents can interact using a standard API like:

* `reset()`
* `step(action)`
* `state()`

This project simulates a strategic turn-based game environment that can be used for:

* AI agent testing
* bot-vs-bot simulations
* reinforcement learning experiments
* strategy benchmarking

---

## 🚀 Problem Statement

Build a complete, real-world environment where an AI agent can learn and make decisions through a structured API.

Our project solves this by creating a playable and testable **Chain Reaction simulation environment**, where bots can:

* observe the board state
* choose valid actions
* trigger chain reactions
* compete against other bots

---

## 🎯 What We Built

We built:

* A **fully working Chain Reaction game engine**
* A **standard environment API**
* Multiple bots with different strategies
* A **bot-vs-bot simulator**
* A **100-game evaluation script**
* A structure that can later support **RL agents / LLM agents**

---

## 🧠 Why This Is Useful

This environment can be used for:

* training game-playing agents
* testing strategic decision-making
* comparing AI bot performance
* experimenting with planning and search algorithms

It behaves like a mini AI research playground.

---

## 🛠️ Features

* ✅ Grid-based Chain Reaction simulation
* ✅ Turn-based environment
* ✅ Standard agent interaction flow
* ✅ Multiple bot strategies
* ✅ Automatic game simulation
* ✅ Win/loss testing over many games
* ✅ Easy to extend for RL / smarter AI

---

## 📂 Project Structure

```bash
Critical-Mass-main/
│
├── chain_reaction.py      # Core game logic / environment
├── bot_vs_bot.py          # Run bot vs bot matches
├── run_100_games.py       # Benchmark bots over 100 games
├── random_bot.py          # Random move bot
├── dummy_bot.py           # Simple baseline bot
├── bot_bot.py             # Custom bot logic
├── Botzilla_bot.py        # Advanced/custom strategy bot
├── gui.py                 # Optional game GUI / visualization
├── strategy.txt           # Strategy notes
└── README.md              # Project documentation
```

---

## ⚙️ How It Works

The environment follows a simple agent loop:

1. **Reset** the board
2. Agent receives current **state**
3. Agent selects an **action**
4. Environment applies the move using **step(action)**
5. Chain reactions are triggered if cell limits are exceeded
6. Game continues until one player wins

---

## 🔁 Environment API

### `reset()`

Resets the board to the initial state.

### `state()`

Returns the current board state.

### `step(action)`

Applies a move and updates the board.

---

## 🤖 Bots Included

### 1. Random Bot

Chooses a valid move randomly.

### 2. Dummy Bot

Uses a simple fixed/basic strategy.

### 3. Botzilla Bot

Our stronger custom bot with better move selection logic.

### 4. Custom Bot

Additional experimental strategy bot.

---

## 📊 Evaluation

We tested the environment by running multiple bot-vs-bot matches.

### Run 100 games benchmark

```bash
python run_100_games.py
```

This helps compare:

* win rate
* consistency
* strategy strength

---

## ▶️ How to Run

### Run bot vs bot

```bash
python bot_vs_bot.py
```

### Run 100 games benchmark

```bash
python run_100_games.py
```

### Run GUI (if needed)

```bash
python gui.py
```

---

## 💻 Tech Stack

* **Python**
* Rule-based AI bot logic
* Game simulation environment
* CLI-based testing

---

## 🔮 Future Improvements

* Reinforcement Learning agent support
* Minimax / Monte Carlo Tree Search bot
* Better GUI visualization
* Performance analytics dashboard
* Multi-agent tournament mode

---

## 👥 Team - Botzilla

* Sai Ganesh Pushadapu
* KOUSHIK RAHUL

---

## 🏁 Conclusion

Critical Mass transforms Chain Reaction into a structured AI environment where intelligent agents can learn, compete, and be evaluated.

This project demonstrates:

* environment design
* simulation engineering
* AI agent interaction
* strategic decision-making systems
