# Stable Programs

This directory contains **verified and tested Pybricks programs** for LEGO Technic builds.  
All scripts in this folder are safe to use.

---

## Available Programs

### 1. `two_rear_one_steer_accel.py`
Simple and robust setup:
- 2× rear direct-drive motors  
- 1× front steering motor  
- Smooth acceleration logic  
→ Reliable baseline for most car-type builds.

---

### 2. `tracks_skid_steer.py`
Minimal version without acceleration ramping.  
→ Use for quick testing or baseline comparison.

---

### 3. `tracks_skid_steer_accel.py`
Classic **tank-style** drive:
- 4× motors for full skid-steer  
- Independent side control  
- Integrated acceleration smoothing  
→ Best for tracked vehicles.

---

### 4. `tracks_skid_steer_accel_xbox.py`
Same as above but with **Xbox Controller** input:
- Left joystick → steering  
- Triggers → throttle/brake  
→ Perfect for precision control and fun driving.

---

### 5. `battery_lvl_technic_hub.py`
Outputs **Technic Hub battery level** to terminal.  
> ⚠ Works only with Technic Hub.

---

### 6. `test_speed_only_forward_NO_REMOTE.py`
Measures speed without any controller.  
→ Ideal for verifying gearing ratios and drivetrain performance.

---

### 7. `dual hubs`
Dual Technic Hub setup with Xbox Controller (BLE broadcast)
→ Advanced version of the skid-steer drive using two LEGO Technic Hubs communicating via BLE broadcast.

Architecture:
	-	Master Hub (rear)
	-	Handles Xbox Controller input
	-	Computes skid-steer logic and acceleration ramps
	-	Broadcasts control commands over BLE
	-	Drives rear axle motors
	-	Slave Hub (front)
	-	Listens to BLE broadcast
	-	Executes received commands
	-	Drives front axle motors

Controls:
	-	Left joystick → steering (skid steering)
	-	Triggers → throttle / brake

---

## Notes

- All programs assume **LEGO 88010 Remote** by default  
  (Xbox variants explicitly mention controller support).  
- Upload via Pybricks Code or command line:
  ```bash
  pybricksdev run ble -n "Your hub name" ./<filename>.py