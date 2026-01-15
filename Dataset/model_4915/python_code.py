from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ServiceType(Enum):
    internal = "internal"
    external = "external"
class StyleEncoding(Enum):
    Document_Literal = "Document_Literal"
    RPC_Encoded = "RPC_Encoded"
class ServiceImpLanguage(Enum):
    Java_EJB = "Java_EJB"
    Java_JSP = "Java_JSP"
class ContainerType(Enum):
    axis = "axis"
class TransportProtocol(Enum):
    SOAP = "SOAP"
    HTTP = "HTTP"
    MIME = "MIME"


############################################
# Definition of Classes
############################################

class service_architecture_ServiceDirectory:

    pass
class architecture_TemplateMatchmaker:

    pass
class architecture_ServiceMatchmaker:

    pass
class service_architecture_ServiceTemplateMatchmaker(architecture_ServiceMatchmaker, architecture_TemplateMatchmaker):

    pass
class service_architecture_ServiceMatchmaker:

    pass
class service_architecture_TemplateMatchmaker:

    pass
class service_architecture_TemplateRepository:

    pass
class service_architecture_DeployedService:

    def __init__(self, artifact: str, ExecutionFramework191: "ExecutionFramework" = None):
        self.artifact = artifact
        self.ExecutionFramework191 = ExecutionFramework191
        
    @property
    def artifact(self) -> str:
        return self.__artifact

    @artifact.setter
    def artifact(self, artifact: str):
        self.__artifact = artifact

    @property
    def ExecutionFramework191(self):
        return self.__ExecutionFramework191

    @ExecutionFramework191.setter
    def ExecutionFramework191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_architecture_DeployedService__ExecutionFramework191", None)
        self.__ExecutionFramework191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "architecture192"):
                opp_val = getattr(old_value, "architecture192", None)
                if opp_val == self:
                    setattr(old_value, "architecture192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "architecture192"):
                opp_val = getattr(value, "architecture192", None)
                setattr(value, "architecture192", self)

class service_architecture_ExecutionFramework:

    def __init__(self, container: str, DeployedService189: set["DeployedService"] = None):
        self.container = container
        self.DeployedService189 = DeployedService189 if DeployedService189 is not None else set()
        
    @property
    def container(self) -> str:
        return self.__container

    @container.setter
    def container(self, container: str):
        self.__container = container

    @property
    def DeployedService189(self):
        return self.__DeployedService189

    @DeployedService189.setter
    def DeployedService189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_architecture_ExecutionFramework__DeployedService189", None)
        self.__DeployedService189 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "architecture"):
                    opp_val = getattr(item, "architecture", None)
                    
                    if opp_val == self:
                        setattr(item, "architecture", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "architecture"):
                    opp_val = getattr(item, "architecture", None)
                    
                    setattr(item, "architecture", self)
                    

class service_template_ControlConstructList:

    pass
class ControlConstructList:

    pass
class TemplateRepository:

    pass
class ServiceDirectory:

    pass
class ExecutionFramework:

    pass
class ServiceTemplateMatchmaker:

    pass
class service_architecture_ServiceFramework:

    pass
class service_template_IntervalThing:

    pass
class service_template_ControlConstructBag:

    pass
class ControlConstructBag:

    pass
class IntervalThing:

    pass
class Iterate:

    pass
class service_template_RepeatWhile(Iterate):

    pass
class service_template_RepeatUntil(Iterate):

    pass
class BoundProcessModel:

    pass
class BoundTemplateParameter:

    pass
class ServiceTemplate:

    pass
