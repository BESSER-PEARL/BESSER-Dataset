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

class cm_seff_Automaton(ABC):

    pass
class seff_ServiceEffectSpecification:

    pass
class BranchAction:

    pass
class seff_Automaton:

    pass
class cm_seff_SimpleBehaviorSpecification(seff_ServiceEffectSpecification, seff_Automaton):

    pass
class AbstractAction:

    pass
class cm_seff_InternalAction(AbstractAction):

    pass
class cm_seff_BranchAction(AbstractAction):

    pass
class ProbabilisticBranchTransition:

    pass
class cm_seff_InternalBehaviour:

    pass
class InternalBehaviour:

    pass
class BasicComponent:

    pass
class cm_seff_ServiceEffectSpecification(ABC):

    pass
class cm_composition_Identifier(ABC):

    def __init__(self, id: str):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    def idHasToBeUnique(self, cm_context, cm_diagnostics) :
        # TODO: Implement idHasToBeUnique method
        pass

class cm_seff_ExternalCallAction(AbstractAction):

    pass
class cm_seff_StopAction(AbstractAction):

    pass
class cm_seff_StartAction(AbstractAction):

    pass
class Automaton:

    pass
class composition_InterfaceRequiringEntity:

    pass
class composition_InterfaceProvidingEntity:

    pass
class cm_composition_InterfaceProvidingRequiringEntity(composition_InterfaceProvidingEntity, composition_InterfaceRequiringEntity):

    pass
class repository_RepositoryComponent:

    pass
class ProvidedRole:

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
        
        pass
    @property
    def entityName(self):
        return self.__entityName

    @entityName.setter
    def entityName(self, entityName: str):
        self.__entityName = entityName


class composition_InterfaceProvidingRequiringEntity:

    pass
class composition_ComposedStructure:

    pass
class cm_composition_ComposedProvidingRequiringEntity(composition_ComposedStructure, composition_InterfaceProvidingRequiringEntity):

    pass
class RequiredRole:

    pass
class DelegationConnector:

    pass
class cm_composition_RequiredDelegationConnector(DelegationConnector):

    pass
class cm_composition_ProvidedDelegationConnector(DelegationConnector):

    def __init__(self, cm_composition_ProvidedDelegationConnector: "ProvidedRole" = None, cm_composition_ProvidedDelegationConnector46: "ProvidedRole" = None, cm_composition_ProvidedDelegationConnector49: "AssemblyContext" = None):
        self.cm_composition_ProvidedDelegationConnector = cm_composition_ProvidedDelegationConnector
        self.cm_composition_ProvidedDelegationConnector46 = cm_composition_ProvidedDelegationConnector46
        self.cm_composition_ProvidedDelegationConnector49 = cm_composition_ProvidedDelegationConnector49
        
        pass
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

    @property
    def cm_composition_ProvidedDelegationConnector49(self):
        return self.__cm_composition_ProvidedDelegationConnector49

    @cm_composition_ProvidedDelegationConnector49.setter
    def cm_composition_ProvidedDelegationConnector49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_composition_ProvidedDelegationConnector__cm_composition_ProvidedDelegationConnector49", None)
        self.__cm_composition_ProvidedDelegationConnector49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AssemblyContext50"):
                opp_val = getattr(old_value, "AssemblyContext50", None)
                if opp_val == self:
                    setattr(old_value, "AssemblyContext50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AssemblyContext50"):
                opp_val = getattr(value, "AssemblyContext50", None)
                setattr(value, "AssemblyContext50", self)

    @property
    def cm_composition_ProvidedDelegationConnector46(self):
        return self.__cm_composition_ProvidedDelegationConnector46

    @cm_composition_ProvidedDelegationConnector46.setter
    def cm_composition_ProvidedDelegationConnector46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_composition_ProvidedDelegationConnector__cm_composition_ProvidedDelegationConnector46", None)
        self.__cm_composition_ProvidedDelegationConnector46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProvidedRole47"):
                opp_val = getattr(old_value, "ProvidedRole47", None)
                if opp_val == self:
                    setattr(old_value, "ProvidedRole47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProvidedRole47"):
                opp_val = getattr(value, "ProvidedRole47", None)
                setattr(value, "ProvidedRole47", self)

    def ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure(self, cm_diagnostics, cm_context) :
        # TODO: Implement ProvidedDelegationConnectorandtheconnectedComponentmustbepartofthesamecompositestructure method
        pass

    def ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame(self, cm_diagnostics, cm_context) :
        # TODO: Implement ComponentOfAssemblyContextAndInnerRoleProvidingComponentNeedToBeTheSame method
        pass

