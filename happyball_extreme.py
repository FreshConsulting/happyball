#!/usr/bin/env python

"""happyball.py: An extreme ball bouncing program to demonstrate programming
				 during the Fresh Future Innovators Workshop."""

__author__ = "Sean Patterson"
__copyright__ = "Copyright 2019, Fresh Consulting"
__credits__ = ["Randall Tateishi", "Sean McKay"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Sean Patterson"
__email__ = "sean@freshconsulting.com"

import sys, pygame

# The HappyBall class. This is an example of object oriented programming.
# By having all the important details about HappyBall (speed, angle, image)
# self contained, it makes our code easier to update and we could even move
# HappyBall code to another program and use it there! Even better, we could
# have TWO or MORE HappyBalls bouncing around in the same environment!
class HappyBall(pygame.sprite.Sprite):

	# HappyBall constructor. When you declare that you want a new HappyBall,
	# this code is run to create all the information we need about HappyBall.
	def __init__(self, pos=(0, 0), size=(50, 50), speed=[5,5]):

		# The super method allows us to talk to the "parent" code that declared
		# a HappyBall needs to be created. You can read more about this at
		# https://docs.python.org/3/library/functions.html#super
		super(HappyBall, self).__init__()

		# Rotating an image in PyGame is a little tricky. The best way to do
		# it is to take do any calculations with a copy of our original image
		# and then apply the results to the original image. That's why you
		# see the two properties declared below.
		self.original_image = pygame.image.load('ball.png').convert_alpha()
		self.image = self.original_image
		self.rect = self.image.get_rect()
		self.rect.center = pos
		self.angle = 0
		self.speed = speed
		self.width = 900
		self.height = 600

		# We use this to track if we've "bounced" off the wall. If we have, then
		# we change our speed direction.
		self.bounced = False

	# HappyBall move method. The HappyBall is responsible for determining where
	# it should go next! This move method will rotate the ball, move it to its
	# new location based on its speed, and then determine if it has bounced. That
	# way any code that wants to draw HappyBall on the screen or interact with it
	# simply needs to ask "Hey HappyBall, where are you now?"
	def move(self):
		# Like we talked about above, we use what's called a transformation method
		# to rotate or original HappyBall image by the angle HappyBall is tracking
		# and then apply that to the image that will be displayed.
		self.image = pygame.transform.rotate(self.original_image, self.angle)

		# After making the transformation, we update our angle in anticipation of
		# the next time we need to move HappyBall. We use "modular arithmetic" here
		# to make sure that our angle always stays within the 360 degrees that a
		# circle can have. You can learn more about this at:
		# https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic
		self.angle += 1 % 360

		# It is important to track where the center of our rotation is. Otherwise
		# over time the rotations will look off.
		x, y = self.rect.center

		# Now that we have our updated value from the rotation, replace our current
		# image with the updated rectangle and then place the new rectangle's center
		# at the old center.
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)

		# Set our new location for HappyBall based on the movement speed.
		self.rect = self.rect.move(self.speed)

		# Everytime we move we assume that HappyBall hasn't bounced off a wall
		# yet. After we move HappyBall we determine whether or not HappyBall has
		# hit a wall. If so, we change the speed to be in the opposite direction
		# in anticipation of the next time we need to move HappyBall.
		self.bounced = False
		if self.rect.left < 0 or self.rect.right > self.width:
			self.speed[0] = -self.speed[0]
			self.bounced = True

		if self.rect.top < 0 or self.rect.bottom > self.height:
			self.speed[1] = -self.speed[1]
			self.bounced = True
		return self.bounced

# Here's the main code that runs when the program is started.
def main():

	pygame.init()

	size = width, height = 900, 600
	white = 255, 255, 255
	red = 255, 0, 0
	running = True
	any_ball_bounced = False

	screen = pygame.display.set_mode(size)

	fresh_background = pygame.image.load('fresh_background.png').convert_alpha()

	# Slow down our ball bouncing.
	clock=pygame.time.Clock()
	fps = 60

	# Create a new HappyBall! We use the constructor parameters
	# to set the starting location and speed for it.
	happyball = HappyBall(pos=(25, 25), speed=[10,7])

	# What?! FIVE HappyBalls, this is insane!
	happyball2 = HappyBall(pos=(25, 25), speed=[2,15])
	happyball3 = HappyBall(pos=(25, 25), speed=[19,3])
	happyball4 = HappyBall(pos=(25, 25), speed=[1,22])
	happyball5 = HappyBall(pos=(25, 25), speed=[7,5])

	# Let's move happy ball around!!!
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.display.quit()
				pygame.quit()
				sys.exit()

		# Clear the event queue after checking for quit event so that the ball
		# can bounce freely.
		pygame.event.clear()

		# Move all of our happy balls to get their new location.
		has_bounced1 = happyball.move()
		has_bounced2 = happyball2.move()
		has_bounced3 = happyball3.move()
		has_bounced4 = happyball4.move()
		has_bounced5 = happyball5.move()
		screen.fill(white)

		# Draw our background on the screen.
		screen.blit(fresh_background, [0,0])

		# If any of the balls have bounced off the edge, then we flash the
		# screen red for extra effect.
		any_ball_bounced = False

		if has_bounced1 or has_bounced2 or has_bounced3 or has_bounced4 or has_bounced5:
			any_ball_bounced = True

		if any_ball_bounced:
			screen.fill(red)

		# Draw all of our happy balls on the screen
		screen.blit(happyball.image, happyball.rect)
		screen.blit(happyball2.image, happyball2.rect)
		screen.blit(happyball3.image, happyball3.rect)
		screen.blit(happyball4.image, happyball4.rect)
		screen.blit(happyball5.image, happyball5.rect)
		pygame.display.update()

		# Tick our clock slowly.
		clock.tick(fps)

if __name__ == '__main__':
	main()
