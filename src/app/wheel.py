from ..lib.motor import Motor

class Wheel():
  def __init__(self):
    print('> Wheel')
    self.motor = Motor()

  def setup(self):
    print('setup Wheel')
