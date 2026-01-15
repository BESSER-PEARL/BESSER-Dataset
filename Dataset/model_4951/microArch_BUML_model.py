####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
CRUDOperation: Enumeration = Enumeration(
    name="CRUDOperation",
    literals={
            EnumerationLiteral(name="create"),
			EnumerationLiteral(name="update"),
			EnumerationLiteral(name="delete"),
			EnumerationLiteral(name="retrieve")
    }
)

CommandType: Enumeration = Enumeration(
    name="CommandType",
    literals={
            EnumerationLiteral(name="compensate"),
			EnumerationLiteral(name="invoke"),
			EnumerationLiteral(name="reply")
    }
)

AttributePrimitiveValue: Enumeration = Enumeration(
    name="AttributePrimitiveValue",
    literals={
            EnumerationLiteral(name="String"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="char"),
			EnumerationLiteral(name="float"),
			EnumerationLiteral(name="long"),
			EnumerationLiteral(name="short")
    }
)

# Classes
micro_MicroserviceArchitecture = Class(name="micro::MicroserviceArchitecture")
NamedElement = Class(name="NamedElement")
micro_Service = Class(name="micro::Service", is_abstract=True)
micro_Model = Class(name="micro::Model")
micro_API = Class(name="micro::API")
micro_Attribute = Class(name="micro::Attribute", is_abstract=True)
micro_ModelEvent = Class(name="micro::ModelEvent")
micro_AggregateService = Class(name="micro::AggregateService")
Service = Class(name="Service")
micro_Operation = Class(name="micro::Operation")
micro_Command = Class(name="micro::Command")
micro_Info = Class(name="micro::Info")
micro_ViewService = Class(name="micro::ViewService")
micro_Event = Class(name="micro::Event")
micro_Saga = Class(name="micro::Saga")
micro_NamedElement = Class(name="micro::NamedElement")
micro_Data = Class(name="micro::Data")
micro_Step = Class(name="micro::Step")
micro_ReferenceAttribute = Class(name="micro::ReferenceAttribute")
Attribute = Class(name="Attribute")
micro_PrimitiveTypeAttribute = Class(name="micro::PrimitiveTypeAttribute")

# micro_MicroserviceArchitecture class attributes and methods

# NamedElement class attributes and methods

# micro_Service class attributes and methods
micro_Service_fullname: Property = Property(name="fullname", type=StringType)
micro_Service_description: Property = Property(name="description", type=StringType)
micro_Service_shortname: Property = Property(name="shortname", type=StringType)
micro_Service_port: Property = Property(name="port", type=IntegerType)
micro_Service.attributes={micro_Service_description, micro_Service_shortname, micro_Service_fullname, micro_Service_port}

# micro_Model class attributes and methods

# micro_API class attributes and methods

# micro_Attribute class attributes and methods
micro_Attribute_name: Property = Property(name="name", type=StringType)
micro_Attribute_isMany: Property = Property(name="isMany", type=BooleanType)
micro_Attribute_isId: Property = Property(name="isId", type=BooleanType)
micro_Attribute_isGenerated: Property = Property(name="isGenerated", type=BooleanType)
micro_Attribute.attributes={micro_Attribute_isGenerated, micro_Attribute_isId, micro_Attribute_isMany, micro_Attribute_name}

# micro_ModelEvent class attributes and methods

# micro_AggregateService class attributes and methods
micro_AggregateService_m_ReferenceModelsIncluded: Method = Method(name="ReferenceModelsIncluded", parameters={}, type=BooleanType)
micro_AggregateService.methods={micro_AggregateService_m_ReferenceModelsIncluded}

# Service class attributes and methods

# micro_Operation class attributes and methods
micro_Operation_operationType: Property = Property(name="operationType", type=StringType)
micro_Operation_isMethodController: Property = Property(name="isMethodController", type=BooleanType)
micro_Operation.attributes={micro_Operation_operationType, micro_Operation_isMethodController}

# micro_Command class attributes and methods
micro_Command_commandType: Property = Property(name="commandType", type=StringType)
micro_Command_isReplyInfoMany: Property = Property(name="isReplyInfoMany", type=BooleanType)
micro_Command.attributes={micro_Command_isReplyInfoMany, micro_Command_commandType}

# micro_Info class attributes and methods

# micro_ViewService class attributes and methods

# micro_Event class attributes and methods

# micro_Saga class attributes and methods

# micro_NamedElement class attributes and methods
micro_NamedElement_name: Property = Property(name="name", type=StringType)
micro_NamedElement.attributes={micro_NamedElement_name}

# micro_Data class attributes and methods

# micro_Step class attributes and methods

# micro_ReferenceAttribute class attributes and methods

# Attribute class attributes and methods

# micro_PrimitiveTypeAttribute class attributes and methods
micro_PrimitiveTypeAttribute_type: Property = Property(name="type", type=StringType)
micro_PrimitiveTypeAttribute.attributes={micro_PrimitiveTypeAttribute_type}

