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
            EnumerationLiteral(name="char"),
			EnumerationLiteral(name="float"),
			EnumerationLiteral(name="long"),
			EnumerationLiteral(name="short"),
			EnumerationLiteral(name="String"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="boolean")
    }
)

# Classes
micro_MicroserviceArchitecture = Class(name="micro::MicroserviceArchitecture")
NamedElement = Class(name="NamedElement")
micro_Service = Class(name="micro::Service", is_abstract=True)
micro_Model = Class(name="micro::Model")
Service = Class(name="Service")
micro_Operation = Class(name="micro::Operation")
micro_API = Class(name="micro::API")
micro_ViewService = Class(name="micro::ViewService")
micro_Event = Class(name="micro::Event")
micro_Attribute = Class(name="micro::Attribute", is_abstract=True)
micro_AggregateService = Class(name="micro::AggregateService")
micro_NamedElement = Class(name="micro::NamedElement")
micro_Command = Class(name="micro::Command")
micro_Info = Class(name="micro::Info")
micro_Saga = Class(name="micro::Saga")
micro_Step = Class(name="micro::Step")
micro_Data = Class(name="micro::Data")
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
micro_Service.attributes={micro_Service_port, micro_Service_shortname, micro_Service_description, micro_Service_fullname}

# micro_Model class attributes and methods

# Service class attributes and methods

# micro_Operation class attributes and methods
micro_Operation_operationType: Property = Property(name="operationType", type=StringType)
micro_Operation_isMethodController: Property = Property(name="isMethodController", type=BooleanType)
micro_Operation.attributes={micro_Operation_operationType, micro_Operation_isMethodController}

# micro_API class attributes and methods

# micro_ViewService class attributes and methods

# micro_Event class attributes and methods

# micro_Attribute class attributes and methods
micro_Attribute_name: Property = Property(name="name", type=StringType)
micro_Attribute_isMany: Property = Property(name="isMany", type=BooleanType)
micro_Attribute_isId: Property = Property(name="isId", type=BooleanType)
micro_Attribute_isGenerated: Property = Property(name="isGenerated", type=BooleanType)
micro_Attribute.attributes={micro_Attribute_isMany, micro_Attribute_isGenerated, micro_Attribute_name, micro_Attribute_isId}

# micro_AggregateService class attributes and methods
micro_AggregateService_m_ReferenceModelsIncluded: Method = Method(name="ReferenceModelsIncluded", parameters={}, type=BooleanType)
micro_AggregateService.methods={micro_AggregateService_m_ReferenceModelsIncluded}

# micro_NamedElement class attributes and methods
micro_NamedElement_name: Property = Property(name="name", type=StringType)
micro_NamedElement.attributes={micro_NamedElement_name}

# micro_Command class attributes and methods
micro_Command_commandType: Property = Property(name="commandType", type=StringType)
micro_Command_isReplyInfoMany: Property = Property(name="isReplyInfoMany", type=BooleanType)
micro_Command.attributes={micro_Command_commandType, micro_Command_isReplyInfoMany}

# micro_Info class attributes and methods

# micro_Saga class attributes and methods

# micro_Step class attributes and methods

