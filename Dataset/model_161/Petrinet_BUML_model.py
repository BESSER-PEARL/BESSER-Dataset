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
PetriNetModel_Transition = Class(name="PetriNetModel_Transition")
Node = Class(name="Node")
PetriNetModel_Place = Class(name="PetriNetModel_Place")
PetriNetModel_Token = Class(name="PetriNetModel_Token")
PetriNetModel_PetriNet = Class(name="PetriNetModel_PetriNet")
PetriNetModel_PObject = Class(name="PetriNetModel_PObject")
PetriNetModel_Node = Class(name="PetriNetModel_Node")
PObject = Class(name="PObject")
PetriNetModel_Arc = Class(name="PetriNetModel_Arc")

# PetriNetModel_Transition class attributes and methods

# Node class attributes and methods

# PetriNetModel_Place class attributes and methods

# PetriNetModel_Token class attributes and methods

# PetriNetModel_PetriNet class attributes and methods

# PetriNetModel_PObject class attributes and methods
PetriNetModel_PObject_id: Property = Property(name="id", type=IntegerType)
PetriNetModel_PObject.attributes={PetriNetModel_PObject_id}

# PetriNetModel_Node class attributes and methods
PetriNetModel_Node_name: Property = Property(name="name", type=StringType)
PetriNetModel_Node.attributes={PetriNetModel_Node_name}

# PObject class attributes and methods

# PetriNetModel_Arc class attributes and methods

# Relationships
in_2: BinaryAssociation = BinaryAssociation(
    name="in_2",
    ends={
        Property(name="Arc3", type=PetriNetModel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=PetriNetModel_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
tokens4: BinaryAssociation = BinaryAssociation(
    name="tokens4",
    ends={
        Property(name="PetriNetModel_Token", type=PetriNetModel_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNetModel_Place", type=PetriNetModel_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objects0: BinaryAssociation = BinaryAssociation(
    name="objects0",
    ends={
        Property(name="PetriNetModel_PObject", type=PetriNetModel_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNetModel_PetriNet", type=PetriNetModel_PObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
out1: BinaryAssociation = BinaryAssociation(
    name="out1",
    ends={
        Property(name="Arc", type=PetriNetModel_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=PetriNetModel_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
source5: BinaryAssociation = BinaryAssociation(
    name="source5",
    ends={
        Property(name="Node", type=PetriNetModel_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=PetriNetModel_Node, multiplicity=Multiplicity(1, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="Node7", type=PetriNetModel_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="in_", type=PetriNetModel_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_PetriNetModel_Transition_Node = Generalization(general=Node, specific=PetriNetModel_Transition)
gen_PetriNetModel_Place_Node = Generalization(general=Node, specific=PetriNetModel_Place)
gen_PetriNetModel_Node_PObject = Generalization(general=PObject, specific=PetriNetModel_Node)
gen_PetriNetModel_Arc_PObject = Generalization(general=PObject, specific=PetriNetModel_Arc)

# Domain Model
domain_model = DomainModel(
    name="PetriNetModel",
    types={PetriNetModel_Transition, Node, PetriNetModel_Place, PetriNetModel_Token, PetriNetModel_PetriNet, PetriNetModel_PObject, PetriNetModel_Node, PObject, PetriNetModel_Arc},
    associations={in_2, tokens4, objects0, out1, source5, target6},
    generalizations={gen_PetriNetModel_Transition_Node, gen_PetriNetModel_Place_Node, gen_PetriNetModel_Node_PObject, gen_PetriNetModel_Arc_PObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)