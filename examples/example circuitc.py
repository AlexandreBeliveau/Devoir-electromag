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

    wires = []
    r = 60
    pas = 0.2
    theta = np.arange(0 , 2*np.pi-pas, pas)
    
    for i in theta:
        wires.append(Wire((r*np.cos(i), r*np.sin(i)), (r*np.cos(i+(pas)), r*np.sin(i+(pas))), diagonal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE))
    wires.append(Wire((r*np.cos(theta[-1]), r*np.sin(theta[-1])), (r*np.cos(2*np.pi), r*np.sin(2*np.pi)), diagonal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE))
    ground_position = (60, 0)
    print(len(wires))

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    world.show_circuit(
        {0: (0, 0), 1: (60, 26), 2: (74, 50), 3: (60, 74), 4: (40, 74), 5: (26, 50)}
    )
    world.compute()
    world.show_all()
