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
fsmcore_Transition = Class(name="fsmcore::Transition")
fsmcore_Program = Class(name="fsmcore::Program")
fsmcore_StateMachine = Class(name="fsmcore::StateMachine")
NamedElement = Class(name="NamedElement")
fsmcore_State = Class(name="fsmcore::State")
fsmcore_Trigger = Class(name="fsmcore::Trigger")
fsmcore_NamedElement = Class(name="fsmcore::NamedElement")
fsmcore_Constraint = Class(name="fsmcore::Constraint")

# fsmcore_Transition class attributes and methods

# fsmcore_Program class attributes and methods

# fsmcore_StateMachine class attributes and methods

# NamedElement class attributes and methods

# fsmcore_State class attributes and methods

# fsmcore_Trigger class attributes and methods
fsmcore_Trigger_expression: Property = Property(name="expression", type=StringType)
fsmcore_Trigger.attributes={fsmcore_Trigger_expression}

# fsmcore_NamedElement class attributes and methods
fsmcore_NamedElement_name: Property = Property(name="name", type=StringType)
fsmcore_NamedElement.attributes={fsmcore_NamedElement_name}

# fsmcore_Constraint class attributes and methods

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="fsmcore_State", type=fsmcore_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmcore_StateMachine", type=fsmcore_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="fsmcore_Transition", type=fsmcore_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmcore_StateMachine2", type=fsmcore_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
doAction3: BinaryAssociation = BinaryAssociation(
    name="doAction3",
    ends={
        Property(name="fsmcore_Program", type=fsmcore_State, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmcore_State4", type=fsmcore_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trigger10: BinaryAssociation = BinaryAssociation(
    name="trigger10",
    ends={
        Property(name="fsmcore_Trigger", type=fsmcore_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmcore_Transition11", type=fsmcore_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="State", type=fsmcore_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=fsmcore_State, multiplicity=Multiplicity(1, 1))
    }
)
source13: BinaryAssociation = BinaryAssociation(
    name="source13",
    ends={
        Property(name="State14", type=fsmcore_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=fsmcore_State, multiplicity=Multiplicity(1, 1))
    }
)
incoming5: BinaryAssociation = BinaryAssociation(
    name="incoming5",
    ends={
        Property(name="Transition", type=fsmcore_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=fsmcore_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing6: BinaryAssociation = BinaryAssociation(
    name="outgoing6",
    ends={
        Property(name="Transition7", type=fsmcore_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fsmcore_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
guard8: BinaryAssociation = BinaryAssociation(
    name="guard8",
    ends={
        Property(name="fsmcore_Constraint", type=fsmcore_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmcore_Transition9", type=fsmcore_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_fsmcore_State_NamedElement = Generalization(general=NamedElement, specific=fsmcore_State)
gen_fsmcore_StateMachine_NamedElement = Generalization(general=NamedElement, specific=fsmcore_StateMachine)
gen_fsmcore_Transition_NamedElement = Generalization(general=NamedElement, specific=fsmcore_Transition)

# Domain Model
domain_model = DomainModel(
    name="fsmcore",
    types={fsmcore_Transition, fsmcore_Program, fsmcore_StateMachine, NamedElement, fsmcore_State, fsmcore_Trigger, fsmcore_NamedElement, fsmcore_Constraint},
    associations={states0, transitions1, doAction3, trigger10, target12, source13, incoming5, outgoing6, guard8},
    generalizations={gen_fsmcore_State_NamedElement, gen_fsmcore_StateMachine_NamedElement, gen_fsmcore_Transition_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)