# Experimental Programs

This directory contains **prototypes, mechanical experiments, and untested code**.  
Use with caution — they may require non-standard builds or wiring setups.

---

## Work-in-Progress Concepts

### 1. `four_by_four_half_skid_accel.py`
Concept for **independent dual-front-fork steering**:
- 2× rear drive motors  
- 2× front steering motors  
- Requires split front axle build with synchronised turn motion.

---

### 2. `three_rear_steer_accel.py`
Triple-rear differential experiment:
- 3× rear drive motors connected via differential  
- 1× front steering motor  
→ Focus: torque distribution and smooth control.

---

### 3. `two_rear_two_steer_accel.py`
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