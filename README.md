# Digital Robotic Simulation Gym Space
## A microcontroller simulator inside the computer in python

###### Requeriments:
* Python 3.6
https://www.python.org/
* pygame
https://www.pygame.org/

###### Recomended:
* Conda
https://conda.io/
* A minimal computer

      -2 GB of RAM

      -At least a Pentium 4

This system was designed to simulate a microcontroller what recives orders and then executes them(like move up, move right etc.).
This allows us to test complex AI algorythms without a real robot, such as simple programmed algorythms(look at the examples
directory) to complex mathematical solutions to certain problems in the agent behaviour.

## stuff what needs to be writed by the notes we have in the real world

#### How to install and use it
First you need to clone the repository into your computer.
For doing that, you can execute this command:
```batch
git clone https://github.com/jlagarespo/Digital-Robotic-Simulation-Gym.git
```
Then to run the following command to run the program:
```batch
python main.py
```
Instead of running this command everytime you want to execute the program, you can just execute the "start.bat" file.

Then, you should see something like this:
![alt text](https://github.com/jlagarespo/Digital-Robotic-Simulation-Gym/blob/master/data/main_window.png)
If you see it, sucsses! Your done it; now you can start creating your own agent behaviours and experimenting by yourself.

####Common issues
```
Sorry, extended image module required
```
Make sure you have an extension to load more than a standart Bitmap.
________________________________________________________________________________
```
Could not load image "image"
```
Make sure the "image" exists.
Recomended to re-clone the repository in this case.
________________________________________________________________________________
```
Warnign, no sound
```
or
```
Warning, unable to load, "sound"
```
Everything should work nice, except the sound engine.
Also recomended to re-clone the repository

#### Main code workflow
When you want to make changes to the code for changing the behaviour of the program, you have to know a couple of things:

    -I'ts not recomended to modify the main.py file, because it going to change the enviroment in what you are working.

    -Also, is not recomended to change the "draw" methods, because he is the ones what draw stuff on the screen.

Then you need to know what there is a few main classes:
###### The main.py file contains no classes, but in it there is the main methods
###### The player.py contains only one class
* The Player class has got the main drawing and basic moving methods methods. Using this methods from the Agent class is what does the player move. Not recomended to modify.
###### The obstacle.py file contains also one class
* This file is work in progress so for the moment I can't give more Info.
###### The agent.py file
* As the obstacle class, this class still WIP, and it does all the program to go bad. So when finished we going to tell here how to create your own agent behaviours.

#### For making changes on the agent.py
Use the Player class methods of movement and obstacle detection to controll the behaviour of the robot what you can write inside this class.
*More info going to be here**

![alt text](https://avatars2.githubusercontent.com/u/26935885?s=40&v=4)   **Jacob Lagares Pozo && Sergi Valverde**   ![alt text](https://avatars1.githubusercontent.com/u/5285442?s=60&v=4)
