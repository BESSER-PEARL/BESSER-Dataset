from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class EdgeLabel:

    pass
class transport_PipeTransportEdgeLabel(EdgeLabel):

    pass
class PopulationEdge:

    pass
class EdgeDecorator:

    pass
class transport_PacketStyleTransportSystemDecorator(EdgeDecorator):

    pass
class LabelValue:

    pass
class transport_PipeTransportEdgeLabelValue(LabelValue):

    def __init__(self, maxFlow: float, timePeriod: str):
        self.maxFlow = maxFlow
        self.timePeriod = timePeriod
        
    @property
    def maxFlow(self) -> float:
        return self.__maxFlow

    @maxFlow.setter
    def maxFlow(self, maxFlow: float):
        self.__maxFlow = maxFlow

    @property
    def timePeriod(self) -> str:
        return self.__timePeriod

    @timePeriod.setter
    def timePeriod(self, timePeriod: str):
        self.__timePeriod = timePeriod

class transport_PacketTransportLabelValue(LabelValue):

    def __init__(self, capacity: float):
        self.capacity = capacity
        
    @property
    def capacity(self) -> float:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: float):
        self.__capacity = capacity

class Node:

    pass
class transport_TransportSystem(Node):

    pass
class TransportSystem:

    pass
class transport_PacketStyleTransportSystem(TransportSystem):

    pass
class transport_STEMTime:

    pass
class DynamicLabel:

    pass
class MigrationEdgeLabel:

    pass
