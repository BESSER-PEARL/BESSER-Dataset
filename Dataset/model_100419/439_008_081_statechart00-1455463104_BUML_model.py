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
statechart00_State = Class(name="statechart00_State")
statechart00_Variable = Class(name="statechart00_Variable")
statechart00_Transition = Class(name="statechart00_Transition")

# statechart00_State class attributes and methods
statechart00_State_name: Property = Property(name="name", type=StringType)
statechart00_State_label: Property = Property(name="label", type=StringType)
statechart00_State_type: Property = Property(name="type", type=StringType)
statechart00_State_activity: Property = Property(name="activity", type=StringType)
statechart00_State.attributes={statechart00_State_name, statechart00_State_activity, statechart00_State_type, statechart00_State_label}

# statechart00_Variable class attributes and methods
statechart00_Variable_name: Property = Property(name="name", type=StringType)
statechart00_Variable_type: Property = Property(name="type", type=StringType)
statechart00_Variable_value: Property = Property(name="value", type=StringType)
statechart00_Variable.attributes={statechart00_Variable_name, statechart00_Variable_type, statechart00_Variable_value}

# statechart00_Transition class attributes and methods
statechart00_Transition_name: Property = Property(name="name", type=StringType)
statechart00_Transition_expression: Property = Property(name="expression", type=StringType)
statechart00_Transition.attributes={statechart00_Transition_expression, statechart00_Transition_name}

# Relationships
substates1: BinaryAssociation = BinaryAssociation(
    name="substates1",
    ends={
        Property(name="State", type=statechart00_State, multiplicity=Multiplicity(1, 1)),
        Property(name="parentstate", type=statechart00_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentstate3: BinaryAssociation = BinaryAssociation(
    name="parentstate3",
    ends={
        Property(name="State4", type=statechart00_State, multiplicity=Multiplicity(1, 1)),
        Property(name="substates", type=statechart00_State, multiplicity=Multiplicity(0, 1))
    }
)
variables5: BinaryAssociation = BinaryAssociation(
    name="variables5",
    ends={
        Property(name="statechart00_Variable", type=statechart00_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart00_State", type=statechart00_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions6: BinaryAssociation = BinaryAssociation(
    name="transitions6",
    ends={
        Property(name="statechart00_Transition", type=statechart00_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart00_State7", type=statechart00_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="statechart00_State10", type=statechart00_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart00_Transition9", type=statechart00_State, multiplicity=Multiplicity(0, 1))
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="statechart00_State13", type=statechart00_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart00_Transition12", type=statechart00_State, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="statechart00",
    types={statechart00_State, statechart00_Variable, statechart00_Transition},
    associations={substates1, parentstate3, variables5, transitions6, source8, target11},
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