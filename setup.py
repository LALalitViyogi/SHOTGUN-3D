import sys
import os 
import cx_Freeze
base = None
if sys.platform == 'win32':
   base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Ad James John\AppData\Local\Programs\Python\Python310\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Ad James John\AppData\Local\Programs\Python\Python310\tcl\tk8.6"

executables = [cx_Freeze.Executable("main.py", base=base, icon="icon.ico")]

cx_Freeze.setup(
   name = "ShotGun 3D",
   options = {
      "build_exe": 
      {
         "packages":
         [
            "pygame",
            "pygame_menu",
            "random",
            "os",
         ], 
         "include_files":
         [
            "icon.ico",
            'resources',
            'tcl86t.dll',
            'tcl86t.lib',
            'tk86t.lib',
            'tk86t.dll',
            'tkstub86.lib',
            'tclstub86.lib',
            'map.py',
            'menu.py',
            'new_credits.py',
            'npc.py',
            'object_handler.py',
            'object_renderer.py',
            'pathfinding.py',
            'player.py',
            'raycasting.py',
            'settings.py',
            'sound.py',
            'sprite_object.py',
            'weapon.py',

         ]
      }
   },
 version = "1.1021",
 description = "Tkinter Application",
 executables = executables
)