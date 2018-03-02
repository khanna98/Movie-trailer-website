import webbrowser
import time

print("This program started on "+time.ctime())
for i in range(0,3):
		time.sleep(10)
		webbrowser.open("https://www.youtube.com/")
