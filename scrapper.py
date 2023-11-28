import pandas as pd
import sqlite3
from datetime import date, timedelta

from main import *

conn = sqlite3.connect("db/data.db")


def check_if_table_exists(table_name: str) -> bool:
    cursor = conn.cursor()

    cursor.execute(f"SELECT count(name) FROM sqlite_master WHERE type='table' AND name='{table_name}'")

    # If the count is 1, then table exists
    if cursor.fetchone()[0] == 1:
        return True

    return False


start_date_year = 2015
start_date_month = 10
mend_date_year = 2016
mend_date_month = 1
end_date = date.today()
start_date = date(start_date_year, start_date_month, 1)
metric_end_date = date(mend_date_year, mend_date_month, 1)
while metric_end_date <= end_date:
    sd_str = start_date.strftime("%Y-%m-%d")
    med_str = metric_end_date.strftime("%Y-%m-%d")
    print(sd_str, "to", med_str)

    # All rankings
    table_name = f"stats_{sd_str}_{med_str}_all"
    if not check_if_table_exists(table_name):
        player_stats = top_players_full(start_date, metric_end_date, 0)
        print(len(player_stats), "players parsed (All rankings).")
        df = pd.DataFrame.from_dict(player_stats)
        df.to_sql(table_name, conn)
    else:
        print(table_name, "exists.")

    # Top-5
    table_name = f"stats_{sd_str}_{med_str}_top_5"
    if not check_if_table_exists(table_name):
        player_stats = top_players_full(start_date, metric_end_date, 5)
        print(len(player_stats), "players parsed (top-5).")
        df = pd.DataFrame.from_dict(player_stats)
        df.to_sql(table_name, conn)
    else:
        print(table_name, "exists.")

    # Top-10
    table_name = f"stats_{sd_str}_{med_str}_top_10"
    if not check_if_table_exists(table_name):
        player_stats = top_players_full(start_date, metric_end_date, 10)
        print(len(player_stats), "players parsed (top-10).")
        df = pd.DataFrame.from_dict(player_stats)
        df.to_sql(table_name, conn)
    else:
        print(table_name, "exists.")

    # Top-20
    table_name = f"stats_{sd_str}_{med_str}_top_20"
    if not check_if_table_exists(table_name):
        player_stats = top_players_full(start_date, metric_end_date, 20)
        print(len(player_stats), "players parsed (top-20).")
        df = pd.DataFrame.from_dict(player_stats)
        df.to_sql(table_name, conn)
    else:
        print(table_name, "exists.")

    # Top-30
    table_name = f"stats_{sd_str}_{med_str}_top_30"
    if not check_if_table_exists(table_name):
        player_stats = top_players_full(start_date, metric_end_date, 30)
        print(len(player_stats), "players parsed (top-30).")
        df = pd.DataFrame.from_dict(player_stats)
        df.to_sql(table_name, conn)
    else:
        print(table_name, "exists.")

    # Top-50
    table_name = f"stats_{sd_str}_{med_str}_top_50"
    if not check_if_table_exists(table_name):
        player_stats = top_players_full(start_date, metric_end_date, 50)
        print(len(player_stats), "players parsed (top-50).")
        df = pd.DataFrame.from_dict(player_stats)
        df.to_sql(table_name, conn)
    else:
        print(table_name, "exists.")

    start_date_month += 3
    if start_date_month > 12:
        start_date_month = 1
        start_date_year += 1

    mend_date_month += 3
    if mend_date_month > 12:
        mend_date_month = 1
        mend_date_year += 1

    start_date = date(start_date_year, start_date_month, 2)
    metric_end_date = date(mend_date_year, mend_date_month, 1)


conn.close()