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
webapp_Collection = Class(name="webapp::Collection")
webapp_Router = Class(name="webapp::Router")
webapp_Model = Class(name="webapp::Model")
webapp_Controller = Class(name="webapp::Controller", is_abstract=True)
webapp_Template = Class(name="webapp::Template")
webapp_View = Class(name="webapp::View")
webapp_Style = Class(name="webapp::Style")
Data = Class(name="Data")
webapp_Attribute = Class(name="webapp::Attribute")
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

# webapp_Collection class attributes and methods

# webapp_Router class attributes and methods

# webapp_Model class attributes and methods

# webapp_Controller class attributes and methods

# webapp_Template class attributes and methods
webapp_Template_structure: Property = Property(name="structure", type=StringType)
webapp_Template.attributes={webapp_Template_structure}

# webapp_View class attributes and methods

# webapp_Style class attributes and methods
webapp_Style_src: Property = Property(name="src", type=StringType)
webapp_Style_href: Property = Property(name="href", type=StringType)
webapp_Style.attributes={webapp_Style_src, webapp_Style_href}

# Data class attributes and methods

# webapp_Attribute class attributes and methods
webapp_Attribute_baseType: Property = Property(name="baseType", type=StringType)
webapp_Attribute_customType: Property = Property(name="customType", type=StringType)
webapp_Attribute.attributes={webapp_Attribute_baseType, webapp_Attribute_customType}

# webapp_Data class attributes and methods
webapp_Data_endpoint: Property = Property(name="endpoint", type=StringType)
webapp_Data.attributes={webapp_Data_endpoint}

# webapp_RouterBinding class attributes and methods
webapp_RouterBinding_requestURL: Property = Property(name="requestURL", type=StringType)
webapp_RouterBinding_requestCookies: Property = Property(name="requestCookies", type=StringType)
webapp_RouterBinding.attributes={webapp_RouterBinding_requestURL, webapp_RouterBinding_requestCookies}

# webapp_PageController class attributes and methods

# Controller class attributes and methods

# webapp_ServiceController class attributes and methods
webapp_ServiceController_endpoint: Property = Property(name="endpoint", type=StringType)
webapp_ServiceController.attributes={webapp_ServiceController_endpoint}

# Relationships
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
views9: BinaryAssociation = BinaryAssociation(
    name="views9",
    ends={
        Property(name="webapp_View", type=webapp_WebApp, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_WebApp10", type=webapp_View, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
styles11: BinaryAssociation = BinaryAssociation(
    name="styles11",
    ends={
        Property(name="webapp_Style", type=webapp_WebApp, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_WebApp12", type=webapp_Style, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes13: BinaryAssociation = BinaryAssociation(
    name="attributes13",
    ends={
        Property(name="webapp_Attribute", type=webapp_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Model14", type=webapp_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model15: BinaryAssociation = BinaryAssociation(
    name="model15",
    ends={
        Property(name="webapp_Model17", type=webapp_Collection, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Collection16", type=webapp_Model, multiplicity=Multiplicity(0, 1))
    }
)
subviews19: BinaryAssociation = BinaryAssociation(
    name="subviews19",
    ends={
        Property(name="webapp_View20", type=webapp_View, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_View18", type=webapp_View, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
data24: BinaryAssociation = BinaryAssociation(
    name="data24",
    ends={
        Property(name="webapp_Attribute26", type=webapp_View, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_View25", type=webapp_Attribute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bindings27: BinaryAssociation = BinaryAssociation(
    name="bindings27",
    ends={
        Property(name="webapp_RouterBinding", type=webapp_Router, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Router28", type=webapp_RouterBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
style29: BinaryAssociation = BinaryAssociation(
    name="style29",
    ends={
        Property(name="webapp_Style31", type=webapp_Template, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Template30", type=webapp_Style, multiplicity=Multiplicity(0, 1))
    }
)
controller32: BinaryAssociation = BinaryAssociation(
    name="controller32",
    ends={
        Property(name="webapp_Controller34", type=webapp_RouterBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_RouterBinding33", type=webapp_Controller, multiplicity=Multiplicity(1, 1))
    }
)
parameters35: BinaryAssociation = BinaryAssociation(
    name="parameters35",
    ends={
        Property(name="webapp_Attribute37", type=webapp_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_Controller36", type=webapp_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
template21: BinaryAssociation = BinaryAssociation(
    name="template21",
    ends={
        Property(name="webapp_Template23", type=webapp_View, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_View22", type=webapp_Template, multiplicity=Multiplicity(0, 1))
    }
)
page38: BinaryAssociation = BinaryAssociation(
    name="page38",
    ends={
        Property(name="webapp_View39", type=webapp_PageController, multiplicity=Multiplicity(1, 1)),
        Property(name="webapp_PageController", type=webapp_View, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_webapp_WebApp_NamedElement = Generalization(general=NamedElement, specific=webapp_WebApp)
gen_webapp_Model_Data = Generalization(general=Data, specific=webapp_Model)
gen_webapp_Collection_Data = Generalization(general=Data, specific=webapp_Collection)
gen_webapp_Data_NamedElement = Generalization(general=NamedElement, specific=webapp_Data)
gen_webapp_View_NamedElement = Generalization(general=NamedElement, specific=webapp_View)
gen_webapp_Template_NamedElement = Generalization(general=NamedElement, specific=webapp_Template)
gen_webapp_Controller_NamedElement = Generalization(general=NamedElement, specific=webapp_Controller)
gen_webapp_PageController_Controller = Generalization(general=Controller, specific=webapp_PageController)
gen_webapp_Style_NamedElement = Generalization(general=NamedElement, specific=webapp_Style)
gen_webapp_Attribute_NamedElement = Generalization(general=NamedElement, specific=webapp_Attribute)
gen_webapp_ServiceController_Controller = Generalization(general=Controller, specific=webapp_ServiceController)

# Domain Model
domain_model = DomainModel(
    name="webapp",
    types={webapp_NamedElement, webapp_WebApp, NamedElement, webapp_Collection, webapp_Router, webapp_Model, webapp_Controller, webapp_Template, webapp_View, webapp_Style, Data, webapp_Attribute, webapp_Data, webapp_RouterBinding, webapp_PageController, Controller, webapp_ServiceController, DataType},
    associations={collections0, router1, models3, controllers5, templates7, views9, styles11, attributes13, model15, subviews19, data24, bindings27, style29, controller32, parameters35, template21, page38},
    generalizations={gen_webapp_WebApp_NamedElement, gen_webapp_Model_Data, gen_webapp_Collection_Data, gen_webapp_Data_NamedElement, gen_webapp_View_NamedElement, gen_webapp_Template_NamedElement, gen_webapp_Controller_NamedElement, gen_webapp_PageController_Controller, gen_webapp_Style_NamedElement, gen_webapp_Attribute_NamedElement, gen_webapp_ServiceController_Controller},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)