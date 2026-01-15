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
StateType: Enumeration = Enumeration(
    name="StateType",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="INITIAL"),
			EnumerationLiteral(name="FINAL")
    }
)

# Classes
statemodel_Activity = Class(name="statemodel::Activity")
statemodel_TransitionBlock = Class(name="statemodel::TransitionBlock")
statemodel_Model = Class(name="statemodel::Model")
statemodel_Import = Class(name="statemodel::Import")
statemodel_Element = Class(name="statemodel::Element")
statemodel_Annotation = Class(name="statemodel::Annotation")
statemodel_Statemachine = Class(name="statemodel::Statemachine")
Element = Class(name="Element")
statemodel_Entity = Class(name="statemodel::Entity")
statemodel_State = Class(name="statemodel::State")
Activity = Class(name="Activity")
statemodel_Transition = Class(name="statemodel::Transition")

# statemodel_Activity class attributes and methods

# statemodel_TransitionBlock class attributes and methods
statemodel_TransitionBlock_event: Property = Property(name="event", type=StringType)
statemodel_TransitionBlock.attributes={statemodel_TransitionBlock_event}

# statemodel_Model class attributes and methods

# statemodel_Import class attributes and methods
statemodel_Import_importURI: Property = Property(name="importURI", type=StringType)
statemodel_Import.attributes={statemodel_Import_importURI}

# statemodel_Element class attributes and methods

# statemodel_Annotation class attributes and methods

# statemodel_Statemachine class attributes and methods

# Element class attributes and methods

# statemodel_Entity class attributes and methods

# statemodel_State class attributes and methods
statemodel_State_type: Property = Property(name="type", type=StringType)
statemodel_State_name: Property = Property(name="name", type=StringType)
statemodel_State.attributes={statemodel_State_name, statemodel_State_type}

# Activity class attributes and methods

# statemodel_Transition class attributes and methods
statemodel_Transition_guard: Property = Property(name="guard", type=StringType)
statemodel_Transition_action: Property = Property(name="action", type=StringType)
statemodel_Transition.attributes={statemodel_Transition_action, statemodel_Transition_guard}

# Relationships
element8: BinaryAssociation = BinaryAssociation(
    name="element8",
    ends={
        Property(name="statemodel_Activity", type=statemodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statemodel_State9", type=statemodel_Activity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="statemodel_Import", type=statemodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="statemodel_Model", type=statemodel_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements1: BinaryAssociation = BinaryAssociation(
    name="elements1",
    ends={
        Property(name="statemodel_Element", type=statemodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="statemodel_Model2", type=statemodel_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation3: BinaryAssociation = BinaryAssociation(
    name="annotation3",
    ends={
        Property(name="statemodel_Annotation", type=statemodel_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="statemodel_Element4", type=statemodel_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
name5: BinaryAssociation = BinaryAssociation(
    name="name5",
    ends={
        Property(name="statemodel_Entity", type=statemodel_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemodel_Statemachine", type=statemodel_Entity, multiplicity=Multiplicity(0, 1))
    }
)
state6: BinaryAssociation = BinaryAssociation(
    name="state6",
    ends={
        Property(name="statemodel_State", type=statemodel_Statemachine, multiplicity=Multiplicity(1, 1)),
        Property(name="statemodel_Statemachine7", type=statemodel_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition10: BinaryAssociation = BinaryAssociation(
    name="transition10",
    ends={
        Property(name="statemodel_Transition", type=statemodel_TransitionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="statemodel_TransitionBlock", type=statemodel_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
state11: BinaryAssociation = BinaryAssociation(
    name="state11",
    ends={
        Property(name="statemodel_State13", type=statemodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statemodel_Transition12", type=statemodel_State, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_statemodel_Statemachine_Element = Generalization(general=Element, specific=statemodel_Statemachine)
gen_statemodel_State_Element = Generalization(general=Element, specific=statemodel_State)
gen_statemodel_State_Activity = Generalization(general=Activity, specific=statemodel_State)
gen_statemodel_TransitionBlock_Activity = Generalization(general=Activity, specific=statemodel_TransitionBlock)

# Domain Model
domain_model = DomainModel(
    name="statemodel",
    types={statemodel_Activity, statemodel_TransitionBlock, statemodel_Model, statemodel_Import, statemodel_Element, statemodel_Annotation, statemodel_Statemachine, Element, statemodel_Entity, statemodel_State, Activity, statemodel_Transition, StateType},
    associations={element8, imports0, elements1, annotation3, name5, state6, transition10, state11},
    generalizations={gen_statemodel_Statemachine_Element, gen_statemodel_State_Element, gen_statemodel_State_Activity, gen_statemodel_TransitionBlock_Activity},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)