# Modules
import numpy as np
# Files
from simulation import Simulation
from time_class import Time

"""
    SCRIPT
"""

# Simulation results list
simulations_results = {
    'lights_enabled': [],
    'lights_disabled': []
}

for _i in range(0, 100):
    # Simulation parameters
    expected_interval = [np.random.randint(low=50.0, high=300.0)/10 for _i in range (0, 6)]
    lights_enabled = True
    green_duration = [np.random.randint(low=15, high=45) for _i in range (0, 3)]
    simulation_results_lights_enabled = []
    simulation_results_lights_disabled = []
    # Repeat 3 times for average
    for _j in range (0, 3):
        # Create and run simulation
        simulation = Simulation(expected_interval, lights_enabled, green_duration)
        simulation_results_lights_enabled.append(simulation.get_results()['avg_time_in_system'].convert_to_seconds())
        # And second time, with lights switched
        simulation = Simulation(expected_interval, not lights_enabled, green_duration)
        simulation_results_lights_disabled.append(simulation.get_results()['avg_time_in_system'].convert_to_seconds())
        print(f"{_i} : {_j}")
    simulations_results['lights_enabled'].append(np.average(np.array(simulation_results_lights_enabled)))
    simulations_results['lights_disabled'].append(np.average(np.array(simulation_results_lights_disabled)))

print(f"Average time in system with lights   : {Time.convert_to_time(seconds=np.average(np.array(simulations_results['lights_enabled']))).convert_to_text()}")
print(f"Average time in system without lights: {Time.convert_to_time(seconds=np.average(np.array(simulations_results['lights_disabled']))).convert_to_text()}")
