import datetime
import time

def start_countdown(target_time):
    """Runs a countdown timer until the target datetime is reached."""
    while True:
        current_time = datetime.datetime.now()
        time_remaining = target_time - current_time

        if time_remaining.total_seconds() <= 0:
            print("\n🎉 Countdown Complete! 🎉")
            break

        days = time_remaining.days
        hours, remainder = divmod(time_remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        print(f"\r⏳ Time Left: {days} days, {hours:02} hours, {minutes:02} minutes, {seconds:02} seconds", end="")
        time.sleep(1)

# Set the countdown target date and time
target_datetime = datetime.datetime(2025, 3, 2, 23, 0, 0)

# Start the countdown
start_countdown(target_datetime)
