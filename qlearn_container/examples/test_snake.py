from keras.models import Sequential
from keras.layers import *
from qlearncatchd3.games import Snake
from keras.optimizers import *
from qlearncatchd3 import Agent

grid_size = 10
nb_frames = 4
nb_actions = 5

model = Sequential()
model.add(Convolution2D(16, nb_row=3, nb_col=3, activation='relu', input_shape=(nb_frames, grid_size, grid_size)))
model.add(Convolution2D(32, nb_row=3, nb_col=3, activation='relu'))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(nb_actions))
model.compile(RMSprop(), 'MSE')

snake = Snake(grid_size)

agent = Agent(model=model, memory_size=-1, nb_frames=nb_frames)
agent.train(snake, batch_size=64, nb_epoch=10000, gamma=0.8)
agent.play(snake)
