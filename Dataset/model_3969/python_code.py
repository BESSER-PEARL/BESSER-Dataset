from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class standard_SystemModel:

    pass
class standard_Model:

    pass
class standard_Metamodel:

    pass
class standard_BuildComponent:

    pass
class standard_Type:

    def __init__(self, standard_Type: "standard_Class" = None):
        self.standard_Type = standard_Type
        
    @property
    def standard_Type(self):
        return self.__standard_Type

    @standard_Type.setter
    def standard_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_Type__standard_Type", None)
        self.__standard_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_Class44"):
                opp_val = getattr(old_value, "standard_Class44", None)
                if opp_val == self:
                    setattr(old_value, "standard_Class44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_Class44"):
                opp_val = getattr(value, "standard_Class44", None)
                setattr(value, "standard_Class44", self)

    def cannot_be_specification(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement cannot_be_specification method
        pass

class standard_Trace:

    pass
class standard_Subsystem:

    pass
class standard_Specification:

    def __init__(self, standard_Specification: "standard_Classifier" = None):
        self.standard_Specification = standard_Specification
        
    @property
    def standard_Specification(self):
        return self.__standard_Specification

    @standard_Specification.setter
    def standard_Specification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_Specification__standard_Specification", None)
        self.__standard_Specification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_Classifier38"):
                opp_val = getattr(old_value, "standard_Classifier38", None)
                if opp_val == self:
                    setattr(old_value, "standard_Classifier38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_Classifier38"):
                opp_val = getattr(value, "standard_Classifier38", None)
                setattr(value, "standard_Classifier38", self)

    def cannot_be_type(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement cannot_be_type method
        pass

class standard_Utility:

    def __init__(self, standard_Utility: "standard_Class" = None):
        self.standard_Utility = standard_Utility
        
    @property
    def standard_Utility(self):
        return self.__standard_Utility

    @standard_Utility.setter
    def standard_Utility(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_Utility__standard_Utility", None)
        self.__standard_Utility = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_Class46"):
                opp_val = getattr(old_value, "standard_Class46", None)
                if opp_val == self:
                    setattr(old_value, "standard_Class46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_Class46"):
                opp_val = getattr(value, "standard_Class46", None)
                setattr(value, "standard_Class46", self)

    def is_utility(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement is_utility method
        pass

class standard_Send:

    def __init__(self, standard_Send: "standard_Usage" = None):
        self.standard_Send = standard_Send
        
    @property
    def standard_Send(self):
        return self.__standard_Send

    @standard_Send.setter
    def standard_Send(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_Send__standard_Send", None)
        self.__standard_Send = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_Usage34"):
                opp_val = getattr(old_value, "standard_Usage34", None)
                if opp_val == self:
                    setattr(old_value, "standard_Usage34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_Usage34"):
                opp_val = getattr(value, "standard_Usage34", None)
                setattr(value, "standard_Usage34", self)

    def client_operation_sends_supplier_signal(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement client_operation_sends_supplier_signal method
        pass

class standard_Responsibility:

    pass
class standard_Refine:

    pass
class standard_Classifier:

    pass
class standard_Service:

    pass
class standard_Process:

    pass
class standard_ModelLibrary:

    pass
class standard_Metaclass:

    pass
class standard_Instantiate:

    def __init__(self, standard_Instantiate: "standard_Usage" = None):
        self.standard_Instantiate = standard_Instantiate
        
    @property
    def standard_Instantiate(self):
        return self.__standard_Instantiate

    @standard_Instantiate.setter
    def standard_Instantiate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_Instantiate__standard_Instantiate", None)
        self.__standard_Instantiate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_Usage21"):
                opp_val = getattr(old_value, "standard_Usage21", None)
                if opp_val == self:
                    setattr(old_value, "standard_Usage21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_Usage21"):
                opp_val = getattr(value, "standard_Usage21", None)
                setattr(value, "standard_Usage21", self)

    def client_and_supplier_are_classifiers(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement client_and_supplier_are_classifiers method
        pass

class standard_Realization:

    def __init__(self, standard_Realization: "standard_Classifier" = None):
        self.standard_Realization = standard_Realization
        
    @property
    def standard_Realization(self):
        return self.__standard_Realization

    @standard_Realization.setter
    def standard_Realization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_Realization__standard_Realization", None)
        self.__standard_Realization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_Classifier"):
                opp_val = getattr(old_value, "standard_Classifier", None)
                if opp_val == self:
                    setattr(old_value, "standard_Classifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_Classifier"):
                opp_val = getattr(value, "standard_Classifier", None)
                setattr(value, "standard_Classifier", self)

    def cannot_be_implementationClass(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement cannot_be_implementationClass method
        pass

class standard_ImplementationClass:

    def __init__(self, standard_ImplementationClass: "standard_Class" = None):
        self.standard_ImplementationClass = standard_ImplementationClass
        
    @property
    def standard_ImplementationClass(self):
        return self.__standard_ImplementationClass

    @standard_ImplementationClass.setter
    def standard_ImplementationClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_ImplementationClass__standard_ImplementationClass", None)
        self.__standard_ImplementationClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_Class19"):
                opp_val = getattr(old_value, "standard_Class19", None)
                if opp_val == self:
                    setattr(old_value, "standard_Class19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_Class19"):
                opp_val = getattr(value, "standard_Class19", None)
                setattr(value, "standard_Class19", self)

    def cannot_be_realization(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement cannot_be_realization method
        pass

class standard_Implement:

    def __init__(self, standard_Implement: "standard_Component" = None):
        self.standard_Implement = standard_Implement
        
    @property
    def standard_Implement(self):
        return self.__standard_Implement

    @standard_Implement.setter
    def standard_Implement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_Implement__standard_Implement", None)
        self.__standard_Implement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_Component17"):
                opp_val = getattr(old_value, "standard_Component17", None)
                if opp_val == self:
                    setattr(old_value, "standard_Component17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_Component17"):
                opp_val = getattr(value, "standard_Component17", None)
                setattr(value, "standard_Component17", self)

    def implements_specification(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement implements_specification method
        pass

class standard_Package:

    pass
class standard_Framework:

    pass
class standard_Focus:

    pass
class standard_Artifact:

    pass
class standard_File(ABC):

    pass
class File:

    pass
class standard_Library(File):

    pass
class standard_Script(File):

    pass
class standard_Source(File):

    pass
class standard_Document(File):

    pass
class standard_Destroy:

    pass
class standard_Abstraction:

    pass
class standard_ValueSpecification:

    pass
class standard_Derive:

    pass
class standard_BehavioralFeature:

    pass
class standard_Executable(File):

    pass
class standard_Component:

    pass
class standard_Entity:

    pass
class standard_Usage:

    pass
class standard_Call:

    def __init__(self, standard_Call: "standard_Usage" = None):
        self.standard_Call = standard_Call
        
    @property
    def standard_Call(self):
        return self.__standard_Call

    @standard_Call.setter
    def standard_Call(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_Call__standard_Call", None)
        self.__standard_Call = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_Usage"):
                opp_val = getattr(old_value, "standard_Usage", None)
                if opp_val == self:
                    setattr(old_value, "standard_Usage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_Usage"):
                opp_val = getattr(value, "standard_Usage", None)
                setattr(value, "standard_Usage", self)

    def client_and_supplier_are_operations(self, context: str, diagnostics: str) -> bool:
        # TODO: Implement client_and_supplier_are_operations method
        pass

class standard_Class:

    pass
class standard_Auxiliary:

    pass
class standard_Create:

    def __init__(self, standard_Create: "standard_BehavioralFeature" = None, standard_Create4: "standard_Usage" = None):
        self.standard_Create = standard_Create
        self.standard_Create4 = standard_Create4
        
    @property
    def standard_Create(self):
        return self.__standard_Create

    @standard_Create.setter
    def standard_Create(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_Create__standard_Create", None)
        self.__standard_Create = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_BehavioralFeature"):
                opp_val = getattr(old_value, "standard_BehavioralFeature", None)
                if opp_val == self:
                    setattr(old_value, "standard_BehavioralFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_BehavioralFeature"):
                opp_val = getattr(value, "standard_BehavioralFeature", None)
                setattr(value, "standard_BehavioralFeature", self)

    @property
    def standard_Create4(self):
        return self.__standard_Create4

    @standard_Create4.setter
    def standard_Create4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_standard_Create__standard_Create4", None)
        self.__standard_Create4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "standard_Usage5"):
                opp_val = getattr(old_value, "standard_Usage5", None)
                if opp_val == self:
                    setattr(old_value, "standard_Usage5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "standard_Usage5"):
                opp_val = getattr(value, "standard_Usage5", None)
                setattr(value, "standard_Usage5", self)

    def client_and_supplier_are_classifiers(self, diagnostics: str, context: str) -> bool:
        # TODO: Implement client_and_supplier_are_classifiers method
        pass
