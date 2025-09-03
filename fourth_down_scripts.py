import pandas as pd
import plotly.express as px
import os

# load multiple seasons
years = [1999, 2000, 2001, 2002, 2003, 2004, 2005, 
        2006, 2007, 2008, 2009, 2010, 2011, 2012, 
        2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 
        2021, 2022, 2023, 2024]
all_fourths = []

for year in years:
    file_path = f"pbp_data/play_by_play_{year}.parquet"
    if os.path.exists(file_path):
        df = pd.read_parquet(file_path)
        focus_cols = ["season","week","posteam","defteam","yardline_100","ydstogo","down","play_type","wp","fourth_down_converted","fourth_down_failed","qtr","game_seconds_remaining"]
        fourths = df.loc[df["down"] == 4, focus_cols].copy()
        all_fourths.append(fourths)
        print(f"Loaded {len(fourths)} 4th downs from {year}")

# combine all years
fourths = pd.concat(all_fourths, ignore_index=True)
print(f"\nTotal 4th downs across all years: {len(fourths)}")
print(fourths.head())

# simple chart: how often teams go for it vs kick
fourths["decision"] = fourths["play_type"].map(lambda x: "go" if x in ["run","pass"] else "kick")
counts = fourths.groupby("decision").size().reset_index(name="count")

fig = px.bar(counts, x="decision", y="count", title="Go vs Kick (1999-2024)")
fig.write_html("first_chart.html")
print("chart saved as first_chart.html")

# yearly trends chart
yearly_counts = fourths.groupby(["season", "decision"]).size().reset_index(name="count")
fig2 = px.line(yearly_counts, x="season", y="count", color="decision", 
               title="4th Down Decision Trends by Year (1999-2024)",
               markers=True)
fig2.write_html("yearly_trends.html")
print("yearly trends chart saved as yearly_trends.html")

# Success rate analysis
print("\n=== SUCCESS RATE ANALYSIS ===")

# Filter to only "go for it" attempts (run/pass plays)
go_attempts = fourths[fourths["decision"] == "go"].copy()
print(f"Total 'go for it' attempts: {len(go_attempts)}")

# Calculate success rate
successful = go_attempts["fourth_down_converted"].sum()
total_attempts = len(go_attempts)
success_rate = (successful / total_attempts) * 100 if total_attempts > 0 else 0

print(f"Successful conversions: {successful}")
print(f"Success rate: {success_rate:.1f}%")

# Success rate by distance
print("\n=== SUCCESS RATE BY DISTANCE ===")
distance_success = go_attempts.groupby("ydstogo").agg({
    "fourth_down_converted": ["count", "sum"]
}).round(2)
distance_success.columns = ["attempts", "successful"]
distance_success["success_rate"] = (distance_success["successful"] / distance_success["attempts"] * 100).round(1)
distance_success = distance_success[distance_success["attempts"] >= 10]  # Only show distances with 10+ attempts
print(distance_success)

# Create success rate visualization
fig3 = px.bar(distance_success.reset_index(), 
              x="ydstogo", y="success_rate",
              title="4th Down Success Rate by Distance to Go (1999-2024)",
              labels={"ydstogo": "Yards to Go", "success_rate": "Success Rate (%)"})
fig3.write_html("success_rate_by_distance.html")
print("Success rate chart saved as success_rate_by_distance.html")

# Time-based aggression analysis
print("\n=== TIME-BASED AGGRESSION ANALYSIS ===")

# Create time categories
def categorize_time(seconds_remaining):
    if seconds_remaining > 2700:  # First half
        return "1st Half"
    elif seconds_remaining > 1800:  # 3rd Quarter
        return "3rd Quarter"
    elif seconds_remaining > 900:   # Early 4th Quarter
        return "Early 4th Quarter"
    elif seconds_remaining > 300:   # Late 4th Quarter
        return "Late 4th Quarter"
    else:  # Final 5 minutes
        return "Final 5 Minutes"

fourths["time_category"] = fourths["game_seconds_remaining"].apply(categorize_time)

# Calculate go-for-it rate by time
time_aggression = fourths.groupby("time_category").agg({
    "decision": lambda x: (x == "go").sum() / len(x) * 100
}).round(1)
time_aggression.columns = ["go_for_it_rate"]
time_aggression = time_aggression.sort_values("go_for_it_rate", ascending=False)

