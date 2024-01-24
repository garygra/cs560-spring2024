from threejs_group import *

if __name__ == "__main__":

	red="0xff0000"
	green="0x00ff00"
	viz_out = threejs_group(js_dir="../js")

	b0 = sphere("obstacle_0", 3, [10,10,3], [0.707, 0, 0, 0.707])
	b1 = sphere("obstacle_1", 1, [10,0,1], [0.707, 0, 0, 0.707])
	viz_out.add_obstacle(b0, "0xff0000")
	viz_out.add_obstacle(b1, "0xff00ff")

	viz_out.to_html("out/obstacles.html");
