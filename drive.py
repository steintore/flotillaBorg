import flotilla
import time


class Drive:

  motors = []

  def __init__(self):
    self.dock = flotilla.Client()

    while not self.dock.ready:
      pass
    self._get_motors()

  def _set_speed(self, speed):
    "Sets speed of all motors"
    for i in range(len(self.motors)):
      if speed == 0:
        print("stopping")
        self.motors[i].stop()
      else:
        if i % 2 == 0:
          self.motors[i].set_speed(speed)
        else:
          self.motors[i].set_speed(speed*-1)

  def _set_inverse_speed(self, speed):
    "Sets inverse speed to make the thing turn"
    for i in range(len(self.motors)):
      self.motors[i].set_speed(speed)

  def _stop(self):
    for m in self.motors:
      m.stop()

  def _stop_in_seconds(self, seconds):
    time.sleep(seconds)
    self._stop()

  def _get_motors(self):
    "fetched all motors connected"
    for module in self.dock.available.values():
      if module.is_a(flotilla.Motor):
        self.motors.append(module)
    print("Motors found:" , self.motors)
  
  def forover(self,seconds):
    self.driveForwards(100, seconds)
 
  def driveForwards(self, speed, seconds):
    "drive forwards for specified time"
    print("forwards", speed, seconds)
    self._set_speed(speed)
    self._stop_in_seconds(seconds)

  def bakover(self,seconds):
    self.driveBackwards(100, seconds)

  def driveBackwards(self, speed, seconds):
    "drive backwards for specified time"
    self._set_speed(speed*-1)
    self._stop_in_seconds(seconds)

  def venstre(self, seconds):
    self.turnLeft(100, seconds)

  def turnLeft(self, speed, seconds):
    "turn left for specified time"
    self._set_inverse_speed(speed)
    self._stop_in_seconds(seconds)

  def turnRight(self, speed, seconds):
    "turn right for specified time"
    self._set_inverse_speed(speed*-1)
    self._stop_in_seconds(seconds)

  def hoyre(self, seconds):
    self.turnRight(100, seconds)

  def finish(self):
    self._stop()
    self.dock.stop()

#getMotors()
#driveForwards(30, 5)
#turnLeft(30, 2)
#turnRight(30, 3)
#finish()