print("Go-for-it rate by time in game:")
print(time_aggression)

# Also show by quarter
quarter_aggression = fourths.groupby("qtr").agg({
    "decision": lambda x: (x == "go").sum() / len(x) * 100
}).round(1)
quarter_aggression.columns = ["go_for_it_rate"]
print("\nGo-for-it rate by quarter:")
print(quarter_aggression)

# Create visualization
fig4 = px.bar(time_aggression.reset_index(), 
              x="time_category", y="go_for_it_rate",
              title="4th Down Go-for-it Rate by Time in Game (1999-2024)",
              labels={"time_category": "Time in Game", "go_for_it_rate": "Go-for-it Rate (%)"})
fig4.write_html("time_aggression.html")
print("Time aggression chart saved as time_aggression.html")

# Run vs Pass analysis on 4th downs
print("\n=== RUN VS PASS ON 4TH DOWNS ===")

# Filter to only "go for it" attempts and categorize by run/pass
go_attempts = fourths[fourths["decision"] == "go"].copy()
go_attempts["play_strategy"] = go_attempts["play_type"].map(lambda x: "run" if x == "run" else "pass" if x == "pass" else "other")

# Overall run vs pass breakdown
strategy_counts = go_attempts["play_strategy"].value_counts()
print("Play type breakdown on 4th down go-for-it attempts:")
print(strategy_counts)

# Success rates by strategy
strategy_success = go_attempts.groupby("play_strategy").agg({
    "fourth_down_converted": ["count", "sum"]
}).round(2)
strategy_success.columns = ["attempts", "successful"]
strategy_success["success_rate"] = (strategy_success["successful"] / strategy_success["attempts"] * 100).round(1)
strategy_success = strategy_success[strategy_success["attempts"] >= 100]  # Only show strategies with 100+ attempts

print("\nSuccess rates by play strategy:")
print(strategy_success)

# Run vs Pass by distance
print("\n=== RUN VS PASS BY DISTANCE ===")
distance_strategy = go_attempts.groupby(["ydstogo", "play_strategy"]).agg({
    "fourth_down_converted": ["count", "sum"]
}).round(2)
distance_strategy.columns = ["attempts", "successful"]
distance_strategy["success_rate"] = (distance_strategy["successful"] / distance_strategy["attempts"] * 100).round(1)

# Pivot to compare run vs pass by distance
distance_comparison = distance_strategy["success_rate"].unstack(fill_value=0)
distance_comparison = distance_comparison[(distance_comparison["run"] >= 20) | (distance_comparison["pass"] >= 20)]  # Min 20 attempts
print("Success rate by distance and strategy (run vs pass):")
print(distance_comparison)

# Create visualization
fig5 = px.bar(strategy_success.reset_index(), 
              x="play_strategy", y="success_rate",
              title="4th Down Success Rate: Run vs Pass (1999-2024)",
              labels={"play_strategy": "Play Strategy", "success_rate": "Success Rate (%)"})
fig5.write_html("run_vs_pass_success.html")
print("Run vs pass success chart saved as run_vs_pass_success.html")

# Distance comparison chart
fig6 = px.bar(distance_comparison.reset_index(), 
              x="ydstogo", y=["run", "pass"],
              title="4th Down Success Rate by Distance: Run vs Pass (1999-2024)",
              labels={"ydstogo": "Yards to Go", "value": "Success Rate (%)"},
              barmode="group")
fig6.write_html("run_vs_pass_by_distance.html")
print("Run vs pass by distance chart saved as run_vs_pass_by_distance.html")

# Field position analysis
print("\n=== FIELD POSITION ANALYSIS ===")

# Create field position categories
def categorize_field_position(yardline_100):
    if yardline_100 <= 10:  # Own goal line area
        return "Own 1-10"
    elif yardline_100 <= 20:  # Own territory
        return "Own 11-20"
    elif yardline_100 <= 30:  # Own territory
        return "Own 21-30"
    elif yardline_100 <= 40:  # Own territory
        return "Own 31-40"
    elif yardline_100 <= 50:  # Midfield
        return "Own 41-50"
    elif yardline_100 <= 60:  # Opponent territory
        return "Opp 40-49"
    elif yardline_100 <= 70:  # Opponent territory
        return "Opp 30-39"
    elif yardline_100 <= 80:  # Opponent territory
        return "Opp 20-29"
    elif yardline_100 <= 90:  # Red zone
        return "Opp 10-19"
    else:  # Goal line area
        return "Opp 1-9"

