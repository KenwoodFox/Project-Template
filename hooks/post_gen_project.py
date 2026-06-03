#!/usr/bin/env python3
"""Remove the CI folder that does not match the selected VCS"""
import os
import shutil
import sys


def remove_path(path: str) -> None:
    if not os.path.exists(path):
        return
    if os.path.isdir(path):
        shutil.rmtree(path)
    else:
        os.remove(path)


def main() -> None:
    platform = "{{ cookiecutter.vcs_platform }}"
    project_dir = os.getcwd()

    if platform == "github":
        remove_path(os.path.join(project_dir, ".gitea"))
    elif platform == "gitea":
        remove_path(os.path.join(project_dir, ".github"))
    else:
        print(f"Unknown vcs_platform: {platform!r}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
