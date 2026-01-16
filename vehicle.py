#Kent Tran, Matthew Trinh
#October 14 , 2025
#Red Racer: User chooses a vehicle and uses it to race the remaining choices

from abc import ABC, abstractmethod
import random

class Vehicle(ABC):
  """
  Abstract base class representing a general vehicle.
  """

  def __init__(self, name: str, initial: str, speed: int):
    """
    Initialize a Vehicle object with given attributes.
    """
    self._name = name
    self._initial = initial
    self._speed = speed
    self._position = 0
    self._energy = 100

  @property
  def initial(self) -> str: # (get) returns vehicle label
    return self._initial

  @property
  def position(self) -> int: # (get) returns vehicle position
    return self._position

  @property
  def energy(self) -> int: # (get) returns vehicle energy
    return self._energy


  def fast(self, obs_loc) -> str: # passes in the location of the next obstacle (if there is one)
    """
    Move the vehicle quickly toward the next obstacle.

    - If energy >= 5:
        * Randomly choose a distance between (speed - 1) and (speed + 1)
        * Deduct 5 energy
        * If the movement < distance to obstacle → move that amount
        * Else → crash into obstacle (set position = obs_loc)
    - If energy < 5:
        * Move one space forward (sluggish move)

    Returns:
        A string describing what happened.
    """
    if self._energy >= 5:
      move_distance = random.randint(self._speed - 1, self._speed + 1)
      self._energy -= 5

      if obs_loc is not None and self._position + move_distance >= obs_loc:
        self._position = obs_loc
        return f"{self._name} CRASHED into an obstacle!"
      else:
        self._position += move_distance
        return f"{self._name} quickly moves {move_distance} spaces forward."
        
    else:
      #not enough energy, move 1 unit
      self._position += 1
      return f"{self._name} moves 1 unit (low energy)."

  def slow(self, obs_loc) -> str:
    """
    Moves the vehicle slowly toward the next obstacle. At half speed +/- 1.

    Args: obs_loc (int): location of the next obstacle
    
    Returns: A string describing what happened with the name of the vehicle and the distance travelled.
    """
    move_distance = random.randint(self._speed // 2 - 1, self._speed // 2 + 1)
    
    if obs_loc is not None and self._position + move_distance >= obs_loc:
      distance_moved = obs_loc + 1 - self._position
      self._position = obs_loc + 1
      return f"{self._name} slowly dodges the obstacle and moves {distance_moved} units!"
    else:
      self._position += move_distance
      return f"{self._name} slowly moves {move_distance} units forward!"

  def __str__(self):
    """
    Returns a string representation of the vehicle.
    """
    return f"{self._name} [Position: {self._position}, Energy: {self._energy}]"

  @abstractmethod
  def special_move(self, obs_loc) -> str:
   """
   Abstract method for the special move of the vehicle.
   """
   pass