# Relationships
services0: BinaryAssociation = BinaryAssociation(
    name="services0",
    ends={
        Property(name="micro_Service", type=micro_MicroserviceArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_MicroserviceArchitecture", type=micro_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
models1: BinaryAssociation = BinaryAssociation(
    name="models1",
    ends={
        Property(name="micro_Model", type=micro_MicroserviceArchitecture, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_MicroserviceArchitecture2", type=micro_Model, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
api10: BinaryAssociation = BinaryAssociation(
    name="api10",
    ends={
        Property(name="micro_API", type=micro_AggregateService, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_AggregateService", type=micro_API, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
handleModelEvents11: BinaryAssociation = BinaryAssociation(
    name="handleModelEvents11",
    ends={
        Property(name="micro_ModelEvent13", type=micro_AggregateService, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_AggregateService12", type=micro_ModelEvent, multiplicity=Multiplicity(0, 9999))
    }
)
attributes3: BinaryAssociation = BinaryAssociation(
    name="attributes3",
    ends={
        Property(name="Attribute", type=micro_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=micro_Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
model4: BinaryAssociation = BinaryAssociation(
    name="model4",
    ends={
        Property(name="micro_Model5", type=micro_ModelEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_ModelEvent", type=micro_Model, multiplicity=Multiplicity(1, 1))
    }
)
aggregateService6: BinaryAssociation = BinaryAssociation(
    name="aggregateService6",
    ends={
        Property(name="AggregateService", type=micro_ModelEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="modelEvents", type=micro_AggregateService, multiplicity=Multiplicity(0, 1))
    }
)
modelEvents7: BinaryAssociation = BinaryAssociation(
    name="modelEvents7",
    ends={
        Property(name="ModelEvent", type=micro_AggregateService, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregateService", type=micro_ModelEvent, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
operation8: BinaryAssociation = BinaryAssociation(
    name="operation8",
    ends={
        Property(name="Operation", type=micro_AggregateService, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregateService9", type=micro_Operation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
commands28: BinaryAssociation = BinaryAssociation(
    name="commands28",
    ends={
        Property(name="Command", type=micro_API, multiplicity=Multiplicity(1, 1)),
        Property(name="api29", type=micro_Command, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
infos30: BinaryAssociation = BinaryAssociation(
    name="infos30",
    ends={
        Property(name="Info", type=micro_API, multiplicity=Multiplicity(1, 1)),
        Property(name="api31", type=micro_Info, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
models14: BinaryAssociation = BinaryAssociation(
    name="models14",
    ends={
        Property(name="micro_Model16", type=micro_AggregateService, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_AggregateService15", type=micro_Model, multiplicity=Multiplicity(1, 9999))
    }
)
replicateServices17: BinaryAssociation = BinaryAssociation(
    name="replicateServices17",
    ends={
        Property(name="micro_AggregateService18", type=micro_ViewService, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_ViewService", type=micro_AggregateService, multiplicity=Multiplicity(0, 9999))
    }
)
publish19: BinaryAssociation = BinaryAssociation(
    name="publish19",
    ends={
        Property(name="micro_Event", type=micro_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_Operation", type=micro_Event, multiplicity=Multiplicity(0, 1))
    }
)
Saga20: BinaryAssociation = BinaryAssociation(
    name="Saga20",
    ends={
        Property(name="micro_Saga", type=micro_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_Operation21", type=micro_Saga, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
model22: BinaryAssociation = BinaryAssociation(
    name="model22",
    ends={
        Property(name="micro_Model24", type=micro_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_Operation23", type=micro_Model, multiplicity=Multiplicity(1, 1))
    }
)
aggregateService25: BinaryAssociation = BinaryAssociation(
    name="aggregateService25",
    ends={
        Property(name="AggregateService26", type=micro_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=micro_AggregateService, multiplicity=Multiplicity(0, 1))
    }
)
events27: BinaryAssociation = BinaryAssociation(
    name="events27",
    ends={
        Property(name="Event", type=micro_API, multiplicity=Multiplicity(1, 1)),
        Property(name="api", type=micro_Event, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
Steps43: BinaryAssociation = BinaryAssociation(
    name="Steps43",
    ends={
        Property(name="micro_Step45", type=micro_Saga, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_Saga44", type=micro_Step, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
Data46: BinaryAssociation = BinaryAssociation(
    name="Data46",
    ends={
        Property(name="micro_Data", type=micro_Saga, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_Saga47", type=micro_Data, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
replyInfo32: BinaryAssociation = BinaryAssociation(
    name="replyInfo32",
    ends={
        Property(name="micro_Info", type=micro_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_Command", type=micro_Info, multiplicity=Multiplicity(0, 1))
    }
)
api33: BinaryAssociation = BinaryAssociation(
    name="api33",
    ends={
        Property(name="API", type=micro_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="commands", type=micro_API, multiplicity=Multiplicity(0, 1))
    }
)
api34: BinaryAssociation = BinaryAssociation(
    name="api34",
    ends={
        Property(name="API35", type=micro_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="events", type=micro_API, multiplicity=Multiplicity(0, 1))
    }
)
dto36: BinaryAssociation = BinaryAssociation(
    name="dto36",
    ends={
        Property(name="micro_Model38", type=micro_Info, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_Info37", type=micro_Model, multiplicity=Multiplicity(0, 1))
    }
)
api39: BinaryAssociation = BinaryAssociation(
    name="api39",
    ends={
        Property(name="API40", type=micro_Info, multiplicity=Multiplicity(1, 1)),
        Property(name="infos", type=micro_API, multiplicity=Multiplicity(0, 1))
    }
)
commands41: BinaryAssociation = BinaryAssociation(
    name="commands41",
    ends={
        Property(name="micro_Command42", type=micro_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_Step", type=micro_Command, multiplicity=Multiplicity(1, 9999))
    }
)
model48: BinaryAssociation = BinaryAssociation(
    name="model48",
    ends={
        Property(name="Model", type=micro_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=micro_Model, multiplicity=Multiplicity(0, 1))
    }
)
type49: BinaryAssociation = BinaryAssociation(
    name="type49",
    ends={
        Property(name="micro_Model50", type=micro_ReferenceAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_ReferenceAttribute", type=micro_Model, multiplicity=Multiplicity(1, 1))
    }
)
ModelToView51: BinaryAssociation = BinaryAssociation(
    name="ModelToView51",
    ends={
        Property(name="micro_Model52", type=micro_PrimitiveTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_PrimitiveTypeAttribute", type=micro_Model, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_micro_MicroserviceArchitecture_NamedElement = Generalization(general=NamedElement, specific=micro_MicroserviceArchitecture)
gen_micro_Service_NamedElement = Generalization(general=NamedElement, specific=micro_Service)
gen_micro_Model_NamedElement = Generalization(general=NamedElement, specific=micro_Model)
gen_micro_ModelEvent_NamedElement = Generalization(general=NamedElement, specific=micro_ModelEvent)
gen_micro_AggregateService_Service = Generalization(general=Service, specific=micro_AggregateService)
gen_micro_ViewService_Service = Generalization(general=Service, specific=micro_ViewService)
gen_micro_Operation_NamedElement = Generalization(general=NamedElement, specific=micro_Operation)
gen_micro_API_NamedElement = Generalization(general=NamedElement, specific=micro_API)
gen_micro_Saga_NamedElement = Generalization(general=NamedElement, specific=micro_Saga)
gen_micro_Command_NamedElement = Generalization(general=NamedElement, specific=micro_Command)
gen_micro_Event_NamedElement = Generalization(general=NamedElement, specific=micro_Event)
gen_micro_Info_NamedElement = Generalization(general=NamedElement, specific=micro_Info)
gen_micro_Step_NamedElement = Generalization(general=NamedElement, specific=micro_Step)
gen_micro_Data_NamedElement = Generalization(general=NamedElement, specific=micro_Data)
gen_micro_ReferenceAttribute_Attribute = Generalization(general=Attribute, specific=micro_ReferenceAttribute)
gen_micro_PrimitiveTypeAttribute_Attribute = Generalization(general=Attribute, specific=micro_PrimitiveTypeAttribute)

# Domain Model
domain_model = DomainModel(
    name="micro",
    types={micro_MicroserviceArchitecture, NamedElement, micro_Service, micro_Model, micro_API, micro_Attribute, micro_ModelEvent, micro_AggregateService, Service, micro_Operation, micro_Command, micro_Info, micro_ViewService, micro_Event, micro_Saga, micro_NamedElement, micro_Data, micro_Step, micro_ReferenceAttribute, Attribute, micro_PrimitiveTypeAttribute, CRUDOperation, CommandType, AttributePrimitiveValue},
    associations={services0, models1, api10, handleModelEvents11, attributes3, model4, aggregateService6, modelEvents7, operation8, commands28, infos30, models14, replicateServices17, publish19, Saga20, model22, aggregateService25, events27, Steps43, Data46, replyInfo32, api33, api34, dto36, api39, commands41, model48, type49, ModelToView51},
    generalizations={gen_micro_MicroserviceArchitecture_NamedElement, gen_micro_Service_NamedElement, gen_micro_Model_NamedElement, gen_micro_ModelEvent_NamedElement, gen_micro_AggregateService_Service, gen_micro_ViewService_Service, gen_micro_Operation_NamedElement, gen_micro_API_NamedElement, gen_micro_Saga_NamedElement, gen_micro_Command_NamedElement, gen_micro_Event_NamedElement, gen_micro_Info_NamedElement, gen_micro_Step_NamedElement, gen_micro_Data_NamedElement, gen_micro_ReferenceAttribute_Attribute, gen_micro_PrimitiveTypeAttribute_Attribute},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)