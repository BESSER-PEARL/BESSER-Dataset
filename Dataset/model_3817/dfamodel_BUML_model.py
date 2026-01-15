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
dfamodel_DFA = Class(name="dfamodel::DFA")
dfamodel_Transition = Class(name="dfamodel::Transition")
dfamodel_State = Class(name="dfamodel::State")

# dfamodel_DFA class attributes and methods

# dfamodel_Transition class attributes and methods
dfamodel_Transition_input: Property = Property(name="input", type=StringType)
dfamodel_Transition.attributes={dfamodel_Transition_input}

# dfamodel_State class attributes and methods
dfamodel_State_isStart: Property = Property(name="isStart", type=BooleanType)
dfamodel_State_isEnd: Property = Property(name="isEnd", type=BooleanType)
dfamodel_State_id: Property = Property(name="id", type=StringType)
dfamodel_State.attributes={dfamodel_State_isStart, dfamodel_State_id, dfamodel_State_isEnd}

# Relationships
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="dfamodel_Transition", type=dfamodel_DFA, multiplicity=Multiplicity(1, 1)),
        Property(name="dfamodel_DFA2", type=dfamodel_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from3: BinaryAssociation = BinaryAssociation(
    name="from3",
    ends={
        Property(name="State", type=dfamodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingTransitions", type=dfamodel_State, multiplicity=Multiplicity(1, 1))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="dfamodel_State", type=dfamodel_DFA, multiplicity=Multiplicity(1, 1)),
        Property(name="dfamodel_DFA", type=dfamodel_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingTransitions6: BinaryAssociation = BinaryAssociation(
    name="outgoingTransitions6",
    ends={
        Property(name="Transition", type=dfamodel_State, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=dfamodel_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
to4: BinaryAssociation = BinaryAssociation(
    name="to4",
    ends={
        Property(name="State5", type=dfamodel_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingTransitions", type=dfamodel_State, multiplicity=Multiplicity(1, 1))
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
    types={dfamodel_DFA, dfamodel_Transition, dfamodel_State},
    associations={transitions1, from3, states0, outgoingTransitions6, to4, incomingTransitions7},
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