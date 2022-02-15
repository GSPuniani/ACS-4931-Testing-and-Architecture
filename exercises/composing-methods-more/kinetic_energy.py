# By Kami Bigdely
# Remove assignment to method parameter.

class Distance:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

class Mass:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

def calculate_kinetic_energy(mass, distance, time):
    adjusted_distance = None
    adjusted_mass = None
    if distance.unit != 'km':
        if distance.unit == "ly":  # [ly] stands for light-year (measure of distance in astronomy)
            # convert from light-year to km unit
            distance_value = distance.value * 9.461e12
            adjusted_distance = Distance(distance_value, "km")
        else:
            print ("Unknown distance unit")
            return

    speed = adjusted_distance.value / time if adjusted_distance else distance.value / time # [km per sec]

    if mass.unit != 'kg':
        if mass.unit == "solar-mass":
            # convert from solar mass to kg
            mass_value = mass.value * 1.98892e30 # [kg]
            adjusted_mass = Mass(mass_value, 'kg')
        else:
            print ("Unknown mass unit")
            return

    kinetic_energy = 0.5 * adjusted_mass.value * speed ** 2 if adjusted_mass else 0.5 * mass.value * speed ** 2
    return kinetic_energy

mass = Mass(2, "solar-mass")
distance = Distance(2, 'ly')
print(calculate_kinetic_energy(mass, distance, 3600e20))
