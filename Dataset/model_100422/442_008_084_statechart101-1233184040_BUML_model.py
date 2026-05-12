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
statechart101_State = Class(name="statechart101_State")
NamedElement = Class(name="NamedElement")
Thing = Class(name="Thing")
statechart101_Variable = Class(name="statechart101_Variable")
statechart101_Transition = Class(name="statechart101_Transition")
statechart101_NamedElement = Class(name="statechart101_NamedElement", is_abstract=True)
statechart101_Thing = Class(name="statechart101_Thing")

# statechart101_State class attributes and methods
statechart101_State_label: Property = Property(name="label", type=StringType)
statechart101_State_type: Property = Property(name="type", type=StringType)
statechart101_State_activity: Property = Property(name="activity", type=StringType)
statechart101_State.attributes={statechart101_State_activity, statechart101_State_label, statechart101_State_type}

# NamedElement class attributes and methods

# Thing class attributes and methods

# statechart101_Variable class attributes and methods
statechart101_Variable_type: Property = Property(name="type", type=StringType)
statechart101_Variable_value: Property = Property(name="value", type=StringType)
statechart101_Variable.attributes={statechart101_Variable_type, statechart101_Variable_value}

# statechart101_Transition class attributes and methods
statechart101_Transition_expression: Property = Property(name="expression", type=StringType)
statechart101_Transition.attributes={statechart101_Transition_expression}

# statechart101_NamedElement class attributes and methods
statechart101_NamedElement_name: Property = Property(name="name", type=StringType)
statechart101_NamedElement.attributes={statechart101_NamedElement_name}

# statechart101_Thing class attributes and methods

# Relationships
substates1: BinaryAssociation = BinaryAssociation(
    name="substates1",
    ends={
        Property(name="State", type=statechart101_State, multiplicity=Multiplicity(1, 1)),
        Property(name="parentstate", type=statechart101_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="statechart101_Transition9", type=statechart101_State, multiplicity=Multiplicity(0, 1)),
        Property(name="statechart101_State10", type=statechart101_Transition, multiplicity=Multiplicity(1, 1))
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="statechart101_State13", type=statechart101_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart101_Transition12", type=statechart101_State, multiplicity=Multiplicity(0, 1))
    }
)
parentstate3: BinaryAssociation = BinaryAssociation(
    name="parentstate3",
    ends={
        Property(name="State4", type=statechart101_State, multiplicity=Multiplicity(1, 1)),
        Property(name="substates", type=statechart101_State, multiplicity=Multiplicity(0, 1))
    }
)
variables5: BinaryAssociation = BinaryAssociation(
    name="variables5",
    ends={
        Property(name="statechart101_Variable", type=statechart101_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart101_State", type=statechart101_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions6: BinaryAssociation = BinaryAssociation(
    name="transitions6",
    ends={
        Property(name="statechart101_Transition", type=statechart101_State, multiplicity=Multiplicity(1, 1)),
        Property(name="statechart101_State7", type=statechart101_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_statechart101_State_NamedElement = Generalization(general=NamedElement, specific=statechart101_State)
gen_statechart101_Variable_NamedElement = Generalization(general=NamedElement, specific=statechart101_Variable)
gen_statechart101_Variable_Thing = Generalization(general=Thing, specific=statechart101_Variable)
gen_statechart101_Transition_NamedElement = Generalization(general=NamedElement, specific=statechart101_Transition)

# Domain Model
domain_model = DomainModel(
    name="statechart101",
    types={statechart101_State, NamedElement, Thing, statechart101_Variable, statechart101_Transition, statechart101_NamedElement, statechart101_Thing},
    associations={substates1, source8, target11, parentstate3, variables5, transitions6},
    generalizations={gen_statechart101_State_NamedElement, gen_statechart101_Variable_NamedElement, gen_statechart101_Variable_Thing, gen_statechart101_Transition_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)