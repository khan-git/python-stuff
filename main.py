"""
Story teller
"""
import os
from story import story

CURR_POINT = 'point1'
STORY_CONTINUES = True
while STORY_CONTINUES:
    os.system('clear')
    point: dict = story.get(CURR_POINT)
    print(f"{CURR_POINT}: {point.get('Q')}")
    for a in point.get('A').keys():
        print(a)
    answer = input("? ").strip().lower().capitalize()
    if answer in point.get('A').keys():
        next_point = point.get('A').get(answer)
        if next_point == "exit":
            STORY_CONTINUES = False
        else:
            CURR_POINT = next_point if next_point in story.keys() else CURR_POINT
