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
            EnumerationLiteral(name="string"),
			EnumerationLiteral(name="number"),
			EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="array"),
			EnumerationLiteral(name="object"),
			EnumerationLiteral(name="date"),
			EnumerationLiteral(name="any")
    }
)

# Classes
webapp_NamedElement = Class(name="webapp::NamedElement")
webapp_WebApp = Class(name="webapp::WebApp")
NamedElement = Class(name="NamedElement")
webapp_View = Class(name="webapp::View")
Data = Class(name="Data")
webapp_Attribute = Class(name="webapp::Attribute")
webapp_Collection = Class(name="webapp::Collection")
webapp_Router = Class(name="webapp::Router")
webapp_Model = Class(name="webapp::Model")
webapp_Controller = Class(name="webapp::Controller", is_abstract=True)
webapp_Template = Class(name="webapp::Template")
webapp_Data = Class(name="webapp::Data")
webapp_RouterBinding = Class(name="webapp::RouterBinding")
webapp_PageController = Class(name="webapp::PageController")
Controller = Class(name="Controller")
webapp_ServiceController = Class(name="webapp::ServiceController")

# webapp_NamedElement class attributes and methods
webapp_NamedElement_name: Property = Property(name="name", type=StringType)
webapp_NamedElement.attributes={webapp_NamedElement_name}

# webapp_WebApp class attributes and methods

# NamedElement class attributes and methods

# webapp_View class attributes and methods

# Data class attributes and methods

# webapp_Attribute class attributes and methods
webapp_Attribute_baseType: Property = Property(name="baseType", type=StringType)
webapp_Attribute_customType: Property = Property(name="customType", type=StringType)
webapp_Attribute.attributes={webapp_Attribute_customType, webapp_Attribute_baseType}

# webapp_Collection class attributes and methods

# webapp_Router class attributes and methods

# webapp_Model class attributes and methods

# webapp_Controller class attributes and methods

# webapp_Template class attributes and methods
webapp_Template_structure: Property = Property(name="structure", type=StringType)
webapp_Template_style: Property = Property(name="style", type=StringType)
webapp_Template.attributes={webapp_Template_style, webapp_Template_structure}

# webapp_Data class attributes and methods
webapp_Data_endpoint: Property = Property(name="endpoint", type=StringType)
webapp_Data.attributes={webapp_Data_endpoint}

# webapp_RouterBinding class attributes and methods
webapp_RouterBinding_url: Property = Property(name="url", type=StringType)
webapp_RouterBinding.attributes={webapp_RouterBinding_url}

# webapp_PageController class attributes and methods

# Controller class attributes and methods

# webapp_ServiceController class attributes and methods
webapp_ServiceController_endpoint: Property = Property(name="endpoint", type=StringType)
webapp_ServiceController.attributes={webapp_ServiceController_endpoint}

