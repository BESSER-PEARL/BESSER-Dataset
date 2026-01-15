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
mvc_Model = Class(name="mvc::Model")
Annotable = Class(name="Annotable")
mvc_Entity = Class(name="mvc::Entity")
mvc_Association = Class(name="mvc::Association")
mvc_Attribute = Class(name="mvc::Attribute")
mvc_Event = Class(name="mvc::Event")
mvc_MVCModel = Class(name="mvc::MVCModel")
mvc_View = Class(name="mvc::View")
mvc_UIComponent = Class(name="mvc::UIComponent")
mvc_Controller = Class(name="mvc::Controller")
mvc_Component = Class(name="mvc::Component")
mvc_Action = Class(name="mvc::Action")
mvc_ControllerView = Class(name="mvc::ControllerView")
mvc_EventAction = Class(name="mvc::EventAction")

# mvc_Model class attributes and methods
mvc_Model_name: Property = Property(name="name", type=StringType)
mvc_Model.attributes={mvc_Model_name}

# Annotable class attributes and methods

# mvc_Entity class attributes and methods
mvc_Entity_name: Property = Property(name="name", type=StringType)
mvc_Entity.attributes={mvc_Entity_name}

# mvc_Association class attributes and methods
mvc_Association_name: Property = Property(name="name", type=StringType)
mvc_Association_containment: Property = Property(name="containment", type=BooleanType)
mvc_Association_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
mvc_Association_upperBound: Property = Property(name="upperBound", type=IntegerType)
mvc_Association_type: Property = Property(name="type", type=StringType)
mvc_Association.attributes={mvc_Association_name, mvc_Association_containment, mvc_Association_lowerBound, mvc_Association_upperBound, mvc_Association_type}

# mvc_Attribute class attributes and methods
mvc_Attribute_name: Property = Property(name="name", type=StringType)
mvc_Attribute_type: Property = Property(name="type", type=StringType)
mvc_Attribute.attributes={mvc_Attribute_type, mvc_Attribute_name}

# mvc_Event class attributes and methods
mvc_Event_name: Property = Property(name="name", type=StringType)
mvc_Event.attributes={mvc_Event_name}

# mvc_MVCModel class attributes and methods
mvc_MVCModel_name: Property = Property(name="name", type=StringType)
mvc_MVCModel_version: Property = Property(name="version", type=StringType)
mvc_MVCModel.attributes={mvc_MVCModel_name, mvc_MVCModel_version}

# mvc_View class attributes and methods
mvc_View_name: Property = Property(name="name", type=StringType)
mvc_View.attributes={mvc_View_name}

# mvc_UIComponent class attributes and methods
mvc_UIComponent_layout: Property = Property(name="layout", type=StringType)
mvc_UIComponent_id: Property = Property(name="id", type=StringType)
mvc_UIComponent_name: Property = Property(name="name", type=StringType)
mvc_UIComponent_type: Property = Property(name="type", type=StringType)
mvc_UIComponent.attributes={mvc_UIComponent_layout, mvc_UIComponent_type, mvc_UIComponent_name, mvc_UIComponent_id}

# mvc_Controller class attributes and methods
mvc_Controller_name: Property = Property(name="name", type=StringType)
mvc_Controller.attributes={mvc_Controller_name}

# mvc_Component class attributes and methods
mvc_Component_name: Property = Property(name="name", type=StringType)
mvc_Component.attributes={mvc_Component_name}

# mvc_Action class attributes and methods
mvc_Action_name: Property = Property(name="name", type=StringType)
mvc_Action.attributes={mvc_Action_name}

# mvc_ControllerView class attributes and methods

# mvc_EventAction class attributes and methods

