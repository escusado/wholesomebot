from .wheel import Wheel

class FourWheelDrive():
  def __init__(self):
    print('> FourWheelDrive')
    self.wheels = [Wheel(), Wheel(), Wheel(), Wheel()]
    # 0 1
    # 2 3

  def setup(self):
    print('setup FourWheelDrive')
