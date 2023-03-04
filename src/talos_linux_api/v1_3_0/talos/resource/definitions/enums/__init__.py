# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: resource/definitions/enums/enums.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


class MachineType(betterproto.Enum):
    """MachineType represents a machine type."""

    TYPE_UNKNOWN = 0
    """
    TypeUnknown represents undefined node type, when there is no machine
    configuration yet.
    """

    TYPE_INIT = 1
    """
    TypeInit type designates the first control plane node to come up. You can
    think of it like a bootstrap node. This node will perform the initial steps
    to bootstrap the cluster -- generation of TLS assets, starting of the
    control plane, etc.
    """

    TYPE_CONTROL_PLANE = 2
    """
    TypeControlPlane designates the node as a control plane member. This means
    it will host etcd along with the Kubernetes controlplane components such as
    API Server, Controller Manager, Scheduler.
    """

    TYPE_WORKER = 3
    """
    TypeWorker designates the node as a worker node. This means it will be an
    available compute node for scheduling workloads.
    """


class KubespanPeerState(betterproto.Enum):
    """KubespanPeerState is KubeSpan peer current state."""

    PEER_STATE_UNKNOWN = 0
    PEER_STATE_UP = 1
    PEER_STATE_DOWN = 2


class NetworkConfigLayer(betterproto.Enum):
    """
    NetworkConfigLayer describes network configuration layers, with lowest
    priority first.
    """

    CONFIG_DEFAULT = 0
    CONFIG_CMDLINE = 1
    CONFIG_PLATFORM = 2
    CONFIG_OPERATOR = 3
    CONFIG_MACHINE_CONFIGURATION = 4


class NetworkOperator(betterproto.Enum):
    """NetworkOperator enumerates Talos network operators."""

    OPERATOR_DHCP_4 = 0
    OPERATOR_DHCP_6 = 1
    OPERATOR_VIP = 2


class NethelpersFamily(betterproto.Enum):
    """NethelpersFamily is a network family."""

    FAMILY_INET_4 = 0
    FAMILY_INET_6 = 1


class NethelpersScope(betterproto.Enum):
    """NethelpersScope is an address scope."""

    SCOPE_GLOBAL = 0
    SCOPE_SITE = 200
    SCOPE_LINK = 253
    SCOPE_HOST = 254
    SCOPE_NOWHERE = 255


class NethelpersAdSelect(betterproto.Enum):
    """NethelpersADSelect is ADSelect."""

    AD_SELECT_STABLE = 0
    AD_SELECT_BANDWIDTH = 1
    AD_SELECT_COUNT = 2


class NethelpersArpAllTargets(betterproto.Enum):
    """NethelpersARPAllTargets is an ARP targets mode."""

    ARP_ALL_TARGETS_ANY = 0
    ARP_ALL_TARGETS_ALL = 1


class NethelpersArpValidate(betterproto.Enum):
    """NethelpersARPValidate is an ARP Validation mode."""

    ARP_VALIDATE_NONE = 0
    ARP_VALIDATE_ACTIVE = 1
    ARP_VALIDATE_BACKUP = 2
    ARP_VALIDATE_ALL = 3


class NethelpersFailOverMac(betterproto.Enum):
    """NethelpersFailOverMAC is a MAC failover mode."""

    FAIL_OVER_MAC_NONE = 0
    FAIL_OVER_MAC_ACTIVE = 1
    FAIL_OVER_MAC_FOLLOW = 2


class NethelpersBondXmitHashPolicy(betterproto.Enum):
    """NethelpersBondXmitHashPolicy is a bond hash policy."""

    BOND_XMIT_POLICY_LAYER2 = 0
    """layer2"""

    BOND_XMIT_POLICY_LAYER34 = 1
    """layer3+4"""

    BOND_XMIT_POLICY_LAYER23 = 2
    """layer2+3"""

    BOND_XMIT_POLICY_ENCAP23 = 3
    """encap2+3"""

    BOND_XMIT_POLICY_ENCAP34 = 4
    """encap3+4"""


