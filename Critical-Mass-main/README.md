# Critical Mass AI Environment

A Python-based AI simulation environment for the **Critical Mass / Chain Reaction** strategy game.

This project was built as an **AI-ready environment** where agents (bots) can interact with the game, make moves, trigger chain reactions, and compete against each other.

---

## Problem Statement

Build a complete environment that an AI agent can learn from using a structured game loop and state transitions.

This environment simulates the strategic board game **Critical Mass**, where:
- players place atoms on a board,
- cells explode when they reach capacity,
- chain reactions spread across the grid,
- and the last surviving player wins.

---

## Project Goal

The goal of this project is to create a reusable environment for:

- AI experimentation
- Bot-vs-bot simulation
- Strategic decision making
- Reinforcement Learning style interaction

---

## Features

- Turn-based board game logic
- Chain reaction explosion system
- Bot vs Bot simulation
- Multiple bot strategies
- Winner detection
- Repeated automated matches
- Optional GUI support

---

## Project Structure

```bash
Critical-Mass-main/
├── bot_bot.py
├── bot_vs_bot.py
├── Botzilla_bot.py
├── chain_reaction.py
├── dummy_bot.py
├── gui.py
├── random_bot.py
├── README.md
├── run_100_games.py
└── strategy.txt