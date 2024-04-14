import sys
from time import sleep
import time

def print_lyrics():
    lines = [
    ("No matter what come between us,", 0.05),
    ("yeah, I decided", 0.04),
    ("I'm forever ridin',", 0.05),
    ("you're forever guidin'", 0.05),
    ("Pull up on an opp,", 0.04),
    ("hit his curb up, slide it", 0.06),
    ("Notice when you mad, ", 0.05),
    ("ain't no words, just silence ", 0.04),
    ("You my favorite color,", 0.03),
    ("now you seein' every shade of me", 0.02),
    ("You say that I'm trippin',", 0.025),
    ("I hit back like, 'Where you takin' me?'", 0.025),
    ("Locked in for life, on God, no replacin' me", 0.025),
    ("Consequences, repercussions, karma keep on changin' me", 0.02)
]

    i = 0
    delays = [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.6, 0.4, 0.3, 0.2, 0.2, 0.3, 0.3, 0.3, 0.3]
    for line, delay in lines:
        for char in line:
            print(char, end='', flush=True)
            sleep(delay)
        time.sleep(delays[i])
        i += 1
        print()

print_lyrics()