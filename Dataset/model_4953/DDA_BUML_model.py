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

# Classes
NamedElement = Class(name="NamedElement")
WebApp_Action = Class(name="WebApp::Action")
WebApp_Views = Class(name="WebApp::Views")
IdElement = Class(name="IdElement")
WebApp_Tables = Class(name="WebApp::Tables")
WebApp_Forms = Class(name="WebApp::Forms")
WebApp_styleElements = Class(name="WebApp::styleElements")
WebApp_FormElements = Class(name="WebApp::FormElements")
WebApp_Pages = Class(name="WebApp::Pages")
WebApp_Dummies = Class(name="WebApp::Dummies")
WebApp_Attribute = Class(name="WebApp::Attribute")
WebApp_NamedElement = Class(name="WebApp::NamedElement", is_abstract=True)
WebApp_DynamicApplication = Class(name="WebApp::DynamicApplication")
WebApp_IdElement = Class(name="WebApp::IdElement", is_abstract=True)
WebApp_Controller = Class(name="WebApp::Controller")
WebApp_ActionMapping = Class(name="WebApp::ActionMapping")
WebApp_Entities = Class(name="WebApp::Entities")

# NamedElement class attributes and methods

# WebApp_Action class attributes and methods

# WebApp_Views class attributes and methods

# IdElement class attributes and methods

# WebApp_Tables class attributes and methods

# WebApp_Forms class attributes and methods

# WebApp_styleElements class attributes and methods

# WebApp_FormElements class attributes and methods

# WebApp_Pages class attributes and methods

# WebApp_Dummies class attributes and methods

# WebApp_Attribute class attributes and methods
WebApp_Attribute_value: Property = Property(name="value", type=StringType)
WebApp_Attribute.attributes={WebApp_Attribute_value}

# WebApp_NamedElement class attributes and methods
WebApp_NamedElement_Name: Property = Property(name="Name", type=StringType)
WebApp_NamedElement.attributes={WebApp_NamedElement_Name}

# WebApp_DynamicApplication class attributes and methods

# WebApp_IdElement class attributes and methods
WebApp_IdElement_Id: Property = Property(name="Id", type=StringType)
WebApp_IdElement.attributes={WebApp_IdElement_Id}

# WebApp_Controller class attributes and methods

# WebApp_ActionMapping class attributes and methods

# WebApp_Entities class attributes and methods

