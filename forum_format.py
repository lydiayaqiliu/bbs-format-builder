#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Converted to Python 3
Original: 2017-11-25, Updated: 2022-03-09
Author: matrixk 
Converted by: Lydia Liu
"""
import random
from datetime import datetime, timedelta

FLUFLUC = [
    2.73, 1.66, 1.10, 0.60, 0.14, 0.05, 0.24, 1.64, 3.32, 4.81, 5.56, 5.64,
    5.53, 5.57, 5.83, 6.00, 6.13, 5.81, 5.68, 6.39, 6.79, 6.59, 5.77, 4.25
]

def fluctuation(hour_flu: int) -> float:
    """Return per-floor expected minute range scaled by the hour-of-day."""
    standard = 30.0
    return standard / FLUFLUC[int(hour_flu) % 24]

def forum_format(date_str: str, hour_start: str, min_start: str, sec_start: str, floor: int) -> None:
    """
    Generate forum-like timestamp blocks from a start date/time over N floors.
    Writes to 'forum_format.md'.
    """
    start_dt = datetime.strptime(
        f"{date_str} {hour_start}:{min_start}:{sec_start}",
        "%Y-%m-%d %H:%M:%S"
    )

    floor_number = 0
    with open("forum_format.md", "w", encoding="utf-8") as f:
        for _ in range(floor_number, int(floor) + 1):
            dt = start_dt
            line = (
                f"№{floor_number} ★★★= =于 "
                f"{dt.strftime('%Y-%m-%d')} "
                f"{dt.strftime('%H:%M:%S')}留言★★★"
            )
            f.write(line + "\n\n----------\n\n\n\n")

            standard = fluctuation(dt.hour)
            sec_inc = random.randint(1, 59)
            min_inc = random.randint(1, max(1, int(standard)))
            start_dt = start_dt + timedelta(minutes=min_inc, seconds=sec_inc)

            floor_number += 1

if __name__ == "__main__":
    date_input = input("date (YYYY-MM-DD): ").strip()
    time_start = input("publish time of the first floor (HH:MM:SS): ").strip()
    hour_input, min_input, sec_input = time_start[0:2], time_start[3:5], time_start[6:8]
    floor_input = int(input("floor (inclusive, starting from 0): ").strip())
    forum_format(date_input, hour_input, min_input, sec_input, floor_input)
