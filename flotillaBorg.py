import flotilla

class FlotillaBorg:

    flippedMotors = True
    motors = []

    def Init(self, flippedMotors = True):
        self.dock = flotilla.Client()
        print("Client connected...")
	self.flippedMotors = flippedMotors
        
	while not self.dock.ready:
            pass

        print("Finding modules...")
	self._get_motors()

    def _get_motors(self):
        "fetched all motors connected"
        for module in self.dock.available.values():
          if module.is_a(flotilla.Motor):
            self.motors.append(module)
        print("Motors found:" , self.motors)

    def _set_speed(selft, speed):
        "Setting speed of all motors"
        for i in range(len(self.motors)):
            if speed == 0:
                self.motors[i].stop()
            else:
                if self.flippedMotors == True & i % 2 != 0:
                    self.motors[i].set_speed(speed *-1)
                else:
                    self.motors[i].set_speed(speed)

    def forwards(self, speed = 100):
        "drive forwards"
        self._set_speed(speed)

    def backwards(self, speed = 100):
        "drive backwards"
        self._set_speed(speed*-1)

    def setMotor1(self, speed):
        self.motors[0].set_speed(speed)

    def setMotor2(self, speed):
        if self.flippedMotors:
            self.motors[1].set_speed(speed*-1)
        else:
            self.motors[1].set_speed(speed)

    def stop(self):
        print("Stopping")
        for m in self.motors:
            m.stop()

    def finish(self):
        print("Finish")
        self.stop()
        self.dock.stop()
