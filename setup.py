from setuptools import setup, find_namespace_packages, Command
import os
from install.install_command import WattsonInstallDependencies


setup(
    name='wattson',
    version="2.0.0",
    packages=find_namespace_packages(include=[
        'wattson.*',
        'wattson.__main__'
    ]),
    package_data={
        '': ["*"]
    },
    entry_points={
        "console_scripts": [
            "wattson = wattson.cosimulation.control.__main__:main",
            "wattson-dedicated = wattson.topology.__main__:standalone",
            "wattson-stats = wattson.analysis.statistics.__main__:main",
            "wattson-preview = wattson.analysis.preview.__main__:main",
            "wattson-clean = wattson.util.clean.__main__:main"
        ]
    },
    cmdclass={
        "wattson": WattsonInstallDependencies,
    },
    install_requires=[
        'wheel',
        'ifcfg',
        'ninja',
        'testresources',
        'c104~=1.16.0',
        'python-dateutil',
        'docker',
        'ipaddress==1.0.23',
        'matplotlib>=3.9.2',
        'more_itertools==5.0.0',
        'netifaces==0.11.0',
        'networkx>=2.5',
        'numba>=0.60.0',
        'numpy==1.26.4',
        'packaging==24.1',
        'pandapower==2.14.11',
        #'pandapower @ git+https://github.com/e2nIEE/pandapower.git@2feba868882479fba6c8b0882c1bc77dfc71c77d#egg=pandapower',
        'powerowl @ git+https://github.com/MForystek/powerowl.git@dev',
        'pandas>=2.2.2',
        'psutil==5.7.0',
        'pydot',
        'pymodbus==2.5.2',
        'pytest',
        'igraph==0.9.9',
        'python-iptables @ git+https://github.com/lennart-bader/python-iptables.git',
        'pathfinding',
        'pyprctl',
        'qtpy',
        'pydantic',
        'pytimeparse2>=1.6.0',
        'PyQt5==5.15.4',
        'PyQtWebEngine==5.15.4',
        'pywebview>=3.3.5',
        'pyyaml>=5.4',
        'pyzmq==20.0.0',
        'scapy==2.4.4',
        'scipy>=1.13.1',
        'setuptools>=74.1.2',
        'shapely',
        'sqlalchemy==1.3.16',
        'tabulate',
        'twisted>=22.2.0',
        'ifcfg'
    ],
    python_requires=">=3.10.12",
    author="Lennart Bader (Fraunhofer FKIE)",
    author_email="lennart.bader@fkie.fraunhofer.de",
)

