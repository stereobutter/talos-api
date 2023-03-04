# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: resource/resource.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime
from typing import (
    TYPE_CHECKING,
    AsyncIterator,
    Dict,
    List,
    Optional,
)

import betterproto
import grpclib
from betterproto.grpc.grpclib_server import ServiceBase

from .. import common as _common__


if TYPE_CHECKING:
    import grpclib.server
    from betterproto.grpc.grpclib_client import MetadataLike
    from grpclib.metadata import Deadline


class EventType(betterproto.Enum):
    CREATED = 0
    UPDATED = 1
    DESTROYED = 2


@dataclass(eq=False, repr=False)
class Resource(betterproto.Message):
    metadata: "Metadata" = betterproto.message_field(1)
    spec: "Spec" = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class Metadata(betterproto.Message):
    namespace: str = betterproto.string_field(1)
    type: str = betterproto.string_field(2)
    id: str = betterproto.string_field(3)
    version: str = betterproto.string_field(4)
    owner: str = betterproto.string_field(7)
    phase: str = betterproto.string_field(5)
    created: datetime = betterproto.message_field(8)
    updated: datetime = betterproto.message_field(9)
    finalizers: List[str] = betterproto.string_field(6)
    labels: Dict[str, str] = betterproto.map_field(
        10, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )


@dataclass(eq=False, repr=False)
class Spec(betterproto.Message):
    yaml: bytes = betterproto.bytes_field(1)


@dataclass(eq=False, repr=False)
class GetRequest(betterproto.Message):
    """rpc Get"""

    namespace: str = betterproto.string_field(1)
    type: str = betterproto.string_field(2)
    id: str = betterproto.string_field(3)


@dataclass(eq=False, repr=False)
class Get(betterproto.Message):
    """The GetResponse message contains the Resource returned."""

    metadata: "_common__.Metadata" = betterproto.message_field(1)
    definition: "Resource" = betterproto.message_field(2)
    resource: "Resource" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class GetResponse(betterproto.Message):
    messages: List["Get"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class ListRequest(betterproto.Message):
    """rpc List The ListResponse message contains the Resource returned."""

    namespace: str = betterproto.string_field(1)
    type: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ListResponse(betterproto.Message):
    metadata: "_common__.Metadata" = betterproto.message_field(1)
    definition: "Resource" = betterproto.message_field(2)
    resource: "Resource" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class WatchRequest(betterproto.Message):
    """rpc Watch The WatchResponse message contains the Resource returned."""

    namespace: str = betterproto.string_field(1)
    type: str = betterproto.string_field(2)
    id: str = betterproto.string_field(3)
    tail_events: int = betterproto.uint32_field(4)


@dataclass(eq=False, repr=False)
class WatchResponse(betterproto.Message):
    metadata: "_common__.Metadata" = betterproto.message_field(1)
    event_type: "EventType" = betterproto.enum_field(2)
    definition: "Resource" = betterproto.message_field(3)
    resource: "Resource" = betterproto.message_field(4)


class ResourceServiceStub(betterproto.ServiceStub):
    async def get(
        self,
        get_request: "GetRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> "GetResponse":
        return await self._unary_unary(
            "/resource.ResourceService/Get",
            get_request,
            GetResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        )

    async def list(
        self,
        list_request: "ListRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> AsyncIterator["ListResponse"]:
        async for response in self._unary_stream(
            "/resource.ResourceService/List",
            list_request,
            ListResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response

    async def watch(
        self,
        watch_request: "WatchRequest",
        *,
        timeout: Optional[float] = None,
        deadline: Optional["Deadline"] = None,
        metadata: Optional["MetadataLike"] = None
    ) -> AsyncIterator["WatchResponse"]:
        async for response in self._unary_stream(
            "/resource.ResourceService/Watch",
            watch_request,
            WatchResponse,
            timeout=timeout,
            deadline=deadline,
            metadata=metadata,
        ):
            yield response


class ResourceServiceBase(ServiceBase):
    async def get(self, get_request: "GetRequest") -> "GetResponse":
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def list(self, list_request: "ListRequest") -> AsyncIterator["ListResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def watch(
        self, watch_request: "WatchRequest"
    ) -> AsyncIterator["WatchResponse"]:
        raise grpclib.GRPCError(grpclib.const.Status.UNIMPLEMENTED)

    async def __rpc_get(
        self, stream: "grpclib.server.Stream[GetRequest, GetResponse]"
    ) -> None:
        request = await stream.recv_message()
        response = await self.get(request)
        await stream.send_message(response)

    async def __rpc_list(
        self, stream: "grpclib.server.Stream[ListRequest, ListResponse]"
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.list,
            stream,
            request,
        )

    async def __rpc_watch(
        self, stream: "grpclib.server.Stream[WatchRequest, WatchResponse]"
    ) -> None:
        request = await stream.recv_message()
        await self._call_rpc_handler_server_stream(
            self.watch,
            stream,
            request,
        )

    def __mapping__(self) -> Dict[str, grpclib.const.Handler]:
        return {
            "/resource.ResourceService/Get": grpclib.const.Handler(
                self.__rpc_get,
                grpclib.const.Cardinality.UNARY_UNARY,
                GetRequest,
                GetResponse,
            ),
            "/resource.ResourceService/List": grpclib.const.Handler(
                self.__rpc_list,
                grpclib.const.Cardinality.UNARY_STREAM,
                ListRequest,
                ListResponse,
            ),
            "/resource.ResourceService/Watch": grpclib.const.Handler(
                self.__rpc_watch,
                grpclib.const.Cardinality.UNARY_STREAM,
                WatchRequest,
                WatchResponse,
            ),
        }
