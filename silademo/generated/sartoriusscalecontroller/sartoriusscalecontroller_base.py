# Generated by sila2.code_generator; sila2.__version__: 0.12.2
from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import timedelta
from queue import Queue
from typing import TYPE_CHECKING, Optional, Union

from sila2.server import FeatureImplementationBase, MetadataDict, ObservableCommandInstance

from .sartoriusscalecontroller_types import Connect_Responses, MeasureWeight_Responses, Tare_Responses, Zero_Responses

if TYPE_CHECKING:

    from ...server import Server


class SartoriusScaleControllerBase(FeatureImplementationBase, ABC):
    parent_server: Server

    _Unit_producer_queue: Queue[Union[str, Exception]]
    _Unit_current_value: str

    _ConnectionStatus_producer_queue: Queue[Union[bool, Exception]]
    _ConnectionStatus_current_value: bool

    _StableReading_producer_queue: Queue[Union[bool, Exception]]
    _StableReading_current_value: bool

    MeasureWeight_default_lifetime_of_execution: Optional[timedelta]

    def __init__(self, parent_server: Server):
        """
        Provides control and measurement capabilities for Sartorius laboratory scales through the sartorius Python library.
        """
        super().__init__(parent_server=parent_server)

        self._Unit_producer_queue = Queue()

        self._ConnectionStatus_producer_queue = Queue()

        self._StableReading_producer_queue = Queue()

        self.MeasureWeight_default_lifetime_of_execution = None

    @abstractmethod
    def get_ScaleInformation(self, *, metadata: MetadataDict) -> str:
        """
        Information about the connected Sartorius scale model, serial number, and firmware version.

        :param metadata: The SiLA Client Metadata attached to the call
        :return: Information about the connected Sartorius scale model, serial number, and firmware version.
        """

    def update_Unit(self, Unit: str, queue: Optional[Queue[str]] = None) -> None:
        """
        The current measurement unit of the scale (e.g., g, kg, mg).

        This method updates the observable property 'Unit'.

        :param queue: The queue to send updates to. If None, the default Queue will be used.
        """
        if queue is None:
            queue = self._Unit_producer_queue
            self._Unit_current_value = Unit
        queue.put(Unit)

    def Unit_on_subscription(self, *, metadata: MetadataDict) -> Optional[Queue[str]]:
        """
        The current measurement unit of the scale (e.g., g, kg, mg).

        This method is called when a client subscribes to the observable property 'Unit'

        :param metadata: The SiLA Client Metadata attached to the call
        :return: Optional `Queue` that should be used for updating this property.
            If None, the default Queue will be used.
        """

    def abort_Unit_subscriptions(self, error: Exception, queue: Optional[Queue[str]] = None) -> None:
        """
        The current measurement unit of the scale (e.g., g, kg, mg).

        This method aborts subscriptions to the observable property 'Unit'.

        :param error: The Exception to be sent to the subscribing client.
            If it is no DefinedExecutionError or UndefinedExecutionError, it will be wrapped in an UndefinedExecutionError.
        :param queue: The queue to abort. If None, the default Queue will be used.
        """
        if queue is None:
            queue = self._Unit_producer_queue
        queue.put(error)

    @property
    def current_Unit(self) -> str:
        try:
            return self._Unit_current_value
        except AttributeError:
            raise AttributeError("Observable property Unit has never been set")

    def update_ConnectionStatus(self, ConnectionStatus: bool, queue: Optional[Queue[bool]] = None) -> None:
        """
        The current connection status of the Sartorius scale.

        This method updates the observable property 'ConnectionStatus'.

        :param queue: The queue to send updates to. If None, the default Queue will be used.
        """
        if queue is None:
            queue = self._ConnectionStatus_producer_queue
            self._ConnectionStatus_current_value = ConnectionStatus
        queue.put(ConnectionStatus)

    def ConnectionStatus_on_subscription(self, *, metadata: MetadataDict) -> Optional[Queue[bool]]:
        """
        The current connection status of the Sartorius scale.

        This method is called when a client subscribes to the observable property 'ConnectionStatus'

        :param metadata: The SiLA Client Metadata attached to the call
        :return: Optional `Queue` that should be used for updating this property.
            If None, the default Queue will be used.
        """

    def abort_ConnectionStatus_subscriptions(self, error: Exception, queue: Optional[Queue[bool]] = None) -> None:
        """
        The current connection status of the Sartorius scale.

        This method aborts subscriptions to the observable property 'ConnectionStatus'.

        :param error: The Exception to be sent to the subscribing client.
            If it is no DefinedExecutionError or UndefinedExecutionError, it will be wrapped in an UndefinedExecutionError.
        :param queue: The queue to abort. If None, the default Queue will be used.
        """
        if queue is None:
            queue = self._ConnectionStatus_producer_queue
        queue.put(error)

    @property
    def current_ConnectionStatus(self) -> bool:
        try:
            return self._ConnectionStatus_current_value
        except AttributeError:
            raise AttributeError("Observable property ConnectionStatus has never been set")

    def update_StableReading(self, StableReading: bool, queue: Optional[Queue[bool]] = None) -> None:
        """
        Indicates whether the current weight reading is stable.

        This method updates the observable property 'StableReading'.

        :param queue: The queue to send updates to. If None, the default Queue will be used.
        """
        if queue is None:
            queue = self._StableReading_producer_queue
            self._StableReading_current_value = StableReading
        queue.put(StableReading)

    def StableReading_on_subscription(self, *, metadata: MetadataDict) -> Optional[Queue[bool]]:
        """
        Indicates whether the current weight reading is stable.

        This method is called when a client subscribes to the observable property 'StableReading'

        :param metadata: The SiLA Client Metadata attached to the call
        :return: Optional `Queue` that should be used for updating this property.
            If None, the default Queue will be used.
        """

    def abort_StableReading_subscriptions(self, error: Exception, queue: Optional[Queue[bool]] = None) -> None:
        """
        Indicates whether the current weight reading is stable.

        This method aborts subscriptions to the observable property 'StableReading'.

        :param error: The Exception to be sent to the subscribing client.
            If it is no DefinedExecutionError or UndefinedExecutionError, it will be wrapped in an UndefinedExecutionError.
        :param queue: The queue to abort. If None, the default Queue will be used.
        """
        if queue is None:
            queue = self._StableReading_producer_queue
        queue.put(error)

    @property
    def current_StableReading(self) -> bool:
        try:
            return self._StableReading_current_value
        except AttributeError:
            raise AttributeError("Observable property StableReading has never been set")

    @abstractmethod
    def Tare(self, *, metadata: MetadataDict) -> Tare_Responses:
        """
        Tares the scale (sets the current weight reading to zero).


        :param metadata: The SiLA Client Metadata attached to the call

        :return:

            - Success: Boolean indicating if the tare operation was successful.


        """

    @abstractmethod
    def Zero(self, *, metadata: MetadataDict) -> Zero_Responses:
        """
        Zeros the scale (calibrates to absolute zero).


        :param metadata: The SiLA Client Metadata attached to the call

        :return:

            - Success: Boolean indicating if the zero operation was successful.


        """

    @abstractmethod
    def Connect(self, Port: str, *, metadata: MetadataDict) -> Connect_Responses:
        """
        Establishes a connection to the Sartorius scale with the specified port.


        :param Port: The serial port or device address for the scale connection.

        :param metadata: The SiLA Client Metadata attached to the call

        :return:

            - Connected: Boolean indicating if the connection was successful.


        """

    @abstractmethod
    def MeasureWeight(self, *, metadata: MetadataDict, instance: ObservableCommandInstance) -> MeasureWeight_Responses:
        """
        Returns the current weight reading from the connected Sartorius scale.


        :param metadata: The SiLA Client Metadata attached to the call
        :param instance: The command instance, enabling sending status updates to subscribed clients

        :return:

            - Weight: The current weight measurement from the scale.


        """
