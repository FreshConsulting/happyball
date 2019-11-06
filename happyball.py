#!/usr/bin/env python

"""happyball.py: A basic ball bouncing program to demonstrate programming
				 during the Fresh Future Innovators Workshop."""

__author__ = "Sean Patterson"
__copyright__ = "Copyright 2019, Fresh Consulting"
__credits__ = ["Randall Tateishi", "Sean McKay"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Sean Patterson"
__email__ = "sean@freshconsulting.com"

import sys, pygame

# Settings for our game area
screen_size = width, height = 900, 600
white_color = 255, 255, 255

# Settings for bouncing happy ball
move_down_by = 5
move_right_by = 5
app_is_running = True

# Startup our environment.
pygame.init()

# This is a little trick to keep Happy Ball from moving too fast.
game_clock=pygame.time.Clock()
frames_per_second = 60

# Build our environment for Happy Ball and put it in there.
screen = pygame.display.set_mode(screen_size)
happy_ball = pygame.image.load('ball.png').convert_alpha()
fresh_background = pygame.image.load('fresh_background.png').convert_alpha()

# The frame holds Happy Ball and that is how we move it around.
happy_ball_frame = happy_ball.get_rect()

# Let's move happy ball around!!!
while app_is_running:

	# Pygame continuously reponds to events that happen while the app is
	# running. The only event we care about right now is if the user wants
	# to quit, by closing the window or pressing CTRL + C. In that case
	# we close up our environment and exit.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.display.quit()
			pygame.quit()
			sys.exit()

	# Since we weren't told to quit, we clear out any other events that
	# might occur (like moving the mouse or keyboard) that would stop
	# Happy Ball from moving.
	pygame.event.clear()

	# Move our ball by moving the frame that holds it.
	happy_ball_frame = happy_ball_frame.move(move_right_by, move_down_by)

	# Don't move into the nothingness...
	if happy_ball_frame.left < 0 or happy_ball_frame.right > width:
		move_right_by = -move_right_by

	if happy_ball_frame.top < 0 or happy_ball_frame.bottom > height:
		move_down_by = -move_down_by

	# Now that we know where the ball moved to. Redraw thsi on the screen.
	screen.fill(white_color)
	screen.blit(fresh_background, [0,0])
	screen.blit(happy_ball, happy_ball_frame)
	pygame.display.flip()

	# Tick our clock to refresh the display.
	game_clock.tick(frames_per_second)
