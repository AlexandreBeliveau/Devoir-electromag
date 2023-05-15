import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol, Pow, Add, atan, Mul
import numpy as np

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World


if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 1.0
    HIGH_WIRE_RESISTANCE = 1.0
    LOW_WIRE_RESISTANCE = 0.01

    cartesian_variables = Symbol("x"), Symbol("y")
    x, y = cartesian_variables

    x_expression_vertical = 0 * x
    y_expression_vertical = y
    vertical_eqs = (x_expression_vertical, y_expression_vertical)

    x_expression_horizontal = x
    y_expression_horizontal = 0 * y
    horizontal_eqs = (x_expression_horizontal, y_expression_horizontal)

    x_expression_diagonal = x
    y_expression_diagonal = y
    diagonal_eqs = (x_expression_diagonal, y_expression_diagonal)
    
    old_x = 75
    old_y = 42
    sides = 64
    wires = []
    r = 30
    old_theta = 0
    theta_start = 0
    pas = 0.1
    for i in range(1, sides):
        theta = old_theta + pas
        if theta > theta_start+np.pi-0.1 and theta < theta_start+np.pi+0.1:
            resistance = HIGH_WIRE_RESISTANCE
        else:
            resistance = LOW_WIRE_RESISTANCE
        new_x = ((np.cos(theta) - np.cos(old_theta))*r) + old_x
        new_y = ((np.sin(theta) - np.sin(old_theta))*r) + old_y
        wire = Wire((old_x, old_y), (new_x, new_y), diagonal_eqs, cartesian_variables, resistance)
        wires.append(wire)
        old_x, old_y, old_theta = new_x, new_y, theta

    wires.append(Wire((old_x, old_y), (77, 42), diagonal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE))
    wires.append(VoltageSource((77, 42), (75, 42), diagonal_eqs, cartesian_variables, BATTERY_VOLTAGE))
    '''
    wires = [
        Wire((75, 42), ())
    ]
    '''
    ground_position = (77, 42)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    world.show_circuit()
    world.compute()
    world.show_all()
