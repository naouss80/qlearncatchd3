__author__ = "Eder Santana"

import numpy as np
from .game import Game


class Catch(Game):

	def __init__(self, grid_size=10):
		self.grid_size = grid_size
		self.won = False
		self.reset()

	def reset(self):
		n = np.random.randint(0, self.grid_size, size=1) # fruit - never at corner (x of fruit)
		m = np.random.randint(1, self.grid_size-1, size=1) # Basket - center always 1 away from corners
		self.state = np.asarray([0, n, m])[np.newaxis]

	@property
	def name(self):
		return "Catch"

	@property
	def nb_actions(self):
		return 3

	def play(self, action):
		state = self.state
		if action == 0:
			action = -1
		elif action == 1:
			action = 0
		else:
			action = 1
		f0, f1, basket = state[0]
		new_basket = min(max(1, basket + action), self.grid_size-2)
		f0 += 1
		out = np.asarray([f0, f1, new_basket])
		out = out[np.newaxis]
		assert len(out.shape) == 2
		self.state = out

	def get_state(self):
		im_size = (self.grid_size,) * 2
		state = self.state[0]
		canvas = np.zeros(im_size)
		canvas[state[0], state[1]] = 1 # plot fruit
		canvas[-1, state[2]-1:state[2] + 2] = 1 # plot basket
		return canvas

	def get_node_state(self):
		node_data = {}
		node_data['fruit_row'] = self.state[0][0]
		node_data['fruit_col'] = self.state[0][1]
		node_data['basket'] = self.state[0][2]		
		return node_data

	def get_score(self):
		fruit_row, fruit_col, basket = self.state[0]
		if fruit_row == self.grid_size-1:
			if abs(fruit_col - basket) <= 1:
				self.won = True
				return 1
			else:
				return -1
		else:
			return 0

	def is_over(self):
		if self.state[0, 0] == self.grid_size-1:
			return True
		else:
			return False

	def is_won(self):
		fruit_row, fruit_col, basket = self.state[0]
		return fruit_row == self.grid_size-1 and abs(fruit_col - basket) <= 1


class CatchReverse(Catch):

	@property
	def name(self):
		return "CatchReverse"	

	def get_score(self):
		fruit_row, fruit_col, basket = self.state[0]
		if fruit_row == self.grid_size-1:
			if abs(fruit_col - basket) > 1:
				self.won = True
				return 1
			else:
				return -1
		else:
			return 0

	def is_won(self):
		fruit_row, fruit_col, basket = self.state[0]
		return fruit_row == self.grid_size-1 and abs(fruit_col - basket) > 1		

class CatchRandom(Catch):

	@property
	def name(self):
		return "CatchRandom"			


	def play(self, action):
		state = self.state
		if action == 0: # move left
			action = -1
		elif action == 1: # no movement
			action = 0
		else: # move right
			action = 1
		f0, f1, basket = state[0]
		# new basket center is always between 1 and 8
		# NOTE: indexing is from 0-9 
		# This solve the conceptial problem but does not help in terms of D3 view
		new_basket = min(max(1, basket + action), self.grid_size-2) 
		# add function to keep everything within the middle 
		fruit_action = np.random.randint(-1, 2, size=1)[0]
		# no less than 0 and no more than 10
		f1 = min(max(0, f1 + fruit_action), self.grid_size-1)
		f0 += 1 # state or y of fruit
		out = np.asarray([f0, f1, new_basket])
		out = out[np.newaxis]
		assert len(out.shape) == 2
		self.state = out



class CatchRandomReverse(CatchRandom):

	@property
	def name(self):
		return "CatchRandomReverse"	

	def get_score(self):
		fruit_row, fruit_col, basket = self.state[0]
		if fruit_row == self.grid_size-1:
			if abs(fruit_col - basket) > 1:
				self.won = True
				return 1
			else:
				return -1
		else:
			return 0

	def is_won(self):
		fruit_row, fruit_col, basket = self.state[0]
		return fruit_row == self.grid_size-1 and abs(fruit_col - basket) > 1			
