#!/usr/bin/python3
"""A module for Fabric script that generates a .tgz archive."""
import os
from datetime import datetime
from fabric.api import local, runs_once

@runs_once
def do_pack():
    """Archives the static files."""
    try:
        if not os.path.isdir("versions"):
            os.mkdir("versions")
        
        d_time = datetime.now()
        output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            d_time.year,
            d_time.month,
            d_time.day,
            d_time.hour,
            d_time.minute,
            d_time.second
        )

        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        
        if os.path.exists(output):
            size = os.path.getsize(output)
            print("web_static packed: {} -> {} Bytes".format(output, size))
        else:
            print("Packaging failed. {} does not exist.".format(output))
            output = None

    except Exception as e:
        print("An error occurred:", str(e))
        output = None

    return output

# Test the do_pack() function
if __name__ == "__main__":
    do_pack()
