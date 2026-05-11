from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class TransportProtocol(Enum):
    SOAP = "SOAP"
    HTTP = "HTTP"
    MIME = "MIME"
class ServiceType(Enum):
    internal = "internal"
    external = "external"
class StyleEncoding(Enum):
    Document_Literal = "Document_Literal"
    RPC_Encoded = "RPC_Encoded"
class ContainerType(Enum):
    axis = "axis"
class ServiceImpLanguage(Enum):
    Java_EJB = "Java_EJB"
    Java_JSP = "Java_JSP"


############################################
# Definition of Classes
############################################

class service_architecture_DeployedService:

    def __init__(self, artifact: str, deployedService: "ExecutionFramework" = None):
        self.artifact = artifact
        self.deployedService = deployedService
        
        pass
    @property
    def artifact(self):
        return self.__artifact

    @artifact.setter
    def artifact(self, artifact: str):
        self.__artifact = artifact


    @property
    def deployedService(self):
        return self.__deployedService

    @deployedService.setter
    def deployedService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_architecture_DeployedService__deployedService", None)
        self.__deployedService = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ExecutionFramework188"):
                opp_val = getattr(old_value, "ExecutionFramework188", None)
                if opp_val == self:
                    setattr(old_value, "ExecutionFramework188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ExecutionFramework188"):
                opp_val = getattr(value, "ExecutionFramework188", None)
                setattr(value, "ExecutionFramework188", self)

class service_architecture_ExecutionFramework:

    def __init__(self, container: str, deploy: set["DeployedService"] = None):
        self.container = container
        self.deploy = deploy if deploy is not None else set()
        
        pass
    @property
    def container(self):
        return self.__container

    @container.setter
    def container(self, container: str):
        self.__container = container


    @property
    def deploy(self):
        return self.__deploy

    @deploy.setter
    def deploy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_architecture_ExecutionFramework__deploy", None)
        self.__deploy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "DeployedService186"):
                    opp_val = getattr(item, "DeployedService186", None)
                    
                    if opp_val == self:
                        setattr(item, "DeployedService186", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "DeployedService186"):
                    opp_val = getattr(item, "DeployedService186", None)
                    
                    setattr(item, "DeployedService186", self)
                    

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
class service_template_ControlConstructList:

    pass
class ControlConstructList:

    pass
class Iterate:

    pass
class service_template_RepeatWhile(Iterate):

    pass
class service_template_RepeatUntil(Iterate):

    pass
class ServiceTemplate:

    pass
class service_template_GroundTemplate:

    def __init__(self, name: str, service_template_GroundTemplate: "ServiceTemplate" = None, service_template_GroundTemplate97: set["BoundTemplateParameter"] = None, service_template_GroundTemplate99: set["BoundProcessModel"] = None, adaptedBy: "template_service_Service" = None):
        self.name = name
        self.service_template_GroundTemplate = service_template_GroundTemplate
        self.service_template_GroundTemplate97 = service_template_GroundTemplate97 if service_template_GroundTemplate97 is not None else set()
        self.service_template_GroundTemplate99 = service_template_GroundTemplate99 if service_template_GroundTemplate99 is not None else set()
        self.adaptedBy = adaptedBy
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
            if hasattr(old_value, "Service101"):
                opp_val = getattr(old_value, "Service101", None)
                if opp_val == self:
                    setattr(old_value, "Service101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Service101"):
                opp_val = getattr(value, "Service101", None)
                setattr(value, "Service101", self)

    @property
    def service_template_GroundTemplate97(self):
        return self.__service_template_GroundTemplate97

    @service_template_GroundTemplate97.setter
    def service_template_GroundTemplate97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_template_GroundTemplate__service_template_GroundTemplate97", None)
        self.__service_template_GroundTemplate97 = value if value is not None else set()
        
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
    def service_template_GroundTemplate99(self):
        return self.__service_template_GroundTemplate99

    @service_template_GroundTemplate99.setter
    def service_template_GroundTemplate99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_template_GroundTemplate__service_template_GroundTemplate99", None)
        self.__service_template_GroundTemplate99 = value if value is not None else set()
        
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

