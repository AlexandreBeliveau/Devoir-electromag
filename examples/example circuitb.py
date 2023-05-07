import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World


if __name__ == "__main__":
    WORLD_SHAPE = (105, 105)
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

    wires = [
        VoltageSource((10, 45), (10, 55), vertical_eqs, cartesian_variables, BATTERY_VOLTAGE),
        Wire((10, 55), (10, 100), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((10, 100), (20, 100), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((20, 100), (20, 60), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((20, 60), (20, 40), vertical_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((20, 40), (20, 10), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((20, 10), (10, 10), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((10, 10), (10, 45), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        
        Wire((20, 100), (30, 100), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((30, 100), (30, 60), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((30, 60), (30, 40), vertical_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((30, 40), (30, 10), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((30, 10), (20, 10), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        
        Wire((30, 100), (40, 100), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((40, 100), (40, 60), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((40, 60), (40, 40), vertical_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((40, 40), (40, 10), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((40, 10), (30, 10), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
    ]
    ground_position = (10, 45)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    world.show_circuit(
        {0: (10, 45), 1: (10, 55), 2: (10, 100), 3: (20, 100), 4: (20, 60), 5: (20, 40), 6: (20, 10), 7: (10, 10),
         8: (20, 100), 9: (30, 100), 10: (30, 60), 11: (30, 40), 12: (30, 10),
         13: (30, 100), 14: (40, 100), 15: (40, 60), 16: (40, 40), 17: (40, 10)}
    )
    world.compute()
    world.show_all()
