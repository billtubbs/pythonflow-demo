import pythonflow as pf
import math

with pf.Graph() as graph:
    pi = pf.constant(math.pi)
    length = pf.constant(1.0)
    radius = pf.constant(0.25)
    density = pf.constant(450)
    volume = length*pi*radius**2
    mass = volume*density

print(f'Volume: {graph(volume)}')
print(f'Mass: {graph(mass)}')
print("\nNow recalculate with twice the length")
print(f'Volume: {graph(volume, {length: graph(length)*2})}')
print(f'Mass: {graph(mass, {length: graph(length)*2})}')
