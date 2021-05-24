from cx_Freeze import *

includefiles = ['Apps.ico']
base = None
# if sys.platform == "win64":
#     base = "win64GUI"

shortcut_table = [
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",  # Directory
     "My Calculator",  # Name
     "TARGETDIR",  # component
     "[TARGETDIR]/smart_calculator.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     None,  # icon
     None,  # iconindex
     None,  # Showcmd
     "TARGETDIR"  # WkDir
     )
]
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above define table

bdist_msi_options = {'data': msi_data}
setup(
    version="0.5",
    description="My Calculator",
    author="Anas Chuadhry",
    name="My Calculator",
    options={'build_exe': {'include_files': includefiles}, "bdist_msi": bdist_msi_options, },
    executables=[
        Executable(
            script="smart_calculator.py",
            base=base,
            icon='Apps.ico'
        )
    ]
)