# micro_Data class attributes and methods

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
aggregateService2: BinaryAssociation = BinaryAssociation(
    name="aggregateService2",
    ends={
        Property(name="models", type=micro_AggregateService, multiplicity=Multiplicity(0, 1)),
        Property(name="AggregateService", type=micro_Model, multiplicity=Multiplicity(1, 1))
    }
)
operation3: BinaryAssociation = BinaryAssociation(
    name="operation3",
    ends={
        Property(name="Operation", type=micro_AggregateService, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregateService", type=micro_Operation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
api4: BinaryAssociation = BinaryAssociation(
    name="api4",
    ends={
        Property(name="micro_API", type=micro_AggregateService, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_AggregateService", type=micro_API, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
models5: BinaryAssociation = BinaryAssociation(
    name="models5",
    ends={
        Property(name="Model", type=micro_AggregateService, multiplicity=Multiplicity(1, 1)),
        Property(name="aggregateService6", type=micro_Model, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
replicateServices7: BinaryAssociation = BinaryAssociation(
    name="replicateServices7",
    ends={
        Property(name="micro_AggregateService8", type=micro_ViewService, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_ViewService", type=micro_AggregateService, multiplicity=Multiplicity(0, 9999))
    }
)
publish9: BinaryAssociation = BinaryAssociation(
    name="publish9",
    ends={
        Property(name="micro_Event", type=micro_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_Operation", type=micro_Event, multiplicity=Multiplicity(0, 1))
    }
)
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="Attribute", type=micro_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=micro_Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
events16: BinaryAssociation = BinaryAssociation(
    name="events16",
    ends={
        Property(name="Event", type=micro_API, multiplicity=Multiplicity(1, 1)),
        Property(name="api", type=micro_Event, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
commands17: BinaryAssociation = BinaryAssociation(
    name="commands17",
    ends={
        Property(name="Command", type=micro_API, multiplicity=Multiplicity(1, 1)),
        Property(name="api18", type=micro_Command, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
infos19: BinaryAssociation = BinaryAssociation(
    name="infos19",
    ends={
        Property(name="Info", type=micro_API, multiplicity=Multiplicity(1, 1)),
        Property(name="api20", type=micro_Info, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
replyInfo21: BinaryAssociation = BinaryAssociation(
    name="replyInfo21",
    ends={
        Property(name="micro_Info", type=micro_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_Command", type=micro_Info, multiplicity=Multiplicity(0, 1))
    }
)
api22: BinaryAssociation = BinaryAssociation(
    name="api22",
    ends={
        Property(name="API", type=micro_Command, multiplicity=Multiplicity(1, 1)),
        Property(name="commands", type=micro_API, multiplicity=Multiplicity(0, 1))
    }
)
api23: BinaryAssociation = BinaryAssociation(
    name="api23",
    ends={
        Property(name="API24", type=micro_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="events", type=micro_API, multiplicity=Multiplicity(0, 1))
    }
)
Saga10: BinaryAssociation = BinaryAssociation(
    name="Saga10",
    ends={
        Property(name="micro_Saga", type=micro_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_Operation11", type=micro_Saga, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
model12: BinaryAssociation = BinaryAssociation(
    name="model12",
    ends={
        Property(name="micro_Model", type=micro_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_Operation13", type=micro_Model, multiplicity=Multiplicity(1, 1))
    }
)
aggregateService14: BinaryAssociation = BinaryAssociation(
    name="aggregateService14",
    ends={
        Property(name="AggregateService15", type=micro_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=micro_AggregateService, multiplicity=Multiplicity(0, 1))
    }
)
commands30: BinaryAssociation = BinaryAssociation(
    name="commands30",
    ends={
        Property(name="micro_Command31", type=micro_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_Step", type=micro_Command, multiplicity=Multiplicity(1, 9999))
    }
)
Steps32: BinaryAssociation = BinaryAssociation(
    name="Steps32",
    ends={
        Property(name="micro_Step34", type=micro_Saga, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_Saga33", type=micro_Step, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
Data35: BinaryAssociation = BinaryAssociation(
    name="Data35",
    ends={
        Property(name="micro_Data", type=micro_Saga, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_Saga36", type=micro_Data, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
model37: BinaryAssociation = BinaryAssociation(
    name="model37",
    ends={
        Property(name="Model38", type=micro_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=micro_Model, multiplicity=Multiplicity(0, 1))
    }
)
type39: BinaryAssociation = BinaryAssociation(
    name="type39",
    ends={
        Property(name="micro_Model40", type=micro_ReferenceAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_ReferenceAttribute", type=micro_Model, multiplicity=Multiplicity(1, 1))
    }
)
dto25: BinaryAssociation = BinaryAssociation(
    name="dto25",
    ends={
        Property(name="micro_Model27", type=micro_Info, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_Info26", type=micro_Model, multiplicity=Multiplicity(0, 1))
    }
)
api28: BinaryAssociation = BinaryAssociation(
    name="api28",
    ends={
        Property(name="API29", type=micro_Info, multiplicity=Multiplicity(1, 1)),
        Property(name="infos", type=micro_API, multiplicity=Multiplicity(0, 1))
    }
)
ModelToView41: BinaryAssociation = BinaryAssociation(
    name="ModelToView41",
    ends={
        Property(name="micro_Model42", type=micro_PrimitiveTypeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="micro_PrimitiveTypeAttribute", type=micro_Model, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_micro_MicroserviceArchitecture_NamedElement = Generalization(general=NamedElement, specific=micro_MicroserviceArchitecture)
gen_micro_Service_NamedElement = Generalization(general=NamedElement, specific=micro_Service)
gen_micro_Model_NamedElement = Generalization(general=NamedElement, specific=micro_Model)
gen_micro_AggregateService_Service = Generalization(general=Service, specific=micro_AggregateService)
gen_micro_ViewService_Service = Generalization(general=Service, specific=micro_ViewService)
gen_micro_Operation_NamedElement = Generalization(general=NamedElement, specific=micro_Operation)
gen_micro_API_NamedElement = Generalization(general=NamedElement, specific=micro_API)
gen_micro_Command_NamedElement = Generalization(general=NamedElement, specific=micro_Command)
gen_micro_Event_NamedElement = Generalization(general=NamedElement, specific=micro_Event)
gen_micro_Info_NamedElement = Generalization(general=NamedElement, specific=micro_Info)
gen_micro_Step_NamedElement = Generalization(general=NamedElement, specific=micro_Step)
gen_micro_Saga_NamedElement = Generalization(general=NamedElement, specific=micro_Saga)
gen_micro_Data_NamedElement = Generalization(general=NamedElement, specific=micro_Data)
gen_micro_ReferenceAttribute_Attribute = Generalization(general=Attribute, specific=micro_ReferenceAttribute)
gen_micro_PrimitiveTypeAttribute_Attribute = Generalization(general=Attribute, specific=micro_PrimitiveTypeAttribute)

# Domain Model
domain_model = DomainModel(
    name="micro",
    types={micro_MicroserviceArchitecture, NamedElement, micro_Service, micro_Model, Service, micro_Operation, micro_API, micro_ViewService, micro_Event, micro_Attribute, micro_AggregateService, micro_NamedElement, micro_Command, micro_Info, micro_Saga, micro_Step, micro_Data, micro_ReferenceAttribute, Attribute, micro_PrimitiveTypeAttribute, CRUDOperation, CommandType, AttributePrimitiveValue},
    associations={services0, aggregateService2, operation3, api4, models5, replicateServices7, publish9, attributes1, events16, commands17, infos19, replyInfo21, api22, api23, Saga10, model12, aggregateService14, commands30, Steps32, Data35, model37, type39, dto25, api28, ModelToView41},
    generalizations={gen_micro_MicroserviceArchitecture_NamedElement, gen_micro_Service_NamedElement, gen_micro_Model_NamedElement, gen_micro_AggregateService_Service, gen_micro_ViewService_Service, gen_micro_Operation_NamedElement, gen_micro_API_NamedElement, gen_micro_Command_NamedElement, gen_micro_Event_NamedElement, gen_micro_Info_NamedElement, gen_micro_Step_NamedElement, gen_micro_Saga_NamedElement, gen_micro_Data_NamedElement, gen_micro_ReferenceAttribute_Attribute, gen_micro_PrimitiveTypeAttribute_Attribute},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)