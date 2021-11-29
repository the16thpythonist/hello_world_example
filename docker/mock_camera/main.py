"""
This is a simple UfoTest plugin which enables the MockCamera to be used instead of the default UfoCamera.
"""
from ufotest.hooks import Filter
from ufotest.camera import MockCamera


@Filter('camera_class', 10)
def use_mock_camera(value):
    return MockCamera
