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
compartments_Canvas = Class(name="compartments::Canvas")
compartments_TopNode = Class(name="compartments::TopNode")
compartments_TopNodeA = Class(name="compartments::TopNodeA")
TopNode = Class(name="TopNode")
compartments_TopNodeB = Class(name="compartments::TopNodeB")
compartments_ChildOfB_E = Class(name="compartments::ChildOfB::E")
compartments_ChildOfB_G = Class(name="compartments::ChildOfB::G")
compartments_ChildOfA_C = Class(name="compartments::ChildOfA::C")
compartments_ChildOfA_D = Class(name="compartments::ChildOfA::D")
compartments_ChildOfAffixed = Class(name="compartments::ChildOfAffixed")
compartments_ChildOfB_F = Class(name="compartments::ChildOfB::F")

# compartments_Canvas class attributes and methods

# compartments_TopNode class attributes and methods

# compartments_TopNodeA class attributes and methods
compartments_TopNodeA_name: Property = Property(name="name", type=StringType)
compartments_TopNodeA.attributes={compartments_TopNodeA_name}

# TopNode class attributes and methods

# compartments_TopNodeB class attributes and methods
compartments_TopNodeB_name: Property = Property(name="name", type=StringType)
compartments_TopNodeB.attributes={compartments_TopNodeB_name}

# compartments_ChildOfB_E class attributes and methods
compartments_ChildOfB_E_name: Property = Property(name="name", type=StringType)
compartments_ChildOfB_E.attributes={compartments_ChildOfB_E_name}

# compartments_ChildOfB_G class attributes and methods
compartments_ChildOfB_G_number: Property = Property(name="number", type=IntegerType)
compartments_ChildOfB_G.attributes={compartments_ChildOfB_G_number}

# compartments_ChildOfA_C class attributes and methods
compartments_ChildOfA_C_name: Property = Property(name="name", type=StringType)
compartments_ChildOfA_C.attributes={compartments_ChildOfA_C_name}

# compartments_ChildOfA_D class attributes and methods
compartments_ChildOfA_D_name: Property = Property(name="name", type=StringType)
compartments_ChildOfA_D.attributes={compartments_ChildOfA_D_name}

# compartments_ChildOfAffixed class attributes and methods
compartments_ChildOfAffixed_description: Property = Property(name="description", type=StringType)
compartments_ChildOfAffixed.attributes={compartments_ChildOfAffixed_description}

# compartments_ChildOfB_F class attributes and methods
compartments_ChildOfB_F_name: Property = Property(name="name", type=StringType)
compartments_ChildOfB_F.attributes={compartments_ChildOfB_F_name}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="compartments_TopNode", type=compartments_Canvas, multiplicity=Multiplicity(1, 1)),
        Property(name="compartments_Canvas", type=compartments_TopNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childrenE4: BinaryAssociation = BinaryAssociation(
    name="childrenE4",
    ends={
        Property(name="compartments_ChildOfB_E", type=compartments_TopNodeB, multiplicity=Multiplicity(1, 1)),
        Property(name="compartments_TopNodeB", type=compartments_ChildOfB_E, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
childrenG5: BinaryAssociation = BinaryAssociation(
    name="childrenG5",
    ends={
        Property(name="compartments_ChildOfB_G", type=compartments_TopNodeB, multiplicity=Multiplicity(1, 1)),
        Property(name="compartments_TopNodeB6", type=compartments_ChildOfB_G, multiplicity=Multiplicity(0, 9999), is_composite=True)
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

# Generalizations
gen_compartments_TopNodeA_TopNode = Generalization(general=TopNode, specific=compartments_TopNodeA)
gen_compartments_TopNodeB_TopNode = Generalization(general=TopNode, specific=compartments_TopNodeB)

# Domain Model
domain_model = DomainModel(
    name="compartments",
    types={compartments_Canvas, compartments_TopNode, compartments_TopNodeA, TopNode, compartments_TopNodeB, compartments_ChildOfB_E, compartments_ChildOfB_G, compartments_ChildOfA_C, compartments_ChildOfA_D, compartments_ChildOfAffixed, compartments_ChildOfB_F},
    associations={elements0, childrenE4, childrenG5, childrenC1, childrenD2, childrenOfAffixed12, dNodeRelation14, childrenF7, cNodeRelation9},
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