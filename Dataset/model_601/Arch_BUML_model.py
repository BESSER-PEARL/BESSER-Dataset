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
Arch_Application = Class(name="Arch::Application")
Arch_FrontEnd = Class(name="Arch::FrontEnd")
Arch_BackEnd = Class(name="Arch::BackEnd")
Arch_Service = Class(name="Arch::Service")
Arch_Logic = Class(name="Arch::Logic")
Arch_Entity = Class(name="Arch::Entity")
Arch_GraphicControl = Class(name="Arch::GraphicControl", is_abstract=True)
Arch_View = Class(name="Arch::View")
Arch_Controller = Class(name="Arch::Controller")
Arch_Method = Class(name="Arch::Method")
Arch_Attribute = Class(name="Arch::Attribute")
Arch_Event = Class(name="Arch::Event")
Arch_Parameter = Class(name="Arch::Parameter")
Arch_Label = Class(name="Arch::Label")
GraphicControl = Class(name="GraphicControl")
Arch_TextBox = Class(name="Arch::TextBox")
Arch_Div = Class(name="Arch::Div")
Arch_DropDownList = Class(name="Arch::DropDownList")

# Arch_Application class attributes and methods
Arch_Application_name: Property = Property(name="name", type=StringType)
Arch_Application.attributes={Arch_Application_name}

# Arch_FrontEnd class attributes and methods
Arch_FrontEnd_name: Property = Property(name="name", type=StringType)
Arch_FrontEnd.attributes={Arch_FrontEnd_name}

# Arch_BackEnd class attributes and methods
Arch_BackEnd_name: Property = Property(name="name", type=StringType)
Arch_BackEnd.attributes={Arch_BackEnd_name}

# Arch_Service class attributes and methods
Arch_Service_name: Property = Property(name="name", type=StringType)
Arch_Service.attributes={Arch_Service_name}

# Arch_Logic class attributes and methods
Arch_Logic_name: Property = Property(name="name", type=StringType)
Arch_Logic.attributes={Arch_Logic_name}

# Arch_Entity class attributes and methods
Arch_Entity_name: Property = Property(name="name", type=StringType)
Arch_Entity.attributes={Arch_Entity_name}

# Arch_GraphicControl class attributes and methods
Arch_GraphicControl_name: Property = Property(name="name", type=StringType)
Arch_GraphicControl.attributes={Arch_GraphicControl_name}

# Arch_View class attributes and methods
Arch_View_name: Property = Property(name="name", type=StringType)
Arch_View.attributes={Arch_View_name}

# Arch_Controller class attributes and methods
Arch_Controller_name: Property = Property(name="name", type=StringType)
Arch_Controller.attributes={Arch_Controller_name}

# Arch_Method class attributes and methods
Arch_Method_returntype: Property = Property(name="returntype", type=StringType)
Arch_Method_name: Property = Property(name="name", type=StringType)
Arch_Method.attributes={Arch_Method_name, Arch_Method_returntype}

# Arch_Attribute class attributes and methods
Arch_Attribute_name: Property = Property(name="name", type=StringType)
Arch_Attribute_type: Property = Property(name="type", type=StringType)
Arch_Attribute.attributes={Arch_Attribute_name, Arch_Attribute_type}

# Arch_Event class attributes and methods
Arch_Event_name: Property = Property(name="name", type=StringType)
Arch_Event.attributes={Arch_Event_name}

# Arch_Parameter class attributes and methods
Arch_Parameter_name: Property = Property(name="name", type=StringType)
Arch_Parameter_type: Property = Property(name="type", type=StringType)
Arch_Parameter.attributes={Arch_Parameter_name, Arch_Parameter_type}

# Arch_Label class attributes and methods
Arch_Label_text: Property = Property(name="text", type=StringType)
Arch_Label.attributes={Arch_Label_text}

# GraphicControl class attributes and methods

# Arch_TextBox class attributes and methods
Arch_TextBox_type: Property = Property(name="type", type=StringType)
Arch_TextBox.attributes={Arch_TextBox_type}

# Arch_Div class attributes and methods

# Arch_DropDownList class attributes and methods
Arch_DropDownList_items: Property = Property(name="items", type=StringType)
Arch_DropDownList.attributes={Arch_DropDownList_items}

