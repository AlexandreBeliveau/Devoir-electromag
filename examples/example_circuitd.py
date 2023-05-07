import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol

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

    x_expression_horizontal = x
    y_expression_horizontal = 0 * y
    horizontal_eqs = (x_expression_horizontal, y_expression_horizontal)

    # Simulation en cartésien du d)
    wires = [
        
        
    ]

    # Simulation en polaire du d)
    pwires = [

    ]

    ground_position = (40, 26)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.POLAR, shape=WORLD_SHAPE)
    world.show_circuit(
        {0: (40, 26), 1: (60, 26), 2: (74, 50), 3: (60, 74), 4: (40, 74), 5: (26, 50)}
    )
    world.compute()
    world.show_all()