fourths["field_position"] = fourths["yardline_100"].apply(categorize_field_position)

# Go-for-it rate by field position
field_aggression = fourths.groupby("field_position").agg({
    "decision": lambda x: (x == "go").sum() / len(x) * 100
}).round(1)
field_aggression.columns = ["go_for_it_rate"]
field_aggression = field_aggression.sort_values("go_for_it_rate", ascending=False)

print("Go-for-it rate by field position:")
print(field_aggression)

# Success rate by field position (for go-for-it attempts)
go_attempts["field_position"] = go_attempts["yardline_100"].apply(categorize_field_position)
field_success = go_attempts.groupby("field_position").agg({
    "fourth_down_converted": ["count", "sum"]
}).round(2)
field_success.columns = ["attempts", "successful"]
field_success["success_rate"] = (field_success["successful"] / field_success["attempts"] * 100).round(1)
field_success = field_success[field_success["attempts"] >= 50]  # Only show positions with 50+ attempts

print("\nSuccess rate by field position (go-for-it attempts):")
print(field_success)

# Create field position order for better visualization
field_order = ["Own 1-10", "Own 11-20", "Own 21-30", "Own 31-40", "Own 41-50", 
               "Opp 40-49", "Opp 30-39", "Opp 20-29", "Opp 10-19", "Opp 1-9"]

# Reorder data for visualization
field_aggression_ordered = field_aggression.reindex(field_order)
field_success_ordered = field_success.reindex(field_order)

# Create visualizations
fig7 = px.bar(field_aggression_ordered.reset_index(), 
              x="field_position", y="go_for_it_rate",
              title="4th Down Go-for-it Rate by Field Position (1999-2024)",
              labels={"field_position": "Field Position", "go_for_it_rate": "Go-for-it Rate (%)"})
fig7.update_xaxes(tickangle=45)
fig7.write_html("field_position_aggression.html")
print("Field position aggression chart saved as field_position_aggression.html")

fig8 = px.bar(field_success_ordered.reset_index(), 
              x="field_position", y="success_rate",
              title="4th Down Success Rate by Field Position (1999-2024)",
              labels={"field_position": "Field Position", "success_rate": "Success Rate (%)"})
fig8.update_xaxes(tickangle=45)
fig8.write_html("field_position_success.html")
print("Field position success chart saved as field_position_success.html")

# Red zone vs non-red zone analysis
print("\n=== RED ZONE VS NON-RED ZONE ===")
fourths["is_red_zone"] = fourths["yardline_100"] >= 80

red_zone_analysis = fourths.groupby("is_red_zone").agg({
    "decision": lambda x: (x == "go").sum() / len(x) * 100
}).round(1)
red_zone_analysis.index = ["Non-Red Zone", "Red Zone"]
red_zone_analysis.columns = ["go_for_it_rate"]

print("Go-for-it rate: Red Zone vs Non-Red Zone")
print(red_zone_analysis)

# Yearly trends for all key metrics
print("\n=== YEARLY TRENDS ANALYSIS ===")

# 1. Yearly success rates
print("1. Success Rate Trends by Year")
yearly_success = go_attempts.groupby("season").agg({
    "fourth_down_converted": ["count", "sum"]
}).round(2)
yearly_success.columns = ["attempts", "successful"]
yearly_success["success_rate"] = (yearly_success["successful"] / yearly_success["attempts"] * 100).round(1)
print(yearly_success[["attempts", "success_rate"]])

# 2. Yearly run vs pass trends
print("\n2. Run vs Pass Trends by Year")
go_attempts["play_strategy"] = go_attempts["play_type"].map(lambda x: "run" if x == "run" else "pass" if x == "pass" else "other")
yearly_strategy = go_attempts.groupby(["season", "play_strategy"]).size().unstack(fill_value=0)
yearly_strategy_pct = yearly_strategy.div(yearly_strategy.sum(axis=1), axis=0) * 100
print("Run vs Pass percentage by year:")
print(yearly_strategy_pct[["run", "pass"]].round(1))

