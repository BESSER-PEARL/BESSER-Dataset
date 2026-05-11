from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class VariableCharacterisationType(Enum):
    STRUCTURE = "STRUCTURE"
    NUMBER_OF_ELEMENTS = "NUMBER_OF_ELEMENTS"
    VALUE = "VALUE"
    BYTESIZE = "BYTESIZE"
    TYPE = "TYPE"
class PrimitiveTypeEnum(Enum):
    INT = "INT"
    STRING = "STRING"
    BOOL = "BOOL"
    DOUBLE = "DOUBLE"
    CHAR = "CHAR"
    BYTE = "BYTE"
    LONG = "LONG"
class ParameterModifier(Enum):
    none = "none"
    in_ = "in_"
    out = "out"
    inout = "inout"
class SchedulingPolicy(Enum):
    DELAY = "DELAY"
    PROCESSOR_SHARING = "PROCESSOR_SHARING"
    FCFS = "FCFS"


############################################
# Definition of Classes
############################################

class repository_DataType:

    pass
class entity_Entity:

    pass
class pcm_repository_CompositeDataType(repository_DataType, entity_Entity):

    pass
class pcm_repository_CollectionDataType(repository_DataType, entity_Entity):

    pass
class PassiveResource:

    pass
class ServiceEffectSpecification:

    pass
class ProvidesComponentType:

    pass
class ImplementationComponentType:

    pass
