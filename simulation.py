import numpy as np
import matplotlib.pyplot as plt

def simulate_physical_system(initial_conditions, time_step, num_steps):
    """
    Simulate the motion of a simple physical system.

    Parameters:
    - initial_conditions: Tuple of initial position and velocity.
    - time_step: Time step for the simulation.
    - num_steps: Number of simulation steps.

    Returns:
    - time: Array of time values.
    - position: Array of position values.
    - velocity: Array of velocity values.
    """
    position, velocity = initial_conditions
    time = np.arange(0, num_steps * time_step, time_step)
    
    for _ in range(num_steps):
        # Using a simple numerical integration method (e.g., Euler method)
        acceleration = -9.8  # Gravitational acceleration (you can customize for your system)
        velocity += acceleration * time_step
        position += velocity * time_step

    return time, position, velocity

def plot_simulation(time, position):
    plt.plot(time, position)
    plt.title('Simulation of a Simple Physical System')
    plt.xlabel('Time (s)')
    plt.ylabel('Position')
    plt.grid(True)
    plt.show()

def main():
    # Set initial conditions
    initial_conditions = (0.0, 5.0)  # Initial position and velocity (customize for your system)

    # Set simulation parameters
    time_step = 0.1
    num_steps = 100

    # Run simulation
    time, position, velocity = simulate_physical_system(initial_conditions, time_step, num_steps)

    # Plot results
    plot_simulation(time, position)

if __name__ == "__main__":
    main()
