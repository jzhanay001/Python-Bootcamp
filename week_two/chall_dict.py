import numpy as np
from binary import signed_binary, convert_to_decimal

class Individual():
    def __init__ (self, x_loc, y_loc, altitude, jsr = 0):
        """
        Initialize a individual.
        \tparam x_loc <int> : x location of the node
        \tparam y_loc <int> : y location of the node
        \tparam altitude <int> : altitude of the node
        \tparam jsr <double> : jammer to signal ratio at node's location
        \tparam fitness <double> : fitness of the individual
        """
        self.x = x_loc
        self.y = y_loc
        self.altitude = altitude
        self.jsr = jsr
        self.chromosome_length = 11 # maximum chromosome length
        self.x_chromosome = signed_binary (self.x, self.chromosome_length)
        self.y_chromosome = signed_binary (self.y, self.chromosome_length)
        self.z_chromosome = signed_binary (self.altitude, self.chromosome_length)
        self.fitness = 100000000

    def return_point(self):
        self.x = convert_to_decimal(self.x_chromosome)
        self.y = convert_to_decimal(self.y_chromosome)
        self.altitude = convert_to_decimal(self.z_chromosome)
        return self.x, self.y, self.altitude

I1=Individual(4,2,3,4)
print(I1.x,I1.y,I1.altitude,I1.jsr)
