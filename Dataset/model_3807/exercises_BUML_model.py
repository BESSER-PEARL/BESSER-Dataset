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
exercises_DFA = Class(name="exercises::DFA")
NamableElement = Class(name="NamableElement")
exercises_State = Class(name="exercises::State")
exercises_Transition = Class(name="exercises::Transition")
exercises_NamableElement = Class(name="exercises::NamableElement", is_abstract=True)

# exercises_DFA class attributes and methods

# NamableElement class attributes and methods

# exercises_State class attributes and methods
exercises_State_id: Property = Property(name="id", type=StringType)
exercises_State_isStart: Property = Property(name="isStart", type=BooleanType)
exercises_State_isEnd: Property = Property(name="isEnd", type=BooleanType)
exercises_State.attributes={exercises_State_id, exercises_State_isStart, exercises_State_isEnd}

# exercises_Transition class attributes and methods
exercises_Transition_input: Property = Property(name="input", type=StringType)
exercises_Transition.attributes={exercises_Transition_input}

# exercises_NamableElement class attributes and methods
exercises_NamableElement_name: Property = Property(name="name", type=StringType)
exercises_NamableElement.attributes={exercises_NamableElement_name}

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="exercises_State", type=exercises_DFA, multiplicity=Multiplicity(1, 1)),
        Property(name="exercises_DFA", type=exercises_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition1: BinaryAssociation = BinaryAssociation(
    name="transition1",
    ends={
        Property(name="exercises_Transition", type=exercises_DFA, multiplicity=Multiplicity(1, 1)),
        Property(name="exercises_DFA2", type=exercises_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming3: BinaryAssociation = BinaryAssociation(
    name="incoming3",
    ends={
        Property(name="exercises_Transition5", type=exercises_State, multiplicity=Multiplicity(1, 1)),
        Property(name="exercises_State4", type=exercises_Transition, multiplicity=Multiplicity(1, 9999))
    }
)
outgoing6: BinaryAssociation = BinaryAssociation(
    name="outgoing6",
    ends={
        Property(name="exercises_Transition8", type=exercises_State, multiplicity=Multiplicity(1, 1)),
        Property(name="exercises_State7", type=exercises_Transition, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_exercises_State_NamableElement = Generalization(general=NamableElement, specific=exercises_State)
gen_exercises_DFA_NamableElement = Generalization(general=NamableElement, specific=exercises_DFA)
gen_exercises_Transition_NamableElement = Generalization(general=NamableElement, specific=exercises_Transition)

# Domain Model
domain_model = DomainModel(
    name="exercises",
    types={exercises_DFA, NamableElement, exercises_State, exercises_Transition, exercises_NamableElement},
    associations={states0, transition1, incoming3, outgoing6},
    generalizations={gen_exercises_State_NamableElement, gen_exercises_DFA_NamableElement, gen_exercises_Transition_NamableElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)