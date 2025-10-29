# Stable Programs

This directory contains **verified and tested Pybricks programs** for LEGO Technic builds.  
All scripts in this folder are safe to use and have been driven on a real LEGO Audi RS Q e-tron (or compatible chassis).

---

## Available Programs

### 1. `2x_rear_1x_steering_acceleration.py`
Simple and robust setup:
- 2× rear direct-drive motors  
- 1× front steering motor  
- Smooth acceleration logic  
→ Reliable baseline for most car-type builds.

---

### 2. `tracks_skid_steer_acceleration.py`
Classic **tank-style** drive:
- 4× motors for full skid-steer  
- Independent side control  
- Integrated acceleration smoothing  
→ Best for tracked vehicles.

---

### 3. `tracks_skid_steer_acceleration_xbox.py`
Same as above but with **Xbox Controller** input:
- Left joystick → steering  
- Triggers → throttle/brake  
→ Perfect for precision control and fun driving.

---

### 4. `tracks_skid_steer.py`
Minimal version without acceleration ramping.  
→ Use for quick testing or baseline comparison.

---

### 5. `battery_lvl_technic_hub.py`
Outputs **Technic Hub battery level** to terminal.  
> ⚠ Works only with Technic Hub.

---

### 6. `test_speed_only_forward_NO_REMOTE.py`
Measures speed without any controller.  
→ Ideal for verifying gearing ratios and drivetrain performance.

---

## Notes

- All programs assume **LEGO 88010 Remote** by default  
  (Xbox variants explicitly mention controller support).  
- Upload via Pybricks Code or command line:
  ```bash
  pybricksdev run ble -n "Audi RS Q e-tron" ./<filename>.py