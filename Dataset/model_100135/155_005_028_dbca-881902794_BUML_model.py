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
DataType: Enumeration = Enumeration(
    name="DataType",
    literals={
            EnumerationLiteral(name="Bool"),
			EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Real"),
			EnumerationLiteral(name="Char"),
			EnumerationLiteral(name="String"),
			EnumerationLiteral(name="Date"),
			EnumerationLiteral(name="DateTime"),
			EnumerationLiteral(name="Time"),
			EnumerationLiteral(name="Blob"),
			EnumerationLiteral(name="GUID")
    }
)

RelationshipType: Enumeration = Enumeration(
    name="RelationshipType",
    literals={
            EnumerationLiteral(name="OneToOne"),
			EnumerationLiteral(name="OneToMany"),
			EnumerationLiteral(name="ManyToOne"),
			EnumerationLiteral(name="ManyToMany")
    }
)

EntityFormType: Enumeration = Enumeration(
    name="EntityFormType",
    literals={
            EnumerationLiteral(name="Select"),
			EnumerationLiteral(name="Insert"),
			EnumerationLiteral(name="Update"),
			EnumerationLiteral(name="Delete")
    }
)

# Classes
dbca_Entity = Class(name="dbca_Entity", is_abstract=True)
DatabaseElement = Class(name="DatabaseElement")
dbca_PrimaryProperty = Class(name="dbca_PrimaryProperty")
dbca_Property = Class(name="dbca_Property")
dbca_Element = Class(name="dbca_Element", is_abstract=True)
dbca_CommentedElement = Class(name="dbca_CommentedElement", is_abstract=True)
Element = Class(name="Element")
dbca_NamedElement = Class(name="dbca_NamedElement", is_abstract=True)
CommentedElement = Class(name="CommentedElement")
dbca_Application = Class(name="dbca_Application")
NamedElement = Class(name="NamedElement")
dbca_Database = Class(name="dbca_Database")
dbca_Server = Class(name="dbca_Server")
dbca_Client = Class(name="dbca_Client")
dbca_DatabaseElement = Class(name="dbca_DatabaseElement", is_abstract=True)
dbca_Attribute = Class(name="dbca_Attribute", is_abstract=True)
dbca_Query = Class(name="dbca_Query")
dbca_ServerElement = Class(name="dbca_ServerElement", is_abstract=True)
dbca_Service = Class(name="dbca_Service", is_abstract=True)
ServerElement = Class(name="ServerElement")
dbca_Relationship = Class(name="dbca_Relationship")
dbca_AbstractEntity = Class(name="dbca_AbstractEntity")
Entity = Class(name="Entity")
dbca_PersistentEntity = Class(name="dbca_PersistentEntity")
dbca_ComputedEntity = Class(name="dbca_ComputedEntity")
dbca_Event = Class(name="dbca_Event")
dbca_Parameter = Class(name="dbca_Parameter", is_abstract=True)
dbca_DataParameter = Class(name="dbca_DataParameter")
Parameter_ = Class(name="Parameter")
dbca_EntityParameter = Class(name="dbca_EntityParameter")
dbca_Function = Class(name="dbca_Function")
dbca_Operation = Class(name="dbca_Operation")
dbca_EntityService = Class(name="dbca_EntityService")
Service = Class(name="Service")
dbca_QueryService = Class(name="dbca_QueryService")
dbca_OperationService = Class(name="dbca_OperationService")
dbca_CustomService = Class(name="dbca_CustomService")
dbca_ClientElement = Class(name="dbca_ClientElement", is_abstract=True)
dbca_Form = Class(name="dbca_Form", is_abstract=True)
ClientElement = Class(name="ClientElement")
dbca_EntityForm = Class(name="dbca_EntityForm")
Form = Class(name="Form")
dbca_EntityContainmentForm = Class(name="dbca_EntityContainmentForm")
dbca_CustomForm = Class(name="dbca_CustomForm")
Attribute = Class(name="Attribute")

# dbca_Entity class attributes and methods

# DatabaseElement class attributes and methods

# dbca_PrimaryProperty class attributes and methods

# dbca_Property class attributes and methods
dbca_Property_isNullable: Property = Property(name="isNullable", type=BooleanType)
dbca_Property_defaultValue: Property = Property(name="defaultValue", type=StringType)
dbca_Property.attributes={dbca_Property_defaultValue, dbca_Property_isNullable}

# dbca_Element class attributes and methods

# dbca_CommentedElement class attributes and methods
dbca_CommentedElement_comment: Property = Property(name="comment", type=StringType)
dbca_CommentedElement.attributes={dbca_CommentedElement_comment}