# Relationships
action0: BinaryAssociation = BinaryAssociation(
    name="action0",
    ends={
        Property(name="WebApp_Action", type=WebApp_Pages, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_Pages", type=WebApp_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
views1: BinaryAssociation = BinaryAssociation(
    name="views1",
    ends={
        Property(name="WebApp_Views", type=WebApp_Pages, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_Pages2", type=WebApp_Views, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tables3: BinaryAssociation = BinaryAssociation(
    name="tables3",
    ends={
        Property(name="WebApp_Tables", type=WebApp_Views, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_Views4", type=WebApp_Tables, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forms5: BinaryAssociation = BinaryAssociation(
    name="forms5",
    ends={
        Property(name="WebApp_Forms", type=WebApp_Views, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_Views6", type=WebApp_Forms, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
has7: BinaryAssociation = BinaryAssociation(
    name="has7",
    ends={
        Property(name="WebApp_styleElements", type=WebApp_Views, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_Views8", type=WebApp_styleElements, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
formelements9: BinaryAssociation = BinaryAssociation(
    name="formelements9",
    ends={
        Property(name="WebApp_FormElements", type=WebApp_Forms, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_Forms10", type=WebApp_FormElements, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values26: BinaryAssociation = BinaryAssociation(
    name="values26",
    ends={
        Property(name="WebApp_Dummies", type=WebApp_Entities, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_Entities27", type=WebApp_Dummies, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute28: BinaryAssociation = BinaryAssociation(
    name="attribute28",
    ends={
        Property(name="WebApp_Attribute", type=WebApp_Entities, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_Entities29", type=WebApp_Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
contain30: BinaryAssociation = BinaryAssociation(
    name="contain30",
    ends={
        Property(name="WebApp_styleElements32", type=WebApp_Tables, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_Tables31", type=WebApp_styleElements, multiplicity=Multiplicity(0, 9999))
    }
)
pages33: BinaryAssociation = BinaryAssociation(
    name="pages33",
    ends={
        Property(name="WebApp_Pages34", type=WebApp_DynamicApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_DynamicApplication", type=WebApp_Pages, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
entities35: BinaryAssociation = BinaryAssociation(
    name="entities35",
    ends={
        Property(name="WebApp_Entities37", type=WebApp_DynamicApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_DynamicApplication36", type=WebApp_Entities, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
attribute38: BinaryAssociation = BinaryAssociation(
    name="attribute38",
    ends={
        Property(name="WebApp_Attribute40", type=WebApp_Dummies, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_Dummies39", type=WebApp_Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
action11: BinaryAssociation = BinaryAssociation(
    name="action11",
    ends={
        Property(name="WebApp_Action12", type=WebApp_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_Controller", type=WebApp_Action, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
actionmapping13: BinaryAssociation = BinaryAssociation(
    name="actionmapping13",
    ends={
        Property(name="WebApp_ActionMapping", type=WebApp_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_Action14", type=WebApp_ActionMapping, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
entities15: BinaryAssociation = BinaryAssociation(
    name="entities15",
    ends={
        Property(name="WebApp_Entities", type=WebApp_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_Action16", type=WebApp_Entities, multiplicity=Multiplicity(1, 9999))
    }
)
Controller17: BinaryAssociation = BinaryAssociation(
    name="Controller17",
    ends={
        Property(name="WebApp_Controller19", type=WebApp_ActionMapping, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_ActionMapping18", type=WebApp_Controller, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
views20: BinaryAssociation = BinaryAssociation(
    name="views20",
    ends={
        Property(name="WebApp_Views22", type=WebApp_Entities, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_Entities21", type=WebApp_Views, multiplicity=Multiplicity(0, 9999))
    }
)
has24: BinaryAssociation = BinaryAssociation(
    name="has24",
    ends={
        Property(name="WebApp_Entities25", type=WebApp_Entities, multiplicity=Multiplicity(1, 1)),
        Property(name="WebApp_Entities23", type=WebApp_Entities, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_WebApp_Pages_NamedElement = Generalization(general=NamedElement, specific=WebApp_Pages)
gen_WebApp_Views_NamedElement = Generalization(general=NamedElement, specific=WebApp_Views)
gen_WebApp_Views_IdElement = Generalization(general=IdElement, specific=WebApp_Views)
gen_WebApp_Forms_NamedElement = Generalization(general=NamedElement, specific=WebApp_Forms)
gen_WebApp_Forms_IdElement = Generalization(general=IdElement, specific=WebApp_Forms)
gen_WebApp_Tables_NamedElement = Generalization(general=NamedElement, specific=WebApp_Tables)
gen_WebApp_Tables_IdElement = Generalization(general=IdElement, specific=WebApp_Tables)
gen_WebApp_styleElements_NamedElement = Generalization(general=NamedElement, specific=WebApp_styleElements)
gen_WebApp_styleElements_IdElement = Generalization(general=IdElement, specific=WebApp_styleElements)
gen_WebApp_DynamicApplication_NamedElement = Generalization(general=NamedElement, specific=WebApp_DynamicApplication)
gen_WebApp_Dummies_NamedElement = Generalization(general=NamedElement, specific=WebApp_Dummies)
gen_WebApp_FormElements_NamedElement = Generalization(general=NamedElement, specific=WebApp_FormElements)
gen_WebApp_FormElements_IdElement = Generalization(general=IdElement, specific=WebApp_FormElements)
gen_WebApp_Controller_NamedElement = Generalization(general=NamedElement, specific=WebApp_Controller)
gen_WebApp_Action_NamedElement = Generalization(general=NamedElement, specific=WebApp_Action)
gen_WebApp_Entities_NamedElement = Generalization(general=NamedElement, specific=WebApp_Entities)
gen_WebApp_Attribute_NamedElement = Generalization(general=NamedElement, specific=WebApp_Attribute)

# Domain Model
domain_model = DomainModel(
    name="WebApp",
    types={NamedElement, WebApp_Action, WebApp_Views, IdElement, WebApp_Tables, WebApp_Forms, WebApp_styleElements, WebApp_FormElements, WebApp_Pages, WebApp_Dummies, WebApp_Attribute, WebApp_NamedElement, WebApp_DynamicApplication, WebApp_IdElement, WebApp_Controller, WebApp_ActionMapping, WebApp_Entities},
    associations={action0, views1, tables3, forms5, has7, formelements9, values26, attribute28, contain30, pages33, entities35, attribute38, action11, actionmapping13, entities15, Controller17, views20, has24},
    generalizations={gen_WebApp_Pages_NamedElement, gen_WebApp_Views_NamedElement, gen_WebApp_Views_IdElement, gen_WebApp_Forms_NamedElement, gen_WebApp_Forms_IdElement, gen_WebApp_Tables_NamedElement, gen_WebApp_Tables_IdElement, gen_WebApp_styleElements_NamedElement, gen_WebApp_styleElements_IdElement, gen_WebApp_DynamicApplication_NamedElement, gen_WebApp_Dummies_NamedElement, gen_WebApp_FormElements_NamedElement, gen_WebApp_FormElements_IdElement, gen_WebApp_Controller_NamedElement, gen_WebApp_Action_NamedElement, gen_WebApp_Entities_NamedElement, gen_WebApp_Attribute_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)