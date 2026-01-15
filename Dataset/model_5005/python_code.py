from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class SystemDiagramKind(Enum):
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"


############################################
# Definition of Classes
############################################

class CorbaObserver:

    pass
class ContextHandler:

    pass
class component_CorbaContextHandler(ContextHandler):

    pass
class ExecutionContext:

    pass
class ConfigurationSet:

    pass
class CorbaWrapperObject:

    pass
class component_CorbaExecutionContext(ExecutionContext, CorbaWrapperObject):

    def __init__(self, rtcExecutionContextProfile: str):
        self.rtcExecutionContextProfile = rtcExecutionContextProfile
        
    @property
    def rtcExecutionContextProfile(self) -> str:
        return self.__rtcExecutionContextProfile

    @rtcExecutionContextProfile.setter
    def rtcExecutionContextProfile(self, rtcExecutionContextProfile: str):
        self.__rtcExecutionContextProfile = rtcExecutionContextProfile

    def stopR(self) -> int:
        # TODO: Implement stopR method
        pass

    def deactivateR(self, comp: Component) -> int:
        # TODO: Implement deactivateR method
        pass

    def resetR(self, comp: Component) -> int:
        # TODO: Implement resetR method
        pass

    def activateR(self, comp: Component) -> int:
        # TODO: Implement activateR method
        pass

    def getComponentState(self, comp: Component) -> int:
        # TODO: Implement getComponentState method
        pass

    def startR(self) -> int:
        # TODO: Implement startR method
        pass

    def getComponentStateName(self, comp: Component) -> str:
        # TODO: Implement getComponentStateName method
        pass

class component_CorbaConfigurationSet(ConfigurationSet):

    def __init__(self, sDOConfigurationSet: str):
        self.sDOConfigurationSet = sDOConfigurationSet
        
    @property
    def sDOConfigurationSet(self) -> str:
        return self.__sDOConfigurationSet

    @sDOConfigurationSet.setter
    def sDOConfigurationSet(self, sDOConfigurationSet: str):
        self.__sDOConfigurationSet = sDOConfigurationSet

class ConnectorProfile:

    pass
class component_CorbaConnectorProfile(ConnectorProfile):

    def __init__(self, rtcConnectorProfile: str):
        self.rtcConnectorProfile = rtcConnectorProfile
        
    @property
    def rtcConnectorProfile(self) -> str:
        return self.__rtcConnectorProfile

    @rtcConnectorProfile.setter
    def rtcConnectorProfile(self, rtcConnectorProfile: str):
        self.__rtcConnectorProfile = rtcConnectorProfile

class PortSynchronizer:

    pass
class component_CorbaPortSynchronizer(PortSynchronizer, CorbaWrapperObject):

    def __init__(self, rTCPortProfile: str):
        self.rTCPortProfile = rTCPortProfile
        
    @property
    def rTCPortProfile(self) -> str:
        return self.__rTCPortProfile

    @rTCPortProfile.setter
    def rTCPortProfile(self, rTCPortProfile: str):
        self.__rTCPortProfile = rTCPortProfile

class component_CorbaLogObserver(CorbaObserver):

    pass
