from setuptools import find_packages, setup

package_name = 'moveit2_tutorials'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dhzrn',
    maintainer_email='dhrn983@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'arm_mover = moveit2_tutorials.arm_mover:main',
            'pose_mover = moveit2_tutorials.pose_mover:main',

        ],
    },
)
