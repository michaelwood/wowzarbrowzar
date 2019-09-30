#!/usr/bin/env python3

from distutils.core import setup

setup(
    name="WowzarBrowzar",
    version="0.1",
    author="Michael Wood",
    description="A browser launcher",
    scripts=['wowzarbrowzar'],
    data_files=[
        ('share/applications', ['wowzarbrowzar.desktop']),
    ]
)

try:
    import subprocess
    # Make sure the desktop database is updated
    subprocess.check_output(['update-desktop-database', '-q'])
except Exception:
    # Optional step to get this in the Xdesktop menus
    pass
