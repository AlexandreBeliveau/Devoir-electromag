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

    x_expression_vertical = 0 * x
    y_expression_vertical = y
    vertical_eqs = (x_expression_vertical, y_expression_vertical)

    x_expression_horizontal = x
    y_expression_horizontal = 0 * y
    horizontal_eqs = (x_expression_horizontal, y_expression_horizontal)

    wires = [
        Wire((26, 74), (42, 74), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((42, 74), (42, 57), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((42, 57), (42, 43), vertical_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((42, 43), (42, 26), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((42, 26), (26, 26), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((26, 26), (26, 43), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((26, 43), (26, 57), vertical_eqs, cartesian_variables, BATTERY_VOLTAGE),
        Wire((26, 57), (26, 74), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),

        Wire((42, 74), (58, 74), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((58, 74), (58, 57), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((58, 57), (58, 43), vertical_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((58, 43), (58, 26), vertical_eqs, cartesian_variables ,LOW_WIRE_RESISTANCE),
        Wire((58, 26), (42, 26), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),

        Wire((58, 74), (74, 74), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((74, 74), (74, 57), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((74, 57), (74, 43), vertical_eqs, cartesian_variables, BATTERY_VOLTAGE),
        Wire((74, 43), (74, 26), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((74, 26), (58, 26), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE)


    ]
    ground_position = (26, 43)#ya deux grounds xddd wsh
    #ground_position = (74, 57), (26, 43)


    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    world.show_circuit(
        {0: (26, 74), 1: (42, 74), 2: (42, 57), 3: (42, 43), 4: (42, 26), 5: (26, 26), 6: (26, 43), 7: (26, 57),
        8: (42, 74), 9: (58, 74), 10: (58, 57), 11: (58, 43), 12: (58, 26),
        13: (58, 74), 14: (74, 74), 15: (74, 57), 16: (73, 43), 17: (74, 26)}
    )
    world.compute()
    world.show_all()
