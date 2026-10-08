"""Fail unless the wheel ships every assembly and the package metadata FreeCAD reads."""

import sys
import zipfile

WANT = [
    "proosaxy/package.xml",
    "proosaxy/pyproject.toml",
    "proosaxy/src/freecad/component-assembly/MAIN.FCStd",
    "proosaxy/src/freecad/component-assembly/frame-assembly.FCStd",
    "proosaxy/src/freecad/component-assembly/toolhead-assembly.FCStd",
    "proosaxy/src/freecad/component-assembly/z-shaft-assembly.FCStd",
    "proosaxy/doc/frame/frame-drawing.FCStd",
]

(wheel,) = sys.argv[1:]
names = set(zipfile.ZipFile(wheel).namelist())
missing = [w for w in WANT if w not in names]
parts = sum(1 for n in names if n.startswith("proosaxy/src/freecad/") and n.endswith(".FCStd"))
print(f"{wheel}: {len(names)} files, {parts} documents")
if missing or parts == 0:
    sys.exit(f"missing from the wheel: {missing or 'src/freecad/**/*.FCStd'}")
