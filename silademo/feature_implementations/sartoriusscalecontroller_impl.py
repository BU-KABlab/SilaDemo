# Generated by sila2.code_generator; sila2.__version__: 0.12.2
from __future__ import annotations

from datetime import timedelta
from typing import TYPE_CHECKING

from sila2.server import MetadataDict, ObservableCommandInstance

from ..generated.sartoriusscalecontroller import (
    Connect_Responses,
    MeasureWeight_Responses,
    SartoriusScaleControllerBase,
    Tare_Responses,
    Zero_Responses,
)

if TYPE_CHECKING:
    from ..server import Server


class SartoriusScaleControllerImpl(SartoriusScaleControllerBase):
    def __init__(self, parent_server: Server) -> None:
        super().__init__(parent_server=parent_server)

        # Default lifetime of observable command instances. Possible values:
        # None: Command instance is valid and stored in memory until server shutdown
        # datetime.timedelta: Command instance is deleted after this duration, can be increased during command runtime
        self.MeasureWeight_default_lifetime_of_execution = timedelta(minutes=30)

    def get_ScaleInformation(self, *, metadata: MetadataDict) -> str:
        raise NotImplementedError  # TODO

    def Tare(self, *, metadata: MetadataDict) -> Tare_Responses:
        raise NotImplementedError  # TODO

    def Zero(self, *, metadata: MetadataDict) -> Zero_Responses:
        raise NotImplementedError  # TODO

    def Connect(self, Port: str, *, metadata: MetadataDict) -> Connect_Responses:
        raise NotImplementedError  # TODO

    def MeasureWeight(self, *, metadata: MetadataDict, instance: ObservableCommandInstance) -> MeasureWeight_Responses:
        # set execution status from `waiting` to `running`
        instance.begin_execution()

        raise NotImplementedError  # TODO