# Relationships
views9: BinaryAssociation = BinaryAssociation(
    name="views9",
    ends={
        Property(name="webapp_View", type=webapp_WebApp, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_WebApp10", type=webapp_View, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes11: BinaryAssociation = BinaryAssociation(
    name="attributes11",
    ends={
        Property(name="webapp_Attribute", type=webapp_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Model12", type=webapp_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collections0: BinaryAssociation = BinaryAssociation(
    name="collections0",
    ends={
        Property(name="webapp_Collection", type=webapp_WebApp, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_WebApp", type=webapp_Collection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
router1: BinaryAssociation = BinaryAssociation(
    name="router1",
    ends={
        Property(name="webapp_Router", type=webapp_WebApp, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_WebApp2", type=webapp_Router, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
models3: BinaryAssociation = BinaryAssociation(
    name="models3",
    ends={
        Property(name="webapp_Model", type=webapp_WebApp, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_WebApp4", type=webapp_Model, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controllers5: BinaryAssociation = BinaryAssociation(
    name="controllers5",
    ends={
        Property(name="webapp_Controller", type=webapp_WebApp, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_WebApp6", type=webapp_Controller, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
templates7: BinaryAssociation = BinaryAssociation(
    name="templates7",
    ends={
        Property(name="webapp_Template", type=webapp_WebApp, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_WebApp8", type=webapp_Template, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings24: BinaryAssociation = BinaryAssociation(
    name="bindings24",
    ends={
        Property(name="webapp_Router25", type=webapp_RouterBinding, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="webapp_RouterBinding", type=webapp_Router, multiplicity=Multiplicity(1, 1))
    }
)
controller26: BinaryAssociation = BinaryAssociation(
    name="controller26",
    ends={
        Property(name="webapp_Controller28", type=webapp_RouterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_RouterBinding27", type=webapp_Controller, multiplicity=Multiplicity(1, 1))
    }
)
model13: BinaryAssociation = BinaryAssociation(
    name="model13",
    ends={
        Property(name="webapp_Model15", type=webapp_Collection, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Collection14", type=webapp_Model, multiplicity=Multiplicity(0, 1))
    }
)
subviews17: BinaryAssociation = BinaryAssociation(
    name="subviews17",
    ends={
        Property(name="webapp_View18", type=webapp_View, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_View16", type=webapp_View, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
template19: BinaryAssociation = BinaryAssociation(
    name="template19",
    ends={
        Property(name="webapp_Template21", type=webapp_View, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_View20", type=webapp_Template, multiplicity=Multiplicity(0, 1))
    }
)
data22: BinaryAssociation = BinaryAssociation(
    name="data22",
    ends={
        Property(name="webapp_Data", type=webapp_View, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_View23", type=webapp_Data, multiplicity=Multiplicity(0, 1))
    }
)
parameters29: BinaryAssociation = BinaryAssociation(
    name="parameters29",
    ends={
        Property(name="webapp_Attribute31", type=webapp_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Controller30", type=webapp_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
page32: BinaryAssociation = BinaryAssociation(
    name="page32",
    ends={
        Property(name="webapp_View33", type=webapp_PageController, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_PageController", type=webapp_View, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_webapp_WebApp_NamedElement = Generalization(general=NamedElement, specific=webapp_WebApp)
gen_webapp_Model_Data = Generalization(general=Data, specific=webapp_Model)
gen_webapp_Collection_Data = Generalization(general=Data, specific=webapp_Collection)
gen_webapp_Template_NamedElement = Generalization(general=NamedElement, specific=webapp_Template)
gen_webapp_Data_NamedElement = Generalization(general=NamedElement, specific=webapp_Data)
gen_webapp_View_NamedElement = Generalization(general=NamedElement, specific=webapp_View)
gen_webapp_Controller_NamedElement = Generalization(general=NamedElement, specific=webapp_Controller)
gen_webapp_PageController_Controller = Generalization(general=Controller, specific=webapp_PageController)
gen_webapp_ServiceController_Controller = Generalization(general=Controller, specific=webapp_ServiceController)
gen_webapp_Attribute_NamedElement = Generalization(general=NamedElement, specific=webapp_Attribute)

# Domain Model
domain_model = DomainModel(
    name="webapp",
    types={webapp_NamedElement, webapp_WebApp, NamedElement, webapp_View, Data, webapp_Attribute, webapp_Collection, webapp_Router, webapp_Model, webapp_Controller, webapp_Template, webapp_Data, webapp_RouterBinding, webapp_PageController, Controller, webapp_ServiceController, DataType},
    associations={views9, attributes11, collections0, router1, models3, controllers5, templates7, bindings24, controller26, model13, subviews17, template19, data22, parameters29, page32},
    generalizations={gen_webapp_WebApp_NamedElement, gen_webapp_Model_Data, gen_webapp_Collection_Data, gen_webapp_Template_NamedElement, gen_webapp_Data_NamedElement, gen_webapp_View_NamedElement, gen_webapp_Controller_NamedElement, gen_webapp_PageController_Controller, gen_webapp_ServiceController_Controller, gen_webapp_Attribute_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)