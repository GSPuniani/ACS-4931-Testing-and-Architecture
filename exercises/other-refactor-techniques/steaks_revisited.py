# by Kami Bigdely
# Extract class
WELL_DONE = 3000
MEDIUM = 2500
COOKED_CONSTANT = 0.05

class Steak():
    def __init__(self, time, temperature, pressure, desired_state) -> None:
        self.time = time
        self.temperature = temperature
        self.pressure = pressure
        self.desired_state = desired_state

    def is_cooking_criteria_satisfied(self):
        return self.is_well_done() or self.is_medium()

    def is_well_done(self):    
        return self.desired_state == 'well-done' and  self.get_cooking_progress() >= WELL_DONE

    def is_medium(self):
        return self.desired_state == 'medium' and  self.get_cooking_progress() >= MEDIUM

    def get_cooking_progress(self):
        return self.time * self.temperature * self.pressure * COOKED_CONSTANT


my_steak = Steak(time = 30, temperature = 103, pressure = 20, desired_state = 'well-done')

if my_steak.is_cooking_criteria_satisfied():
    print('Cooking is done.')
else:
    print('Cooking is ongoing.')