class ControlConstructBag:

    pass
class IntervalThing:

    pass
class service_template_ControlConstruct(ABC):

    pass
class template_service_Antecedent:

    pass
class service_template_TemplateConstraint:

    pass
class service_template_BoundProcessModel:

    pass
class service_template_BoundTemplateParameter:

    pass
class template_service_Service:

    pass
class BoundProcessModel:

    pass
class BoundTemplateParameter:

    pass
class semantics_service_EObject:

    pass
class service_semantics_ServiceParameter(ABC):

    def __init__(self, name: str, service_semantics_ServiceParameter: "semantics_service_EObject" = None):
        self.name = name
        self.service_semantics_ServiceParameter = service_semantics_ServiceParameter
        
        pass
    @property
    def name(self):
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

class ControlConstruct:

    pass
class service_template_IfThenElse(ControlConstruct):

    pass
class service_template_Split(ControlConstruct):

    pass
class service_template_Iterate(ControlConstruct):

    pass
class service_template_SplitJoin(ControlConstruct):

    pass
class service_template_Perform(ControlConstruct):

    pass
class service_template_AnyOrder(ControlConstruct):

    pass
class service_template_Sequence(ControlConstruct):

    pass
class service_template_Choice(ControlConstruct):

    pass
class service_template_TemplateFlow:

    pass
class service_semantics_ServiceCategory:

    def __init__(self, taxonomy: str, value: str, name: str, code: str):
        self.taxonomy = taxonomy
        self.value = value
        self.name = name
        self.code = code
        
        pass
    @property
    def taxonomy(self):
        return self.__taxonomy

    @taxonomy.setter
    def taxonomy(self, taxonomy: str):
        self.__taxonomy = taxonomy


    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


class TemplateConstraint:

    pass
class AbstractProcessModel:

    pass
class IOEP:

    pass
class service_template_AbstractProcessModel(IOEP):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class service_semantics_ProcessModel(IOEP):

    def __init__(self, name: str, describedBy: "semantics_service_Service" = None):
        self.name = name
        self.describedBy = describedBy
        
        pass
    @property
    def name(self):
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
            if hasattr(old_value, "Service69"):
                opp_val = getattr(old_value, "Service69", None)
                if opp_val == self:
                    setattr(old_value, "Service69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Service69"):
                opp_val = getattr(value, "Service69", None)
                setattr(value, "Service69", self)

class TemplateFlow:

    pass
class service_template_ServiceTemplate:

    def __init__(self, URI: str, service_template_ServiceTemplate: "TemplateFlow" = None, service_template_ServiceTemplate89: set["ServiceParameter"] = None, service_template_ServiceTemplate91: "AbstractProcessModel" = None, service_template_ServiceTemplate93: set["TemplateConstraint"] = None):
        self.URI = URI
        self.service_template_ServiceTemplate = service_template_ServiceTemplate
        self.service_template_ServiceTemplate89 = service_template_ServiceTemplate89 if service_template_ServiceTemplate89 is not None else set()
        self.service_template_ServiceTemplate91 = service_template_ServiceTemplate91
        self.service_template_ServiceTemplate93 = service_template_ServiceTemplate93 if service_template_ServiceTemplate93 is not None else set()
        
        pass
    @property
    def URI(self):
        return self.__URI

    @URI.setter
    def URI(self, URI: str):
        self.__URI = URI


    @property
    def service_template_ServiceTemplate89(self):
        return self.__service_template_ServiceTemplate89

    @service_template_ServiceTemplate89.setter
    def service_template_ServiceTemplate89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_template_ServiceTemplate__service_template_ServiceTemplate89", None)
        self.__service_template_ServiceTemplate89 = value if value is not None else set()
        
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

    @property
    def service_template_ServiceTemplate91(self):
        return self.__service_template_ServiceTemplate91

    @service_template_ServiceTemplate91.setter
    def service_template_ServiceTemplate91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_template_ServiceTemplate__service_template_ServiceTemplate91", None)
        self.__service_template_ServiceTemplate91 = value
        
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
    def service_template_ServiceTemplate93(self):
        return self.__service_template_ServiceTemplate93

    @service_template_ServiceTemplate93.setter
    def service_template_ServiceTemplate93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_template_ServiceTemplate__service_template_ServiceTemplate93", None)
        self.__service_template_ServiceTemplate93 = value if value is not None else set()
        
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
                    

