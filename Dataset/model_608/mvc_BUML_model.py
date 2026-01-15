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
mvc_MvcApplication = Class(name="mvc::MvcApplication")
mvc_View = Class(name="mvc::View")
mvc_Model = Class(name="mvc::Model")
mvc_Controller = Class(name="mvc::Controller")
mvc_Position = Class(name="mvc::Position")
mvc_Attribute = Class(name="mvc::Attribute")
mvc_Method = Class(name="mvc::Method")
mvc_Client = Class(name="mvc::Client")
Model = Class(name="Model")
mvc_DataBase = Class(name="mvc::DataBase")
mvc_GraphicComponent = Class(name="mvc::GraphicComponent")
View = Class(name="View")
mvc_MapComponent = Class(name="mvc::MapComponent")
mvc_ReturnParameter = Class(name="mvc::ReturnParameter")
mvc_SocialComponent = Class(name="mvc::SocialComponent")

# mvc_MvcApplication class attributes and methods
mvc_MvcApplication_name: Property = Property(name="name", type=StringType)
mvc_MvcApplication_picture: Property = Property(name="picture", type=StringType)
mvc_MvcApplication_description: Property = Property(name="description", type=StringType)
mvc_MvcApplication_email: Property = Property(name="email", type=StringType)
mvc_MvcApplication_pagelink: Property = Property(name="pagelink", type=StringType)
mvc_MvcApplication.attributes={mvc_MvcApplication_pagelink, mvc_MvcApplication_email, mvc_MvcApplication_name, mvc_MvcApplication_description, mvc_MvcApplication_picture}

# mvc_View class attributes and methods
mvc_View_name: Property = Property(name="name", type=StringType)
mvc_View_type: Property = Property(name="type", type=StringType)
mvc_View.attributes={mvc_View_type, mvc_View_name}

# mvc_Model class attributes and methods
mvc_Model_nameclass: Property = Property(name="nameclass", type=StringType)
mvc_Model_type: Property = Property(name="type", type=StringType)
mvc_Model.attributes={mvc_Model_nameclass, mvc_Model_type}

# mvc_Controller class attributes and methods
mvc_Controller_name: Property = Property(name="name", type=StringType)
mvc_Controller.attributes={mvc_Controller_name}

# mvc_Position class attributes and methods
mvc_Position_above: Property = Property(name="above", type=IntegerType)
mvc_Position_align_left: Property = Property(name="align_left", type=IntegerType)
mvc_Position_wide: Property = Property(name="wide", type=IntegerType)
mvc_Position_long: Property = Property(name="long", type=IntegerType)
mvc_Position_name: Property = Property(name="name", type=StringType)
mvc_Position.attributes={mvc_Position_long, mvc_Position_name, mvc_Position_align_left, mvc_Position_above, mvc_Position_wide}

# mvc_Attribute class attributes and methods
mvc_Attribute_nameattribute: Property = Property(name="nameattribute", type=StringType)
mvc_Attribute_typeattribute: Property = Property(name="typeattribute", type=StringType)
mvc_Attribute.attributes={mvc_Attribute_nameattribute, mvc_Attribute_typeattribute}

# mvc_Method class attributes and methods
mvc_Method_type: Property = Property(name="type", type=StringType)
mvc_Method_namemethod: Property = Property(name="namemethod", type=StringType)
mvc_Method.attributes={mvc_Method_namemethod, mvc_Method_type}

# mvc_Client class attributes and methods
mvc_Client_nameservice: Property = Property(name="nameservice", type=StringType)
mvc_Client.attributes={mvc_Client_nameservice}

# Model class attributes and methods

# mvc_DataBase class attributes and methods

# mvc_GraphicComponent class attributes and methods
mvc_GraphicComponent_stepSize: Property = Property(name="stepSize", type=IntegerType)
mvc_GraphicComponent.attributes={mvc_GraphicComponent_stepSize}

# View class attributes and methods

# mvc_MapComponent class attributes and methods
mvc_MapComponent_marker: Property = Property(name="marker", type=BooleanType)
mvc_MapComponent_latitude: Property = Property(name="latitude", type=FloatType)
mvc_MapComponent_longitude: Property = Property(name="longitude", type=FloatType)
mvc_MapComponent.attributes={mvc_MapComponent_latitude, mvc_MapComponent_marker, mvc_MapComponent_longitude}

