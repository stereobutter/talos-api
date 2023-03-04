# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: resource/definitions/runtime/runtime.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .. import enums as _enums__


@dataclass(eq=False, repr=False)
class KernelModuleSpecSpec(betterproto.Message):
    """KernelModuleSpecSpec describes Linux kernel module to load."""

    name: str = betterproto.string_field(1)
    parameters: List[str] = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class KernelParamSpecSpec(betterproto.Message):
    """KernelParamSpecSpec describes status of the defined sysctls."""

    value: str = betterproto.string_field(1)
    ignore_errors: bool = betterproto.bool_field(2)


@dataclass(eq=False, repr=False)
class KernelParamStatusSpec(betterproto.Message):
    """KernelParamStatusSpec describes status of the defined sysctls."""

    current: str = betterproto.string_field(1)
    default: str = betterproto.string_field(2)
    unsupported: bool = betterproto.bool_field(3)


@dataclass(eq=False, repr=False)
class MachineStatusSpec(betterproto.Message):
    """MachineStatusSpec describes status of the defined sysctls."""

    stage: "_enums__.RuntimeMachineStage" = betterproto.enum_field(1)
    status: "MachineStatusStatus" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class MachineStatusStatus(betterproto.Message):
    """MachineStatusStatus describes machine current status at the stage."""

    ready: bool = betterproto.bool_field(1)
    unmet_conditions: List["UnmetCondition"] = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class MountStatusSpec(betterproto.Message):
    """MountStatusSpec describes status of the defined sysctls."""

    source: str = betterproto.string_field(1)
    target: str = betterproto.string_field(2)
    filesystem_type: str = betterproto.string_field(3)
    options: List[str] = betterproto.string_field(4)


@dataclass(eq=False, repr=False)
class PlatformMetadataSpec(betterproto.Message):
    """PlatformMetadataSpec describes platform metadata properties."""

    platform: str = betterproto.string_field(1)
    hostname: str = betterproto.string_field(2)
    region: str = betterproto.string_field(3)
    zone: str = betterproto.string_field(4)
    instance_type: str = betterproto.string_field(5)
    instance_id: str = betterproto.string_field(6)
    provider_id: str = betterproto.string_field(7)
    spot: bool = betterproto.bool_field(8)


@dataclass(eq=False, repr=False)
class UnmetCondition(betterproto.Message):
    """
    UnmetCondition is a failure which prevents machine from being ready at the
    stage.
    """

    name: str = betterproto.string_field(1)
    reason: str = betterproto.string_field(2)
