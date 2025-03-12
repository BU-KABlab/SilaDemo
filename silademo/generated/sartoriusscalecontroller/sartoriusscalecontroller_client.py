# Generated by sila2.code_generator; sila2.__version__: 0.12.2
# -----
# This class does not do anything useful at runtime. Its only purpose is to provide type annotations.
# Since sphinx does not support .pyi files (yet?), this is a .py file.
# -----

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:

    from typing import Iterable, Optional

    from sartoriusscalecontroller_types import (
        Connect_Responses,
        MeasureWeight_Responses,
        Tare_Responses,
        Zero_Responses,
    )
    from sila2.client import (
        ClientMetadataInstance,
        ClientObservableCommandInstance,
        ClientObservableProperty,
        ClientUnobservableProperty,
    )


class SartoriusScaleControllerClient:
    """
    Provides control and measurement capabilities for Sartorius laboratory scales through the sartorius Python library.
    """

    ScaleInformation: ClientUnobservableProperty[str]
    """
    Information about the connected Sartorius scale model, serial number, and firmware version.
    """

    Unit: ClientObservableProperty[str]
    """
    The current measurement unit of the scale (e.g., g, kg, mg).
    """

    ConnectionStatus: ClientObservableProperty[bool]
    """
    The current connection status of the Sartorius scale.
    """

    StableReading: ClientObservableProperty[bool]
    """
    Indicates whether the current weight reading is stable.
    """

    def Tare(self, *, metadata: Optional[Iterable[ClientMetadataInstance]] = None) -> Tare_Responses:
        """
        Tares the scale (sets the current weight reading to zero).
        """
        ...

    def Zero(self, *, metadata: Optional[Iterable[ClientMetadataInstance]] = None) -> Zero_Responses:
        """
        Zeros the scale (calibrates to absolute zero).
        """
        ...

    def Connect(self, Port: str, *, metadata: Optional[Iterable[ClientMetadataInstance]] = None) -> Connect_Responses:
        """
        Establishes a connection to the Sartorius scale with the specified port.
        """
        ...

    def MeasureWeight(
        self, *, metadata: Optional[Iterable[ClientMetadataInstance]] = None
    ) -> ClientObservableCommandInstance[MeasureWeight_Responses]:
        """
        Returns the current weight reading from the connected Sartorius scale.
        """
        ...
