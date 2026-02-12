# SLAVE HUB
# Controls front bucket and rear tub
# BLE observe:
#   - Receives (bucket_step, tub_step) from MASTER HUB
#   - bucket: analog, target updated by bucket_step, limited by BUCKET_MIN/MAX
#   - tub: digital, target updated by tub_step, limited by TUB_MIN/MAX
# Motors run via run_target (SPEED_BUCKET / SPEED_TUB)
# Notes:
#   - Positions are relative to hub power-on zero
#   - No homing/calibration implemented yet
#   - Smooth motion via run_target, loops every `delay` ms

from pybricks.hubs import ThisHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction
from pybricks.tools import wait

hub = ThisHub(observe_channels=[1])

# --- ACTUATOR MOTORS ---
rear_tub = Motor(Port.B, Direction.CLOCKWISE)
front_bucket = Motor(Port.A, Direction.CLOCKWISE)

# --- LIMITS ---
BUCKET_MIN = -40
BUCKET_MAX = 120

TUB_MIN = 0
TUB_MAX = 90

SPEED_BUCKET = 400
SPEED_TUB = 400

delay = 50
bucket_target = 0
tub_target = 0

while True:
    data = hub.ble.observe(1)

    if data is not None:
        loader_cmd, tub_cmd = data

        # BUCKET (analog step)
        bucket_target += loader_cmd
        bucket_target = max(min(bucket_target, BUCKET_MAX), BUCKET_MIN)
        front_bucket.run_target(SPEED_BUCKET, bucket_target, wait=False)

        # TUB (digital step)
        tub_target += tub_cmd
        tub_target = max(min(tub_target, TUB_MAX), TUB_MIN)
        rear_tub.run_target(SPEED_TUB, tub_target, wait=False)

    wait(delay)