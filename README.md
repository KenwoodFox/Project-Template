# KenwoodFox's Cookie Cutter Project Template

I very often find myself using or suggesting this project layout, so I've gone ahead and cookie-cuttered
it so everyone else can use it too!


## Using this template.

Its as easy as

```shell
$ cookiecutter https://github.com/KenwoodFox/Project-Template
```

If you dont have cookie-cutter, install it from [here](https://cookiecutter.readthedocs.io/en/stable/installation.html)!


## Whats in this template?

```
.
└── YourProject
    ├── CAD                                 # CAD Files, 3D objects (cases, brackets, big things)
    ├── Docs                                # Documentation (setup by default with Sphinx)
    ├── Firmware                            # Firmware (setup by default with PIO)
    │   ├── include                         # Include files like pindefs and headers
    │   ├── lib                             # Custom lib files like project objects and memory
    │   ├── src                             # Source code files
    │   └── test                            # PIO Tests
    ├── Hardware                            # Hardware (setup by default with KiCAD and KiBOT)
    │   └── YourProject                     # KiCAD project with the same name
    │       ├── Libraries                   # External KiCAD libs!
    │       └── Stencils                    # Stencils and jigs
    └── Static                              # Pictures and Docs
```

