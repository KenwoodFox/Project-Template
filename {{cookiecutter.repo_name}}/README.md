{%- if cookiecutter.vcs_platform == "github" -%}
[![Docs](https://github.com/{{cookiecutter.vcs_owner}}/{{cookiecutter.repo_name}}/actions/workflows/docs_workflow.yml/badge.svg)](https://github.com/{{cookiecutter.vcs_owner}}/{{cookiecutter.repo_name}}/actions/workflows/docs_workflow.yml)
[![Hardware](https://github.com/{{cookiecutter.vcs_owner}}/{{cookiecutter.repo_name}}/actions/workflows/hardware_workflow.yml/badge.svg)](https://github.com/{{cookiecutter.vcs_owner}}/{{cookiecutter.repo_name}}/actions/workflows/hardware_workflow.yml)
[![Firmware](https://github.com/{{cookiecutter.vcs_owner}}/{{cookiecutter.repo_name}}/actions/workflows/firmware_workflow.yml/badge.svg)](https://github.com/{{cookiecutter.vcs_owner}}/{{cookiecutter.repo_name}}/actions/workflows/firmware_workflow.yml)
{%- else -%}
[![Docs]({{cookiecutter.gitea_url}}/{{cookiecutter.vcs_owner}}/{{cookiecutter.repo_name}}/actions/workflows/docs_workflow.yml/badge.svg)]({{cookiecutter.gitea_url}}/{{cookiecutter.vcs_owner}}/{{cookiecutter.repo_name}}/actions/workflows/docs_workflow.yml)
[![Hardware]({{cookiecutter.gitea_url}}/{{cookiecutter.vcs_owner}}/{{cookiecutter.repo_name}}/actions/workflows/hardware_workflow.yml/badge.svg)]({{cookiecutter.gitea_url}}/{{cookiecutter.vcs_owner}}/{{cookiecutter.repo_name}}/actions/workflows/hardware_workflow.yml)
[![Firmware]({{cookiecutter.gitea_url}}/{{cookiecutter.vcs_owner}}/{{cookiecutter.repo_name}}/actions/workflows/firmware_workflow.yml/badge.svg)]({{cookiecutter.gitea_url}}/{{cookiecutter.vcs_owner}}/{{cookiecutter.repo_name}}/actions/workflows/firmware_workflow.yml)
{%- endif %}


# {{cookiecutter.repo_name}}

![Banner](Static/Banner.png)

This repo contains all the firmware and hardware for the {{cookiecutter.repo_name}}.

{%- if cookiecutter.vcs_platform == "github" %}
If you're looking for the latest docs/builds, see our [Releases Page](https://github.com/{{cookiecutter.vcs_owner}}/{{cookiecutter.repo_name}}/releases).
{%- else %}
If you're looking for the latest docs/builds, see our [Releases Page]({{cookiecutter.gitea_url}}/{{cookiecutter.vcs_owner}}/{{cookiecutter.repo_name}}/releases).
{%- endif %}

# Getting Started

First, clone this repo (and optionally checkout a branch)

```shell
{%- if cookiecutter.vcs_platform == "github" %}
git clone https://github.com/{{cookiecutter.vcs_owner}}/{{cookiecutter.repo_name}}.git
{%- else %}
git clone {{cookiecutter.gitea_url}}/{{cookiecutter.vcs_owner}}/{{cookiecutter.repo_name}}.git
{%- endif %}
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

If you want to use this project template for yourself, you can find it [here!](https://github.com/KenwoodFox/Project-Template)
