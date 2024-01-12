import pandas as pd
pd.set_option('display.max_columns', None)
pd.options.mode.chained_assignment = None

df = pd.read_csv("data/all_fixtures_all_days_across_71_leagues.csv")
df.drop(columns=["Unnamed: 0", "season"], inplace=True)


df1 = df[df["match_status"] == "Match Finished"]
df1 = df1.drop(columns=["match_status"])

f1 = input("Choose your first team: ")
print("\n")
f2 = input("Choose your second team: ")
print("\n")


# Get the last 6 fixtures for both home and away teams
last_5_home_team_fixtures = df1[(df1['home_team'].astype(str).str.lower() == f1.lower()) | (
    df1['away_team'].astype(str).str.lower() == f1.lower())].sort_values(by='date', ascending=False).head(5)

last_5_home_team_fixtures['home_team_score'] = pd.to_numeric(
    last_5_home_team_fixtures['home_team_score'], errors='coerce').astype('Int64')
last_5_home_team_fixtures['away_team_score'] = pd.to_numeric(
    last_5_home_team_fixtures['away_team_score'], errors='coerce').astype('Int64')

last_5_home_team_fixtures["date"] = last_5_home_team_fixtures["date"].str[:10]
#
last_5_away_team_fixtures = df1[(df1['home_team'].astype(str).str.lower() == f2.lower()) | (
    df1['away_team'].astype(str).str.lower() == f2.lower())].sort_values(by='date', ascending=False).head(5)

last_5_away_team_fixtures['home_team_score'] = pd.to_numeric(
    last_5_away_team_fixtures['home_team_score'], errors='coerce').astype('Int64')
last_5_away_team_fixtures['away_team_score'] = pd.to_numeric(
    last_5_away_team_fixtures['away_team_score'], errors='coerce').astype('Int64')
last_5_away_team_fixtures["date"] = last_5_away_team_fixtures["date"].str[:10]


print(last_5_away_team_fixtures)
print("\n")
print(last_5_home_team_fixtures)
