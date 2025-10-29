# This programme concept requires a vehicle that does NOT have 1 common front axle.
# The programme requires a vehicle that has 2 front forks.
# A non-drive wheel is mounted on each.
# Turning must be synchronised between the 2 forks.

from pybricks.parameters import Button, Direction, Port
from pybricks.pupdevices import Motor, Remote # remote-control-88010
from pybricks.tools import wait

# Set up all Motors
front_left_steering = Motor(Port.A, Direction.CLOCKWISE)
front_right_steering = Motor(Port.C, Direction.CLOCKWISE)

# 2 motors - each with a wheel directly attached
# It appears that the LEGO motors are intended to be arranged along the fuselage rather than across it.
# When they are across, at right angles - like the rear axle then you have to watch out for their positions.
# Then use the correct Direction PER motor!
rear_left_drive = Motor(Port.B, Direction.COUNTERCLOCKWISE)
rear_right_drive = Motor(Port.D, Direction.CLOCKWISE)

remote = Remote(timeout=None)

# Steering state
steering_angle = 0
steering_step = 5
steering_max = 45

# Drive power state
current_power = 0
target_power = 0
power_step = 10 # adjust this to control ramp-up speed

# The main program starts here
while True:
    buttons = remote.buttons.pressed()

    # --- Steering input ---
    # Control with remote-control-88010
    # Steering using the left horizontal: - and + buttons
    if Button.LEFT_PLUS in buttons:
        steering_angle += steering_step
    elif Button.LEFT_MINUS in buttons:
        steering_angle -= steering_step
    else:
        # Auto-centering
        if steering_angle > 0:
            steering_angle -= steering_step
        elif steering_angle < 0:
            steering_angle += steering_step

    # Clamp steering angle
    steering_angle = max(-steering_max, min(steering_max, steering_angle))

    # Apply steering angle
    front_left_steering.run_target(300, steering_angle, wait=False)
    front_right_steering.run_target(300, steering_angle, wait=False)

    # --- Drive power ---
    # Drive power using the right vertical: - and + buttons
    # Determine target power
    if Button.RIGHT_PLUS in buttons:
        target_power = 100
    elif Button.RIGHT_MINUS in buttons:
        target_power = -100
    else:
        target_power = 0

    # Gradually change current power toward target
    if current_power < target_power:
        current_power += power_step
        if current_power > target_power:
            current_power = target_power
    elif current_power > target_power:
        current_power -= power_step
        if current_power < target_power:
            current_power = target_power

    rear_left_drive.dc(current_power)
    rear_right_drive.dc(current_power)

    wait(50)
