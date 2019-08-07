from .wheel import Wheel

class FourWheelDrive():
  def __init__(self):
    print('> FourWheelDrive')
    self.wheels = [Wheel(1), Wheel(2), Wheel(3), Wheel(4)]
    # 1 2
    # 3 4

  def setup(self):
    print('setup FourWheelDrive')

  def update(self):
    self.wheels[0].accelerate(10)
    self.wheels[1].accelerate(10)
    self.wheels[2].accelerate(10)
    self.wheels[3].accelerate(10)
