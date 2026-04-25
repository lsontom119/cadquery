"""Geometry utilities for CadQuery.

This module provides core geometric primitives and transformations
used throughout the CadQuery modeling pipeline.
"""

from typing import Optional, Tuple, Union
import math

from OCC.Core.gp import (
    gp_Vec,
    gp_Pnt,
    gp_Dir,
    gp_Ax1,
    gp_Ax2,
    gp_Ax3,
    gp_Trsf,
    gp_GTrsf,
    gp_XYZ,
)
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform

DEFAULT_TOLERANCE = 1e-6


class Vector:
    """Represents a 3D vector or point in space.

    Wraps the OCC gp_Vec and gp_Pnt types, providing a unified
    interface for geometric operations.
    """

    def __init__(
        self,
        x: Union[float, gp_Vec, gp_Pnt, gp_XYZ, Tuple] = 0,
        y: float = 0,
        z: float = 0,
    ):
        if isinstance(x, gp_Vec):
            self._v = x
        elif isinstance(x, gp_Pnt):
            self._v = gp_Vec(x.X(), x.Y(), x.Z())
        elif isinstance(x, gp_XYZ):
            self._v = gp_Vec(x.X(), x.Y(), x.Z())
        elif isinstance(x, (list, tuple)):
            self._v = gp_Vec(*x)
        else:
            self._v = gp_Vec(x, y, z)

    @property
    def x(self) -> float:
        return self._v.X()

    @property
    def y(self) -> float:
        return self._v.Y()

    @property
    def z(self) -> float:
        return self._v.Z()

    def to_pnt(self) -> gp_Pnt:
        """Convert to an OCC point."""
        return gp_Pnt(self._v.X(), self._v.Y(), self._v.Z())

    def to_dir(self) -> gp_Dir:
        """Convert to an OCC direction (normalized)."""
        return gp_Dir(self._v)

    def length(self) -> float:
        """Return the magnitude of the vector."""
        return self._v.Magnitude()

    def normalized(self) -> "Vector":
        """Return a unit vector in the same direction."""
        mag = self.length()
        if mag < DEFAULT_TOLERANCE:
            raise ValueError("Cannot normalize a zero-length vector")
        return Vector(self._v.Normalized())

    def dot(self, other: "Vector") -> float:
        """Compute the dot product with another vector."""
        return self._v.Dot(other._v)

    def cross(self, other: "Vector") -> "Vector":
        """Compute the cross product with another vector."""
        return Vector(self._v.Crossed(other._v))

    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self._v.Added(other._v))

    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self._v.Subtracted(other._v))

    def __mul__(self, scalar: float) -> "Vector":
        return Vector(self._v.Multiplied(scalar))

    def __rmul__(self, scalar: float) -> "Vector":
        return self.__mul__(scalar)

    def __neg__(self) -> "Vector":
        return Vector(self._v.Reversed())

    def __repr__(self) -> str:
        return f"Vector({self.x:.6g}, {self.y:.6g}, {self.z:.6g})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return (
            abs(self.x - other.x) < DEFAULT_TOLERANCE
            and abs(self.y - other.y) < DEFAULT_TOLERANCE
            and abs(self.z - other.z) < DEFAULT_TOLERANCE
        )


class Plane:
    """Represents an infinite 2D plane in 3D space.

    Defined by an origin point and a normal vector. Provides
    coordinate system transformations between world and local space.
    """

    XY = None  # initialized below
    YZ = None
    ZX = None

    def __init__(self, origin: Vector, normal: Vector):
        self.origin = origin
        self.normal = normal.normalized()

    @classmethod
    def named(cls, name: str) -> "Plane":
        """Create a standard named plane."""
        planes = {
            "XY": cls(Vector(0, 0, 0), Vector(0, 0, 1)),
            "YZ": cls(Vector(0, 0, 0), Vector(1, 0, 0)),
            "ZX": cls(Vector(0, 0, 0), Vector(0, 1, 0)),
            "front": cls(Vector(0, 0, 0), Vector(0, -1, 0)),
            "back": cls(Vector(0, 0, 0), Vector(0, 1, 0)),
            "left": cls(Vector(0, 0, 0), Vector(-1, 0, 0)),
            "right": cls(Vector(0, 0, 0), Vector(1, 0, 0)),
            "top": cls(Vector(0, 0, 0), Vector(0, 0, 1)),
            "bottom": cls(Vector(0, 0, 0), Vector(0, 0, -1)),
        }
        if name not in planes:
            raise ValueError(f"Unknown plane name '{name}'. Choose from: {list(planes)}")
        return planes[name]

    def __repr__(self) -> str:
        return f"Plane(origin={self.origin}, normal={self.normal})"
