from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PrimitiveType(Enum):
    INT = "INT"
    STRING = "STRING"
    BOOL = "BOOL"
    DOUBLE = "DOUBLE"
    CHAR = "CHAR"
    BYTE = "BYTE"
    LONG = "LONG"


############################################
# Definition of Classes
############################################

class Automaton:

    pass
class AbstractAction:

    pass
class ProbabilisticBranchTransition:

    pass
class cm_seff_InternalBehaviour:

    pass
class InternalBehaviour:

    pass
class cm_seff_Automaton(ABC):

    pass
class cm_seff_InternalAction(AbstractAction):

    pass
class seff_ServiceEffectSpecification:

    pass
class BranchAction:

    pass
class seff_Automaton:

    pass
class cm_seff_SimpleBehaviorSpecification(seff_Automaton, seff_ServiceEffectSpecification):

    pass
class cm_seff_BranchAction(AbstractAction):

    pass
class cm_seff_ExternalCallAction(AbstractAction):

    pass
class cm_seff_StopAction(AbstractAction):

    pass
class cm_seff_StartAction(AbstractAction):

    pass
class composition_InterfaceRequiringEntity:

    pass
class composition_InterfaceProvidingEntity:

    pass
class cm_composition_InterfaceProvidingRequiringEntity(composition_InterfaceRequiringEntity, composition_InterfaceProvidingEntity):

    pass
class repository_RepositoryComponent:

    pass
class BasicComponent:

    pass
class cm_seff_ServiceEffectSpecification(ABC):

    pass
