# Modules
import numpy as np
# Files
from simulation import Simulation

"""
    SCRIPT
"""

# Simulation parameters
expected_interval = [np.random.uniform(low=5.0, high=10.0) for _i in range (0, 6)]
lights_enabled = True
green_duration = [np.random.randint(low=10, high=20) for _i in range (0, 3)]

# Create and run simulation
simulation = Simulation(expected_interval, lights_enabled, green_duration)
simulation.print_stats()
# And second time, with lights switched
simulation = Simulation(expected_interval, not lights_enabled, green_duration)
simulation.print_stats()
