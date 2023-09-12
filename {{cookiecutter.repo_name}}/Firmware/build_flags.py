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
except Exception as e:
    logging.warning(f"Error fetching revision! {e}")
    revision = "UnknownRevision"

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
except Exception as e:
    logging.warning(f"Error fetching build host! {e}")
    revision = "UnknownHost"

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
except Exception as e:
    logging.warning(f"Error fetching build user! {e}")
    username = "UnknownUser"

# Cleanup CI
if username == "root":
    username = "github"
    host = "github"

# # Colors!
# revision = revision.replace("dirty", "\x1B[31mdirty\x1B[0m")
# host = "\x1B[34m" + host + "\x1B[0m"
# username = "\x1B[34m" + username + "\x1B[0m"

print(f"-DREVISION='\"{revision}\"'")
print(f"-DHOST='\"{host}\"'")
print(f"-DUSER='\"{username}\"'")
