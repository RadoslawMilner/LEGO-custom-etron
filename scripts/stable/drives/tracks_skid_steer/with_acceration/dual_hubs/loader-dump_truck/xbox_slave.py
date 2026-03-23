# Slave hub for dual-hub loader system.
#
# Responsibilities:
# - Receives control data via BLE from master hub
# - Drives front axle motors (mirrors rear drive)
# - Controls front spoon (lift mechanism) using incremental target positioning
#
# Input (from master via BLE):
# - left_power  → power for left track
# - right_power → power for right track
# - spoon_step  → incremental step for spoon angle
#
# Notes:
# - Slave does NOT interpret controller input (no Xbox here)
# - Slave enforces mechanical limits and executes motion
# - Angle is relative (reset at startup)

from pybricks.hubs import ThisHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

hub = ThisHub(observe_channels=[1])

# --- FRONT DRIVE MOTORS ---
front_left = Motor(Port.D, Direction.COUNTERCLOCKWISE)
front_right = Motor(Port.C, Direction.CLOCKWISE)

# --- SPOON MOTOR (front lift) ---
front_spoon = Motor(Port.A, Direction.CLOCKWISE)
front_spoon.reset_angle(0)

# --- SPOON LIMITS ---
SPOON_MIN = 0       # base position (aligned with chassis)
SPOON_MAX = 130     # max lift angle (dump position)

# --- CONTROL PARAMS ---
SPOON_SPEED = 200   # deg/s
DELAY = 50          # loop delay (ms)

# --- STATE ---
spoon_target = 0


while True:
    data = hub.ble.observe(1)

    if data is not None:
        left_power, right_power, spoon_step = data

        # --- DRIVE (mirror master) ---
        front_left.dc(left_power)
        front_right.dc(right_power)

        # --- SPOON CONTROL ---
        spoon_target += spoon_step
        spoon_target = max(min(spoon_target, SPOON_MAX), SPOON_MIN)

        front_spoon.run_target(SPOON_SPEED, spoon_target, wait=False)

    else:
        # safety fallback if signal lost
        front_left.dc(0)
        front_right.dc(0)

    wait(DELAY)