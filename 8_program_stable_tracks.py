from pybricks.parameters import Button, Direction, Port
from pybricks.pupdevices import Motor, Remote # remote-control-88010
from pybricks.tools import wait

# Set up all devices
# 4 motors - each with a wheel directly attached
# It appears that the LEGO motors are intended to be arranged along the fuselage rather than across it.
# When they are across, at right angles - like the rear axle then you have to watch out for their positions.
# Then use the correct Direction PER motor!
front_left = Motor(Port.D, Direction.COUNTERCLOCKWISE)
front_right = Motor(Port.C, Direction.CLOCKWISE)
rear_left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
rear_right = Motor(Port.A, Direction.CLOCKWISE)

remote = Remote(timeout=None)

# The main program starts here
# Main loop
while True:
    # Control with remote-control-88010

    buttons = remote.buttons.pressed()

    left_power = 0
    right_power = 0

    # Forward / backward using the right vertical: - and + buttons
    if Button.RIGHT_PLUS in buttons:
        left_power = 100
        right_power = 100
    elif Button.RIGHT_MINUS in buttons:
        left_power = -100
        right_power = -100

    # Turning (skid steering) using the left horizontal: - and + buttons
    if Button.LEFT_PLUS in buttons:
        left_power -= 100
        right_power += 100
    elif Button.LEFT_MINUS in buttons:
        left_power += 100
        right_power -= 100

    # Clamp power to range -100 to 100
    left_power = max(min(left_power, 100), -100)
    right_power = max(min(right_power, 100), -100)

    # Apply power to motors
    front_left.dc(left_power)
    rear_left.dc(left_power)
    front_right.dc(right_power)
    rear_right.dc(right_power)

    wait(50)