# 3. Yearly field position aggression trends
print("\n3. Field Position Aggression Trends by Year")
fourths["field_position"] = fourths["yardline_100"].apply(categorize_field_position)
yearly_field_aggression = fourths.groupby(["season", "field_position"]).agg({
    "decision": lambda x: (x == "go").sum() / len(x) * 100
}).round(1)
yearly_field_aggression.columns = ["go_for_it_rate"]

# Show midfield and red zone trends specifically
midfield_trends = yearly_field_aggression.loc[(slice(None), ["Own 41-50", "Opp 40-49"]), :].unstack(level=1)
red_zone_trends = yearly_field_aggression.loc[(slice(None), ["Opp 10-19", "Opp 1-9"]), :].unstack(level=1)
print("Midfield go-for-it rate trends:")
print(midfield_trends.round(1))
print("\nRed zone go-for-it rate trends:")
print(red_zone_trends.round(1))

# 4. Yearly time-based aggression trends
print("\n4. Time-Based Aggression Trends by Year")
fourths["time_category"] = fourths["game_seconds_remaining"].apply(categorize_time)
yearly_time_aggression = fourths.groupby(["season", "time_category"]).agg({
    "decision": lambda x: (x == "go").sum() / len(x) * 100
}).round(1)
yearly_time_aggression.columns = ["go_for_it_rate"]

# Show first half vs final 5 minutes trends
time_trends = yearly_time_aggression.loc[(slice(None), ["1st Half", "Final 5 Minutes"]), :].unstack(level=1)
print("First Half vs Final 5 Minutes go-for-it rate trends:")
print(time_trends.round(1))

# Create comprehensive yearly trends visualization
fig9 = px.line(yearly_success.reset_index(), 
               x="season", y="success_rate",
               title="4th Down Success Rate Trends by Year (1999-2024)",
               markers=True)
fig9.write_html("yearly_success_trends.html")
print("Yearly success trends chart saved as yearly_success_trends.html")

# Run vs Pass trends visualization
fig10 = px.line(yearly_strategy_pct.reset_index(), 
                x="season", y=["run", "pass"],
                title="Run vs Pass Strategy Trends by Year (1999-2024)",
                markers=True)
fig10.write_html("yearly_strategy_trends.html")
print("Yearly strategy trends chart saved as yearly_strategy_trends.html")

# Field position trends visualization (midfield focus)
midfield_trends_clean = midfield_trends.reset_index()
midfield_trends_clean.columns = ["season", "Own_41_50", "Opp_40_49"]
fig11 = px.line(midfield_trends_clean, 
                x="season", y=["Own_41_50", "Opp_40_49"],
                title="Midfield 4th Down Aggression Trends by Year (1999-2024)",
                markers=True)
fig11.write_html("yearly_field_position_trends.html")
print("Yearly field position trends chart saved as yearly_field_position_trends.html")

# Time-based trends visualization
time_trends_clean = time_trends.reset_index()
time_trends_clean.columns = ["season", "First_Half", "Final_5_Minutes"]
fig12 = px.line(time_trends_clean, 
                x="season", y=["First_Half", "Final_5_Minutes"],
                title="Time-Based 4th Down Aggression Trends by Year (1999-2024)",
                markers=True)
fig12.write_html("yearly_time_trends.html")
print("Yearly time trends chart saved as yearly_time_trends.html")

# Heatmap Analysis
print("\n=== HEATMAP ANALYSIS ===")

# 1. Field Position vs Distance Heatmap (Go-for-it rates)
print("1. Creating Field Position vs Distance Heatmap")
field_distance_heatmap = fourths.groupby(["field_position", "ydstogo"]).agg({
    "decision": lambda x: (x == "go").sum() / len(x) * 100
}).round(1)
field_distance_heatmap.columns = ["go_for_it_rate"]

# Pivot for heatmap
field_distance_pivot = field_distance_heatmap.unstack(level=1, fill_value=0)
field_distance_pivot.columns = field_distance_pivot.columns.droplevel(0)

# Create heatmap
fig13 = px.imshow(field_distance_pivot, 
                  title="4th Down Go-for-it Rate Heatmap: Field Position vs Distance (1999-2024)",
                  labels=dict(x="Yards to Go", y="Field Position", color="Go-for-it Rate (%)"),
                  aspect="auto")
fig13.write_html("field_distance_heatmap.html")
print("Field position vs distance heatmap saved as field_distance_heatmap.html")

