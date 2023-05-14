import env_examples  # Modifies path, DO NOT REMOVE
import numpy as np

from sympy import Symbol

from src import Circuit, CoordinateSystem, VoltageSource, Wire, World


if __name__ == "__main__":
    WORLD_SHAPE = (101, 101)
    BATTERY_VOLTAGE = 1.0
    HIGH_WIRE_RESISTANCE = 1.0
    LOW_WIRE_RESISTANCE = 0.01

    polaire_variables = Symbol("r"), Symbol("θ")
    r, θ = polaire_variables

    r_expression_radial = 1 * r
    θ_expression_radial = 0 * θ
    radial_eqs = (r_expression_radial, θ_expression_radial)

    r_expression_azimutale = 0 * r
    θ_expression_azimutale = 1 * θ
    azimutale_eqs = (r_expression_azimutale, θ_expression_azimutale)
    #On considére que les deux rayons sont de 26 et 74 respectivements
    wires = [
        Wire((26, np.pi/12), (26, np.pi/6), azimutale_eqs, polaire_variables, LOW_WIRE_RESISTANCE),
        VoltageSource((26, np.pi/6), (26, 7*np.pi/36), azimutale_eqs, polaire_variables, BATTERY_VOLTAGE),
        Wire((26, 7*np.pi/36), (26, np.pi/3), azimutale_eqs, polaire_variables, LOW_WIRE_RESISTANCE),
        Wire((26, np.pi/3), (74, np.pi/3), radial_eqs, polaire_variables, LOW_WIRE_RESISTANCE),
        Wire((74, np.pi/3), (74, 7*np.pi/36), azimutale_eqs, polaire_variables, LOW_WIRE_RESISTANCE),
        Wire((74, 7*np.pi/36), (74, np.pi/6),azimutale_eqs, polaire_variables, HIGH_WIRE_RESISTANCE),
        Wire((74, np.pi/6), (74, np.pi/12), azimutale_eqs, polaire_variables, LOW_WIRE_RESISTANCE),
        Wire((74, np.pi/12), (26, np.pi/12), radial_eqs, polaire_variables, LOW_WIRE_RESISTANCE)
    ]
    ground_position = (26, np.pi/6)

    
    circuit = Circuit(wires, ground_position)
    world = World(circuit=circuit, coordinate_system=CoordinateSystem.POLAR, shape=WORLD_SHAPE)
    world.show_circuit(
        {0: (26, np.pi/12), 1: (26, np.pi/6), 2: (26, 7*np.pi/36), 3: (26, np.pi/3), 4: (74, np.pi/3), 5: (74, 7*np.pi/36), 6: (74, np.pi/6), 7: (74, np.pi/12)}
    )
    
    world.compute()
    world.show_all()
