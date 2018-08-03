import json
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

class Motor():
  def __init__(self, motorInstance):
    print('> Motor')
    self.motor = motorInstance
    self.speed = 0 # backwards - 0 + foward

  def arm(self):
    print('Motor arm')
    self.motor.run(Adafruit_MotorHAT.RELEASE)
    self.motor.run(Adafruit_MotorHAT.FORWARD)

  def set(self, properties):
    print('set %s', json.dumps(properties))
    self.state.update(properties)

  def update(self):
    print('setting speed:', self.state['speed'])
    self.motor.setSpeed(self.state['speed'])
    print('speed set')