# Relationships
frontend0: BinaryAssociation = BinaryAssociation(
    name="frontend0",
    ends={
        Property(name="Arch_FrontEnd", type=Arch_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="Arch_Application", type=Arch_FrontEnd, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
backend1: BinaryAssociation = BinaryAssociation(
    name="backend1",
    ends={
        Property(name="Arch_BackEnd", type=Arch_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="Arch_Application2", type=Arch_BackEnd, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
services7: BinaryAssociation = BinaryAssociation(
    name="services7",
    ends={
        Property(name="Arch_Service", type=Arch_BackEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="Arch_BackEnd8", type=Arch_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logics9: BinaryAssociation = BinaryAssociation(
    name="logics9",
    ends={
        Property(name="Arch_Logic", type=Arch_BackEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="Arch_BackEnd10", type=Arch_Logic, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entities11: BinaryAssociation = BinaryAssociation(
    name="entities11",
    ends={
        Property(name="Arch_Entity", type=Arch_BackEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="Arch_BackEnd12", type=Arch_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graphicControls13: BinaryAssociation = BinaryAssociation(
    name="graphicControls13",
    ends={
        Property(name="Arch_GraphicControl", type=Arch_View, multiplicity=Multiplicity(1, 1)),
        Property(name="Arch_View14", type=Arch_GraphicControl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
views3: BinaryAssociation = BinaryAssociation(
    name="views3",
    ends={
        Property(name="Arch_View", type=Arch_FrontEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="Arch_FrontEnd4", type=Arch_View, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controllers5: BinaryAssociation = BinaryAssociation(
    name="controllers5",
    ends={
        Property(name="Arch_Controller", type=Arch_FrontEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="Arch_FrontEnd6", type=Arch_Controller, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods23: BinaryAssociation = BinaryAssociation(
    name="methods23",
    ends={
        Property(name="Arch_Method", type=Arch_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="Arch_Service24", type=Arch_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods25: BinaryAssociation = BinaryAssociation(
    name="methods25",
    ends={
        Property(name="Arch_Method27", type=Arch_Logic, multiplicity=Multiplicity(1, 1)),
        Property(name="Arch_Logic26", type=Arch_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controllers15: BinaryAssociation = BinaryAssociation(
    name="controllers15",
    ends={
        Property(name="Arch_Controller17", type=Arch_View, multiplicity=Multiplicity(1, 1)),
        Property(name="Arch_View16", type=Arch_Controller, multiplicity=Multiplicity(0, 9999))
    }
)
views18: BinaryAssociation = BinaryAssociation(
    name="views18",
    ends={
        Property(name="Arch_View20", type=Arch_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="Arch_Controller19", type=Arch_View, multiplicity=Multiplicity(0, 9999))
    }
)
events21: BinaryAssociation = BinaryAssociation(
    name="events21",
    ends={
        Property(name="Arch_Event", type=Arch_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="Arch_Controller22", type=Arch_Event, multiplicity=Multiplicity(0, 9999))
    }
)
parameters33: BinaryAssociation = BinaryAssociation(
    name="parameters33",
    ends={
        Property(name="Arch_Parameter", type=Arch_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="Arch_Method34", type=Arch_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events35: BinaryAssociation = BinaryAssociation(
    name="events35",
    ends={
        Property(name="Arch_Event37", type=Arch_GraphicControl, multiplicity=Multiplicity(1, 1)),
        Property(name="Arch_GraphicControl36", type=Arch_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes28: BinaryAssociation = BinaryAssociation(
    name="attributes28",
    ends={
        Property(name="Arch_Attribute", type=Arch_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="Arch_Entity29", type=Arch_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods30: BinaryAssociation = BinaryAssociation(
    name="methods30",
    ends={
        Property(name="Arch_Method32", type=Arch_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="Arch_Entity31", type=Arch_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graphicControls38: BinaryAssociation = BinaryAssociation(
    name="graphicControls38",
    ends={
        Property(name="Arch_GraphicControl39", type=Arch_Div, multiplicity=Multiplicity(1, 1)),
        Property(name="Arch_Div", type=Arch_GraphicControl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Arch_Label_GraphicControl = Generalization(general=GraphicControl, specific=Arch_Label)
gen_Arch_TextBox_GraphicControl = Generalization(general=GraphicControl, specific=Arch_TextBox)
gen_Arch_Div_GraphicControl = Generalization(general=GraphicControl, specific=Arch_Div)
gen_Arch_DropDownList_GraphicControl = Generalization(general=GraphicControl, specific=Arch_DropDownList)

# Domain Model
domain_model = DomainModel(
    name="Arch",
    types={Arch_Application, Arch_FrontEnd, Arch_BackEnd, Arch_Service, Arch_Logic, Arch_Entity, Arch_GraphicControl, Arch_View, Arch_Controller, Arch_Method, Arch_Attribute, Arch_Event, Arch_Parameter, Arch_Label, GraphicControl, Arch_TextBox, Arch_Div, Arch_DropDownList},
    associations={frontend0, backend1, services7, logics9, entities11, graphicControls13, views3, controllers5, methods23, methods25, controllers15, views18, events21, parameters33, events35, attributes28, methods30, graphicControls38},
    generalizations={gen_Arch_Label_GraphicControl, gen_Arch_TextBox_GraphicControl, gen_Arch_Div_GraphicControl, gen_Arch_DropDownList_GraphicControl},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)