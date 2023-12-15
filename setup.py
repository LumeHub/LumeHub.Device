from setuptools import setup, find_packages

setup(
    name='lumehub-device',
    version='0.1',
    packages=find_packages(),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            'lumehub_device = lumehub_device.main:main',
        ],
    },
    package_data={
        '': ['*.ini'],  # Include configuration files
    },
)