class AssemblyContext:

    pass
class ComposedStructure:

    pass
class Connector:

    pass
class cm_composition_AssemblyConnector(Connector):

    def __init__(self, cm_composition_AssemblyConnector: "AssemblyContext" = None, cm_composition_AssemblyConnector61: "AssemblyContext" = None, cm_composition_AssemblyConnector64: "ProvidedRole" = None, cm_composition_AssemblyConnector67: "RequiredRole" = None, Connector: "cm_composition_ComposedStructure" = None):
        self.cm_composition_AssemblyConnector = cm_composition_AssemblyConnector
        self.cm_composition_AssemblyConnector61 = cm_composition_AssemblyConnector61
        self.cm_composition_AssemblyConnector64 = cm_composition_AssemblyConnector64
        self.cm_composition_AssemblyConnector67 = cm_composition_AssemblyConnector67
        
        pass
    @property
    def cm_composition_AssemblyConnector67(self):
        return self.__cm_composition_AssemblyConnector67

    @cm_composition_AssemblyConnector67.setter
    def cm_composition_AssemblyConnector67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_composition_AssemblyConnector__cm_composition_AssemblyConnector67", None)
        self.__cm_composition_AssemblyConnector67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RequiredRole68"):
                opp_val = getattr(old_value, "RequiredRole68", None)
                if opp_val == self:
                    setattr(old_value, "RequiredRole68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RequiredRole68"):
                opp_val = getattr(value, "RequiredRole68", None)
                setattr(value, "RequiredRole68", self)

    @property
    def cm_composition_AssemblyConnector61(self):
        return self.__cm_composition_AssemblyConnector61

    @cm_composition_AssemblyConnector61.setter
    def cm_composition_AssemblyConnector61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_composition_AssemblyConnector__cm_composition_AssemblyConnector61", None)
        self.__cm_composition_AssemblyConnector61 = value
        
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
    def cm_composition_AssemblyConnector64(self):
        return self.__cm_composition_AssemblyConnector64

    @cm_composition_AssemblyConnector64.setter
    def cm_composition_AssemblyConnector64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_composition_AssemblyConnector__cm_composition_AssemblyConnector64", None)
        self.__cm_composition_AssemblyConnector64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProvidedRole65"):
                opp_val = getattr(old_value, "ProvidedRole65", None)
                if opp_val == self:
                    setattr(old_value, "ProvidedRole65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProvidedRole65"):
                opp_val = getattr(value, "ProvidedRole65", None)
                setattr(value, "ProvidedRole65", self)

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
            if hasattr(old_value, "AssemblyContext59"):
                opp_val = getattr(old_value, "AssemblyContext59", None)
                if opp_val == self:
                    setattr(old_value, "AssemblyContext59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AssemblyContext59"):
                opp_val = getattr(value, "AssemblyContext59", None)
                setattr(value, "AssemblyContext59", self)

    def AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch(self, cm_diagnostics, cm_context) :
        # TODO: Implement AssemblyConnectorsReferencedProvidedRolesAndChildContextMustMatch method
        pass

    def AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch(self, cm_context, cm_diagnostics) :
        # TODO: Implement AssemblyConnectorsReferencedRequiredRoleAndChildContextMustMatch method
        pass

    def AssemblyConnectorsReferencedInterfacesMustMatch(self, cm_diagnostics, cm_context) :
        # TODO: Implement AssemblyConnectorsReferencedInterfacesMustMatch method
        pass

