import webbrowser
import time

count = 0
breaks = 3

# Ed Sheeran - Shape of You [Official Video]
video = "https://www.youtube.com/watch?v=JGwWNGJdvx8&index=4&list=PLMC9KNkIncKt\
PzgY-5rmhvj7fax8fdxoj"

wait = 60

print "This program started on: " + time.ctime()
while count < breaks:
    time.sleep(wait)
    webbrowser.open(video)
    count += 1
