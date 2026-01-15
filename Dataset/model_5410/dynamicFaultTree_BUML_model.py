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
dynamicFaultTree_DFT = Class(name="dynamicFaultTree::DFT")
dynamicFaultTree_TopLevelEvent = Class(name="dynamicFaultTree::TopLevelEvent")
dynamicFaultTree_Dependency = Class(name="dynamicFaultTree::Dependency", is_abstract=True)
dynamicFaultTree_Element = Class(name="dynamicFaultTree::Element", is_abstract=True)
Element = Class(name="Element")
dynamicFaultTree_Gate = Class(name="dynamicFaultTree::Gate", is_abstract=True)
dynamicFaultTree_Event = Class(name="dynamicFaultTree::Event")
dynamicFaultTree_FunctionalDependency = Class(name="dynamicFaultTree::FunctionalDependency")
dynamicFaultTree_AND = Class(name="dynamicFaultTree::AND")
Gate = Class(name="Gate")
dynamicFaultTree_PAND = Class(name="dynamicFaultTree::PAND")
dynamicFaultTree_OR = Class(name="dynamicFaultTree::OR")
dynamicFaultTree_POR = Class(name="dynamicFaultTree::POR")
dynamicFaultTree_XOR = Class(name="dynamicFaultTree::XOR")
dynamicFaultTree_Spare = Class(name="dynamicFaultTree::Spare")
dynamicFaultTree_Sequence = Class(name="dynamicFaultTree::Sequence")
Dependency = Class(name="Dependency")

# dynamicFaultTree_DFT class attributes and methods
dynamicFaultTree_DFT_name: Property = Property(name="name", type=StringType)
dynamicFaultTree_DFT.attributes={dynamicFaultTree_DFT_name}

# dynamicFaultTree_TopLevelEvent class attributes and methods

# dynamicFaultTree_Dependency class attributes and methods

# dynamicFaultTree_Element class attributes and methods
dynamicFaultTree_Element_name: Property = Property(name="name", type=StringType)
dynamicFaultTree_Element_probability: Property = Property(name="probability", type=FloatType)
dynamicFaultTree_Element_sequencePosition: Property = Property(name="sequencePosition", type=IntegerType)
dynamicFaultTree_Element_elementID: Property = Property(name="elementID", type=IntegerType)
dynamicFaultTree_Element.attributes={dynamicFaultTree_Element_name, dynamicFaultTree_Element_elementID, dynamicFaultTree_Element_sequencePosition, dynamicFaultTree_Element_probability}

# Element class attributes and methods

# dynamicFaultTree_Gate class attributes and methods

# dynamicFaultTree_Event class attributes and methods

# dynamicFaultTree_FunctionalDependency class attributes and methods

# dynamicFaultTree_AND class attributes and methods

# Gate class attributes and methods

# dynamicFaultTree_PAND class attributes and methods

# dynamicFaultTree_OR class attributes and methods

# dynamicFaultTree_POR class attributes and methods

# dynamicFaultTree_XOR class attributes and methods

# dynamicFaultTree_Spare class attributes and methods

# dynamicFaultTree_Sequence class attributes and methods

# Dependency class attributes and methods

