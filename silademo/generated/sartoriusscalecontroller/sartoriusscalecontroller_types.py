# Generated by sila2.code_generator; sila2.__version__: 0.12.2
from __future__ import annotations

from typing import NamedTuple


class Tare_Responses(NamedTuple):

    Success: bool
    """
    Boolean indicating if the tare operation was successful.
    """


class Zero_Responses(NamedTuple):

    Success: bool
    """
    Boolean indicating if the zero operation was successful.
    """


class Connect_Responses(NamedTuple):

    Connected: bool
    """
    Boolean indicating if the connection was successful.
    """


class MeasureWeight_Responses(NamedTuple):

    Weight: float
    """
    The current weight measurement from the scale.
    """
