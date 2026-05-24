#!/usr/bin/env python3
"""
הרץ פעם אחת כדי למחוק תחנות שלא גאוקודדו (null) מ-coords.json
כדי שה-Action ינסה אותן מחדש עם queries משופרות.
"""
import json, os

OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "coords.json")
if not os.path.exists(OUTPUT):
    print("coords.json not found")
    exit()

with open(OUTPUT, "r", encoding="utf-8") as f:
    coords = json.load(f)

before = len(coords)
coords = {k: v for k, v in coords.items() if v is not None}
after = len(coords)

with open(OUTPUT, "w", encoding="utf-8") as f:
    json.dump(coords, f, ensure_ascii=False)

print(f"Removed {before - after} null entries. {after} remain.")
