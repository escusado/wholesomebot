import json
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

class Motor():
  def __init__(self, motorInstance):
    print('> Motor')
    self.motor = motorInstance
    self.state = {
      speed : 0 # backwards - 0 + foward
    }

  def arm(self):
    print('Motor arm')
    self.motor.run(Adafruit_MotorHAT.RELEASE)
    self.motor.run(Adafruit_MotorHAT.FORWARD)

  def set(self, properties):
    print('set %s', json.dumps(properties))
    self.state.update(properties)

  def update(self):
    print('setting speed:', self.state['speed'])
    if(self.state['speed']):
      self.motor.run(Adafruit_MotorHAT.FORWARD)
    else:
      self.motor.run(Adafruit_MotorHAT.BACKWARD)
    self.motor.setSpeed(abs(self.state['speed']))
    print('speed set')