# 2. Field Position vs Distance Heatmap (Success rates)
print("2. Creating Field Position vs Distance Success Rate Heatmap")
go_attempts["field_position"] = go_attempts["yardline_100"].apply(categorize_field_position)
field_distance_success = go_attempts.groupby(["field_position", "ydstogo"]).agg({
    "fourth_down_converted": ["count", "sum"]
}).round(2)
field_distance_success.columns = ["attempts", "successful"]
field_distance_success["success_rate"] = (field_distance_success["successful"] / field_distance_success["attempts"] * 100).round(1)

# Filter for sufficient sample sizes
field_distance_success = field_distance_success[field_distance_success["attempts"] >= 20]
field_distance_success_pivot = field_distance_success["success_rate"].unstack(level=1, fill_value=0)

# Create success rate heatmap
fig14 = px.imshow(field_distance_success_pivot, 
                  title="4th Down Success Rate Heatmap: Field Position vs Distance (1999-2024)",
                  labels=dict(x="Yards to Go", y="Field Position", color="Success Rate (%)"),
                  aspect="auto")
fig14.write_html("field_distance_success_heatmap.html")
print("Field position vs distance success rate heatmap saved as field_distance_success_heatmap.html")

# 3. Time vs Field Position Heatmap
print("3. Creating Time vs Field Position Heatmap")
fourths["time_category"] = fourths["game_seconds_remaining"].apply(categorize_time)
time_field_heatmap = fourths.groupby(["time_category", "field_position"]).agg({
    "decision": lambda x: (x == "go").sum() / len(x) * 100
}).round(1)
time_field_heatmap.columns = ["go_for_it_rate"]

# Pivot for heatmap
time_field_pivot = time_field_heatmap.unstack(level=1, fill_value=0)
time_field_pivot.columns = time_field_pivot.columns.droplevel(0)

# Create time vs field position heatmap
fig15 = px.imshow(time_field_pivot, 
                  title="4th Down Go-for-it Rate Heatmap: Time vs Field Position (1999-2024)",
                  labels=dict(x="Field Position", y="Time in Game", color="Go-for-it Rate (%)"),
                  aspect="auto")
fig15.write_html("time_field_heatmap.html")
print("Time vs field position heatmap saved as time_field_heatmap.html")

# 4. Yearly Trends Heatmap (Field Position)
print("4. Creating Yearly Field Position Trends Heatmap")
yearly_field_heatmap = fourths.groupby(["season", "field_position"]).agg({
    "decision": lambda x: (x == "go").sum() / len(x) * 100
}).round(1)
yearly_field_heatmap.columns = ["go_for_it_rate"]

# Pivot for heatmap
yearly_field_pivot = yearly_field_heatmap.unstack(level=1, fill_value=0)
yearly_field_pivot.columns = yearly_field_pivot.columns.droplevel(0)

# Create yearly field position heatmap
fig16 = px.imshow(yearly_field_pivot, 
                  title="4th Down Go-for-it Rate Heatmap: Year vs Field Position (1999-2024)",
                  labels=dict(x="Field Position", y="Year", color="Go-for-it Rate (%)"),
                  aspect="auto")
fig16.write_html("yearly_field_heatmap.html")
print("Yearly field position heatmap saved as yearly_field_heatmap.html")

# QB Sneak Analysis
print("\n=== QB SNEAK ANALYSIS ===")

# First, let's check what columns we have for QB sneaks
print("Checking available QB sneak columns...")
sample_df = pd.read_parquet('pbp_data/play_by_play_2017.parquet')
qb_sneak_cols = [col for col in sample_df.columns if 'sneak' in col.lower() or 'qb' in col.lower()]
print(f"QB-related columns: {qb_sneak_cols}")

# Load data with QB and rusher information for sneak identification
print("Loading data with QB and rusher information...")
all_fourths_with_sneaks = []

for year in years:
    file_path = f"pbp_data/play_by_play_{year}.parquet"
    if os.path.exists(file_path):
        df = pd.read_parquet(file_path)
        # Include QB and rusher columns for sneak identification
        focus_cols = ["season","week","posteam","defteam","yardline_100","ydstogo","down","play_type","wp","fourth_down_converted","fourth_down_failed","qtr","game_seconds_remaining","passer_player_name","rusher_player_name","desc"]
        available_cols = [col for col in focus_cols if col in df.columns]
        fourths_with_sneaks = df.loc[df["down"] == 4, available_cols].copy()
        all_fourths_with_sneaks.append(fourths_with_sneaks)
        print(f"Loaded {len(fourths_with_sneaks)} 4th downs from {year}")

