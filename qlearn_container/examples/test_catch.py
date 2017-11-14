from keras.models import Sequential
from keras.layers import Flatten, Dense
from qlearncatchd3.games import Catch, CatchReverse, CatchRandom, CatchRandomReverse
from keras.optimizers import *
from qlearncatchd3 import Agent
import sys
import argparse

# to get longer epochs
def int_it(x):
	try:
		x = int(x)
	except:
		x = 0
	return x

# to get arguments of the command line
def get_arg(x):
	try:
		if x in sys.argv[1:]:
			x = True
		else:
			x = None
	except:
		x = None
	return x

# find IP addess
def get_ip(arg_list):
	for x in arg_list:
		x = str(x)
		if x.find('.')>0:
			return x
	if x.find('.')<0:
		return 'localhost'


# to get the debug argument
debug = get_arg("debug")

# to get the with node argument
with_node = get_arg("with_node")

# to get ip_adress passed
ip_address = get_ip(sys.argv[1:])


# to get the game name
try:
	the_game = sorted(list(set(['Catch', 'CatchReverse', 'CatchRandom', 'CatchRandomReverse']).intersection(set(sys.argv[1:]))))[0]
except:
	the_game = "Catch"

# get user privided number of epochs
nb_epoch = sum([int_it(x) for x in sys.argv[1:]])
# default to 1000 if none provided
if (nb_epoch==0): nb_epoch = 1000

print("The number of epochs is: {}, The game is: {}, The ip_address is: {} ".format(nb_epoch, the_game, ip_address))

grid_size = 10
hidden_size = 100
nb_frames = 1


model = Sequential()
model.add(Flatten(input_shape=(nb_frames, grid_size, grid_size)))
model.add(Dense(hidden_size, activation='relu'))
model.add(Dense(hidden_size, activation='relu'))
model.add(Dense(3))
model.compile(sgd(lr=.2), "mse")

the_games = {'Catch': Catch(grid_size), 
			'CatchReverse': CatchReverse(grid_size), 
			'CatchRandom': CatchRandom(grid_size), 
			'CatchRandomReverse': CatchRandomReverse(grid_size)}

catch = the_games[the_game]
agent = Agent(model=model, debug=debug, with_node=with_node, ip_address=ip_address)
agent.train(catch, batch_size=1000, nb_epoch=nb_epoch, epsilon=.1,) # nb_epoch=1000
agent.play(catch, visualize=True)