class NethelpersLacpRate(betterproto.Enum):
    """NethelpersLACPRate is a LACP rate."""

    LACP_RATE_SLOW = 0
    LACP_RATE_FAST = 1


class NethelpersBondMode(betterproto.Enum):
    """NethelpersBondMode is a bond mode."""

    BOND_MODE_ROUNDROBIN = 0
    BOND_MODE_ACTIVE_BACKUP = 1
    BOND_MODE_XOR = 2
    BOND_MODE_BROADCAST = 3
    BOND_MODE8023_AD = 4
    BOND_MODE_TLB = 5
    BOND_MODE_ALB = 6


class NethelpersPrimaryReselect(betterproto.Enum):
    """NethelpersPrimaryReselect is an ARP targets mode."""

    PRIMARY_RESELECT_ALWAYS = 0
    PRIMARY_RESELECT_BETTER = 1
    PRIMARY_RESELECT_FAILURE = 2


class NethelpersLinkType(betterproto.Enum):
    """NethelpersLinkType is a link type."""

    LINK_NETROM = 0
    LINK_ETHER = 1
    LINK_EETHER = 2
    LINK_AX25 = 3
    LINK_PRONET = 4
    LINK_CHAOS = 5
    LINK_IEE802 = 6
    LINK_ARCNET = 7
    LINK_ATALK = 8
    LINK_DLCI = 15
    LINK_ATM = 19
    LINK_METRICOM = 23
    LINK_IEEE1394 = 24
    LINK_EUI64 = 27
    LINK_INFINIBAND = 32
    LINK_SLIP = 256
    LINK_CSLIP = 257
    LINK_SLIP6 = 258
    LINK_CSLIP6 = 259
    LINK_RSRVD = 260
    LINK_ADAPT = 264
    LINK_ROSE = 270
    LINK_X25 = 271
    LINK_HWX25 = 272
    LINK_CAN = 280
    LINK_PPP = 512
    LINK_CISCO_HDLC = 513
    LINK_LAPB = 516
    LINK_DDCMP = 517
    LINK_RAWHDLC = 518
    LINK_TUNNEL = 768
    LINK_TUNNEL6 = 769
    LINK_FRAD = 770
    LINK_SKIP = 771
    LINK_LOOPBCK = 772
    LINK_LOCALTLK = 773
    LINK_FDDI = 774
    LINK_BIF = 775
    LINK_SIT = 776
    LINK_IPDDP = 777
    LINK_IPGRE = 778
    LINK_PIMREG = 779
    LINK_HIPPI = 780
    LINK_ASH = 781
    LINK_ECONET = 782
    LINK_IRDA = 783
    LINK_FCPP = 784
    LINK_FCAL = 785
    LINK_FCPL = 786
    LINK_FCFABRIC = 787
    LINK_FCFABRIC1 = 788
    LINK_FCFABRIC2 = 789
    LINK_FCFABRIC3 = 790
    LINK_FCFABRIC4 = 791
    LINK_FCFABRIC5 = 792
    LINK_FCFABRIC6 = 793
    LINK_FCFABRIC7 = 794
    LINK_FCFABRIC8 = 795
    LINK_FCFABRIC9 = 796
    LINK_FCFABRIC10 = 797
    LINK_FCFABRIC11 = 798
    LINK_FCFABRIC12 = 799
    LINK_IEE802_TR = 800
    LINK_IEE80211 = 801
    LINK_IEE80211_PRISM = 802
    LINK_IEE80211_RADIOTAP = 803
    LINK_IEE8021154 = 804
    LINK_IEE8021154_MONITOR = 805
    LINK_PHONET = 820
    LINK_PHONETPIPE = 821
    LINK_CAIF = 822
    LINK_IP6_GRE = 823
    LINK_NETLINK = 824
    LINK6_LOWPAN = 825
    LINK_VOID = 65535
    LINK_NONE = 65534


