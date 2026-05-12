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
pETRI_PetriNetElement = Class(name="pETRI_PetriNetElement")
pETRI_Node = Class(name="pETRI_Node")
PetriNetElement = Class(name="PetriNetElement")
pETRI_PetriNet = Class(name="pETRI_PetriNet")
pETRI_Place = Class(name="pETRI_Place")
Node = Class(name="Node")
pETRI_Transition = Class(name="pETRI_Transition")
pETRI_Arc = Class(name="pETRI_Arc")

# pETRI_PetriNetElement class attributes and methods

# pETRI_Node class attributes and methods
pETRI_Node_name: Property = Property(name="name", type=StringType)
pETRI_Node.attributes={pETRI_Node_name}

# PetriNetElement class attributes and methods

# pETRI_PetriNet class attributes and methods
pETRI_PetriNet_name: Property = Property(name="name", type=StringType)
pETRI_PetriNet.attributes={pETRI_PetriNet_name}

# pETRI_Place class attributes and methods
pETRI_Place_marking: Property = Property(name="marking", type=IntegerType)
pETRI_Place.attributes={pETRI_Place_marking}

# Node class attributes and methods

# pETRI_Transition class attributes and methods

# pETRI_Arc class attributes and methods
pETRI_Arc_multiplicity: Property = Property(name="multiplicity", type=IntegerType)
pETRI_Arc_readOnly: Property = Property(name="readOnly", type=BooleanType)
pETRI_Arc.attributes={pETRI_Arc_readOnly, pETRI_Arc_multiplicity}

# Relationships
petriNetElements0: BinaryAssociation = BinaryAssociation(
    name="petriNetElements0",
    ends={
        Property(name="pETRI_PetriNetElement", type=pETRI_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="pETRI_PetriNet", type=pETRI_PetriNetElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
predecessor1: BinaryAssociation = BinaryAssociation(
    name="predecessor1",
    ends={
        Property(name="pETRI_Node", type=pETRI_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="pETRI_Arc", type=pETRI_Node, multiplicity=Multiplicity(0, 1))
    }
)
successor2: BinaryAssociation = BinaryAssociation(
    name="successor2",
    ends={
        Property(name="pETRI_Node4", type=pETRI_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="pETRI_Arc3", type=pETRI_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_pETRI_Node_PetriNetElement = Generalization(general=PetriNetElement, specific=pETRI_Node)
gen_pETRI_Arc_PetriNetElement = Generalization(general=PetriNetElement, specific=pETRI_Arc)
gen_pETRI_Place_Node = Generalization(general=Node, specific=pETRI_Place)
gen_pETRI_Transition_Node = Generalization(general=Node, specific=pETRI_Transition)

# Domain Model
domain_model = DomainModel(
    name="pETRI",
    types={pETRI_PetriNetElement, pETRI_Node, PetriNetElement, pETRI_PetriNet, pETRI_Place, Node, pETRI_Transition, pETRI_Arc},
    associations={petriNetElements0, predecessor1, successor2},
    generalizations={gen_pETRI_Node_PetriNetElement, gen_pETRI_Arc_PetriNetElement, gen_pETRI_Place_Node, gen_pETRI_Transition_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)