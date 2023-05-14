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

    x_expression_vertical = 1*x
    y_expression_vertical = 1*y
    vertical_eqs = (x_expression_vertical, y_expression_vertical)

    x_expression_horizontal = 1*x
    y_expression_horizontal = 1*y
    horizontal_eqs = (x_expression_horizontal, y_expression_horizontal)

   #Considérons les deux rayons du circuit D, soit le petit rayon de 20 et le grand rayon de 30. L'angle du rayon le plus haut est de 
   # 60 degrés donc pi/3 et l'angle le plus bas est de 15 degrés donc pi/12. Cependant, puisque que le programme considère
   # seulement les angles entre 0 et pi/4, on devra diviser les angles par 4. Dans un premier temps, on peu créer 
   #les fils qui ne requierts pas d'angle (qui ne sont pas en forme d'arc de cercle) et ensuite, à l'aide d'une boucle for, on peut faire une multitude de petits déplacements
   #qui donneront une forme circulaire pour les deux boucles.

    wires = [
        VoltageSource((20*np.cos(np.pi/24), 20*np.sin(np.pi/24)), (20*np.cos(7*np.pi/144), (20*np.sin(7*np.pi/144))), horizontal_eqs, cartesian_variables, BATTERY_VOLTAGE),
        Wire((30*np.cos(np.pi/24), 30*np.sin(np.pi/24)), (30*np.cos(7*np.pi/144), 30*np.sin(7*np.pi/144)), horizontal_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE),
        Wire((20*np.cos(np.pi/12), 20*np.sin(np.pi/12)), (30*np.cos(np.pi/12), 30*np.sin(np.pi/12)), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
        Wire((30*np.cos(np.pi/48), 30*np.sin(np.pi/48)), (20*np.cos(np.pi/48), 20*np.sin(np.pi/48)), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE),
    ]
    
    wires1 = []
    #On peut ensuite faire la forloop pour la partie du bas (avant la source et les résistances):
    #wires2 = []
    for i in range(3):
        wires1.append(Wire((30*np.cos(np.pi/48+np.pi*i/144), 30*np.sin(np.pi/48+np.pi*i/144)),(30*np.cos(np.pi/48+np.pi*(i+1)/144), 30*np.sin(np.pi/48+np.pi*(i+1)/144)), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE))

        wires.append(Wire((20*np.cos(np.pi/48+np.pi*i/144), 20*np.sin(np.pi/48+np.pi*i/144)),(20*np.cos(np.pi/48+np.pi*(i+1)/144), 20*np.sin(np.pi/48+np.pi*(i+1)/144)), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE))
    
    #On fait la boucle pour la partie du haut après la source et les résistances
    for j in range(5):
        wires1.append(Wire((30*np.cos(7*np.pi/144+np.pi*j/144), 30*np.sin(7*np.pi/144+np.pi*j/144)),(30*np.cos(7*np.pi/144+np.pi*(j+1)/144), 30*np.sin(7*np.pi/144+np.pi*(j+1)/144)), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE))

        wires.append(Wire((20*np.cos(7*np.pi/144+np.pi*j/144), 20*np.sin(7*np.pi/144+np.pi*j/144)),(20*np.cos(7*np.pi/144+np.pi*(j+1)/144), 20*np.sin(7*np.pi/144+np.pi*(j+1)/144)), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE))
    
    #w = Wire((30*np.cos(np.pi/48+np.pi*i/144), 30*np.sin(np.pi/48+np.pi*i/144)),(30*np.cos(np.pi/48+np.pi*(i+1)/144), 30*np.sin(np.pi/48+np.pi*(i+1)/144)), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE)
    #print(w._start_position)
    ground_position = ((20*np.cos(np.pi/24)), (20*np.sin(np.pi/24)))
    count = 0
    for w in wires1:
        
        print('start: '+ str(count) +str(w._start_position))
        print('__________________')
        print('stop: '+ str(count) +str(w._stop_position))
        count += 1
    s = Wire((30*np.cos(np.pi/24), 30*np.sin(np.pi/24)), (30*np.cos(7*np.pi/144), 30*np.sin(7*np.pi/144)), horizontal_eqs, cartesian_variables, HIGH_WIRE_RESISTANCE)
    print('start' + str(s._start_position))
    print('stop' + str(s._stop_position))
    print('_______________')
    a =Wire((20*np.cos(np.pi/12), 20*np.sin(np.pi/12)), (30*np.cos(np.pi/12), 30*np.sin(np.pi/12)), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE)
    b = Wire((30*np.cos(np.pi/48), 30*np.sin(np.pi/48)), (20*np.cos(np.pi/48), 20*np.sin(np.pi/48)), horizontal_eqs, cartesian_variables, LOW_WIRE_RESISTANCE)

    print('b start:' + str(b.start_position))
    print('b stop:' + str(b.stop_position))
    print('a start' + str(a.start_position))
    print('a fin' + str(a.stop_position))
    c = VoltageSource((20*np.cos(np.pi/24), 20*np.sin(np.pi/24)), (20*np.cos(7*np.pi/144), (20*np.sin(7*np.pi/144))), horizontal_eqs, cartesian_variables, BATTERY_VOLTAGE)
    print('source start:' + str(c._start_position))
    print('source stop:' + str(c.stop_position))
    #circuit = Circuit(wires, ground_position)
    #world = World(circuit=circuit, coordinate_system=CoordinateSystem.CARTESIAN, shape=WORLD_SHAPE)
    #world.show_circuit({0: ()})
    #world.compute()
    #world.show_all()