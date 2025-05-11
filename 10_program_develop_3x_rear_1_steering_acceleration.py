from pybricks.parameters import Button, Direction, Port
from pybricks.pupdevices import Motor, Remote #remote-control-88010
from pybricks.robotics import Car
from pybricks.tools import wait

# Set up all devices
front_steering = Motor(Port.C, Direction.CLOCKWISE)
# 3 motors - through differential
rear_1 = Motor(Port.A, Direction.CLOCKWISE)
rear_2 = Motor(Port.B, Direction.CLOCKWISE)
rear_3 = Motor(Port.D, Direction.CLOCKWISE)
car = Car(front_steering, [rear_1, rear_2, rear_3])
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