# Combine all years
fourths_with_sneaks = pd.concat(all_fourths_with_sneaks, ignore_index=True)
print(f"\nTotal 4th downs with QB/rusher data: {len(fourths_with_sneaks)}")

# Categorize decisions
fourths_with_sneaks["decision"] = fourths_with_sneaks["play_type"].map(lambda x: "go" if x in ["run","pass"] else "kick")

# Filter to go-for-it attempts
go_attempts_with_sneaks = fourths_with_sneaks[fourths_with_sneaks["decision"] == "go"].copy()

# Identify QB sneaks: rusher name = passer name AND yards to go <= 2
print("Identifying QB sneaks using rusher = passer method...")

# Debug: Check what we have in the data
print(f"Total go-for-it attempts: {len(go_attempts_with_sneaks)}")
print(f"Attempts with rusher data: {go_attempts_with_sneaks['rusher_player_name'].notna().sum()}")
print(f"Attempts with passer data: {go_attempts_with_sneaks['passer_player_name'].notna().sum()}")
print(f"Attempts with ydstogo <= 2: {(go_attempts_with_sneaks['ydstogo'] <= 2).sum()}")

# Check for exact matches
exact_matches = (go_attempts_with_sneaks["rusher_player_name"] == go_attempts_with_sneaks["passer_player_name"]).sum()
print(f"Exact rusher=passer matches: {exact_matches}")

# More flexible approach: Look for QB sneaks in short yardage situations
# QB sneaks are typically run plays where the QB is the rusher
go_attempts_with_sneaks["is_qb_sneak"] = (
    (go_attempts_with_sneaks["play_type"] == "run") &
    (go_attempts_with_sneaks["ydstogo"] <= 2) &
    (go_attempts_with_sneaks["rusher_player_name"].notna())
)

# Also try the original method for comparison
go_attempts_with_sneaks["is_qb_sneak_original"] = (
    (go_attempts_with_sneaks["rusher_player_name"] == go_attempts_with_sneaks["passer_player_name"]) &
    (go_attempts_with_sneaks["ydstogo"] <= 2) &
    (go_attempts_with_sneaks["rusher_player_name"].notna()) &
    (go_attempts_with_sneaks["passer_player_name"].notna())
)

print(f"QB sneaks (run plays, ydstogo <= 2): {go_attempts_with_sneaks['is_qb_sneak'].sum()}")
print(f"QB sneaks (rusher=passer method): {go_attempts_with_sneaks['is_qb_sneak_original'].sum()}")

# QB Sneak Analysis
total_qb_sneaks_found = go_attempts_with_sneaks["is_qb_sneak"].sum()
print(f"Found {total_qb_sneaks_found} QB sneaks using rusher=passer method")

