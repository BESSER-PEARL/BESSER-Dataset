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
refinher2_E = Class(name="refinher2::E", is_abstract=True)
DNamedElement = Class(name="DNamedElement")
refinher2_N = Class(name="refinher2::N")
refinher2_M = Class(name="refinher2::M")
refinher2_DNamedElement = Class(name="refinher2::DNamedElement", is_abstract=True)
refinher2_DL = Class(name="refinher2::DL")
CE = Class(name="CE")
refinher2_BB = Class(name="refinher2::BB")
refinher2_DR = Class(name="refinher2::DR")
E = Class(name="E")
refinher2_DC = Class(name="refinher2::DC")
refinher2_DG = Class(name="refinher2::DG")
refinher2_CE = Class(name="refinher2::CE", is_abstract=True)
A = Class(name="A")
M = Class(name="M")
refinher2_H = Class(name="refinher2::H")
N = Class(name="N")
refinher2_Y = Class(name="refinher2::Y")
refinher2_AB = Class(name="refinher2::AB")
refinher2_A = Class(name="refinher2::A", is_abstract=True)

# refinher2_E class attributes and methods

# DNamedElement class attributes and methods

# refinher2_N class attributes and methods

# refinher2_M class attributes and methods

# refinher2_DNamedElement class attributes and methods
refinher2_DNamedElement_name: Property = Property(name="name", type=StringType)
refinher2_DNamedElement.attributes={refinher2_DNamedElement_name}

# refinher2_DL class attributes and methods

# CE class attributes and methods

# refinher2_BB class attributes and methods

# refinher2_DR class attributes and methods

# E class attributes and methods

# refinher2_DC class attributes and methods

# refinher2_DG class attributes and methods

# refinher2_CE class attributes and methods

# A class attributes and methods

# M class attributes and methods

# refinher2_H class attributes and methods

# N class attributes and methods

# refinher2_Y class attributes and methods

# refinher2_AB class attributes and methods

# refinher2_A class attributes and methods

# Relationships
sn0: BinaryAssociation = BinaryAssociation(
    name="sn0",
    ends={
        Property(name="refinher2_N", type=refinher2_E, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher2_E", type=refinher2_N, multiplicity=Multiplicity(0, 1))
    }
)
tn1: BinaryAssociation = BinaryAssociation(
    name="tn1",
    ends={
        Property(name="refinher2_M", type=refinher2_E, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher2_E2", type=refinher2_M, multiplicity=Multiplicity(0, 1))
    }
)
bBridge3: BinaryAssociation = BinaryAssociation(
    name="bBridge3",
    ends={
        Property(name="refinher2_BB", type=refinher2_DL, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher2_DL", type=refinher2_BB, multiplicity=Multiplicity(0, 1))
    }
)
aBridge11: BinaryAssociation = BinaryAssociation(
    name="aBridge11",
    ends={
        Property(name="refinher2_AB12", type=refinher2_A, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher2_A", type=refinher2_AB, multiplicity=Multiplicity(0, 1))
    }
)
n13: BinaryAssociation = BinaryAssociation(
    name="n13",
    ends={
        Property(name="refinher2_N15", type=refinher2_A, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher2_A14", type=refinher2_N, multiplicity=Multiplicity(0, 1))
    }
)
es16: BinaryAssociation = BinaryAssociation(
    name="es16",
    ends={
        Property(name="refinher2_E17", type=refinher2_H, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher2_H", type=refinher2_E, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ns4: BinaryAssociation = BinaryAssociation(
    name="ns4",
    ends={
        Property(name="refinher2_N5", type=refinher2_DG, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher2_DG", type=refinher2_N, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bridges6: BinaryAssociation = BinaryAssociation(
    name="bridges6",
    ends={
        Property(name="refinher2_BB8", type=refinher2_DG, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher2_DG7", type=refinher2_BB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
abridges9: BinaryAssociation = BinaryAssociation(
    name="abridges9",
    ends={
        Property(name="refinher2_AB", type=refinher2_DG, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher2_DG10", type=refinher2_AB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_refinher2_E_DNamedElement = Generalization(general=DNamedElement, specific=refinher2_E)
gen_refinher2_DL_CE = Generalization(general=CE, specific=refinher2_DL)
gen_refinher2_DR_E = Generalization(general=E, specific=refinher2_DR)
gen_refinher2_DC_CE = Generalization(general=CE, specific=refinher2_DC)
gen_refinher2_CE_A = Generalization(general=A, specific=refinher2_CE)
gen_refinher2_CE_E = Generalization(general=E, specific=refinher2_CE)
gen_refinher2_N_DNamedElement = Generalization(general=DNamedElement, specific=refinher2_N)
gen_refinher2_N_A = Generalization(general=A, specific=refinher2_N)
gen_refinher2_N_M = Generalization(general=M, specific=refinher2_N)
gen_refinher2_BB_DNamedElement = Generalization(general=DNamedElement, specific=refinher2_BB)
gen_refinher2_AB_DNamedElement = Generalization(general=DNamedElement, specific=refinher2_AB)
gen_refinher2_H_N = Generalization(general=N, specific=refinher2_H)
gen_refinher2_Y_N = Generalization(general=N, specific=refinher2_Y)
gen_refinher2_A_DNamedElement = Generalization(general=DNamedElement, specific=refinher2_A)

# Domain Model
domain_model = DomainModel(
    name="refinher2",
    types={refinher2_E, DNamedElement, refinher2_N, refinher2_M, refinher2_DNamedElement, refinher2_DL, CE, refinher2_BB, refinher2_DR, E, refinher2_DC, refinher2_DG, refinher2_CE, A, M, refinher2_H, N, refinher2_Y, refinher2_AB, refinher2_A},
    associations={sn0, tn1, bBridge3, aBridge11, n13, es16, ns4, bridges6, abridges9},
    generalizations={gen_refinher2_E_DNamedElement, gen_refinher2_DL_CE, gen_refinher2_DR_E, gen_refinher2_DC_CE, gen_refinher2_CE_A, gen_refinher2_CE_E, gen_refinher2_N_DNamedElement, gen_refinher2_N_A, gen_refinher2_N_M, gen_refinher2_BB_DNamedElement, gen_refinher2_AB_DNamedElement, gen_refinher2_H_N, gen_refinher2_Y_N, gen_refinher2_A_DNamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)