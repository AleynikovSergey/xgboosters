# General modules
############################################################################
import time
import sys
import socket
import threading
import pytest
import collections
############################################################################


# Path to project code. Need to be changed in each version
############################################################################
# Add the folder path to the sys.path list
sys.path.append('../../code/SmartHouse-2.0.0/')
############################################################################


# Proejct module import - what is tested
############################################################################
from monitor.monitor import MessageHandler
from monitor.monitor import Monitor
from monitor.message_service import MessageServer
from monitor.config import Config
############################################################################


# Wrapper for monitor calls. It is used majority of unit tests
############################################################################
# Create monitor_default from config.yaml
class MonitorDefaultThread(object):
    # Creata a new monitor in separate thread
    def __init__(self):
        self._thread_a = threading.Thread(target=self.run_wrapper)
        self._thread_a.daemon = True
        self._thread_a.start()

    # Wrapper to run monitor run function
    def run_wrapper(self):
        Monitor('config.yaml').run()

    # Stop executing monitor
    def stop(self, timeout):
        self._thread_a.join(timeout)

# Monitor uses default settings
@pytest.fixture()
def monitor_default():
    return MonitorDefaultThread()


############################################################################