"""
Contrib part of the library'
"""
from __future__ import annotations
import g2o.g2o
__all__ = ['SmoothEstimatePropagator']
class SmoothEstimatePropagator(g2o.g2o.EstimatePropagator):
    def __init__(self, g: g2o.g2o.SparseOptimizer, maxDistance: float = 1.7976931348623157e+308, maxEdgeCost: float = 1.7976931348623157e+308) -> None:
        ...
    def propagate(self, v: g2o.g2o.OptimizableGraph_Vertex) -> None:
        ...
