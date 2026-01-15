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
PetrinetDSL_Petrinet = Class(name="PetrinetDSL::Petrinet")
PetrinetDSL_Node = Class(name="PetrinetDSL::Node")
Petrinet = Class(name="Petrinet")
PetrinetDSL_Edge = Class(name="PetrinetDSL::Edge")
PetrinetDSL_Token = Class(name="PetrinetDSL::Token")
Node = Class(name="Node")
PetrinetDSL_Transition = Class(name="PetrinetDSL::Transition")
PetrinetDSL_Place = Class(name="PetrinetDSL::Place")
PetrinetDSL_TPEdge = Class(name="PetrinetDSL::TPEdge")
PetrinetDSL_PTEdge = Class(name="PetrinetDSL::PTEdge")
Edge = Class(name="Edge")

# PetrinetDSL_Petrinet class attributes and methods
PetrinetDSL_Petrinet_name: Property = Property(name="name", type=StringType)
PetrinetDSL_Petrinet_description: Property = Property(name="description", type=StringType)
PetrinetDSL_Petrinet.attributes={PetrinetDSL_Petrinet_description, PetrinetDSL_Petrinet_name}

# PetrinetDSL_Node class attributes and methods

# Petrinet class attributes and methods

# PetrinetDSL_Edge class attributes and methods

# PetrinetDSL_Token class attributes and methods

# Node class attributes and methods

# PetrinetDSL_Transition class attributes and methods

# PetrinetDSL_Place class attributes and methods

# PetrinetDSL_TPEdge class attributes and methods

# PetrinetDSL_PTEdge class attributes and methods

# Edge class attributes and methods

# Relationships
mapelements1: BinaryAssociation = BinaryAssociation(
    name="mapelements1",
    ends={
        Property(name="PetrinetDSL_Petrinet", type=PetrinetDSL_Petrinet, multiplicity=Multiplicity(1, 1)),
        Property(name="PetrinetDSL_Petrinet0", type=PetrinetDSL_Petrinet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fromPlace3: BinaryAssociation = BinaryAssociation(
    name="fromPlace3",
    ends={
        Property(name="PetrinetDSL_Place4", type=PetrinetDSL_PTEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="PetrinetDSL_PTEdge", type=PetrinetDSL_Place, multiplicity=Multiplicity(0, 1))
    }
)
toTransition5: BinaryAssociation = BinaryAssociation(
    name="toTransition5",
    ends={
        Property(name="PetrinetDSL_Transition", type=PetrinetDSL_PTEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="PetrinetDSL_PTEdge6", type=PetrinetDSL_Transition, multiplicity=Multiplicity(0, 1))
    }
)
fromTransition7: BinaryAssociation = BinaryAssociation(
    name="fromTransition7",
    ends={
        Property(name="PetrinetDSL_Transition8", type=PetrinetDSL_TPEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="PetrinetDSL_TPEdge", type=PetrinetDSL_Transition, multiplicity=Multiplicity(0, 1))
    }
)
toPlace9: BinaryAssociation = BinaryAssociation(
    name="toPlace9",
    ends={
        Property(name="PetrinetDSL_Place11", type=PetrinetDSL_TPEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="PetrinetDSL_TPEdge10", type=PetrinetDSL_Place, multiplicity=Multiplicity(0, 1))
    }
)
tokens2: BinaryAssociation = BinaryAssociation(
    name="tokens2",
    ends={
        Property(name="PetrinetDSL_Token", type=PetrinetDSL_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="PetrinetDSL_Place", type=PetrinetDSL_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_PetrinetDSL_Node_Petrinet = Generalization(general=Petrinet, specific=PetrinetDSL_Node)
gen_PetrinetDSL_Edge_Petrinet = Generalization(general=Petrinet, specific=PetrinetDSL_Edge)
gen_PetrinetDSL_Token_Node = Generalization(general=Node, specific=PetrinetDSL_Token)
gen_PetrinetDSL_Transition_Node = Generalization(general=Node, specific=PetrinetDSL_Transition)
gen_PetrinetDSL_Place_Node = Generalization(general=Node, specific=PetrinetDSL_Place)
gen_PetrinetDSL_TPEdge_Edge = Generalization(general=Edge, specific=PetrinetDSL_TPEdge)
gen_PetrinetDSL_PTEdge_Edge = Generalization(general=Edge, specific=PetrinetDSL_PTEdge)

# Domain Model
domain_model = DomainModel(
    name="PetrinetDSL",
    types={PetrinetDSL_Petrinet, PetrinetDSL_Node, Petrinet, PetrinetDSL_Edge, PetrinetDSL_Token, Node, PetrinetDSL_Transition, PetrinetDSL_Place, PetrinetDSL_TPEdge, PetrinetDSL_PTEdge, Edge},
    associations={mapelements1, fromPlace3, toTransition5, fromTransition7, toPlace9, tokens2},
    generalizations={gen_PetrinetDSL_Node_Petrinet, gen_PetrinetDSL_Edge_Petrinet, gen_PetrinetDSL_Token_Node, gen_PetrinetDSL_Transition_Node, gen_PetrinetDSL_Place_Node, gen_PetrinetDSL_TPEdge_Edge, gen_PetrinetDSL_PTEdge_Edge},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)