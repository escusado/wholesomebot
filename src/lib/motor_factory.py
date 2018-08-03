import json
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
from .motor import Motor

class MotorFactory():
  class __MotorFactory:
    def __str__(self):
      return repr(self) + self.val
  instance = None
  def __init__(self):
    mh = Adafruit_MotorHAT(addr=0x60)

    if not MotorFactory.instance:
      MotorFactory.instance = MotorFactory.__MotorFactory()
      atexit.register(MotorFactory.instance.turnOffMotors)

  def __getattr__(self, name):
    return getattr(self.instance, name)

  def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

  def makeMotor(self, id):
    print('> makeMotor %d' % id)
    return Motor(mh.getMotor(id))
