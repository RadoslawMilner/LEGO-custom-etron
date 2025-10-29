# Experimental Programs

This directory contains **prototypes, mechanical experiments, and untested code**.  
Use with caution — they may require non-standard builds or wiring setups.

---

## Work-in-Progress Concepts

### 1. `2x_rear_2x_steering_acceleration.py`
Concept for **independent dual-front-fork steering**:
- 2× rear drive motors  
- 2× front steering motors  
- Requires split front axle build with synchronised turn motion.

---

### 2. `3x_rear_steering_acceleration.py`
Triple-rear differential experiment:
- 3× rear drive motors connected via differential  
- 1× front steering motor  
→ Focus: torque distribution and smooth control.

---

### 3. `4x4_with_half_skid_with_acceleration.py`
Hybrid **half-skid steering** setup:
- 4×4 drive  
- Only front axle turns, with torsion and shock absorbers  
→ Experimental control logic and physical dynamics.

---

## Development Notes

- These files are for **testing logic, geometry, and motor control**.  
- Expect unpredictable behaviour — especially with skid/hybrid setups.  
- Each script is isolated for quick iteration.

---

## Status

🚧 In progress — may evolve into new stable releases.