import numpy as np
from threejs_group import *

if __name__ == "__main__":

  red="0xff0000"
  green="0x00ff00"
  purple="0xff00ff"

  # state: [t, position, quaternion, color] 
  trajectory0 = []
  trajectory1 = []
  trajectory_obs = []
  for t in np.arange(0, 10, 0.5, dtype=float):
    color = green if t < 5 else purple
    color_obs = purple if t < 3 else green
    state0 = [t, [t, 2*t, 0.5],[1,0,0,0], green]
    state1 = [t, [2*t, t, 0.5],[1,0,0,0], color]
    state_obs = [t, [1,2,0.5],[1,0,0,0], color_obs]
    trajectory0.append(state0)
    trajectory1.append(state1)
    trajectory_obs.append(state_obs)


  viz_out = threejs_group(1000, 600, "../js/")
  geom0 = box("box0", 1, 1, 1, position = trajectory0[0][1], quaternion = trajectory0[0][2])
  geom1 = box("box1", 1, 1, 1, position = trajectory1[0][1], quaternion = trajectory1[0][2])
  obstacle = sphere("obstacle", 0.5)
  viz_out.add_animation(geom0, trajectory0)
  viz_out.add_animation(geom1, trajectory1)
  viz_out.add_animation(obstacle, trajectory_obs)

  viz_out.to_html("animation.html", "out/");