class cm_composition_DelegationConnector(Connector):

    pass
class NamedElement:

    pass
class cm_repository_InnerDeclaration(NamedElement):

    pass
class InnerDeclaration:

    pass
class CompositeDataType:

    pass
class repository_DataType:

    pass
class composition_Entity:

    pass
class cm_seff_ProbabilisticBranchTransition(composition_Entity, seff_Automaton):

    def __init__(self, branchProbability: float, branchTransitions: "BranchAction" = None):
        self.branchProbability = branchProbability
        self.branchTransitions = branchTransitions
        
        pass
    @property
    def branchProbability(self):
        return self.__branchProbability

    @branchProbability.setter
    def branchProbability(self, branchProbability: float):
        self.__branchProbability = branchProbability


    @property
    def branchTransitions(self):
        return self.__branchTransitions

    @branchTransitions.setter
    def branchTransitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_seff_ProbabilisticBranchTransition__branchTransitions", None)
        self.__branchTransitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BranchAction"):
                opp_val = getattr(old_value, "BranchAction", None)
                if opp_val == self:
                    setattr(old_value, "BranchAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BranchAction"):
                opp_val = getattr(value, "BranchAction", None)
                setattr(value, "BranchAction", self)

class cm_repository_CompositeDataType(repository_DataType, composition_Entity):

    pass
class cm_repository_CollectionDataType(repository_DataType, composition_Entity):

    pass
class repository_ComponentTypeImplementation:

    pass
class composition_ComposedProvidingRequiringEntity:

    pass
class cm_composition_System(composition_ComposedProvidingRequiringEntity, composition_Entity):

    def __init__(self):
        
        pass
    def SystemMustHaveAtLeastOneProvidedRole(self, cm_diagnostics, cm_context) :
        # TODO: Implement SystemMustHaveAtLeastOneProvidedRole method
        pass

class cm_composition_SubSystem(composition_ComposedProvidingRequiringEntity, repository_RepositoryComponent):

    pass
class cm_repository_CompositeComponent(repository_ComponentTypeImplementation, composition_ComposedProvidingRequiringEntity):

    def __init__(self):
        
        pass
    def ProvideSameInterfaces(self, cm_context, cm_diagnostics) :
        # TODO: Implement ProvideSameInterfaces method
        pass

    def RequireSameInterfaces(self, cm_diagnostics, cm_context) :
        # TODO: Implement RequireSameInterfaces method
        pass

class InterfaceRequiringEntity:

    pass
class cm_repository_ExceptionType:

    def __init__(self, name: str, message: str):
        self.name = name
        self.message = message
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, message: str):
        self.__message = message


class Parameter:

    pass
class ExceptionType:

    pass
class InterfaceProvidingRequiringEntity:

    pass
class cm_repository_RepositoryComponent(InterfaceProvidingRequiringEntity):

    pass
class ComponentType:

    pass
class Entity:

    pass
class cm_composition_Connector(Entity):

    pass
class cm_composition_InterfaceProvidingEntity(Entity):

    pass
class cm_composition_InterfaceRequiringEntity(Entity):

    pass
class cm_seff_AbstractAction(Entity):

    pass
class cm_repository_Signature(Entity):

    pass
class cm_composition_AssemblyContext(Entity):

    pass
