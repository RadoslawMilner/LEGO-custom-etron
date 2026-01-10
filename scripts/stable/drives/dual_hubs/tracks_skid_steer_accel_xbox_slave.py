# 4x4 skid-steer drive with acceleration control using Xbox Controller
# Each wheel independent; left joystick = steering, triggers = throttle/brake

# SLAVE HUB
# Front axle drive + BLE observe

from pybricks.hubs import ThisHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

hub = ThisHub(observe_channels=[1])

# --- FRONT MOTORS ---
front_left = Motor(Port.D, Direction.COUNTERCLOCKWISE)
front_right = Motor(Port.C, Direction.CLOCKWISE)

delay = 50

while True:
    data = hub.ble.observe(1)

    if data is not None:
        left_power, right_power = data
        front_left.dc(left_power)
        front_right.dc(right_power)
    else:
        front_left.dc(0)
        front_right.dc(0)

    wait(delay)