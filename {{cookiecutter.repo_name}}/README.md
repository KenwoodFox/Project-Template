[![Docs](https://{{cookiecutter.gitprovider}}.com/{{cookiecutter.username}}/{{cookiecutter.repo_name}}/actions/workflows/docs_workflow.yml/badge.svg)](https://{{cookiecutter.gitprovider}}.com/{{cookiecutter.username}}/{{cookiecutter.repo_name}}/actions/workflows/docs_workflow.yml)
[![Hardware](https://{{cookiecutter.gitprovider}}.com/{{cookiecutter.username}}/{{cookiecutter.repo_name}}/actions/workflows/hardware_workflow.yml/badge.svg)](https://{{cookiecutter.gitprovider}}.com/{{cookiecutter.username}}/{{cookiecutter.repo_name}}/actions/workflows/hardware_workflow.yml)
[![Firmware](https://{{cookiecutter.gitprovider}}.com/{{cookiecutter.username}}/{{cookiecutter.repo_name}}/actions/workflows/firmware_workflow.yml/badge.svg)](https://{{cookiecutter.gitprovider}}.com/{{cookiecutter.username}}/{{cookiecutter.repo_name}}/actions/workflows/firmware_workflow.yml)


# {{cookiecutter.repo_name}}

![Banner](Static/Banner.png)

This repo contains all the firmware and hardware for the {{cookiecutter.repo_name}}.

If you're looking for the latest docs/builds, see our [Releases Page](https://{{cookiecutter.gitprovider}}.com/{{cookiecutter.username}}/{{cookiecutter.repo_name}}/releases).

# Getting Started

First, clone this repo (and optionally checkout a branch)

```shell
git clone https://{{cookiecutter.gitprovider}}.com/{{cookiecutter.username}}/{{cookiecutter.repo_name}}.git
cd {{cookiecutter.repo_name}}
```

# Init Submodules

Some libraries and resources are included as submodules, run the following
command to initialize them before opening the main sch

(If you get a missing library error, make sure to do this)

```shell
git submodule update --init --recursive
```


## Project Layout

If you want to use this project template for yourself, you can find it [here!](https://{{cookiecutter.gitprovider}}.com/KenwoodFox/Project-Template)
