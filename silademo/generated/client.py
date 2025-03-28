# Generated by sila2.code_generator; sila2.__version__: 0.12.2
from __future__ import annotations

from typing import Set

from sila2.client import SilaClient
from sila2.framework import FullyQualifiedFeatureIdentifier

from . import greetingprovider, sartoriusscalecontroller


class Client(SilaClient):

    GreetingProvider: greetingprovider.GreetingProviderClient

    SartoriusScaleController: sartoriusscalecontroller.SartoriusScaleControllerClient

    _expected_features: Set[FullyQualifiedFeatureIdentifier] = {
        FullyQualifiedFeatureIdentifier("org.silastandard/core/SiLAService/v1"),
        FullyQualifiedFeatureIdentifier("org.silastandard/examples/GreetingProvider/v1"),
        FullyQualifiedFeatureIdentifier("org.sartorius/laboratory.devices.scales/SartoriusScaleController/v1"),
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
