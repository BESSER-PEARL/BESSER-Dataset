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
kiamaas_Top = Class(name="kiamaas::Top")
kiamaas_Node = Class(name="kiamaas::Node", is_abstract=True)
kiamaas_Plus = Class(name="kiamaas::Plus")
Node = Class(name="Node")
kiamaas_Num = Class(name="kiamaas::Num")

# kiamaas_Top class attributes and methods

# kiamaas_Node class attributes and methods
kiamaas_Node_height: Property = Property(name="height", type=IntegerType)
kiamaas_Node_deep: Property = Property(name="deep", type=IntegerType)
kiamaas_Node.attributes={kiamaas_Node_deep, kiamaas_Node_height}

# kiamaas_Plus class attributes and methods

# Node class attributes and methods

# kiamaas_Num class attributes and methods
kiamaas_Num_value: Property = Property(name="value", type=IntegerType)
kiamaas_Num.attributes={kiamaas_Num_value}

# Relationships
node0: BinaryAssociation = BinaryAssociation(
    name="node0",
    ends={
        Property(name="kiamaas_Node", type=kiamaas_Top, multiplicity=Multiplicity(1, 1)),
        Property(name="kiamaas_Top", type=kiamaas_Node, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left1: BinaryAssociation = BinaryAssociation(
    name="left1",
    ends={
        Property(name="kiamaas_Node2", type=kiamaas_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="kiamaas_Plus", type=kiamaas_Node, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right3: BinaryAssociation = BinaryAssociation(
    name="right3",
    ends={
        Property(name="kiamaas_Node5", type=kiamaas_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="kiamaas_Plus4", type=kiamaas_Node, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_kiamaas_Plus_Node = Generalization(general=Node, specific=kiamaas_Plus)
gen_kiamaas_Num_Node = Generalization(general=Node, specific=kiamaas_Num)

# Domain Model
domain_model = DomainModel(
    name="kiamaas",
    types={kiamaas_Top, kiamaas_Node, kiamaas_Plus, Node, kiamaas_Num},
    associations={node0, left1, right3},
    generalizations={gen_kiamaas_Plus_Node, gen_kiamaas_Num_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)