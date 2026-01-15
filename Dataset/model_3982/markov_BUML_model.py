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
            EnumerationLiteral(name="Default"),
			EnumerationLiteral(name="Start"),
			EnumerationLiteral(name="Success"),
			EnumerationLiteral(name="Failure")
    }
)

# Classes
markov_State = Class(name="markov::State")
Entity = Class(name="Entity")
markov_Label = Class(name="markov::Label")
markov_Entity = Class(name="markov::Entity")
markov_Transition = Class(name="markov::Transition")
markov_MarkovChain = Class(name="markov::MarkovChain")

# markov_State class attributes and methods
markov_State_type: Property = Property(name="type", type=StringType)
markov_State_traces: Property = Property(name="traces", type=StringType)
markov_State.attributes={markov_State_type, markov_State_traces}

# Entity class attributes and methods

# markov_Label class attributes and methods
markov_Label_key: Property = Property(name="key", type=StringType)
markov_Label_value: Property = Property(name="value", type=StringType)
markov_Label.attributes={markov_Label_value, markov_Label_key}

# markov_Entity class attributes and methods
markov_Entity_Name: Property = Property(name="Name", type=StringType)
markov_Entity.attributes={markov_Entity_Name}

# markov_Transition class attributes and methods
markov_Transition_probability: Property = Property(name="probability", type=FloatType)
markov_Transition.attributes={markov_Transition_probability}

# markov_MarkovChain class attributes and methods

# Relationships
labels0: BinaryAssociation = BinaryAssociation(
    name="labels0",
    ends={
        Property(name="markov_Label", type=markov_State, multiplicity=Multiplicity(1, 1)),
        Property(name="markov_State", type=markov_Label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromState1: BinaryAssociation = BinaryAssociation(
    name="fromState1",
    ends={
        Property(name="markov_State2", type=markov_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="markov_Transition", type=markov_State, multiplicity=Multiplicity(1, 1))
    }
)
toState3: BinaryAssociation = BinaryAssociation(
    name="toState3",
    ends={
        Property(name="markov_State5", type=markov_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="markov_Transition4", type=markov_State, multiplicity=Multiplicity(1, 1))
    }
)
states6: BinaryAssociation = BinaryAssociation(
    name="states6",
    ends={
        Property(name="markov_State7", type=markov_MarkovChain, multiplicity=Multiplicity(1, 1)),
        Property(name="markov_MarkovChain", type=markov_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions8: BinaryAssociation = BinaryAssociation(
    name="transitions8",
    ends={
        Property(name="markov_Transition10", type=markov_MarkovChain, multiplicity=Multiplicity(1, 1)),
        Property(name="markov_MarkovChain9", type=markov_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_markov_State_Entity = Generalization(general=Entity, specific=markov_State)
gen_markov_Transition_Entity = Generalization(general=Entity, specific=markov_Transition)
gen_markov_MarkovChain_Entity = Generalization(general=Entity, specific=markov_MarkovChain)

# Domain Model
domain_model = DomainModel(
    name="markov",
    types={markov_State, Entity, markov_Label, markov_Entity, markov_Transition, markov_MarkovChain, StateType},
    associations={labels0, fromState1, toState3, states6, transitions8},
    generalizations={gen_markov_State_Entity, gen_markov_Transition_Entity, gen_markov_MarkovChain_Entity},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)