class service_semantics_ServiceGrounding:

    def __init__(self, name: str, bindParams: str, supports: "semantics_service_Service" = None, service_semantics_ServiceGrounding: "ProcessModel" = None, service_semantics_ServiceGrounding66: "InterfaceDescription" = None):
        self.name = name
        self.bindParams = bindParams
        self.supports = supports
        self.service_semantics_ServiceGrounding = service_semantics_ServiceGrounding
        self.service_semantics_ServiceGrounding66 = service_semantics_ServiceGrounding66
        
        pass
    @property
    def bindParams(self):
        return self.__bindParams

    @bindParams.setter
    def bindParams(self, bindParams: str):
        self.__bindParams = bindParams


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
            if hasattr(old_value, "ProcessModel64"):
                opp_val = getattr(old_value, "ProcessModel64", None)
                if opp_val == self:
                    setattr(old_value, "ProcessModel64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessModel64"):
                opp_val = getattr(value, "ProcessModel64", None)
                setattr(value, "ProcessModel64", self)

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
            if hasattr(old_value, "Service62"):
                opp_val = getattr(old_value, "Service62", None)
                if opp_val == self:
                    setattr(old_value, "Service62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Service62"):
                opp_val = getattr(value, "Service62", None)
                setattr(value, "Service62", self)

    @property
    def service_semantics_ServiceGrounding66(self):
        return self.__service_semantics_ServiceGrounding66

    @service_semantics_ServiceGrounding66.setter
    def service_semantics_ServiceGrounding66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_semantics_ServiceGrounding__service_semantics_ServiceGrounding66", None)
        self.__service_semantics_ServiceGrounding66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InterfaceDescription67"):
                opp_val = getattr(old_value, "InterfaceDescription67", None)
                if opp_val == self:
                    setattr(old_value, "InterfaceDescription67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InterfaceDescription67"):
                opp_val = getattr(value, "InterfaceDescription67", None)
                setattr(value, "InterfaceDescription67", self)

class service_semantics_IOEP(ABC):

    pass
class semantics_service_Consequent:

    pass