# Relationships
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
events18: BinaryAssociation = BinaryAssociation(
    name="events18",
    ends={
        Property(name="mvc_Event", type=mvc_UIComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_UIComponent19", type=mvc_Event, multiplicity=Multiplicity(0, 9999))
    }
)
models20: BinaryAssociation = BinaryAssociation(
    name="models20",
    ends={
        Property(name="mvc_Model21", type=mvc_MVCModel, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_MVCModel", type=mvc_Model, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
views22: BinaryAssociation = BinaryAssociation(
    name="views22",
    ends={
        Property(name="mvc_View24", type=mvc_MVCModel, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_MVCModel23", type=mvc_View, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events25: BinaryAssociation = BinaryAssociation(
    name="events25",
    ends={
        Property(name="mvc_Event27", type=mvc_MVCModel, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_MVCModel26", type=mvc_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="mvc_Entity13", type=mvc_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_Association12", type=mvc_Entity, multiplicity=Multiplicity(1, 1))
    }
)
rootComponent14: BinaryAssociation = BinaryAssociation(
    name="rootComponent14",
    ends={
        Property(name="mvc_UIComponent", type=mvc_View, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_View", type=mvc_UIComponent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
childs16: BinaryAssociation = BinaryAssociation(
    name="childs16",
    ends={
        Property(name="mvc_UIComponent17", type=mvc_UIComponent, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_UIComponent15", type=mvc_UIComponent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
eventActions36: BinaryAssociation = BinaryAssociation(
    name="eventActions36",
    ends={
        Property(name="mvc_Controller37", type=mvc_EventAction, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="mvc_EventAction", type=mvc_Controller, multiplicity=Multiplicity(1, 1))
    }
)
preExecutionEvent38: BinaryAssociation = BinaryAssociation(
    name="preExecutionEvent38",
    ends={
        Property(name="mvc_Event40", type=mvc_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_Action39", type=mvc_Event, multiplicity=Multiplicity(0, 1))
    }
)
postExecutionEvent41: BinaryAssociation = BinaryAssociation(
    name="postExecutionEvent41",
    ends={
        Property(name="mvc_Event43", type=mvc_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_Action42", type=mvc_Event, multiplicity=Multiplicity(0, 1))
    }
)
triggerEvents44: BinaryAssociation = BinaryAssociation(
    name="triggerEvents44",
    ends={
        Property(name="mvc_Event46", type=mvc_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_Action45", type=mvc_Event, multiplicity=Multiplicity(0, 9999))
    }
)
controllers28: BinaryAssociation = BinaryAssociation(
    name="controllers28",
    ends={
        Property(name="mvc_Controller", type=mvc_MVCModel, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_MVCModel29", type=mvc_Controller, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
components30: BinaryAssociation = BinaryAssociation(
    name="components30",
    ends={
        Property(name="mvc_Component", type=mvc_MVCModel, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_MVCModel31", type=mvc_Component, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
actions32: BinaryAssociation = BinaryAssociation(
    name="actions32",
    ends={
        Property(name="mvc_Action", type=mvc_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_Controller33", type=mvc_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
views34: BinaryAssociation = BinaryAssociation(
    name="views34",
    ends={
        Property(name="mvc_ControllerView", type=mvc_Controller, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_Controller35", type=mvc_ControllerView, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
view47: BinaryAssociation = BinaryAssociation(
    name="view47",
    ends={
        Property(name="mvc_View49", type=mvc_ControllerView, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_ControllerView48", type=mvc_View, multiplicity=Multiplicity(1, 1))
    }
)
models50: BinaryAssociation = BinaryAssociation(
    name="models50",
    ends={
        Property(name="mvc_Model52", type=mvc_ControllerView, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_ControllerView51", type=mvc_Model, multiplicity=Multiplicity(0, 9999))
    }
)
controllers53: BinaryAssociation = BinaryAssociation(
    name="controllers53",
    ends={
        Property(name="mvc_Controller55", type=mvc_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_Component54", type=mvc_Controller, multiplicity=Multiplicity(1, 9999))
    }
)
action56: BinaryAssociation = BinaryAssociation(
    name="action56",
    ends={
        Property(name="mvc_Action58", type=mvc_EventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_EventAction57", type=mvc_Action, multiplicity=Multiplicity(1, 1))
    }
)
events59: BinaryAssociation = BinaryAssociation(
    name="events59",
    ends={
        Property(name="mvc_Event61", type=mvc_EventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="mvc_EventAction60", type=mvc_Event, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_mvc_Attribute_Annotable = Generalization(general=Annotable, specific=mvc_Attribute)
gen_mvc_Association_Annotable = Generalization(general=Annotable, specific=mvc_Association)
gen_mvc_Model_Annotable = Generalization(general=Annotable, specific=mvc_Model)
gen_mvc_Entity_Annotable = Generalization(general=Annotable, specific=mvc_Entity)
gen_mvc_MVCModel_Annotable = Generalization(general=Annotable, specific=mvc_MVCModel)
gen_mvc_View_Annotable = Generalization(general=Annotable, specific=mvc_View)
gen_mvc_UIComponent_Annotable = Generalization(general=Annotable, specific=mvc_UIComponent)
gen_mvc_Event_Annotable = Generalization(general=Annotable, specific=mvc_Event)
gen_mvc_Action_Annotable = Generalization(general=Annotable, specific=mvc_Action)
gen_mvc_ControllerView_Annotable = Generalization(general=Annotable, specific=mvc_ControllerView)
gen_mvc_Controller_Annotable = Generalization(general=Annotable, specific=mvc_Controller)
gen_mvc_Component_Annotable = Generalization(general=Annotable, specific=mvc_Component)
gen_mvc_EventAction_Annotable = Generalization(general=Annotable, specific=mvc_EventAction)

# Domain Model
domain_model = DomainModel(
    name="mvc",
    types={mvc_Model, Annotable, mvc_Entity, mvc_Association, mvc_Attribute, mvc_Event, mvc_MVCModel, mvc_View, mvc_UIComponent, mvc_Controller, mvc_Component, mvc_Action, mvc_ControllerView, mvc_EventAction, AssociationType},
    associations={extends6, source8, rootEntity0, associations1, attributes3, events18, models20, views22, events25, target11, rootComponent14, childs16, eventActions36, preExecutionEvent38, postExecutionEvent41, triggerEvents44, controllers28, components30, actions32, views34, view47, models50, controllers53, action56, events59},
    generalizations={gen_mvc_Attribute_Annotable, gen_mvc_Association_Annotable, gen_mvc_Model_Annotable, gen_mvc_Entity_Annotable, gen_mvc_MVCModel_Annotable, gen_mvc_View_Annotable, gen_mvc_UIComponent_Annotable, gen_mvc_Event_Annotable, gen_mvc_Action_Annotable, gen_mvc_ControllerView_Annotable, gen_mvc_Controller_Annotable, gen_mvc_Component_Annotable, gen_mvc_EventAction_Annotable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)