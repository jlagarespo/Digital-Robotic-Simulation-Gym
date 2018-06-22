# Digital Robotic Simulation Gym Space
## A microcontroller simulator inside the computer in python

Programation workflow language: *Python*

![alt text](https://github.com/jlagarespo/Digital-Robotic-Simulation-Gym/blob/master/data/python.png)

Programming workflow language: *Python*

###### Requeriments:
* Python 3.6
https://www.python.org/
* pygame
https://www.pygame.org/
* git
https://git-scm.com/
* numpy
http://www.numpy.org/

###### Recomended:
* Conda
https://conda.io/

* A minimal computer

      -2 GB of RAM
      -At least a Pentium 4

This system was designed to simulate the behavior of an automated
agent. The agent receives orders and then executes them (like move up, move right etc.).
This will allow us to understand several algorithms ranging from
path planning to AI algorithms.
________________________________________________________________________________
## stuff what needs to be writed by the notes we have in the real world
________________________________________________________________________________
#### How to install and use it
First things first, you need to install everything.
First execute this:
```batch
cd "installation folder"
```
In the first argument, put the directory you want everything to install.
The execute this other command:
```batch
git clone https://github.com/jlagarespo/Digital-Robotic-Simulation-Gym.git
```
Congrats! You installed it!

Then to run the following command to run the program:
```batch
python main.py
```
Instead of running this command everytime you want to execute the program, you can just execute the "start.bat" file.

Then, you should see something like this:

![alt text](https://github.com/jlagarespo/Digital-Robotic-Simulation-Gym/blob/master/data/main_window.png)

Also your console, should look like this:

![alt text](https://github.com/jlagarespo/Digital-Robotic-Simulation-Gym/blob/master/data/console.png)

If it does, success! Your did it; now you can start to create and
experiment by yourself your own agent behaviors.
________________________________________________________________________________

#### Common issues
* If you get this output:
```
Sorry, extended image module required
```
Make sure you have an extension to load more than a standart Bitmap.

* Also, if something goes wrong, make sure you don't have this message:
```
Could not load image "image"
```
Make sure the "image" exists.
Recommended to re-clone the repository in this case.

* If no sound is playing, is possible to be because:
```
Warnign, no sound
```
or
```
Warning, unable to load, "sound"
```
Everything should work nicely, except the sound engine.
Also recomended to re-clone the repository.
________________________________________________________________________________
#### Main code workflow
When you want to make changes to the code for changing the behaviour of the program, you have to know a couple of things:

    -I'ts not recomended to modify the main.py file, because it going to change the enviroment in what you are working.

    -Also, is not recomended to change the "draw" methods, because he is the ones what draw stuff on the screen.

For creating your own behaviours, you should go to the brain.py class, in where the documentation already explains how to use it.
![alt text](https://github.com/jlagarespo/Digital-Robotic-Simulation-Gym/blob/master/data/brain.png)

Also for changing the main problem parameters, you should change the main simulation constants at the start of the `problem.py`

![alt text](https://github.com/jlagarespo/Digital-Robotic-Simulation-Gym/blob/master/data/problem.png)

For changing other stuff in the main code of the simulation you can
follow the comments.

________________________________________________________________________________

#### Algorithm examples
The main code is in the main folder, but in the examples folder,
there are some example algorithms (example brain and problem classes):

* The stupid agent: A simple agent that when finds an obstacle, goes in the other directions.

#### Remember we always are updating brand new algorithms!

________________________________________________________________________________
