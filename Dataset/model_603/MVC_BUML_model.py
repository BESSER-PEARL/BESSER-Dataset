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
AssociationType: Enumeration = Enumeration(
    name="AssociationType",
    literals={
            
    }
)

# Classes
mvc_Entity = Class(name="mvc::Entity")
mvc_Association = Class(name="mvc::Association")
mvc_Attribute = Class(name="mvc::Attribute")
mvc_Model = Class(name="mvc::Model")
Annotable = Class(name="Annotable")
mvc_MVCModel = Class(name="mvc::MVCModel")
mvc_Event = Class(name="mvc::Event")
mvc_Controller = Class(name="mvc::Controller")
mvc_Component = Class(name="mvc::Component")
mvc_Action = Class(name="mvc::Action")
mvc_View = Class(name="mvc::View")
mvc_UILayout = Class(name="mvc::UILayout")
mvc_UIComponent = Class(name="mvc::UIComponent", is_abstract=True)
UIComponent = Class(name="UIComponent")
mvc_ControllerView = Class(name="mvc::ControllerView")
mvc_EventAction = Class(name="mvc::EventAction")
mvc_UIInput = Class(name="mvc::UIInput")
mvc_UIActions = Class(name="mvc::UIActions")

# mvc_Entity class attributes and methods
mvc_Entity_name: Property = Property(name="name", type=StringType)
mvc_Entity.attributes={mvc_Entity_name}

# mvc_Association class attributes and methods
mvc_Association_name: Property = Property(name="name", type=StringType)
mvc_Association_containment: Property = Property(name="containment", type=BooleanType)
mvc_Association_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
mvc_Association_upperBound: Property = Property(name="upperBound", type=IntegerType)
mvc_Association_type: Property = Property(name="type", type=StringType)
mvc_Association.attributes={mvc_Association_containment, mvc_Association_lowerBound, mvc_Association_type, mvc_Association_upperBound, mvc_Association_name}

# mvc_Attribute class attributes and methods
mvc_Attribute_name: Property = Property(name="name", type=StringType)
mvc_Attribute_type: Property = Property(name="type", type=StringType)
mvc_Attribute.attributes={mvc_Attribute_name, mvc_Attribute_type}

# mvc_Model class attributes and methods
mvc_Model_name: Property = Property(name="name", type=StringType)
mvc_Model.attributes={mvc_Model_name}

# Annotable class attributes and methods

# mvc_MVCModel class attributes and methods
mvc_MVCModel_name: Property = Property(name="name", type=StringType)
mvc_MVCModel_version: Property = Property(name="version", type=StringType)
mvc_MVCModel.attributes={mvc_MVCModel_version, mvc_MVCModel_name}

# mvc_Event class attributes and methods
mvc_Event_name: Property = Property(name="name", type=StringType)
mvc_Event.attributes={mvc_Event_name}

# mvc_Controller class attributes and methods
mvc_Controller_name: Property = Property(name="name", type=StringType)
mvc_Controller.attributes={mvc_Controller_name}

# mvc_Component class attributes and methods
mvc_Component_name: Property = Property(name="name", type=StringType)
mvc_Component.attributes={mvc_Component_name}

# mvc_Action class attributes and methods
mvc_Action_name: Property = Property(name="name", type=StringType)
mvc_Action.attributes={mvc_Action_name}

# mvc_View class attributes and methods
mvc_View_name: Property = Property(name="name", type=StringType)
mvc_View.attributes={mvc_View_name}

# mvc_UILayout class attributes and methods
mvc_UILayout_orientation: Property = Property(name="orientation", type=StringType)
mvc_UILayout_columns: Property = Property(name="columns", type=IntegerType)
mvc_UILayout.attributes={mvc_UILayout_orientation, mvc_UILayout_columns}

# mvc_UIComponent class attributes and methods
mvc_UIComponent_name: Property = Property(name="name", type=StringType)
mvc_UIComponent_type: Property = Property(name="type", type=StringType)
mvc_UIComponent.attributes={mvc_UIComponent_type, mvc_UIComponent_name}

# UIComponent class attributes and methods

# mvc_ControllerView class attributes and methods

# mvc_EventAction class attributes and methods

# mvc_UIInput class attributes and methods

# mvc_UIActions class attributes and methods

