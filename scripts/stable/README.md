# Stable Programs

This directory contains **verified and tested Pybricks programs** for LEGO Technic builds.  
All scripts in this folder are safe to use.

---

## Available Programs

### 1. `drives/two_rear_one_steer_accel.py`
Simple and robust setup:
- 2× rear direct-drive motors  
- 1× front steering motor  
- Smooth acceleration logic  
→ Reliable baseline for most car-type builds.

---

### 2. `drives/tracks_skid_steer/basic.py`
Classic **tank-style** drive:
- 4× motors for full skid-steer  
- Independent side control  
→ Best for tracked vehicles.

---

### 3. `drives/tracks_skid_steer/with_acceration/basic.py`
Same as above but with integrated acceleration smoothing

---

### 4. `drives/tracks_skid_steer/with_acceration/xbox.py`
Same as above but with **Xbox Controller** input:
- Left joystick → steering  
- Triggers → throttle/brake  
→ Perfect for precision control and fun driving.

---

### 5. `drives/tracks_skid_steer/with_acceration/dual_hubs/xbox_(master+slave).py`
Skid-steer drive with acceleration – dual Technic Hub architecture (Xbox Controller, BLE broadcast)
→ Advanced version of the skid-steer drive using two LEGO Technic Hubs communicating via BLE broadcast.

This implementation consists of two cooperating scripts that must run together:
-	xbox_master.py – rear hub
-	xbox_slave.py – front hub

The description below refers to both files as a single system.

Responsibilities:
-	Master hub (rear)
-	Reads Xbox Controller input
-	Computes skid-steer + acceleration ramp
-	Broadcasts control values via BLE
-	Drives rear track motors
-	Slave hub (front)
-	Listens for BLE broadcast
-	Mirrors received motor commands
-	Drives front track motors

Controls:
-	Left joystick → steering (skid steering)
-	Triggers → throttle / brake

---

### 6. `tests/test_speed_only_forward_NO_REMOTE.py`
Measures speed without any controller.  
→ Ideal for verifying gearing ratios and drivetrain performance.

---

### 7. `utils/battery_lvl_technic_hub.py`
Outputs **Technic Hub battery level** to terminal.  
> ⚠ Works only with Technic Hub.

## Notes

- All programs assume **LEGO 88010 Remote** by default  
  (Xbox variants explicitly mention controller support).  
- Upload via Pybricks Code or command line:
  ```bash
  pybricksdev run ble -n "Your hub name" ./<filename>.py