class cm_composition_ComposedStructure(Entity):

    def __init__(self, parentStructure: set["AssemblyContext"] = None, parentStructure43: set["Connector"] = None):
        self.parentStructure = parentStructure if parentStructure is not None else set()
        self.parentStructure43 = parentStructure43 if parentStructure43 is not None else set()
        
        pass
    @property
    def parentStructure43(self):
        return self.__parentStructure43

    @parentStructure43.setter
    def parentStructure43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_composition_ComposedStructure__parentStructure43", None)
        self.__parentStructure43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Connector"):
                    opp_val = getattr(item, "Connector", None)
                    
                    if opp_val == self:
                        setattr(item, "Connector", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Connector"):
                    opp_val = getattr(item, "Connector", None)
                    
                    setattr(item, "Connector", self)
                    

    @property
    def parentStructure(self):
        return self.__parentStructure

    @parentStructure.setter
    def parentStructure(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_composition_ComposedStructure__parentStructure", None)
        self.__parentStructure = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "AssemblyContext"):
                    opp_val = getattr(item, "AssemblyContext", None)
                    
                    if opp_val == self:
                        setattr(item, "AssemblyContext", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "AssemblyContext"):
                    opp_val = getattr(item, "AssemblyContext", None)
                    
                    setattr(item, "AssemblyContext", self)
                    

    def MultipleConnectorsConstraint(self, cm_context, cm_diagnostics) :
        # TODO: Implement MultipleConnectorsConstraint method
        pass

    def MultipleConnectorsConstraintForAssemblyConnectors(self, cm_context, cm_diagnostics) :
        # TODO: Implement MultipleConnectorsConstraintForAssemblyConnectors method
        pass

class cm_repository_Repository(Entity):

    def __init__(self, description: str, repository: set["RepositoryComponent"] = None, repository11: set["Interface"] = None, repository14: set["DataType"] = None):
        self.description = description
        self.repository = repository if repository is not None else set()
        self.repository11 = repository11 if repository11 is not None else set()
        self.repository14 = repository14 if repository14 is not None else set()
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def repository11(self):
        return self.__repository11

    @repository11.setter
    def repository11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_repository_Repository__repository11", None)
        self.__repository11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Interface12"):
                    opp_val = getattr(item, "Interface12", None)
                    
                    if opp_val == self:
                        setattr(item, "Interface12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Interface12"):
                    opp_val = getattr(item, "Interface12", None)
                    
                    setattr(item, "Interface12", self)
                    

    @property
    def repository14(self):
        return self.__repository14

    @repository14.setter
    def repository14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_repository_Repository__repository14", None)
        self.__repository14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DataType15"):
                    opp_val = getattr(item, "DataType15", None)
                    
                    if opp_val == self:
                        setattr(item, "DataType15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DataType15"):
                    opp_val = getattr(item, "DataType15", None)
                    
                    setattr(item, "DataType15", self)
                    

    @property
    def repository(self):
        return self.__repository

    @repository.setter
    def repository(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_repository_Repository__repository", None)
        self.__repository = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RepositoryComponent"):
                    opp_val = getattr(item, "RepositoryComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "RepositoryComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RepositoryComponent"):
                    opp_val = getattr(item, "RepositoryComponent", None)
                    
                    setattr(item, "RepositoryComponent", self)
                    

class cm_repository_Interface(Entity):

    pass
class cm_repository_Role(Entity):

    pass
class cm_repository_DataType(ABC):

    pass
class Signature:

    pass
class DataType:

    pass
class cm_repository_PrimitiveDataType(DataType):

    def __init__(self, type: str, DataType15: "cm_repository_Repository" = None, DataType: "cm_repository_Parameter" = None, DataType37: "cm_repository_InnerDeclaration" = None, DataType26: "cm_repository_Signature" = None, DataType33: "cm_repository_CollectionDataType" = None):
        self.type = type
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


class cm_repository_Parameter:

    def __init__(self, name: str, cm_repository_Parameter: "DataType" = None, parameters: "Signature" = None):
        self.name = name
        self.cm_repository_Parameter = cm_repository_Parameter
        self.parameters = parameters
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def parameters(self):
        return self.__parameters

    @parameters.setter
    def parameters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cm_repository_Parameter__parameters", None)
        self.__parameters = value
        
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
class Repository:

    pass
class RepositoryComponent:

    pass
class cm_repository_ComponentType(RepositoryComponent):

    pass
class cm_repository_ComponentTypeImplementation(RepositoryComponent):

    pass
class ServiceEffectSpecification:

    pass
class ComponentTypeImplementation:

    pass
class cm_repository_BasicComponent(ComponentTypeImplementation):

    pass