# Relationships
rootEntity0: BinaryAssociation = BinaryAssociation(
    name="rootEntity0",
    ends={
        Property(name="mvc_Entity", type=mvc_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_Model", type=mvc_Entity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
associations1: BinaryAssociation = BinaryAssociation(
    name="associations1",
    ends={
        Property(name="mvc_Association", type=mvc_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_Model2", type=mvc_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes3: BinaryAssociation = BinaryAssociation(
    name="attributes3",
    ends={
        Property(name="mvc_Attribute", type=mvc_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_Entity4", type=mvc_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends6: BinaryAssociation = BinaryAssociation(
    name="extends6",
    ends={
        Property(name="mvc_Entity7", type=mvc_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_Entity5", type=mvc_Entity, multiplicity=Multiplicity(0, 9999))
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="mvc_Entity10", type=mvc_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_Association9", type=mvc_Entity, multiplicity=Multiplicity(1, 1))
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="mvc_Entity13", type=mvc_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_Association12", type=mvc_Entity, multiplicity=Multiplicity(1, 1))
    }
)
models15: BinaryAssociation = BinaryAssociation(
    name="models15",
    ends={
        Property(name="mvc_Model16", type=mvc_MVCModel, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_MVCModel", type=mvc_Model, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
views17: BinaryAssociation = BinaryAssociation(
    name="views17",
    ends={
        Property(name="mvc_View19", type=mvc_MVCModel, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_MVCModel18", type=mvc_View, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events20: BinaryAssociation = BinaryAssociation(
    name="events20",
    ends={
        Property(name="mvc_Event", type=mvc_MVCModel, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_MVCModel21", type=mvc_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controllers22: BinaryAssociation = BinaryAssociation(
    name="controllers22",
    ends={
        Property(name="mvc_Controller", type=mvc_MVCModel, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_MVCModel23", type=mvc_Controller, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components24: BinaryAssociation = BinaryAssociation(
    name="components24",
    ends={
        Property(name="mvc_Component", type=mvc_MVCModel, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_MVCModel25", type=mvc_Component, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
actions26: BinaryAssociation = BinaryAssociation(
    name="actions26",
    ends={
        Property(name="mvc_Action", type=mvc_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_Controller27", type=mvc_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rootComponent14: BinaryAssociation = BinaryAssociation(
    name="rootComponent14",
    ends={
        Property(name="mvc_UILayout", type=mvc_View, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_View", type=mvc_UILayout, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
preExecutionEvent32: BinaryAssociation = BinaryAssociation(
    name="preExecutionEvent32",
    ends={
        Property(name="mvc_Event34", type=mvc_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_Action33", type=mvc_Event, multiplicity=Multiplicity(0, 1))
    }
)
postExecutionEvent35: BinaryAssociation = BinaryAssociation(
    name="postExecutionEvent35",
    ends={
        Property(name="mvc_Event37", type=mvc_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_Action36", type=mvc_Event, multiplicity=Multiplicity(0, 1))
    }
)
triggerEvents38: BinaryAssociation = BinaryAssociation(
    name="triggerEvents38",
    ends={
        Property(name="mvc_Event40", type=mvc_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_Action39", type=mvc_Event, multiplicity=Multiplicity(0, 9999))
    }
)
view41: BinaryAssociation = BinaryAssociation(
    name="view41",
    ends={
        Property(name="mvc_View43", type=mvc_ControllerView, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_ControllerView42", type=mvc_View, multiplicity=Multiplicity(1, 1))
    }
)
models44: BinaryAssociation = BinaryAssociation(
    name="models44",
    ends={
        Property(name="mvc_Model46", type=mvc_ControllerView, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_ControllerView45", type=mvc_Model, multiplicity=Multiplicity(0, 9999))
    }
)
controllers47: BinaryAssociation = BinaryAssociation(
    name="controllers47",
    ends={
        Property(name="mvc_Controller49", type=mvc_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_Component48", type=mvc_Controller, multiplicity=Multiplicity(1, 9999))
    }
)
action50: BinaryAssociation = BinaryAssociation(
    name="action50",
    ends={
        Property(name="mvc_Action52", type=mvc_EventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_EventAction51", type=mvc_Action, multiplicity=Multiplicity(1, 1))
    }
)
events53: BinaryAssociation = BinaryAssociation(
    name="events53",
    ends={
        Property(name="mvc_Event55", type=mvc_EventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_EventAction54", type=mvc_Event, multiplicity=Multiplicity(0, 9999))
    }
)
views28: BinaryAssociation = BinaryAssociation(
    name="views28",
    ends={
        Property(name="mvc_ControllerView", type=mvc_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_Controller29", type=mvc_ControllerView, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventActions30: BinaryAssociation = BinaryAssociation(
    name="eventActions30",
    ends={
        Property(name="mvc_EventAction", type=mvc_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_Controller31", type=mvc_EventAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
importView58: BinaryAssociation = BinaryAssociation(
    name="importView58",
    ends={
        Property(name="mvc_View60", type=mvc_UILayout, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_UILayout59", type=mvc_View, multiplicity=Multiplicity(0, 9999))
    }
)
value61: BinaryAssociation = BinaryAssociation(
    name="value61",
    ends={
        Property(name="mvc_Attribute62", type=mvc_UIInput, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_UIInput", type=mvc_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
triggerEvent63: BinaryAssociation = BinaryAssociation(
    name="triggerEvent63",
    ends={
        Property(name="mvc_Event64", type=mvc_UIActions, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_UIActions", type=mvc_Event, multiplicity=Multiplicity(0, 1))
    }
)
components56: BinaryAssociation = BinaryAssociation(
    name="components56",
    ends={
        Property(name="mvc_UIComponent", type=mvc_UILayout, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_UILayout57", type=mvc_UIComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_mvc_Entity_Annotable = Generalization(general=Annotable, specific=mvc_Entity)
gen_mvc_Attribute_Annotable = Generalization(general=Annotable, specific=mvc_Attribute)
gen_mvc_Association_Annotable = Generalization(general=Annotable, specific=mvc_Association)
gen_mvc_Model_Annotable = Generalization(general=Annotable, specific=mvc_Model)
gen_mvc_MVCModel_Annotable = Generalization(general=Annotable, specific=mvc_MVCModel)
gen_mvc_Controller_Annotable = Generalization(general=Annotable, specific=mvc_Controller)
gen_mvc_View_Annotable = Generalization(general=Annotable, specific=mvc_View)
gen_mvc_UIComponent_Annotable = Generalization(general=Annotable, specific=mvc_UIComponent)
gen_mvc_ControllerView_Annotable = Generalization(general=Annotable, specific=mvc_ControllerView)
gen_mvc_Component_Annotable = Generalization(general=Annotable, specific=mvc_Component)
gen_mvc_EventAction_Annotable = Generalization(general=Annotable, specific=mvc_EventAction)
gen_mvc_UILayout_UIComponent = Generalization(general=UIComponent, specific=mvc_UILayout)
gen_mvc_Event_Annotable = Generalization(general=Annotable, specific=mvc_Event)
gen_mvc_Action_Annotable = Generalization(general=Annotable, specific=mvc_Action)
gen_mvc_UIInput_UIComponent = Generalization(general=UIComponent, specific=mvc_UIInput)
gen_mvc_UIActions_UIComponent = Generalization(general=UIComponent, specific=mvc_UIActions)

# Domain Model
domain_model = DomainModel(
    name="mvc",
    types={mvc_Entity, mvc_Association, mvc_Attribute, mvc_Model, Annotable, mvc_MVCModel, mvc_Event, mvc_Controller, mvc_Component, mvc_Action, mvc_View, mvc_UILayout, mvc_UIComponent, UIComponent, mvc_ControllerView, mvc_EventAction, mvc_UIInput, mvc_UIActions, AssociationType},
    associations={rootEntity0, associations1, attributes3, extends6, source8, target11, models15, views17, events20, controllers22, components24, actions26, rootComponent14, preExecutionEvent32, postExecutionEvent35, triggerEvents38, view41, models44, controllers47, action50, events53, views28, eventActions30, importView58, value61, triggerEvent63, components56},
    generalizations={gen_mvc_Entity_Annotable, gen_mvc_Attribute_Annotable, gen_mvc_Association_Annotable, gen_mvc_Model_Annotable, gen_mvc_MVCModel_Annotable, gen_mvc_Controller_Annotable, gen_mvc_View_Annotable, gen_mvc_UIComponent_Annotable, gen_mvc_ControllerView_Annotable, gen_mvc_Component_Annotable, gen_mvc_EventAction_Annotable, gen_mvc_UILayout_UIComponent, gen_mvc_Event_Annotable, gen_mvc_Action_Annotable, gen_mvc_UIInput_UIComponent, gen_mvc_UIActions_UIComponent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)