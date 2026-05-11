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
dfamodel_DFA = Class(name="dfamodel_DFA")
dfamodel_State = Class(name="dfamodel_State")
dfamodel_Transition = Class(name="dfamodel_Transition")

# dfamodel_DFA class attributes and methods

# dfamodel_State class attributes and methods
dfamodel_State_id: Property = Property(name="id", type=StringType)
dfamodel_State_isStart: Property = Property(name="isStart", type=BooleanType)
dfamodel_State_isEnd: Property = Property(name="isEnd", type=BooleanType)
dfamodel_State.attributes={dfamodel_State_isEnd, dfamodel_State_id, dfamodel_State_isStart}

# dfamodel_Transition class attributes and methods
dfamodel_Transition_input: Property = Property(name="input", type=StringType)
dfamodel_Transition.attributes={dfamodel_Transition_input}

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="dfamodel_State", type=dfamodel_DFA, multiplicity=Multiplicity(1, 1)),
        Property(name="dfamodel_DFA", type=dfamodel_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="dfamodel_Transition", type=dfamodel_DFA, multiplicity=Multiplicity(1, 1)),
        Property(name="dfamodel_DFA2", type=dfamodel_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from_3: BinaryAssociation = BinaryAssociation(
    name="from_3",
    ends={
        Property(name="State", type=dfamodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=dfamodel_State, multiplicity=Multiplicity(1, 1))
    }
)
to4: BinaryAssociation = BinaryAssociation(
    name="to4",
    ends={
        Property(name="State5", type=dfamodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=dfamodel_State, multiplicity=Multiplicity(1, 1))
    }
)
outgoingTransitions6: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions6",
    ends={
        Property(name="Transition", type=dfamodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="from_", type=dfamodel_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingTransitions7: BinaryAssociation = BinaryAssociation(
    name="incomingTransitions7",
    ends={
        Property(name="Transition8", type=dfamodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=dfamodel_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="dfamodel",
    types={dfamodel_DFA, dfamodel_State, dfamodel_Transition},
    associations={states0, transitions1, from_3, to4, outgoingTransitions6, incomingTransitions7},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)