# Element class attributes and methods

# dbca_NamedElement class attributes and methods
dbca_NamedElement_name: Property = Property(name="name", type=StringType)
dbca_NamedElement.attributes={dbca_NamedElement_name}

# CommentedElement class attributes and methods

# dbca_Application class attributes and methods

# NamedElement class attributes and methods

# dbca_Database class attributes and methods

# dbca_Server class attributes and methods

# dbca_Client class attributes and methods

# dbca_DatabaseElement class attributes and methods

# dbca_Attribute class attributes and methods
dbca_Attribute_type: Property = Property(name="type", type=StringType)
dbca_Attribute_maxLength: Property = Property(name="maxLength", type=IntegerType)
dbca_Attribute.attributes={dbca_Attribute_type, dbca_Attribute_maxLength}

# dbca_Query class attributes and methods

# dbca_ServerElement class attributes and methods

# dbca_Service class attributes and methods

# ServerElement class attributes and methods

# dbca_Relationship class attributes and methods
dbca_Relationship_type: Property = Property(name="type", type=StringType)
dbca_Relationship_isNullable: Property = Property(name="isNullable", type=BooleanType)
dbca_Relationship_isContainment: Property = Property(name="isContainment", type=StringType)
dbca_Relationship.attributes={dbca_Relationship_type, dbca_Relationship_isContainment, dbca_Relationship_isNullable}

# dbca_AbstractEntity class attributes and methods

# Entity class attributes and methods

# dbca_PersistentEntity class attributes and methods

# dbca_ComputedEntity class attributes and methods

# dbca_Event class attributes and methods

# dbca_Parameter class attributes and methods

# dbca_DataParameter class attributes and methods
dbca_DataParameter_type: Property = Property(name="type", type=StringType)
dbca_DataParameter.attributes={dbca_DataParameter_type}

# Parameter class attributes and methods

# dbca_EntityParameter class attributes and methods

# dbca_Function class attributes and methods
dbca_Function_returnType: Property = Property(name="returnType", type=StringType)
dbca_Function.attributes={dbca_Function_returnType}

# dbca_Operation class attributes and methods

# dbca_EntityService class attributes and methods

# Service class attributes and methods

# dbca_QueryService class attributes and methods

# dbca_OperationService class attributes and methods

# dbca_CustomService class attributes and methods

# dbca_ClientElement class attributes and methods

# dbca_Form class attributes and methods

# ClientElement class attributes and methods

# dbca_EntityForm class attributes and methods
dbca_EntityForm_type: Property = Property(name="type", type=StringType)
dbca_EntityForm.attributes={dbca_EntityForm_type}

# Form class attributes and methods

# dbca_EntityContainmentForm class attributes and methods

# dbca_CustomForm class attributes and methods

# Attribute class attributes and methods

