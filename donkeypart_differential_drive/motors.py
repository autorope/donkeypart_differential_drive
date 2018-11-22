import time

def map_range(x, X_min, X_max, Y_min, Y_max):
    '''
    Linear mapping between two ranges of values
    '''
    X_range = X_max - X_min
    Y_range = Y_max - Y_min
    XY_ratio = X_range/Y_range

    y = ((x-X_min) / XY_ratio + Y_min) // 1

    return int(y)

class AdafruitMotor:
    """
    Adafruit DC Motor Controller
    For differential drive cars you need one controller for each motor.
    """

    def __init__(self, motor_num):
        from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor
        import atexit

        self.FORWARD = Adafruit_MotorHAT.FORWARD
        self.BACKWARD = Adafruit_MotorHAT.BACKWARD
        self.mh = Adafruit_MotorHAT(addr=0x60)

        self.motor = self.mh.getMotor(motor_num)
        self.motor_num = motor_num

        atexit.register(self.turn_off_motor)
        self.speed = 0
        self.throttle = 0

    def turn_off_motor(self):
        self.mh.getMotor(self.motor_num).run(Adafruit_MotorHAT.RELEASE)

    def turn(self, speed):
        '''
        Update the speed of the motor where 1 is full forward and
        -1 is full backwards.
        '''
        if speed > 1 or speed < -1:
            raise ValueError("Speed must be between 1(forward) and -1(reverse)")

        self.speed = speed
        self.throttle = int(map_range(abs(speed), -1, 1, -255, 255))

        if speed > 0:
            self.motor.run(self.FORWARD)
        else:
            self.motor.run(self.BACKWARD)

        self.motor.setSpeed(self.throttle)

    def test(self, seconds=.5):
        speeds = [-.5, -1, -.5, 0, .5, 1, 0]
        for s in speeds:
            self.turn(s)
            time.sleep(seconds)
            print('speed: %s   throttle: %s' % (self.speed, self.throttle))
        print('motor #%s test complete' % self.motor_num)