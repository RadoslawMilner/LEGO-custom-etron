# Master hub for dual-hub loader-dump system.
#
# Responsibilities:
# - Reads Xbox Controller input
# - Controls rear axle (skid-steer with acceleration ramp)
# - Sends drive + front spoon commands via BLE broadcast
#
# Controls:
# - Left joystick X → steering
# - Triggers → throttle / brake
# - D-Pad UP / DOWN → front spoon (handled by slave)
#
# Notes:
# - Rear dump tub temporarily disabled (code scaffold left for future use)
# - BLE payload: (left_power, right_power, spoon_step)

from pybricks.hubs import ThisHub
from pybricks.iodevices import XboxController
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Button
from pybricks.tools import wait

hub = ThisHub(broadcast_channel=1)

# --- REAR DRIVE MOTORS ---
rear_left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
rear_right = Motor(Port.A, Direction.CLOCKWISE)

# --- TUB MOTOR (rear dump) ---
# rear_tub = Motor(Port.D, Direction.CLOCKWISE)

# --- CONTROLLER ---
xbox = XboxController()

# --- DRIVE PARAMS ---
left_power = 0
right_power = 0
STEP = 10     # acceleration increment per loop
DELAY = 50    # loop delay (ms)

# --- SPOON CONTROL (sent to slave) ---
SPOON_STEP = 2   # degrees per loop (digital step via D-Pad)

# --- TUB PARAMS ---
# TUB_MIN = 0
# TUB_MAX = 90
# TUB_STEP = 2
# TUB_SPEED = 200
# tub_target = 0


def get_spoon_step():
    pressed = xbox.buttons.pressed()

    if Button.UP in pressed:
        return SPOON_STEP
    elif Button.DOWN in pressed:
        return -SPOON_STEP
    return 0


while True:
    # --- DRIVE CONTROL ---
    steer = xbox.joystick_left()[0]       # -100..100
    triggers = xbox.triggers()            # (left, right)
    drive = triggers[1] - triggers[0]     # forward/backward

    target_left = max(min(drive + steer, 100), -100)
    target_right = max(min(drive - steer, 100), -100)

    # --- ACCELERATION RAMP ---
    if left_power < target_left:
        left_power = min(left_power + STEP, target_left)
    elif left_power > target_left:
        left_power = max(left_power - STEP, target_left)

    if right_power < target_right:
        right_power = min(right_power + STEP, target_right)
    elif right_power > target_right:
        right_power = max(right_power - STEP, target_right)

    # --- APPLY DRIVE ---
    rear_left.dc(left_power)
    rear_right.dc(right_power)

    # --- SPOON COMMAND (for slave) ---
    spoon_step = get_spoon_step()

    # --- BLE BROADCAST ---
    hub.ble.broadcast((left_power, right_power, spoon_step))

    wait(DELAY)