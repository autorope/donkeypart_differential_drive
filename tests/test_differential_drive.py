# -*- coding: utf-8 -*-
import pytest
from donkeypart_differential_drive import TwoWheelDifferentialDrive

class FakeMotor:
    speed = 0
    def turn(self, speed):
        self.speed = speed
        return speed


@pytest.fixture()
def differential_drive_part():
    left_motor = FakeMotor()
    right_motor = FakeMotor()
    dd = TwoWheelDifferentialDrive(left_motor, right_motor)
    return dd


def test_update(differential_drive_part):
    """Example test."""
    dd = differential_drive_part
    dd.update(1, 0)
    assert dd.throttle == 1
    assert dd.angle == 0



