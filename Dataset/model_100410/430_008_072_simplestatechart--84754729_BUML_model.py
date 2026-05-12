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
simplestatechart_RelatedTo = Class(name="simplestatechart_RelatedTo")
simplestatechart_NamedElement = Class(name="simplestatechart_NamedElement", is_abstract=True)
simplestatechart_Thing = Class(name="simplestatechart_Thing", is_abstract=True)
NamedElement = Class(name="NamedElement")
simplestatechart_Transition = Class(name="simplestatechart_Transition")
simplestatechart_State = Class(name="simplestatechart_State")
simplestatechart_Variable = Class(name="simplestatechart_Variable")
Thing = Class(name="Thing")

# simplestatechart_RelatedTo class attributes and methods
simplestatechart_RelatedTo_since: Property = Property(name="since", type=StringType)
simplestatechart_RelatedTo.attributes={simplestatechart_RelatedTo_since}

# simplestatechart_NamedElement class attributes and methods
simplestatechart_NamedElement_name: Property = Property(name="name", type=StringType)
simplestatechart_NamedElement.attributes={simplestatechart_NamedElement_name}

# simplestatechart_Thing class attributes and methods
simplestatechart_Thing_id: Property = Property(name="id", type=IntegerType)
simplestatechart_Thing.attributes={simplestatechart_Thing_id}

# NamedElement class attributes and methods

# simplestatechart_Transition class attributes and methods
simplestatechart_Transition_expression: Property = Property(name="expression", type=StringType)
simplestatechart_Transition.attributes={simplestatechart_Transition_expression}

# simplestatechart_State class attributes and methods
simplestatechart_State_label: Property = Property(name="label", type=StringType)
simplestatechart_State_type: Property = Property(name="type", type=StringType)
simplestatechart_State_activity: Property = Property(name="activity", type=StringType)
simplestatechart_State.attributes={simplestatechart_State_label, simplestatechart_State_activity, simplestatechart_State_type}

# simplestatechart_Variable class attributes and methods
simplestatechart_Variable_type: Property = Property(name="type", type=StringType)
simplestatechart_Variable_value: Property = Property(name="value", type=StringType)
simplestatechart_Variable.attributes={simplestatechart_Variable_value, simplestatechart_Variable_type}

# Thing class attributes and methods

# Relationships
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
parentstate11: BinaryAssociation = BinaryAssociation(
    name="parentstate11",
    ends={
        Property(name="simplestatechart_State12", type=simplestatechart_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simplestatechart_State10", type=simplestatechart_State, multiplicity=Multiplicity(0, 1))
    }
)
variables13: BinaryAssociation = BinaryAssociation(
    name="variables13",
    ends={
        Property(name="simplestatechart_Variable", type=simplestatechart_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simplestatechart_State14", type=simplestatechart_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions15: BinaryAssociation = BinaryAssociation(
    name="transitions15",
    ends={
        Property(name="simplestatechart_Transition17", type=simplestatechart_State, multiplicity=Multiplicity(1, 1)),
        Property(name="simplestatechart_State16", type=simplestatechart_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
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

# Generalizations
gen_simplestatechart_Thing_NamedElement = Generalization(general=NamedElement, specific=simplestatechart_Thing)
gen_simplestatechart_Transition_NamedElement = Generalization(general=NamedElement, specific=simplestatechart_Transition)
gen_simplestatechart_RelatedTo_NamedElement = Generalization(general=NamedElement, specific=simplestatechart_RelatedTo)
gen_simplestatechart_Variable_Thing = Generalization(general=Thing, specific=simplestatechart_Variable)
gen_simplestatechart_State_NamedElement = Generalization(general=NamedElement, specific=simplestatechart_State)

# Domain Model
domain_model = DomainModel(
    name="simplestatechart",
    types={simplestatechart_RelatedTo, simplestatechart_NamedElement, simplestatechart_Thing, NamedElement, simplestatechart_Transition, simplestatechart_State, simplestatechart_Variable, Thing},
    associations={relations0, source3, fromThing1, toThing2, parentstate11, variables13, transitions15, target4, substates8},
    generalizations={gen_simplestatechart_Thing_NamedElement, gen_simplestatechart_Transition_NamedElement, gen_simplestatechart_RelatedTo_NamedElement, gen_simplestatechart_Variable_Thing, gen_simplestatechart_State_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)