class service_semantics_ServiceResult:

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
class service_syntax_Binding:

    def __init__(self, name: str, transport: str, style: str, binding: "InterfaceDescription" = None):
        self.name = name
        self.transport = transport
        self.style = style
        self.binding = binding
        
        pass
    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, style: str):
        self.__style = style


    @property
    def transport(self):
        return self.__transport

    @transport.setter
    def transport(self, transport: str):
        self.__transport = transport


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def binding(self):
        return self.__binding

    @binding.setter
    def binding(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_syntax_Binding__binding", None)
        self.__binding = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "InterfaceDescription47"):
                opp_val = getattr(old_value, "InterfaceDescription47", None)
                if opp_val == self:
                    setattr(old_value, "InterfaceDescription47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "InterfaceDescription47"):
                opp_val = getattr(value, "InterfaceDescription47", None)
                setattr(value, "InterfaceDescription47", self)

class DeployedService:

    pass
class syntax_service_ServiceImplemetation:

    pass
class service_syntax_Endpoint:

    def __init__(self, name: str, location: str, service_syntax_Endpoint: "Binding" = None, service_syntax_Endpoint43: "syntax_service_ServiceImplemetation" = None, service_syntax_Endpoint45: "DeployedService" = None):
        self.name = name
        self.location = location
        self.service_syntax_Endpoint = service_syntax_Endpoint
        self.service_syntax_Endpoint43 = service_syntax_Endpoint43
        self.service_syntax_Endpoint45 = service_syntax_Endpoint45
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
            if hasattr(old_value, "Binding41"):
                opp_val = getattr(old_value, "Binding41", None)
                if opp_val == self:
                    setattr(old_value, "Binding41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Binding41"):
                opp_val = getattr(value, "Binding41", None)
                setattr(value, "Binding41", self)

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
    def service_syntax_Endpoint43(self):
        return self.__service_syntax_Endpoint43

    @service_syntax_Endpoint43.setter
    def service_syntax_Endpoint43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_syntax_Endpoint__service_syntax_Endpoint43", None)
        self.__service_syntax_Endpoint43 = value
        
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

class ServiceCondition:

    pass
class ServiceResult:

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

    def __init__(self, name: str, serviceClassification: str, presents: "semantics_service_Service" = None, service_semantics_ServiceProfile: "ProcessModel" = None, service_semantics_ServiceProfile52: "ServiceCategory" = None, service_semantics_ServiceProfile54: set["ServiceInput"] = None, service_semantics_ServiceProfile56: set["ServiceOutput"] = None, service_semantics_ServiceProfile58: set["ServiceResult"] = None, service_semantics_ServiceProfile60: set["ServiceCondition"] = None):
        self.name = name
        self.serviceClassification = serviceClassification
        self.presents = presents
        self.service_semantics_ServiceProfile = service_semantics_ServiceProfile
        self.service_semantics_ServiceProfile52 = service_semantics_ServiceProfile52
        self.service_semantics_ServiceProfile54 = service_semantics_ServiceProfile54 if service_semantics_ServiceProfile54 is not None else set()
        self.service_semantics_ServiceProfile56 = service_semantics_ServiceProfile56 if service_semantics_ServiceProfile56 is not None else set()
        self.service_semantics_ServiceProfile58 = service_semantics_ServiceProfile58 if service_semantics_ServiceProfile58 is not None else set()
        self.service_semantics_ServiceProfile60 = service_semantics_ServiceProfile60 if service_semantics_ServiceProfile60 is not None else set()
        
        pass
    @property
    def serviceClassification(self):
        return self.__serviceClassification

    @serviceClassification.setter
    def serviceClassification(self, serviceClassification: str):
        self.__serviceClassification = serviceClassification


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
    def service_semantics_ServiceProfile54(self):
        return self.__service_semantics_ServiceProfile54

    @service_semantics_ServiceProfile54.setter
    def service_semantics_ServiceProfile54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_semantics_ServiceProfile__service_semantics_ServiceProfile54", None)
        self.__service_semantics_ServiceProfile54 = value if value is not None else set()
        
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
    def service_semantics_ServiceProfile56(self):
        return self.__service_semantics_ServiceProfile56

    @service_semantics_ServiceProfile56.setter
    def service_semantics_ServiceProfile56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_semantics_ServiceProfile__service_semantics_ServiceProfile56", None)
        self.__service_semantics_ServiceProfile56 = value if value is not None else set()
        
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
    def service_semantics_ServiceProfile58(self):
        return self.__service_semantics_ServiceProfile58

    @service_semantics_ServiceProfile58.setter
    def service_semantics_ServiceProfile58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_semantics_ServiceProfile__service_semantics_ServiceProfile58", None)
        self.__service_semantics_ServiceProfile58 = value if value is not None else set()
        
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
    def service_semantics_ServiceProfile60(self):
        return self.__service_semantics_ServiceProfile60

    @service_semantics_ServiceProfile60.setter
    def service_semantics_ServiceProfile60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_semantics_ServiceProfile__service_semantics_ServiceProfile60", None)
        self.__service_semantics_ServiceProfile60 = value if value is not None else set()
        
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
                    

    @property
    def service_semantics_ServiceProfile52(self):
        return self.__service_semantics_ServiceProfile52

    @service_semantics_ServiceProfile52.setter
    def service_semantics_ServiceProfile52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_semantics_ServiceProfile__service_semantics_ServiceProfile52", None)
        self.__service_semantics_ServiceProfile52 = value
        
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
    def service_semantics_ServiceProfile(self):
        return self.__service_semantics_ServiceProfile

    @service_semantics_ServiceProfile.setter
    def service_semantics_ServiceProfile(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_semantics_ServiceProfile__service_semantics_ServiceProfile", None)
        self.__service_semantics_ServiceProfile = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcessModel50"):
                opp_val = getattr(old_value, "ProcessModel50", None)
                if opp_val == self:
                    setattr(old_value, "ProcessModel50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessModel50"):
                opp_val = getattr(value, "ProcessModel50", None)
                setattr(value, "ProcessModel50", self)

class Binding:

    pass
class OperationDescription:

    pass
class service_syntax_InterfaceDescription:

    def __init__(self, name: str, service_syntax_InterfaceDescription: set["OperationDescription"] = None, type: set["Binding"] = None, service_syntax_InterfaceDescription26: "syntax_service_SchemaType" = None, service_syntax_InterfaceDescription28: set["syntax_service_SchemaType"] = None):
        self.name = name
        self.service_syntax_InterfaceDescription = service_syntax_InterfaceDescription if service_syntax_InterfaceDescription is not None else set()
        self.type = type if type is not None else set()
        self.service_syntax_InterfaceDescription26 = service_syntax_InterfaceDescription26
        self.service_syntax_InterfaceDescription28 = service_syntax_InterfaceDescription28 if service_syntax_InterfaceDescription28 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def service_syntax_InterfaceDescription26(self):
        return self.__service_syntax_InterfaceDescription26

    @service_syntax_InterfaceDescription26.setter
    def service_syntax_InterfaceDescription26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_syntax_InterfaceDescription__service_syntax_InterfaceDescription26", None)
        self.__service_syntax_InterfaceDescription26 = value
        
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
    def service_syntax_InterfaceDescription28(self):
        return self.__service_syntax_InterfaceDescription28

    @service_syntax_InterfaceDescription28.setter
    def service_syntax_InterfaceDescription28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_syntax_InterfaceDescription__service_syntax_InterfaceDescription28", None)
        self.__service_syntax_InterfaceDescription28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "syntax_service_SchemaType29"):
                    opp_val = getattr(item, "syntax_service_SchemaType29", None)
                    
                    if opp_val == self:
                        setattr(item, "syntax_service_SchemaType29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "syntax_service_SchemaType29"):
                    opp_val = getattr(item, "syntax_service_SchemaType29", None)
                    
                    setattr(item, "syntax_service_SchemaType29", self)
                    

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_syntax_InterfaceDescription__type", None)
        self.__type = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Binding"):
                    opp_val = getattr(item, "Binding", None)
                    
                    if opp_val == self:
                        setattr(item, "Binding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Binding"):
                    opp_val = getattr(item, "Binding", None)
                    
                    setattr(item, "Binding", self)
                    

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
                    

class ServiceFramework:

    pass
class syntax_service_TopLevelElement:

    pass
class syntax_service_TopLevelComplexType:

    pass
class service_syntax_Message:

    def __init__(self, name: str, service_syntax_Message: "syntax_service_TopLevelComplexType" = None, service_syntax_Message39: "syntax_service_TopLevelElement" = None):
        self.name = name
        self.service_syntax_Message = service_syntax_Message
        self.service_syntax_Message39 = service_syntax_Message39
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def service_syntax_Message39(self):
        return self.__service_syntax_Message39

    @service_syntax_Message39.setter
    def service_syntax_Message39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_syntax_Message__service_syntax_Message39", None)
        self.__service_syntax_Message39 = value
        
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

    def __init__(self, name: str, service_syntax_OperationDescription: set["Message"] = None, service_syntax_OperationDescription32: set["Message"] = None, service_syntax_OperationDescription35: set["Message"] = None):
        self.name = name
        self.service_syntax_OperationDescription = service_syntax_OperationDescription if service_syntax_OperationDescription is not None else set()
        self.service_syntax_OperationDescription32 = service_syntax_OperationDescription32 if service_syntax_OperationDescription32 is not None else set()
        self.service_syntax_OperationDescription35 = service_syntax_OperationDescription35 if service_syntax_OperationDescription35 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def service_syntax_OperationDescription35(self):
        return self.__service_syntax_OperationDescription35

    @service_syntax_OperationDescription35.setter
    def service_syntax_OperationDescription35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_syntax_OperationDescription__service_syntax_OperationDescription35", None)
        self.__service_syntax_OperationDescription35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Message36"):
                    opp_val = getattr(item, "Message36", None)
                    
                    if opp_val == self:
                        setattr(item, "Message36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Message36"):
                    opp_val = getattr(item, "Message36", None)
                    
                    setattr(item, "Message36", self)
                    

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
                    

    @property
    def service_syntax_OperationDescription32(self):
        return self.__service_syntax_OperationDescription32

    @service_syntax_OperationDescription32.setter
    def service_syntax_OperationDescription32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_syntax_OperationDescription__service_syntax_OperationDescription32", None)
        self.__service_syntax_OperationDescription32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Message33"):
                    opp_val = getattr(item, "Message33", None)
                    
                    if opp_val == self:
                        setattr(item, "Message33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Message33"):
                    opp_val = getattr(item, "Message33", None)
                    
                    setattr(item, "Message33", self)
                    

class syntax_service_SchemaType:

    pass
class Agent:

    pass
class service_ServiceProvider(Agent):

    def __init__(self, isType: str, service_ServiceProvider: set["service_Service"] = None, service_ServiceProvider10: set["service_ServiceImplemetation"] = None, service_ServiceProvider17: "service_SL" = None):
        self.isType = isType
        self.service_ServiceProvider = service_ServiceProvider if service_ServiceProvider is not None else set()
        self.service_ServiceProvider10 = service_ServiceProvider10 if service_ServiceProvider10 is not None else set()
        self.service_ServiceProvider17 = service_ServiceProvider17
        
        pass
    @property
    def isType(self):
        return self.__isType

    @isType.setter
    def isType(self, isType: str):
        self.__isType = isType


    @property
    def service_ServiceProvider10(self):
        return self.__service_ServiceProvider10

    @service_ServiceProvider10.setter
    def service_ServiceProvider10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_ServiceProvider__service_ServiceProvider10", None)
        self.__service_ServiceProvider10 = value if value is not None else set()
        
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
                if hasattr(item, "service_Service8"):
                    opp_val = getattr(item, "service_Service8", None)
                    
                    if opp_val == self:
                        setattr(item, "service_Service8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "service_Service8"):
                    opp_val = getattr(item, "service_Service8", None)
                    
                    setattr(item, "service_Service8", self)
                    

    @property
    def service_ServiceProvider17(self):
        return self.__service_ServiceProvider17

    @service_ServiceProvider17.setter
    def service_ServiceProvider17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_ServiceProvider__service_ServiceProvider17", None)
        self.__service_ServiceProvider17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service_SL16"):
                opp_val = getattr(old_value, "service_SL16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service_SL16"):
                opp_val = getattr(value, "service_SL16", None)
                if opp_val is None:
                    setattr(value, "service_SL16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
class service_SL:

    pass
class service_ServiceConsumer(Agent):

    def __init__(self, isType: str, service_ServiceConsumer: set["service_Service"] = None, service_ServiceConsumer20: "service_SL" = None):
        self.isType = isType
        self.service_ServiceConsumer = service_ServiceConsumer if service_ServiceConsumer is not None else set()
        self.service_ServiceConsumer20 = service_ServiceConsumer20
        
        pass
    @property
    def isType(self):
        return self.__isType

    @isType.setter
    def isType(self, isType: str):
        self.__isType = isType


    @property
    def service_ServiceConsumer20(self):
        return self.__service_ServiceConsumer20

    @service_ServiceConsumer20.setter
    def service_ServiceConsumer20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_ServiceConsumer__service_ServiceConsumer20", None)
        self.__service_ServiceConsumer20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service_SL19"):
                opp_val = getattr(old_value, "service_SL19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service_SL19"):
                opp_val = getattr(value, "service_SL19", None)
                if opp_val is None:
                    setattr(value, "service_SL19", set([self]))
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
                if hasattr(item, "service_Service12"):
                    opp_val = getattr(item, "service_Service12", None)
                    
                    if opp_val == self:
                        setattr(item, "service_Service12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "service_Service12"):
                    opp_val = getattr(item, "service_Service12", None)
                    
                    setattr(item, "service_Service12", self)
                    

class service_ServiceImplemetation:

    def __init__(self, language: str, uri: str, service_ServiceImplemetation: "service_ServiceProvider" = None):
        self.language = language
        self.uri = uri
        self.service_ServiceImplemetation = service_ServiceImplemetation
        
        pass
    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language


    @property
    def uri(self):
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
            if hasattr(old_value, "service_ServiceProvider10"):
                opp_val = getattr(old_value, "service_ServiceProvider10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service_ServiceProvider10"):
                opp_val = getattr(value, "service_ServiceProvider10", None)
                if opp_val is None:
                    setattr(value, "service_ServiceProvider10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Endpoint:

    pass
class service_Service:

    def __init__(self, name: str, namespace: str, description: str, service_Service: set["Endpoint"] = None, service_Service8: "service_ServiceProvider" = None, service_Service12: "service_ServiceConsumer" = None, service_Service14: "service_SL" = None, service_Service2: "InterfaceDescription" = None, presentedBy: "ServiceProfile" = None, supportedBy: set["ServiceGrounding"] = None, describes: "ProcessModel" = None, expose: "GroundTemplate" = None):
        self.name = name
        self.namespace = namespace
        self.description = description
        self.service_Service = service_Service if service_Service is not None else set()
        self.service_Service8 = service_Service8
        self.service_Service12 = service_Service12
        self.service_Service14 = service_Service14
        self.service_Service2 = service_Service2
        self.presentedBy = presentedBy
        self.supportedBy = supportedBy if supportedBy is not None else set()
        self.describes = describes
        self.expose = expose
        
        pass
    @property
    def namespace(self):
        return self.__namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self.__namespace = namespace


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def expose(self):
        return self.__expose

    @expose.setter
    def expose(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Service__expose", None)
        self.__expose = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "GroundTemplate"):
                opp_val = getattr(old_value, "GroundTemplate", None)
                if opp_val == self:
                    setattr(old_value, "GroundTemplate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "GroundTemplate"):
                opp_val = getattr(value, "GroundTemplate", None)
                setattr(value, "GroundTemplate", self)

    @property
    def describes(self):
        return self.__describes

    @describes.setter
    def describes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Service__describes", None)
        self.__describes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProcessModel"):
                opp_val = getattr(old_value, "ProcessModel", None)
                if opp_val == self:
                    setattr(old_value, "ProcessModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProcessModel"):
                opp_val = getattr(value, "ProcessModel", None)
                setattr(value, "ProcessModel", self)

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
    def supportedBy(self):
        return self.__supportedBy

    @supportedBy.setter
    def supportedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Service__supportedBy", None)
        self.__supportedBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ServiceGrounding"):
                    opp_val = getattr(item, "ServiceGrounding", None)
                    
                    if opp_val == self:
                        setattr(item, "ServiceGrounding", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ServiceGrounding"):
                    opp_val = getattr(item, "ServiceGrounding", None)
                    
                    setattr(item, "ServiceGrounding", self)
                    

    @property
    def service_Service12(self):
        return self.__service_Service12

    @service_Service12.setter
    def service_Service12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Service__service_Service12", None)
        self.__service_Service12 = value
        
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
    def service_Service8(self):
        return self.__service_Service8

    @service_Service8.setter
    def service_Service8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Service__service_Service8", None)
        self.__service_Service8 = value
        
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
                    

    @property
    def presentedBy(self):
        return self.__presentedBy

    @presentedBy.setter
    def presentedBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_service_Service__presentedBy", None)
        self.__presentedBy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ServiceProfile"):
                opp_val = getattr(old_value, "ServiceProfile", None)
                if opp_val == self:
                    setattr(old_value, "ServiceProfile", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ServiceProfile"):
                opp_val = getattr(value, "ServiceProfile", None)
                setattr(value, "ServiceProfile", self)
