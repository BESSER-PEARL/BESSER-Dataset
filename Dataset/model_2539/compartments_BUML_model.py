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
compartments_Canvas = Class(name="compartments_Canvas")
compartments_TopNode = Class(name="compartments_TopNode")
compartments_TopNodeA = Class(name="compartments_TopNodeA")
TopNode = Class(name="TopNode")
compartments_ChildOfA_C = Class(name="compartments_ChildOfA_C")
compartments_ChildOfA_D = Class(name="compartments_ChildOfA_D")
compartments_ChildOfB_F = Class(name="compartments_ChildOfB_F")
compartments_ChildOfAffixed = Class(name="compartments_ChildOfAffixed")
compartments_TopNodeB = Class(name="compartments_TopNodeB")
compartments_ChildOfB_E = Class(name="compartments_ChildOfB_E")
compartments_ChildOfB_G = Class(name="compartments_ChildOfB_G")

# compartments_Canvas class attributes and methods

# compartments_TopNode class attributes and methods

# compartments_TopNodeA class attributes and methods
compartments_TopNodeA_name: Property = Property(name="name", type=StringType)
compartments_TopNodeA.attributes={compartments_TopNodeA_name}

# TopNode class attributes and methods

# compartments_ChildOfA_C class attributes and methods
compartments_ChildOfA_C_name: Property = Property(name="name", type=StringType)
compartments_ChildOfA_C.attributes={compartments_ChildOfA_C_name}

# compartments_ChildOfA_D class attributes and methods
compartments_ChildOfA_D_name: Property = Property(name="name", type=StringType)
compartments_ChildOfA_D.attributes={compartments_ChildOfA_D_name}

# compartments_ChildOfB_F class attributes and methods
compartments_ChildOfB_F_name: Property = Property(name="name", type=StringType)
compartments_ChildOfB_F.attributes={compartments_ChildOfB_F_name}

# compartments_ChildOfAffixed class attributes and methods
compartments_ChildOfAffixed_description: Property = Property(name="description", type=StringType)
compartments_ChildOfAffixed.attributes={compartments_ChildOfAffixed_description}

# compartments_TopNodeB class attributes and methods
compartments_TopNodeB_name: Property = Property(name="name", type=StringType)
compartments_TopNodeB.attributes={compartments_TopNodeB_name}

# compartments_ChildOfB_E class attributes and methods
compartments_ChildOfB_E_name: Property = Property(name="name", type=StringType)
compartments_ChildOfB_E.attributes={compartments_ChildOfB_E_name}

# compartments_ChildOfB_G class attributes and methods
compartments_ChildOfB_G_number: Property = Property(name="number", type=IntegerType)
compartments_ChildOfB_G.attributes={compartments_ChildOfB_G_number}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="compartments_TopNode", type=compartments_Canvas, multiplicity=Multiplicity(1, 1)),
        Property(name="compartments_Canvas", type=compartments_TopNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childrenC1: BinaryAssociation = BinaryAssociation(
    name="childrenC1",
    ends={
        Property(name="compartments_ChildOfA_C", type=compartments_TopNodeA, multiplicity=Multiplicity(1, 1)),
        Property(name="compartments_TopNodeA", type=compartments_ChildOfA_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childrenD2: BinaryAssociation = BinaryAssociation(
    name="childrenD2",
    ends={
        Property(name="compartments_ChildOfA_D", type=compartments_TopNodeA, multiplicity=Multiplicity(1, 1)),
        Property(name="compartments_TopNodeA3", type=compartments_ChildOfA_D, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childrenG5: BinaryAssociation = BinaryAssociation(
    name="childrenG5",
    ends={
        Property(name="compartments_ChildOfB_G", type=compartments_TopNodeB, multiplicity=Multiplicity(1, 1)),
        Property(name="compartments_TopNodeB6", type=compartments_ChildOfB_G, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childrenF7: BinaryAssociation = BinaryAssociation(
    name="childrenF7",
    ends={
        Property(name="compartments_ChildOfB_F", type=compartments_TopNodeB, multiplicity=Multiplicity(1, 1)),
        Property(name="compartments_TopNodeB8", type=compartments_ChildOfB_F, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cNodeRelation9: BinaryAssociation = BinaryAssociation(
    name="cNodeRelation9",
    ends={
        Property(name="compartments_ChildOfA_C11", type=compartments_ChildOfB_E, multiplicity=Multiplicity(1, 1)),
        Property(name="compartments_ChildOfB_E10", type=compartments_ChildOfA_C, multiplicity=Multiplicity(0, 1))
    }
)
childrenOfAffixed12: BinaryAssociation = BinaryAssociation(
    name="childrenOfAffixed12",
    ends={
        Property(name="compartments_ChildOfAffixed", type=compartments_ChildOfB_G, multiplicity=Multiplicity(1, 1)),
        Property(name="compartments_ChildOfB_G13", type=compartments_ChildOfAffixed, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dNodeRelation14: BinaryAssociation = BinaryAssociation(
    name="dNodeRelation14",
    ends={
        Property(name="compartments_ChildOfA_D16", type=compartments_ChildOfB_F, multiplicity=Multiplicity(1, 1)),
        Property(name="compartments_ChildOfB_F15", type=compartments_ChildOfA_D, multiplicity=Multiplicity(0, 1))
    }
)
childrenE4: BinaryAssociation = BinaryAssociation(
    name="childrenE4",
    ends={
        Property(name="compartments_ChildOfB_E", type=compartments_TopNodeB, multiplicity=Multiplicity(1, 1)),
        Property(name="compartments_TopNodeB", type=compartments_ChildOfB_E, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_compartments_TopNodeA_TopNode = Generalization(general=TopNode, specific=compartments_TopNodeA)
gen_compartments_TopNodeB_TopNode = Generalization(general=TopNode, specific=compartments_TopNodeB)

# Domain Model
domain_model = DomainModel(
    name="compartments",
    types={compartments_Canvas, compartments_TopNode, compartments_TopNodeA, TopNode, compartments_ChildOfA_C, compartments_ChildOfA_D, compartments_ChildOfB_F, compartments_ChildOfAffixed, compartments_TopNodeB, compartments_ChildOfB_E, compartments_ChildOfB_G},
    associations={elements0, childrenC1, childrenD2, childrenG5, childrenF7, cNodeRelation9, childrenOfAffixed12, dNodeRelation14, childrenE4},
    generalizations={gen_compartments_TopNodeA_TopNode, gen_compartments_TopNodeB_TopNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)