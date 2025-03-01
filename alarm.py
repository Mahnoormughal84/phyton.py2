#part 12
#easy


from time import playsound
import time

def alarm(seconds):
    time_elapsed = 0

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{minutes_left}:{seconds_left}")

    # Play the alarm sound when the countdown ends
    playsound("path/to/alarm.mp3")  # Replace with the correct path

# Example: 10-second timer
alarm(10)
