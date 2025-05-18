# The foundation is the skid steering idea. 
# But only the front axle works for turning.
# To fully exploit its potential, the front axle must be built with torsion capability AND
# shock absorbers must be used to ensure that it bounces back to its original centre position.

from pybricks.parameters import Button, Direction, Port
from pybricks.pupdevices import Motor, Remote
from pybricks.tools import wait

# Set up motors
# 4 motors - each with a wheel directly attached
# It appears that the LEGO motors are intended to be arranged along the fuselage rather than across it.
# When they are across, at right angles - like the rear axle then you have to watch out for their positions.
# Then use the correct Direction PER motor!
front_left = Motor(Port.D, Direction.COUNTERCLOCKWISE)
front_right = Motor(Port.C, Direction.CLOCKWISE)
rear_left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
rear_right = Motor(Port.A, Direction.CLOCKWISE)

# Set up 88010 Remote Control
remote = Remote(timeout=None)

# Current drive and steer power
current_drive = 0
current_steer = 0
step = 10  # Acceleration step per loop

while True:
    buttons = remote.buttons.pressed()

    target_drive = 0
    target_steer = 0

    # Forward/backward
    if Button.RIGHT_PLUS in buttons:
        target_drive = 100
    elif Button.RIGHT_MINUS in buttons:
        target_drive = -100

    # Steering
    if Button.LEFT_PLUS in buttons:
        target_steer = 100
    elif Button.LEFT_MINUS in buttons:
        target_steer = -100

    # Smooth acceleration for drive
    if current_drive < target_drive:
        current_drive = min(current_drive + step, target_drive)
    elif current_drive > target_drive:
        current_drive = max(current_drive - step, target_drive)

    # Smooth adjustment for steering
    if current_steer < target_steer:
        current_steer = min(current_steer + step, target_steer)
    elif current_steer > target_steer:
        current_steer = max(current_steer - step, target_steer)

    # Power per wheel
    front_left.dc(max(min(current_drive - current_steer, 100), -100))
    rear_left.dc(current_drive)
    front_right.dc(max(min(current_drive + current_steer, 100), -100))
    rear_right.dc(current_drive)

    wait(50)
