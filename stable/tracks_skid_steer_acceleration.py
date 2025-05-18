# tank build
# simple and effective
# 4x4 direct drive with skid steering
# added acceleration system

from pybricks.parameters import Button, Direction, Port
from pybricks.pupdevices import Motor, Remote  # remote-control-88010
from pybricks.tools import wait

# Motors setup
front_left = Motor(Port.D, Direction.COUNTERCLOCKWISE)
front_right = Motor(Port.C, Direction.CLOCKWISE)
rear_left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
rear_right = Motor(Port.A, Direction.CLOCKWISE)

remote = Remote(timeout=None)

# Acceleration logic
left_power = 0
right_power = 0
target_left = 0
target_right = 0
step = 10  # acceleration rate
delay = 50  # loop delay in ms

# Main loop
while True:
    buttons = remote.buttons.pressed()

    # Determine target power based on remote buttons
    if Button.RIGHT_PLUS in buttons:
        target_left = 100
        target_right = 100
    elif Button.RIGHT_MINUS in buttons:
        target_left = -100
        target_right = -100
    else:
        target_left = 0
        target_right = 0

    # Skid steering (turn in place or while moving)
    if Button.LEFT_PLUS in buttons:
        target_left -= 100
        target_right += 100
    elif Button.LEFT_MINUS in buttons:
        target_left += 100
        target_right -= 100

    # Clamp values to [-100, 100]
    target_left = max(min(target_left, 100), -100)
    target_right = max(min(target_right, 100), -100)

    # Apply acceleration (ramp current power to target)
    if left_power < target_left:
        left_power += step
        if left_power > target_left:
            left_power = target_left
    elif left_power > target_left:
        left_power -= step
        if left_power < target_left:
            left_power = target_left

    if right_power < target_right:
        right_power += step
        if right_power > target_right:
            right_power = target_right
    elif right_power > target_right:
        right_power -= step
        if right_power < target_right:
            right_power = target_right

    # Apply motor power
    front_left.dc(left_power)
    rear_left.dc(left_power)
    front_right.dc(right_power)
    rear_right.dc(right_power)

    wait(delay)
  
