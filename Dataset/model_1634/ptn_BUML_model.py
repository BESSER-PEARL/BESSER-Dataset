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
ptn_Place = Class(name="ptn::Place")
AbstractNode = Class(name="AbstractNode")
ptn_Token = Class(name="ptn::Token")
ptn_AbstractNode = Class(name="ptn::AbstractNode", is_abstract=True)
ptn_AbstractTransition = Class(name="ptn::AbstractTransition", is_abstract=True)
ptn_Transition = Class(name="ptn::Transition")
AbstractTransition = Class(name="AbstractTransition")

# ptn_Place class attributes and methods

# AbstractNode class attributes and methods

# ptn_Token class attributes and methods

# ptn_AbstractNode class attributes and methods
ptn_AbstractNode_name: Property = Property(name="name", type=StringType)
ptn_AbstractNode_tMin: Property = Property(name="tMin", type=IntegerType)
ptn_AbstractNode_tMax: Property = Property(name="tMax", type=IntegerType)
ptn_AbstractNode.attributes={ptn_AbstractNode_name, ptn_AbstractNode_tMax, ptn_AbstractNode_tMin}

# ptn_AbstractTransition class attributes and methods
ptn_AbstractTransition_guard: Property = Property(name="guard", type=StringType)
ptn_AbstractTransition.attributes={ptn_AbstractTransition_guard}

# ptn_Transition class attributes and methods
ptn_Transition_weight: Property = Property(name="weight", type=IntegerType)
ptn_Transition.attributes={ptn_Transition_weight}

# AbstractTransition class attributes and methods

# Relationships
tokens6: BinaryAssociation = BinaryAssociation(
    name="tokens6",
    ends={
        Property(name="ptn_Token", type=ptn_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="ptn_Place7", type=ptn_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subnets1: BinaryAssociation = BinaryAssociation(
    name="subnets1",
    ends={
        Property(name="ptn_Place", type=ptn_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="ptn_Place0", type=ptn_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes2: BinaryAssociation = BinaryAssociation(
    name="nodes2",
    ends={
        Property(name="ptn_AbstractNode", type=ptn_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="ptn_Place3", type=ptn_AbstractNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions4: BinaryAssociation = BinaryAssociation(
    name="transitions4",
    ends={
        Property(name="ptn_AbstractTransition", type=ptn_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="ptn_Place5", type=ptn_AbstractTransition, multiplicity=Multiplicity(0, 9999))
    }
)
places8: BinaryAssociation = BinaryAssociation(
    name="places8",
    ends={
        Property(name="ptn_Place10", type=ptn_AbstractTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="ptn_AbstractTransition9", type=ptn_Place, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_ptn_Place_AbstractNode = Generalization(general=AbstractNode, specific=ptn_Place)
gen_ptn_AbstractTransition_AbstractNode = Generalization(general=AbstractNode, specific=ptn_AbstractTransition)
gen_ptn_Transition_AbstractTransition = Generalization(general=AbstractTransition, specific=ptn_Transition)

# Domain Model
domain_model = DomainModel(
    name="ptn",
    types={ptn_Place, AbstractNode, ptn_Token, ptn_AbstractNode, ptn_AbstractTransition, ptn_Transition, AbstractTransition},
    associations={tokens6, subnets1, nodes2, transitions4, places8},
    generalizations={gen_ptn_Place_AbstractNode, gen_ptn_AbstractTransition_AbstractNode, gen_ptn_Transition_AbstractTransition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)