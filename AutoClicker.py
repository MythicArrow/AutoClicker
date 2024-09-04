import pyautogui
import time
import keyboard

interval = int(input("Write the interval "))
duration = int(input("Write the duration "))
end_time = time.time() + duration


print("Auto-clicker started. Press 'q' to stop.")

try:
    while time.time() < end_time:
        if keyboard.is_pressed('q'):
            print("Auto-clicker stopped.")
            break
        pyautogui.click()
        time.sleep(interval)
except KeyboardInterrupt:
    print("Auto-clicker stopped.")

print("Done!")