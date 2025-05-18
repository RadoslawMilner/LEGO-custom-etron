# Output in Your terminal battery level.
# Warning!
# works only for TechnicHub!

from pybricks.hubs import TechnicHub

hub = TechnicHub()
voltage = hub.battery.voltage()

# Convert to percent assuming typical LEGO range: 6.0V (empty) to 8.4V (full)
percent = int((voltage - 6000) / (8400 - 6000) * 100)
percent = max(0, min(100, percent))  # Clamp between 0 and 100

print(f"{percent}/100")
