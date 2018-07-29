from subprocess import call
import os

path = os.path.dirname(os.path.abspath(__file__))

print("You are in", path)
print("Input the name of the model you want to run> ")

a = input()
call(["cd", path + "/models/" + a + "/"])
call(["python", ("/problem.py")])
