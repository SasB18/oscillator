# Importing necesarry libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class oscillator:
    """
    Creates a class called 'oscillator'. This is what we use to solve the motion of a general oscillator
    
    Functions:
    Range: sets the range of the motion
    in_val: sets the initial values
    model: sets the general model, this is what the 'odeint' uses to solve the motion
    ode_solver: solves the motion
    position: returns the values of the position
    velocity: returns the values of the velocity
    plot: plots the graph
    """
    def __init__(self):
        # if there is no Range given, this is what the solver uses
        self.t = np.linspace(0, 150, 200)

    def Range(self, a):
        """
        Sets the range of the motion

        parameters:
        a: upper bound
        """
        # this part devides the range to 3/2 times the range
        x = 3/2 * a
        self.t = np.linspace(0, a, int(x))
        return self.t

    def in_val(self, x0, v0, omega_null, beta, a0, omega):
        """
        Sets the initial values

        parameters:
        x0: initial position
        v0: initial velocity
        omega_null: frequency of the oscillator
        beta: damping factor
        a0: acceleration of resonance
        omega: frequency of resonance
        """
        # puts the initial values into a list
        self.in_val_ = [x0, v0, omega_null, beta, a0, omega]
        return self.in_val_

    def model(self, O, t, in_val_):
        """Sets the model for the motion. This is what the 'odeint' uses to solve the motion"""
        # the 'x' values will be the first and the 'v' values will be the second value of 'O'
        x = O[0]
        v = O[1]
        # give the differential equation(s)
        dxdt = v
        dvdt = -in_val_[2]**2*x -2*in_val_[3]*v + in_val_[4]*np.sin(in_val_[5]*t)
        # returns the value of the derivatives
        return [dxdt, dvdt]

    def ode_solver(self):
        """Solves the system of differential equations"""
        C = [self.in_val_[0], self.in_val_[1]]
        # the 'odeint' solves the motion, given the initial values
        solution = odeint(self.model, C, self.t, args=(self.in_val_,))
        # we put the 'x' and 'v' values into two different lists
        self.x = solution[:,0]
        self.v = solution[:,1]
        # returns the 'x' and 'v' values
        return [self.x, self.v]

    def position(self):
        """Returns the values of the position"""
        return self.x

    def velocity(self):
        """Returns the values of the velocity"""
        return self.v

    def plot(self, position=True, velocity=True):
        """Plots the graph of the motion

        parameters:
        position: when set to 'False', it will only graph the velocity
        velocity: when set to 'False', it will only graph the position
        At least one of them has to be 'True'."""
        # create the coordinate-system
        fig, ax = plt.subplots()
        # set title and label
        ax.set_xlabel("time(s)")
        ax.set_title("The position and velocity on function of time")
        # we can set if we want to plot the position, velocity or both
        if position == True: 
            ax.plot(self.t, self.x, 'b-', label="Position")
        if velocity == True:
            ax.plot(self.t, self.v, 'g-', label="Velocity")
        if position == False and velocity == False:
            print("At least one of them has to be called!")
            return
        ax.legend()
        ax.grid(True)
        plt.show()

# example
osc = oscillator() # set an oscillator
osc.Range(200) # set the range
osc.in_val(2, 1, 0.3, 0.05, 0.02, 0.2) # set the initial conditions
osc.ode_solver() # solve the motion
osc.plot() # plot the solution


