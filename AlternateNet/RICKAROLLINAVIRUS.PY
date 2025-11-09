import webbrowser
import time as t
ask = input("Are you sure to continue?(Y/N):")
if ask=="Y":
    url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    print("Loading this super-duper-muper-zuper operation...")
    t.sleep(5)
    print(":>")

    webbrowser.open(url)
elif ask=="N":
    print("Ah, you are safe... for now.")
else:
    print("I diden't got a shit!")