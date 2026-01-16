#Kent Tran, Matthew Trinh
#October 14 , 2025
#Red Racer: User chooses a vehicle and uses it to race the remaining choices

from vehicle import Vehicle

class Truck(Vehicle):
  def special_move(self, obs_loc) -> str:
    """
    Special Move: Ram
    moves at 2x speed and crushes through obstacles

    Args: obs_loc (int): location of the next obstacle
    
    Returns: A string describing what happened with the name of the truck and the distance travelled.
    """
    if self._energy >= 15:
      self._energy -= 15
      move_distance = self._speed * 2
      self._position += move_distance
      return f"{self._name} rams forward {move_distance} units!"
    else:
       self._position += 1
       return f"{self._name} tries to ram forward, but is all out of energy!"