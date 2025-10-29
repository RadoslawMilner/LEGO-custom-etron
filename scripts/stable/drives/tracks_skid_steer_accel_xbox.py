# 4x4 skid-steer drive with acceleration control using Xbox Controller
# Each wheel independent; left joystick = steering, triggers = throttle/brake

from pybricks.iodevices import XboxController
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.tools import wait

# --- Motor setup ---
front_left = Motor(Port.D, Direction.COUNTERCLOCKWISE)
front_right = Motor(Port.C, Direction.CLOCKWISE)
rear_left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
rear_right = Motor(Port.A, Direction.CLOCKWISE)

# --- Controller setup ---
xbox = XboxController()

# --- Acceleration parameters ---
left_power = 0
right_power = 0
target_left = 0
target_right = 0
step = 10     # acceleration increment per loop
delay = 50    # loop delay in ms

# --- Main loop ---
while True:
    # Read inputs
    steer = xbox.joystick_left()[0]     # left stick X: -100..100
    triggers = xbox.triggers()          # (left, right), each 0..100

    # Forward/backward based on triggers
    drive = triggers[1] - triggers[0]   # right = forward, left = backward

    # Base target power
    target_left = drive
    target_right = drive

    # Apply steering (skid-steer style)
    target_left += steer
    target_right -= steer

    # Clamp to [-100, 100]
    target_left = max(min(target_left, 100), -100)
    target_right = max(min(target_right, 100), -100)

    # Smooth acceleration (ramp up/down)
    if left_power < target_left:
        left_power = min(left_power + step, target_left)
    elif left_power > target_left:
        left_power = max(left_power - step, target_left)

    if right_power < target_right:
        right_power = min(right_power + step, target_right)
    elif right_power > target_right:
        right_power = max(right_power - step, target_right)

    # Drive motors
    front_left.dc(left_power)
    rear_left.dc(left_power)
    front_right.dc(right_power)
    rear_right.dc(right_power)

    wait(delay)