class component_CorbaStatusObserver(CorbaObserver):

    def __init__(self, component_CorbaStatusObserver: "component_CorbaComponent" = None):
        self.component_CorbaStatusObserver = component_CorbaStatusObserver
        
    @property
    def component_CorbaStatusObserver(self):
        return self.__component_CorbaStatusObserver

    @component_CorbaStatusObserver.setter
    def component_CorbaStatusObserver(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_CorbaStatusObserver__component_CorbaStatusObserver", None)
        self.__component_CorbaStatusObserver = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_CorbaComponent"):
                opp_val = getattr(old_value, "component_CorbaComponent", None)
                if opp_val == self:
                    setattr(old_value, "component_CorbaComponent", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_CorbaComponent"):
                opp_val = getattr(value, "component_CorbaComponent", None)
                setattr(value, "component_CorbaComponent", self)

    def isTimeOut(self) -> bool:
        # TODO: Implement isTimeOut method
        pass

class Port:

    pass
class component_EIntegerObjectToPointMapEntry:

    def __init__(self, key: str, value: str, component_EIntegerObjectToPointMapEntry: "component_PortConnector" = None):
        self.key = key
        self.value = value
        self.component_EIntegerObjectToPointMapEntry = component_EIntegerObjectToPointMapEntry
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def component_EIntegerObjectToPointMapEntry(self):
        return self.__component_EIntegerObjectToPointMapEntry

    @component_EIntegerObjectToPointMapEntry.setter
    def component_EIntegerObjectToPointMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_EIntegerObjectToPointMapEntry__component_EIntegerObjectToPointMapEntry", None)
        self.__component_EIntegerObjectToPointMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_PortConnector54"):
                opp_val = getattr(old_value, "component_PortConnector54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_PortConnector54"):
                opp_val = getattr(value, "component_PortConnector54", None)
                if opp_val is None:
                    setattr(value, "component_PortConnector54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class IAdaptable:

    pass
class component_IPropertyMap(IAdaptable):

    def __init__(self):
        
    def getProperty(self, key: str) -> str:
        # TODO: Implement getProperty method
        pass

    def getPropertyMap(self) -> IPropertyMap:
        # TODO: Implement getPropertyMap method
        pass

    def setProperty(self, key: str, value: str):
        # TODO: Implement setProperty method
        pass

    def getPropertyKeys(self) -> str:
        # TODO: Implement getPropertyKeys method
        pass

    def removeProperty(self, key: str) -> str:
        # TODO: Implement removeProperty method
        pass

class component_ContextHandler(IAdaptable):

    def __init__(self, component_ContextHandler: "component_Component" = None, component_ContextHandler35: "component_Component" = None):
        self.component_ContextHandler = component_ContextHandler
        self.component_ContextHandler35 = component_ContextHandler35
        
    @property
    def component_ContextHandler(self):
        return self.__component_ContextHandler

    @component_ContextHandler.setter
    def component_ContextHandler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_ContextHandler__component_ContextHandler", None)
        self.__component_ContextHandler = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_Component32"):
                opp_val = getattr(old_value, "component_Component32", None)
                if opp_val == self:
                    setattr(old_value, "component_Component32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_Component32"):
                opp_val = getattr(value, "component_Component32", None)
                setattr(value, "component_Component32", self)

    @property
    def component_ContextHandler35(self):
        return self.__component_ContextHandler35

    @component_ContextHandler35.setter
    def component_ContextHandler35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_ContextHandler__component_ContextHandler35", None)
        self.__component_ContextHandler35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_Component34"):
                opp_val = getattr(old_value, "component_Component34", None)
                if opp_val == self:
                    setattr(old_value, "component_Component34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_Component34"):
                opp_val = getattr(value, "component_Component34", None)
                setattr(value, "component_Component34", self)

    def sync(self):
        # TODO: Implement sync method
        pass

    def clear(self):
        # TODO: Implement clear method
        pass

    def keys(self) -> str:
        # TODO: Implement keys method
        pass

    def getContext(self, id: str) -> str:
        # TODO: Implement getContext method
        pass

    def values(self) -> str:
        # TODO: Implement values method
        pass

    def removeId(self, ec: str) -> str:
        # TODO: Implement removeId method
        pass

    def getId(self, ec: str) -> str:
        # TODO: Implement getId method
        pass

    def removeContext(self, id: str) -> str:
        # TODO: Implement removeContext method
        pass

    def getType(self) -> str:
        # TODO: Implement getType method
        pass

    def getOwnerContexts(self) -> str:
        # TODO: Implement getOwnerContexts method
        pass

    def setContext(self, ec: str, id: str) -> str:
        # TODO: Implement setContext method
        pass

class component_ServicePort(Port):

    pass
class component_OutPort(Port):

    pass
class Component:

    pass
class component_CorbaComponent(Component, CorbaWrapperObject):

    def __init__(self, ior: str, rTCComponentProfile: str, rTCExecutionContexts: str, rTCParticipationContexts: str, sDOConfiguration: str, sDOOrganization: str, rTCRTObjects: str, componentState: int, component_CorbaComponent: "component_CorbaStatusObserver" = None, component_CorbaComponent63: "component_CorbaLogObserver" = None):
        self.ior = ior
        self.rTCComponentProfile = rTCComponentProfile
        self.rTCExecutionContexts = rTCExecutionContexts
        self.rTCParticipationContexts = rTCParticipationContexts
        self.sDOConfiguration = sDOConfiguration
        self.sDOOrganization = sDOOrganization
        self.rTCRTObjects = rTCRTObjects
        self.componentState = componentState
        self.component_CorbaComponent = component_CorbaComponent
        self.component_CorbaComponent63 = component_CorbaComponent63
        
    @property
    def rTCComponentProfile(self) -> str:
        return self.__rTCComponentProfile

    @rTCComponentProfile.setter
    def rTCComponentProfile(self, rTCComponentProfile: str):
        self.__rTCComponentProfile = rTCComponentProfile

    @property
    def sDOOrganization(self) -> str:
        return self.__sDOOrganization

    @sDOOrganization.setter
    def sDOOrganization(self, sDOOrganization: str):
        self.__sDOOrganization = sDOOrganization

    @property
    def rTCRTObjects(self) -> str:
        return self.__rTCRTObjects

    @rTCRTObjects.setter
    def rTCRTObjects(self, rTCRTObjects: str):
        self.__rTCRTObjects = rTCRTObjects

    @property
    def componentState(self) -> int:
        return self.__componentState

    @componentState.setter
    def componentState(self, componentState: int):
        self.__componentState = componentState

    @property
    def sDOConfiguration(self) -> str:
        return self.__sDOConfiguration

    @sDOConfiguration.setter
    def sDOConfiguration(self, sDOConfiguration: str):
        self.__sDOConfiguration = sDOConfiguration

    @property
    def rTCParticipationContexts(self) -> str:
        return self.__rTCParticipationContexts

    @rTCParticipationContexts.setter
    def rTCParticipationContexts(self, rTCParticipationContexts: str):
        self.__rTCParticipationContexts = rTCParticipationContexts

    @property
    def rTCExecutionContexts(self) -> str:
        return self.__rTCExecutionContexts

    @rTCExecutionContexts.setter
    def rTCExecutionContexts(self, rTCExecutionContexts: str):
        self.__rTCExecutionContexts = rTCExecutionContexts

    @property
    def ior(self) -> str:
        return self.__ior

    @ior.setter
    def ior(self, ior: str):
        self.__ior = ior

    @property
    def component_CorbaComponent(self):
        return self.__component_CorbaComponent

    @component_CorbaComponent.setter
    def component_CorbaComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_CorbaComponent__component_CorbaComponent", None)
        self.__component_CorbaComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_CorbaStatusObserver"):
                opp_val = getattr(old_value, "component_CorbaStatusObserver", None)
                if opp_val == self:
                    setattr(old_value, "component_CorbaStatusObserver", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_CorbaStatusObserver"):
                opp_val = getattr(value, "component_CorbaStatusObserver", None)
                setattr(value, "component_CorbaStatusObserver", self)

    @property
    def component_CorbaComponent63(self):
        return self.__component_CorbaComponent63

    @component_CorbaComponent63.setter
    def component_CorbaComponent63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_CorbaComponent__component_CorbaComponent63", None)
        self.__component_CorbaComponent63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_CorbaLogObserver"):
                opp_val = getattr(old_value, "component_CorbaLogObserver", None)
                if opp_val == self:
                    setattr(old_value, "component_CorbaLogObserver", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_CorbaLogObserver"):
                opp_val = getattr(value, "component_CorbaLogObserver", None)
                setattr(value, "component_CorbaLogObserver", self)

    def detatchPortEventObserver(self, observer: str):
        # TODO: Implement detatchPortEventObserver method
        pass

    def stopAll(self):
        # TODO: Implement stopAll method
        pass

    def getExecutionContextState(self, ec: str) -> int:
        # TODO: Implement getExecutionContextState method
        pass

    def getComponentStateName(self) -> str:
        # TODO: Implement getComponentStateName method
        pass

    def deactivateR(self) -> int:
        # TODO: Implement deactivateR method
        pass

    def getExecutionContextState(self) -> int:
        # TODO: Implement getExecutionContextState method
        pass

    def startR(self) -> int:
        # TODO: Implement startR method
        pass

    def deactivateAll(self):
        # TODO: Implement deactivateAll method
        pass

    def attachPortEventObserver(self, observer: str):
        # TODO: Implement attachPortEventObserver method
        pass

    def activateAll(self):
        # TODO: Implement activateAll method
        pass

    def finalizeR(self) -> int:
        # TODO: Implement finalizeR method
        pass

    def getExecutionContextStateName(self) -> str:
        # TODO: Implement getExecutionContextStateName method
        pass

    def getExecutionContextStateName(self, ec: str) -> str:
        # TODO: Implement getExecutionContextStateName method
        pass

    def getCorbaObjectInterface(self) -> str:
        # TODO: Implement getCorbaObjectInterface method
        pass

    def stopR(self) -> int:
        # TODO: Implement stopR method
        pass

    def exitR(self) -> int:
        # TODO: Implement exitR method
        pass

    def activateR(self) -> int:
        # TODO: Implement activateR method
        pass

    def startAll(self):
        # TODO: Implement startAll method
        pass

    def resetR(self) -> int:
        # TODO: Implement resetR method
        pass

    def supportedCorbaObserver(self) -> bool:
        # TODO: Implement supportedCorbaObserver method
        pass

class component_ComponentSpecification(Component):

    def __init__(self, aliasName: str, specUnLoad: bool, rtcType: str):
        self.aliasName = aliasName
        self.specUnLoad = specUnLoad
        self.rtcType = rtcType
        
    @property
    def aliasName(self) -> str:
        return self.__aliasName

    @aliasName.setter
    def aliasName(self, aliasName: str):
        self.__aliasName = aliasName

    @property
    def specUnLoad(self) -> bool:
        return self.__specUnLoad

    @specUnLoad.setter
    def specUnLoad(self, specUnLoad: bool):
        self.__specUnLoad = specUnLoad

    @property
    def rtcType(self) -> str:
        return self.__rtcType

    @rtcType.setter
    def rtcType(self, rtcType: str):
        self.__rtcType = rtcType

class WrapperObject:

    pass
class component_PortConnector(WrapperObject):

    def __init__(self, component_PortConnector: "component_ConnectorProfile" = None, component_PortConnector54: set["component_EIntegerObjectToPointMapEntry"] = None, component_PortConnector56: "component_Port" = None, component_PortConnector59: "component_Port" = None):
        self.component_PortConnector = component_PortConnector
        self.component_PortConnector54 = component_PortConnector54 if component_PortConnector54 is not None else set()
        self.component_PortConnector56 = component_PortConnector56
        self.component_PortConnector59 = component_PortConnector59
        
    @property
    def component_PortConnector59(self):
        return self.__component_PortConnector59

    @component_PortConnector59.setter
    def component_PortConnector59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_PortConnector__component_PortConnector59", None)
        self.__component_PortConnector59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_Port60"):
                opp_val = getattr(old_value, "component_Port60", None)
                if opp_val == self:
                    setattr(old_value, "component_Port60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_Port60"):
                opp_val = getattr(value, "component_Port60", None)
                setattr(value, "component_Port60", self)

    @property
    def component_PortConnector54(self):
        return self.__component_PortConnector54

    @component_PortConnector54.setter
    def component_PortConnector54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_PortConnector__component_PortConnector54", None)
        self.__component_PortConnector54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "component_EIntegerObjectToPointMapEntry"):
                    opp_val = getattr(item, "component_EIntegerObjectToPointMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "component_EIntegerObjectToPointMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "component_EIntegerObjectToPointMapEntry"):
                    opp_val = getattr(item, "component_EIntegerObjectToPointMapEntry", None)
                    
                    setattr(item, "component_EIntegerObjectToPointMapEntry", self)
                    

    @property
    def component_PortConnector(self):
        return self.__component_PortConnector

    @component_PortConnector.setter
    def component_PortConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_PortConnector__component_PortConnector", None)
        self.__component_PortConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_ConnectorProfile52"):
                opp_val = getattr(old_value, "component_ConnectorProfile52", None)
                if opp_val == self:
                    setattr(old_value, "component_ConnectorProfile52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_ConnectorProfile52"):
                opp_val = getattr(value, "component_ConnectorProfile52", None)
                setattr(value, "component_ConnectorProfile52", self)

    @property
    def component_PortConnector56(self):
        return self.__component_PortConnector56

    @component_PortConnector56.setter
    def component_PortConnector56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_PortConnector__component_PortConnector56", None)
        self.__component_PortConnector56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_Port57"):
                opp_val = getattr(old_value, "component_Port57", None)
                if opp_val == self:
                    setattr(old_value, "component_Port57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_Port57"):
                opp_val = getattr(value, "component_Port57", None)
                setattr(value, "component_Port57", self)

    def createConnectorR(self) -> bool:
        # TODO: Implement createConnectorR method
        pass

    def deleteConnectorR(self) -> bool:
        # TODO: Implement deleteConnectorR method
        pass

class component_NameValue(WrapperObject):

    def __init__(self, name: str, value: str, typeName: str, component_NameValue: "component_ConfigurationSet" = None):
        self.name = name
        self.value = value
        self.typeName = typeName
        self.component_NameValue = component_NameValue
        
    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def component_NameValue(self):
        return self.__component_NameValue

    @component_NameValue.setter
    def component_NameValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_NameValue__component_NameValue", None)
        self.__component_NameValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_ConfigurationSet46"):
                opp_val = getattr(old_value, "component_ConfigurationSet46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_ConfigurationSet46"):
                opp_val = getattr(value, "component_ConfigurationSet46", None)
                if opp_val is None:
                    setattr(value, "component_ConfigurationSet46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class component_InPort(Port):

    pass
class component_Port(WrapperObject):

    def __init__(self, originalPortString: str, nameL: str, allowAnyDataType: bool, allowAnyInterfaceType: bool, allowAnyDataflowType: bool, allowAnySubscriptionType: bool, interfaces: str, dataflowType: str, subscriptionType: str, dataType: str, interfaceType: str, component_Port: "component_Component" = None, component_Port57: "component_PortConnector" = None, component_Port60: "component_PortConnector" = None, component_Port48: "component_PortSynchronizer" = None, component_Port50: set["component_ConnectorProfile"] = None):
        self.originalPortString = originalPortString
        self.nameL = nameL
        self.allowAnyDataType = allowAnyDataType
        self.allowAnyInterfaceType = allowAnyInterfaceType
        self.allowAnyDataflowType = allowAnyDataflowType
        self.allowAnySubscriptionType = allowAnySubscriptionType
        self.interfaces = interfaces
        self.dataflowType = dataflowType
        self.subscriptionType = subscriptionType
        self.dataType = dataType
        self.interfaceType = interfaceType
        self.component_Port = component_Port
        self.component_Port57 = component_Port57
        self.component_Port60 = component_Port60
        self.component_Port48 = component_Port48
        self.component_Port50 = component_Port50 if component_Port50 is not None else set()
        
    @property
    def subscriptionType(self) -> str:
        return self.__subscriptionType

    @subscriptionType.setter
    def subscriptionType(self, subscriptionType: str):
        self.__subscriptionType = subscriptionType

    @property
    def interfaceType(self) -> str:
        return self.__interfaceType

    @interfaceType.setter
    def interfaceType(self, interfaceType: str):
        self.__interfaceType = interfaceType

    @property
    def interfaces(self) -> str:
        return self.__interfaces

    @interfaces.setter
    def interfaces(self, interfaces: str):
        self.__interfaces = interfaces

    @property
    def allowAnyDataflowType(self) -> bool:
        return self.__allowAnyDataflowType

    @allowAnyDataflowType.setter
    def allowAnyDataflowType(self, allowAnyDataflowType: bool):
        self.__allowAnyDataflowType = allowAnyDataflowType

    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

    @property
    def dataflowType(self) -> str:
        return self.__dataflowType

    @dataflowType.setter
    def dataflowType(self, dataflowType: str):
        self.__dataflowType = dataflowType

    @property
    def allowAnyDataType(self) -> bool:
        return self.__allowAnyDataType

    @allowAnyDataType.setter
    def allowAnyDataType(self, allowAnyDataType: bool):
        self.__allowAnyDataType = allowAnyDataType

    @property
    def nameL(self) -> str:
        return self.__nameL

    @nameL.setter
    def nameL(self, nameL: str):
        self.__nameL = nameL

    @property
    def allowAnyInterfaceType(self) -> bool:
        return self.__allowAnyInterfaceType

    @allowAnyInterfaceType.setter
    def allowAnyInterfaceType(self, allowAnyInterfaceType: bool):
        self.__allowAnyInterfaceType = allowAnyInterfaceType

    @property
    def allowAnySubscriptionType(self) -> bool:
        return self.__allowAnySubscriptionType

    @allowAnySubscriptionType.setter
    def allowAnySubscriptionType(self, allowAnySubscriptionType: bool):
        self.__allowAnySubscriptionType = allowAnySubscriptionType

    @property
    def originalPortString(self) -> str:
        return self.__originalPortString

    @originalPortString.setter
    def originalPortString(self, originalPortString: str):
        self.__originalPortString = originalPortString

    @property
    def component_Port60(self):
        return self.__component_Port60

    @component_Port60.setter
    def component_Port60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_Port__component_Port60", None)
        self.__component_Port60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_PortConnector59"):
                opp_val = getattr(old_value, "component_PortConnector59", None)
                if opp_val == self:
                    setattr(old_value, "component_PortConnector59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_PortConnector59"):
                opp_val = getattr(value, "component_PortConnector59", None)
                setattr(value, "component_PortConnector59", self)

    @property
    def component_Port50(self):
        return self.__component_Port50

    @component_Port50.setter
    def component_Port50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_Port__component_Port50", None)
        self.__component_Port50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "component_ConnectorProfile"):
                    opp_val = getattr(item, "component_ConnectorProfile", None)
                    
                    if opp_val == self:
                        setattr(item, "component_ConnectorProfile", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "component_ConnectorProfile"):
                    opp_val = getattr(item, "component_ConnectorProfile", None)
                    
                    setattr(item, "component_ConnectorProfile", self)
                    

    @property
    def component_Port48(self):
        return self.__component_Port48

    @component_Port48.setter
    def component_Port48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_Port__component_Port48", None)
        self.__component_Port48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_PortSynchronizer"):
                opp_val = getattr(old_value, "component_PortSynchronizer", None)
                if opp_val == self:
                    setattr(old_value, "component_PortSynchronizer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_PortSynchronizer"):
                opp_val = getattr(value, "component_PortSynchronizer", None)
                setattr(value, "component_PortSynchronizer", self)

    @property
    def component_Port(self):
        return self.__component_Port

    @component_Port.setter
    def component_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_Port__component_Port", None)
        self.__component_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_Component13"):
                opp_val = getattr(old_value, "component_Component13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_Component13"):
                opp_val = getattr(value, "component_Component13", None)
                if opp_val is None:
                    setattr(value, "component_Component13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def component_Port57(self):
        return self.__component_Port57

    @component_Port57.setter
    def component_Port57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_Port__component_Port57", None)
        self.__component_Port57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_PortConnector56"):
                opp_val = getattr(old_value, "component_PortConnector56", None)
                if opp_val == self:
                    setattr(old_value, "component_PortConnector56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_PortConnector56"):
                opp_val = getattr(value, "component_PortConnector56", None)
                setattr(value, "component_PortConnector56", self)

    def findPort(self, originalPortString: str, diagram: str) -> str:
        # TODO: Implement findPort method
        pass

    def validateSourceConnector(self, source: str) -> bool:
        # TODO: Implement validateSourceConnector method
        pass

    def validateTargetConnector(self, target: str) -> bool:
        # TODO: Implement validateTargetConnector method
        pass

    def disconnectAll(self):
        # TODO: Implement disconnectAll method
        pass

class component_ConfigurationSet(WrapperObject):

    def __init__(self, id: str, component_ConfigurationSet: "component_Component" = None, component_ConfigurationSet11: "component_Component" = None, component_ConfigurationSet46: set["component_NameValue"] = None):
        self.id = id
        self.component_ConfigurationSet = component_ConfigurationSet
        self.component_ConfigurationSet11 = component_ConfigurationSet11
        self.component_ConfigurationSet46 = component_ConfigurationSet46 if component_ConfigurationSet46 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def component_ConfigurationSet46(self):
        return self.__component_ConfigurationSet46

    @component_ConfigurationSet46.setter
    def component_ConfigurationSet46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_ConfigurationSet__component_ConfigurationSet46", None)
        self.__component_ConfigurationSet46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "component_NameValue"):
                    opp_val = getattr(item, "component_NameValue", None)
                    
                    if opp_val == self:
                        setattr(item, "component_NameValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "component_NameValue"):
                    opp_val = getattr(item, "component_NameValue", None)
                    
                    setattr(item, "component_NameValue", self)
                    

    @property
    def component_ConfigurationSet(self):
        return self.__component_ConfigurationSet

    @component_ConfigurationSet.setter
    def component_ConfigurationSet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_ConfigurationSet__component_ConfigurationSet", None)
        self.__component_ConfigurationSet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_Component8"):
                opp_val = getattr(old_value, "component_Component8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_Component8"):
                opp_val = getattr(value, "component_Component8", None)
                if opp_val is None:
                    setattr(value, "component_Component8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def component_ConfigurationSet11(self):
        return self.__component_ConfigurationSet11

    @component_ConfigurationSet11.setter
    def component_ConfigurationSet11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_ConfigurationSet__component_ConfigurationSet11", None)
        self.__component_ConfigurationSet11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_Component10"):
                opp_val = getattr(old_value, "component_Component10", None)
                if opp_val == self:
                    setattr(old_value, "component_Component10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_Component10"):
                opp_val = getattr(value, "component_Component10", None)
                setattr(value, "component_Component10", self)

class IPropertyMap:

    pass
class component_ExecutionContext(WrapperObject, IPropertyMap):

    def __init__(self, kindL: int, rateL: str, stateL: int, component_ExecutionContext: "component_Component" = None, component_ExecutionContext27: "component_Component" = None, component_ExecutionContext30: "component_Component" = None, component_ExecutionContext40: "component_Component" = None, component_ExecutionContext43: set["component_Component"] = None):
        self.kindL = kindL
        self.rateL = rateL
        self.stateL = stateL
        self.component_ExecutionContext = component_ExecutionContext
        self.component_ExecutionContext27 = component_ExecutionContext27
        self.component_ExecutionContext30 = component_ExecutionContext30
        self.component_ExecutionContext40 = component_ExecutionContext40
        self.component_ExecutionContext43 = component_ExecutionContext43 if component_ExecutionContext43 is not None else set()
        
    @property
    def rateL(self) -> str:
        return self.__rateL

    @rateL.setter
    def rateL(self, rateL: str):
        self.__rateL = rateL

    @property
    def stateL(self) -> int:
        return self.__stateL

    @stateL.setter
    def stateL(self, stateL: int):
        self.__stateL = stateL

    @property
    def kindL(self) -> int:
        return self.__kindL

    @kindL.setter
    def kindL(self, kindL: int):
        self.__kindL = kindL

    @property
    def component_ExecutionContext(self):
        return self.__component_ExecutionContext

    @component_ExecutionContext.setter
    def component_ExecutionContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_ExecutionContext__component_ExecutionContext", None)
        self.__component_ExecutionContext = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_Component24"):
                opp_val = getattr(old_value, "component_Component24", None)
                if opp_val == self:
                    setattr(old_value, "component_Component24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_Component24"):
                opp_val = getattr(value, "component_Component24", None)
                setattr(value, "component_Component24", self)

    @property
    def component_ExecutionContext43(self):
        return self.__component_ExecutionContext43

    @component_ExecutionContext43.setter
    def component_ExecutionContext43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_ExecutionContext__component_ExecutionContext43", None)
        self.__component_ExecutionContext43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "component_Component44"):
                    opp_val = getattr(item, "component_Component44", None)
                    
                    if opp_val == self:
                        setattr(item, "component_Component44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "component_Component44"):
                    opp_val = getattr(item, "component_Component44", None)
                    
                    setattr(item, "component_Component44", self)
                    

    @property
    def component_ExecutionContext40(self):
        return self.__component_ExecutionContext40

    @component_ExecutionContext40.setter
    def component_ExecutionContext40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_ExecutionContext__component_ExecutionContext40", None)
        self.__component_ExecutionContext40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_Component41"):
                opp_val = getattr(old_value, "component_Component41", None)
                if opp_val == self:
                    setattr(old_value, "component_Component41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_Component41"):
                opp_val = getattr(value, "component_Component41", None)
                setattr(value, "component_Component41", self)

    @property
    def component_ExecutionContext27(self):
        return self.__component_ExecutionContext27

    @component_ExecutionContext27.setter
    def component_ExecutionContext27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_ExecutionContext__component_ExecutionContext27", None)
        self.__component_ExecutionContext27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_Component26"):
                opp_val = getattr(old_value, "component_Component26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_Component26"):
                opp_val = getattr(value, "component_Component26", None)
                if opp_val is None:
                    setattr(value, "component_Component26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def component_ExecutionContext30(self):
        return self.__component_ExecutionContext30

    @component_ExecutionContext30.setter
    def component_ExecutionContext30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_ExecutionContext__component_ExecutionContext30", None)
        self.__component_ExecutionContext30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_Component29"):
                opp_val = getattr(old_value, "component_Component29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_Component29"):
                opp_val = getattr(value, "component_Component29", None)
                if opp_val is None:
                    setattr(value, "component_Component29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getId(self) -> str:
        # TODO: Implement getId method
        pass

    def getKindName(self) -> str:
        # TODO: Implement getKindName method
        pass

    def setRateR(self, rate: str) -> bool:
        # TODO: Implement setRateR method
        pass

    def addComponentR(self, comp: Component) -> bool:
        # TODO: Implement addComponentR method
        pass

    def removeComponentR(self, comp: Component) -> bool:
        # TODO: Implement removeComponentR method
        pass

    def getStateName(self) -> str:
        # TODO: Implement getStateName method
        pass

    def containsComponent(self, comp: Component) -> bool:
        # TODO: Implement containsComponent method
        pass

    def isOwner(self, comp: Component) -> bool:
        # TODO: Implement isOwner method
        pass

class component_PortSynchronizer(IPropertyMap):

    def __init__(self, originalPortString: str, component_PortSynchronizer: "component_Port" = None):
        self.originalPortString = originalPortString
        self.component_PortSynchronizer = component_PortSynchronizer
        
    @property
    def originalPortString(self) -> str:
        return self.__originalPortString

    @originalPortString.setter
    def originalPortString(self, originalPortString: str):
        self.__originalPortString = originalPortString

    @property
    def component_PortSynchronizer(self):
        return self.__component_PortSynchronizer

    @component_PortSynchronizer.setter
    def component_PortSynchronizer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_PortSynchronizer__component_PortSynchronizer", None)
        self.__component_PortSynchronizer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_Port48"):
                opp_val = getattr(old_value, "component_Port48", None)
                if opp_val == self:
                    setattr(old_value, "component_Port48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_Port48"):
                opp_val = getattr(value, "component_Port48", None)
                setattr(value, "component_Port48", self)

    def disconnect(self, conn_id: str) -> bool:
        # TODO: Implement disconnect method
        pass

    def disconnect(self, conn_prof: str) -> bool:
        # TODO: Implement disconnect method
        pass

    def disconnectAll(self) -> bool:
        # TODO: Implement disconnectAll method
        pass

class component_ConnectorProfile(WrapperObject, IPropertyMap):

    def __init__(self, dataflowType: str, subscriptionType: str, subscriptionTypeAvailable: bool, pushIntervalAvailable: bool, name: str, connectorId: str, dataType: str, interfaceType: str, pushRate: str, pushPolicy: str, skipCount: str, pushPolicyAvailable: bool, skipCountAvailable: bool, sourceString: str, targetString: str, outportBufferLength: str, outportBufferFullPolicy: str, outportBufferWriteTimeout: str, outportBufferEmptyPolicy: str, outportBufferReadTimeout: str, inportBufferLength: str, inportBufferFullPolicy: str, inportBufferWriteTimeout: str, inportBufferEmptyPolicy: str, inportBufferReadTimeout: str, timestampPolicy: str, isReverse: bool, outportSerializerType: str, inportSerializerType: str, component_ConnectorProfile52: "component_PortConnector" = None, component_ConnectorProfile: "component_Port" = None):
        self.dataflowType = dataflowType
        self.subscriptionType = subscriptionType
        self.subscriptionTypeAvailable = subscriptionTypeAvailable
        self.pushIntervalAvailable = pushIntervalAvailable
        self.name = name
        self.connectorId = connectorId
        self.dataType = dataType
        self.interfaceType = interfaceType
        self.pushRate = pushRate
        self.pushPolicy = pushPolicy
        self.skipCount = skipCount
        self.pushPolicyAvailable = pushPolicyAvailable
        self.skipCountAvailable = skipCountAvailable
        self.sourceString = sourceString
        self.targetString = targetString
        self.outportBufferLength = outportBufferLength
        self.outportBufferFullPolicy = outportBufferFullPolicy
        self.outportBufferWriteTimeout = outportBufferWriteTimeout
        self.outportBufferEmptyPolicy = outportBufferEmptyPolicy
        self.outportBufferReadTimeout = outportBufferReadTimeout
        self.inportBufferLength = inportBufferLength
        self.inportBufferFullPolicy = inportBufferFullPolicy
        self.inportBufferWriteTimeout = inportBufferWriteTimeout
        self.inportBufferEmptyPolicy = inportBufferEmptyPolicy
        self.inportBufferReadTimeout = inportBufferReadTimeout
        self.timestampPolicy = timestampPolicy
        self.isReverse = isReverse
        self.outportSerializerType = outportSerializerType
        self.inportSerializerType = inportSerializerType
        self.component_ConnectorProfile52 = component_ConnectorProfile52
        self.component_ConnectorProfile = component_ConnectorProfile
        
    @property
    def inportBufferLength(self) -> str:
        return self.__inportBufferLength

    @inportBufferLength.setter
    def inportBufferLength(self, inportBufferLength: str):
        self.__inportBufferLength = inportBufferLength

    @property
    def connectorId(self) -> str:
        return self.__connectorId

    @connectorId.setter
    def connectorId(self, connectorId: str):
        self.__connectorId = connectorId

    @property
    def outportBufferReadTimeout(self) -> str:
        return self.__outportBufferReadTimeout

    @outportBufferReadTimeout.setter
    def outportBufferReadTimeout(self, outportBufferReadTimeout: str):
        self.__outportBufferReadTimeout = outportBufferReadTimeout

    @property
    def inportBufferReadTimeout(self) -> str:
        return self.__inportBufferReadTimeout

    @inportBufferReadTimeout.setter
    def inportBufferReadTimeout(self, inportBufferReadTimeout: str):
        self.__inportBufferReadTimeout = inportBufferReadTimeout

    @property
    def skipCountAvailable(self) -> bool:
        return self.__skipCountAvailable

    @skipCountAvailable.setter
    def skipCountAvailable(self, skipCountAvailable: bool):
        self.__skipCountAvailable = skipCountAvailable

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def skipCount(self) -> str:
        return self.__skipCount

    @skipCount.setter
    def skipCount(self, skipCount: str):
        self.__skipCount = skipCount

    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

    @property
    def interfaceType(self) -> str:
        return self.__interfaceType

    @interfaceType.setter
    def interfaceType(self, interfaceType: str):
        self.__interfaceType = interfaceType

    @property
    def pushRate(self) -> str:
        return self.__pushRate

    @pushRate.setter
    def pushRate(self, pushRate: str):
        self.__pushRate = pushRate

    @property
    def targetString(self) -> str:
        return self.__targetString

    @targetString.setter
    def targetString(self, targetString: str):
        self.__targetString = targetString

    @property
    def inportBufferWriteTimeout(self) -> str:
        return self.__inportBufferWriteTimeout

    @inportBufferWriteTimeout.setter
    def inportBufferWriteTimeout(self, inportBufferWriteTimeout: str):
        self.__inportBufferWriteTimeout = inportBufferWriteTimeout

    @property
    def isReverse(self) -> bool:
        return self.__isReverse

    @isReverse.setter
    def isReverse(self, isReverse: bool):
        self.__isReverse = isReverse

    @property
    def outportBufferLength(self) -> str:
        return self.__outportBufferLength

    @outportBufferLength.setter
    def outportBufferLength(self, outportBufferLength: str):
        self.__outportBufferLength = outportBufferLength

    @property
    def sourceString(self) -> str:
        return self.__sourceString

    @sourceString.setter
    def sourceString(self, sourceString: str):
        self.__sourceString = sourceString

    @property
    def inportBufferFullPolicy(self) -> str:
        return self.__inportBufferFullPolicy

    @inportBufferFullPolicy.setter
    def inportBufferFullPolicy(self, inportBufferFullPolicy: str):
        self.__inportBufferFullPolicy = inportBufferFullPolicy

    @property
    def inportSerializerType(self) -> str:
        return self.__inportSerializerType

    @inportSerializerType.setter
    def inportSerializerType(self, inportSerializerType: str):
        self.__inportSerializerType = inportSerializerType

    @property
    def outportBufferFullPolicy(self) -> str:
        return self.__outportBufferFullPolicy

    @outportBufferFullPolicy.setter
    def outportBufferFullPolicy(self, outportBufferFullPolicy: str):
        self.__outportBufferFullPolicy = outportBufferFullPolicy

    @property
    def pushPolicy(self) -> str:
        return self.__pushPolicy

    @pushPolicy.setter
    def pushPolicy(self, pushPolicy: str):
        self.__pushPolicy = pushPolicy

    @property
    def inportBufferEmptyPolicy(self) -> str:
        return self.__inportBufferEmptyPolicy

    @inportBufferEmptyPolicy.setter
    def inportBufferEmptyPolicy(self, inportBufferEmptyPolicy: str):
        self.__inportBufferEmptyPolicy = inportBufferEmptyPolicy

    @property
    def pushPolicyAvailable(self) -> bool:
        return self.__pushPolicyAvailable

    @pushPolicyAvailable.setter
    def pushPolicyAvailable(self, pushPolicyAvailable: bool):
        self.__pushPolicyAvailable = pushPolicyAvailable

    @property
    def subscriptionTypeAvailable(self) -> bool:
        return self.__subscriptionTypeAvailable

    @subscriptionTypeAvailable.setter
    def subscriptionTypeAvailable(self, subscriptionTypeAvailable: bool):
        self.__subscriptionTypeAvailable = subscriptionTypeAvailable

    @property
    def pushIntervalAvailable(self) -> bool:
        return self.__pushIntervalAvailable

    @pushIntervalAvailable.setter
    def pushIntervalAvailable(self, pushIntervalAvailable: bool):
        self.__pushIntervalAvailable = pushIntervalAvailable

    @property
    def outportBufferEmptyPolicy(self) -> str:
        return self.__outportBufferEmptyPolicy

    @outportBufferEmptyPolicy.setter
    def outportBufferEmptyPolicy(self, outportBufferEmptyPolicy: str):
        self.__outportBufferEmptyPolicy = outportBufferEmptyPolicy

    @property
    def timestampPolicy(self) -> str:
        return self.__timestampPolicy

    @timestampPolicy.setter
    def timestampPolicy(self, timestampPolicy: str):
        self.__timestampPolicy = timestampPolicy

    @property
    def outportBufferWriteTimeout(self) -> str:
        return self.__outportBufferWriteTimeout

    @outportBufferWriteTimeout.setter
    def outportBufferWriteTimeout(self, outportBufferWriteTimeout: str):
        self.__outportBufferWriteTimeout = outportBufferWriteTimeout

    @property
    def subscriptionType(self) -> str:
        return self.__subscriptionType

    @subscriptionType.setter
    def subscriptionType(self, subscriptionType: str):
        self.__subscriptionType = subscriptionType

    @property
    def outportSerializerType(self) -> str:
        return self.__outportSerializerType

    @outportSerializerType.setter
    def outportSerializerType(self, outportSerializerType: str):
        self.__outportSerializerType = outportSerializerType

    @property
    def dataflowType(self) -> str:
        return self.__dataflowType

    @dataflowType.setter
    def dataflowType(self, dataflowType: str):
        self.__dataflowType = dataflowType

    @property
    def component_ConnectorProfile(self):
        return self.__component_ConnectorProfile

    @component_ConnectorProfile.setter
    def component_ConnectorProfile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_ConnectorProfile__component_ConnectorProfile", None)
        self.__component_ConnectorProfile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_Port50"):
                opp_val = getattr(old_value, "component_Port50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_Port50"):
                opp_val = getattr(value, "component_Port50", None)
                if opp_val is None:
                    setattr(value, "component_Port50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def component_ConnectorProfile52(self):
        return self.__component_ConnectorProfile52

    @component_ConnectorProfile52.setter
    def component_ConnectorProfile52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_ConnectorProfile__component_ConnectorProfile52", None)
        self.__component_ConnectorProfile52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_PortConnector"):
                opp_val = getattr(old_value, "component_PortConnector", None)
                if opp_val == self:
                    setattr(old_value, "component_PortConnector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_PortConnector"):
                opp_val = getattr(value, "component_PortConnector", None)
                setattr(value, "component_PortConnector", self)

class component_CorbaObserver(IPropertyMap, IAdaptable):

    def __init__(self, serviceProfile: str, servant: str):
        self.serviceProfile = serviceProfile
        self.servant = servant
        
    @property
    def servant(self) -> str:
        return self.__servant

    @servant.setter
    def servant(self, servant: str):
        self.__servant = servant

    @property
    def serviceProfile(self) -> str:
        return self.__serviceProfile

    @serviceProfile.setter
    def serviceProfile(self, serviceProfile: str):
        self.__serviceProfile = serviceProfile

    def finish(self) -> bool:
        # TODO: Implement finish method
        pass

    def detachComponent(self) -> bool:
        # TODO: Implement detachComponent method
        pass

    def attachComponent(self, component: str) -> bool:
        # TODO: Implement attachComponent method
        pass

    def activate(self):
        # TODO: Implement activate method
        pass

    def deactivate(self):
        # TODO: Implement deactivate method
        pass

class component_Component(WrapperObject, IPropertyMap):

    def __init__(self, shutDown: str, activation: str, deActivation: str, resetting: str, initialize: str, finalize: str, instanceNameL: str, venderL: str, descriptionL: str, categoryL: str, typeNameL: str, versionL: str, pathId: str, outportDirection: str, compositeTypeL: str, componentId: str, required: bool, startUp: str, component_Component8: set["component_ConfigurationSet"] = None, component_Component10: "component_ConfigurationSet" = None, component_Component13: set["component_Port"] = None, component_Component15: set["component_InPort"] = None, component_Component: "component_SystemDiagram" = None, component_Component6: "component_SystemDiagram" = None, component_Component17: set["component_OutPort"] = None, component_Component19: set["component_ServicePort"] = None, component_Component22: "component_Component" = None, component_Component20: set["component_Component"] = None, component_Component24: "component_ExecutionContext" = None, component_Component26: set["component_ExecutionContext"] = None, component_Component29: set["component_ExecutionContext"] = None, component_Component32: "component_ContextHandler" = None, component_Component34: "component_ContextHandler" = None, component_Component37: "component_SystemDiagram" = None, component_Component41: "component_ExecutionContext" = None, component_Component44: "component_ExecutionContext" = None):
        self.shutDown = shutDown
        self.activation = activation
        self.deActivation = deActivation
        self.resetting = resetting
        self.initialize = initialize
        self.finalize = finalize
        self.instanceNameL = instanceNameL
        self.venderL = venderL
        self.descriptionL = descriptionL
        self.categoryL = categoryL
        self.typeNameL = typeNameL
        self.versionL = versionL
        self.pathId = pathId
        self.outportDirection = outportDirection
        self.compositeTypeL = compositeTypeL
        self.componentId = componentId
        self.required = required
        self.startUp = startUp
        self.component_Component8 = component_Component8 if component_Component8 is not None else set()
        self.component_Component10 = component_Component10
        self.component_Component13 = component_Component13 if component_Component13 is not None else set()
        self.component_Component15 = component_Component15 if component_Component15 is not None else set()
        self.component_Component = component_Component
        self.component_Component6 = component_Component6
        self.component_Component17 = component_Component17 if component_Component17 is not None else set()
        self.component_Component19 = component_Component19 if component_Component19 is not None else set()
        self.component_Component22 = component_Component22
        self.component_Component20 = component_Component20 if component_Component20 is not None else set()
        self.component_Component24 = component_Component24
        self.component_Component26 = component_Component26 if component_Component26 is not None else set()
        self.component_Component29 = component_Component29 if component_Component29 is not None else set()
        self.component_Component32 = component_Component32
        self.component_Component34 = component_Component34
        self.component_Component37 = component_Component37
        self.component_Component41 = component_Component41
        self.component_Component44 = component_Component44
        
    @property
    def componentId(self) -> str:
        return self.__componentId

    @componentId.setter
    def componentId(self, componentId: str):
        self.__componentId = componentId

    @property
    def typeNameL(self) -> str:
        return self.__typeNameL

    @typeNameL.setter
    def typeNameL(self, typeNameL: str):
        self.__typeNameL = typeNameL

    @property
    def pathId(self) -> str:
        return self.__pathId

    @pathId.setter
    def pathId(self, pathId: str):
        self.__pathId = pathId

    @property
    def deActivation(self) -> str:
        return self.__deActivation

    @deActivation.setter
    def deActivation(self, deActivation: str):
        self.__deActivation = deActivation

    @property
    def instanceNameL(self) -> str:
        return self.__instanceNameL

    @instanceNameL.setter
    def instanceNameL(self, instanceNameL: str):
        self.__instanceNameL = instanceNameL

    @property
    def startUp(self) -> str:
        return self.__startUp

    @startUp.setter
    def startUp(self, startUp: str):
        self.__startUp = startUp

    @property
    def outportDirection(self) -> str:
        return self.__outportDirection

    @outportDirection.setter
    def outportDirection(self, outportDirection: str):
        self.__outportDirection = outportDirection

    @property
    def categoryL(self) -> str:
        return self.__categoryL

    @categoryL.setter
    def categoryL(self, categoryL: str):
        self.__categoryL = categoryL

    @property
    def activation(self) -> str:
        return self.__activation

    @activation.setter
    def activation(self, activation: str):
        self.__activation = activation

    @property
    def initialize(self) -> str:
        return self.__initialize

    @initialize.setter
    def initialize(self, initialize: str):
        self.__initialize = initialize

    @property
    def compositeTypeL(self) -> str:
        return self.__compositeTypeL

    @compositeTypeL.setter
    def compositeTypeL(self, compositeTypeL: str):
        self.__compositeTypeL = compositeTypeL

    @property
    def required(self) -> bool:
        return self.__required

    @required.setter
    def required(self, required: bool):
        self.__required = required

    @property
    def resetting(self) -> str:
        return self.__resetting

    @resetting.setter
    def resetting(self, resetting: str):
        self.__resetting = resetting

    @property
    def venderL(self) -> str:
        return self.__venderL

    @venderL.setter
    def venderL(self, venderL: str):
        self.__venderL = venderL

    @property
    def finalize(self) -> str:
        return self.__finalize

    @finalize.setter
    def finalize(self, finalize: str):
        self.__finalize = finalize

    @property
    def shutDown(self) -> str:
        return self.__shutDown

    @shutDown.setter
    def shutDown(self, shutDown: str):
        self.__shutDown = shutDown

    @property
    def versionL(self) -> str:
        return self.__versionL

    @versionL.setter
    def versionL(self, versionL: str):
        self.__versionL = versionL

    @property
    def descriptionL(self) -> str:
        return self.__descriptionL

    @descriptionL.setter
    def descriptionL(self, descriptionL: str):
        self.__descriptionL = descriptionL

    @property
    def component_Component32(self):
        return self.__component_Component32

    @component_Component32.setter
    def component_Component32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_Component__component_Component32", None)
        self.__component_Component32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_ContextHandler"):
                opp_val = getattr(old_value, "component_ContextHandler", None)
                if opp_val == self:
                    setattr(old_value, "component_ContextHandler", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_ContextHandler"):
                opp_val = getattr(value, "component_ContextHandler", None)
                setattr(value, "component_ContextHandler", self)

    @property
    def component_Component15(self):
        return self.__component_Component15

    @component_Component15.setter
    def component_Component15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_Component__component_Component15", None)
        self.__component_Component15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "component_InPort"):
                    opp_val = getattr(item, "component_InPort", None)
                    
                    if opp_val == self:
                        setattr(item, "component_InPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "component_InPort"):
                    opp_val = getattr(item, "component_InPort", None)
                    
                    setattr(item, "component_InPort", self)
                    

    @property
    def component_Component13(self):
        return self.__component_Component13

    @component_Component13.setter
    def component_Component13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_Component__component_Component13", None)
        self.__component_Component13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "component_Port"):
                    opp_val = getattr(item, "component_Port", None)
                    
                    if opp_val == self:
                        setattr(item, "component_Port", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "component_Port"):
                    opp_val = getattr(item, "component_Port", None)
                    
                    setattr(item, "component_Port", self)
                    

    @property
    def component_Component6(self):
        return self.__component_Component6

    @component_Component6.setter
    def component_Component6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_Component__component_Component6", None)
        self.__component_Component6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_SystemDiagram5"):
                opp_val = getattr(old_value, "component_SystemDiagram5", None)
                if opp_val == self:
                    setattr(old_value, "component_SystemDiagram5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_SystemDiagram5"):
                opp_val = getattr(value, "component_SystemDiagram5", None)
                setattr(value, "component_SystemDiagram5", self)

    @property
    def component_Component44(self):
        return self.__component_Component44

    @component_Component44.setter
    def component_Component44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_Component__component_Component44", None)
        self.__component_Component44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_ExecutionContext43"):
                opp_val = getattr(old_value, "component_ExecutionContext43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_ExecutionContext43"):
                opp_val = getattr(value, "component_ExecutionContext43", None)
                if opp_val is None:
                    setattr(value, "component_ExecutionContext43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def component_Component26(self):
        return self.__component_Component26

    @component_Component26.setter
    def component_Component26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_Component__component_Component26", None)
        self.__component_Component26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "component_ExecutionContext27"):
                    opp_val = getattr(item, "component_ExecutionContext27", None)
                    
                    if opp_val == self:
                        setattr(item, "component_ExecutionContext27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "component_ExecutionContext27"):
                    opp_val = getattr(item, "component_ExecutionContext27", None)
                    
                    setattr(item, "component_ExecutionContext27", self)
                    

    @property
    def component_Component10(self):
        return self.__component_Component10

    @component_Component10.setter
    def component_Component10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_Component__component_Component10", None)
        self.__component_Component10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_ConfigurationSet11"):
                opp_val = getattr(old_value, "component_ConfigurationSet11", None)
                if opp_val == self:
                    setattr(old_value, "component_ConfigurationSet11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_ConfigurationSet11"):
                opp_val = getattr(value, "component_ConfigurationSet11", None)
                setattr(value, "component_ConfigurationSet11", self)

    @property
    def component_Component34(self):
        return self.__component_Component34

    @component_Component34.setter
    def component_Component34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_Component__component_Component34", None)
        self.__component_Component34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_ContextHandler35"):
                opp_val = getattr(old_value, "component_ContextHandler35", None)
                if opp_val == self:
                    setattr(old_value, "component_ContextHandler35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_ContextHandler35"):
                opp_val = getattr(value, "component_ContextHandler35", None)
                setattr(value, "component_ContextHandler35", self)

    @property
    def component_Component24(self):
        return self.__component_Component24

    @component_Component24.setter
    def component_Component24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_Component__component_Component24", None)
        self.__component_Component24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_ExecutionContext"):
                opp_val = getattr(old_value, "component_ExecutionContext", None)
                if opp_val == self:
                    setattr(old_value, "component_ExecutionContext", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_ExecutionContext"):
                opp_val = getattr(value, "component_ExecutionContext", None)
                setattr(value, "component_ExecutionContext", self)

    @property
    def component_Component17(self):
        return self.__component_Component17

    @component_Component17.setter
    def component_Component17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_Component__component_Component17", None)
        self.__component_Component17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "component_OutPort"):
                    opp_val = getattr(item, "component_OutPort", None)
                    
                    if opp_val == self:
                        setattr(item, "component_OutPort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "component_OutPort"):
                    opp_val = getattr(item, "component_OutPort", None)
                    
                    setattr(item, "component_OutPort", self)
                    

    @property
    def component_Component22(self):
        return self.__component_Component22

    @component_Component22.setter
    def component_Component22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_Component__component_Component22", None)
        self.__component_Component22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_Component20"):
                opp_val = getattr(old_value, "component_Component20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_Component20"):
                opp_val = getattr(value, "component_Component20", None)
                if opp_val is None:
                    setattr(value, "component_Component20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def component_Component8(self):
        return self.__component_Component8

    @component_Component8.setter
    def component_Component8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_Component__component_Component8", None)
        self.__component_Component8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "component_ConfigurationSet"):
                    opp_val = getattr(item, "component_ConfigurationSet", None)
                    
                    if opp_val == self:
                        setattr(item, "component_ConfigurationSet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "component_ConfigurationSet"):
                    opp_val = getattr(item, "component_ConfigurationSet", None)
                    
                    setattr(item, "component_ConfigurationSet", self)
                    

    @property
    def component_Component41(self):
        return self.__component_Component41

    @component_Component41.setter
    def component_Component41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_Component__component_Component41", None)
        self.__component_Component41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_ExecutionContext40"):
                opp_val = getattr(old_value, "component_ExecutionContext40", None)
                if opp_val == self:
                    setattr(old_value, "component_ExecutionContext40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_ExecutionContext40"):
                opp_val = getattr(value, "component_ExecutionContext40", None)
                setattr(value, "component_ExecutionContext40", self)

    @property
    def component_Component19(self):
        return self.__component_Component19

    @component_Component19.setter
    def component_Component19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_Component__component_Component19", None)
        self.__component_Component19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "component_ServicePort"):
                    opp_val = getattr(item, "component_ServicePort", None)
                    
                    if opp_val == self:
                        setattr(item, "component_ServicePort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "component_ServicePort"):
                    opp_val = getattr(item, "component_ServicePort", None)
                    
                    setattr(item, "component_ServicePort", self)
                    

    @property
    def component_Component37(self):
        return self.__component_Component37

    @component_Component37.setter
    def component_Component37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_Component__component_Component37", None)
        self.__component_Component37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_SystemDiagram38"):
                opp_val = getattr(old_value, "component_SystemDiagram38", None)
                if opp_val == self:
                    setattr(old_value, "component_SystemDiagram38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_SystemDiagram38"):
                opp_val = getattr(value, "component_SystemDiagram38", None)
                setattr(value, "component_SystemDiagram38", self)

    @property
    def component_Component20(self):
        return self.__component_Component20

    @component_Component20.setter
    def component_Component20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_Component__component_Component20", None)
        self.__component_Component20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "component_Component22"):
                    opp_val = getattr(item, "component_Component22", None)
                    
                    if opp_val == self:
                        setattr(item, "component_Component22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "component_Component22"):
                    opp_val = getattr(item, "component_Component22", None)
                    
                    setattr(item, "component_Component22", self)
                    

    @property
    def component_Component(self):
        return self.__component_Component

    @component_Component.setter
    def component_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_Component__component_Component", None)
        self.__component_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_SystemDiagram"):
                opp_val = getattr(old_value, "component_SystemDiagram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_SystemDiagram"):
                opp_val = getattr(value, "component_SystemDiagram", None)
                if opp_val is None:
                    setattr(value, "component_SystemDiagram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def component_Component29(self):
        return self.__component_Component29

    @component_Component29.setter
    def component_Component29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_Component__component_Component29", None)
        self.__component_Component29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "component_ExecutionContext30"):
                    opp_val = getattr(item, "component_ExecutionContext30", None)
                    
                    if opp_val == self:
                        setattr(item, "component_ExecutionContext30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "component_ExecutionContext30"):
                    opp_val = getattr(item, "component_ExecutionContext30", None)
                    
                    setattr(item, "component_ExecutionContext30", self)
                    

    def hasComponentAction(self) -> bool:
        # TODO: Implement hasComponentAction method
        pass

    def isGroupingCompositeComponent(self) -> bool:
        # TODO: Implement isGroupingCompositeComponent method
        pass

    def removeComponentR(self, component: str) -> bool:
        # TODO: Implement removeComponentR method
        pass

    def setComponentsR(self, componentList: str) -> bool:
        # TODO: Implement setComponentsR method
        pass

    def addComponentsR(self, componentList: str) -> bool:
        # TODO: Implement addComponentsR method
        pass

    def inOnlineSystemDiagram(self) -> bool:
        # TODO: Implement inOnlineSystemDiagram method
        pass

    def updateConfigurationSetR(self, configSet: str, isActive: bool) -> bool:
        # TODO: Implement updateConfigurationSetR method
        pass

    def updateConfigurationSetListR(self, originallist: str, list: str, activeConfigurationSet: str) -> bool:
        # TODO: Implement updateConfigurationSetListR method
        pass

    def getPath(self) -> str:
        # TODO: Implement getPath method
        pass

    def getAllComponents(self) -> str:
        # TODO: Implement getAllComponents method
        pass

    def setExportedPorts(self, values: str) -> bool:
        # TODO: Implement setExportedPorts method
        pass

    def isCompositeComponent(self) -> bool:
        # TODO: Implement isCompositeComponent method
        pass

class ModelElement:

    pass
class component_SystemDiagram(IPropertyMap, ModelElement):

    def __init__(self, kind: str, ConnectorProcessing: bool, systemId: str, creationDate: str, updateDate: str, component_SystemDiagram: set["component_Component"] = None, component_SystemDiagram3: "component_SystemDiagram" = None, component_SystemDiagram1: "component_SystemDiagram" = None, component_SystemDiagram5: "component_Component" = None, component_SystemDiagram38: "component_Component" = None):
        self.kind = kind
        self.ConnectorProcessing = ConnectorProcessing
        self.systemId = systemId
        self.creationDate = creationDate
        self.updateDate = updateDate
        self.component_SystemDiagram = component_SystemDiagram if component_SystemDiagram is not None else set()
        self.component_SystemDiagram3 = component_SystemDiagram3
        self.component_SystemDiagram1 = component_SystemDiagram1
        self.component_SystemDiagram5 = component_SystemDiagram5
        self.component_SystemDiagram38 = component_SystemDiagram38
        
    @property
    def ConnectorProcessing(self) -> bool:
        return self.__ConnectorProcessing

    @ConnectorProcessing.setter
    def ConnectorProcessing(self, ConnectorProcessing: bool):
        self.__ConnectorProcessing = ConnectorProcessing

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def updateDate(self) -> str:
        return self.__updateDate

    @updateDate.setter
    def updateDate(self, updateDate: str):
        self.__updateDate = updateDate

    @property
    def creationDate(self) -> str:
        return self.__creationDate

    @creationDate.setter
    def creationDate(self, creationDate: str):
        self.__creationDate = creationDate

    @property
    def systemId(self) -> str:
        return self.__systemId

    @systemId.setter
    def systemId(self, systemId: str):
        self.__systemId = systemId

    @property
    def component_SystemDiagram38(self):
        return self.__component_SystemDiagram38

    @component_SystemDiagram38.setter
    def component_SystemDiagram38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_SystemDiagram__component_SystemDiagram38", None)
        self.__component_SystemDiagram38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_Component37"):
                opp_val = getattr(old_value, "component_Component37", None)
                if opp_val == self:
                    setattr(old_value, "component_Component37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_Component37"):
                opp_val = getattr(value, "component_Component37", None)
                setattr(value, "component_Component37", self)

    @property
    def component_SystemDiagram5(self):
        return self.__component_SystemDiagram5

    @component_SystemDiagram5.setter
    def component_SystemDiagram5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_SystemDiagram__component_SystemDiagram5", None)
        self.__component_SystemDiagram5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_Component6"):
                opp_val = getattr(old_value, "component_Component6", None)
                if opp_val == self:
                    setattr(old_value, "component_Component6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_Component6"):
                opp_val = getattr(value, "component_Component6", None)
                setattr(value, "component_Component6", self)

    @property
    def component_SystemDiagram(self):
        return self.__component_SystemDiagram

    @component_SystemDiagram.setter
    def component_SystemDiagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_SystemDiagram__component_SystemDiagram", None)
        self.__component_SystemDiagram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "component_Component"):
                    opp_val = getattr(item, "component_Component", None)
                    
                    if opp_val == self:
                        setattr(item, "component_Component", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "component_Component"):
                    opp_val = getattr(item, "component_Component", None)
                    
                    setattr(item, "component_Component", self)
                    

    @property
    def component_SystemDiagram3(self):
        return self.__component_SystemDiagram3

    @component_SystemDiagram3.setter
    def component_SystemDiagram3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_SystemDiagram__component_SystemDiagram3", None)
        self.__component_SystemDiagram3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_SystemDiagram1"):
                opp_val = getattr(old_value, "component_SystemDiagram1", None)
                if opp_val == self:
                    setattr(old_value, "component_SystemDiagram1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_SystemDiagram1"):
                opp_val = getattr(value, "component_SystemDiagram1", None)
                setattr(value, "component_SystemDiagram1", self)

    @property
    def component_SystemDiagram1(self):
        return self.__component_SystemDiagram1

    @component_SystemDiagram1.setter
    def component_SystemDiagram1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_component_SystemDiagram__component_SystemDiagram1", None)
        self.__component_SystemDiagram1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "component_SystemDiagram3"):
                opp_val = getattr(old_value, "component_SystemDiagram3", None)
                if opp_val == self:
                    setattr(old_value, "component_SystemDiagram3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "component_SystemDiagram3"):
                opp_val = getattr(value, "component_SystemDiagram3", None)
                setattr(value, "component_SystemDiagram3", self)

    def setSynchronizeInterval(self, milliSecond: str):
        # TODO: Implement setSynchronizeInterval method
        pass

    def removePropertyChangeListener(self, listener: str):
        # TODO: Implement removePropertyChangeListener method
        pass

    def addPropertyChangeListener(self, listener: str):
        # TODO: Implement addPropertyChangeListener method
        pass
