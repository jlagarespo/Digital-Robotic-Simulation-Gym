# Digital Robotic Simulation Gym Space
## A microcontroller simulator inside the computer in python

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
* For the moment it does not exist, but in the future, here is were all the modificable stuff is. It's the behaviour what program uses for controlling the player. The better modificable file. Some example behaviour going to be in the future "examples" directory.

#### For making changes on the agent.py
Use the Player class methods of movement and obstacle detection to controll the behaviour of the robot what you can write inside this class.
*More info going to be here**

**Jacob Lagares Pozo && Sergi Valverde**
