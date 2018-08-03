import json
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

class Motor():
  def __init__(self, motorInstance):
    print('> Motor')
    self.motor = motorInstance
    self.speed = 0 # backwards - 0 + foward

  def set(self, properties):
    print('set %s', json.dumps(properties))
    print('set speed %d', properties['speed'])
    self.motor.setSpeed(properties['speed'])
    self.motor.run(Adafruit_MotorHAT.FORWARD);
    print('speed set')
