import env_examples  # Modifies path, DO NOT REMOVE

from sympy import Symbol

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World


if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 1.0
    HIGH_WIRE_RESISTANCE = 1.0
    LOW_WIRE_RESISTANCE = 0.01

    polar_variables = Symbol("r"), Symbol("θ")
    r, θ = polar_variables

    r_expression_vertical = 0 * r
    θ_expression_vertical = θ
    vertical_eqs = (r_expression_vertical, θ_expression_vertical)

    r_expression_horizontal = r
    θ_expression_horizontal = 0 * θ
    horizontal_eqs = (r_expression_horizontal, θ_expression_horizontal)

    wires = [
        Wire((20, 60),(30, 60), horizontal_eqs, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((30, 60), (30, 40), vertical_eqs, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((30, 40), (30, 35), vertical_eqs, polar_variables, HIGH_WIRE_RESISTANCE),
        Wire((30, 35), (30, 15), vertical_eqs, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((30, 15), (20, 15), horizontal_eqs, polar_variables, LOW_WIRE_RESISTANCE),
        Wire((20, 15), (20, 35), vertical_eqs, polar_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((20, 35), (20, 40), vertical_eqs, polar_variables, BATTERY_VOLTAGE),
        Wire((20, 40), (20, 60), vertical_eqs, polar_variables, LOW_WIRE_RESISTANCE)
    ]
    ground_position = (20, 35)

    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.POLAR, shape=WORLD_SHAPE)
    world.show_circuit(
        {0: (20, 60), 1: (30, 60), 2: (30, 40), 3: (30, 35), 4: (30, 15), 5: (20, 15), 6: (20, 35), 7: (40, 40)}
    )
    world.compute()
    world.show_all()
