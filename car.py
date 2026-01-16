#Kent Tran, Matthew Trinh
#October 14 , 2025
#Red Racer: User chooses a vehicle and uses it to race the remaining choices

from vehicle import Vehicle
import random

class Car(Vehicle):
  def special_move(self, obs_loc) -> str:
    """
    Special move for car: Nitro boost
    Passes in the location of the next obstacle (if there is one)
    If energy >= 15, deduct 15 and move the car 1.5x speed +/- 1.
    If there's an obstacle, move to the obstacle and stop there. Otherwise move a randomized distance.
    If energy < 15, move one space forward (sluggish move)
    Returns: A string describing what happened with the name of the car and the distance travelled.
    """
    if self._energy >= 15:
      self._energy -= 15
      movement = random.randint(int(self._speed * 1.5 - 1), int(self._speed * 1.5 + 1))

      if obs_loc is not None and self._position + movement >= obs_loc:
        self._position = obs_loc
        return f"{self._name} used nitro boost and CRASHED into an obstacle!"
      else:
        self._position += movement
        return f"{self._name} used nitro boost and moved {movement} units forward!"

    else:
      self._position += 1
      return f"{self._name} tries to use nitro boost, but is all out of energy!"