# This program is designed to use 3 motors for the rear drive
# Those 3 motoros must be build with diffential
# Front is driveless. Front 4th motor is for turning.

from pybricks.parameters import Button, Direction, Port
from pybricks.pupdevices import Motor, Remote
from pybricks.tools import wait

# Set up motors
steering = Motor(Port.C, Direction.CLOCKWISE)
rear_1 = Motor(Port.A)
rear_2 = Motor(Port.B)
rear_3 = Motor(Port.D)
motors = [rear_1, rear_2, rear_3]

remote = Remote(timeout=None)

current_power = 0
step = 10

# Main loop
while True:
    buttons = remote.buttons.pressed()

    # Steering - short burst
    if Button.LEFT_PLUS in buttons:
        steering.run_angle(300, 20)
    elif Button.LEFT_MINUS in buttons:
        steering.run_angle(300, -20)
    else:
        # Optional: return to center
        steering.run_target(300, 0)

    # Drive power logic
    if Button.RIGHT_PLUS in buttons:
        target_power = 100
    elif Button.RIGHT_MINUS in buttons:
        target_power = -100
    else:
        target_power = 0

    # Smooth ramping
    if current_power < target_power:
        current_power += step
        if current_power > target_power:
            current_power = target_power
    elif current_power > target_power:
        current_power -= step
        if current_power < target_power:
            current_power = target_power

    for m in motors:
        m.dc(current_power)

    wait(50)
