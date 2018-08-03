import time
from app.rover import Rover

class Wholesomebot():
  def __init__(self):
    print('> Wholesomebot')
    self.rover = Rover()

  def setup(self):
    self.rover.setup()

  def start(self):
    print('> Wholesomebot.started')
    while(True):
      self.rover.update()
      time.sleep(0.01)