if total_qb_sneaks_found > 0:
    print("\n1. Overall QB Sneak Statistics")
    total_go_attempts = len(go_attempts_with_sneaks)
    qb_sneaks = go_attempts_with_sneaks[go_attempts_with_sneaks["is_qb_sneak"] == True]
    total_qb_sneaks = len(qb_sneaks)
    
    print(f"Total go-for-it attempts: {total_go_attempts}")
    print(f"Total QB sneaks: {total_qb_sneaks}")
    print(f"QB sneak percentage: {(total_qb_sneaks/total_go_attempts*100):.1f}%")
    
    # QB Sneak success rate
    if total_qb_sneaks > 0:
        qb_sneak_successful = qb_sneaks["fourth_down_converted"].sum()
        qb_sneak_success_rate = (qb_sneak_successful / total_qb_sneaks) * 100
        print(f"QB sneak success rate: {qb_sneak_success_rate:.1f}%")
        
        # Compare to non-sneak attempts
        non_sneaks = go_attempts_with_sneaks[go_attempts_with_sneaks["is_qb_sneak"] == False]
        non_sneak_successful = non_sneaks["fourth_down_converted"].sum()
        non_sneak_success_rate = (non_sneak_successful / len(non_sneaks)) * 100 if len(non_sneaks) > 0 else 0
        print(f"Non-sneak success rate: {non_sneak_success_rate:.1f}%")
        
        # QB Sneak by distance
        print("\n2. QB Sneak by Distance")
        qb_sneak_distance = qb_sneaks.groupby("ydstogo").agg({
            "fourth_down_converted": ["count", "sum"]
        }).round(2)
        qb_sneak_distance.columns = ["attempts", "successful"]
        qb_sneak_distance["success_rate"] = (qb_sneak_distance["successful"] / qb_sneak_distance["attempts"] * 100).round(1)
        qb_sneak_distance = qb_sneak_distance[qb_sneak_distance["attempts"] >= 5]  # Min 5 attempts
        print("QB Sneak success rate by distance:")
        print(qb_sneak_distance)
        
        # Yearly QB Sneak trends
        print("\n3. Yearly QB Sneak Trends")
        yearly_qb_sneaks = go_attempts_with_sneaks.groupby("season").agg({
            "is_qb_sneak": ["count", "sum"]
        }).round(2)
        yearly_qb_sneaks.columns = ["total_attempts", "qb_sneaks"]
        yearly_qb_sneaks["qb_sneak_pct"] = (yearly_qb_sneaks["qb_sneaks"] / yearly_qb_sneaks["total_attempts"] * 100).round(1)
        
        # QB Sneak success rate by year
        yearly_qb_sneak_success = qb_sneaks.groupby("season").agg({
            "fourth_down_converted": ["count", "sum"]
        }).round(2)
        yearly_qb_sneak_success.columns = ["attempts", "successful"]
        yearly_qb_sneak_success["success_rate"] = (yearly_qb_sneak_success["successful"] / yearly_qb_sneak_success["attempts"] * 100).round(1)
        
        print("Yearly QB sneak trends:")
        print(yearly_qb_sneaks[["total_attempts", "qb_sneaks", "qb_sneak_pct"]])
        print("\nYearly QB sneak success rates:")
        print(yearly_qb_sneak_success[["attempts", "success_rate"]])
        
        # Create visualizations
        fig17 = px.bar(qb_sneak_distance.reset_index(), 
                      x="ydstogo", y="success_rate",
                      title="QB Sneak Success Rate by Distance (1999-2024)",
                      labels={"ydstogo": "Yards to Go", "success_rate": "Success Rate (%)"})
        fig17.write_html("qb_sneak_success_by_distance.html")
        print("QB sneak success by distance chart saved as qb_sneak_success_by_distance.html")
        
        fig18 = px.line(yearly_qb_sneaks.reset_index(), 
                       x="season", y="qb_sneak_pct",
                       title="QB Sneak Usage Trends by Year (1999-2024)",
                       markers=True)
        fig18.write_html("qb_sneak_usage_trends.html")
        print("QB sneak usage trends chart saved as qb_sneak_usage_trends.html")
        
        fig19 = px.line(yearly_qb_sneak_success.reset_index(), 
                       x="season", y="success_rate",
                       title="QB Sneak Success Rate Trends by Year (1999-2024)",
                       markers=True)
        fig19.write_html("qb_sneak_success_trends.html")
        print("QB sneak success trends chart saved as qb_sneak_success_trends.html")
        
else:
    print("QB sneak column not found. Let's try to identify sneaks from play descriptions...")
    
    # Alternative: Try to identify sneaks from play descriptions
    if "desc" in fourths_with_sneaks.columns:
        print("Analyzing play descriptions for QB sneaks...")
        # Look for common QB sneak patterns in descriptions
        sneak_patterns = ["sneak", "qb sneak", "quarterback sneak"]
        fourths_with_sneaks["is_sneak"] = fourths_with_sneaks["desc"].str.lower().str.contains("|".join(sneak_patterns), na=False)
        
        total_sneaks = fourths_with_sneaks["is_sneak"].sum()
        print(f"Found {total_sneaks} potential QB sneaks from play descriptions")
        
        if total_sneaks > 0:
            sneaks = fourths_with_sneaks[fourths_with_sneaks["is_sneak"] == True]
            sneak_successful = sneaks["fourth_down_converted"].sum()
            sneak_success_rate = (sneak_successful / total_sneaks) * 100
            print(f"QB sneak success rate (from descriptions): {sneak_success_rate:.1f}%")
    else:
        print("No QB sneak data available in this dataset")
