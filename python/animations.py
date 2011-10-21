import math
import random
import octoapi
import time
import thread

class Animation():
	is_running = True
	pixels = []

	def update(self, timeDiff):
		pass

	def render(self, pixels):
		pass
	
	def destroy(self):
		self.is_running = False

class SunClouds(Animation):
	"""Represents cloudiness/sunshine"""

	def __init__(self, shine_type, speed, width):
		for i in range(0, 8):
			self.pixels.append((0,0,0))

		self.speed = float(speed)
		self.shine_type = shine_type
		self.position = 0.0
		self.direction = -1.0
		self.width = random.random() * 5

	def loop(self):
		if self.is_running:
			c.update(0.04)
			c.render()
			octoapi.write(self.pixels)
			time.sleep(.03)

	def update(self, timeDiff):
		self.position += self.direction * self.speed * timeDiff
		if (self.position < -1.):
			self.position = 2.
			width = random.random() * 5 
		print "position: %f, speed: %f direction: %f"%(self.position, self.speed, self.direction)
	
	def render(self):
		size = float(len(self.pixels))
		qq = [0,0,0,0,0,0,0,0]
		for i,pixel in enumerate(self.pixels):
			pos = (i+0.5)/size
			intensity = max(0,min(1,(1-abs(pos-self.position))))
			intensity = math.pow(intensity,self.width)
			maxval = 1022
			val = maxval * intensity + 1
			if shine_type == "cloud":
				self.pixels[i] = (val, val, val)
			else:
				self.pixels[i] = (val, val, 0)
			qq[i] = intensity
		print qq
		return self.pixels

class RSL(Animation):
	"""Represents Rain | Snow | Lightning, since their codebases are quite similar"""

	def __init__(self, precip_type, lightning, update_speed):
		self.update_speed = update_speed
		self.precip_type = precip_type
		self.lightning = lightning

		for i in range(0, 8):
			self.pixels.append((0,0,0))
		self.thread_id = thread.start_new_thread(self.loop, ())

	def loop(self):
		while self.is_running:
			self.render()
			octoapi.write(self.pixels)
			time.sleep(self.update_speed)

	def render(self, pixels):
		size = float(len(pixels))
		qq = [0,0,0,0,0,0,0,0]

		for i, pixel in enumerate(pixels):
			pixels[i] = (0,0,0)

		indexCount = random.randint(0, 7)
		for i in range(0, indexCount):
			randomIndex = random.randint(0, 7)
			if (precip_type == "rain"):
				pixels[randomIndex] = (0, 0, 100)
			else:
				pixels[randomIndex] = (1023, 1023, 1023)

		if self.lightning:
			if random.randint(0, 10) is 5:
				randomIndex = random.randint(0,7)
				pixels[randomIndex] = (1023, 1023, 1023)

		print pixels
		return pixels

#if __name__ == "__main__":
#	pixels = [(),(),(),(),(),(),(),()]
#	c = Cloudy(0.1, 0.1)
#	while True:
#		c.update(0.04)
#		c.render(pixels)
#		octoapi.write(pixels)
#		time.sleep(.03)
