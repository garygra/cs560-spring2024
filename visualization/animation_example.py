import numpy as np
from threejs_group import *

if __name__ == "__main__":

  red="0xff0000"
  green="0x00ff00"
  purple="0xff00ff"
  blue="0x0000ff"

  # state: [t, position, quaternion, color] 
  trajectory0 = []
  trajectory1 = []
  trajectory_obs = []
  line = []
  rad = 2
  cube_length=5
  for t in np.arange(0, 10, 0.1, dtype=float):
    color = green if t < 5 else purple
    color_obs = red if t < 3 else green
    state0 = [t, [t, 2*t, cube_length/2],[1,0,0,0], blue]
    state1 = [t, [2*t, t, 0.5],[1,0,0,0], color]
    state_obs = [t, [1,2,rad],[1,0,0,0], color_obs]
    line.append(state0[1])
    trajectory0.append(state0)
    trajectory1.append(state1)
    trajectory_obs.append(state_obs)


  viz_out = threejs_group(1000, 600, "../js/")
  geom0 = box("box0", cube_length, cube_length, cube_length, position = trajectory0[0][1], quaternion = trajectory0[0][2])
  geom1 = box("box1", 1, 1, 1, position = trajectory1[0][1], quaternion = trajectory1[0][2])
  obstacle = sphere("obstacle", rad)
  viz_out.add_line(line, red)
  viz_out.add_animation(geom0, trajectory0)
  viz_out.add_animation(geom1, trajectory1)
  viz_out.add_animation(obstacle, trajectory_obs)

  viz_out.to_html("animation.html", "out/");
