from pybricks.parameters import Button, Direction, Port
from pybricks.pupdevices import Motor, Remote #remote-control-88010
from pybricks.robotics import Car
from pybricks.tools import wait

# Set up all devices
steering = Motor(Port.C, Direction.CLOCKWISE)
# 2 motors - each with a wheel directly attached
# It appears that the LEGO motors are intended to be arranged along the fuselage rather than across it.
# When they are across, at right angles - like the rear axle then you have to watch out for their positions.
# Then use the correct Direction PER motor!
left_rear = Motor(Port.B, Direction.COUNTERCLOCKWISE)
right_rear = Motor(Port.A, Direction.CLOCKWISE)
car = Car(steering, [left_rear, right_rear])
remote = Remote(timeout=None)

# Drive power state
current_power = 0
step = 10  # adjust this to control ramp-up speed

# The main program starts here
# Main loop
while True:
    # Control with remote-control-88010
    # Steering using the left horizontal: - and + buttons
    car.steer(100 if Button.LEFT_PLUS in remote.buttons.pressed() else (-100 if Button.LEFT_MINUS in remote.buttons.pressed() else 0))
    
    # Drive power using the right vertical: - and + buttons
    # Determine target power
    if Button.RIGHT_PLUS in remote.buttons.pressed():
        target_power = 100
    elif Button.RIGHT_MINUS in remote.buttons.pressed():
        target_power = -100
    else:
        target_power = 0

    # Gradually change current power toward target
    if current_power < target_power:
        current_power += step
        if current_power > target_power:
            current_power = target_power
    elif current_power > target_power:
        current_power -= step
        if current_power < target_power:
            current_power = target_power

    car.drive_power(current_power)

    wait(50)