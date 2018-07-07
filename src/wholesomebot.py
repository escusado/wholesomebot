from app.motors_controller import MotorsController

class Wholesomebot():
  def __init__(self):
    print('> Wholesomebot')
    self.motorsController = MotorsController()

  def setup(self):
    self.motorsController.setup()

  def start(self):
    print('> Wholesomebot.started')
