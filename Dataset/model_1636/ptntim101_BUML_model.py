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
ptntim101_Place = Class(name="ptntim101_Place")
ptntim101_AbstractNode = Class(name="ptntim101_AbstractNode", is_abstract=True)
ptntim101_AbstractTransition = Class(name="ptntim101_AbstractTransition", is_abstract=True)
ptntim101_Token = Class(name="ptntim101_Token")
AbstractNode = Class(name="AbstractNode")
ptntim101_Transition = Class(name="ptntim101_Transition")
AbstractTransition = Class(name="AbstractTransition")

# ptntim101_Place class attributes and methods

# ptntim101_AbstractNode class attributes and methods
ptntim101_AbstractNode_name: Property = Property(name="name", type=StringType)
ptntim101_AbstractNode_tMin: Property = Property(name="tMin", type=IntegerType)
ptntim101_AbstractNode_tMax: Property = Property(name="tMax", type=IntegerType)
ptntim101_AbstractNode.attributes={ptntim101_AbstractNode_tMax, ptntim101_AbstractNode_name, ptntim101_AbstractNode_tMin}

# ptntim101_AbstractTransition class attributes and methods
ptntim101_AbstractTransition_guard: Property = Property(name="guard", type=StringType)
ptntim101_AbstractTransition.attributes={ptntim101_AbstractTransition_guard}

# ptntim101_Token class attributes and methods

# AbstractNode class attributes and methods

# ptntim101_Transition class attributes and methods
ptntim101_Transition_weight: Property = Property(name="weight", type=IntegerType)
ptntim101_Transition.attributes={ptntim101_Transition_weight}

# AbstractTransition class attributes and methods

# Relationships
subnets1: BinaryAssociation = BinaryAssociation(
    name="subnets1",
    ends={
        Property(name="ptntim101_Place", type=ptntim101_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="ptntim101_Place0", type=ptntim101_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes2: BinaryAssociation = BinaryAssociation(
    name="nodes2",
    ends={
        Property(name="ptntim101_AbstractNode", type=ptntim101_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="ptntim101_Place3", type=ptntim101_AbstractNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions4: BinaryAssociation = BinaryAssociation(
    name="transitions4",
    ends={
        Property(name="ptntim101_AbstractTransition", type=ptntim101_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="ptntim101_Place5", type=ptntim101_AbstractTransition, multiplicity=Multiplicity(0, 9999))
    }
)
tokens6: BinaryAssociation = BinaryAssociation(
    name="tokens6",
    ends={
        Property(name="ptntim101_Token", type=ptntim101_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="ptntim101_Place7", type=ptntim101_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
places8: BinaryAssociation = BinaryAssociation(
    name="places8",
    ends={
        Property(name="ptntim101_Place10", type=ptntim101_AbstractTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="ptntim101_AbstractTransition9", type=ptntim101_Place, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_ptntim101_Place_AbstractNode = Generalization(general=AbstractNode, specific=ptntim101_Place)
gen_ptntim101_Transition_AbstractTransition = Generalization(general=AbstractTransition, specific=ptntim101_Transition)
gen_ptntim101_AbstractTransition_AbstractNode = Generalization(general=AbstractNode, specific=ptntim101_AbstractTransition)

# Domain Model
domain_model = DomainModel(
    name="ptntim101",
    types={ptntim101_Place, ptntim101_AbstractNode, ptntim101_AbstractTransition, ptntim101_Token, AbstractNode, ptntim101_Transition, AbstractTransition},
    associations={subnets1, nodes2, transitions4, tokens6, places8},
    generalizations={gen_ptntim101_Place_AbstractNode, gen_ptntim101_Transition_AbstractTransition, gen_ptntim101_AbstractTransition_AbstractNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)