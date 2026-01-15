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
simplestatechart_Thing = Class(name="simplestatechart::Thing", is_abstract=True)
NamedElement = Class(name="NamedElement")
simplestatechart_NamedElement = Class(name="simplestatechart::NamedElement", is_abstract=True)
simplestatechart_Variable = Class(name="simplestatechart::Variable")
Thing = Class(name="Thing")
simplestatechart_Transition = Class(name="simplestatechart::Transition")
simplestatechart_RelatedTo = Class(name="simplestatechart::RelatedTo")
simplestatechart_State = Class(name="simplestatechart::State")

# simplestatechart_Thing class attributes and methods
simplestatechart_Thing_id: Property = Property(name="id", type=IntegerType)
simplestatechart_Thing.attributes={simplestatechart_Thing_id}

# NamedElement class attributes and methods

# simplestatechart_NamedElement class attributes and methods
simplestatechart_NamedElement_name: Property = Property(name="name", type=StringType)
simplestatechart_NamedElement.attributes={simplestatechart_NamedElement_name}

# simplestatechart_Variable class attributes and methods
simplestatechart_Variable_type: Property = Property(name="type", type=StringType)
simplestatechart_Variable_value: Property = Property(name="value", type=StringType)
simplestatechart_Variable.attributes={simplestatechart_Variable_type, simplestatechart_Variable_value}

# Thing class attributes and methods

# simplestatechart_Transition class attributes and methods
simplestatechart_Transition_expression: Property = Property(name="expression", type=StringType)
simplestatechart_Transition.attributes={simplestatechart_Transition_expression}

# simplestatechart_RelatedTo class attributes and methods
simplestatechart_RelatedTo_since: Property = Property(name="since", type=StringType)
simplestatechart_RelatedTo.attributes={simplestatechart_RelatedTo_since}

# simplestatechart_State class attributes and methods
simplestatechart_State_label: Property = Property(name="label", type=StringType)
simplestatechart_State_type: Property = Property(name="type", type=StringType)
simplestatechart_State_activity: Property = Property(name="activity", type=StringType)
simplestatechart_State.attributes={simplestatechart_State_label, simplestatechart_State_type, simplestatechart_State_activity}

# Relationships
fromThing1: BinaryAssociation = BinaryAssociation(
    name="fromThing1",
    ends={
        Property(name="Thing", type=simplestatechart_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="relations", type=simplestatechart_Thing, multiplicity=Multiplicity(0, 1))
    }
)
toThing2: BinaryAssociation = BinaryAssociation(
    name="toThing2",
    ends={
        Property(name="simplestatechart_Thing", type=simplestatechart_RelatedTo, multiplicity=Multiplicity(1, 1)),
        Property(name="simplestatechart_RelatedTo", type=simplestatechart_Thing, multiplicity=Multiplicity(0, 1))
    }
)
relations0: BinaryAssociation = BinaryAssociation(
    name="relations0",
    ends={
        Property(name="RelatedTo", type=simplestatechart_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="fromThing", type=simplestatechart_RelatedTo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="simplestatechart_State", type=simplestatechart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="simplestatechart_Transition", type=simplestatechart_State, multiplicity=Multiplicity(0, 1))
    }
)
target4: BinaryAssociation = BinaryAssociation(
    name="target4",
    ends={
        Property(name="simplestatechart_State6", type=simplestatechart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="simplestatechart_Transition5", type=simplestatechart_State, multiplicity=Multiplicity(0, 1))
    }
)
substates8: BinaryAssociation = BinaryAssociation(
    name="substates8",
    ends={
        Property(name="simplestatechart_State9", type=simplestatechart_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simplestatechart_State7", type=simplestatechart_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables13: BinaryAssociation = BinaryAssociation(
    name="variables13",
    ends={
        Property(name="simplestatechart_State14", type=simplestatechart_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="simplestatechart_Variable", type=simplestatechart_State, multiplicity=Multiplicity(1, 1))
    }
)
transitions15: BinaryAssociation = BinaryAssociation(
    name="transitions15",
    ends={
        Property(name="simplestatechart_Transition17", type=simplestatechart_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simplestatechart_State16", type=simplestatechart_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentstate11: BinaryAssociation = BinaryAssociation(
    name="parentstate11",
    ends={
        Property(name="simplestatechart_State12", type=simplestatechart_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simplestatechart_State10", type=simplestatechart_State, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_simplestatechart_Thing_NamedElement = Generalization(general=NamedElement, specific=simplestatechart_Thing)
gen_simplestatechart_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=simplestatechart_RelatedTo)
gen_simplestatechart_Variable_Thing = Generalization(general=Thing, specific=simplestatechart_Variable)
gen_simplestatechart_State_NamedElement = Generalization(general=NamedElement, specific=simplestatechart_State)
gen_simplestatechart_Transition_NamedElement = Generalization(general=NamedElement, specific=simplestatechart_Transition)

# Domain Model
domain_model = DomainModel(
    name="simplestatechart",
    types={simplestatechart_Thing, NamedElement, simplestatechart_NamedElement, simplestatechart_Variable, Thing, simplestatechart_Transition, simplestatechart_RelatedTo, simplestatechart_State},
    associations={fromThing1, toThing2, relations0, source3, target4, substates8, variables13, transitions15, parentstate11},
    generalizations={gen_simplestatechart_Thing_NamedElement, gen_simplestatechart_RelatedTo_NamedElement, gen_simplestatechart_Variable_Thing, gen_simplestatechart_State_NamedElement, gen_simplestatechart_Transition_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)