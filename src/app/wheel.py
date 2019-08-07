
from ..lib.motor_factory import MotorFactory

class Wheel():
  def __init__(self, id):
    print('> Wheel %d' % id)
    self.motor = MotorFactory().makeMotor(id)
    self.motor.arm()

  def accelerate(self, speed):
    print('Wheel.accelerate')
    self.motor.set({
        'speed': speed
    })
