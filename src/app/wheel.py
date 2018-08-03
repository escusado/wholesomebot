
from ..lib.motor_factory import MotorFactory

class Wheel():
  def __init__(self, id):
    print('> Wheel %d' % id)
    self.motor = MotorFactory().makeMotor(id)

  def setup(self):
    print('setup Wheel')
    self.motor.set({
        'speed': 10
    })
