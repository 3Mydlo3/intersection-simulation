# Modules
import numpy as np
# Files
from simulation import Simulation
from time_class import Time

"""
    SCRIPT
"""

# Simulation settings
# How many simulations will run
simulations_number = 100
# How many times simulation will be run for given params (to get average result)
simulation_repeats = 3
# Range for green light duration (in seconds)
green_duration_range = [15, 45]
# Controls whether all traffic lights have the same green light duration
equal_green_duration = True
# Range for stream cars arrival expected interval (in seconds)
expected_interval_range = [5, 15]
# Controls whether all streams have the same expected interval
equal_expected_interval = False

# Simulation results list
simulations_results = {
    'lights_enabled': [],
    'lights_disabled': []
}

for _i in range(0, simulations_number):
    # Randomize simulation parameters
    # Green duration
    green_duration = []
    if equal_green_duration:
        green_duration = np.random.randint(low=green_duration_range[0], high=green_duration_range[1])
        green_duration = [green_duration for _i in range (0, 3)]
    else:
        green_duration = [np.random.randint(low=green_duration_range[0], high=green_duration_range[1]) for _i in range (0, 3)]

    # Expected interval
    expected_interval = []
    if equal_expected_interval:
        expected_interval = np.random.randint(low=expected_interval_range[0]*10, high=expected_interval_range[1]*10)/10
        expected_interval = [expected_interval for _i in range (0, 3)]
    else:
        expected_interval = [np.random.randint(low=expected_interval_range[0]*10, high=expected_interval_range[1]*10)/10 for _i in range (0, 6)]

    # Lists to store temporary results
    simulation_results_lights_enabled = []
    simulation_results_lights_disabled = []
    # Repeat 'simulation_repeats' times for average for given params
    for _j in range (0, simulation_repeats):
        # Create and run simulation with lights enabled
        simulation = Simulation(expected_interval=expected_interval, lights_enabled=True, green_duration=green_duration)
        simulation_results_lights_enabled.append(simulation.get_results()['avg_time_in_system'].convert_to_seconds())
        # And second time, with lights disabled
        simulation = Simulation(expected_interval=expected_interval, lights_enabled=False, green_duration=green_duration)
        simulation_results_lights_disabled.append(simulation.get_results()['avg_time_in_system'].convert_to_seconds())
        print(f"{_i} : {_j}")
    simulations_results['lights_enabled'].append(np.average(np.array(simulation_results_lights_enabled)))
    simulations_results['lights_disabled'].append(np.average(np.array(simulation_results_lights_disabled)))

print(f"Average time in system with lights   : {Time.convert_to_time(seconds=np.average(np.array(simulations_results['lights_enabled']))).convert_to_text()}")
print(f"Average time in system without lights: {Time.convert_to_time(seconds=np.average(np.array(simulations_results['lights_disabled']))).convert_to_text()}")
