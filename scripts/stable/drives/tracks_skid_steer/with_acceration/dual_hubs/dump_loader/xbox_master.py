# MASTER HUB
# 4x4 skid-steer dump loader (both axles)
# Xbox Controller input:
#   - Left stick: X = steering, Y = throttle
#   - Triggers: control bucket (analog, +/- step mapped)
#   - Bumpers: control tub (digital, fixed step)
# BLE broadcast:
#   - Sends bucket and tub step commands to SLAVE HUB
# Notes:
#   - bucket_step: float degrees per loop
#   - tub_step: digital +/- fixed step
#   - Smooth drive acceleration applied
#   - No homing/calibration implemented (positions relative to start)

from pybricks.hubs import ThisHub
from pybricks.iodevices import XboxController
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Button
from pybricks.tools import wait

hub = ThisHub(broadcast_channel=1)
xbox = XboxController()

# --- DRIVE MOTORS ---
rear_left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
rear_right = Motor(Port.A, Direction.CLOCKWISE)
front_left = Motor(Port.D, Direction.COUNTERCLOCKWISE)
front_right = Motor(Port.C, Direction.CLOCKWISE)

# --- DRIVE PARAMS ---
left_power = 0
right_power = 0
step = 10
delay = 50

# --- BUCKET PARAMS ---
BUCKET_STEP_MAX = 8     # max degrees per loop (full trigger)
BUCKET_DEADZONE = 5

# --- TUB PARAMS ---
TUB_STEP = 5


def apply_deadzone(value, zone):
    return 0 if abs(value) < zone else value


def get_bucket_step():
    left_trigger, right_trigger = xbox.triggers()

    # analog difference
    value = right_trigger - left_trigger

    if abs(value) < BUCKET_DEADZONE:
        return 0

    # map 0..100 → 0..BUCKET_STEP_MAX
    step = (value / 100) * BUCKET_STEP_MAX
    return step


def get_tub_step():
    pressed = xbox.buttons.pressed()

    if Button.RB in pressed:
        return TUB_STEP
    elif Button.LB in pressed:
        return -TUB_STEP
    return 0


while True:

    # --- DRIVE (left stick full control) ---
    steer = xbox.joystick_left()[0]
    throttle = xbox.joystick_left()[1]

    target_left = max(min(throttle + steer, 100), -100)
    target_right = max(min(throttle - steer, 100), -100)

    if left_power < target_left:
        left_power = min(left_power + step, target_left)
    elif left_power > target_left:
        left_power = max(left_power - step, target_left)

    if right_power < target_right:
        right_power = min(right_power + step, target_right)
    elif right_power > target_right:
        right_power = max(right_power - step, target_right)

    rear_left.dc(left_power)
    rear_right.dc(right_power)
    front_left.dc(left_power)
    front_right.dc(right_power)

    # --- ACTUATOR COMMANDS ---
    bucket_step = get_bucket_step()
    tub_step = get_tub_step()

    hub.ble.broadcast((bucket_step, tub_step))

    wait(delay)