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
Operation: Enumeration = Enumeration(
    name="Operation",
    literals={
            EnumerationLiteral(name="_create"),
			EnumerationLiteral(name="read"),
			EnumerationLiteral(name="update"),
			EnumerationLiteral(name="delete"),
			EnumerationLiteral(name="readONE"),
			EnumerationLiteral(name="readALL"),
			EnumerationLiteral(name="forward")
    }
)

AttributeType: Enumeration = Enumeration(
    name="AttributeType",
    literals={
            EnumerationLiteral(name="VARCHAR"),
			EnumerationLiteral(name="BIGINTEGER"),
			EnumerationLiteral(name="DOUBLE"),
			EnumerationLiteral(name="OID"),
			EnumerationLiteral(name="VOID")
    }
)

# Classes
SMVC_Entity = Class(name="SMVC::Entity")
SMVC_SMVCApplication = Class(name="SMVC::SMVCApplication")
SMVC_Controller = Class(name="SMVC::Controller")
SMVC_DataAccessObject = Class(name="SMVC::DataAccessObject")
SMVC_Page = Class(name="SMVC::Page")
SMVC_EntityController = Class(name="SMVC::EntityController")
Controller = Class(name="Controller")
SMVC_Attribute = Class(name="SMVC::Attribute")
SMVC_Link = Class(name="SMVC::Link")
SMVC_View = Class(name="SMVC::View")
SMVC_Component = Class(name="SMVC::Component", is_abstract=True)
SMVC_EntityComponent = Class(name="SMVC::EntityComponent", is_abstract=True)
Component = Class(name="Component")
SMVC_List = Class(name="SMVC::List")
EntityComponent = Class(name="EntityComponent")
SMVC_SupportedOperation = Class(name="SMVC::SupportedOperation")
SMVC_Form = Class(name="SMVC::Form")

# SMVC_Entity class attributes and methods
SMVC_Entity_name: Property = Property(name="name", type=StringType)
SMVC_Entity.attributes={SMVC_Entity_name}

# SMVC_SMVCApplication class attributes and methods
SMVC_SMVCApplication_name: Property = Property(name="name", type=StringType)
SMVC_SMVCApplication.attributes={SMVC_SMVCApplication_name}

# SMVC_Controller class attributes and methods
SMVC_Controller_url: Property = Property(name="url", type=StringType)
SMVC_Controller_operation: Property = Property(name="operation", type=StringType)
SMVC_Controller.attributes={SMVC_Controller_operation, SMVC_Controller_url}

# SMVC_DataAccessObject class attributes and methods
SMVC_DataAccessObject_name: Property = Property(name="name", type=StringType)
SMVC_DataAccessObject_showDirectInstancesOnly: Property = Property(name="showDirectInstancesOnly", type=BooleanType)
SMVC_DataAccessObject.attributes={SMVC_DataAccessObject_showDirectInstancesOnly, SMVC_DataAccessObject_name}

# SMVC_Page class attributes and methods
SMVC_Page_title: Property = Property(name="title", type=StringType)
SMVC_Page.attributes={SMVC_Page_title}

# SMVC_EntityController class attributes and methods
SMVC_EntityController_returnOKURL: Property = Property(name="returnOKURL", type=StringType)
SMVC_EntityController_returnKOURL: Property = Property(name="returnKOURL", type=StringType)
SMVC_EntityController.attributes={SMVC_EntityController_returnOKURL, SMVC_EntityController_returnKOURL}

# Controller class attributes and methods

# SMVC_Attribute class attributes and methods
SMVC_Attribute_name: Property = Property(name="name", type=StringType)
SMVC_Attribute_type: Property = Property(name="type", type=StringType)
SMVC_Attribute_multiValued: Property = Property(name="multiValued", type=BooleanType)
SMVC_Attribute.attributes={SMVC_Attribute_name, SMVC_Attribute_type, SMVC_Attribute_multiValued}

# SMVC_Link class attributes and methods
SMVC_Link_url: Property = Property(name="url", type=StringType)
SMVC_Link.attributes={SMVC_Link_url}

# SMVC_View class attributes and methods
SMVC_View_text: Property = Property(name="text", type=StringType)
SMVC_View.attributes={SMVC_View_text}

# SMVC_Component class attributes and methods

# SMVC_EntityComponent class attributes and methods

# Component class attributes and methods

# SMVC_List class attributes and methods

# EntityComponent class attributes and methods

# SMVC_SupportedOperation class attributes and methods
SMVC_SupportedOperation_operationKind: Property = Property(name="operationKind", type=StringType)
SMVC_SupportedOperation_url: Property = Property(name="url", type=StringType)
SMVC_SupportedOperation.attributes={SMVC_SupportedOperation_operationKind, SMVC_SupportedOperation_url}

# SMVC_Form class attributes and methods

