from app.rover import Rover

class Wholesomebot():
  def __init__(self):
    print('> Wholesomebot')
    self.rover = Rover()

  def setup(self):
    self.rover.setup()

  def start(self):
    print('> Wholesomebot.started')
