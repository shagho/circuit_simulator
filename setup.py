from cx_Freeze import setup, Executable

base = None    

executables = [Executable("Circuit_Viewer.py", base=base)]

packages = ["idna","pygame","matplotlib","numpy","math","matplotlib.pyplot","copy","Analyze","Buttons","enum","sys","struct","importlib","time","pygame.locals","eztext"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Circuit simulator",
    options = options,
    version = "1.0",
    description = 'a program for circuit simulation with Navid Shaghozahi license ',
    executables = executables
)