# Relationships
primaries7: BinaryAssociation = BinaryAssociation(
    name="primaries7",
    ends={
        Property(name="dbca_PrimaryProperty", type=dbca_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="dbca_Entity", type=dbca_PrimaryProperty, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
properties8: BinaryAssociation = BinaryAssociation(
    name="properties8",
    ends={
        Property(name="dbca_Property", type=dbca_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="dbca_Entity9", type=dbca_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
database0: BinaryAssociation = BinaryAssociation(
    name="database0",
    ends={
        Property(name="dbca_Database", type=dbca_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="dbca_Application", type=dbca_Database, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
server1: BinaryAssociation = BinaryAssociation(
    name="server1",
    ends={
        Property(name="dbca_Server", type=dbca_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="dbca_Application2", type=dbca_Server, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
clients3: BinaryAssociation = BinaryAssociation(
    name="clients3",
    ends={
        Property(name="dbca_Client", type=dbca_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="dbca_Application4", type=dbca_Client, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements5: BinaryAssociation = BinaryAssociation(
    name="elements5",
    ends={
        Property(name="dbca_DatabaseElement", type=dbca_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="dbca_Database6", type=dbca_DatabaseElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements25: BinaryAssociation = BinaryAssociation(
    name="elements25",
    ends={
        Property(name="dbca_ServerElement", type=dbca_Server, multiplicity=Multiplicity(1, 1)),
        Property(name="dbca_Server26", type=dbca_ServerElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relationships10: BinaryAssociation = BinaryAssociation(
    name="relationships10",
    ends={
        Property(name="dbca_Relationship", type=dbca_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="dbca_Entity11", type=dbca_Relationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
super13: BinaryAssociation = BinaryAssociation(
    name="super13",
    ends={
        Property(name="dbca_Entity14", type=dbca_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="dbca_Entity12", type=dbca_Entity, multiplicity=Multiplicity(0, 1))
    }
)
target15: BinaryAssociation = BinaryAssociation(
    name="target15",
    ends={
        Property(name="dbca_Entity17", type=dbca_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="dbca_Relationship16", type=dbca_Entity, multiplicity=Multiplicity(1, 1))
    }
)
properties18: BinaryAssociation = BinaryAssociation(
    name="properties18",
    ends={
        Property(name="dbca_Property20", type=dbca_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="dbca_Relationship19", type=dbca_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entity21: BinaryAssociation = BinaryAssociation(
    name="entity21",
    ends={
        Property(name="dbca_Entity22", type=dbca_EntityParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="dbca_EntityParameter", type=dbca_Entity, multiplicity=Multiplicity(1, 1))
    }
)
parameters23: BinaryAssociation = BinaryAssociation(
    name="parameters23",
    ends={
        Property(name="dbca_DataParameter", type=dbca_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="dbca_Function", type=dbca_DataParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters24: BinaryAssociation = BinaryAssociation(
    name="parameters24",
    ends={
        Property(name="dbca_Parameter", type=dbca_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="dbca_Operation", type=dbca_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entity27: BinaryAssociation = BinaryAssociation(
    name="entity27",
    ends={
        Property(name="dbca_Entity28", type=dbca_EntityService, multiplicity=Multiplicity(1, 1)),
        Property(name="dbca_EntityService", type=dbca_Entity, multiplicity=Multiplicity(1, 1))
    }
)
query29: BinaryAssociation = BinaryAssociation(
    name="query29",
    ends={
        Property(name="dbca_Query", type=dbca_QueryService, multiplicity=Multiplicity(1, 1)),
        Property(name="dbca_QueryService", type=dbca_Query, multiplicity=Multiplicity(1, 1))
    }
)
operation30: BinaryAssociation = BinaryAssociation(
    name="operation30",
    ends={
        Property(name="dbca_Operation31", type=dbca_OperationService, multiplicity=Multiplicity(1, 1)),
        Property(name="dbca_OperationService", type=dbca_Operation, multiplicity=Multiplicity(1, 1))
    }
)
elements32: BinaryAssociation = BinaryAssociation(
    name="elements32",
    ends={
        Property(name="dbca_ClientElement", type=dbca_Client, multiplicity=Multiplicity(1, 1)),
        Property(name="dbca_Client33", type=dbca_ClientElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entity34: BinaryAssociation = BinaryAssociation(
    name="entity34",
    ends={
        Property(name="dbca_Entity35", type=dbca_EntityForm, multiplicity=Multiplicity(1, 1)),
        Property(name="dbca_EntityForm", type=dbca_Entity, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_dbca_Entity_DatabaseElement = Generalization(general=DatabaseElement, specific=dbca_Entity)
gen_dbca_CommentedElement_Element = Generalization(general=Element, specific=dbca_CommentedElement)
gen_dbca_NamedElement_CommentedElement = Generalization(general=CommentedElement, specific=dbca_NamedElement)
gen_dbca_Application_NamedElement = Generalization(general=NamedElement, specific=dbca_Application)
gen_dbca_Database_NamedElement = Generalization(general=NamedElement, specific=dbca_Database)
gen_dbca_DatabaseElement_NamedElement = Generalization(general=NamedElement, specific=dbca_DatabaseElement)
gen_dbca_Attribute_NamedElement = Generalization(general=NamedElement, specific=dbca_Attribute)
gen_dbca_Query_DatabaseElement = Generalization(general=DatabaseElement, specific=dbca_Query)
gen_dbca_Server_NamedElement = Generalization(general=NamedElement, specific=dbca_Server)
gen_dbca_ServerElement_NamedElement = Generalization(general=NamedElement, specific=dbca_ServerElement)
gen_dbca_Service_ServerElement = Generalization(general=ServerElement, specific=dbca_Service)
gen_dbca_AbstractEntity_Entity = Generalization(general=Entity, specific=dbca_AbstractEntity)
gen_dbca_PersistentEntity_Entity = Generalization(general=Entity, specific=dbca_PersistentEntity)
gen_dbca_ComputedEntity_Entity = Generalization(general=Entity, specific=dbca_ComputedEntity)
gen_dbca_Relationship_NamedElement = Generalization(general=NamedElement, specific=dbca_Relationship)
gen_dbca_Event_DatabaseElement = Generalization(general=DatabaseElement, specific=dbca_Event)
gen_dbca_Parameter_NamedElement = Generalization(general=NamedElement, specific=dbca_Parameter)
gen_dbca_DataParameter_Parameter = Generalization(general=Parameter_, specific=dbca_DataParameter)
gen_dbca_EntityParameter_Parameter = Generalization(general=Parameter_, specific=dbca_EntityParameter)
gen_dbca_Function_DatabaseElement = Generalization(general=DatabaseElement, specific=dbca_Function)
gen_dbca_Operation_DatabaseElement = Generalization(general=DatabaseElement, specific=dbca_Operation)
gen_dbca_EntityService_Service = Generalization(general=Service, specific=dbca_EntityService)
gen_dbca_QueryService_Service = Generalization(general=Service, specific=dbca_QueryService)
gen_dbca_OperationService_Service = Generalization(general=Service, specific=dbca_OperationService)
gen_dbca_CustomService_Service = Generalization(general=Service, specific=dbca_CustomService)
gen_dbca_Client_NamedElement = Generalization(general=NamedElement, specific=dbca_Client)
gen_dbca_ClientElement_NamedElement = Generalization(general=NamedElement, specific=dbca_ClientElement)
gen_dbca_Form_ClientElement = Generalization(general=ClientElement, specific=dbca_Form)
gen_dbca_EntityForm_Form = Generalization(general=Form, specific=dbca_EntityForm)
gen_dbca_EntityContainmentForm_Form = Generalization(general=Form, specific=dbca_EntityContainmentForm)
gen_dbca_CustomForm_Form = Generalization(general=Form, specific=dbca_CustomForm)
gen_dbca_PrimaryProperty_Attribute = Generalization(general=Attribute, specific=dbca_PrimaryProperty)
gen_dbca_Property_Attribute = Generalization(general=Attribute, specific=dbca_Property)

# Domain Model
domain_model = DomainModel(
    name="dbca",
    types={dbca_Entity, DatabaseElement, dbca_PrimaryProperty, dbca_Property, dbca_Element, dbca_CommentedElement, Element, dbca_NamedElement, CommentedElement, dbca_Application, NamedElement, dbca_Database, dbca_Server, dbca_Client, dbca_DatabaseElement, dbca_Attribute, dbca_Query, dbca_ServerElement, dbca_Service, ServerElement, dbca_Relationship, dbca_AbstractEntity, Entity, dbca_PersistentEntity, dbca_ComputedEntity, dbca_Event, dbca_Parameter, dbca_DataParameter, Parameter_, dbca_EntityParameter, dbca_Function, dbca_Operation, dbca_EntityService, Service, dbca_QueryService, dbca_OperationService, dbca_CustomService, dbca_ClientElement, dbca_Form, ClientElement, dbca_EntityForm, Form, dbca_EntityContainmentForm, dbca_CustomForm, Attribute, DataType, RelationshipType, EntityFormType},
    associations={primaries7, properties8, database0, server1, clients3, elements5, elements25, relationships10, super13, target15, properties18, entity21, parameters23, parameters24, entity27, query29, operation30, elements32, entity34},
    generalizations={gen_dbca_Entity_DatabaseElement, gen_dbca_CommentedElement_Element, gen_dbca_NamedElement_CommentedElement, gen_dbca_Application_NamedElement, gen_dbca_Database_NamedElement, gen_dbca_DatabaseElement_NamedElement, gen_dbca_Attribute_NamedElement, gen_dbca_Query_DatabaseElement, gen_dbca_Server_NamedElement, gen_dbca_ServerElement_NamedElement, gen_dbca_Service_ServerElement, gen_dbca_AbstractEntity_Entity, gen_dbca_PersistentEntity_Entity, gen_dbca_ComputedEntity_Entity, gen_dbca_Relationship_NamedElement, gen_dbca_Event_DatabaseElement, gen_dbca_Parameter_NamedElement, gen_dbca_DataParameter_Parameter, gen_dbca_EntityParameter_Parameter, gen_dbca_Function_DatabaseElement, gen_dbca_Operation_DatabaseElement, gen_dbca_EntityService_Service, gen_dbca_QueryService_Service, gen_dbca_OperationService_Service, gen_dbca_CustomService_Service, gen_dbca_Client_NamedElement, gen_dbca_ClientElement_NamedElement, gen_dbca_Form_ClientElement, gen_dbca_EntityForm_Form, gen_dbca_EntityContainmentForm_Form, gen_dbca_CustomForm_Form, gen_dbca_PrimaryProperty_Attribute, gen_dbca_Property_Attribute},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)