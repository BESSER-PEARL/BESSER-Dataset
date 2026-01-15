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
pnw_NetElement = Class(name="pnw::NetElement", is_abstract=True)
pnw_NamedElement = Class(name="pnw::NamedElement", is_abstract=True)
pnw_Net = Class(name="pnw::Net")
NamedElement = Class(name="NamedElement")
pnw_Edge = Class(name="pnw::Edge", is_abstract=True)
pnw_Transition = Class(name="pnw::Transition")
NetElement = Class(name="NetElement")
pnw_TPEdge = Class(name="pnw::TPEdge")
pnw_PTEdge = Class(name="pnw::PTEdge")
pnw_Place = Class(name="pnw::Place")
Edge = Class(name="Edge")

# pnw_NetElement class attributes and methods

# pnw_NamedElement class attributes and methods
pnw_NamedElement_name: Property = Property(name="name", type=StringType)
pnw_NamedElement.attributes={pnw_NamedElement_name}

# pnw_Net class attributes and methods
pnw_Net_incrementalID: Property = Property(name="incrementalID", type=StringType)
pnw_Net.attributes={pnw_Net_incrementalID}

# NamedElement class attributes and methods

# pnw_Edge class attributes and methods
pnw_Edge_weight: Property = Property(name="weight", type=IntegerType)
pnw_Edge.attributes={pnw_Edge_weight}

# pnw_Transition class attributes and methods

# NetElement class attributes and methods

# pnw_TPEdge class attributes and methods

# pnw_PTEdge class attributes and methods

# pnw_Place class attributes and methods
pnw_Place_noOfTokens: Property = Property(name="noOfTokens", type=IntegerType)
pnw_Place.attributes={pnw_Place_noOfTokens}

# Edge class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="NetElement", type=pnw_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=pnw_NetElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net1: BinaryAssociation = BinaryAssociation(
    name="net1",
    ends={
        Property(name="Net", type=pnw_NetElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=pnw_Net, multiplicity=Multiplicity(1, 1))
    }
)
outTPEdges2: BinaryAssociation = BinaryAssociation(
    name="outTPEdges2",
    ends={
        Property(name="TPEdge", type=pnw_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="fromTransition", type=pnw_TPEdge, multiplicity=Multiplicity(0, 9999))
    }
)
inPTEdges3: BinaryAssociation = BinaryAssociation(
    name="inPTEdges3",
    ends={
        Property(name="PTEdge", type=pnw_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="toTransition", type=pnw_PTEdge, multiplicity=Multiplicity(0, 9999))
    }
)
outPTEdges4: BinaryAssociation = BinaryAssociation(
    name="outPTEdges4",
    ends={
        Property(name="PTEdge5", type=pnw_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="fromPlace", type=pnw_PTEdge, multiplicity=Multiplicity(0, 9999))
    }
)
inTPEdges6: BinaryAssociation = BinaryAssociation(
    name="inTPEdges6",
    ends={
        Property(name="TPEdge7", type=pnw_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="toPlace", type=pnw_TPEdge, multiplicity=Multiplicity(0, 9999))
    }
)
fromTransition8: BinaryAssociation = BinaryAssociation(
    name="fromTransition8",
    ends={
        Property(name="Transition", type=pnw_TPEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outTPEdges", type=pnw_Transition, multiplicity=Multiplicity(1, 1))
    }
)
toPlace9: BinaryAssociation = BinaryAssociation(
    name="toPlace9",
    ends={
        Property(name="Place", type=pnw_TPEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="inTPEdges", type=pnw_Place, multiplicity=Multiplicity(1, 1))
    }
)
fromPlace10: BinaryAssociation = BinaryAssociation(
    name="fromPlace10",
    ends={
        Property(name="Place11", type=pnw_PTEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="outPTEdges", type=pnw_Place, multiplicity=Multiplicity(1, 1))
    }
)
toTransition12: BinaryAssociation = BinaryAssociation(
    name="toTransition12",
    ends={
        Property(name="Transition13", type=pnw_PTEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="inPTEdges", type=pnw_Transition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_pnw_Net_NamedElement = Generalization(general=NamedElement, specific=pnw_Net)
gen_pnw_Edge_NetElement = Generalization(general=NetElement, specific=pnw_Edge)
gen_pnw_Transition_NetElement = Generalization(general=NetElement, specific=pnw_Transition)
gen_pnw_Transition_NamedElement = Generalization(general=NamedElement, specific=pnw_Transition)
gen_pnw_Place_NetElement = Generalization(general=NetElement, specific=pnw_Place)
gen_pnw_Place_NamedElement = Generalization(general=NamedElement, specific=pnw_Place)
gen_pnw_TPEdge_Edge = Generalization(general=Edge, specific=pnw_TPEdge)
gen_pnw_PTEdge_Edge = Generalization(general=Edge, specific=pnw_PTEdge)

# Domain Model
domain_model = DomainModel(
    name="pnw",
    types={pnw_NetElement, pnw_NamedElement, pnw_Net, NamedElement, pnw_Edge, pnw_Transition, NetElement, pnw_TPEdge, pnw_PTEdge, pnw_Place, Edge},
    associations={elements0, net1, outTPEdges2, inPTEdges3, outPTEdges4, inTPEdges6, fromTransition8, toPlace9, fromPlace10, toTransition12},
    generalizations={gen_pnw_Net_NamedElement, gen_pnw_Edge_NetElement, gen_pnw_Transition_NetElement, gen_pnw_Transition_NamedElement, gen_pnw_Place_NetElement, gen_pnw_Place_NamedElement, gen_pnw_TPEdge_Edge, gen_pnw_PTEdge_Edge},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)