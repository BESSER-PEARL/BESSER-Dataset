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
statechart01_State = Class(name="statechart01_State")
statechart01_Variable = Class(name="statechart01_Variable")
statechart01_Transition = Class(name="statechart01_Transition")

# statechart01_State class attributes and methods
statechart01_State_name: Property = Property(name="name", type=StringType)
statechart01_State_label: Property = Property(name="label", type=StringType)
statechart01_State_type: Property = Property(name="type", type=StringType)
statechart01_State_activity: Property = Property(name="activity", type=StringType)
statechart01_State.attributes={statechart01_State_activity, statechart01_State_type, statechart01_State_name, statechart01_State_label}

# statechart01_Variable class attributes and methods
statechart01_Variable_name: Property = Property(name="name", type=StringType)
statechart01_Variable_type: Property = Property(name="type", type=StringType)
statechart01_Variable_value: Property = Property(name="value", type=StringType)
statechart01_Variable.attributes={statechart01_Variable_value, statechart01_Variable_name, statechart01_Variable_type}

# statechart01_Transition class attributes and methods
statechart01_Transition_expression: Property = Property(name="expression", type=StringType)
statechart01_Transition_name: Property = Property(name="name", type=StringType)
statechart01_Transition.attributes={statechart01_Transition_expression, statechart01_Transition_name}

# Relationships
substates1: BinaryAssociation = BinaryAssociation(
    name="substates1",
    ends={
        Property(name="State", type=statechart01_State, multiplicity=Multiplicity(1, 1)),
        Property(name="parentstate", type=statechart01_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentstate3: BinaryAssociation = BinaryAssociation(
    name="parentstate3",
    ends={
        Property(name="State4", type=statechart01_State, multiplicity=Multiplicity(1, 1)),
        Property(name="substates", type=statechart01_State, multiplicity=Multiplicity(0, 1))
    }
)
variables5: BinaryAssociation = BinaryAssociation(
    name="variables5",
    ends={
        Property(name="statechart01_Variable", type=statechart01_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart01_State", type=statechart01_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="statechart01_State13", type=statechart01_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart01_Transition12", type=statechart01_State, multiplicity=Multiplicity(0, 1))
    }
)
transitions6: BinaryAssociation = BinaryAssociation(
    name="transitions6",
    ends={
        Property(name="statechart01_Transition", type=statechart01_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart01_State7", type=statechart01_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="statechart01_State10", type=statechart01_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart01_Transition9", type=statechart01_State, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="statechart01",
    types={statechart01_State, statechart01_Variable, statechart01_Transition},
    associations={substates1, parentstate3, variables5, target11, transitions6, source8},
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