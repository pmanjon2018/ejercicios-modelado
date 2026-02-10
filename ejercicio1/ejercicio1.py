#python3 -m ejercicio1.py

import pybullet as p
import pybullet_data
import time
import math

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)

planeId = p.loadURDF("plane.urdf")

euler_angles = [0, 0, 0]
startOrientation = p.getQuaternionFromEuler(euler_angles)
startPosition = [0, 0, 1]

robotId = p.loadURDF("ejercicio1.urdf", startPosition, startOrientation)

# Sliders para controlar los giros
slider_horizontal = p.addUserDebugParameter("Horizontal Z", -math.pi, math.pi, 0.0)
slider_vertical = p.addUserDebugParameter("Vertical Y", -math.pi/2, math.pi/2, 0.0)

for i in range(10000):
    p.setJointMotorControl2(robotId, 0, p.POSITION_CONTROL, p.readUserDebugParameter(slider_horizontal))
    p.setJointMotorControl2(robotId, 1, p.POSITION_CONTROL, p.readUserDebugParameter(slider_vertical))
    p.stepSimulation()
    time.sleep(1./240.)

p.disconnect()