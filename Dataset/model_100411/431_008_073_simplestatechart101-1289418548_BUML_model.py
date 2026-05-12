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
simplestatechart101_NamedElement = Class(name="simplestatechart101_NamedElement", is_abstract=True)
simplestatechart101_Thing = Class(name="simplestatechart101_Thing", is_abstract=True)
NamedElement = Class(name="NamedElement")
simplestatechart101_RelatedTo = Class(name="simplestatechart101_RelatedTo")
simplestatechart101_State = Class(name="simplestatechart101_State")
simplestatechart101_Variable = Class(name="simplestatechart101_Variable")
Thing = Class(name="Thing")
simplestatechart101_Transition = Class(name="simplestatechart101_Transition")

# simplestatechart101_NamedElement class attributes and methods
simplestatechart101_NamedElement_name: Property = Property(name="name", type=StringType)
simplestatechart101_NamedElement.attributes={simplestatechart101_NamedElement_name}

# simplestatechart101_Thing class attributes and methods
simplestatechart101_Thing_id: Property = Property(name="id", type=IntegerType)
simplestatechart101_Thing.attributes={simplestatechart101_Thing_id}

# NamedElement class attributes and methods

# simplestatechart101_RelatedTo class attributes and methods
simplestatechart101_RelatedTo_since: Property = Property(name="since", type=StringType)
simplestatechart101_RelatedTo.attributes={simplestatechart101_RelatedTo_since}

# simplestatechart101_State class attributes and methods
simplestatechart101_State_label: Property = Property(name="label", type=StringType)
simplestatechart101_State_type: Property = Property(name="type", type=StringType)
simplestatechart101_State_activity: Property = Property(name="activity", type=StringType)
simplestatechart101_State.attributes={simplestatechart101_State_type, simplestatechart101_State_activity, simplestatechart101_State_label}

# simplestatechart101_Variable class attributes and methods
simplestatechart101_Variable_type: Property = Property(name="type", type=StringType)
simplestatechart101_Variable_value: Property = Property(name="value", type=StringType)
simplestatechart101_Variable.attributes={simplestatechart101_Variable_value, simplestatechart101_Variable_type}

# Thing class attributes and methods

# simplestatechart101_Transition class attributes and methods
simplestatechart101_Transition_expression: Property = Property(name="expression", type=StringType)
simplestatechart101_Transition.attributes={simplestatechart101_Transition_expression}

# Relationships
fromThing1: BinaryAssociation = BinaryAssociation(
    name="fromThing1",
    ends={
        Property(name="Thing", type=simplestatechart101_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=simplestatechart101_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing2: BinaryAssociation = BinaryAssociation(
    name="toThing2",
    ends={
        Property(name="simplestatechart101_Thing", type=simplestatechart101_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="simplestatechart101_RelatedTo", type=simplestatechart101_Thing, multiplicity=Multiplicity(0, 1))
    }
)
relations0: BinaryAssociation = BinaryAssociation(
    name="relations0",
    ends={
        Property(name="RelatedTo", type=simplestatechart101_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=simplestatechart101_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="simplestatechart101_State", type=simplestatechart101_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="simplestatechart101_Transition", type=simplestatechart101_State, multiplicity=Multiplicity(0, 1))
    }
)
target4: BinaryAssociation = BinaryAssociation(
    name="target4",
    ends={
        Property(name="simplestatechart101_State6", type=simplestatechart101_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="simplestatechart101_Transition5", type=simplestatechart101_State, multiplicity=Multiplicity(0, 1))
    }
)
transitions15: BinaryAssociation = BinaryAssociation(
    name="transitions15",
    ends={
        Property(name="simplestatechart101_Transition17", type=simplestatechart101_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simplestatechart101_State16", type=simplestatechart101_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
substates8: BinaryAssociation = BinaryAssociation(
    name="substates8",
    ends={
        Property(name="simplestatechart101_State9", type=simplestatechart101_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simplestatechart101_State7", type=simplestatechart101_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentstate11: BinaryAssociation = BinaryAssociation(
    name="parentstate11",
    ends={
        Property(name="simplestatechart101_State12", type=simplestatechart101_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simplestatechart101_State10", type=simplestatechart101_State, multiplicity=Multiplicity(0, 1))
    }
)
variables13: BinaryAssociation = BinaryAssociation(
    name="variables13",
    ends={
        Property(name="simplestatechart101_Variable", type=simplestatechart101_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simplestatechart101_State14", type=simplestatechart101_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_simplestatechart101_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=simplestatechart101_RelatedTo)
gen_simplestatechart101_Thing_NamedElement = Generalization(general=NamedElement, specific=simplestatechart101_Thing)
gen_simplestatechart101_State_NamedElement = Generalization(general=NamedElement, specific=simplestatechart101_State)
gen_simplestatechart101_Variable_Thing = Generalization(general=Thing, specific=simplestatechart101_Variable)
gen_simplestatechart101_Transition_NamedElement = Generalization(general=NamedElement, specific=simplestatechart101_Transition)

# Domain Model
domain_model = DomainModel(
    name="simplestatechart101",
    types={simplestatechart101_NamedElement, simplestatechart101_Thing, NamedElement, simplestatechart101_RelatedTo, simplestatechart101_State, simplestatechart101_Variable, Thing, simplestatechart101_Transition},
    associations={fromThing1, toThing2, relations0, source3, target4, transitions15, substates8, parentstate11, variables13},
    generalizations={gen_simplestatechart101_RelatedTo_NamedElement, gen_simplestatechart101_Thing_NamedElement, gen_simplestatechart101_State_NamedElement, gen_simplestatechart101_Variable_Thing, gen_simplestatechart101_Transition_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)