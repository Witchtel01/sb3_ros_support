#!/usr/bin/env python

from setuptools import find_packages, setup

package_name = "sb3_ros_support"
# fetch values from package.xml
setup(
    name=package_name,
    version="2.0.0",
    packages=find_packages(exclude=[]),
    data_files=[
        ("share/ament_index/resource_index/packages",
            ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools", "rclpy"],
    zip_safe=True,
    maintainer="Witchtel01",
    maintainer_email="engineeringkerbals@gmail.com",
    description="The ROS Support Package for Stable Baselines3",
    license="MIT",
    url="https://github.com/ncbdrck/sb3_ros_support",
    author="Jayasekara Kapukotuwa",
    author_email="j.kapukotuwa@research.ait.ie",
    keywords=["ROS", "reinforcement learning", "machine-learning", "gym", "robotics", "openai", "stable-baselines3", "multiros", "sb3"],
    # package_dir={"": "src"}
)