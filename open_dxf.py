import FreeCAD as App
import Part
from freecad.macros import fast_dxf as dxf
import numpy as np

entries, results = dxf.prase('/home/lo/Schreibtisch/leparagliding_converter/lep-3d.dxf')
geometries = []
for ln in results:
    if hasattr(ln, 'is_line'):
        geometries.append(ln.toEdge())

comp = Part.Compound(geometries)
comp.scale(0.01)
comp.rotate(App.Vector(0,1,0), App.Vector(0, 1, 0), 180)
Part.show(comp)
