import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World


if __name__ == "__main__":
    WORLD_SHAPE = (150, 150)
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
        #Wire((26, 60), (26, 74), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        #Wire((26, 74), (74, 74), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
       # Wire((74, 74), (74, 60), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
       # Wire((74, 60), (74, 40), vertical_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
       # Wire((74, 40), (74, 26), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
       # Wire((74, 26), (26, 26), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
       # Wire((26, 26), (26, 40), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        #VoltageSource((26, 40), (26, 60), vertical_eqs, cartesian_variables, BATTERY_VOLTAGE)
       Wire((26, 100), (60, 100), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
       Wire((60, 100), (86, 100), horizontal_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
       Wire((86, 100), (86, 40), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
       Wire((86, 40), (86, 10), vertical_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
       Wire((86, 10), (45, 10), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
       VoltageSource((45, 10), (30, 10), horizontal_eqs, cartesian_variables, BATTERY_VOLTAGE),
       Wire((30, 10), (26, 10), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
       Wire((26, 10), (26, 100), vertical_eqs, cartesian_variables, LOW_WIRE_RESISTANCE) 
    ]
    ground_position = (45, 10)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    world.show_circuit(
        #{0: (26, 60), 1: (26, 74), 2: (74, 74), 3: (74, 60), 4: (74, 40), 5: (74, 26), 6: (26, 26), 7: (26, 40)}
        {0: (26, 100), 1: (60, 100), 2: (86, 100), 3: (86, 40), 4: (86, 10), 5: (45, 10), 6: (30, 10), 7: (26, 10)}
    )
    world.compute()
    world.show_all()
