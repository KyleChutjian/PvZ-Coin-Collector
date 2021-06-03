import cv2
import pyautogui
from WindowCapture import WindowCapture
from Vision import Vision
from time import sleep

try:
    # Instantiating the WindowCapture
    pvz_window = WindowCapture("Plants vs. Zombies")
except:
    # If no window detected, stop program
    print("No Plants vs. Zombies window detected!")
    quit()
# Instantiating the silver coin Vision object
vision_silver = Vision("pictures/silver_coin.jpg")
# Instantiating the gold coin Vision object
vision_gold = Vision("pictures/gold_coin.jpg")

print("Waiting for \"k\" to be pressed.")

while True:
    # Updates second window with green rectangles
    screenshot = pvz_window.get_screenshot()
    silver_points = vision_silver.find(screenshot, 0.55, 'rectangles')
    gold_points = vision_gold.find(vision_silver.get_image(), 0.55, 'rectangles')

    # If "K" is pressed, exit loop
    if cv2.waitKey(1) == ord('k'):
        break

while True:
    # Updates the screenshot with green rectangles
    screenshot = pvz_window.get_screenshot()
    silver_points = vision_silver.find(screenshot, 0.55, 'rectangles')
    gold_points = vision_gold.find(vision_silver.get_image(), 0.55, 'rectangles')

    # Checks if there is a rectangle on screen
    if len(gold_points) > 0:
        # Gets the center x,y points and clicks that position
        x = gold_points[0][0] + pvz_window.offset_x
        y = gold_points[0][1] + pvz_window.offset_y
        print('Moving mouse to x:{} y:{}'.format(x, y))
        pyautogui.moveTo(x=x, y=y)
        pyautogui.click()
    elif len(silver_points) > 0:
        # Gets the center x,y points and clicks that position
        x = silver_points[0][0] + pvz_window.offset_x
        y = silver_points[0][1] + pvz_window.offset_y
        print('Moving mouse to x:{} y:{}'.format(x, y))
        if y > pvz_window.offset_y + 120:
            pyautogui.moveTo(x=x, y=y)
            pyautogui.click()
    else:
        # No rectangles found, program stops for 5 seconds allowing you to stop it
        print("sleeping")
        sleep(5)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break
