# from ..lib.motor import Motor
from .four_wheel_drive import FourWheelDrive

class Rover():
  def __init__(self):
    print('> Rover')
    self.fourWheelDrive = FourWheelDrive()

  def setup(self):
    print('setup Rover')

  def update(self):
    self.fourWheelDrive.update()