# mvc_ReturnParameter class attributes and methods

# mvc_SocialComponent class attributes and methods
mvc_SocialComponent_social: Property = Property(name="social", type=StringType)
mvc_SocialComponent_socialname: Property = Property(name="socialname", type=StringType)
mvc_SocialComponent.attributes={mvc_SocialComponent_socialname, mvc_SocialComponent_social}

# Relationships
views0: BinaryAssociation = BinaryAssociation(
    name="views0",
    ends={
        Property(name="mvc_View", type=mvc_MvcApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_MvcApplication", type=mvc_View, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
models1: BinaryAssociation = BinaryAssociation(
    name="models1",
    ends={
        Property(name="mvc_Model", type=mvc_MvcApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_MvcApplication2", type=mvc_Model, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
controllers3: BinaryAssociation = BinaryAssociation(
    name="controllers3",
    ends={
        Property(name="mvc_Controller", type=mvc_MvcApplication, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_MvcApplication4", type=mvc_Controller, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
model5: BinaryAssociation = BinaryAssociation(
    name="model5",
    ends={
        Property(name="Model", type=mvc_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="controller", type=mvc_Model, multiplicity=Multiplicity(1, 1))
    }
)
controller8: BinaryAssociation = BinaryAssociation(
    name="controller8",
    ends={
        Property(name="Controller", type=mvc_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="model", type=mvc_Controller, multiplicity=Multiplicity(1, 1))
    }
)
controller9: BinaryAssociation = BinaryAssociation(
    name="controller9",
    ends={
        Property(name="Controller10", type=mvc_View, multiplicity=Multiplicity(1, 1)),
        Property(name="view", type=mvc_Controller, multiplicity=Multiplicity(1, 1))
    }
)
position11: BinaryAssociation = BinaryAssociation(
    name="position11",
    ends={
        Property(name="mvc_Position", type=mvc_View, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_View12", type=mvc_Position, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attrib13: BinaryAssociation = BinaryAssociation(
    name="attrib13",
    ends={
        Property(name="mvc_Attribute", type=mvc_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_Method", type=mvc_Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
method14: BinaryAssociation = BinaryAssociation(
    name="method14",
    ends={
        Property(name="mvc_Method15", type=mvc_Client, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_Client", type=mvc_Method, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attribute16: BinaryAssociation = BinaryAssociation(
    name="attribute16",
    ends={
        Property(name="mvc_Attribute17", type=mvc_DataBase, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_DataBase", type=mvc_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
datoA18: BinaryAssociation = BinaryAssociation(
    name="datoA18",
    ends={
        Property(name="mvc_Attribute19", type=mvc_GraphicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_GraphicComponent", type=mvc_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
datoB20: BinaryAssociation = BinaryAssociation(
    name="datoB20",
    ends={
        Property(name="mvc_Attribute22", type=mvc_GraphicComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_GraphicComponent21", type=mvc_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
view6: BinaryAssociation = BinaryAssociation(
    name="view6",
    ends={
        Property(name="View", type=mvc_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="controller7", type=mvc_View, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_mvc_Client_Model = Generalization(general=Model, specific=mvc_Client)
gen_mvc_DataBase_Model = Generalization(general=Model, specific=mvc_DataBase)
gen_mvc_GraphicComponent_View = Generalization(general=View, specific=mvc_GraphicComponent)
gen_mvc_MapComponent_View = Generalization(general=View, specific=mvc_MapComponent)
gen_mvc_SocialComponent_View = Generalization(general=View, specific=mvc_SocialComponent)

# Domain Model
domain_model = DomainModel(
    name="mvc",
    types={mvc_MvcApplication, mvc_View, mvc_Model, mvc_Controller, mvc_Position, mvc_Attribute, mvc_Method, mvc_Client, Model, mvc_DataBase, mvc_GraphicComponent, View, mvc_MapComponent, mvc_ReturnParameter, mvc_SocialComponent},
    associations={views0, models1, controllers3, model5, controller8, controller9, position11, attrib13, method14, attribute16, datoA18, datoB20, view6},
    generalizations={gen_mvc_Client_Model, gen_mvc_DataBase_Model, gen_mvc_GraphicComponent_View, gen_mvc_MapComponent_View, gen_mvc_SocialComponent_View},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)