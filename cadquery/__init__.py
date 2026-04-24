"""CadQuery - A parametric 3D CAD scripting framework.

CadQuery is an intuitive, easy-to-use Python module for building parametric
3D CAD models. It is inspired by OpenSCAD but uses Python instead of a
domain-specific language.

Example usage::

    import cadquery as cq

    result = cq.Workplane("XY").box(1, 2, 3)

Note: This is a personal fork used for learning and experimentation.
Upstream project: https://github.com/CadQuery/cadquery
"""

from .cq import (
    CQContext,
    CQObject,
    Workplane,
)
from .assembly import (
    Assembly,
    Color,
    Constraint,
)
from .occ_impl.geom import (
    BoundBox,
    Location,
    Matrix,
    Plane,
    Vector,
)
from .occ_impl.shapes import (
    compound,
    Compound,
    Edge,
    Face,
    Shell,
    Solid,
    Shape,
    Vertex,
    Wire,
)
from .occ_impl.exporters import (
    exporters,
)
from .selectors import (
    AndSelector,
    AreaNthSelector,
    BaseDirSelector,
    BinarySelector,
    BoxSelector,
    CenterNthSelector,
    DirectionMinMaxSelector,
    DirectionNthSelector,
    DirectionSelector,
    EdgeLengthSelector,
    FaceAreaSelector,
    InverseSelector,
    LengthNthSelector,
    NearestToPointSelector,
    OrSelector,
    ParallelDirSelector,
    PerpendicularDirSelector,
    RadiusNthSelector,
    StringSyntaxSelector,
    SubtractSelector,
    SumSelector,
    TypeSelector,
)
from .sketch import Sketch

__version__ = "2.4.0"

__all__ = [
    # Core workplane
    "CQContext",
    "CQObject",
    "Workplane",
    # Assembly
    "Assembly",
    "Color",
    "Constraint",
    # Geometry
    "BoundBox",
    "Location",
    "Matrix",
    "Plane",
    "Vector",
    # Shapes
    "compound",
    "Compound",
    "Edge",
    "Face",
    "Shell",
    "Solid",
    "Shape",
    "Vertex",
    "Wire",
    # Exporters
    "exporters",
    # Selectors
    "AndSelector",
    "AreaNthSelector",
    "BaseDirSelector",
    "BinarySelector",
    "BoxSelector",
    "CenterNthSelector",
    "DirectionMinMaxSelector",
    "DirectionNthSelector",
    "DirectionSelector",
    "EdgeLengthSelector",
    "FaceAreaSelector",
    "InverseSelector",
    "LengthNthSelector",
    "NearestToPointSelector",
    "OrSelector",
    "ParallelDirSelector",
    "PerpendicularDirSelector",
    "RadiusNthSelector",
    "StringSyntaxSelector",
    "SubtractSelector",
    "SumSelector",
    "TypeSelector",
    # Sketch
    "Sketch",
    # Version
    "__version__",
]