class pcm_repository_BasicComponent(ImplementationComponentType):

    def __init__(self, pcm_repository_BasicComponent: set["ServiceEffectSpecification"] = None, pcm_repository_BasicComponent93: set["PassiveResource"] = None):
        self.pcm_repository_BasicComponent = pcm_repository_BasicComponent if pcm_repository_BasicComponent is not None else set()
        self.pcm_repository_BasicComponent93 = pcm_repository_BasicComponent93 if pcm_repository_BasicComponent93 is not None else set()
        
        pass
    @property
    def pcm_repository_BasicComponent(self):
        return self.__pcm_repository_BasicComponent

    @pcm_repository_BasicComponent.setter
    def pcm_repository_BasicComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_BasicComponent__pcm_repository_BasicComponent", None)
        self.__pcm_repository_BasicComponent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ServiceEffectSpecification"):
                    opp_val = getattr(item, "ServiceEffectSpecification", None)
                    
                    if opp_val == self:
                        setattr(item, "ServiceEffectSpecification", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ServiceEffectSpecification"):
                    opp_val = getattr(item, "ServiceEffectSpecification", None)
                    
                    setattr(item, "ServiceEffectSpecification", self)
                    

    @property
    def pcm_repository_BasicComponent93(self):
        return self.__pcm_repository_BasicComponent93

    @pcm_repository_BasicComponent93.setter
    def pcm_repository_BasicComponent93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_BasicComponent__pcm_repository_BasicComponent93", None)
        self.__pcm_repository_BasicComponent93 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PassiveResource"):
                    opp_val = getattr(item, "PassiveResource", None)
                    
                    if opp_val == self:
                        setattr(item, "PassiveResource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PassiveResource"):
                    opp_val = getattr(item, "PassiveResource", None)
                    
                    setattr(item, "PassiveResource", self)
                    

    def RequireSameInterfacesAsImplementationType(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement RequireSameInterfacesAsImplementationType method
        pass

    def NoSeffTypeUsedTwice(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement NoSeffTypeUsedTwice method
        pass

    def ProvideSameInterfacesAsImplementationType(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement ProvideSameInterfacesAsImplementationType method
        pass

class repository_ImplementationComponentType:

    pass
class entity_ComposedProvidingRequiringEntity:

    pass
class pcm_repository_CompositeComponent(repository_ImplementationComponentType, entity_ComposedProvidingRequiringEntity):

    def __init__(self):
        
        pass
    def RequireSameInterfaces(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement RequireSameInterfaces method
        pass

    def ProvideSameInterfaces(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement ProvideSameInterfaces method
        pass

class CompleteComponentType:

    pass
class pcm_repository_ExceptionType:

    def __init__(self, exceptionName: str, exceptionMessage: str):
        self.exceptionName = exceptionName
        self.exceptionMessage = exceptionMessage
        
        pass
    @property
    def exceptionMessage(self):
        return self.__exceptionMessage

    @exceptionMessage.setter
    def exceptionMessage(self, exceptionMessage: str):
        self.__exceptionMessage = exceptionMessage


    @property
    def exceptionName(self):
        return self.__exceptionName

    @exceptionName.setter
    def exceptionName(self, exceptionName: str):
        self.__exceptionName = exceptionName


class Protocol:

    pass
class Role:

    pass
class pcm_repository_ResourceRequiredRole(Role):

    pass
class pcm_repository_RequiredRole(Role):

    pass
class InterfaceProvidingRequiringEntity:

    pass
class pcm_repository_RepositoryComponent(InterfaceProvidingRequiringEntity):

    pass
class Interface:

    pass
class Repository:

    pass
class pcm_repository_DataType(ABC):

    pass
class Signature:

    pass
class pcm_repository_Parameter:

    def __init__(self, parameterName: str, modifier__Parameter: str, pcm_repository_Parameter: "DataType" = None, parameters__Signature: "Signature" = None):
        self.parameterName = parameterName
        self.modifier__Parameter = modifier__Parameter
        self.pcm_repository_Parameter = pcm_repository_Parameter
        self.parameters__Signature = parameters__Signature
        
        pass
    @property
    def modifier__Parameter(self):
        return self.__modifier__Parameter

    @modifier__Parameter.setter
    def modifier__Parameter(self, modifier__Parameter: str):
        self.__modifier__Parameter = modifier__Parameter


    @property
    def parameterName(self):
        return self.__parameterName

    @parameterName.setter
    def parameterName(self, parameterName: str):
        self.__parameterName = parameterName


    @property
    def pcm_repository_Parameter(self):
        return self.__pcm_repository_Parameter

    @pcm_repository_Parameter.setter
    def pcm_repository_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Parameter__pcm_repository_Parameter", None)
        self.__pcm_repository_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType58"):
                opp_val = getattr(old_value, "DataType58", None)
                if opp_val == self:
                    setattr(old_value, "DataType58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType58"):
                opp_val = getattr(value, "DataType58", None)
                setattr(value, "DataType58", self)

    @property
    def parameters__Signature(self):
        return self.__parameters__Signature

    @parameters__Signature.setter
    def parameters__Signature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Parameter__parameters__Signature", None)
        self.__parameters__Signature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Signature"):
                opp_val = getattr(old_value, "Signature", None)
                if opp_val == self:
                    setattr(old_value, "Signature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Signature"):
                opp_val = getattr(value, "Signature", None)
                setattr(value, "Signature", self)

class ExceptionType:

    pass
class DataType:

    pass
class pcm_repository_PrimitiveDataType(DataType):

    def __init__(self, type: str, DataType100: "pcm_repository_InnerDeclaration" = None, DataType66: "pcm_repository_Repository" = None, DataType58: "pcm_repository_Parameter" = None, DataType: "pcm_repository_Signature" = None, DataType95: "pcm_repository_CollectionDataType" = None):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class composition_ProvidedDelegationConnector:

    pass
class Parameter:

    pass
class pcm_repository_Signature:

    def __init__(self, serviceName: str, signature_Parameter: set["Parameter"] = None, signatures__Interface: "Interface" = None, pcm_repository_Signature: "DataType" = None, pcm_repository_Signature56: set["ExceptionType"] = None):
        self.serviceName = serviceName
        self.signature_Parameter = signature_Parameter if signature_Parameter is not None else set()
        self.signatures__Interface = signatures__Interface
        self.pcm_repository_Signature = pcm_repository_Signature
        self.pcm_repository_Signature56 = pcm_repository_Signature56 if pcm_repository_Signature56 is not None else set()
        
        pass
    @property
    def serviceName(self):
        return self.__serviceName

    @serviceName.setter
    def serviceName(self, serviceName: str):
        self.__serviceName = serviceName


    @property
    def pcm_repository_Signature56(self):
        return self.__pcm_repository_Signature56

    @pcm_repository_Signature56.setter
    def pcm_repository_Signature56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Signature__pcm_repository_Signature56", None)
        self.__pcm_repository_Signature56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExceptionType"):
                    opp_val = getattr(item, "ExceptionType", None)
                    
                    if opp_val == self:
                        setattr(item, "ExceptionType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExceptionType"):
                    opp_val = getattr(item, "ExceptionType", None)
                    
                    setattr(item, "ExceptionType", self)
                    

    @property
    def signatures__Interface(self):
        return self.__signatures__Interface

    @signatures__Interface.setter
    def signatures__Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Signature__signatures__Interface", None)
        self.__signatures__Interface = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Interface"):
                opp_val = getattr(old_value, "Interface", None)
                if opp_val == self:
                    setattr(old_value, "Interface", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Interface"):
                opp_val = getattr(value, "Interface", None)
                setattr(value, "Interface", self)

    @property
    def pcm_repository_Signature(self):
        return self.__pcm_repository_Signature

    @pcm_repository_Signature.setter
    def pcm_repository_Signature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Signature__pcm_repository_Signature", None)
        self.__pcm_repository_Signature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DataType"):
                opp_val = getattr(old_value, "DataType", None)
                if opp_val == self:
                    setattr(old_value, "DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DataType"):
                opp_val = getattr(value, "DataType", None)
                setattr(value, "DataType", self)

    @property
    def signature_Parameter(self):
        return self.__signature_Parameter

    @signature_Parameter.setter
    def signature_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Signature__signature_Parameter", None)
        self.__signature_Parameter = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parameter"):
                    opp_val = getattr(item, "Parameter", None)
                    
                    setattr(item, "Parameter", self)
                    

    def ParameterNamesHaveToBeUniqueForASignature(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement ParameterNamesHaveToBeUniqueForASignature method
        pass

class PCMRandomVariable:

    pass
class composition_ResourceRequiredDelegationConnector:

    pass
class composition_AssemblyConnector:

    pass
class composition_RequiredDelegationConnector:

    pass
class pcm_composition_ResourceRequiredDelegationConnector:

    pass
class Connector:

    pass
class pcm_repository_DelegationConnector(Connector):

    pass
class pcm_composition_AssemblyConnector(Connector):

    def __init__(self, pcm_composition_AssemblyConnector: "composition_AssemblyContext" = None, pcm_composition_AssemblyConnector29: "composition_AssemblyContext" = None, pcm_composition_AssemblyConnector32: "ProvidedRole" = None, pcm_composition_AssemblyConnector35: "RequiredRole" = None, assemblyConnectors_ComposedStructure: "composition_ComposedStructure" = None):
        self.pcm_composition_AssemblyConnector = pcm_composition_AssemblyConnector
        self.pcm_composition_AssemblyConnector29 = pcm_composition_AssemblyConnector29
        self.pcm_composition_AssemblyConnector32 = pcm_composition_AssemblyConnector32
        self.pcm_composition_AssemblyConnector35 = pcm_composition_AssemblyConnector35
        self.assemblyConnectors_ComposedStructure = assemblyConnectors_ComposedStructure
        
        pass
    @property
    def pcm_composition_AssemblyConnector32(self):
        return self.__pcm_composition_AssemblyConnector32

    @pcm_composition_AssemblyConnector32.setter
    def pcm_composition_AssemblyConnector32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_AssemblyConnector__pcm_composition_AssemblyConnector32", None)
        self.__pcm_composition_AssemblyConnector32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProvidedRole33"):
                opp_val = getattr(old_value, "ProvidedRole33", None)
                if opp_val == self:
                    setattr(old_value, "ProvidedRole33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProvidedRole33"):
                opp_val = getattr(value, "ProvidedRole33", None)
                setattr(value, "ProvidedRole33", self)

    @property
    def pcm_composition_AssemblyConnector35(self):
        return self.__pcm_composition_AssemblyConnector35

    @pcm_composition_AssemblyConnector35.setter
    def pcm_composition_AssemblyConnector35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_AssemblyConnector__pcm_composition_AssemblyConnector35", None)
        self.__pcm_composition_AssemblyConnector35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RequiredRole36"):
                opp_val = getattr(old_value, "RequiredRole36", None)
                if opp_val == self:
                    setattr(old_value, "RequiredRole36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RequiredRole36"):
                opp_val = getattr(value, "RequiredRole36", None)
                setattr(value, "RequiredRole36", self)

    @property
    def assemblyConnectors_ComposedStructure(self):
        return self.__assemblyConnectors_ComposedStructure

    @assemblyConnectors_ComposedStructure.setter
    def assemblyConnectors_ComposedStructure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_AssemblyConnector__assemblyConnectors_ComposedStructure", None)
        self.__assemblyConnectors_ComposedStructure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ComposedStructure38"):
                opp_val = getattr(old_value, "ComposedStructure38", None)
                if opp_val == self:
                    setattr(old_value, "ComposedStructure38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ComposedStructure38"):
                opp_val = getattr(value, "ComposedStructure38", None)
                setattr(value, "ComposedStructure38", self)

    @property
    def pcm_composition_AssemblyConnector(self):
        return self.__pcm_composition_AssemblyConnector

    @pcm_composition_AssemblyConnector.setter
    def pcm_composition_AssemblyConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_AssemblyConnector__pcm_composition_AssemblyConnector", None)
        self.__pcm_composition_AssemblyConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_AssemblyContext27"):
                opp_val = getattr(old_value, "composition_AssemblyContext27", None)
                if opp_val == self:
                    setattr(old_value, "composition_AssemblyContext27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_AssemblyContext27"):
                opp_val = getattr(value, "composition_AssemblyContext27", None)
                setattr(value, "composition_AssemblyContext27", self)

    @property
    def pcm_composition_AssemblyConnector29(self):
        return self.__pcm_composition_AssemblyConnector29

    @pcm_composition_AssemblyConnector29.setter
    def pcm_composition_AssemblyConnector29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_AssemblyConnector__pcm_composition_AssemblyConnector29", None)
        self.__pcm_composition_AssemblyConnector29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_AssemblyContext30"):
                opp_val = getattr(old_value, "composition_AssemblyContext30", None)
                if opp_val == self:
                    setattr(old_value, "composition_AssemblyContext30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_AssemblyContext30"):
                opp_val = getattr(value, "composition_AssemblyContext30", None)
                setattr(value, "composition_AssemblyContext30", self)

    def AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch method
        pass

    def AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch method
        pass

class VariableUsage:

    pass
class RepositoryComponent:

    pass
class pcm_repository_CompleteComponentType(RepositoryComponent):

    def __init__(self, pcm_repository_CompleteComponentType: set["ProvidesComponentType"] = None, RepositoryComponent62: "pcm_repository_Repository" = None, RepositoryComponent: "pcm_composition_AssemblyContext" = None):
        self.pcm_repository_CompleteComponentType = pcm_repository_CompleteComponentType if pcm_repository_CompleteComponentType is not None else set()
        
        pass
    @property
    def pcm_repository_CompleteComponentType(self):
        return self.__pcm_repository_CompleteComponentType

    @pcm_repository_CompleteComponentType.setter
    def pcm_repository_CompleteComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_CompleteComponentType__pcm_repository_CompleteComponentType", None)
        self.__pcm_repository_CompleteComponentType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProvidesComponentType"):
                    opp_val = getattr(item, "ProvidesComponentType", None)
                    
                    if opp_val == self:
                        setattr(item, "ProvidesComponentType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProvidesComponentType"):
                    opp_val = getattr(item, "ProvidesComponentType", None)
                    
                    setattr(item, "ProvidesComponentType", self)
                    

    def providedInterfacesHaveToConformToProvidedType2(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement providedInterfacesHaveToConformToProvidedType2 method
        pass

    def AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement AtLeastOneInterfaceHasToBeProvidedOrRequiredByAUsefullCompleteComponentType method
        pass

class pcm_repository_ProvidesComponentType(RepositoryComponent):

    def __init__(self, RepositoryComponent62: "pcm_repository_Repository" = None, RepositoryComponent: "pcm_composition_AssemblyContext" = None):
        
        pass
    def AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement AtLeastOneInterfaceHasToBeProvidedByAUsefullProvidesComponentType method
        pass

class pcm_repository_ImplementationComponentType(RepositoryComponent):

    def __init__(self, pcm_repository_ImplementationComponentType: set["CompleteComponentType"] = None, pcm_repository_ImplementationComponentType88: set["VariableUsage"] = None, RepositoryComponent62: "pcm_repository_Repository" = None, RepositoryComponent: "pcm_composition_AssemblyContext" = None):
        self.pcm_repository_ImplementationComponentType = pcm_repository_ImplementationComponentType if pcm_repository_ImplementationComponentType is not None else set()
        self.pcm_repository_ImplementationComponentType88 = pcm_repository_ImplementationComponentType88 if pcm_repository_ImplementationComponentType88 is not None else set()
        
        pass
    @property
    def pcm_repository_ImplementationComponentType88(self):
        return self.__pcm_repository_ImplementationComponentType88

    @pcm_repository_ImplementationComponentType88.setter
    def pcm_repository_ImplementationComponentType88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_ImplementationComponentType__pcm_repository_ImplementationComponentType88", None)
        self.__pcm_repository_ImplementationComponentType88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableUsage89"):
                    opp_val = getattr(item, "VariableUsage89", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableUsage89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableUsage89"):
                    opp_val = getattr(item, "VariableUsage89", None)
                    
                    setattr(item, "VariableUsage89", self)
                    

    @property
    def pcm_repository_ImplementationComponentType(self):
        return self.__pcm_repository_ImplementationComponentType

    @pcm_repository_ImplementationComponentType.setter
    def pcm_repository_ImplementationComponentType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_ImplementationComponentType__pcm_repository_ImplementationComponentType", None)
        self.__pcm_repository_ImplementationComponentType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CompleteComponentType"):
                    opp_val = getattr(item, "CompleteComponentType", None)
                    
                    if opp_val == self:
                        setattr(item, "CompleteComponentType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CompleteComponentType"):
                    opp_val = getattr(item, "CompleteComponentType", None)
                    
                    setattr(item, "CompleteComponentType", self)
                    

    def providedInterfacesHaveToConformToCompleteType(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement providedInterfacesHaveToConformToCompleteType method
        pass

    def RequiredInterfacesHaveToConformToCompleteType(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement RequiredInterfacesHaveToConformToCompleteType method
        pass

class composition_AssemblyContext:

    pass
class DelegationConnector:

    pass
class pcm_composition_RequiredDelegationConnector(DelegationConnector):

    def __init__(self, pcm_composition_RequiredDelegationConnector: "RequiredRole" = None, pcm_composition_RequiredDelegationConnector19: "RequiredRole" = None, pcm_composition_RequiredDelegationConnector22: "composition_AssemblyContext" = None, requiredDelegationConnectors_ComposedStructure: "composition_ComposedStructure" = None):
        self.pcm_composition_RequiredDelegationConnector = pcm_composition_RequiredDelegationConnector
        self.pcm_composition_RequiredDelegationConnector19 = pcm_composition_RequiredDelegationConnector19
        self.pcm_composition_RequiredDelegationConnector22 = pcm_composition_RequiredDelegationConnector22
        self.requiredDelegationConnectors_ComposedStructure = requiredDelegationConnectors_ComposedStructure
        
        pass
    @property
    def requiredDelegationConnectors_ComposedStructure(self):
        return self.__requiredDelegationConnectors_ComposedStructure

    @requiredDelegationConnectors_ComposedStructure.setter
    def requiredDelegationConnectors_ComposedStructure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_RequiredDelegationConnector__requiredDelegationConnectors_ComposedStructure", None)
        self.__requiredDelegationConnectors_ComposedStructure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ComposedStructure25"):
                opp_val = getattr(old_value, "ComposedStructure25", None)
                if opp_val == self:
                    setattr(old_value, "ComposedStructure25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ComposedStructure25"):
                opp_val = getattr(value, "ComposedStructure25", None)
                setattr(value, "ComposedStructure25", self)

    @property
    def pcm_composition_RequiredDelegationConnector22(self):
        return self.__pcm_composition_RequiredDelegationConnector22

    @pcm_composition_RequiredDelegationConnector22.setter
    def pcm_composition_RequiredDelegationConnector22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_RequiredDelegationConnector__pcm_composition_RequiredDelegationConnector22", None)
        self.__pcm_composition_RequiredDelegationConnector22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_AssemblyContext23"):
                opp_val = getattr(old_value, "composition_AssemblyContext23", None)
                if opp_val == self:
                    setattr(old_value, "composition_AssemblyContext23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_AssemblyContext23"):
                opp_val = getattr(value, "composition_AssemblyContext23", None)
                setattr(value, "composition_AssemblyContext23", self)

    @property
    def pcm_composition_RequiredDelegationConnector(self):
        return self.__pcm_composition_RequiredDelegationConnector

    @pcm_composition_RequiredDelegationConnector.setter
    def pcm_composition_RequiredDelegationConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_RequiredDelegationConnector__pcm_composition_RequiredDelegationConnector", None)
        self.__pcm_composition_RequiredDelegationConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RequiredRole17"):
                opp_val = getattr(old_value, "RequiredRole17", None)
                if opp_val == self:
                    setattr(old_value, "RequiredRole17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RequiredRole17"):
                opp_val = getattr(value, "RequiredRole17", None)
                setattr(value, "RequiredRole17", self)

    @property
    def pcm_composition_RequiredDelegationConnector19(self):
        return self.__pcm_composition_RequiredDelegationConnector19

    @pcm_composition_RequiredDelegationConnector19.setter
    def pcm_composition_RequiredDelegationConnector19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_RequiredDelegationConnector__pcm_composition_RequiredDelegationConnector19", None)
        self.__pcm_composition_RequiredDelegationConnector19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RequiredRole20"):
                opp_val = getattr(old_value, "RequiredRole20", None)
                if opp_val == self:
                    setattr(old_value, "RequiredRole20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RequiredRole20"):
                opp_val = getattr(value, "RequiredRole20", None)
                setattr(value, "RequiredRole20", self)

    def RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement RequiredDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

    def ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement ComponentOfAssemblyContextAndInnerRoleRequiringComponentNeedToBeTheSame method
        pass

class pcm_composition_ProvidedDelegationConnector(DelegationConnector):

    def __init__(self, pcm_composition_ProvidedDelegationConnector: "ProvidedRole" = None, pcm_composition_ProvidedDelegationConnector6: "ProvidedRole" = None, pcm_composition_ProvidedDelegationConnector9: "composition_AssemblyContext" = None, providedDelegationConnectors_ComposedStructure: "composition_ComposedStructure" = None):
        self.pcm_composition_ProvidedDelegationConnector = pcm_composition_ProvidedDelegationConnector
        self.pcm_composition_ProvidedDelegationConnector6 = pcm_composition_ProvidedDelegationConnector6
        self.pcm_composition_ProvidedDelegationConnector9 = pcm_composition_ProvidedDelegationConnector9
        self.providedDelegationConnectors_ComposedStructure = providedDelegationConnectors_ComposedStructure
        
        pass
    @property
    def pcm_composition_ProvidedDelegationConnector9(self):
        return self.__pcm_composition_ProvidedDelegationConnector9

    @pcm_composition_ProvidedDelegationConnector9.setter
    def pcm_composition_ProvidedDelegationConnector9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_ProvidedDelegationConnector__pcm_composition_ProvidedDelegationConnector9", None)
        self.__pcm_composition_ProvidedDelegationConnector9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "composition_AssemblyContext"):
                opp_val = getattr(old_value, "composition_AssemblyContext", None)
                if opp_val == self:
                    setattr(old_value, "composition_AssemblyContext", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "composition_AssemblyContext"):
                opp_val = getattr(value, "composition_AssemblyContext", None)
                setattr(value, "composition_AssemblyContext", self)

    @property
    def providedDelegationConnectors_ComposedStructure(self):
        return self.__providedDelegationConnectors_ComposedStructure

    @providedDelegationConnectors_ComposedStructure.setter
    def providedDelegationConnectors_ComposedStructure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_ProvidedDelegationConnector__providedDelegationConnectors_ComposedStructure", None)
        self.__providedDelegationConnectors_ComposedStructure = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ComposedStructure"):
                opp_val = getattr(old_value, "ComposedStructure", None)
                if opp_val == self:
                    setattr(old_value, "ComposedStructure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ComposedStructure"):
                opp_val = getattr(value, "ComposedStructure", None)
                setattr(value, "ComposedStructure", self)

    @property
    def pcm_composition_ProvidedDelegationConnector(self):
        return self.__pcm_composition_ProvidedDelegationConnector

    @pcm_composition_ProvidedDelegationConnector.setter
    def pcm_composition_ProvidedDelegationConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_ProvidedDelegationConnector__pcm_composition_ProvidedDelegationConnector", None)
        self.__pcm_composition_ProvidedDelegationConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProvidedRole4"):
                opp_val = getattr(old_value, "ProvidedRole4", None)
                if opp_val == self:
                    setattr(old_value, "ProvidedRole4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProvidedRole4"):
                opp_val = getattr(value, "ProvidedRole4", None)
                setattr(value, "ProvidedRole4", self)

    @property
    def pcm_composition_ProvidedDelegationConnector6(self):
        return self.__pcm_composition_ProvidedDelegationConnector6

    @pcm_composition_ProvidedDelegationConnector6.setter
    def pcm_composition_ProvidedDelegationConnector6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_composition_ProvidedDelegationConnector__pcm_composition_ProvidedDelegationConnector6", None)
        self.__pcm_composition_ProvidedDelegationConnector6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProvidedRole7"):
                opp_val = getattr(old_value, "ProvidedRole7", None)
                if opp_val == self:
                    setattr(old_value, "ProvidedRole7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProvidedRole7"):
                opp_val = getattr(value, "ProvidedRole7", None)
                setattr(value, "ProvidedRole7", self)

    def ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame method
        pass

    def ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

class entity_InterfaceProvidingRequiringEntity:

    pass
class composition_ComposedStructure:

    pass
class pcm_entity_ComposedProvidingRequiringEntity(composition_ComposedStructure, entity_InterfaceProvidingRequiringEntity):

    def __init__(self, ComposedStructure: "pcm_composition_ProvidedDelegationConnector" = None, ComposedStructure25: "pcm_composition_RequiredDelegationConnector" = None, ComposedStructure13: "pcm_composition_AssemblyContext" = None, ComposedStructure40: "pcm_composition_ResourceRequiredDelegationConnector" = None, ComposedStructure38: "pcm_composition_AssemblyConnector" = None):
        
        pass
    def ProvidedRolesMustBeBound(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement ProvidedRolesMustBeBound method
        pass

class ResourceRequiredRole:

    pass
class RequiredRole:

    pass
class entity_ResourceInterfaceRequiringEntity:

    pass
class entity_InterfaceRequiringEntity:

    pass
class entity_InterfaceProvidingEntity:

    pass
class pcm_entity_InterfaceProvidingRequiringEntity(entity_InterfaceProvidingEntity, entity_ResourceInterfaceRequiringEntity, entity_InterfaceRequiringEntity):

    pass
class ProvidedRole:

    pass
class Entity:

    pass
class pcm_repository_Role(Entity):

    pass
class pcm_repository_Repository(Entity):

    def __init__(self, repositoryDescription: str, repository_Interface: set["Interface"] = None, repository_DataType: set["DataType"] = None, repository_RepositoryComponent: set["RepositoryComponent"] = None):
        self.repositoryDescription = repositoryDescription
        self.repository_Interface = repository_Interface if repository_Interface is not None else set()
        self.repository_DataType = repository_DataType if repository_DataType is not None else set()
        self.repository_RepositoryComponent = repository_RepositoryComponent if repository_RepositoryComponent is not None else set()
        
        pass
    @property
    def repositoryDescription(self):
        return self.__repositoryDescription

    @repositoryDescription.setter
    def repositoryDescription(self, repositoryDescription: str):
        self.__repositoryDescription = repositoryDescription


    @property
    def repository_DataType(self):
        return self.__repository_DataType

    @repository_DataType.setter
    def repository_DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Repository__repository_DataType", None)
        self.__repository_DataType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataType66"):
                    opp_val = getattr(item, "DataType66", None)
                    
                    if opp_val == self:
                        setattr(item, "DataType66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataType66"):
                    opp_val = getattr(item, "DataType66", None)
                    
                    setattr(item, "DataType66", self)
                    

    @property
    def repository_RepositoryComponent(self):
        return self.__repository_RepositoryComponent

    @repository_RepositoryComponent.setter
    def repository_RepositoryComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Repository__repository_RepositoryComponent", None)
        self.__repository_RepositoryComponent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RepositoryComponent62"):
                    opp_val = getattr(item, "RepositoryComponent62", None)
                    
                    if opp_val == self:
                        setattr(item, "RepositoryComponent62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RepositoryComponent62"):
                    opp_val = getattr(item, "RepositoryComponent62", None)
                    
                    setattr(item, "RepositoryComponent62", self)
                    

    @property
    def repository_Interface(self):
        return self.__repository_Interface

    @repository_Interface.setter
    def repository_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Repository__repository_Interface", None)
        self.__repository_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Interface64"):
                    opp_val = getattr(item, "Interface64", None)
                    
                    if opp_val == self:
                        setattr(item, "Interface64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interface64"):
                    opp_val = getattr(item, "Interface64", None)
                    
                    setattr(item, "Interface64", self)
                    

class pcm_entity_InterfaceRequiringEntity(Entity):

    pass
class pcm_composition_AssemblyContext(Entity):

    pass
class pcm_composition_ComposedStructure(Entity):

    pass
class pcm_repository_Interface(Entity):

    def __init__(self, pcm_repository_Interface: set["Interface"] = None, pcm_repository_Interface78: set["Protocol"] = None, interface_Signature: set["Signature"] = None, interfaces__Repository: "Repository" = None, pcm_repository_Interface75: set["Interface"] = None):
        self.pcm_repository_Interface = pcm_repository_Interface if pcm_repository_Interface is not None else set()
        self.pcm_repository_Interface78 = pcm_repository_Interface78 if pcm_repository_Interface78 is not None else set()
        self.interface_Signature = interface_Signature if interface_Signature is not None else set()
        self.interfaces__Repository = interfaces__Repository
        self.pcm_repository_Interface75 = pcm_repository_Interface75 if pcm_repository_Interface75 is not None else set()
        
        pass
    @property
    def pcm_repository_Interface78(self):
        return self.__pcm_repository_Interface78

    @pcm_repository_Interface78.setter
    def pcm_repository_Interface78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Interface__pcm_repository_Interface78", None)
        self.__pcm_repository_Interface78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Protocol"):
                    opp_val = getattr(item, "Protocol", None)
                    
                    if opp_val == self:
                        setattr(item, "Protocol", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Protocol"):
                    opp_val = getattr(item, "Protocol", None)
                    
                    setattr(item, "Protocol", self)
                    

    @property
    def pcm_repository_Interface(self):
        return self.__pcm_repository_Interface

    @pcm_repository_Interface.setter
    def pcm_repository_Interface(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Interface__pcm_repository_Interface", None)
        self.__pcm_repository_Interface = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Interface73"):
                    opp_val = getattr(item, "Interface73", None)
                    
                    if opp_val == self:
                        setattr(item, "Interface73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interface73"):
                    opp_val = getattr(item, "Interface73", None)
                    
                    setattr(item, "Interface73", self)
                    

    @property
    def interface_Signature(self):
        return self.__interface_Signature

    @interface_Signature.setter
    def interface_Signature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Interface__interface_Signature", None)
        self.__interface_Signature = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Signature80"):
                    opp_val = getattr(item, "Signature80", None)
                    
                    if opp_val == self:
                        setattr(item, "Signature80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Signature80"):
                    opp_val = getattr(item, "Signature80", None)
                    
                    setattr(item, "Signature80", self)
                    

    @property
    def pcm_repository_Interface75(self):
        return self.__pcm_repository_Interface75

    @pcm_repository_Interface75.setter
    def pcm_repository_Interface75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Interface__pcm_repository_Interface75", None)
        self.__pcm_repository_Interface75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Interface76"):
                    opp_val = getattr(item, "Interface76", None)
                    
                    if opp_val == self:
                        setattr(item, "Interface76", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interface76"):
                    opp_val = getattr(item, "Interface76", None)
                    
                    setattr(item, "Interface76", self)
                    

    @property
    def interfaces__Repository(self):
        return self.__interfaces__Repository

    @interfaces__Repository.setter
    def interfaces__Repository(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_repository_Interface__interfaces__Repository", None)
        self.__interfaces__Repository = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Repository82"):
                opp_val = getattr(old_value, "Repository82", None)
                if opp_val == self:
                    setattr(old_value, "Repository82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Repository82"):
                opp_val = getattr(value, "Repository82", None)
                setattr(value, "Repository82", self)

    def NoProtocolTypeIDUsedTwice(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement NoProtocolTypeIDUsedTwice method
        pass

    def SignaturesHaveToBeUniqueForAnInterface(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement SignaturesHaveToBeUniqueForAnInterface method
        pass

class pcm_entity_ResourceInterfaceRequiringEntity(Entity):

    pass
class pcm_repository_PassiveResource(Entity):

    pass
class pcm_connectors_Connector(Entity):

    pass
class pcm_entity_InterfaceProvidingEntity(Entity):

    pass
class pcm_entity_NamedElement(ABC):

    def __init__(self, entityName: str):
        self.entityName = entityName
        
        pass
    @property
    def entityName(self):
        return self.__entityName

    @entityName.setter
    def entityName(self, entityName: str):
        self.__entityName = entityName


class entity_NamedElement:

    pass
class Identifier:

    pass
class pcm_entity_Entity(Identifier, entity_NamedElement):

    pass
class RandomVariable:

    pass
class pcm_core_PCMRandomVariable(RandomVariable):

    def __init__(self):
        
        pass
    def SpecificationMustNotBeNULL(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement SpecificationMustNotBeNULL method
        pass

class repository_RepositoryComponent:

    pass
class pcm_subsystem_SubSystem(repository_RepositoryComponent, entity_ComposedProvidingRequiringEntity):

    pass
class pcm_usagemodel_BranchTransition:

    def __init__(self, branchProbability: float, pcm_usagemodel_BranchTransition: "ScenarioBehaviour" = None):
        self.branchProbability = branchProbability
        self.pcm_usagemodel_BranchTransition = pcm_usagemodel_BranchTransition
        
        pass
    @property
    def branchProbability(self):
        return self.__branchProbability

    @branchProbability.setter
    def branchProbability(self, branchProbability: float):
        self.__branchProbability = branchProbability


    @property
    def pcm_usagemodel_BranchTransition(self):
        return self.__pcm_usagemodel_BranchTransition

    @pcm_usagemodel_BranchTransition.setter
    def pcm_usagemodel_BranchTransition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_usagemodel_BranchTransition__pcm_usagemodel_BranchTransition", None)
        self.__pcm_usagemodel_BranchTransition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ScenarioBehaviour252"):
                opp_val = getattr(old_value, "ScenarioBehaviour252", None)
                if opp_val == self:
                    setattr(old_value, "ScenarioBehaviour252", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ScenarioBehaviour252"):
                opp_val = getattr(value, "ScenarioBehaviour252", None)
                setattr(value, "ScenarioBehaviour252", self)

class BranchTransition:

    pass
class pcm_usagemodel_UserData:

    pass
class UserData:

    pass
class UsageScenario:

    pass
class pcm_usagemodel_UsageModel:

    pass
class pcm_usagemodel_AbstractUserAction(Entity):

    pass
class AbstractUserAction:

    pass
class pcm_usagemodel_Delay(AbstractUserAction):

    pass
class pcm_usagemodel_Stop(AbstractUserAction):

    def __init__(self, AbstractUserAction: "pcm_usagemodel_ScenarioBehaviour" = None, AbstractUserAction221: "pcm_usagemodel_AbstractUserAction" = None, AbstractUserAction219: "pcm_usagemodel_AbstractUserAction" = None):
        
        pass
    def StopHasNoSuccessor(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement StopHasNoSuccessor method
        pass

class pcm_usagemodel_Branch(AbstractUserAction):

    def __init__(self, pcm_usagemodel_Branch: set["BranchTransition"] = None, AbstractUserAction: "pcm_usagemodel_ScenarioBehaviour" = None, AbstractUserAction221: "pcm_usagemodel_AbstractUserAction" = None, AbstractUserAction219: "pcm_usagemodel_AbstractUserAction" = None):
        self.pcm_usagemodel_Branch = pcm_usagemodel_Branch if pcm_usagemodel_Branch is not None else set()
        
        pass
    @property
    def pcm_usagemodel_Branch(self):
        return self.__pcm_usagemodel_Branch

    @pcm_usagemodel_Branch.setter
    def pcm_usagemodel_Branch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_usagemodel_Branch__pcm_usagemodel_Branch", None)
        self.__pcm_usagemodel_Branch = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BranchTransition"):
                    opp_val = getattr(item, "BranchTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "BranchTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BranchTransition"):
                    opp_val = getattr(item, "BranchTransition", None)
                    
                    setattr(item, "BranchTransition", self)
                    

    def AllBranchProbabilitiesMustSumUpTo1(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement AllBranchProbabilitiesMustSumUpTo1 method
        pass

class pcm_usagemodel_EntryLevelSystemCall(AbstractUserAction):

    pass
class pcm_usagemodel_Loop(AbstractUserAction):

    pass
class pcm_usagemodel_Start(AbstractUserAction):

    def __init__(self, AbstractUserAction: "pcm_usagemodel_ScenarioBehaviour" = None, AbstractUserAction221: "pcm_usagemodel_AbstractUserAction" = None, AbstractUserAction219: "pcm_usagemodel_AbstractUserAction" = None):
        
        pass
    def StartHasNoPredecessor(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement StartHasNoPredecessor method
        pass

class pcm_usagemodel_ScenarioBehaviour(Entity):

    def __init__(self, pcm_usagemodel_ScenarioBehaviour: set["AbstractUserAction"] = None):
        self.pcm_usagemodel_ScenarioBehaviour = pcm_usagemodel_ScenarioBehaviour if pcm_usagemodel_ScenarioBehaviour is not None else set()
        
        pass
    @property
    def pcm_usagemodel_ScenarioBehaviour(self):
        return self.__pcm_usagemodel_ScenarioBehaviour

    @pcm_usagemodel_ScenarioBehaviour.setter
    def pcm_usagemodel_ScenarioBehaviour(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_usagemodel_ScenarioBehaviour__pcm_usagemodel_ScenarioBehaviour", None)
        self.__pcm_usagemodel_ScenarioBehaviour = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractUserAction"):
                    opp_val = getattr(item, "AbstractUserAction", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractUserAction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractUserAction"):
                    opp_val = getattr(item, "AbstractUserAction", None)
                    
                    setattr(item, "AbstractUserAction", self)
                    

    def Exactlyonestop(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement Exactlyonestop method
        pass

    def Exactlyonestart(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement Exactlyonestart method
        pass

    def EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement EachuseractionexceptStartandStopmusthaveapredecessorandsuccessor method
        pass

class ScenarioBehaviour:

    pass
class Workload:

    pass
class pcm_usagemodel_ClosedWorkload(Workload):

    def __init__(self, population: int, pcm_usagemodel_ClosedWorkload: "PCMRandomVariable" = None, Workload: "pcm_usagemodel_UsageScenario" = None):
        self.population = population
        self.pcm_usagemodel_ClosedWorkload = pcm_usagemodel_ClosedWorkload
        
        pass
    @property
    def population(self):
        return self.__population

    @population.setter
    def population(self, population: int):
        self.__population = population


    @property
    def pcm_usagemodel_ClosedWorkload(self):
        return self.__pcm_usagemodel_ClosedWorkload

    @pcm_usagemodel_ClosedWorkload.setter
    def pcm_usagemodel_ClosedWorkload(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_usagemodel_ClosedWorkload__pcm_usagemodel_ClosedWorkload", None)
        self.__pcm_usagemodel_ClosedWorkload = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable249"):
                opp_val = getattr(old_value, "PCMRandomVariable249", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable249", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable249"):
                opp_val = getattr(value, "PCMRandomVariable249", None)
                setattr(value, "PCMRandomVariable249", self)

    def PopulationInClosedWorkloadNeedsToBeSpecified(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement PopulationInClosedWorkloadNeedsToBeSpecified method
        pass

    def ThinkTimeInClosedWorkloadNeedsToBeSpecified(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement ThinkTimeInClosedWorkloadNeedsToBeSpecified method
        pass

class pcm_usagemodel_OpenWorkload(Workload):

    def __init__(self, pcm_usagemodel_OpenWorkload: "PCMRandomVariable" = None, Workload: "pcm_usagemodel_UsageScenario" = None):
        self.pcm_usagemodel_OpenWorkload = pcm_usagemodel_OpenWorkload
        
        pass
    @property
    def pcm_usagemodel_OpenWorkload(self):
        return self.__pcm_usagemodel_OpenWorkload

    @pcm_usagemodel_OpenWorkload.setter
    def pcm_usagemodel_OpenWorkload(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_usagemodel_OpenWorkload__pcm_usagemodel_OpenWorkload", None)
        self.__pcm_usagemodel_OpenWorkload = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable231"):
                opp_val = getattr(old_value, "PCMRandomVariable231", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable231"):
                opp_val = getattr(value, "PCMRandomVariable231", None)
                setattr(value, "PCMRandomVariable231", self)

    def InterArrivalTimeInOpenWorkloadNeedsToBeSpecified(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement InterArrivalTimeInOpenWorkloadNeedsToBeSpecified method
        pass

class pcm_usagemodel_UsageScenario(Entity):

    pass
class pcm_usagemodel_Workload(ABC):

    pass
class SpecifiedOutputParameterAbstraction:

    pass
class SpecifiedQoSAnnotation:

    pass
class pcm_reliability_SpecifiedFailureProbability(SpecifiedQoSAnnotation):

    def __init__(self, failureProbability: float, SpecifiedQoSAnnotation: "pcm_qosannotations_QoSAnnotations" = None):
        self.failureProbability = failureProbability
        
        pass
    @property
    def failureProbability(self):
        return self.__failureProbability

    @failureProbability.setter
    def failureProbability(self, failureProbability: float):
        self.__failureProbability = failureProbability


class pcm_performance_SystemSpecifiedExecutionTime(SpecifiedQoSAnnotation):

    pass
class pcm_qosannotations_QoSAnnotations(Entity):

    pass
class pcm_qosannotations_SpecifiedOutputParameterAbstraction(ABC):

    pass
class pcm_qosannotations_SpecifiedQoSAnnotation(ABC):

    pass
class QoSAnnotations:

    pass
class pcm_system_System(entity_ComposedProvidingRequiringEntity, entity_Entity):

    pass
class pcm_performance_ComponentSpecifiedExecutionTime(SpecifiedQoSAnnotation):

    pass
class pcm_resourceenvironment_ProcessingResourceSpecification:

    def __init__(self, MTTR: float, MTTF: float, schedulingPolicy: str, pcm_resourceenvironment_ProcessingResourceSpecification: "ProcessingResourceType" = None, pcm_resourceenvironment_ProcessingResourceSpecification189: "PCMRandomVariable" = None):
        self.MTTR = MTTR
        self.MTTF = MTTF
        self.schedulingPolicy = schedulingPolicy
        self.pcm_resourceenvironment_ProcessingResourceSpecification = pcm_resourceenvironment_ProcessingResourceSpecification
        self.pcm_resourceenvironment_ProcessingResourceSpecification189 = pcm_resourceenvironment_ProcessingResourceSpecification189
        
        pass
    @property
    def MTTR(self):
        return self.__MTTR

    @MTTR.setter
    def MTTR(self, MTTR: float):
        self.__MTTR = MTTR


    @property
    def MTTF(self):
        return self.__MTTF

    @MTTF.setter
    def MTTF(self, MTTF: float):
        self.__MTTF = MTTF


    @property
    def schedulingPolicy(self):
        return self.__schedulingPolicy

    @schedulingPolicy.setter
    def schedulingPolicy(self, schedulingPolicy: str):
        self.__schedulingPolicy = schedulingPolicy


    @property
    def pcm_resourceenvironment_ProcessingResourceSpecification189(self):
        return self.__pcm_resourceenvironment_ProcessingResourceSpecification189

    @pcm_resourceenvironment_ProcessingResourceSpecification189.setter
    def pcm_resourceenvironment_ProcessingResourceSpecification189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_resourceenvironment_ProcessingResourceSpecification__pcm_resourceenvironment_ProcessingResourceSpecification189", None)
        self.__pcm_resourceenvironment_ProcessingResourceSpecification189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable190"):
                opp_val = getattr(old_value, "PCMRandomVariable190", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable190"):
                opp_val = getattr(value, "PCMRandomVariable190", None)
                setattr(value, "PCMRandomVariable190", self)

    @property
    def pcm_resourceenvironment_ProcessingResourceSpecification(self):
        return self.__pcm_resourceenvironment_ProcessingResourceSpecification

    @pcm_resourceenvironment_ProcessingResourceSpecification.setter
    def pcm_resourceenvironment_ProcessingResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_resourceenvironment_ProcessingResourceSpecification__pcm_resourceenvironment_ProcessingResourceSpecification", None)
        self.__pcm_resourceenvironment_ProcessingResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcessingResourceType187"):
                opp_val = getattr(old_value, "ProcessingResourceType187", None)
                if opp_val == self:
                    setattr(old_value, "ProcessingResourceType187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessingResourceType187"):
                opp_val = getattr(value, "ProcessingResourceType187", None)
                setattr(value, "ProcessingResourceType187", self)

class CommunicationLinkResourceType:

    pass
class pcm_resourceenvironment_CommunicationLinkResourceSpecification:

    def __init__(self, failureProbability: float, pcm_resourceenvironment_CommunicationLinkResourceSpecification: "CommunicationLinkResourceType" = None, pcm_resourceenvironment_CommunicationLinkResourceSpecification181: "PCMRandomVariable" = None, pcm_resourceenvironment_CommunicationLinkResourceSpecification184: "PCMRandomVariable" = None):
        self.failureProbability = failureProbability
        self.pcm_resourceenvironment_CommunicationLinkResourceSpecification = pcm_resourceenvironment_CommunicationLinkResourceSpecification
        self.pcm_resourceenvironment_CommunicationLinkResourceSpecification181 = pcm_resourceenvironment_CommunicationLinkResourceSpecification181
        self.pcm_resourceenvironment_CommunicationLinkResourceSpecification184 = pcm_resourceenvironment_CommunicationLinkResourceSpecification184
        
        pass
    @property
    def failureProbability(self):
        return self.__failureProbability

    @failureProbability.setter
    def failureProbability(self, failureProbability: float):
        self.__failureProbability = failureProbability


    @property
    def pcm_resourceenvironment_CommunicationLinkResourceSpecification184(self):
        return self.__pcm_resourceenvironment_CommunicationLinkResourceSpecification184

    @pcm_resourceenvironment_CommunicationLinkResourceSpecification184.setter
    def pcm_resourceenvironment_CommunicationLinkResourceSpecification184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_resourceenvironment_CommunicationLinkResourceSpecification__pcm_resourceenvironment_CommunicationLinkResourceSpecification184", None)
        self.__pcm_resourceenvironment_CommunicationLinkResourceSpecification184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable185"):
                opp_val = getattr(old_value, "PCMRandomVariable185", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable185"):
                opp_val = getattr(value, "PCMRandomVariable185", None)
                setattr(value, "PCMRandomVariable185", self)

    @property
    def pcm_resourceenvironment_CommunicationLinkResourceSpecification181(self):
        return self.__pcm_resourceenvironment_CommunicationLinkResourceSpecification181

    @pcm_resourceenvironment_CommunicationLinkResourceSpecification181.setter
    def pcm_resourceenvironment_CommunicationLinkResourceSpecification181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_resourceenvironment_CommunicationLinkResourceSpecification__pcm_resourceenvironment_CommunicationLinkResourceSpecification181", None)
        self.__pcm_resourceenvironment_CommunicationLinkResourceSpecification181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable182"):
                opp_val = getattr(old_value, "PCMRandomVariable182", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable182"):
                opp_val = getattr(value, "PCMRandomVariable182", None)
                setattr(value, "PCMRandomVariable182", self)

    @property
    def pcm_resourceenvironment_CommunicationLinkResourceSpecification(self):
        return self.__pcm_resourceenvironment_CommunicationLinkResourceSpecification

    @pcm_resourceenvironment_CommunicationLinkResourceSpecification.setter
    def pcm_resourceenvironment_CommunicationLinkResourceSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_resourceenvironment_CommunicationLinkResourceSpecification__pcm_resourceenvironment_CommunicationLinkResourceSpecification", None)
        self.__pcm_resourceenvironment_CommunicationLinkResourceSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CommunicationLinkResourceType"):
                opp_val = getattr(old_value, "CommunicationLinkResourceType", None)
                if opp_val == self:
                    setattr(old_value, "CommunicationLinkResourceType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CommunicationLinkResourceType"):
                opp_val = getattr(value, "CommunicationLinkResourceType", None)
                setattr(value, "CommunicationLinkResourceType", self)

class CommunicationLinkResourceSpecification:

    pass
class ProcessingResourceSpecification:

    pass
class pcm_resourceenvironment_ResourceContainer(Entity):

    pass
class pcm_resourceenvironment_LinkingResource(Entity):

    pass
class LinkingResource:

    pass
class pcm_resourceenvironment_ResourceEnvironment:

    pass
class System:

    pass
class ResourceEnvironment:

    pass
class AllocationContext:

    pass
class pcm_allocation_Allocation(Entity):

    def __init__(self, pcm_allocation_Allocation: set["AllocationContext"] = None, pcm_allocation_Allocation165: "ResourceEnvironment" = None, pcm_allocation_Allocation167: "System" = None):
        self.pcm_allocation_Allocation = pcm_allocation_Allocation if pcm_allocation_Allocation is not None else set()
        self.pcm_allocation_Allocation165 = pcm_allocation_Allocation165
        self.pcm_allocation_Allocation167 = pcm_allocation_Allocation167
        
        pass
    @property
    def pcm_allocation_Allocation165(self):
        return self.__pcm_allocation_Allocation165

    @pcm_allocation_Allocation165.setter
    def pcm_allocation_Allocation165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_allocation_Allocation__pcm_allocation_Allocation165", None)
        self.__pcm_allocation_Allocation165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResourceEnvironment"):
                opp_val = getattr(old_value, "ResourceEnvironment", None)
                if opp_val == self:
                    setattr(old_value, "ResourceEnvironment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResourceEnvironment"):
                opp_val = getattr(value, "ResourceEnvironment", None)
                setattr(value, "ResourceEnvironment", self)

    @property
    def pcm_allocation_Allocation167(self):
        return self.__pcm_allocation_Allocation167

    @pcm_allocation_Allocation167.setter
    def pcm_allocation_Allocation167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_allocation_Allocation__pcm_allocation_Allocation167", None)
        self.__pcm_allocation_Allocation167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "System"):
                opp_val = getattr(old_value, "System", None)
                if opp_val == self:
                    setattr(old_value, "System", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "System"):
                opp_val = getattr(value, "System", None)
                setattr(value, "System", self)

    @property
    def pcm_allocation_Allocation(self):
        return self.__pcm_allocation_Allocation

    @pcm_allocation_Allocation.setter
    def pcm_allocation_Allocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_allocation_Allocation__pcm_allocation_Allocation", None)
        self.__pcm_allocation_Allocation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AllocationContext"):
                    opp_val = getattr(item, "AllocationContext", None)
                    
                    if opp_val == self:
                        setattr(item, "AllocationContext", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AllocationContext"):
                    opp_val = getattr(item, "AllocationContext", None)
                    
                    setattr(item, "AllocationContext", self)
                    

    def EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement EachAssemblyContextWithinSystemHasToBeAllocatedExactlyOnce method
        pass

class ResourceType:

    pass
class pcm_resourcetype_ProcessingResourceType(ResourceType):

    pass
class pcm_resourcetype_ResourceRepository:

    pass
class UnitCarryingElement:

    pass
class pcm_resourcetype_ResourceType(UnitCarryingElement, entity_Entity):

    pass
class ProcessingResourceType:

    pass
class pcm_resourcetype_CommunicationLinkResourceType(ProcessingResourceType):

    pass
class pcm_performance_ParametricResourceDemand:

    pass
class pcm_seff_ServiceEffectSpecification(ABC):

    def __init__(self, seffTypeID: str, pcm_seff_ServiceEffectSpecification: "Signature" = None):
        self.seffTypeID = seffTypeID
        self.pcm_seff_ServiceEffectSpecification = pcm_seff_ServiceEffectSpecification
        
        pass
    @property
    def seffTypeID(self):
        return self.__seffTypeID

    @seffTypeID.setter
    def seffTypeID(self, seffTypeID: str):
        self.__seffTypeID = seffTypeID


    @property
    def pcm_seff_ServiceEffectSpecification(self):
        return self.__pcm_seff_ServiceEffectSpecification

    @pcm_seff_ServiceEffectSpecification.setter
    def pcm_seff_ServiceEffectSpecification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_seff_ServiceEffectSpecification__pcm_seff_ServiceEffectSpecification", None)
        self.__pcm_seff_ServiceEffectSpecification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Signature152"):
                opp_val = getattr(old_value, "Signature152", None)
                if opp_val == self:
                    setattr(old_value, "Signature152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Signature152"):
                opp_val = getattr(value, "Signature152", None)
                setattr(value, "Signature152", self)

class ResourceContainer:

    pass
class pcm_allocation_AllocationContext(Entity):

    pass
class AbstractBranchTransition:

    pass
class pcm_seff_GuardedBranchTransition(AbstractBranchTransition):

    pass
class pcm_seff_ProbabilisticBranchTransition(AbstractBranchTransition):

    def __init__(self, branchProbability: float, AbstractBranchTransition: "pcm_seff_BranchAction" = None):
        self.branchProbability = branchProbability
        
        pass
    @property
    def branchProbability(self):
        return self.__branchProbability

    @branchProbability.setter
    def branchProbability(self, branchProbability: float):
        self.__branchProbability = branchProbability


class pcm_seff_SynchronisationPoint:

    pass
class SynchronisationPoint:

    pass
class ForkedBehaviour:

    pass
class ResourceDemandingBehaviour:

    pass
class pcm_seff_ForkedBehaviour(ResourceDemandingBehaviour):

    pass
class AbstractLoopAction:

    pass
class pcm_seff_CollectionIteratorAction(AbstractLoopAction):

    pass
class pcm_seff_LoopAction(AbstractLoopAction):

    pass
class performance_ParametricResourceDemand:

    pass
class pcm_seff_ResourceDemandingBehaviour:

    def __init__(self, pcm_seff_ResourceDemandingBehaviour: set["AbstractAction"] = None):
        self.pcm_seff_ResourceDemandingBehaviour = pcm_seff_ResourceDemandingBehaviour if pcm_seff_ResourceDemandingBehaviour is not None else set()
        
        pass
    @property
    def pcm_seff_ResourceDemandingBehaviour(self):
        return self.__pcm_seff_ResourceDemandingBehaviour

    @pcm_seff_ResourceDemandingBehaviour.setter
    def pcm_seff_ResourceDemandingBehaviour(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_seff_ResourceDemandingBehaviour__pcm_seff_ResourceDemandingBehaviour", None)
        self.__pcm_seff_ResourceDemandingBehaviour = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractAction116"):
                    opp_val = getattr(item, "AbstractAction116", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractAction116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractAction116"):
                    opp_val = getattr(item, "AbstractAction116", None)
                    
                    setattr(item, "AbstractAction116", self)
                    

    def EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement EachActionExceptStartActionandStopActionMustHhaveAPredecessorAndSuccessor method
        pass

    def ExactlyOneStopAction(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement ExactlyOneStopAction method
        pass

    def ExactlyOneStartAction(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement ExactlyOneStartAction method
        pass

class seff_ResourceDemandingBehaviour:

    pass
class seff_ServiceEffectSpecification:

    pass
class pcm_seff_ResourceDemandingSEFF(seff_ResourceDemandingBehaviour, seff_ServiceEffectSpecification, Identifier):

    pass
class pcm_seff_AbstractAction(Entity):

    pass
class AbstractAction:

    pass
class pcm_seff_ExternalCallAction(AbstractAction):

    def __init__(self, retryCount: int, pcm_seff_ExternalCallAction: "Signature" = None, pcm_seff_ExternalCallAction133: set["VariableUsage"] = None, pcm_seff_ExternalCallAction136: set["VariableUsage"] = None, pcm_seff_ExternalCallAction139: "Role" = None, AbstractAction114: "pcm_seff_AbstractAction" = None, AbstractAction: "pcm_seff_AbstractAction" = None, AbstractAction116: "pcm_seff_ResourceDemandingBehaviour" = None):
        self.retryCount = retryCount
        self.pcm_seff_ExternalCallAction = pcm_seff_ExternalCallAction
        self.pcm_seff_ExternalCallAction133 = pcm_seff_ExternalCallAction133 if pcm_seff_ExternalCallAction133 is not None else set()
        self.pcm_seff_ExternalCallAction136 = pcm_seff_ExternalCallAction136 if pcm_seff_ExternalCallAction136 is not None else set()
        self.pcm_seff_ExternalCallAction139 = pcm_seff_ExternalCallAction139
        
        pass
    @property
    def retryCount(self):
        return self.__retryCount

    @retryCount.setter
    def retryCount(self, retryCount: int):
        self.__retryCount = retryCount


    @property
    def pcm_seff_ExternalCallAction136(self):
        return self.__pcm_seff_ExternalCallAction136

    @pcm_seff_ExternalCallAction136.setter
    def pcm_seff_ExternalCallAction136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_seff_ExternalCallAction__pcm_seff_ExternalCallAction136", None)
        self.__pcm_seff_ExternalCallAction136 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableUsage137"):
                    opp_val = getattr(item, "VariableUsage137", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableUsage137", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableUsage137"):
                    opp_val = getattr(item, "VariableUsage137", None)
                    
                    setattr(item, "VariableUsage137", self)
                    

    @property
    def pcm_seff_ExternalCallAction(self):
        return self.__pcm_seff_ExternalCallAction

    @pcm_seff_ExternalCallAction.setter
    def pcm_seff_ExternalCallAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_seff_ExternalCallAction__pcm_seff_ExternalCallAction", None)
        self.__pcm_seff_ExternalCallAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Signature131"):
                opp_val = getattr(old_value, "Signature131", None)
                if opp_val == self:
                    setattr(old_value, "Signature131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Signature131"):
                opp_val = getattr(value, "Signature131", None)
                setattr(value, "Signature131", self)

    @property
    def pcm_seff_ExternalCallAction139(self):
        return self.__pcm_seff_ExternalCallAction139

    @pcm_seff_ExternalCallAction139.setter
    def pcm_seff_ExternalCallAction139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_seff_ExternalCallAction__pcm_seff_ExternalCallAction139", None)
        self.__pcm_seff_ExternalCallAction139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Role"):
                opp_val = getattr(old_value, "Role", None)
                if opp_val == self:
                    setattr(old_value, "Role", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Role"):
                opp_val = getattr(value, "Role", None)
                setattr(value, "Role", self)

    @property
    def pcm_seff_ExternalCallAction133(self):
        return self.__pcm_seff_ExternalCallAction133

    @pcm_seff_ExternalCallAction133.setter
    def pcm_seff_ExternalCallAction133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_seff_ExternalCallAction__pcm_seff_ExternalCallAction133", None)
        self.__pcm_seff_ExternalCallAction133 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VariableUsage134"):
                    opp_val = getattr(item, "VariableUsage134", None)
                    
                    if opp_val == self:
                        setattr(item, "VariableUsage134", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VariableUsage134"):
                    opp_val = getattr(item, "VariableUsage134", None)
                    
                    setattr(item, "VariableUsage134", self)
                    

class pcm_seff_AbstractInternalControlFlowAction(AbstractAction):

    pass
class AbstractInternalControlFlowAction:

    pass
class pcm_seff_StartAction(AbstractInternalControlFlowAction):

    def __init__(self, AbstractInternalControlFlowAction: "pcm_performance_ParametricResourceDemand" = None):
        
        pass
    def StartActionPredecessorMustNotBeDefined(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement StartActionPredecessorMustNotBeDefined method
        pass

class pcm_seff_AcquireAction(AbstractInternalControlFlowAction):

    pass
class pcm_seff_ForkAction(AbstractInternalControlFlowAction):

    pass
class pcm_seff_SetVariableAction(AbstractInternalControlFlowAction):

    pass
class pcm_seff_InternalAction(AbstractInternalControlFlowAction):

    def __init__(self, failureProbability: float, AbstractInternalControlFlowAction: "pcm_performance_ParametricResourceDemand" = None):
        self.failureProbability = failureProbability
        
        pass
    @property
    def failureProbability(self):
        return self.__failureProbability

    @failureProbability.setter
    def failureProbability(self, failureProbability: float):
        self.__failureProbability = failureProbability


class pcm_seff_BranchAction(AbstractInternalControlFlowAction):

    def __init__(self, pcm_seff_BranchAction: set["AbstractBranchTransition"] = None, AbstractInternalControlFlowAction: "pcm_performance_ParametricResourceDemand" = None):
        self.pcm_seff_BranchAction = pcm_seff_BranchAction if pcm_seff_BranchAction is not None else set()
        
        pass
    @property
    def pcm_seff_BranchAction(self):
        return self.__pcm_seff_BranchAction

    @pcm_seff_BranchAction.setter
    def pcm_seff_BranchAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_seff_BranchAction__pcm_seff_BranchAction", None)
        self.__pcm_seff_BranchAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AbstractBranchTransition"):
                    opp_val = getattr(item, "AbstractBranchTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "AbstractBranchTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AbstractBranchTransition"):
                    opp_val = getattr(item, "AbstractBranchTransition", None)
                    
                    setattr(item, "AbstractBranchTransition", self)
                    

    def EitherGuardedBranchesOrProbabilisiticBranchTransitions(self, pcm_context, pcm_diagnostics) :
        # TODO: Implement EitherGuardedBranchesOrProbabilisiticBranchTransitions method
        pass

    def AllProbabilisticBranchProbabilitiesMustSumUpTo1(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement AllProbabilisticBranchProbabilitiesMustSumUpTo1 method
        pass

class pcm_seff_ReleaseAction(AbstractInternalControlFlowAction):

    pass
class pcm_seff_AbstractLoopAction(AbstractInternalControlFlowAction):

    pass
class pcm_seff_StopAction(AbstractInternalControlFlowAction):

    def __init__(self, AbstractInternalControlFlowAction: "pcm_performance_ParametricResourceDemand" = None):
        
        pass
    def StopActionSuccessorMustNotBeDefined(self, pcm_diagnostics, pcm_context) :
        # TODO: Implement StopActionSuccessorMustNotBeDefined method
        pass

class parameter_pcm_AbstractNamedReference:

    pass
class VariableCharacterisation:

    pass
class pcm_parameter_VariableUsage:

    pass
class Variable:

    pass
class pcm_parameter_CharacterisedVariable(Variable):

    def __init__(self, characterisationType: str):
        self.characterisationType = characterisationType
        
        pass
    @property
    def characterisationType(self):
        return self.__characterisationType

    @characterisationType.setter
    def characterisationType(self, characterisationType: str):
        self.__characterisationType = characterisationType


class NamedElement:

    pass
class pcm_seff_AbstractBranchTransition(NamedElement):

    pass
class pcm_repository_InnerDeclaration(NamedElement):

    pass
class pcm_parameter_VariableCharacterisation:

    def __init__(self, type: str, pcm_parameter_VariableCharacterisation: "PCMRandomVariable" = None):
        self.type = type
        self.pcm_parameter_VariableCharacterisation = pcm_parameter_VariableCharacterisation
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def pcm_parameter_VariableCharacterisation(self):
        return self.__pcm_parameter_VariableCharacterisation

    @pcm_parameter_VariableCharacterisation.setter
    def pcm_parameter_VariableCharacterisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pcm_parameter_VariableCharacterisation__pcm_parameter_VariableCharacterisation", None)
        self.__pcm_parameter_VariableCharacterisation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PCMRandomVariable107"):
                opp_val = getattr(old_value, "PCMRandomVariable107", None)
                if opp_val == self:
                    setattr(old_value, "PCMRandomVariable107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PCMRandomVariable107"):
                opp_val = getattr(value, "PCMRandomVariable107", None)
                setattr(value, "PCMRandomVariable107", self)

class pcm_protocol_Protocol(ABC):

    def __init__(self, protocolTypeID: str):
        self.protocolTypeID = protocolTypeID
        
        pass
    @property
    def protocolTypeID(self):
        return self.__protocolTypeID

    @protocolTypeID.setter
    def protocolTypeID(self, protocolTypeID: str):
        self.__protocolTypeID = protocolTypeID


class pcm_protocol_ServiceCall(ABC):

    pass
class pcm_repository_ProvidedRole(Role):

    pass
class InnerDeclaration:

    pass
class CompositeDataType:

    pass