# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: resource/definitions/etcd/etcd.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import (
    Dict,
    List,
)

import betterproto

from ..... import common as ____common__


@dataclass(eq=False, repr=False)
class ConfigSpec(betterproto.Message):
    """ConfigSpec describes (some) configuration settings of etcd."""

    advertise_valid_subnets: List[str] = betterproto.string_field(1)
    advertise_exclude_subnets: List[str] = betterproto.string_field(2)
    image: str = betterproto.string_field(3)
    extra_args: Dict[str, str] = betterproto.map_field(
        4, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )
    listen_valid_subnets: List[str] = betterproto.string_field(5)
    listen_exclude_subnets: List[str] = betterproto.string_field(6)


@dataclass(eq=False, repr=False)
class MemberSpec(betterproto.Message):
    """MemberSpec holds information about an etcd member."""

    member_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class PkiStatusSpec(betterproto.Message):
    """PKIStatusSpec describes status of rendered secrets."""

    ready: bool = betterproto.bool_field(1)
    version: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class SpecSpec(betterproto.Message):
    """SpecSpec describes (some) Specuration settings of etcd."""

    name: str = betterproto.string_field(1)
    advertised_addresses: List["____common__.NetIp"] = betterproto.message_field(2)
    image: str = betterproto.string_field(3)
    extra_args: Dict[str, str] = betterproto.map_field(
        4, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )
    listen_peer_addresses: List["____common__.NetIp"] = betterproto.message_field(5)
    listen_client_addresses: List["____common__.NetIp"] = betterproto.message_field(6)
