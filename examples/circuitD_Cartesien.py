import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol
import numpy as np

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World


if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 1.0
    HIGH_WIRE_RESISTANCE = 1.0
    LOW_WIRE_RESISTANCE = 0.01

    cartesian_variables = Symbol("x"), Symbol("y")
    x, y = cartesian_variables

    polar_variables = Symbol('r'), Symbol('theta')
    r, theta = polar_variables

    x_expression_vertical = 0 * x
    y_expression_vertical = y
    vertical_eqs = (x_expression_vertical, y_expression_vertical)

    x_expression_horizontal = x # Pour le polaire on considère que les x sont les r et le y sont les thetas...
    y_expression_horizontal = 0 * y
    horizontal_eqs = (x_expression_horizontal, y_expression_horizontal)

    x_expression_diagonal = x
    y_expression_diagonal = y
    diagonal_eqs = (x_expression_diagonal, y_expression_diagonal)

    theta_1 = np.pi / 24
    theta_2 = np.pi / 3
    # Simulation en cartésien du d)
    wires = [
        Wire((60*np.cos(theta_1), 60*np.sin(theta_1)), (74*np.cos(theta_1), 74*np.sin(theta_1)), diagonal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((74*np.cos(theta_1), 74*np.sin(theta_1)), (74 * np.cos(np.pi / 7), 74 * np.sin(np.pi / 7)), diagonal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((74 * np.cos(np.pi / 7), 74 * np.sin(np.pi / 7)), (74 * np.cos(2*np.pi / 9), 74 * np.sin(2*np.pi / 9)), diagonal_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((74 * np.cos(2*np.pi / 9), 74 * np.sin(2*np.pi / 9)), (74 * np.cos(theta_2), 74 * np.sin(theta_2)), diagonal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((74 * np.cos(theta_2), 74 * np.sin(theta_2)), (60 * np.cos(theta_2), 60 * np.sin(theta_2)), diagonal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((60 * np.cos(theta_2), 60 * np.sin(theta_2)), (60 * np.cos(2*np.pi / 9), 60 * np.sin(2*np.pi / 9)), diagonal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((60 * np.cos(2*np.pi / 9), 60 * np.sin(2*np.pi / 9)), (60 * np.cos(np.pi / 7), 60 * np.sin(np.pi / 7)), diagonal_eqs, cartesian_variables, BATTERY_VOLTAGE),
        Wire((60 * np.cos(np.pi / 7), 60 * np.sin(np.pi / 7)), (60*np.cos(theta_1), 60*np.sin(theta_1)), diagonal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE) 
    ]

    ground_position = ((60 * np.cos(2*np.pi / 9), 60 * np.sin(2*np.pi / 9)))

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    world.show_circuit(
        {0: (60*np.cos(theta_1), 60*np.sin(theta_1)),
        1: (74*np.cos(theta_1), 74*np.sin(theta_1)), 2: (74 * np.cos(np.pi / 7), 74 * np.sin(np.pi / 7)), 
        3: (74 * np.cos(2*np.pi / 9), 74 * np.sin(2*np.pi / 9)), 4: (74 * np.cos(theta_2), 74 * np.sin(theta_2)), 
        5: (60 * np.cos(theta_2), 60 * np.sin(theta_2)), 6: (60 * np.cos(2*np.pi / 9), 60 * np.sin(2*np.pi / 9)),
        7: (60 * np.cos(np.pi / 7), 60 * np.sin(np.pi / 7))
        }
    )
    world.compute()
    world.show_all()
