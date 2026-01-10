# Test speed Your car and output the results into Your terminal.
# WARNING!
# IT DOES NOT USE REMOTE

from pybricks.parameters import Port, Direction
from pybricks.pupdevices import Motor
from pybricks.tools import wait, StopWatch

# Motors
rear_left = Motor(Port.B, Direction.COUNTERCLOCKWISE)
rear_right = Motor(Port.A, Direction.CLOCKWISE)

# Reset angles
rear_left.reset_angle(0)
rear_right.reset_angle(0)

# Stopwatch
watch = StopWatch()
watch.reset()

# Run rear motors at fixed power
rear_left.dc(100)
rear_right.dc(100)

# Run for 3 seconds
wait(3000)

# Stop motors
rear_left.stop()
rear_right.stop()

# Measure distance
angle_left = rear_left.angle()
angle_right = rear_right.angle()

# Print results
print("Left rear angle:", angle_left)
print("Right rear angle:", angle_right)
print("Elapsed time (ms):", watch.time())
