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
ptn103_AbstractNode = Class(name="ptn103::AbstractNode", is_abstract=True)
ptn103_AbstractTransition = Class(name="ptn103::AbstractTransition", is_abstract=True)
ptn103_Token = Class(name="ptn103::Token")
ptn103_Place = Class(name="ptn103::Place")
AbstractNode = Class(name="AbstractNode")
ptn103_Transition = Class(name="ptn103::Transition")
AbstractTransition = Class(name="AbstractTransition")

# ptn103_AbstractNode class attributes and methods
ptn103_AbstractNode_name: Property = Property(name="name", type=StringType)
ptn103_AbstractNode.attributes={ptn103_AbstractNode_name}

# ptn103_AbstractTransition class attributes and methods
ptn103_AbstractTransition_guard: Property = Property(name="guard", type=StringType)
ptn103_AbstractTransition.attributes={ptn103_AbstractTransition_guard}

# ptn103_Token class attributes and methods

# ptn103_Place class attributes and methods

# AbstractNode class attributes and methods

# ptn103_Transition class attributes and methods

# AbstractTransition class attributes and methods

# Relationships
subnets1: BinaryAssociation = BinaryAssociation(
    name="subnets1",
    ends={
        Property(name="ptn103_Place", type=ptn103_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="ptn103_Place0", type=ptn103_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes2: BinaryAssociation = BinaryAssociation(
    name="nodes2",
    ends={
        Property(name="ptn103_AbstractNode", type=ptn103_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="ptn103_Place3", type=ptn103_AbstractNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions4: BinaryAssociation = BinaryAssociation(
    name="transitions4",
    ends={
        Property(name="ptn103_AbstractTransition", type=ptn103_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="ptn103_Place5", type=ptn103_AbstractTransition, multiplicity=Multiplicity(0, 9999))
    }
)
tokens6: BinaryAssociation = BinaryAssociation(
    name="tokens6",
    ends={
        Property(name="ptn103_Token", type=ptn103_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="ptn103_Place7", type=ptn103_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
places8: BinaryAssociation = BinaryAssociation(
    name="places8",
    ends={
        Property(name="ptn103_Place10", type=ptn103_AbstractTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="ptn103_AbstractTransition9", type=ptn103_Place, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_ptn103_AbstractTransition_AbstractNode = Generalization(general=AbstractNode, specific=ptn103_AbstractTransition)
gen_ptn103_Place_AbstractNode = Generalization(general=AbstractNode, specific=ptn103_Place)
gen_ptn103_Transition_AbstractTransition = Generalization(general=AbstractTransition, specific=ptn103_Transition)

# Domain Model
domain_model = DomainModel(
    name="ptn103",
    types={ptn103_AbstractNode, ptn103_AbstractTransition, ptn103_Token, ptn103_Place, AbstractNode, ptn103_Transition, AbstractTransition},
    associations={subnets1, nodes2, transitions4, tokens6, places8},
    generalizations={gen_ptn103_AbstractTransition_AbstractNode, gen_ptn103_Place_AbstractNode, gen_ptn103_Transition_AbstractTransition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)