#Kent Tran, Matthew Trinh
#October 14 , 2025
#Red Racer: User chooses a vehicle and uses it to race the remaining choices

from vehicle import Vehicle
import random

class Motorcycle(Vehicle):
   def slow(self, obs_loc) -> str:
     """
     Motorcycle moves at 75% speed +/- 1. If there's an obstacle, it will go around it. There's no energy cost.
     Args: obs_loc (int): location of the next obstacle
     Returns: A string describing what happened with the name of the motorcycle and the distance travelled.
     """
      
     move_distance = random.randint(int(self._speed * 0.75 - 1), int(self._speed * 0.75 + 1))
     if obs_loc is not None and self._position + move_distance >= obs_loc:
        distance_moved = obs_loc + 1 - self._position
        self._position = obs_loc + 1
        return f"{self._name} slowly dodges the obstacle and moves {distance_moved} units!"
     else:
         self._position += move_distance
         return f"{self._name} slowly moves {move_distance} units forward!"

   
   def special_move(self, obs_loc) -> str:
    """
    Special Move: Speed Boost
    >=15 Energy: deduct 15 energy and 75% chance to go 2x speed +/- 1. If successful, move a randomized distance. If there's an obstacle in the        way, 
    move to the obstacle and crash there.
    <15 Energy: fall over and only move 1 unit forward.

    Args: obs_loc (int): location of the next obstacle

    Returns: A string describing what happened with the name of the motorcycle and the distance travelled.
    """
    if self._energy >= 15:
      self._energy -= 15

      #75% chance to wheelie
      if random.random() < 0.75:
         move_distance = random.randint(self._speed * 2 - 1, self._speed * 2 + 1)
         if obs_loc is not None and  self._position + move_distance >= obs_loc:
            self._position = obs_loc
            return f"{self._name} used speed boost and CRASHED into an obstacle!"

         else:
          self._position += move_distance
          return f"{self._name} used speed boost and moved {move_distance} units forward!"
      else:
         self._position += 1
         return f"{self._name} tried to wheelie but fell over and only moves 1 unit!"

    #when energy is less than 15
    else:
        self._position += 1
        return f"{self._name} tries to wheelie, but is all out of energy!"