class NethelpersDuplex(betterproto.Enum):
    """NethelpersDuplex wraps ethtool.Duplex for YAML marshaling."""

    HALF = 0
    FULL = 1
    UNKNOWN = 255


class NethelpersOperationalState(betterproto.Enum):
    """
    NethelpersOperationalState wraps rtnetlink.OperationalState for YAML
    marshaling.
    """

    OPER_STATE_UNKNOWN = 0
    OPER_STATE_NOT_PRESENT = 1
    OPER_STATE_DOWN = 2
    OPER_STATE_LOWER_LAYER_DOWN = 3
    OPER_STATE_TESTING = 4
    OPER_STATE_DORMANT = 5
    OPER_STATE_UP = 6


class NethelpersPort(betterproto.Enum):
    """NethelpersPort wraps ethtool.Port for YAML marshaling."""

    TWISTED_PAIR = 0
    AUI = 1
    MII = 2
    FIBRE = 3
    BNC = 4
    DIRECT_ATTACH = 5
    NONE = 239
    OTHER = 255


class NethelpersRouteProtocol(betterproto.Enum):
    """NethelpersRouteProtocol is a routing protocol."""

    PROTOCOL_UNSPEC = 0
    PROTOCOL_REDIRECT = 1
    PROTOCOL_KERNEL = 2
    PROTOCOL_BOOT = 3
    PROTOCOL_STATIC = 4
    PROTOCOL_RA = 9
    PROTOCOL_MRT = 10
    PROTOCOL_ZEBRA = 11
    PROTOCOL_BIRD = 12
    PROTOCOL_DNROUTED = 13
    PROTOCOL_XORP = 14
    PROTOCOL_NTK = 15
    PROTOCOL_DHCP = 16
    PROTOCOL_MRTD = 17
    PROTOCOL_KEEPALIVED = 18
    PROTOCOL_BABEL = 42
    PROTOCOL_OPENR = 99
    PROTOCOL_BGP = 186
    PROTOCOL_ISIS = 187
    PROTOCOL_OSPF = 188
    PROTOCOL_RIP = 189
    PROTOCOL_EIGRP = 192


class NethelpersRoutingTable(betterproto.Enum):
    """NethelpersRoutingTable is a routing table ID."""

    TABLE_UNSPEC = 0
    TABLE_DEFAULT = 253
    TABLE_MAIN = 254
    TABLE_LOCAL = 255


class NethelpersRouteType(betterproto.Enum):
    """NethelpersRouteType is a route type."""

    TYPE_UNSPEC = 0
    TYPE_UNICAST = 1
    TYPE_LOCAL = 2
    TYPE_BROADCAST = 3
    TYPE_ANYCAST = 4
    TYPE_MULTICAST = 5
    TYPE_BLACKHOLE = 6
    TYPE_UNREACHABLE = 7
    TYPE_PROHIBIT = 8
    TYPE_THROW = 9
    TYPE_NAT = 10
    TYPE_X_RESOLVE = 11


class NethelpersVlanProtocol(betterproto.Enum):
    """NethelpersVLANProtocol is a VLAN protocol."""

    VLAN_PROTOCOL8021_Q = 0
    VLAN_PROTOCOL8021_AD = 1


class RuntimeMachineStage(betterproto.Enum):
    """
    RuntimeMachineStage describes the stage of the machine boot/run process.
    """

    MACHINE_STAGE_UNKNOWN = 0
    MACHINE_STAGE_BOOTING = 1
    MACHINE_STAGE_INSTALLING = 2
    MACHINE_STAGE_MAINTENANCE = 3
    MACHINE_STAGE_RUNNING = 4
    MACHINE_STAGE_REBOOTING = 5
    MACHINE_STAGE_SHUTTING_DOWN = 6
    MACHINE_STAGE_RESETTING = 7
    MACHINE_STAGE_UPGRADING = 8
