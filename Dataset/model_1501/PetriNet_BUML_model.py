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
PetriNet_PetriNode = Class(name="PetriNet::PetriNode")
PetriModel = Class(name="PetriModel")
PetriNet_Place = Class(name="PetriNet::Place")
PetriNode = Class(name="PetriNode")
PetriNet_Token = Class(name="PetriNet::Token")
PetriNet_PetriModel = Class(name="PetriNet::PetriModel")
PetriNet_PetriEdge = Class(name="PetriNet::PetriEdge")
PetriNet_Transition = Class(name="PetriNet::Transition")
PetriNet_Arc = Class(name="PetriNet::Arc")
PetriEdge = Class(name="PetriEdge")

# PetriNet_PetriNode class attributes and methods

# PetriModel class attributes and methods

# PetriNet_Place class attributes and methods

# PetriNode class attributes and methods

# PetriNet_Token class attributes and methods

# PetriNet_PetriModel class attributes and methods
PetriNet_PetriModel_name: Property = Property(name="name", type=StringType)
PetriNet_PetriModel_description: Property = Property(name="description", type=StringType)
PetriNet_PetriModel.attributes={PetriNet_PetriModel_name, PetriNet_PetriModel_description}

# PetriNet_PetriEdge class attributes and methods

# PetriNet_Transition class attributes and methods

# PetriNet_Arc class attributes and methods

# PetriEdge class attributes and methods

# Relationships
token0: BinaryAssociation = BinaryAssociation(
    name="token0",
    ends={
        Property(name="PetriNet_Token", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Place", type=PetriNet_Token, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
petriFrom2: BinaryAssociation = BinaryAssociation(
    name="petriFrom2",
    ends={
        Property(name="PetriNet_PetriNode3", type=PetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Arc", type=PetriNet_PetriNode, multiplicity=Multiplicity(0, 1))
    }
)
petriTo4: BinaryAssociation = BinaryAssociation(
    name="petriTo4",
    ends={
        Property(name="PetriNet_PetriNode6", type=PetriNet_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Arc5", type=PetriNet_PetriNode, multiplicity=Multiplicity(0, 1))
    }
)
petriModels8: BinaryAssociation = BinaryAssociation(
    name="petriModels8",
    ends={
        Property(name="PetriNet_PetriModel", type=PetriNet_PetriModel, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_PetriModel7", type=PetriNet_PetriModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
test1: BinaryAssociation = BinaryAssociation(
    name="test1",
    ends={
        Property(name="PetriNet_PetriNode", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="PetriNet_Transition", type=PetriNet_PetriNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_PetriNet_PetriNode_PetriModel = Generalization(general=PetriModel, specific=PetriNet_PetriNode)
gen_PetriNet_Place_PetriNode = Generalization(general=PetriNode, specific=PetriNet_Place)
gen_PetriNet_PetriEdge_PetriModel = Generalization(general=PetriModel, specific=PetriNet_PetriEdge)
gen_PetriNet_Token_PetriNode = Generalization(general=PetriNode, specific=PetriNet_Token)
gen_PetriNet_Transition_PetriNode = Generalization(general=PetriNode, specific=PetriNet_Transition)
gen_PetriNet_Arc_PetriEdge = Generalization(general=PetriEdge, specific=PetriNet_Arc)

# Domain Model
domain_model = DomainModel(
    name="PetriNet",
    types={PetriNet_PetriNode, PetriModel, PetriNet_Place, PetriNode, PetriNet_Token, PetriNet_PetriModel, PetriNet_PetriEdge, PetriNet_Transition, PetriNet_Arc, PetriEdge},
    associations={token0, petriFrom2, petriTo4, petriModels8, test1},
    generalizations={gen_PetriNet_PetriNode_PetriModel, gen_PetriNet_Place_PetriNode, gen_PetriNet_PetriEdge_PetriModel, gen_PetriNet_Token_PetriNode, gen_PetriNet_Transition_PetriNode, gen_PetriNet_Arc_PetriEdge},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)