## CONFIG
#########
# MONITORS:
#   Monitors from left to right, position is measured from left top corner of canvas encompassing screens
#   for both px and mm, order of size is of no matter and the screen that determinates the size for one
#   measure can be or not the same that does it for the other
#
#(0,0)_____________________________________________
#     |                   |                       |
#     |___________________|                       |
#     |                   |                       |
#     |    Screen 1       |        Screen 2       |
#     |___________________|_______________________|
#
# The values are
# [ height_in_px, position_x_px, position_y_px, height_in_mm, position_y_mm ]
MONITORS = [
    [1080, 0, 0, 290, 100],
    [768, 1920, 312, 390, 0]
]

# GAP:
#   pixels on border on which if the pointer is present it will jump to the other side
GAP = 15

# INTERVAL:
#   seconds the script will wait between checking pointer position,
#   more time reduces cpu usage but may cause the pointer to not jump when wanted
INTERVAL = 0.25

# COOL_DOWN:
#   seconds the script will not work after jumping (you may want it if you want to use the mouse near the border)
COOL_DOWN = 0

################################################################################
#  DON'T CHANGE ANYTHING BELLOW THIS POINT WITHOUT KNOWING WHAT YOU ARE DOING  #
################################################################################

## SCRIPT
#########

import time
import pyautogui


def px_to_mm(monitor, y):
    return (y-monitor[2])*(monitor[3])/monitor[0] + monitor[4]

def mm_to_px(monitor, y):
    return (y-monitor[4])*(monitor[0])/monitor[3] + monitor[2]

while True:
    try:
        current_pos = pyautogui.position()
        for i in range(len(MONITORS)-1):
            left = MONITORS[i]
            right = MONITORS[i+1]

            # Move left to right
            if right[1] - GAP < current_pos.x < right[1]:
                mm = px_to_mm(left, current_pos.y)
                new_y = mm_to_px(right, mm)
                pyautogui.moveTo(right[1] + GAP, new_y)
                time.sleep(COOL_DOWN)

            # Move right to left
            elif right[1] < current_pos.x < right[1] + GAP:
                mm = px_to_mm(right, current_pos.y)
                new_y = mm_to_px(left, mm)
                pyautogui.moveTo(right[1] - GAP, new_y)
                time.sleep(COOL_DOWN)

    except KeyboardInterrupt:
        break
