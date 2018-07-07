from ..lib.motor import Motor

class MotorsController():
  def __init__(self):
    print('> MotorsController')

  def setup(self):
    print('> Creating Motors')
    self.motors = [Motor(1), Motor(2), Motor(3), Motor(4)]
