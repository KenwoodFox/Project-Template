import logging
import subprocess

from datetime import date


today = date.today()

try:
    revision = (
        subprocess.check_output(
            [
                "git",
                "describe",
                "--abbrev=8",
                "--dirty",
                "--always",
                "--tags",
            ]
        )
        .strip()
        .decode("utf-8")
    )

    print(f"-D REVISION='\"{revision}\"'")
except Exception as e:
    logging.warning("Getting git revision failed!! Check that you have git installed?")
    logging.warning(e)

    print("-D REVISION='Unknown'")

try:
    host = (
        subprocess.check_output(
            [
                "hostname",
            ]
        )
        .strip()
        .decode("utf-8")
    )

    print(f"-D FWHOST='\"{host}\"'")
except Exception as e:
    logging.warning("Getting host failed!! Are you using a UNIX compatible system?")
    logging.warning(e)

    print("-D FWHOST='Unknown'")

try:
    username = (
        subprocess.check_output(
            [
                "id",
                "-u",
                "-n",
            ]
        )
        .strip()
        .decode("utf-8")
    )

    # Cleanup CI
    if username == "root":
        username = "git"
        host = "git"

    print(f"-D USERNAME='\"{username}\"'")
except Exception as e:
    logging.warning("Getting host failed!! Are you using a UNIX compatible system?")
    logging.warning(e)

    print("-D USERNAME='Unknown'")

# Print to enable debugging
# print("-D DEBUG")
