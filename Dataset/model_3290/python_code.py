from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PortKind(Enum):
    external = "external"
    internal = "internal"
    relay = "relay"
    interface = "interface"


############################################
# Definition of Classes
############################################

class etricegen_GraphContainer:

    pass
class WiredStructureClass:

    pass
class etricegen_WiredSubSystemClass(WiredStructureClass):

    pass
class etricegen_WiredActorClass(WiredStructureClass):

    pass
class etricegen_OpenServiceConnection:

    def __init__(self, path: str, etricegen_OpenServiceConnection: "etricegen_WiredStructureClass" = None, etricegen_OpenServiceConnection109: "etricegen_WiredStructureClass" = None, etricegen_OpenServiceConnection114: "etricegen_ProtocolClass" = None):
        self.path = path
        self.etricegen_OpenServiceConnection = etricegen_OpenServiceConnection
        self.etricegen_OpenServiceConnection109 = etricegen_OpenServiceConnection109
        self.etricegen_OpenServiceConnection114 = etricegen_OpenServiceConnection114
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def etricegen_OpenServiceConnection(self):
        return self.__etricegen_OpenServiceConnection

    @etricegen_OpenServiceConnection.setter
    def etricegen_OpenServiceConnection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_OpenServiceConnection__etricegen_OpenServiceConnection", None)
        self.__etricegen_OpenServiceConnection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etricegen_WiredStructureClass106"):
                opp_val = getattr(old_value, "etricegen_WiredStructureClass106", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etricegen_WiredStructureClass106"):
                opp_val = getattr(value, "etricegen_WiredStructureClass106", None)
                if opp_val is None:
                    setattr(value, "etricegen_WiredStructureClass106", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def etricegen_OpenServiceConnection114(self):
        return self.__etricegen_OpenServiceConnection114

    @etricegen_OpenServiceConnection114.setter
    def etricegen_OpenServiceConnection114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_OpenServiceConnection__etricegen_OpenServiceConnection114", None)
        self.__etricegen_OpenServiceConnection114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etricegen_ProtocolClass115"):
                opp_val = getattr(old_value, "etricegen_ProtocolClass115", None)
                if opp_val == self:
                    setattr(old_value, "etricegen_ProtocolClass115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etricegen_ProtocolClass115"):
                opp_val = getattr(value, "etricegen_ProtocolClass115", None)
                setattr(value, "etricegen_ProtocolClass115", self)

    @property
    def etricegen_OpenServiceConnection109(self):
        return self.__etricegen_OpenServiceConnection109

    @etricegen_OpenServiceConnection109.setter
    def etricegen_OpenServiceConnection109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_OpenServiceConnection__etricegen_OpenServiceConnection109", None)
        self.__etricegen_OpenServiceConnection109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etricegen_WiredStructureClass108"):
                opp_val = getattr(old_value, "etricegen_WiredStructureClass108", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etricegen_WiredStructureClass108"):
                opp_val = getattr(value, "etricegen_WiredStructureClass108", None)
                if opp_val is None:
                    setattr(value, "etricegen_WiredStructureClass108", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class etricegen_OpenBinding:

    def __init__(self, path: str, etricegen_OpenBinding: "etricegen_WiredStructureClass" = None, etricegen_OpenBinding111: "etricegen_Port" = None):
        self.path = path
        self.etricegen_OpenBinding = etricegen_OpenBinding
        self.etricegen_OpenBinding111 = etricegen_OpenBinding111
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

    @property
    def etricegen_OpenBinding(self):
        return self.__etricegen_OpenBinding

    @etricegen_OpenBinding.setter
    def etricegen_OpenBinding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_OpenBinding__etricegen_OpenBinding", None)
        self.__etricegen_OpenBinding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etricegen_WiredStructureClass104"):
                opp_val = getattr(old_value, "etricegen_WiredStructureClass104", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etricegen_WiredStructureClass104"):
                opp_val = getattr(value, "etricegen_WiredStructureClass104", None)
                if opp_val is None:
                    setattr(value, "etricegen_WiredStructureClass104", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def etricegen_OpenBinding111(self):
        return self.__etricegen_OpenBinding111

    @etricegen_OpenBinding111.setter
    def etricegen_OpenBinding111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_OpenBinding__etricegen_OpenBinding111", None)
        self.__etricegen_OpenBinding111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etricegen_Port112"):
                opp_val = getattr(old_value, "etricegen_Port112", None)
                if opp_val == self:
                    setattr(old_value, "etricegen_Port112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etricegen_Port112"):
                opp_val = getattr(value, "etricegen_Port112", None)
                setattr(value, "etricegen_Port112", self)

class etricegen_Wire:

    def __init__(self, dataDriven: bool, path1: str, path2: str, etricegen_Wire: "etricegen_WiredStructureClass" = None):
        self.dataDriven = dataDriven
        self.path1 = path1
        self.path2 = path2
        self.etricegen_Wire = etricegen_Wire
        
    @property
    def dataDriven(self) -> bool:
        return self.__dataDriven

    @dataDriven.setter
    def dataDriven(self, dataDriven: bool):
        self.__dataDriven = dataDriven

    @property
    def path2(self) -> str:
        return self.__path2

    @path2.setter
    def path2(self, path2: str):
        self.__path2 = path2

    @property
    def path1(self) -> str:
        return self.__path1

    @path1.setter
    def path1(self, path1: str):
        self.__path1 = path1

    @property
    def etricegen_Wire(self):
        return self.__etricegen_Wire

    @etricegen_Wire.setter
    def etricegen_Wire(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_Wire__etricegen_Wire", None)
        self.__etricegen_Wire = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etricegen_WiredStructureClass102"):
                opp_val = getattr(old_value, "etricegen_WiredStructureClass102", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etricegen_WiredStructureClass102"):
                opp_val = getattr(value, "etricegen_WiredStructureClass102", None)
                if opp_val is None:
                    setattr(value, "etricegen_WiredStructureClass102", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class etricegen_LayerConnection:

    pass
class etricegen_ServiceImplementation:

    pass
class etricegen_SPP:

    pass
class etricegen_SAP:

    pass
class etricegen_Binding:

    pass
class etricegen_Port:

    pass
class InterfaceItemInstance:

    pass
class StructureInstance:

    pass
class etricegen_LogicalSystem:

    pass
class etricegen_ActorInstance(StructureInstance):

    def __init__(self, replIdx: int, unindexedName: str, etricegen_ActorInstance: "etricegen_StructureInstance" = None, etricegen_ActorInstance64: "etricegen_ActorClass" = None):
        self.replIdx = replIdx
        self.unindexedName = unindexedName
        self.etricegen_ActorInstance = etricegen_ActorInstance
        self.etricegen_ActorInstance64 = etricegen_ActorInstance64
        
    @property
    def replIdx(self) -> int:
        return self.__replIdx

    @replIdx.setter
    def replIdx(self, replIdx: int):
        self.__replIdx = replIdx

    @property
    def unindexedName(self) -> str:
        return self.__unindexedName

    @unindexedName.setter
    def unindexedName(self, unindexedName: str):
        self.__unindexedName = unindexedName

    @property
    def etricegen_ActorInstance64(self):
        return self.__etricegen_ActorInstance64

    @etricegen_ActorInstance64.setter
    def etricegen_ActorInstance64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_ActorInstance__etricegen_ActorInstance64", None)
        self.__etricegen_ActorInstance64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etricegen_ActorClass65"):
                opp_val = getattr(old_value, "etricegen_ActorClass65", None)
                if opp_val == self:
                    setattr(old_value, "etricegen_ActorClass65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etricegen_ActorClass65"):
                opp_val = getattr(value, "etricegen_ActorClass65", None)
                setattr(value, "etricegen_ActorClass65", self)

    @property
    def etricegen_ActorInstance(self):
        return self.__etricegen_ActorInstance

    @etricegen_ActorInstance.setter
    def etricegen_ActorInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_ActorInstance__etricegen_ActorInstance", None)
        self.__etricegen_ActorInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etricegen_StructureInstance52"):
                opp_val = getattr(old_value, "etricegen_StructureInstance52", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etricegen_StructureInstance52"):
                opp_val = getattr(value, "etricegen_StructureInstance52", None)
                if opp_val is None:
                    setattr(value, "etricegen_StructureInstance52", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class etricegen_ConnectionInstance:

    pass
class etricegen_BindingInstance:

    pass
class etricegen_SAPInstance(InterfaceItemInstance):

    pass
class etricegen_ServiceImplInstance(InterfaceItemInstance):

    pass
class AbstractInstance:

    pass
class etricegen_StructureInstance(AbstractInstance):

    def __init__(self, etricegen_StructureInstance: set["etricegen_AbstractInstance"] = None, etricegen_StructureInstance41: set["etricegen_SAPInstance"] = None, etricegen_StructureInstance43: set["etricegen_SPPInstance"] = None, etricegen_StructureInstance45: set["etricegen_ServiceImplInstance"] = None, etricegen_StructureInstance48: set["etricegen_BindingInstance"] = None, etricegen_StructureInstance50: set["etricegen_ConnectionInstance"] = None, etricegen_StructureInstance52: set["etricegen_ActorInstance"] = None, etricegen_StructureInstance54: set["etricegen_InterfaceItemInstance"] = None):
        self.etricegen_StructureInstance = etricegen_StructureInstance if etricegen_StructureInstance is not None else set()
        self.etricegen_StructureInstance41 = etricegen_StructureInstance41 if etricegen_StructureInstance41 is not None else set()
        self.etricegen_StructureInstance43 = etricegen_StructureInstance43 if etricegen_StructureInstance43 is not None else set()
        self.etricegen_StructureInstance45 = etricegen_StructureInstance45 if etricegen_StructureInstance45 is not None else set()
        self.etricegen_StructureInstance48 = etricegen_StructureInstance48 if etricegen_StructureInstance48 is not None else set()
        self.etricegen_StructureInstance50 = etricegen_StructureInstance50 if etricegen_StructureInstance50 is not None else set()
        self.etricegen_StructureInstance52 = etricegen_StructureInstance52 if etricegen_StructureInstance52 is not None else set()
        self.etricegen_StructureInstance54 = etricegen_StructureInstance54 if etricegen_StructureInstance54 is not None else set()
        
    @property
    def etricegen_StructureInstance45(self):
        return self.__etricegen_StructureInstance45

    @etricegen_StructureInstance45.setter
    def etricegen_StructureInstance45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_StructureInstance__etricegen_StructureInstance45", None)
        self.__etricegen_StructureInstance45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_ServiceImplInstance46"):
                    opp_val = getattr(item, "etricegen_ServiceImplInstance46", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_ServiceImplInstance46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_ServiceImplInstance46"):
                    opp_val = getattr(item, "etricegen_ServiceImplInstance46", None)
                    
                    setattr(item, "etricegen_ServiceImplInstance46", self)
                    

    @property
    def etricegen_StructureInstance43(self):
        return self.__etricegen_StructureInstance43

    @etricegen_StructureInstance43.setter
    def etricegen_StructureInstance43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_StructureInstance__etricegen_StructureInstance43", None)
        self.__etricegen_StructureInstance43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_SPPInstance"):
                    opp_val = getattr(item, "etricegen_SPPInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_SPPInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_SPPInstance"):
                    opp_val = getattr(item, "etricegen_SPPInstance", None)
                    
                    setattr(item, "etricegen_SPPInstance", self)
                    

    @property
    def etricegen_StructureInstance52(self):
        return self.__etricegen_StructureInstance52

    @etricegen_StructureInstance52.setter
    def etricegen_StructureInstance52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_StructureInstance__etricegen_StructureInstance52", None)
        self.__etricegen_StructureInstance52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_ActorInstance"):
                    opp_val = getattr(item, "etricegen_ActorInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_ActorInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_ActorInstance"):
                    opp_val = getattr(item, "etricegen_ActorInstance", None)
                    
                    setattr(item, "etricegen_ActorInstance", self)
                    

    @property
    def etricegen_StructureInstance48(self):
        return self.__etricegen_StructureInstance48

    @etricegen_StructureInstance48.setter
    def etricegen_StructureInstance48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_StructureInstance__etricegen_StructureInstance48", None)
        self.__etricegen_StructureInstance48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_BindingInstance"):
                    opp_val = getattr(item, "etricegen_BindingInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_BindingInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_BindingInstance"):
                    opp_val = getattr(item, "etricegen_BindingInstance", None)
                    
                    setattr(item, "etricegen_BindingInstance", self)
                    

    @property
    def etricegen_StructureInstance54(self):
        return self.__etricegen_StructureInstance54

    @etricegen_StructureInstance54.setter
    def etricegen_StructureInstance54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_StructureInstance__etricegen_StructureInstance54", None)
        self.__etricegen_StructureInstance54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_InterfaceItemInstance"):
                    opp_val = getattr(item, "etricegen_InterfaceItemInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_InterfaceItemInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_InterfaceItemInstance"):
                    opp_val = getattr(item, "etricegen_InterfaceItemInstance", None)
                    
                    setattr(item, "etricegen_InterfaceItemInstance", self)
                    

    @property
    def etricegen_StructureInstance(self):
        return self.__etricegen_StructureInstance

    @etricegen_StructureInstance.setter
    def etricegen_StructureInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_StructureInstance__etricegen_StructureInstance", None)
        self.__etricegen_StructureInstance = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_AbstractInstance39"):
                    opp_val = getattr(item, "etricegen_AbstractInstance39", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_AbstractInstance39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_AbstractInstance39"):
                    opp_val = getattr(item, "etricegen_AbstractInstance39", None)
                    
                    setattr(item, "etricegen_AbstractInstance39", self)
                    

    @property
    def etricegen_StructureInstance41(self):
        return self.__etricegen_StructureInstance41

    @etricegen_StructureInstance41.setter
    def etricegen_StructureInstance41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_StructureInstance__etricegen_StructureInstance41", None)
        self.__etricegen_StructureInstance41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_SAPInstance"):
                    opp_val = getattr(item, "etricegen_SAPInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_SAPInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_SAPInstance"):
                    opp_val = getattr(item, "etricegen_SAPInstance", None)
                    
                    setattr(item, "etricegen_SAPInstance", self)
                    

    @property
    def etricegen_StructureInstance50(self):
        return self.__etricegen_StructureInstance50

    @etricegen_StructureInstance50.setter
    def etricegen_StructureInstance50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_StructureInstance__etricegen_StructureInstance50", None)
        self.__etricegen_StructureInstance50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_ConnectionInstance"):
                    opp_val = getattr(item, "etricegen_ConnectionInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_ConnectionInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_ConnectionInstance"):
                    opp_val = getattr(item, "etricegen_ConnectionInstance", None)
                    
                    setattr(item, "etricegen_ConnectionInstance", self)
                    

    def getActorInstances(self) -> str:
        # TODO: Implement getActorInstances method
        pass

class etricegen_ActorInterfaceInstance(AbstractInstance):

    def __init__(self, array: bool, etricegen_ActorInterfaceInstance: "etricegen_ActorClass" = None, etricegen_ActorInterfaceInstance34: set["etricegen_ServiceImplInstance"] = None, etricegen_ActorInterfaceInstance36: set["etricegen_OptionalActorInstance"] = None):
        self.array = array
        self.etricegen_ActorInterfaceInstance = etricegen_ActorInterfaceInstance
        self.etricegen_ActorInterfaceInstance34 = etricegen_ActorInterfaceInstance34 if etricegen_ActorInterfaceInstance34 is not None else set()
        self.etricegen_ActorInterfaceInstance36 = etricegen_ActorInterfaceInstance36 if etricegen_ActorInterfaceInstance36 is not None else set()
        
    @property
    def array(self) -> bool:
        return self.__array

    @array.setter
    def array(self, array: bool):
        self.__array = array

    @property
    def etricegen_ActorInterfaceInstance34(self):
        return self.__etricegen_ActorInterfaceInstance34

    @etricegen_ActorInterfaceInstance34.setter
    def etricegen_ActorInterfaceInstance34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_ActorInterfaceInstance__etricegen_ActorInterfaceInstance34", None)
        self.__etricegen_ActorInterfaceInstance34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_ServiceImplInstance"):
                    opp_val = getattr(item, "etricegen_ServiceImplInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_ServiceImplInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_ServiceImplInstance"):
                    opp_val = getattr(item, "etricegen_ServiceImplInstance", None)
                    
                    setattr(item, "etricegen_ServiceImplInstance", self)
                    

    @property
    def etricegen_ActorInterfaceInstance36(self):
        return self.__etricegen_ActorInterfaceInstance36

    @etricegen_ActorInterfaceInstance36.setter
    def etricegen_ActorInterfaceInstance36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_ActorInterfaceInstance__etricegen_ActorInterfaceInstance36", None)
        self.__etricegen_ActorInterfaceInstance36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_OptionalActorInstance37"):
                    opp_val = getattr(item, "etricegen_OptionalActorInstance37", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_OptionalActorInstance37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_OptionalActorInstance37"):
                    opp_val = getattr(item, "etricegen_OptionalActorInstance37", None)
                    
                    setattr(item, "etricegen_OptionalActorInstance37", self)
                    

    @property
    def etricegen_ActorInterfaceInstance(self):
        return self.__etricegen_ActorInterfaceInstance

    @etricegen_ActorInterfaceInstance.setter
    def etricegen_ActorInterfaceInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_ActorInterfaceInstance__etricegen_ActorInterfaceInstance", None)
        self.__etricegen_ActorInterfaceInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etricegen_ActorClass32"):
                opp_val = getattr(old_value, "etricegen_ActorClass32", None)
                if opp_val == self:
                    setattr(old_value, "etricegen_ActorClass32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etricegen_ActorClass32"):
                opp_val = getattr(value, "etricegen_ActorClass32", None)
                setattr(value, "etricegen_ActorClass32", self)

class etricegen_PortInstance(InterfaceItemInstance):

    def __init__(self, kind: str, etricegen_PortInstance: "etricegen_AbstractInstance" = None, etricegen_PortInstance79: "etricegen_Port" = None, ports: set["etricegen_BindingInstance"] = None, PortInstance: "etricegen_BindingInstance" = None):
        self.kind = kind
        self.etricegen_PortInstance = etricegen_PortInstance
        self.etricegen_PortInstance79 = etricegen_PortInstance79
        self.ports = ports if ports is not None else set()
        self.PortInstance = PortInstance
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def ports(self):
        return self.__ports

    @ports.setter
    def ports(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_PortInstance__ports", None)
        self.__ports = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BindingInstance"):
                    opp_val = getattr(item, "BindingInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "BindingInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BindingInstance"):
                    opp_val = getattr(item, "BindingInstance", None)
                    
                    setattr(item, "BindingInstance", self)
                    

    @property
    def etricegen_PortInstance(self):
        return self.__etricegen_PortInstance

    @etricegen_PortInstance.setter
    def etricegen_PortInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_PortInstance__etricegen_PortInstance", None)
        self.__etricegen_PortInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etricegen_AbstractInstance"):
                opp_val = getattr(old_value, "etricegen_AbstractInstance", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etricegen_AbstractInstance"):
                opp_val = getattr(value, "etricegen_AbstractInstance", None)
                if opp_val is None:
                    setattr(value, "etricegen_AbstractInstance", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def etricegen_PortInstance79(self):
        return self.__etricegen_PortInstance79

    @etricegen_PortInstance79.setter
    def etricegen_PortInstance79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_PortInstance__etricegen_PortInstance79", None)
        self.__etricegen_PortInstance79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etricegen_Port"):
                opp_val = getattr(old_value, "etricegen_Port", None)
                if opp_val == self:
                    setattr(old_value, "etricegen_Port", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etricegen_Port"):
                opp_val = getattr(value, "etricegen_Port", None)
                setattr(value, "etricegen_Port", self)

    @property
    def PortInstance(self):
        return self.__PortInstance

    @PortInstance.setter
    def PortInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_PortInstance__PortInstance", None)
        self.__PortInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bindings"):
                opp_val = getattr(old_value, "bindings", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bindings"):
                opp_val = getattr(value, "bindings", None)
                if opp_val is None:
                    setattr(value, "bindings", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class InstanceBase:

    pass
class etricegen_SPPInstance(InstanceBase):

    pass
class etricegen_InterfaceItemInstance(InstanceBase):

    def __init__(self, etricegen_InterfaceItemInstance: "etricegen_StructureInstance" = None, etricegen_InterfaceItemInstance73: "etricegen_ProtocolClass" = None, etricegen_InterfaceItemInstance77: "etricegen_InterfaceItemInstance" = None, etricegen_InterfaceItemInstance75: set["etricegen_InterfaceItemInstance"] = None):
        self.etricegen_InterfaceItemInstance = etricegen_InterfaceItemInstance
        self.etricegen_InterfaceItemInstance73 = etricegen_InterfaceItemInstance73
        self.etricegen_InterfaceItemInstance77 = etricegen_InterfaceItemInstance77
        self.etricegen_InterfaceItemInstance75 = etricegen_InterfaceItemInstance75 if etricegen_InterfaceItemInstance75 is not None else set()
        
    @property
    def etricegen_InterfaceItemInstance75(self):
        return self.__etricegen_InterfaceItemInstance75

    @etricegen_InterfaceItemInstance75.setter
    def etricegen_InterfaceItemInstance75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_InterfaceItemInstance__etricegen_InterfaceItemInstance75", None)
        self.__etricegen_InterfaceItemInstance75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_InterfaceItemInstance77"):
                    opp_val = getattr(item, "etricegen_InterfaceItemInstance77", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_InterfaceItemInstance77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_InterfaceItemInstance77"):
                    opp_val = getattr(item, "etricegen_InterfaceItemInstance77", None)
                    
                    setattr(item, "etricegen_InterfaceItemInstance77", self)
                    

    @property
    def etricegen_InterfaceItemInstance(self):
        return self.__etricegen_InterfaceItemInstance

    @etricegen_InterfaceItemInstance.setter
    def etricegen_InterfaceItemInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_InterfaceItemInstance__etricegen_InterfaceItemInstance", None)
        self.__etricegen_InterfaceItemInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etricegen_StructureInstance54"):
                opp_val = getattr(old_value, "etricegen_StructureInstance54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etricegen_StructureInstance54"):
                opp_val = getattr(value, "etricegen_StructureInstance54", None)
                if opp_val is None:
                    setattr(value, "etricegen_StructureInstance54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def etricegen_InterfaceItemInstance77(self):
        return self.__etricegen_InterfaceItemInstance77

    @etricegen_InterfaceItemInstance77.setter
    def etricegen_InterfaceItemInstance77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_InterfaceItemInstance__etricegen_InterfaceItemInstance77", None)
        self.__etricegen_InterfaceItemInstance77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etricegen_InterfaceItemInstance75"):
                opp_val = getattr(old_value, "etricegen_InterfaceItemInstance75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etricegen_InterfaceItemInstance75"):
                opp_val = getattr(value, "etricegen_InterfaceItemInstance75", None)
                if opp_val is None:
                    setattr(value, "etricegen_InterfaceItemInstance75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def etricegen_InterfaceItemInstance73(self):
        return self.__etricegen_InterfaceItemInstance73

    @etricegen_InterfaceItemInstance73.setter
    def etricegen_InterfaceItemInstance73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_InterfaceItemInstance__etricegen_InterfaceItemInstance73", None)
        self.__etricegen_InterfaceItemInstance73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etricegen_ProtocolClass74"):
                opp_val = getattr(old_value, "etricegen_ProtocolClass74", None)
                if opp_val == self:
                    setattr(old_value, "etricegen_ProtocolClass74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etricegen_ProtocolClass74"):
                opp_val = getattr(value, "etricegen_ProtocolClass74", None)
                setattr(value, "etricegen_ProtocolClass74", self)

    def isReplicated(self) -> bool:
        # TODO: Implement isReplicated method
        pass

    def isSimple(self) -> bool:
        # TODO: Implement isSimple method
        pass

    def isRelay(self) -> bool:
        # TODO: Implement isRelay method
        pass

    def getInterfaceItem(self) -> str:
        # TODO: Implement getInterfaceItem method
        pass

class etricegen_AbstractInstance(InstanceBase):

    pass
class etricegen_InstanceBase(ABC):

    def __init__(self, name: str, path: str, objId: int, threadId: int, nObjIDs: int):
        self.name = name
        self.path = path
        self.objId = objId
        self.threadId = threadId
        self.nObjIDs = nObjIDs
        
    @property
    def nObjIDs(self) -> int:
        return self.__nObjIDs

    @nObjIDs.setter
    def nObjIDs(self, nObjIDs: int):
        self.__nObjIDs = nObjIDs

    @property
    def threadId(self) -> int:
        return self.__threadId

    @threadId.setter
    def threadId(self, threadId: int):
        self.__threadId = threadId

    @property
    def objId(self) -> int:
        return self.__objId

    @objId.setter
    def objId(self, objId: int):
        self.__objId = objId

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

class etricegen_OptionalActorInstance(StructureInstance):

    pass
class etricegen_SubSystemClass:

    pass
class etricegen_EnumerationType:

    pass
class etricegen_ActorClass:

    pass
class etricegen_ProtocolClass:

    pass
class etricegen_DataClass:

    pass
class etricegen_ExpandedActorClass:

    def __init__(self, etricegen_ExpandedActorClass: "etricegen_Root" = None, etricegen_ExpandedActorClass121: "etricegen_ActorClass" = None, etricegen_ExpandedActorClass124: "etricegen_GraphContainer" = None):
        self.etricegen_ExpandedActorClass = etricegen_ExpandedActorClass
        self.etricegen_ExpandedActorClass121 = etricegen_ExpandedActorClass121
        self.etricegen_ExpandedActorClass124 = etricegen_ExpandedActorClass124
        
    @property
    def etricegen_ExpandedActorClass124(self):
        return self.__etricegen_ExpandedActorClass124

    @etricegen_ExpandedActorClass124.setter
    def etricegen_ExpandedActorClass124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_ExpandedActorClass__etricegen_ExpandedActorClass124", None)
        self.__etricegen_ExpandedActorClass124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etricegen_GraphContainer"):
                opp_val = getattr(old_value, "etricegen_GraphContainer", None)
                if opp_val == self:
                    setattr(old_value, "etricegen_GraphContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etricegen_GraphContainer"):
                opp_val = getattr(value, "etricegen_GraphContainer", None)
                setattr(value, "etricegen_GraphContainer", self)

    @property
    def etricegen_ExpandedActorClass121(self):
        return self.__etricegen_ExpandedActorClass121

    @etricegen_ExpandedActorClass121.setter
    def etricegen_ExpandedActorClass121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_ExpandedActorClass__etricegen_ExpandedActorClass121", None)
        self.__etricegen_ExpandedActorClass121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etricegen_ActorClass122"):
                opp_val = getattr(old_value, "etricegen_ActorClass122", None)
                if opp_val == self:
                    setattr(old_value, "etricegen_ActorClass122", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etricegen_ActorClass122"):
                opp_val = getattr(value, "etricegen_ActorClass122", None)
                setattr(value, "etricegen_ActorClass122", self)

    @property
    def etricegen_ExpandedActorClass(self):
        return self.__etricegen_ExpandedActorClass

    @etricegen_ExpandedActorClass.setter
    def etricegen_ExpandedActorClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_ExpandedActorClass__etricegen_ExpandedActorClass", None)
        self.__etricegen_ExpandedActorClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etricegen_Root12"):
                opp_val = getattr(old_value, "etricegen_Root12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etricegen_Root12"):
                opp_val = getattr(value, "etricegen_Root12", None)
                if opp_val is None:
                    setattr(value, "etricegen_Root12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getInterfaceItemLocalId(self, ifitem: str) -> int:
        # TODO: Implement getInterfaceItemLocalId method
        pass

class etricegen_RoomModel:

    pass
class etricegen_SubSystemInstance(StructureInstance):

    def __init__(self, maxObjId: int, etricegen_SubSystemInstance: "etricegen_Root" = None, etricegen_SubSystemInstance5: "etricegen_Root" = None, etricegen_SubSystemInstance57: "etricegen_SystemInstance" = None, etricegen_SubSystemInstance61: "etricegen_SubSystemClass" = None):
        self.maxObjId = maxObjId
        self.etricegen_SubSystemInstance = etricegen_SubSystemInstance
        self.etricegen_SubSystemInstance5 = etricegen_SubSystemInstance5
        self.etricegen_SubSystemInstance57 = etricegen_SubSystemInstance57
        self.etricegen_SubSystemInstance61 = etricegen_SubSystemInstance61
        
    @property
    def maxObjId(self) -> int:
        return self.__maxObjId

    @maxObjId.setter
    def maxObjId(self, maxObjId: int):
        self.__maxObjId = maxObjId

    @property
    def etricegen_SubSystemInstance5(self):
        return self.__etricegen_SubSystemInstance5

    @etricegen_SubSystemInstance5.setter
    def etricegen_SubSystemInstance5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_SubSystemInstance__etricegen_SubSystemInstance5", None)
        self.__etricegen_SubSystemInstance5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etricegen_Root4"):
                opp_val = getattr(old_value, "etricegen_Root4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etricegen_Root4"):
                opp_val = getattr(value, "etricegen_Root4", None)
                if opp_val is None:
                    setattr(value, "etricegen_Root4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def etricegen_SubSystemInstance(self):
        return self.__etricegen_SubSystemInstance

    @etricegen_SubSystemInstance.setter
    def etricegen_SubSystemInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_SubSystemInstance__etricegen_SubSystemInstance", None)
        self.__etricegen_SubSystemInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etricegen_Root2"):
                opp_val = getattr(old_value, "etricegen_Root2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etricegen_Root2"):
                opp_val = getattr(value, "etricegen_Root2", None)
                if opp_val is None:
                    setattr(value, "etricegen_Root2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def etricegen_SubSystemInstance57(self):
        return self.__etricegen_SubSystemInstance57

    @etricegen_SubSystemInstance57.setter
    def etricegen_SubSystemInstance57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_SubSystemInstance__etricegen_SubSystemInstance57", None)
        self.__etricegen_SubSystemInstance57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etricegen_SystemInstance56"):
                opp_val = getattr(old_value, "etricegen_SystemInstance56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etricegen_SystemInstance56"):
                opp_val = getattr(value, "etricegen_SystemInstance56", None)
                if opp_val is None:
                    setattr(value, "etricegen_SystemInstance56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def etricegen_SubSystemInstance61(self):
        return self.__etricegen_SubSystemInstance61

    @etricegen_SubSystemInstance61.setter
    def etricegen_SubSystemInstance61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_SubSystemInstance__etricegen_SubSystemInstance61", None)
        self.__etricegen_SubSystemInstance61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "etricegen_SubSystemClass62"):
                opp_val = getattr(old_value, "etricegen_SubSystemClass62", None)
                if opp_val == self:
                    setattr(old_value, "etricegen_SubSystemClass62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "etricegen_SubSystemClass62"):
                opp_val = getattr(value, "etricegen_SubSystemClass62", None)
                setattr(value, "etricegen_SubSystemClass62", self)

    def getThreadId(self, instance: InstanceBase) -> int:
        # TODO: Implement getThreadId method
        pass

class etricegen_SystemInstance(InstanceBase):

    pass
class etricegen_WiredStructureClass(ABC):

    pass
class etricegen_Root:

    def __init__(self, library: bool, etricegen_Root: set["etricegen_SystemInstance"] = None, etricegen_Root2: set["etricegen_SubSystemInstance"] = None, etricegen_Root4: set["etricegen_SubSystemInstance"] = None, etricegen_Root7: set["etricegen_RoomModel"] = None, etricegen_Root9: set["etricegen_RoomModel"] = None, etricegen_Root12: set["etricegen_ExpandedActorClass"] = None, etricegen_Root14: set["etricegen_DataClass"] = None, etricegen_Root16: set["etricegen_ProtocolClass"] = None, etricegen_Root18: set["etricegen_ActorClass"] = None, etricegen_Root20: set["etricegen_EnumerationType"] = None, etricegen_Root22: set["etricegen_SubSystemClass"] = None, etricegen_Root24: set["etricegen_OptionalActorInstance"] = None, etricegen_Root26: set["etricegen_ActorClass"] = None, etricegen_Root29: set["etricegen_WiredStructureClass"] = None):
        self.library = library
        self.etricegen_Root = etricegen_Root if etricegen_Root is not None else set()
        self.etricegen_Root2 = etricegen_Root2 if etricegen_Root2 is not None else set()
        self.etricegen_Root4 = etricegen_Root4 if etricegen_Root4 is not None else set()
        self.etricegen_Root7 = etricegen_Root7 if etricegen_Root7 is not None else set()
        self.etricegen_Root9 = etricegen_Root9 if etricegen_Root9 is not None else set()
        self.etricegen_Root12 = etricegen_Root12 if etricegen_Root12 is not None else set()
        self.etricegen_Root14 = etricegen_Root14 if etricegen_Root14 is not None else set()
        self.etricegen_Root16 = etricegen_Root16 if etricegen_Root16 is not None else set()
        self.etricegen_Root18 = etricegen_Root18 if etricegen_Root18 is not None else set()
        self.etricegen_Root20 = etricegen_Root20 if etricegen_Root20 is not None else set()
        self.etricegen_Root22 = etricegen_Root22 if etricegen_Root22 is not None else set()
        self.etricegen_Root24 = etricegen_Root24 if etricegen_Root24 is not None else set()
        self.etricegen_Root26 = etricegen_Root26 if etricegen_Root26 is not None else set()
        self.etricegen_Root29 = etricegen_Root29 if etricegen_Root29 is not None else set()
        
    @property
    def library(self) -> bool:
        return self.__library

    @library.setter
    def library(self, library: bool):
        self.__library = library

    @property
    def etricegen_Root14(self):
        return self.__etricegen_Root14

    @etricegen_Root14.setter
    def etricegen_Root14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_Root__etricegen_Root14", None)
        self.__etricegen_Root14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_DataClass"):
                    opp_val = getattr(item, "etricegen_DataClass", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_DataClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_DataClass"):
                    opp_val = getattr(item, "etricegen_DataClass", None)
                    
                    setattr(item, "etricegen_DataClass", self)
                    

    @property
    def etricegen_Root26(self):
        return self.__etricegen_Root26

    @etricegen_Root26.setter
    def etricegen_Root26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_Root__etricegen_Root26", None)
        self.__etricegen_Root26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_ActorClass27"):
                    opp_val = getattr(item, "etricegen_ActorClass27", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_ActorClass27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_ActorClass27"):
                    opp_val = getattr(item, "etricegen_ActorClass27", None)
                    
                    setattr(item, "etricegen_ActorClass27", self)
                    

    @property
    def etricegen_Root4(self):
        return self.__etricegen_Root4

    @etricegen_Root4.setter
    def etricegen_Root4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_Root__etricegen_Root4", None)
        self.__etricegen_Root4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_SubSystemInstance5"):
                    opp_val = getattr(item, "etricegen_SubSystemInstance5", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_SubSystemInstance5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_SubSystemInstance5"):
                    opp_val = getattr(item, "etricegen_SubSystemInstance5", None)
                    
                    setattr(item, "etricegen_SubSystemInstance5", self)
                    

    @property
    def etricegen_Root16(self):
        return self.__etricegen_Root16

    @etricegen_Root16.setter
    def etricegen_Root16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_Root__etricegen_Root16", None)
        self.__etricegen_Root16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_ProtocolClass"):
                    opp_val = getattr(item, "etricegen_ProtocolClass", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_ProtocolClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_ProtocolClass"):
                    opp_val = getattr(item, "etricegen_ProtocolClass", None)
                    
                    setattr(item, "etricegen_ProtocolClass", self)
                    

    @property
    def etricegen_Root22(self):
        return self.__etricegen_Root22

    @etricegen_Root22.setter
    def etricegen_Root22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_Root__etricegen_Root22", None)
        self.__etricegen_Root22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_SubSystemClass"):
                    opp_val = getattr(item, "etricegen_SubSystemClass", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_SubSystemClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_SubSystemClass"):
                    opp_val = getattr(item, "etricegen_SubSystemClass", None)
                    
                    setattr(item, "etricegen_SubSystemClass", self)
                    

    @property
    def etricegen_Root18(self):
        return self.__etricegen_Root18

    @etricegen_Root18.setter
    def etricegen_Root18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_Root__etricegen_Root18", None)
        self.__etricegen_Root18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_ActorClass"):
                    opp_val = getattr(item, "etricegen_ActorClass", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_ActorClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_ActorClass"):
                    opp_val = getattr(item, "etricegen_ActorClass", None)
                    
                    setattr(item, "etricegen_ActorClass", self)
                    

    @property
    def etricegen_Root12(self):
        return self.__etricegen_Root12

    @etricegen_Root12.setter
    def etricegen_Root12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_Root__etricegen_Root12", None)
        self.__etricegen_Root12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_ExpandedActorClass"):
                    opp_val = getattr(item, "etricegen_ExpandedActorClass", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_ExpandedActorClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_ExpandedActorClass"):
                    opp_val = getattr(item, "etricegen_ExpandedActorClass", None)
                    
                    setattr(item, "etricegen_ExpandedActorClass", self)
                    

    @property
    def etricegen_Root29(self):
        return self.__etricegen_Root29

    @etricegen_Root29.setter
    def etricegen_Root29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_Root__etricegen_Root29", None)
        self.__etricegen_Root29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_WiredStructureClass"):
                    opp_val = getattr(item, "etricegen_WiredStructureClass", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_WiredStructureClass", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_WiredStructureClass"):
                    opp_val = getattr(item, "etricegen_WiredStructureClass", None)
                    
                    setattr(item, "etricegen_WiredStructureClass", self)
                    

    @property
    def etricegen_Root24(self):
        return self.__etricegen_Root24

    @etricegen_Root24.setter
    def etricegen_Root24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_Root__etricegen_Root24", None)
        self.__etricegen_Root24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_OptionalActorInstance"):
                    opp_val = getattr(item, "etricegen_OptionalActorInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_OptionalActorInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_OptionalActorInstance"):
                    opp_val = getattr(item, "etricegen_OptionalActorInstance", None)
                    
                    setattr(item, "etricegen_OptionalActorInstance", self)
                    

    @property
    def etricegen_Root(self):
        return self.__etricegen_Root

    @etricegen_Root.setter
    def etricegen_Root(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_Root__etricegen_Root", None)
        self.__etricegen_Root = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_SystemInstance"):
                    opp_val = getattr(item, "etricegen_SystemInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_SystemInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_SystemInstance"):
                    opp_val = getattr(item, "etricegen_SystemInstance", None)
                    
                    setattr(item, "etricegen_SystemInstance", self)
                    

    @property
    def etricegen_Root20(self):
        return self.__etricegen_Root20

    @etricegen_Root20.setter
    def etricegen_Root20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_Root__etricegen_Root20", None)
        self.__etricegen_Root20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_EnumerationType"):
                    opp_val = getattr(item, "etricegen_EnumerationType", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_EnumerationType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_EnumerationType"):
                    opp_val = getattr(item, "etricegen_EnumerationType", None)
                    
                    setattr(item, "etricegen_EnumerationType", self)
                    

    @property
    def etricegen_Root2(self):
        return self.__etricegen_Root2

    @etricegen_Root2.setter
    def etricegen_Root2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_Root__etricegen_Root2", None)
        self.__etricegen_Root2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_SubSystemInstance"):
                    opp_val = getattr(item, "etricegen_SubSystemInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_SubSystemInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_SubSystemInstance"):
                    opp_val = getattr(item, "etricegen_SubSystemInstance", None)
                    
                    setattr(item, "etricegen_SubSystemInstance", self)
                    

    @property
    def etricegen_Root9(self):
        return self.__etricegen_Root9

    @etricegen_Root9.setter
    def etricegen_Root9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_Root__etricegen_Root9", None)
        self.__etricegen_Root9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_RoomModel10"):
                    opp_val = getattr(item, "etricegen_RoomModel10", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_RoomModel10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_RoomModel10"):
                    opp_val = getattr(item, "etricegen_RoomModel10", None)
                    
                    setattr(item, "etricegen_RoomModel10", self)
                    

    @property
    def etricegen_Root7(self):
        return self.__etricegen_Root7

    @etricegen_Root7.setter
    def etricegen_Root7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_etricegen_Root__etricegen_Root7", None)
        self.__etricegen_Root7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "etricegen_RoomModel"):
                    opp_val = getattr(item, "etricegen_RoomModel", None)
                    
                    if opp_val == self:
                        setattr(item, "etricegen_RoomModel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "etricegen_RoomModel"):
                    opp_val = getattr(item, "etricegen_RoomModel", None)
                    
                    setattr(item, "etricegen_RoomModel", self)
                    

    def getReferencedModels(self, cls: str) -> str:
        # TODO: Implement getReferencedModels method
        pass

    def getReferencedProtocolClasses(self, cls: str) -> str:
        # TODO: Implement getReferencedProtocolClasses method
        pass

    def getReferencedActorClasses(self, cls: str) -> str:
        # TODO: Implement getReferencedActorClasses method
        pass

    def computeSubClasses(self):
        # TODO: Implement computeSubClasses method
        pass

    def getReferencedDataClasses(self, cls: str) -> str:
        # TODO: Implement getReferencedDataClasses method
        pass

    def getInstance(self, path: str) -> str:
        # TODO: Implement getInstance method
        pass

    def getSubClasses(self, ac: str) -> str:
        # TODO: Implement getSubClasses method
        pass

    def getExpandedActorClass(self, ai: str) -> str:
        # TODO: Implement getExpandedActorClass method
        pass

    def getReferencedEnumClasses(self, cls: str) -> str:
        # TODO: Implement getReferencedEnumClasses method
        pass

    def getExpandedActorClass(self, ac: str) -> str:
        # TODO: Implement getExpandedActorClass method
        pass
