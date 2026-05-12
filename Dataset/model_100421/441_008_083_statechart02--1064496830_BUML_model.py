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
statechart02_State = Class(name="statechart02_State")
statechart02_Variable = Class(name="statechart02_Variable")
statechart02_Transition = Class(name="statechart02_Transition")

# statechart02_State class attributes and methods
statechart02_State_name: Property = Property(name="name", type=StringType)
statechart02_State_label: Property = Property(name="label", type=StringType)
statechart02_State_type: Property = Property(name="type", type=StringType)
statechart02_State_activity: Property = Property(name="activity", type=StringType)
statechart02_State.attributes={statechart02_State_label, statechart02_State_type, statechart02_State_activity, statechart02_State_name}

# statechart02_Variable class attributes and methods
statechart02_Variable_name: Property = Property(name="name", type=StringType)
statechart02_Variable_type: Property = Property(name="type", type=StringType)
statechart02_Variable_value: Property = Property(name="value", type=StringType)
statechart02_Variable.attributes={statechart02_Variable_name, statechart02_Variable_type, statechart02_Variable_value}

# statechart02_Transition class attributes and methods
statechart02_Transition_expression: Property = Property(name="expression", type=StringType)
statechart02_Transition_name: Property = Property(name="name", type=StringType)
statechart02_Transition.attributes={statechart02_Transition_name, statechart02_Transition_expression}

# Relationships
substates1: BinaryAssociation = BinaryAssociation(
    name="substates1",
    ends={
        Property(name="parentstate", type=statechart02_State, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="State", type=statechart02_State, multiplicity=Multiplicity(1, 1))
    }
)
parentstate3: BinaryAssociation = BinaryAssociation(
    name="parentstate3",
    ends={
        Property(name="State4", type=statechart02_State, multiplicity=Multiplicity(1, 1)),
        Property(name="substates", type=statechart02_State, multiplicity=Multiplicity(0, 1))
    }
)
variables5: BinaryAssociation = BinaryAssociation(
    name="variables5",
    ends={
        Property(name="statechart02_Variable", type=statechart02_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart02_State", type=statechart02_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions6: BinaryAssociation = BinaryAssociation(
    name="transitions6",
    ends={
        Property(name="statechart02_Transition", type=statechart02_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart02_State7", type=statechart02_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="statechart02_State10", type=statechart02_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart02_Transition9", type=statechart02_State, multiplicity=Multiplicity(0, 1))
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="statechart02_State13", type=statechart02_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart02_Transition12", type=statechart02_State, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="statechart02",
    types={statechart02_State, statechart02_Variable, statechart02_Transition},
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