class service_template_GroundTemplate:

    def __init__(self, name: str, adaptedBy: "template_service_Service" = None, service_template_GroundTemplate: "ServiceTemplate" = None, service_template_GroundTemplate100: set["BoundTemplateParameter"] = None, service_template_GroundTemplate102: set["BoundProcessModel"] = None):
        self.name = name
        self.adaptedBy = adaptedBy
        self.service_template_GroundTemplate = service_template_GroundTemplate
        self.service_template_GroundTemplate100 = service_template_GroundTemplate100 if service_template_GroundTemplate100 is not None else set()
        self.service_template_GroundTemplate102 = service_template_GroundTemplate102 if service_template_GroundTemplate102 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def service_template_GroundTemplate100(self):
        return self.__service_template_GroundTemplate100

    @service_template_GroundTemplate100.setter
    def service_template_GroundTemplate100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_template_GroundTemplate__service_template_GroundTemplate100", None)
        self.__service_template_GroundTemplate100 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BoundTemplateParameter"):
                    opp_val = getattr(item, "BoundTemplateParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "BoundTemplateParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BoundTemplateParameter"):
                    opp_val = getattr(item, "BoundTemplateParameter", None)
                    
                    setattr(item, "BoundTemplateParameter", self)
                    

    @property
    def service_template_GroundTemplate102(self):
        return self.__service_template_GroundTemplate102

    @service_template_GroundTemplate102.setter
    def service_template_GroundTemplate102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_template_GroundTemplate__service_template_GroundTemplate102", None)
        self.__service_template_GroundTemplate102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BoundProcessModel"):
                    opp_val = getattr(item, "BoundProcessModel", None)
                    
                    if opp_val == self:
                        setattr(item, "BoundProcessModel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BoundProcessModel"):
                    opp_val = getattr(item, "BoundProcessModel", None)
                    
                    setattr(item, "BoundProcessModel", self)
                    

    @property
    def service_template_GroundTemplate(self):
        return self.__service_template_GroundTemplate

    @service_template_GroundTemplate.setter
    def service_template_GroundTemplate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_template_GroundTemplate__service_template_GroundTemplate", None)
        self.__service_template_GroundTemplate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ServiceTemplate"):
                opp_val = getattr(old_value, "ServiceTemplate", None)
                if opp_val == self:
                    setattr(old_value, "ServiceTemplate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ServiceTemplate"):
                opp_val = getattr(value, "ServiceTemplate", None)
                setattr(value, "ServiceTemplate", self)

    @property
    def adaptedBy(self):
        return self.__adaptedBy

    @adaptedBy.setter
    def adaptedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_template_GroundTemplate__adaptedBy", None)
        self.__adaptedBy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Service104"):
                opp_val = getattr(old_value, "Service104", None)
                if opp_val == self:
                    setattr(old_value, "Service104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Service104"):
                opp_val = getattr(value, "Service104", None)
                setattr(value, "Service104", self)

class ControlConstruct:

    pass
class service_template_AnyOrder(ControlConstruct):

    pass
class service_template_SplitJoin(ControlConstruct):

    pass
class service_template_Choice(ControlConstruct):

    pass
class service_template_Sequence(ControlConstruct):

    pass
class service_template_Perform(ControlConstruct):

    pass
class service_template_IfThenElse(ControlConstruct):

    pass
class service_template_Split(ControlConstruct):

    pass
class service_template_Iterate(ControlConstruct):

    pass
class service_template_TemplateFlow:

    pass
class TemplateConstraint:

    pass
class AbstractProcessModel:

    pass
class service_template_ControlConstruct(ABC):

    pass
class TemplateFlow:

    pass
class template_service_Antecedent:

    pass
class service_template_ServiceTemplate:

    def __init__(self, URI: str, service_template_ServiceTemplate: "TemplateFlow" = None, service_template_ServiceTemplate92: set["ServiceParameter"] = None, service_template_ServiceTemplate94: "AbstractProcessModel" = None, service_template_ServiceTemplate96: set["TemplateConstraint"] = None):
        self.URI = URI
        self.service_template_ServiceTemplate = service_template_ServiceTemplate
        self.service_template_ServiceTemplate92 = service_template_ServiceTemplate92 if service_template_ServiceTemplate92 is not None else set()
        self.service_template_ServiceTemplate94 = service_template_ServiceTemplate94
        self.service_template_ServiceTemplate96 = service_template_ServiceTemplate96 if service_template_ServiceTemplate96 is not None else set()
        
    @property
    def URI(self) -> str:
        return self.__URI

    @URI.setter
    def URI(self, URI: str):
        self.__URI = URI

    @property
    def service_template_ServiceTemplate96(self):
        return self.__service_template_ServiceTemplate96

    @service_template_ServiceTemplate96.setter
    def service_template_ServiceTemplate96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_template_ServiceTemplate__service_template_ServiceTemplate96", None)
        self.__service_template_ServiceTemplate96 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TemplateConstraint"):
                    opp_val = getattr(item, "TemplateConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "TemplateConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TemplateConstraint"):
                    opp_val = getattr(item, "TemplateConstraint", None)
                    
                    setattr(item, "TemplateConstraint", self)
                    

    @property
    def service_template_ServiceTemplate92(self):
        return self.__service_template_ServiceTemplate92

    @service_template_ServiceTemplate92.setter
    def service_template_ServiceTemplate92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_template_ServiceTemplate__service_template_ServiceTemplate92", None)
        self.__service_template_ServiceTemplate92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ServiceParameter"):
                    opp_val = getattr(item, "ServiceParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "ServiceParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ServiceParameter"):
                    opp_val = getattr(item, "ServiceParameter", None)
                    
                    setattr(item, "ServiceParameter", self)
                    

    @property
    def service_template_ServiceTemplate94(self):
        return self.__service_template_ServiceTemplate94

    @service_template_ServiceTemplate94.setter
    def service_template_ServiceTemplate94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_template_ServiceTemplate__service_template_ServiceTemplate94", None)
        self.__service_template_ServiceTemplate94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "AbstractProcessModel"):
                opp_val = getattr(old_value, "AbstractProcessModel", None)
                if opp_val == self:
                    setattr(old_value, "AbstractProcessModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "AbstractProcessModel"):
                opp_val = getattr(value, "AbstractProcessModel", None)
                setattr(value, "AbstractProcessModel", self)

    @property
    def service_template_ServiceTemplate(self):
        return self.__service_template_ServiceTemplate

    @service_template_ServiceTemplate.setter
    def service_template_ServiceTemplate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_template_ServiceTemplate__service_template_ServiceTemplate", None)
        self.__service_template_ServiceTemplate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TemplateFlow"):
                opp_val = getattr(old_value, "TemplateFlow", None)
                if opp_val == self:
                    setattr(old_value, "TemplateFlow", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TemplateFlow"):
                opp_val = getattr(value, "TemplateFlow", None)
                setattr(value, "TemplateFlow", self)

class service_template_TemplateConstraint:

    pass
class service_template_BoundProcessModel:

    pass
class service_template_BoundTemplateParameter:

    pass
class template_service_Service:

    pass
class semantics_service_Antecedent:

    pass
class service_semantics_ServiceCondition:

    pass
class ServiceParameter:

    pass
class service_semantics_ServiceOutput(ServiceParameter):

    pass
class service_semantics_ServiceInput(ServiceParameter):

    pass
class semantics_service_EObject:

    pass
class service_semantics_ServiceParameter(ABC):

    def __init__(self, name: str, service_semantics_ServiceParameter: "semantics_service_EObject" = None):
        self.name = name
        self.service_semantics_ServiceParameter = service_semantics_ServiceParameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def service_semantics_ServiceParameter(self):
        return self.__service_semantics_ServiceParameter

    @service_semantics_ServiceParameter.setter
    def service_semantics_ServiceParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_semantics_ServiceParameter__service_semantics_ServiceParameter", None)
        self.__service_semantics_ServiceParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "semantics_service_EObject"):
                opp_val = getattr(old_value, "semantics_service_EObject", None)
                if opp_val == self:
                    setattr(old_value, "semantics_service_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "semantics_service_EObject"):
                opp_val = getattr(value, "semantics_service_EObject", None)
                setattr(value, "semantics_service_EObject", self)

class service_semantics_ServiceCategory:

    def __init__(self, taxonomy: str, value: str, name: str, code: str):
        self.taxonomy = taxonomy
        self.value = value
        self.name = name
        self.code = code
        
    @property
    def taxonomy(self) -> str:
        return self.__taxonomy

    @taxonomy.setter
    def taxonomy(self, taxonomy: str):
        self.__taxonomy = taxonomy

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

class IOEP:

    pass
class service_template_AbstractProcessModel(IOEP):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class service_semantics_ProcessModel(IOEP):

    def __init__(self, name: str, describedBy: "semantics_service_Service" = None):
        self.name = name
        self.describedBy = describedBy
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def describedBy(self):
        return self.__describedBy

    @describedBy.setter
    def describedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_semantics_ProcessModel__describedBy", None)
        self.__describedBy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Service72"):
                opp_val = getattr(old_value, "Service72", None)
                if opp_val == self:
                    setattr(old_value, "Service72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Service72"):
                opp_val = getattr(value, "Service72", None)
                setattr(value, "Service72", self)

class service_semantics_IOEP(ABC):

    pass
class semantics_service_Consequent:

    pass
class service_semantics_ServiceResult:

    pass
class ServiceOutput:

    pass
class ServiceInput:

    pass
class ServiceCategory:

    pass
class semantics_service_Service:

    pass
class service_semantics_ServiceProfile:

    def __init__(self, serviceClassification: str, name: str, service_semantics_ServiceProfile59: set["ServiceOutput"] = None, service_semantics_ServiceProfile61: set["ServiceResult"] = None, service_semantics_ServiceProfile63: set["ServiceCondition"] = None, presents: "semantics_service_Service" = None, service_semantics_ServiceProfile: "ProcessModel" = None, service_semantics_ServiceProfile55: "ServiceCategory" = None, service_semantics_ServiceProfile57: set["ServiceInput"] = None):
        self.serviceClassification = serviceClassification
        self.name = name
        self.service_semantics_ServiceProfile59 = service_semantics_ServiceProfile59 if service_semantics_ServiceProfile59 is not None else set()
        self.service_semantics_ServiceProfile61 = service_semantics_ServiceProfile61 if service_semantics_ServiceProfile61 is not None else set()
        self.service_semantics_ServiceProfile63 = service_semantics_ServiceProfile63 if service_semantics_ServiceProfile63 is not None else set()
        self.presents = presents
        self.service_semantics_ServiceProfile = service_semantics_ServiceProfile
        self.service_semantics_ServiceProfile55 = service_semantics_ServiceProfile55
        self.service_semantics_ServiceProfile57 = service_semantics_ServiceProfile57 if service_semantics_ServiceProfile57 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def serviceClassification(self) -> str:
        return self.__serviceClassification

    @serviceClassification.setter
    def serviceClassification(self, serviceClassification: str):
        self.__serviceClassification = serviceClassification

    @property
    def presents(self):
        return self.__presents

    @presents.setter
    def presents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_semantics_ServiceProfile__presents", None)
        self.__presents = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Service"):
                opp_val = getattr(old_value, "Service", None)
                if opp_val == self:
                    setattr(old_value, "Service", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Service"):
                opp_val = getattr(value, "Service", None)
                setattr(value, "Service", self)

    @property
    def service_semantics_ServiceProfile61(self):
        return self.__service_semantics_ServiceProfile61

    @service_semantics_ServiceProfile61.setter
    def service_semantics_ServiceProfile61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_semantics_ServiceProfile__service_semantics_ServiceProfile61", None)
        self.__service_semantics_ServiceProfile61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ServiceResult"):
                    opp_val = getattr(item, "ServiceResult", None)
                    
                    if opp_val == self:
                        setattr(item, "ServiceResult", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ServiceResult"):
                    opp_val = getattr(item, "ServiceResult", None)
                    
                    setattr(item, "ServiceResult", self)
                    

    @property
    def service_semantics_ServiceProfile(self):
        return self.__service_semantics_ServiceProfile

    @service_semantics_ServiceProfile.setter
    def service_semantics_ServiceProfile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_semantics_ServiceProfile__service_semantics_ServiceProfile", None)
        self.__service_semantics_ServiceProfile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcessModel53"):
                opp_val = getattr(old_value, "ProcessModel53", None)
                if opp_val == self:
                    setattr(old_value, "ProcessModel53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessModel53"):
                opp_val = getattr(value, "ProcessModel53", None)
                setattr(value, "ProcessModel53", self)

    @property
    def service_semantics_ServiceProfile57(self):
        return self.__service_semantics_ServiceProfile57

    @service_semantics_ServiceProfile57.setter
    def service_semantics_ServiceProfile57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_semantics_ServiceProfile__service_semantics_ServiceProfile57", None)
        self.__service_semantics_ServiceProfile57 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ServiceInput"):
                    opp_val = getattr(item, "ServiceInput", None)
                    
                    if opp_val == self:
                        setattr(item, "ServiceInput", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ServiceInput"):
                    opp_val = getattr(item, "ServiceInput", None)
                    
                    setattr(item, "ServiceInput", self)
                    

    @property
    def service_semantics_ServiceProfile55(self):
        return self.__service_semantics_ServiceProfile55

    @service_semantics_ServiceProfile55.setter
    def service_semantics_ServiceProfile55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_semantics_ServiceProfile__service_semantics_ServiceProfile55", None)
        self.__service_semantics_ServiceProfile55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ServiceCategory"):
                opp_val = getattr(old_value, "ServiceCategory", None)
                if opp_val == self:
                    setattr(old_value, "ServiceCategory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ServiceCategory"):
                opp_val = getattr(value, "ServiceCategory", None)
                setattr(value, "ServiceCategory", self)

    @property
    def service_semantics_ServiceProfile59(self):
        return self.__service_semantics_ServiceProfile59

    @service_semantics_ServiceProfile59.setter
    def service_semantics_ServiceProfile59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_semantics_ServiceProfile__service_semantics_ServiceProfile59", None)
        self.__service_semantics_ServiceProfile59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ServiceOutput"):
                    opp_val = getattr(item, "ServiceOutput", None)
                    
                    if opp_val == self:
                        setattr(item, "ServiceOutput", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ServiceOutput"):
                    opp_val = getattr(item, "ServiceOutput", None)
                    
                    setattr(item, "ServiceOutput", self)
                    

    @property
    def service_semantics_ServiceProfile63(self):
        return self.__service_semantics_ServiceProfile63

    @service_semantics_ServiceProfile63.setter
    def service_semantics_ServiceProfile63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_semantics_ServiceProfile__service_semantics_ServiceProfile63", None)
        self.__service_semantics_ServiceProfile63 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ServiceCondition"):
                    opp_val = getattr(item, "ServiceCondition", None)
                    
                    if opp_val == self:
                        setattr(item, "ServiceCondition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ServiceCondition"):
                    opp_val = getattr(item, "ServiceCondition", None)
                    
                    setattr(item, "ServiceCondition", self)
                    

class service_semantics_ServiceGrounding:

    def __init__(self, name: str, bindParams: str, supports: "semantics_service_Service" = None, service_semantics_ServiceGrounding: "ProcessModel" = None, service_semantics_ServiceGrounding69: "InterfaceDescription" = None):
        self.name = name
        self.bindParams = bindParams
        self.supports = supports
        self.service_semantics_ServiceGrounding = service_semantics_ServiceGrounding
        self.service_semantics_ServiceGrounding69 = service_semantics_ServiceGrounding69
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bindParams(self) -> str:
        return self.__bindParams

    @bindParams.setter
    def bindParams(self, bindParams: str):
        self.__bindParams = bindParams

    @property
    def supports(self):
        return self.__supports

    @supports.setter
    def supports(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_semantics_ServiceGrounding__supports", None)
        self.__supports = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Service65"):
                opp_val = getattr(old_value, "Service65", None)
                if opp_val == self:
                    setattr(old_value, "Service65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Service65"):
                opp_val = getattr(value, "Service65", None)
                setattr(value, "Service65", self)

    @property
    def service_semantics_ServiceGrounding69(self):
        return self.__service_semantics_ServiceGrounding69

    @service_semantics_ServiceGrounding69.setter
    def service_semantics_ServiceGrounding69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_semantics_ServiceGrounding__service_semantics_ServiceGrounding69", None)
        self.__service_semantics_ServiceGrounding69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InterfaceDescription70"):
                opp_val = getattr(old_value, "InterfaceDescription70", None)
                if opp_val == self:
                    setattr(old_value, "InterfaceDescription70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InterfaceDescription70"):
                opp_val = getattr(value, "InterfaceDescription70", None)
                setattr(value, "InterfaceDescription70", self)

    @property
    def service_semantics_ServiceGrounding(self):
        return self.__service_semantics_ServiceGrounding

    @service_semantics_ServiceGrounding.setter
    def service_semantics_ServiceGrounding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_semantics_ServiceGrounding__service_semantics_ServiceGrounding", None)
        self.__service_semantics_ServiceGrounding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcessModel67"):
                opp_val = getattr(old_value, "ProcessModel67", None)
                if opp_val == self:
                    setattr(old_value, "ProcessModel67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessModel67"):
                opp_val = getattr(value, "ProcessModel67", None)
                setattr(value, "ProcessModel67", self)

class ServiceCondition:

    pass
class ServiceResult:

    pass
class service_syntax_Binding:

    def __init__(self, transport: str, style: str, name: str, InterfaceDescription49: "InterfaceDescription" = None):
        self.transport = transport
        self.style = style
        self.name = name
        self.InterfaceDescription49 = InterfaceDescription49
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def style(self) -> str:
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style

    @property
    def transport(self) -> str:
        return self.__transport

    @transport.setter
    def transport(self, transport: str):
        self.__transport = transport

    @property
    def InterfaceDescription49(self):
        return self.__InterfaceDescription49

    @InterfaceDescription49.setter
    def InterfaceDescription49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_syntax_Binding__InterfaceDescription49", None)
        self.__InterfaceDescription49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syntax50"):
                opp_val = getattr(old_value, "syntax50", None)
                if opp_val == self:
                    setattr(old_value, "syntax50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syntax50"):
                opp_val = getattr(value, "syntax50", None)
                setattr(value, "syntax50", self)

class DeployedService:

    pass
class syntax_service_ServiceImplemetation:

    pass
class service_syntax_Endpoint:

    def __init__(self, name: str, location: str, service_syntax_Endpoint: "Binding" = None, service_syntax_Endpoint45: "syntax_service_ServiceImplemetation" = None, service_syntax_Endpoint47: "DeployedService" = None):
        self.name = name
        self.location = location
        self.service_syntax_Endpoint = service_syntax_Endpoint
        self.service_syntax_Endpoint45 = service_syntax_Endpoint45
        self.service_syntax_Endpoint47 = service_syntax_Endpoint47
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def service_syntax_Endpoint47(self):
        return self.__service_syntax_Endpoint47

    @service_syntax_Endpoint47.setter
    def service_syntax_Endpoint47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_syntax_Endpoint__service_syntax_Endpoint47", None)
        self.__service_syntax_Endpoint47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DeployedService"):
                opp_val = getattr(old_value, "DeployedService", None)
                if opp_val == self:
                    setattr(old_value, "DeployedService", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DeployedService"):
                opp_val = getattr(value, "DeployedService", None)
                setattr(value, "DeployedService", self)

    @property
    def service_syntax_Endpoint(self):
        return self.__service_syntax_Endpoint

    @service_syntax_Endpoint.setter
    def service_syntax_Endpoint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_syntax_Endpoint__service_syntax_Endpoint", None)
        self.__service_syntax_Endpoint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Binding43"):
                opp_val = getattr(old_value, "Binding43", None)
                if opp_val == self:
                    setattr(old_value, "Binding43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Binding43"):
                opp_val = getattr(value, "Binding43", None)
                setattr(value, "Binding43", self)

    @property
    def service_syntax_Endpoint45(self):
        return self.__service_syntax_Endpoint45

    @service_syntax_Endpoint45.setter
    def service_syntax_Endpoint45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_syntax_Endpoint__service_syntax_Endpoint45", None)
        self.__service_syntax_Endpoint45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syntax_service_ServiceImplemetation"):
                opp_val = getattr(old_value, "syntax_service_ServiceImplemetation", None)
                if opp_val == self:
                    setattr(old_value, "syntax_service_ServiceImplemetation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syntax_service_ServiceImplemetation"):
                opp_val = getattr(value, "syntax_service_ServiceImplemetation", None)
                setattr(value, "syntax_service_ServiceImplemetation", self)

class syntax_service_TopLevelElement:

    pass
class Binding:

    pass
class OperationDescription:

    pass
class service_syntax_InterfaceDescription:

    def __init__(self, name: str, service_syntax_InterfaceDescription28: "syntax_service_SchemaType" = None, service_syntax_InterfaceDescription30: set["syntax_service_SchemaType"] = None, service_syntax_InterfaceDescription: set["OperationDescription"] = None, Binding: set["Binding"] = None):
        self.name = name
        self.service_syntax_InterfaceDescription28 = service_syntax_InterfaceDescription28
        self.service_syntax_InterfaceDescription30 = service_syntax_InterfaceDescription30 if service_syntax_InterfaceDescription30 is not None else set()
        self.service_syntax_InterfaceDescription = service_syntax_InterfaceDescription if service_syntax_InterfaceDescription is not None else set()
        self.Binding = Binding if Binding is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def service_syntax_InterfaceDescription30(self):
        return self.__service_syntax_InterfaceDescription30

    @service_syntax_InterfaceDescription30.setter
    def service_syntax_InterfaceDescription30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_syntax_InterfaceDescription__service_syntax_InterfaceDescription30", None)
        self.__service_syntax_InterfaceDescription30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syntax_service_SchemaType31"):
                    opp_val = getattr(item, "syntax_service_SchemaType31", None)
                    
                    if opp_val == self:
                        setattr(item, "syntax_service_SchemaType31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syntax_service_SchemaType31"):
                    opp_val = getattr(item, "syntax_service_SchemaType31", None)
                    
                    setattr(item, "syntax_service_SchemaType31", self)
                    

    @property
    def service_syntax_InterfaceDescription(self):
        return self.__service_syntax_InterfaceDescription

    @service_syntax_InterfaceDescription.setter
    def service_syntax_InterfaceDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_syntax_InterfaceDescription__service_syntax_InterfaceDescription", None)
        self.__service_syntax_InterfaceDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "OperationDescription"):
                    opp_val = getattr(item, "OperationDescription", None)
                    
                    if opp_val == self:
                        setattr(item, "OperationDescription", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "OperationDescription"):
                    opp_val = getattr(item, "OperationDescription", None)
                    
                    setattr(item, "OperationDescription", self)
                    

    @property
    def service_syntax_InterfaceDescription28(self):
        return self.__service_syntax_InterfaceDescription28

    @service_syntax_InterfaceDescription28.setter
    def service_syntax_InterfaceDescription28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_syntax_InterfaceDescription__service_syntax_InterfaceDescription28", None)
        self.__service_syntax_InterfaceDescription28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syntax_service_SchemaType"):
                opp_val = getattr(old_value, "syntax_service_SchemaType", None)
                if opp_val == self:
                    setattr(old_value, "syntax_service_SchemaType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syntax_service_SchemaType"):
                opp_val = getattr(value, "syntax_service_SchemaType", None)
                setattr(value, "syntax_service_SchemaType", self)

    @property
    def Binding(self):
        return self.__Binding

    @Binding.setter
    def Binding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_syntax_InterfaceDescription__Binding", None)
        self.__Binding = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syntax"):
                    opp_val = getattr(item, "syntax", None)
                    
                    if opp_val == self:
                        setattr(item, "syntax", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syntax"):
                    opp_val = getattr(item, "syntax", None)
                    
                    setattr(item, "syntax", self)
                    

class ServiceFramework:

    pass
class service_SL:

    pass
class syntax_service_TopLevelComplexType:

    pass
class service_syntax_Message:

    def __init__(self, name: str, service_syntax_Message: "syntax_service_TopLevelComplexType" = None, service_syntax_Message41: "syntax_service_TopLevelElement" = None):
        self.name = name
        self.service_syntax_Message = service_syntax_Message
        self.service_syntax_Message41 = service_syntax_Message41
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def service_syntax_Message41(self):
        return self.__service_syntax_Message41

    @service_syntax_Message41.setter
    def service_syntax_Message41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_syntax_Message__service_syntax_Message41", None)
        self.__service_syntax_Message41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syntax_service_TopLevelElement"):
                opp_val = getattr(old_value, "syntax_service_TopLevelElement", None)
                if opp_val == self:
                    setattr(old_value, "syntax_service_TopLevelElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syntax_service_TopLevelElement"):
                opp_val = getattr(value, "syntax_service_TopLevelElement", None)
                setattr(value, "syntax_service_TopLevelElement", self)

    @property
    def service_syntax_Message(self):
        return self.__service_syntax_Message

    @service_syntax_Message.setter
    def service_syntax_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_syntax_Message__service_syntax_Message", None)
        self.__service_syntax_Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "syntax_service_TopLevelComplexType"):
                opp_val = getattr(old_value, "syntax_service_TopLevelComplexType", None)
                if opp_val == self:
                    setattr(old_value, "syntax_service_TopLevelComplexType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "syntax_service_TopLevelComplexType"):
                opp_val = getattr(value, "syntax_service_TopLevelComplexType", None)
                setattr(value, "syntax_service_TopLevelComplexType", self)

class Message:

    pass
class service_syntax_OperationDescription:

    def __init__(self, name: str, service_syntax_OperationDescription: set["Message"] = None, service_syntax_OperationDescription34: set["Message"] = None, service_syntax_OperationDescription37: set["Message"] = None):
        self.name = name
        self.service_syntax_OperationDescription = service_syntax_OperationDescription if service_syntax_OperationDescription is not None else set()
        self.service_syntax_OperationDescription34 = service_syntax_OperationDescription34 if service_syntax_OperationDescription34 is not None else set()
        self.service_syntax_OperationDescription37 = service_syntax_OperationDescription37 if service_syntax_OperationDescription37 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def service_syntax_OperationDescription34(self):
        return self.__service_syntax_OperationDescription34

    @service_syntax_OperationDescription34.setter
    def service_syntax_OperationDescription34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_syntax_OperationDescription__service_syntax_OperationDescription34", None)
        self.__service_syntax_OperationDescription34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Message35"):
                    opp_val = getattr(item, "Message35", None)
                    
                    if opp_val == self:
                        setattr(item, "Message35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Message35"):
                    opp_val = getattr(item, "Message35", None)
                    
                    setattr(item, "Message35", self)
                    

    @property
    def service_syntax_OperationDescription37(self):
        return self.__service_syntax_OperationDescription37

    @service_syntax_OperationDescription37.setter
    def service_syntax_OperationDescription37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_syntax_OperationDescription__service_syntax_OperationDescription37", None)
        self.__service_syntax_OperationDescription37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Message38"):
                    opp_val = getattr(item, "Message38", None)
                    
                    if opp_val == self:
                        setattr(item, "Message38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Message38"):
                    opp_val = getattr(item, "Message38", None)
                    
                    setattr(item, "Message38", self)
                    

    @property
    def service_syntax_OperationDescription(self):
        return self.__service_syntax_OperationDescription

    @service_syntax_OperationDescription.setter
    def service_syntax_OperationDescription(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_syntax_OperationDescription__service_syntax_OperationDescription", None)
        self.__service_syntax_OperationDescription = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Message"):
                    opp_val = getattr(item, "Message", None)
                    
                    if opp_val == self:
                        setattr(item, "Message", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Message"):
                    opp_val = getattr(item, "Message", None)
                    
                    setattr(item, "Message", self)
                    

class syntax_service_SchemaType:

    pass
class GroundTemplate:

    pass
class ProcessModel:

    pass
class ServiceGrounding:

    pass
class ServiceProfile:

    pass
class InterfaceDescription:

    pass
class Endpoint:

    pass
class service_Service:

    def __init__(self, name: str, namespace: str, description: str, service_Service10: "service_ServiceProvider" = None, service_Service14: "service_ServiceConsumer" = None, service_Service: set["Endpoint"] = None, service_Service2: "InterfaceDescription" = None, ServiceProfile: "ServiceProfile" = None, ServiceGrounding: set["ServiceGrounding"] = None, ProcessModel: "ProcessModel" = None, GroundTemplate: "GroundTemplate" = None, service_Service16: "service_SL" = None):
        self.name = name
        self.namespace = namespace
        self.description = description
        self.service_Service10 = service_Service10
        self.service_Service14 = service_Service14
        self.service_Service = service_Service if service_Service is not None else set()
        self.service_Service2 = service_Service2
        self.ServiceProfile = ServiceProfile
        self.ServiceGrounding = ServiceGrounding if ServiceGrounding is not None else set()
        self.ProcessModel = ProcessModel
        self.GroundTemplate = GroundTemplate
        self.service_Service16 = service_Service16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def namespace(self) -> str:
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace

    @property
    def service_Service16(self):
        return self.__service_Service16

    @service_Service16.setter
    def service_Service16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Service__service_Service16", None)
        self.__service_Service16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service_SL"):
                opp_val = getattr(old_value, "service_SL", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service_SL"):
                opp_val = getattr(value, "service_SL", None)
                if opp_val is None:
                    setattr(value, "service_SL", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def service_Service2(self):
        return self.__service_Service2

    @service_Service2.setter
    def service_Service2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Service__service_Service2", None)
        self.__service_Service2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InterfaceDescription"):
                opp_val = getattr(old_value, "InterfaceDescription", None)
                if opp_val == self:
                    setattr(old_value, "InterfaceDescription", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InterfaceDescription"):
                opp_val = getattr(value, "InterfaceDescription", None)
                setattr(value, "InterfaceDescription", self)

    @property
    def GroundTemplate(self):
        return self.__GroundTemplate

    @GroundTemplate.setter
    def GroundTemplate(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Service__GroundTemplate", None)
        self.__GroundTemplate = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "template"):
                opp_val = getattr(old_value, "template", None)
                if opp_val == self:
                    setattr(old_value, "template", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "template"):
                opp_val = getattr(value, "template", None)
                setattr(value, "template", self)

    @property
    def service_Service10(self):
        return self.__service_Service10

    @service_Service10.setter
    def service_Service10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Service__service_Service10", None)
        self.__service_Service10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service_ServiceProvider"):
                opp_val = getattr(old_value, "service_ServiceProvider", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service_ServiceProvider"):
                opp_val = getattr(value, "service_ServiceProvider", None)
                if opp_val is None:
                    setattr(value, "service_ServiceProvider", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ServiceGrounding(self):
        return self.__ServiceGrounding

    @ServiceGrounding.setter
    def ServiceGrounding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Service__ServiceGrounding", None)
        self.__ServiceGrounding = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "semantics5"):
                    opp_val = getattr(item, "semantics5", None)
                    
                    if opp_val == self:
                        setattr(item, "semantics5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "semantics5"):
                    opp_val = getattr(item, "semantics5", None)
                    
                    setattr(item, "semantics5", self)
                    

    @property
    def ServiceProfile(self):
        return self.__ServiceProfile

    @ServiceProfile.setter
    def ServiceProfile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Service__ServiceProfile", None)
        self.__ServiceProfile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "semantics"):
                opp_val = getattr(old_value, "semantics", None)
                if opp_val == self:
                    setattr(old_value, "semantics", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "semantics"):
                opp_val = getattr(value, "semantics", None)
                setattr(value, "semantics", self)

    @property
    def service_Service14(self):
        return self.__service_Service14

    @service_Service14.setter
    def service_Service14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Service__service_Service14", None)
        self.__service_Service14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service_ServiceConsumer"):
                opp_val = getattr(old_value, "service_ServiceConsumer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service_ServiceConsumer"):
                opp_val = getattr(value, "service_ServiceConsumer", None)
                if opp_val is None:
                    setattr(value, "service_ServiceConsumer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ProcessModel(self):
        return self.__ProcessModel

    @ProcessModel.setter
    def ProcessModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Service__ProcessModel", None)
        self.__ProcessModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "semantics7"):
                opp_val = getattr(old_value, "semantics7", None)
                if opp_val == self:
                    setattr(old_value, "semantics7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "semantics7"):
                opp_val = getattr(value, "semantics7", None)
                setattr(value, "semantics7", self)

    @property
    def service_Service(self):
        return self.__service_Service

    @service_Service.setter
    def service_Service(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Service__service_Service", None)
        self.__service_Service = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Endpoint"):
                    opp_val = getattr(item, "Endpoint", None)
                    
                    if opp_val == self:
                        setattr(item, "Endpoint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Endpoint"):
                    opp_val = getattr(item, "Endpoint", None)
                    
                    setattr(item, "Endpoint", self)
                    

class service_ServiceImplemetation:

    def __init__(self, language: str, uri: str, service_ServiceImplemetation: "service_ServiceProvider" = None):
        self.language = language
        self.uri = uri
        self.service_ServiceImplemetation = service_ServiceImplemetation
        
    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def service_ServiceImplemetation(self):
        return self.__service_ServiceImplemetation

    @service_ServiceImplemetation.setter
    def service_ServiceImplemetation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_ServiceImplemetation__service_ServiceImplemetation", None)
        self.__service_ServiceImplemetation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service_ServiceProvider12"):
                opp_val = getattr(old_value, "service_ServiceProvider12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service_ServiceProvider12"):
                opp_val = getattr(value, "service_ServiceProvider12", None)
                if opp_val is None:
                    setattr(value, "service_ServiceProvider12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Agent:

    pass
class service_ServiceConsumer(Agent):

    def __init__(self, isType: str, service_ServiceConsumer: set["service_Service"] = None, service_ServiceConsumer22: "service_SL" = None):
        self.isType = isType
        self.service_ServiceConsumer = service_ServiceConsumer if service_ServiceConsumer is not None else set()
        self.service_ServiceConsumer22 = service_ServiceConsumer22
        
    @property
    def isType(self) -> str:
        return self.__isType

    @isType.setter
    def isType(self, isType: str):
        self.__isType = isType

    @property
    def service_ServiceConsumer22(self):
        return self.__service_ServiceConsumer22

    @service_ServiceConsumer22.setter
    def service_ServiceConsumer22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_ServiceConsumer__service_ServiceConsumer22", None)
        self.__service_ServiceConsumer22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service_SL21"):
                opp_val = getattr(old_value, "service_SL21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service_SL21"):
                opp_val = getattr(value, "service_SL21", None)
                if opp_val is None:
                    setattr(value, "service_SL21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def service_ServiceConsumer(self):
        return self.__service_ServiceConsumer

    @service_ServiceConsumer.setter
    def service_ServiceConsumer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_ServiceConsumer__service_ServiceConsumer", None)
        self.__service_ServiceConsumer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "service_Service14"):
                    opp_val = getattr(item, "service_Service14", None)
                    
                    if opp_val == self:
                        setattr(item, "service_Service14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "service_Service14"):
                    opp_val = getattr(item, "service_Service14", None)
                    
                    setattr(item, "service_Service14", self)
                    

class service_ServiceProvider(Agent):

    def __init__(self, isType: str, service_ServiceProvider: set["service_Service"] = None, service_ServiceProvider12: set["service_ServiceImplemetation"] = None, service_ServiceProvider19: "service_SL" = None):
        self.isType = isType
        self.service_ServiceProvider = service_ServiceProvider if service_ServiceProvider is not None else set()
        self.service_ServiceProvider12 = service_ServiceProvider12 if service_ServiceProvider12 is not None else set()
        self.service_ServiceProvider19 = service_ServiceProvider19
        
    @property
    def isType(self) -> str:
        return self.__isType

    @isType.setter
    def isType(self, isType: str):
        self.__isType = isType

    @property
    def service_ServiceProvider(self):
        return self.__service_ServiceProvider

    @service_ServiceProvider.setter
    def service_ServiceProvider(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_ServiceProvider__service_ServiceProvider", None)
        self.__service_ServiceProvider = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "service_Service10"):
                    opp_val = getattr(item, "service_Service10", None)
                    
                    if opp_val == self:
                        setattr(item, "service_Service10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "service_Service10"):
                    opp_val = getattr(item, "service_Service10", None)
                    
                    setattr(item, "service_Service10", self)
                    

    @property
    def service_ServiceProvider19(self):
        return self.__service_ServiceProvider19

    @service_ServiceProvider19.setter
    def service_ServiceProvider19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_ServiceProvider__service_ServiceProvider19", None)
        self.__service_ServiceProvider19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service_SL18"):
                opp_val = getattr(old_value, "service_SL18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service_SL18"):
                opp_val = getattr(value, "service_SL18", None)
                if opp_val is None:
                    setattr(value, "service_SL18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def service_ServiceProvider12(self):
        return self.__service_ServiceProvider12

    @service_ServiceProvider12.setter
    def service_ServiceProvider12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_ServiceProvider__service_ServiceProvider12", None)
        self.__service_ServiceProvider12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "service_ServiceImplemetation"):
                    opp_val = getattr(item, "service_ServiceImplemetation", None)
                    
                    if opp_val == self:
                        setattr(item, "service_ServiceImplemetation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "service_ServiceImplemetation"):
                    opp_val = getattr(item, "service_ServiceImplemetation", None)
                    
                    setattr(item, "service_ServiceImplemetation", self)
                    
