from src import Wholesomebot
import os

wholesomebot = Wholesomebot()
print('Setup App...')
wholesomebot.setup()
print('Starting App...')
wholesomebot.start()
print('App started!' os.getpid())
