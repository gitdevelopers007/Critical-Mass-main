import subprocess
import re

wins = {0: 0, 1: 0, "unknown": 0}

NUM_GAMES = 20   # keep 20 for now, faster

for i in range(NUM_GAMES):
    print(f"\n=== GAME {i+1} ===")
    
    result = subprocess.run(
        ["python", "bot_vs_bot.py"],
        capture_output=True,
        text=True
    )

    output = result.stdout
    print(output.split("Winner:")[-1].strip() if "Winner:" in output else "No winner found")

    match = re.search(r"Winner:\s*Player\s*(\d+)", output)
    if match:
        winner = int(match.group(1))
        wins[winner] += 1
    else:
        wins["unknown"] += 1

print("\n======================")
print("FINAL RESULTS")
print("======================")
print(f"Player 0 Wins: {wins[0]}")
print(f"Player 1 Wins: {wins[1]}")
print(f"Unknown: {wins['unknown']}")