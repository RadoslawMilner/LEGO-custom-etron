# 4x4 skid-steer drive with acceleration control using Xbox Controller
# Each wheel independent; left joystick = steering, triggers = throttle/brake

# MASTER HUB
# Rear axle drive + Xbox + BLE broadcast

from pybricks.hubs import ThisHub
from pybricks.iodevices import XboxController
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

hub = ThisHub(broadcast_channel=1)

# --- REAR MOTORS ---
rear_left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
rear_right = Motor(Port.A, Direction.CLOCKWISE)

# --- Controller setup ---
xbox = XboxController()

# --- Acceleration parameters ---
left_power = 0
right_power = 0
step = 10 # acceleration increment per loop
delay = 50 # loop delay in ms

while True:
    # steering based on left joystick
    steer = xbox.joystick_left()[0] # left stick X: -100..100

    # Forward/backward based on triggers
    triggers = xbox.triggers() # (left, right), each 0..100
    drive = triggers[1] - triggers[0] # right = forward, left = backward

    # Base target power with Applied steering (skid-steer style) and clamped it to [-100, 100]
    target_left = max(min(drive + steer, 100), -100)
    target_right = max(min(drive - steer, 100), -100)

    # Smooth acceleration (ramp up/down)
    if left_power < target_left:
        left_power = min(left_power + step, target_left)
    elif left_power > target_left:
        left_power = max(left_power - step, target_left)

    if right_power < target_right:
        right_power = min(right_power + step, target_right)
    elif right_power > target_right:
        right_power = max(right_power - step, target_right)

    # rear drive motors
    rear_left.dc(left_power)
    rear_right.dc(right_power)

    hub.ble.broadcast((left_power, right_power))

    wait(delay)