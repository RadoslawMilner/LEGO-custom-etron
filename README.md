# LEGO Custom Audi RS Q e-tron

<p align="center">
  <img src="./assets/four_on_four_drive_in_wheels_motors.jpg" width="600" alt="LEGO four on four drive in wheels motors">
</p>

Custom LEGO Audi RS Q e-tron project powered by **Pybricks** firmware.  
This repository explores and documents various drivetrain and steering concepts for LEGO Technic vehicles — from proven stable builds to experimental prototypes.

---

## Structure

- **[`stable/`](scripts/stable/)** — Tested and verified programs.
  Reliable for reuse, demo, and everyday driving.

- **[`experimental/`](scripts/experimental/)** — Prototypes and unfinished concepts.  
  Used for testing ideas and mechanical setups.

---

## Highlights

- Multiple drive configurations: 2× rear, 4×4, half-skid, and tracked
- Smooth acceleration control and turning logic
- Support for LEGO 88010 Remote and Xbox Controller
- Battery monitoring for LEGO Technic Hub
- Modular, readable Python code compatible with Pybricks

---

## Hardware & Requirements

- LEGO Technic Hub (Control+ / 4-port)
- LEGO L or XL motors
- LEGO 88010 Remote *(default)*
- Xbox Controller *(optional, supported in selected builds)*
- Pybricks firmware installed on Hub
- Wheels or tracks depending on variant

---

## Usage

1. Flash your Technic Hub with [Pybricks firmware](https://code.pybricks.com)  
2. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/lego-etron.git
   cd lego-etron
3. Choose a program from stable/
4. Upload it via Pybricks Code or run: pybricksdev run ble -n "Audi RS Q e-tron" .scripts/stable/drives/<script>.py

---

## Documentation

See:
	•	Stable builds →￼
	•	Experimental prototypes →￼

---

## Status

🚗 Actively developed — multiple configurations tested and iterated.

## License

MIT

---

> Built by [Radosław Milner](https://github.com/RadoslawMilner) using LEGO and lots of iterations 🚗🔧
