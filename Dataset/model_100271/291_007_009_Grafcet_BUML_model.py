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
Grafcet_Grafcet = Class(name="Grafcet_Grafcet")
NamedElement = Class(name="NamedElement")
Element = Class(name="Element")
Grafcet_LocatedElement = Class(name="Grafcet_LocatedElement", is_abstract=True)
Grafcet_NamedElement = Class(name="Grafcet_NamedElement", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
Grafcet = Class(name="Grafcet")
Grafcet_Step = Class(name="Grafcet_Step")
Connection = Class(name="Connection")
Grafcet_Element = Class(name="Grafcet_Element", is_abstract=True)
Grafcet_Transition = Class(name="Grafcet_Transition")
TransitionToStep = Class(name="TransitionToStep")
StepToTransition = Class(name="StepToTransition")
Grafcet_StepToTransition = Class(name="Grafcet_StepToTransition")
Step = Class(name="Step")
Grafcet_Connection = Class(name="Grafcet_Connection", is_abstract=True)
Transition = Class(name="Transition")
Grafcet_TransitionToStep = Class(name="Grafcet_TransitionToStep")

# Grafcet_Grafcet class attributes and methods

# NamedElement class attributes and methods

# Element class attributes and methods

# Grafcet_LocatedElement class attributes and methods
Grafcet_LocatedElement_location: Property = Property(name="location", type=StringType)
Grafcet_LocatedElement.attributes={Grafcet_LocatedElement_location}

# Grafcet_NamedElement class attributes and methods
Grafcet_NamedElement_name: Property = Property(name="name", type=StringType)
Grafcet_NamedElement.attributes={Grafcet_NamedElement_name}

# LocatedElement class attributes and methods

# Grafcet class attributes and methods

# Grafcet_Step class attributes and methods
Grafcet_Step_isInitial: Property = Property(name="isInitial", type=StringType)
Grafcet_Step_isActive: Property = Property(name="isActive", type=StringType)
Grafcet_Step_action: Property = Property(name="action", type=StringType)
Grafcet_Step.attributes={Grafcet_Step_isInitial, Grafcet_Step_isActive, Grafcet_Step_action}

# Connection class attributes and methods

# Grafcet_Element class attributes and methods

# Grafcet_Transition class attributes and methods
Grafcet_Transition_condition: Property = Property(name="condition", type=StringType)
Grafcet_Transition.attributes={Grafcet_Transition_condition}

# TransitionToStep class attributes and methods

# StepToTransition class attributes and methods

# Grafcet_StepToTransition class attributes and methods

# Step class attributes and methods

# Grafcet_Connection class attributes and methods

# Transition class attributes and methods

# Grafcet_TransitionToStep class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="Element", type=Grafcet_Grafcet, multiplicity=Multiplicity(1, 1)),
        Property(name="grafcet", type=Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
grafcet3: BinaryAssociation = BinaryAssociation(
    name="grafcet3",
    ends={
        Property(name="Grafcet", type=Grafcet_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=Grafcet, multiplicity=Multiplicity(1, 1))
    }
)
connections1: BinaryAssociation = BinaryAssociation(
    name="connections1",
    ends={
        Property(name="Connection", type=Grafcet_Grafcet, multiplicity=Multiplicity(1, 1)),
        Property(name="grafcet2", type=Connection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoingConnections5: BinaryAssociation = BinaryAssociation(
    name="outgoingConnections5",
    ends={
        Property(name="StepToTransition", type=Grafcet_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="from_", type=StepToTransition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingConnections4: BinaryAssociation = BinaryAssociation(
    name="incomingConnections4",
    ends={
        Property(name="TransitionToStep", type=Grafcet_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=TransitionToStep, multiplicity=Multiplicity(0, 9999))
    }
)
grafcet12: BinaryAssociation = BinaryAssociation(
    name="grafcet12",
    ends={
        Property(name="Grafcet13", type=Grafcet_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="connections", type=Grafcet, multiplicity=Multiplicity(1, 1))
    }
)
from_14: BinaryAssociation = BinaryAssociation(
    name="from_14",
    ends={
        Property(name="Step", type=Grafcet_StepToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingConnections", type=Step, multiplicity=Multiplicity(1, 1))
    }
)
incomingConnections6: BinaryAssociation = BinaryAssociation(
    name="incomingConnections6",
    ends={
        Property(name="StepToTransition8", type=Grafcet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="to7", type=StepToTransition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingConnections9: BinaryAssociation = BinaryAssociation(
    name="outgoingConnections9",
    ends={
        Property(name="TransitionToStep11", type=Grafcet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="from_10", type=TransitionToStep, multiplicity=Multiplicity(0, 9999))
    }
)
to19: BinaryAssociation = BinaryAssociation(
    name="to19",
    ends={
        Property(name="Step21", type=Grafcet_TransitionToStep, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingConnections20", type=Step, multiplicity=Multiplicity(1, 1))
    }
)
to15: BinaryAssociation = BinaryAssociation(
    name="to15",
    ends={
        Property(name="Transition", type=Grafcet_StepToTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingConnections", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)
from_16: BinaryAssociation = BinaryAssociation(
    name="from_16",
    ends={
        Property(name="Transition18", type=Grafcet_TransitionToStep, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingConnections17", type=Transition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Grafcet_Grafcet_NamedElement = Generalization(general=NamedElement, specific=Grafcet_Grafcet)
gen_Grafcet_NamedElement_LocatedElement = Generalization(general=LocatedElement, specific=Grafcet_NamedElement)
gen_Grafcet_Step_Element = Generalization(general=Element, specific=Grafcet_Step)
gen_Grafcet_Element_NamedElement = Generalization(general=NamedElement, specific=Grafcet_Element)
gen_Grafcet_Transition_Element = Generalization(general=Element, specific=Grafcet_Transition)
gen_Grafcet_StepToTransition_Connection = Generalization(general=Connection, specific=Grafcet_StepToTransition)
gen_Grafcet_Connection_NamedElement = Generalization(general=NamedElement, specific=Grafcet_Connection)
gen_Grafcet_TransitionToStep_Connection = Generalization(general=Connection, specific=Grafcet_TransitionToStep)

# Domain Model
domain_model = DomainModel(
    name="Grafcet",
    types={Grafcet_Grafcet, NamedElement, Element, Grafcet_LocatedElement, Grafcet_NamedElement, LocatedElement, Grafcet, Grafcet_Step, Connection, Grafcet_Element, Grafcet_Transition, TransitionToStep, StepToTransition, Grafcet_StepToTransition, Step, Grafcet_Connection, Transition, Grafcet_TransitionToStep},
    associations={elements0, grafcet3, connections1, outgoingConnections5, incomingConnections4, grafcet12, from_14, incomingConnections6, outgoingConnections9, to19, to15, from_16},
    generalizations={gen_Grafcet_Grafcet_NamedElement, gen_Grafcet_NamedElement_LocatedElement, gen_Grafcet_Step_Element, gen_Grafcet_Element_NamedElement, gen_Grafcet_Transition_Element, gen_Grafcet_StepToTransition_Connection, gen_Grafcet_Connection_NamedElement, gen_Grafcet_TransitionToStep_Connection},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)