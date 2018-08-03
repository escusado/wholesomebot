import json

class Motor():
  def __init__(self, motorInstance):
    print('> Motor')
    self.motor = motorInstance
    self.speed = 0 # backwards - 0 + foward

  def set(self, properties):
    print('set %s', json.dumps(properties))
    self.motor.setSpeed(properties['speed'])
