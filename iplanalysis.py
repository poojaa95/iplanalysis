import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# LOAD DATA
# -----------------------------
matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

# Detect column names automatically
batter_col = 'batter' if 'batter' in deliveries.columns else 'batsman'
run_col = 'batsman_runs' if 'batsman_runs' in deliveries.columns else 'runs_off_bat'

# Professional Style
plt.style.use("dark_background")
sns.set_theme(style="darkgrid")

# -----------------------------
# 1️⃣ TOP 10 RUN SCORERS
# -----------------------------
top_batsmen = (
    deliveries.groupby(batter_col)[run_col]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

plt.figure(figsize=(10,6))
ax = sns.barplot(
    data=top_batsmen,
    x=run_col,
    y=batter_col,
    hue=batter_col,
    palette="magma",
    legend=False
)

plt.title("Top 10 IPL Run Scorers", fontsize=16, fontweight='bold')
plt.xlabel("Total Runs")
plt.ylabel("Player")

for container in ax.containers:
    ax.bar_label(container)

plt.tight_layout()
plt.show()

# -----------------------------
# 2️⃣ STRIKE RATE (Min 100 Balls)
# -----------------------------
balls = deliveries.groupby(batter_col).size()
runs = deliveries.groupby(batter_col)[run_col].sum()

strike_rate = (runs / balls) * 100

qualified = strike_rate[balls > 100] \
    .sort_values(ascending=False) \
    .head(10) \
    .reset_index()

qualified.columns = [batter_col, 'strike_rate']

plt.figure(figsize=(10,6))
ax = sns.barplot(
    data=qualified,
    x='strike_rate',
    y=batter_col,
    hue=batter_col,
    palette="flare",
    legend=False
)

plt.title("Top 10 Strike Rates (Min 100 Balls)", fontsize=16, fontweight='bold')
plt.xlabel("Strike Rate")
plt.ylabel("Player")

for container in ax.containers:
    ax.bar_label(container, fmt="%.1f")

plt.tight_layout()
plt.show()

# -----------------------------
# 3️⃣ MOST SIXES
# -----------------------------
sixes = deliveries[deliveries[run_col] == 6]

top_sixes = (
    sixes[batter_col]
    .value_counts()
    .head(10)
    .reset_index()
)

top_sixes.columns = [batter_col, 'sixes']

plt.figure(figsize=(10,6))
ax = sns.barplot(
    data=top_sixes,
    x='sixes',
    y=batter_col,
    hue=batter_col,
    palette="coolwarm",
    legend=False
)

plt.title("Top 10 Players with Most Sixes", fontsize=16, fontweight='bold')
plt.xlabel("Number of Sixes")
plt.ylabel("Player")

for container in ax.containers:
    ax.bar_label(container)

plt.tight_layout()
plt.show()

# -----------------------------
# 4️⃣ TOP 10 BOWLERS
# -----------------------------
wickets = deliveries[
    (deliveries['dismissal_kind'].notna()) &
    (deliveries['dismissal_kind'] != 'run out')
]

top_bowlers = (
    wickets['bowler']
    .value_counts()
    .head(10)
    .reset_index()
)

top_bowlers.columns = ['bowler', 'wickets']

plt.figure(figsize=(10,6))
ax = sns.barplot(
    data=top_bowlers,
    x='wickets',
    y='bowler',
    hue='bowler',
    palette="rocket",
    legend=False
)

plt.title("Top 10 Wicket Takers", fontsize=16, fontweight='bold')
plt.xlabel("Total Wickets")
plt.ylabel("Bowler")

for container in ax.containers:
    ax.bar_label(container)

plt.tight_layout()
plt.show()

# -----------------------------
# 5️⃣ TOP 5 TEAMS BY WINS
# -----------------------------
top_teams = (
    matches['winner']
    .value_counts()
    .head(5)
    .reset_index()
)

top_teams.columns = ['team', 'wins']

plt.figure(figsize=(8,5))
ax = sns.barplot(
    data=top_teams,
    x='wins',
    y='team',
    hue='team',
    palette="viridis",
    legend=False
)

plt.title("Top 5 Teams by Wins", fontsize=16, fontweight='bold')
plt.xlabel("Number of Wins")
plt.ylabel("Team")

for container in ax.containers:
    ax.bar_label(container)

plt.tight_layout()
plt.show()

print("\nIPL Analysis Completed Successfully!")