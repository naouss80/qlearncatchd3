# qlearncatchd3
A simple game of catch using QLearning 

## Intro

This is a very simplified start to Qlearning using docker inspired by [farizrahman4u link](https://github.com/farizrahman4u/qlearning4k).

### Requirements
Please install docker on your Unix based or Windows 10 machine.
This is 10x easier than trying to install python3, node, tensorflow, keras, d3, socket.io, express ...
Docker will do this for you

To run this, do the following

## 1 - Clone and build-run the viz server
```Bash
# a- clone the container
git clone 
# b- access the folder
cd qlearncatchd3
# build the container
docker build -t viz_server node_container
# run the container
docker run -it -p 80:80 -p 2814:2814 viz_server node viz_server.js debug
```
## 2 - Open the browser
Go to `localhost`
You should see the following


![alt text](https://github.com/naouss80/qlearncatchd3/raw/master/images/start_window.PNG)

## 3 - Get local IP addres and build-run the qlearning app
Get IP adddress for [windows link](https://kb.wisc.edu/page.php?id=27309) with `ipconfig /all`.
For Unix systems use `ifconfig`
An example of this can be 10.227.40.281

Open another command line window
```Bash
# assuming one is still in the repository folder 
# build the container qlearncatchd3
docker build -t qlearnin qlearn_container
# run the container
# docker run -it qlearnin python test_catch.py <game> <ip_address> <debug_optional> <node_optional> <count_of_epoch_optional>
docker run -it qlearnin python test_catch.py Catch 10.227.40.281 debug with_node 1000
```

There are 4 games:
* `Catch`: The basket should catch a fruit falling linearly
* `CatchReverse`: The basket should avoid the fruit linearly
* `CatchRandom`: The basket should catch a fruit falling randomly
* `CatchRandomReverse`: The basket should avoid a fruit falling randomly

## 4 - Go back to browser
Go back to the browser and see the training process


![alt text](https://github.com/naouss80/qlearncatchd3/raw/master/images/catch_game.gif)