class transport_LoadUnloadEdgeLabel(DynamicLabel, MigrationEdgeLabel):

    def __init__(self, activatedRate: float, transport_LoadUnloadEdgeLabel: "transport_STEMTime" = None, transport_LoadUnloadEdgeLabel2: "transport_STEMTime" = None):
        self.activatedRate = activatedRate
        self.transport_LoadUnloadEdgeLabel = transport_LoadUnloadEdgeLabel
        self.transport_LoadUnloadEdgeLabel2 = transport_LoadUnloadEdgeLabel2
        
    @property
    def activatedRate(self) -> float:
        return self.__activatedRate

    @activatedRate.setter
    def activatedRate(self, activatedRate: float):
        self.__activatedRate = activatedRate

    @property
    def transport_LoadUnloadEdgeLabel2(self):
        return self.__transport_LoadUnloadEdgeLabel2

    @transport_LoadUnloadEdgeLabel2.setter
    def transport_LoadUnloadEdgeLabel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transport_LoadUnloadEdgeLabel__transport_LoadUnloadEdgeLabel2", None)
        self.__transport_LoadUnloadEdgeLabel2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transport_STEMTime3"):
                opp_val = getattr(old_value, "transport_STEMTime3", None)
                if opp_val == self:
                    setattr(old_value, "transport_STEMTime3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transport_STEMTime3"):
                opp_val = getattr(value, "transport_STEMTime3", None)
                setattr(value, "transport_STEMTime3", self)

    @property
    def transport_LoadUnloadEdgeLabel(self):
        return self.__transport_LoadUnloadEdgeLabel

    @transport_LoadUnloadEdgeLabel.setter
    def transport_LoadUnloadEdgeLabel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transport_LoadUnloadEdgeLabel__transport_LoadUnloadEdgeLabel", None)
        self.__transport_LoadUnloadEdgeLabel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transport_STEMTime"):
                opp_val = getattr(old_value, "transport_STEMTime", None)
                if opp_val == self:
                    setattr(old_value, "transport_STEMTime", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transport_STEMTime"):
                opp_val = getattr(value, "transport_STEMTime", None)
                setattr(value, "transport_STEMTime", self)

class MigrationEdge:

    pass
class transport_LoadUnloadEdge(MigrationEdge):

    def __init__(self, loadingEdge: bool, transport_LoadUnloadEdge: "transport_PacketStyleTransportSystem" = None, transport_LoadUnloadEdge9: "transport_PacketStyleTransportSystem" = None):
        self.loadingEdge = loadingEdge
        self.transport_LoadUnloadEdge = transport_LoadUnloadEdge
        self.transport_LoadUnloadEdge9 = transport_LoadUnloadEdge9
        
    @property
    def loadingEdge(self) -> bool:
        return self.__loadingEdge

    @loadingEdge.setter
    def loadingEdge(self, loadingEdge: bool):
        self.__loadingEdge = loadingEdge

    @property
    def transport_LoadUnloadEdge9(self):
        return self.__transport_LoadUnloadEdge9

    @transport_LoadUnloadEdge9.setter
    def transport_LoadUnloadEdge9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transport_LoadUnloadEdge__transport_LoadUnloadEdge9", None)
        self.__transport_LoadUnloadEdge9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transport_PacketStyleTransportSystem8"):
                opp_val = getattr(old_value, "transport_PacketStyleTransportSystem8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transport_PacketStyleTransportSystem8"):
                opp_val = getattr(value, "transport_PacketStyleTransportSystem8", None)
                if opp_val is None:
                    setattr(value, "transport_PacketStyleTransportSystem8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def transport_LoadUnloadEdge(self):
        return self.__transport_LoadUnloadEdge

    @transport_LoadUnloadEdge.setter
    def transport_LoadUnloadEdge(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transport_LoadUnloadEdge__transport_LoadUnloadEdge", None)
        self.__transport_LoadUnloadEdge = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transport_PacketStyleTransportSystem6"):
                opp_val = getattr(old_value, "transport_PacketStyleTransportSystem6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transport_PacketStyleTransportSystem6"):
                opp_val = getattr(value, "transport_PacketStyleTransportSystem6", None)
                if opp_val is None:
                    setattr(value, "transport_PacketStyleTransportSystem6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class transport_PipeTransportEdge(PopulationEdge):

    pass
class transport_PipeStyleTransportSystem(TransportSystem):

    def __init__(self, maxCapacity: float, transport_PipeStyleTransportSystem: set["transport_PipeTransportEdge"] = None, transport_PipeStyleTransportSystem12: set["transport_PipeTransportEdge"] = None):
        self.maxCapacity = maxCapacity
        self.transport_PipeStyleTransportSystem = transport_PipeStyleTransportSystem if transport_PipeStyleTransportSystem is not None else set()
        self.transport_PipeStyleTransportSystem12 = transport_PipeStyleTransportSystem12 if transport_PipeStyleTransportSystem12 is not None else set()
        
    @property
    def maxCapacity(self) -> float:
        return self.__maxCapacity

    @maxCapacity.setter
    def maxCapacity(self, maxCapacity: float):
        self.__maxCapacity = maxCapacity

    @property
    def transport_PipeStyleTransportSystem(self):
        return self.__transport_PipeStyleTransportSystem

    @transport_PipeStyleTransportSystem.setter
    def transport_PipeStyleTransportSystem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transport_PipeStyleTransportSystem__transport_PipeStyleTransportSystem", None)
        self.__transport_PipeStyleTransportSystem = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "transport_PipeTransportEdge"):
                    opp_val = getattr(item, "transport_PipeTransportEdge", None)
                    
                    if opp_val == self:
                        setattr(item, "transport_PipeTransportEdge", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "transport_PipeTransportEdge"):
                    opp_val = getattr(item, "transport_PipeTransportEdge", None)
                    
                    setattr(item, "transport_PipeTransportEdge", self)
                    

    @property
    def transport_PipeStyleTransportSystem12(self):
        return self.__transport_PipeStyleTransportSystem12

    @transport_PipeStyleTransportSystem12.setter
    def transport_PipeStyleTransportSystem12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transport_PipeStyleTransportSystem__transport_PipeStyleTransportSystem12", None)
        self.__transport_PipeStyleTransportSystem12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "transport_PipeTransportEdge13"):
                    opp_val = getattr(item, "transport_PipeTransportEdge13", None)
                    
                    if opp_val == self:
                        setattr(item, "transport_PipeTransportEdge13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "transport_PipeTransportEdge13"):
                    opp_val = getattr(item, "transport_PipeTransportEdge13", None)
                    
                    setattr(item, "transport_PipeTransportEdge13", self)
                    

class NodeLabel:

    pass
class transport_PacketTransportLabel(NodeLabel):

    pass