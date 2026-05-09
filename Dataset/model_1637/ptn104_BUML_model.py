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
ptn104_Place = Class(name="ptn104_Place")
AbstractNode = Class(name="AbstractNode")
ptn104_AbstractNode = Class(name="ptn104_AbstractNode", is_abstract=True)
ptn104_AbstractTransition = Class(name="ptn104_AbstractTransition", is_abstract=True)
ptn104_Token = Class(name="ptn104_Token")
ptn104_Or = Class(name="ptn104_Or")
AbstractTransition = Class(name="AbstractTransition")
ptn104_And = Class(name="ptn104_And")

# ptn104_Place class attributes and methods

# AbstractNode class attributes and methods

# ptn104_AbstractNode class attributes and methods
ptn104_AbstractNode_name: Property = Property(name="name", type=StringType)
ptn104_AbstractNode.attributes={ptn104_AbstractNode_name}

# ptn104_AbstractTransition class attributes and methods
ptn104_AbstractTransition_guard: Property = Property(name="guard", type=StringType)
ptn104_AbstractTransition.attributes={ptn104_AbstractTransition_guard}

# ptn104_Token class attributes and methods

# ptn104_Or class attributes and methods

# AbstractTransition class attributes and methods

# ptn104_And class attributes and methods

# Relationships
subnets1: BinaryAssociation = BinaryAssociation(
    name="subnets1",
    ends={
        Property(name="ptn104_Place", type=ptn104_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="ptn104_Place0", type=ptn104_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes2: BinaryAssociation = BinaryAssociation(
    name="nodes2",
    ends={
        Property(name="ptn104_AbstractNode", type=ptn104_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="ptn104_Place3", type=ptn104_AbstractNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions4: BinaryAssociation = BinaryAssociation(
    name="transitions4",
    ends={
        Property(name="ptn104_AbstractTransition", type=ptn104_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="ptn104_Place5", type=ptn104_AbstractTransition, multiplicity=Multiplicity(0, 9999))
    }
)
tokens6: BinaryAssociation = BinaryAssociation(
    name="tokens6",
    ends={
        Property(name="ptn104_Token", type=ptn104_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="ptn104_Place7", type=ptn104_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
places8: BinaryAssociation = BinaryAssociation(
    name="places8",
    ends={
        Property(name="ptn104_Place10", type=ptn104_AbstractTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="ptn104_AbstractTransition9", type=ptn104_Place, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_ptn104_Place_AbstractNode = Generalization(general=AbstractNode, specific=ptn104_Place)
gen_ptn104_AbstractTransition_AbstractNode = Generalization(general=AbstractNode, specific=ptn104_AbstractTransition)
gen_ptn104_Or_AbstractTransition = Generalization(general=AbstractTransition, specific=ptn104_Or)
gen_ptn104_And_AbstractTransition = Generalization(general=AbstractTransition, specific=ptn104_And)

# Domain Model
domain_model = DomainModel(
    name="ptn104",
    types={ptn104_Place, AbstractNode, ptn104_AbstractNode, ptn104_AbstractTransition, ptn104_Token, ptn104_Or, AbstractTransition, ptn104_And},
    associations={subnets1, nodes2, transitions4, tokens6, places8},
    generalizations={gen_ptn104_Place_AbstractNode, gen_ptn104_AbstractTransition_AbstractNode, gen_ptn104_Or_AbstractTransition, gen_ptn104_And_AbstractTransition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)