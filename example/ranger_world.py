import irsim

env = irsim.make('configs/ranger_world.yaml') # initialize the environment with the configuration file

try:
  while True: # run the simulation for 300 steps

    env.step()  # update the environment
    env.render() # render the environment

    if env.done(): break # check if the simulation is done
          
  env.end() # close the environment
except KeyboardInterrupt:
  env.logger.warning("Keyboard interrupt!")