# Relationships
topLevelEvent0: BinaryAssociation = BinaryAssociation(
    name="topLevelEvent0",
    ends={
        Property(name="dynamicFaultTree_TopLevelEvent", type=dynamicFaultTree_DFT, multiplicity=Multiplicity(1, 1)),
        Property(name="dynamicFaultTree_DFT", type=dynamicFaultTree_TopLevelEvent, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
dependencies1: BinaryAssociation = BinaryAssociation(
    name="dependencies1",
    ends={
        Property(name="dynamicFaultTree_Dependency", type=dynamicFaultTree_DFT, multiplicity=Multiplicity(1, 1)),
        Property(name="dynamicFaultTree_DFT2", type=dynamicFaultTree_Dependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gate3: BinaryAssociation = BinaryAssociation(
    name="gate3",
    ends={
        Property(name="Gate", type=dynamicFaultTree_TopLevelEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="toplevelevent", type=dynamicFaultTree_Gate, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toplevelevent4: BinaryAssociation = BinaryAssociation(
    name="toplevelevent4",
    ends={
        Property(name="TopLevelEvent", type=dynamicFaultTree_Gate, multiplicity=Multiplicity(1, 1)),
        Property(name="gate", type=dynamicFaultTree_TopLevelEvent, multiplicity=Multiplicity(0, 1))
    }
)
childGate6: BinaryAssociation = BinaryAssociation(
    name="childGate6",
    ends={
        Property(name="Gate7", type=dynamicFaultTree_Gate, multiplicity=Multiplicity(1, 1)),
        Property(name="parentGate", type=dynamicFaultTree_Gate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentGate9: BinaryAssociation = BinaryAssociation(
    name="parentGate9",
    ends={
        Property(name="Gate10", type=dynamicFaultTree_Gate, multiplicity=Multiplicity(1, 1)),
        Property(name="childGate", type=dynamicFaultTree_Gate, multiplicity=Multiplicity(0, 1))
    }
)
childEvent11: BinaryAssociation = BinaryAssociation(
    name="childEvent11",
    ends={
        Property(name="Event", type=dynamicFaultTree_Gate, multiplicity=Multiplicity(1, 1)),
        Property(name="parentGate12", type=dynamicFaultTree_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentGate13: BinaryAssociation = BinaryAssociation(
    name="parentGate13",
    ends={
        Property(name="Gate14", type=dynamicFaultTree_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="childEvent", type=dynamicFaultTree_Gate, multiplicity=Multiplicity(0, 1))
    }
)
dependency15: BinaryAssociation = BinaryAssociation(
    name="dependency15",
    ends={
        Property(name="Dependency", type=dynamicFaultTree_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="events", type=dynamicFaultTree_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
spares18: BinaryAssociation = BinaryAssociation(
    name="spares18",
    ends={
        Property(name="dynamicFaultTree_Event", type=dynamicFaultTree_Spare, multiplicity=Multiplicity(1, 1)),
        Property(name="dynamicFaultTree_Spare", type=dynamicFaultTree_Event, multiplicity=Multiplicity(0, 9999))
    }
)
events16: BinaryAssociation = BinaryAssociation(
    name="events16",
    ends={
        Property(name="Event17", type=dynamicFaultTree_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="dependency", type=dynamicFaultTree_Event, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_dynamicFaultTree_TopLevelEvent_Element = Generalization(general=Element, specific=dynamicFaultTree_TopLevelEvent)
gen_dynamicFaultTree_Gate_Element = Generalization(general=Element, specific=dynamicFaultTree_Gate)
gen_dynamicFaultTree_Event_Element = Generalization(general=Element, specific=dynamicFaultTree_Event)
gen_dynamicFaultTree_Sequence_Dependency = Generalization(general=Dependency, specific=dynamicFaultTree_Sequence)
gen_dynamicFaultTree_FunctionalDependency_Dependency = Generalization(general=Dependency, specific=dynamicFaultTree_FunctionalDependency)
gen_dynamicFaultTree_AND_Gate = Generalization(general=Gate, specific=dynamicFaultTree_AND)
gen_dynamicFaultTree_PAND_Gate = Generalization(general=Gate, specific=dynamicFaultTree_PAND)
gen_dynamicFaultTree_OR_Gate = Generalization(general=Gate, specific=dynamicFaultTree_OR)
gen_dynamicFaultTree_POR_Gate = Generalization(general=Gate, specific=dynamicFaultTree_POR)
gen_dynamicFaultTree_XOR_Gate = Generalization(general=Gate, specific=dynamicFaultTree_XOR)
gen_dynamicFaultTree_Spare_Gate = Generalization(general=Gate, specific=dynamicFaultTree_Spare)
gen_dynamicFaultTree_Dependency_Element = Generalization(general=Element, specific=dynamicFaultTree_Dependency)

# Domain Model
domain_model = DomainModel(
    name="dynamicFaultTree",
    types={dynamicFaultTree_DFT, dynamicFaultTree_TopLevelEvent, dynamicFaultTree_Dependency, dynamicFaultTree_Element, Element, dynamicFaultTree_Gate, dynamicFaultTree_Event, dynamicFaultTree_FunctionalDependency, dynamicFaultTree_AND, Gate, dynamicFaultTree_PAND, dynamicFaultTree_OR, dynamicFaultTree_POR, dynamicFaultTree_XOR, dynamicFaultTree_Spare, dynamicFaultTree_Sequence, Dependency},
    associations={topLevelEvent0, dependencies1, gate3, toplevelevent4, childGate6, parentGate9, childEvent11, parentGate13, dependency15, spares18, events16},
    generalizations={gen_dynamicFaultTree_TopLevelEvent_Element, gen_dynamicFaultTree_Gate_Element, gen_dynamicFaultTree_Event_Element, gen_dynamicFaultTree_Sequence_Dependency, gen_dynamicFaultTree_FunctionalDependency_Dependency, gen_dynamicFaultTree_AND_Gate, gen_dynamicFaultTree_PAND_Gate, gen_dynamicFaultTree_OR_Gate, gen_dynamicFaultTree_POR_Gate, gen_dynamicFaultTree_XOR_Gate, gen_dynamicFaultTree_Spare_Gate, gen_dynamicFaultTree_Dependency_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)