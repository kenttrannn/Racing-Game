#Kent Tran, Matthew Trinh
#October 14 , 2025
#Red Racer: User chooses a vehicle and uses it to race the remaining choices

import random
from car import Car
from motorcycle import Motorcycle
from truck import Truck
import check_input

track_length = 100
num_lanes = 3

def create_track():
  """
  Create a track using a 2D list with obstacles (O)

  Args: none
  
  Returns: 2D list representing the track
  """
  track = []
  for i in range(num_lanes):
    lane = ['-'] * track_length
    obstacle_position = random.sample(range(10, track_length - 10), 2)
    for pos in obstacle_position:
      lane[pos] = '0'
    track.append(lane)
  return track

def display_track(track, vehicles):
  """
  Display the current state of the track with all vehicles position and obstacles
  
  Args: track: 2D list of the track
        vehicles: list of vehicle objects

  Returns: none
  """
  for i, vehicle in enumerate(vehicles):
    print(''.join(track[i]))

def update_track(track, vehicles, prev_position):
  """
  Update the track with new position and movement trails

  Args: track:
        vehicles:
        prev_position:
  """
  for i, vehicle in enumerate(vehicles):
    if vehicle.initial in prev_position:
      old_pos = prev_position[vehicle.initial]
      if old_pos < track_length and track[i][old_pos] == vehicle.initial:
        track[i][old_pos] = '*'

    new_pos = vehicle.position
    if new_pos < track_length:
      track[i][new_pos] = vehicle.initial

def next_obstacle(track, lane, position):
  """
  Get location of the next obstacle in the lane

  Args: track: 2D list of the track
        lane: lane index
        position: current position in the lane
  """
  try:
    return track[lane].index('0', position)
  except ValueError:
    return None

def other_move(vehicle):
  """
  Randomly choose a move for the other vehicles

  Args: vehicle: vehicle object

  Returns: int representing the move choice
  """
  if vehicle.energy < 5:
    return 2

  rand = random.random()
  if rand < 0.4:
    return 2
  elif rand < 0.7:
    return 1
  else:
    return 3

def main():
  print("Welcome to Red Racer!")
  print("Choose your vehicle and race it down the track(player = 'P'). Slow down for obstacles (O) or else you'll crash!\n")
  
  car = Car("Lightning Car", "C", 7)
  motorcycle = Motorcycle("Swift Bike", "M", 8)
  truck = Truck("Behemoth Truck", "T", 6)

  print("1. Lightning Car - a fast car. Speed: 7. Special Move: Nitro Boost (1.5x Speed).")
  print("2. Swift Bike - a speedy motorcycle. Speed: 8. Special Move: Wheelie (2x Speed but there's a chance you'll wipe out).")
  print("3. Behemoth Truck - a heavy truck. Speed: 6. Special Move: Ram (2x Speed and smashes through obstacles).")

  choice = check_input.get_int_range("Enter the number of your chosen vehicle: ", 1, 3)
  print()

  vehicles = [car, motorcycle, truck]
  if choice == 1:
    car._initial = "P"
    player_vehicle = car
  elif choice == 2:
    motorcycle._initial = "P"
    player_vehicle = motorcycle
  else:
    truck._initial = "P"
    player_vehicle = truck

  track = create_track()

  for i, vehicle in enumerate(vehicles):
    track[i][0] = vehicle.initial

  #initializes everything
  prev_position = {}
  finished = []
  finished_vehicles = set()

  for vehicle in vehicles:
    print (vehicle)

  while len(finished) < 3:
    print()
    display_track(track, vehicles)
    print()

    for vehicle in vehicles:
      prev_position[vehicle.initial] = vehicle.position

    if player_vehicle not in finished_vehicles:
      action = check_input.get_int_range("Choose action: 1. Fast, 2. Slow, 3. Special Move: ", 1, 3)

      player_lane = vehicles.index(player_vehicle)
      obs_loc = next_obstacle(track, player_lane, player_vehicle.position)

      if action == 1:
        print(player_vehicle.fast(obs_loc))
      elif action == 2:
        print(player_vehicle.slow(obs_loc))
      else:
        print(player_vehicle.special_move(obs_loc))

      if player_vehicle.position >= track_length:
        finished.append(player_vehicle)
        finished_vehicles.add(player_vehicle)

    for i, vehicle in enumerate(vehicles):
      if vehicle  != player_vehicle and vehicle not in finished_vehicles:
         action = other_move(vehicle)
         obs_loc = next_obstacle(track, i, vehicle.position)

         if action == 1:
            result = vehicle.fast(obs_loc)
         elif action == 2:
            result = vehicle.slow(obs_loc)
         else:
            result = vehicle.special_move(obs_loc)

         print(result)

         if vehicle.position >= track_length:
            finished.append(vehicle)
            finished_vehicles.add(vehicle)
    
    update_track(track, vehicles, prev_position)

    print()

    for vehicle in vehicles:
      print(vehicle)

  print()
  display_track(track, vehicles)
  print()

  print(f"1st place {finished[0]}!")
  print(f"2nd place {finished[1]}!")
  print(f"3rd place {finished[2]}!")

main()