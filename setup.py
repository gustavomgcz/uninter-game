from cx_Freeze import setup, Executable

# Create the executable file for the game
executables = [Executable('main.py')]

setup(
    name='Halloween Flight',
    version='0.1',
    description='Halloween Flight app',
    options={'build_exe': {'packages': ['pygame']}},
    executables=executables
)