# Relationships
entities6: BinaryAssociation = BinaryAssociation(
    name="entities6",
    ends={
        Property(name="SMVC_Entity", type=SMVC_SMVCApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="SMVC_SMVCApplication7", type=SMVC_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
homeController0: BinaryAssociation = BinaryAssociation(
    name="homeController0",
    ends={
        Property(name="SMVC_Controller", type=SMVC_SMVCApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="SMVC_SMVCApplication", type=SMVC_Controller, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
controller1: BinaryAssociation = BinaryAssociation(
    name="controller1",
    ends={
        Property(name="SMVC_Controller3", type=SMVC_SMVCApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="SMVC_SMVCApplication2", type=SMVC_Controller, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
daos4: BinaryAssociation = BinaryAssociation(
    name="daos4",
    ends={
        Property(name="SMVC_DataAccessObject", type=SMVC_SMVCApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="SMVC_SMVCApplication5", type=SMVC_DataAccessObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subController9: BinaryAssociation = BinaryAssociation(
    name="subController9",
    ends={
        Property(name="SMVC_Controller10", type=SMVC_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="SMVC_Controller8", type=SMVC_Controller, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
page11: BinaryAssociation = BinaryAssociation(
    name="page11",
    ends={
        Property(name="SMVC_Page", type=SMVC_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="SMVC_Controller12", type=SMVC_Page, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dao13: BinaryAssociation = BinaryAssociation(
    name="dao13",
    ends={
        Property(name="SMVC_DataAccessObject14", type=SMVC_EntityController, multiplicity=Multiplicity(1, 1)),
        Property(name="SMVC_EntityController", type=SMVC_DataAccessObject, multiplicity=Multiplicity(1, 1))
    }
)
forEntity15: BinaryAssociation = BinaryAssociation(
    name="forEntity15",
    ends={
        Property(name="SMVC_Entity17", type=SMVC_DataAccessObject, multiplicity=Multiplicity(1, 1)),
        Property(name="SMVC_DataAccessObject16", type=SMVC_Entity, multiplicity=Multiplicity(1, 1))
    }
)
attributes18: BinaryAssociation = BinaryAssociation(
    name="attributes18",
    ends={
        Property(name="SMVC_Attribute", type=SMVC_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="SMVC_Entity19", type=SMVC_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
complexType20: BinaryAssociation = BinaryAssociation(
    name="complexType20",
    ends={
        Property(name="SMVC_Entity22", type=SMVC_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="SMVC_Attribute21", type=SMVC_Entity, multiplicity=Multiplicity(0, 1))
    }
)
view25: BinaryAssociation = BinaryAssociation(
    name="view25",
    ends={
        Property(name="SMVC_View", type=SMVC_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="SMVC_Page26", type=SMVC_View, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
links23: BinaryAssociation = BinaryAssociation(
    name="links23",
    ends={
        Property(name="SMVC_Link", type=SMVC_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="SMVC_Page24", type=SMVC_Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entity29: BinaryAssociation = BinaryAssociation(
    name="entity29",
    ends={
        Property(name="SMVC_Entity30", type=SMVC_EntityComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="SMVC_EntityComponent", type=SMVC_Entity, multiplicity=Multiplicity(1, 1))
    }
)
components27: BinaryAssociation = BinaryAssociation(
    name="components27",
    ends={
        Property(name="SMVC_Component", type=SMVC_View, multiplicity=Multiplicity(1, 1)),
        Property(name="SMVC_View28", type=SMVC_Component, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
supportedOperations31: BinaryAssociation = BinaryAssociation(
    name="supportedOperations31",
    ends={
        Property(name="SMVC_SupportedOperation", type=SMVC_List, multiplicity=Multiplicity(1, 1)),
        Property(name="SMVC_List", type=SMVC_SupportedOperation, multiplicity=Multiplicity(0, 4), is_composite=True)
    }
)

# Generalizations
gen_SMVC_EntityController_Controller = Generalization(general=Controller, specific=SMVC_EntityController)
gen_SMVC_EntityComponent_Component = Generalization(general=Component, specific=SMVC_EntityComponent)
gen_SMVC_List_EntityComponent = Generalization(general=EntityComponent, specific=SMVC_List)
gen_SMVC_Form_EntityComponent = Generalization(general=EntityComponent, specific=SMVC_Form)

# Domain Model
domain_model = DomainModel(
    name="SMVC",
    types={SMVC_Entity, SMVC_SMVCApplication, SMVC_Controller, SMVC_DataAccessObject, SMVC_Page, SMVC_EntityController, Controller, SMVC_Attribute, SMVC_Link, SMVC_View, SMVC_Component, SMVC_EntityComponent, Component, SMVC_List, EntityComponent, SMVC_SupportedOperation, SMVC_Form, Operation, AttributeType},
    associations={entities6, homeController0, controller1, daos4, subController9, page11, dao13, forEntity15, attributes18, complexType20, view25, links23, entity29, components27, supportedOperations31},
    generalizations={gen_SMVC_EntityController_Controller, gen_SMVC_EntityComponent_Component, gen_SMVC_List_EntityComponent, gen_SMVC_Form_EntityComponent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)