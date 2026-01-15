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
simple200_Thing = Class(name="simple200::Thing", is_abstract=True)
NamedElement = Class(name="NamedElement")
simple200_RelatedTo = Class(name="simple200::RelatedTo")
simple200_NamedElement = Class(name="simple200::NamedElement", is_abstract=True)
simple200_Variable = Class(name="simple200::Variable")
Thing = Class(name="Thing")
simple200_Transition = Class(name="simple200::Transition")
simple200_State = Class(name="simple200::State")

# simple200_Thing class attributes and methods
simple200_Thing_id: Property = Property(name="id", type=IntegerType)
simple200_Thing.attributes={simple200_Thing_id}

# NamedElement class attributes and methods

# simple200_RelatedTo class attributes and methods
simple200_RelatedTo_since: Property = Property(name="since", type=StringType)
simple200_RelatedTo.attributes={simple200_RelatedTo_since}

# simple200_NamedElement class attributes and methods
simple200_NamedElement_name: Property = Property(name="name", type=StringType)
simple200_NamedElement.attributes={simple200_NamedElement_name}

# simple200_Variable class attributes and methods
simple200_Variable_type: Property = Property(name="type", type=StringType)
simple200_Variable_value: Property = Property(name="value", type=StringType)
simple200_Variable.attributes={simple200_Variable_type, simple200_Variable_value}

# Thing class attributes and methods

# simple200_Transition class attributes and methods
simple200_Transition_expression: Property = Property(name="expression", type=StringType)
simple200_Transition.attributes={simple200_Transition_expression}

# simple200_State class attributes and methods
simple200_State_label: Property = Property(name="label", type=StringType)
simple200_State_type: Property = Property(name="type", type=StringType)
simple200_State_activity: Property = Property(name="activity", type=StringType)
simple200_State.attributes={simple200_State_activity, simple200_State_label, simple200_State_type}

# Relationships
fromThing1: BinaryAssociation = BinaryAssociation(
    name="fromThing1",
    ends={
        Property(name="Thing", type=simple200_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=simple200_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing2: BinaryAssociation = BinaryAssociation(
    name="toThing2",
    ends={
        Property(name="simple200_Thing", type=simple200_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="simple200_RelatedTo", type=simple200_Thing, multiplicity=Multiplicity(0, 1))
    }
)
relations0: BinaryAssociation = BinaryAssociation(
    name="relations0",
    ends={
        Property(name="RelatedTo", type=simple200_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=simple200_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
substates6: BinaryAssociation = BinaryAssociation(
    name="substates6",
    ends={
        Property(name="simple200_State7", type=simple200_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simple200_State5", type=simple200_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentstate9: BinaryAssociation = BinaryAssociation(
    name="parentstate9",
    ends={
        Property(name="simple200_State10", type=simple200_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simple200_State8", type=simple200_State, multiplicity=Multiplicity(0, 1))
    }
)
variables11: BinaryAssociation = BinaryAssociation(
    name="variables11",
    ends={
        Property(name="simple200_Variable", type=simple200_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simple200_State12", type=simple200_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions13: BinaryAssociation = BinaryAssociation(
    name="transitions13",
    ends={
        Property(name="Transition", type=simple200_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=simple200_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="State", type=simple200_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=simple200_State, multiplicity=Multiplicity(0, 1))
    }
)
target4: BinaryAssociation = BinaryAssociation(
    name="target4",
    ends={
        Property(name="simple200_State", type=simple200_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="simple200_Transition", type=simple200_State, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_simple200_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=simple200_RelatedTo)
gen_simple200_Thing_NamedElement = Generalization(general=NamedElement, specific=simple200_Thing)
gen_simple200_State_NamedElement = Generalization(general=NamedElement, specific=simple200_State)
gen_simple200_Variable_Thing = Generalization(general=Thing, specific=simple200_Variable)
gen_simple200_Transition_NamedElement = Generalization(general=NamedElement, specific=simple200_Transition)

# Domain Model
domain_model = DomainModel(
    name="simple200",
    types={simple200_Thing, NamedElement, simple200_RelatedTo, simple200_NamedElement, simple200_Variable, Thing, simple200_Transition, simple200_State},
    associations={fromThing1, toThing2, relations0, substates6, parentstate9, variables11, transitions13, source3, target4},
    generalizations={gen_simple200_RelatedTo_NamedElement, gen_simple200_Thing_NamedElement, gen_simple200_State_NamedElement, gen_simple200_Variable_Thing, gen_simple200_Transition_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)