class cm_composition_Identifier(ABC):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    def idHasToBeUnique(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement idHasToBeUnique method
        pass

class composition_Identifier:

    pass
class composition_NamedElement:

    pass
class cm_composition_Entity(composition_NamedElement, composition_Identifier):

    pass
class cm_composition_NamedElement(ABC):

    def __init__(self, entityName: str):
        self.entityName = entityName
        
    @property
    def entityName(self) -> str:
        return self.__entityName

    @entityName.setter
    def entityName(self, entityName: str):
        self.__entityName = entityName

class composition_InterfaceProvidingRequiringEntity:

    pass
class composition_ComposedStructure:

    pass
class cm_composition_ComposedProvidingRequiringEntity(composition_InterfaceProvidingRequiringEntity, composition_ComposedStructure):

    pass
class RequiredRole:

    pass
class ProvidedRole:

    pass
class NamedElement:

    pass
class cm_repository_InnerDeclaration(NamedElement):

    pass
class InnerDeclaration:

    pass
class CompositeDataType:

    pass
class DelegationConnector:

    pass
class cm_composition_RequiredDelegationConnector(DelegationConnector):

    pass
class cm_composition_ProvidedDelegationConnector(DelegationConnector):

    def __init__(self, cm_composition_ProvidedDelegationConnector: "ProvidedRole" = None, cm_composition_ProvidedDelegationConnector58: "ProvidedRole" = None, cm_composition_ProvidedDelegationConnector61: "AssemblyContext" = None):
        self.cm_composition_ProvidedDelegationConnector = cm_composition_ProvidedDelegationConnector
        self.cm_composition_ProvidedDelegationConnector58 = cm_composition_ProvidedDelegationConnector58
        self.cm_composition_ProvidedDelegationConnector61 = cm_composition_ProvidedDelegationConnector61
        
    @property
    def cm_composition_ProvidedDelegationConnector61(self):
        return self.__cm_composition_ProvidedDelegationConnector61

    @cm_composition_ProvidedDelegationConnector61.setter
    def cm_composition_ProvidedDelegationConnector61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_composition_ProvidedDelegationConnector__cm_composition_ProvidedDelegationConnector61", None)
        self.__cm_composition_ProvidedDelegationConnector61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AssemblyContext62"):
                opp_val = getattr(old_value, "AssemblyContext62", None)
                if opp_val == self:
                    setattr(old_value, "AssemblyContext62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AssemblyContext62"):
                opp_val = getattr(value, "AssemblyContext62", None)
                setattr(value, "AssemblyContext62", self)

    @property
    def cm_composition_ProvidedDelegationConnector58(self):
        return self.__cm_composition_ProvidedDelegationConnector58

    @cm_composition_ProvidedDelegationConnector58.setter
    def cm_composition_ProvidedDelegationConnector58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_composition_ProvidedDelegationConnector__cm_composition_ProvidedDelegationConnector58", None)
        self.__cm_composition_ProvidedDelegationConnector58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProvidedRole59"):
                opp_val = getattr(old_value, "ProvidedRole59", None)
                if opp_val == self:
                    setattr(old_value, "ProvidedRole59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProvidedRole59"):
                opp_val = getattr(value, "ProvidedRole59", None)
                setattr(value, "ProvidedRole59", self)

    @property
    def cm_composition_ProvidedDelegationConnector(self):
        return self.__cm_composition_ProvidedDelegationConnector

    @cm_composition_ProvidedDelegationConnector.setter
    def cm_composition_ProvidedDelegationConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_composition_ProvidedDelegationConnector__cm_composition_ProvidedDelegationConnector", None)
        self.__cm_composition_ProvidedDelegationConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProvidedRole"):
                opp_val = getattr(old_value, "ProvidedRole", None)
                if opp_val == self:
                    setattr(old_value, "ProvidedRole", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProvidedRole"):
                opp_val = getattr(value, "ProvidedRole", None)
                setattr(value, "ProvidedRole", self)

    def ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

    def ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame method
        pass

class AssemblyContext:

    pass
class ComposedStructure:

    pass
class Connector:

    pass
class cm_composition_AssemblyConnector(Connector):

    def __init__(self, cm_composition_AssemblyConnector: "AssemblyContext" = None, cm_composition_AssemblyConnector73: "AssemblyContext" = None, cm_composition_AssemblyConnector76: "ProvidedRole" = None, cm_composition_AssemblyConnector79: "RequiredRole" = None, composition55: "cm_composition_ComposedStructure"):
        self.cm_composition_AssemblyConnector = cm_composition_AssemblyConnector
        self.cm_composition_AssemblyConnector73 = cm_composition_AssemblyConnector73
        self.cm_composition_AssemblyConnector76 = cm_composition_AssemblyConnector76
        self.cm_composition_AssemblyConnector79 = cm_composition_AssemblyConnector79
        
    @property
    def cm_composition_AssemblyConnector79(self):
        return self.__cm_composition_AssemblyConnector79

    @cm_composition_AssemblyConnector79.setter
    def cm_composition_AssemblyConnector79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_composition_AssemblyConnector__cm_composition_AssemblyConnector79", None)
        self.__cm_composition_AssemblyConnector79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RequiredRole80"):
                opp_val = getattr(old_value, "RequiredRole80", None)
                if opp_val == self:
                    setattr(old_value, "RequiredRole80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RequiredRole80"):
                opp_val = getattr(value, "RequiredRole80", None)
                setattr(value, "RequiredRole80", self)

    @property
    def cm_composition_AssemblyConnector76(self):
        return self.__cm_composition_AssemblyConnector76

    @cm_composition_AssemblyConnector76.setter
    def cm_composition_AssemblyConnector76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_composition_AssemblyConnector__cm_composition_AssemblyConnector76", None)
        self.__cm_composition_AssemblyConnector76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProvidedRole77"):
                opp_val = getattr(old_value, "ProvidedRole77", None)
                if opp_val == self:
                    setattr(old_value, "ProvidedRole77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProvidedRole77"):
                opp_val = getattr(value, "ProvidedRole77", None)
                setattr(value, "ProvidedRole77", self)

    @property
    def cm_composition_AssemblyConnector(self):
        return self.__cm_composition_AssemblyConnector

    @cm_composition_AssemblyConnector.setter
    def cm_composition_AssemblyConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_composition_AssemblyConnector__cm_composition_AssemblyConnector", None)
        self.__cm_composition_AssemblyConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AssemblyContext71"):
                opp_val = getattr(old_value, "AssemblyContext71", None)
                if opp_val == self:
                    setattr(old_value, "AssemblyContext71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AssemblyContext71"):
                opp_val = getattr(value, "AssemblyContext71", None)
                setattr(value, "AssemblyContext71", self)

    @property
    def cm_composition_AssemblyConnector73(self):
        return self.__cm_composition_AssemblyConnector73

    @cm_composition_AssemblyConnector73.setter
    def cm_composition_AssemblyConnector73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_composition_AssemblyConnector__cm_composition_AssemblyConnector73", None)
        self.__cm_composition_AssemblyConnector73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AssemblyContext74"):
                opp_val = getattr(old_value, "AssemblyContext74", None)
                if opp_val == self:
                    setattr(old_value, "AssemblyContext74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AssemblyContext74"):
                opp_val = getattr(value, "AssemblyContext74", None)
                setattr(value, "AssemblyContext74", self)

    def AssemblyConnectorsReferencedInterfacesMustMatch(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement AssemblyConnectorsReferencedInterfacesMustMatch method
        pass

    def AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch method
        pass

    def AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch method
        pass

class cm_composition_DelegationConnector(Connector):

    pass
class repository_DataType:

    pass
class composition_Entity:

    pass
class cm_repository_CompositeDataType(repository_DataType, composition_Entity):

    pass
class cm_seff_ProbabilisticBranchTransition(seff_Automaton, composition_Entity):

    def __init__(self, branchProbability: float, BranchAction: "BranchAction" = None):
        self.branchProbability = branchProbability
        self.BranchAction = BranchAction
        
    @property
    def branchProbability(self) -> float:
        return self.__branchProbability

    @branchProbability.setter
    def branchProbability(self, branchProbability: float):
        self.__branchProbability = branchProbability

    @property
    def BranchAction(self):
        return self.__BranchAction

    @BranchAction.setter
    def BranchAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_seff_ProbabilisticBranchTransition__BranchAction", None)
        self.__BranchAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "seff124"):
                opp_val = getattr(old_value, "seff124", None)
                if opp_val == self:
                    setattr(old_value, "seff124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "seff124"):
                opp_val = getattr(value, "seff124", None)
                setattr(value, "seff124", self)

class cm_repository_CollectionDataType(repository_DataType, composition_Entity):

    pass
class Parameter:

    pass
class ExceptionType:

    pass
class repository_ComponentTypeImplementation:

    pass
class composition_ComposedProvidingRequiringEntity:

    pass
class cm_composition_SubSystem(composition_ComposedProvidingRequiringEntity, repository_RepositoryComponent):

    pass
class cm_composition_System(composition_ComposedProvidingRequiringEntity, composition_Entity):

    def __init__(self):
        
    def SystemMustHaveAtLeastOneProvidedRole(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement SystemMustHaveAtLeastOneProvidedRole method
        pass

class cm_repository_CompositeComponent(composition_ComposedProvidingRequiringEntity, repository_ComponentTypeImplementation):

    def __init__(self):
        
    def ProvideSameInterfaces(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement ProvideSameInterfaces method
        pass

    def RequireSameInterfaces(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement RequireSameInterfaces method
        pass

class InterfaceRequiringEntity:

    pass
class cm_repository_ExceptionType:

    def __init__(self, name: str, message: str):
        self.name = name
        self.message = message
        
    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Entity:

    pass
class cm_repository_Signature(Entity):

    pass
class cm_repository_Repository(Entity):

    def __init__(self, description: str, Interface14: set["Interface"] = None, DataType17: set["DataType"] = None, RepositoryComponent: set["RepositoryComponent"] = None):
        self.description = description
        self.Interface14 = Interface14 if Interface14 is not None else set()
        self.DataType17 = DataType17 if DataType17 is not None else set()
        self.RepositoryComponent = RepositoryComponent if RepositoryComponent is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def DataType17(self):
        return self.__DataType17

    @DataType17.setter
    def DataType17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_repository_Repository__DataType17", None)
        self.__DataType17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository18"):
                    opp_val = getattr(item, "repository18", None)
                    
                    if opp_val == self:
                        setattr(item, "repository18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository18"):
                    opp_val = getattr(item, "repository18", None)
                    
                    setattr(item, "repository18", self)
                    

    @property
    def RepositoryComponent(self):
        return self.__RepositoryComponent

    @RepositoryComponent.setter
    def RepositoryComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_repository_Repository__RepositoryComponent", None)
        self.__RepositoryComponent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository12"):
                    opp_val = getattr(item, "repository12", None)
                    
                    if opp_val == self:
                        setattr(item, "repository12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository12"):
                    opp_val = getattr(item, "repository12", None)
                    
                    setattr(item, "repository12", self)
                    

    @property
    def Interface14(self):
        return self.__Interface14

    @Interface14.setter
    def Interface14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_repository_Repository__Interface14", None)
        self.__Interface14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "repository15"):
                    opp_val = getattr(item, "repository15", None)
                    
                    if opp_val == self:
                        setattr(item, "repository15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "repository15"):
                    opp_val = getattr(item, "repository15", None)
                    
                    setattr(item, "repository15", self)
                    

class cm_composition_InterfaceRequiringEntity(Entity):

    pass
class cm_composition_Connector(Entity):

    pass
class cm_composition_ComposedStructure(Entity):

    def __init__(self, AssemblyContext: set["AssemblyContext"] = None, Connector: set["Connector"] = None):
        self.AssemblyContext = AssemblyContext if AssemblyContext is not None else set()
        self.Connector = Connector if Connector is not None else set()
        
    @property
    def Connector(self):
        return self.__Connector

    @Connector.setter
    def Connector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_composition_ComposedStructure__Connector", None)
        self.__Connector = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "composition55"):
                    opp_val = getattr(item, "composition55", None)
                    
                    if opp_val == self:
                        setattr(item, "composition55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "composition55"):
                    opp_val = getattr(item, "composition55", None)
                    
                    setattr(item, "composition55", self)
                    

    @property
    def AssemblyContext(self):
        return self.__AssemblyContext

    @AssemblyContext.setter
    def AssemblyContext(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_composition_ComposedStructure__AssemblyContext", None)
        self.__AssemblyContext = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "composition53"):
                    opp_val = getattr(item, "composition53", None)
                    
                    if opp_val == self:
                        setattr(item, "composition53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "composition53"):
                    opp_val = getattr(item, "composition53", None)
                    
                    setattr(item, "composition53", self)
                    

    def MultipleConnectorsConstraintForAssemblyConnectors(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MultipleConnectorsConstraintForAssemblyConnectors method
        pass

    def MultipleConnectorsConstraint(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement MultipleConnectorsConstraint method
        pass

class cm_composition_AssemblyContext(Entity):

    pass
class cm_composition_InterfaceProvidingEntity(Entity):

    pass
class cm_seff_AbstractAction(Entity):

    pass
class cm_repository_Role(Entity):

    pass
class cm_repository_Interface(Entity):

    pass
class Repository:

    pass
class InterfaceProvidingRequiringEntity:

    pass
class cm_repository_RepositoryComponent(InterfaceProvidingRequiringEntity):

    pass
class ComponentType:

    pass
class RepositoryComponent:

    pass
class cm_repository_ComponentTypeImplementation(RepositoryComponent):

    pass
class ServiceEffectSpecification:

    pass
class cm_repository_DataType(ABC):

    pass
class Signature:

    pass
class DataType:

    pass
class cm_repository_PrimitiveDataType(DataType):

    def __init__(self, type: str, DataType32: "cm_repository_Signature", DataType41: "cm_repository_CollectionDataType", DataType46: "cm_repository_InnerDeclaration", repository18: "cm_repository_Repository", DataType: "cm_repository_Parameter"):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class cm_repository_Parameter:

    def __init__(self, name: str, cm_repository_Parameter: "DataType" = None, Signature: "Signature" = None):
        self.name = name
        self.cm_repository_Parameter = cm_repository_Parameter
        self.Signature = Signature
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Signature(self):
        return self.__Signature

    @Signature.setter
    def Signature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_repository_Parameter__Signature", None)
        self.__Signature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "repository7"):
                opp_val = getattr(old_value, "repository7", None)
                if opp_val == self:
                    setattr(old_value, "repository7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "repository7"):
                opp_val = getattr(value, "repository7", None)
                setattr(value, "repository7", self)

    @property
    def cm_repository_Parameter(self):
        return self.__cm_repository_Parameter

    @cm_repository_Parameter.setter
    def cm_repository_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_repository_Parameter__cm_repository_Parameter", None)
        self.__cm_repository_Parameter = value
        
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

class Interface:

    pass
class InterfaceProvidingEntity:

    pass
class Role:

    pass
class cm_repository_RequiredRole(Role):

    pass
class cm_repository_ProvidedRole(Role):

    pass
class cm_repository_ComponentType(RepositoryComponent):

    pass
class ComponentTypeImplementation:

    pass
class cm_repository_BasicComponent(ComponentTypeImplementation):

    pass