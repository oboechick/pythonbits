# step 1: make a timer. Check.
# Step 1.5: Make a loop to go 3 times.
# step 2: create action that pops up browser. Check.
# step 3: find a song to put into browser
import webbrowser
import time

print("This was started at" + time.ctime())
times_run = 0
while times_run <= 2:
	time.sleep(7200) #Two hours will be 7200
	webbrowser.open('https://www.youtube.com/watch?v=3oc1XuqzyGs')
	times_run = times_run + 1