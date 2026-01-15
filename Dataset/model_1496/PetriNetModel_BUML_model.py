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
PetriNet_PetriNetRoot = Class(name="PetriNet::PetriNetRoot")
PetriNet_Element = Class(name="PetriNet::Element", is_abstract=True)
PetriNet_Transition = Class(name="PetriNet::Transition")
PetriNet_Arc = Class(name="PetriNet::Arc")
PetriNet_Place = Class(name="PetriNet::Place")
Element = Class(name="Element")

# PetriNet_PetriNetRoot class attributes and methods

# PetriNet_Element class attributes and methods
PetriNet_Element_name: Property = Property(name="name", type=StringType)
PetriNet_Element.attributes={PetriNet_Element_name}

# PetriNet_Transition class attributes and methods
PetriNet_Transition_minTime: Property = Property(name="minTime", type=IntegerType)
PetriNet_Transition_maxTime: Property = Property(name="maxTime", type=IntegerType)
PetriNet_Transition.attributes={PetriNet_Transition_minTime, PetriNet_Transition_maxTime}

# PetriNet_Arc class attributes and methods

# PetriNet_Place class attributes and methods
PetriNet_Place_Tokens: Property = Property(name="Tokens", type=IntegerType)
PetriNet_Place.attributes={PetriNet_Place_Tokens}

# Element class attributes and methods

# Relationships
In3: BinaryAssociation = BinaryAssociation(
    name="In3",
    ends={
        Property(name="PetriNet_Element5", type=PetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Arc4", type=PetriNet_Element, multiplicity=Multiplicity(1, 1))
    }
)
Out6: BinaryAssociation = BinaryAssociation(
    name="Out6",
    ends={
        Property(name="PetriNet_Element8", type=PetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Arc7", type=PetriNet_Element, multiplicity=Multiplicity(1, 1))
    }
)
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="PetriNet_Element", type=PetriNet_PetriNetRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNetRoot", type=PetriNet_Element, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="PetriNet_Arc", type=PetriNet_PetriNetRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriNetRoot2", type=PetriNet_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_PetriNet_Transition_Element = Generalization(general=Element, specific=PetriNet_Transition)
gen_PetriNet_Place_Element = Generalization(general=Element, specific=PetriNet_Place)

# Domain Model
domain_model = DomainModel(
    name="PetriNet",
    types={PetriNet_PetriNetRoot, PetriNet_Element, PetriNet_Transition, PetriNet_Arc, PetriNet_Place, Element},
    associations={In3, Out6, elements0, arcs1},
    generalizations={gen_PetriNet_Transition_Element, gen_PetriNet_Place_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)