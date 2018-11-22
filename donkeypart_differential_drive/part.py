import time

class TwoWheelDifferentialDrive:
    """
    Mixer for vehicles driving differential drive vehicle.
    Currently designed for cars with 2 wheels.
    """

    def __init__(self, left_motor, right_motor):

        self.left_motor = left_motor
        self.right_motor = right_motor

        self.angle = 0
        self.throttle = 0

    def update(self, throttle, angle):
        self.throttle = throttle
        self.angle = angle

        if throttle == 0 and angle == 0:
            self.stop()
        else:

            l_speed = ((self.left_motor.speed + throttle) / 3 - angle / 5)
            r_speed = ((self.right_motor.speed + throttle) / 3 + angle / 5)
            l_speed = min(max(l_speed, -1), 1)
            r_speed = min(max(r_speed, -1), 1)

            self.left_motor.turn(l_speed)
            self.right_motor.turn(r_speed)

    def test(self, seconds=1):
        telemetry = [(0, -.5), (0, -.5), (0, 0), (0, .5), (0, .5), (0, 0), ]
        for t in telemetry:
            self.update(*t)
            print('throttle: %s   angle: %s' % (self.throttle, self.angle))
            print('l_speed: %s  r_speed: %s' % (self.left_motor.speed,
                                                self.right_motor.speed))
            time.sleep(seconds)

        print('test complete')

    def stop(self):
        self.left_motor.turn(0)
        self.right_motor.turn(0)
