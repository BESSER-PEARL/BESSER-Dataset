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
refinher3_DG = Class(name="refinher3::DG")
refinher3_E = Class(name="refinher3::E")
DNamedElement = Class(name="DNamedElement")
refinher3_N = Class(name="refinher3::N")
refinher3_DNamedElement = Class(name="refinher3::DNamedElement", is_abstract=True)
refinher3_DL = Class(name="refinher3::DL")
CE = Class(name="CE")
refinher3_BB = Class(name="refinher3::BB")
refinher3_DR = Class(name="refinher3::DR")
E = Class(name="E")
refinher3_DC = Class(name="refinher3::DC")
refinher3_M = Class(name="refinher3::M")
refinher3_A = Class(name="refinher3::A", is_abstract=True)
refinher3_CE = Class(name="refinher3::CE")
A = Class(name="A")
refinher3_Foobar = Class(name="refinher3::Foobar")

# refinher3_DG class attributes and methods

# refinher3_E class attributes and methods

# DNamedElement class attributes and methods

# refinher3_N class attributes and methods
refinher3_N_nam: Property = Property(name="nam", type=StringType)
refinher3_N.attributes={refinher3_N_nam}

# refinher3_DNamedElement class attributes and methods
refinher3_DNamedElement_name: Property = Property(name="name", type=StringType)
refinher3_DNamedElement.attributes={refinher3_DNamedElement_name}

# refinher3_DL class attributes and methods

# CE class attributes and methods

# refinher3_BB class attributes and methods

# refinher3_DR class attributes and methods

# E class attributes and methods

# refinher3_DC class attributes and methods

# refinher3_M class attributes and methods
refinher3_M_id: Property = Property(name="id", type=StringType)
refinher3_M.attributes={refinher3_M_id}

# refinher3_A class attributes and methods

# refinher3_CE class attributes and methods

# A class attributes and methods

# refinher3_Foobar class attributes and methods

# Relationships
sn0: BinaryAssociation = BinaryAssociation(
    name="sn0",
    ends={
        Property(name="refinher3_N", type=refinher3_E, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher3_E", type=refinher3_N, multiplicity=Multiplicity(0, 1))
    }
)
tn1: BinaryAssociation = BinaryAssociation(
    name="tn1",
    ends={
        Property(name="refinher3_N3", type=refinher3_E, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher3_E2", type=refinher3_N, multiplicity=Multiplicity(0, 1))
    }
)
bBridge4: BinaryAssociation = BinaryAssociation(
    name="bBridge4",
    ends={
        Property(name="refinher3_BB", type=refinher3_DL, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher3_DL", type=refinher3_BB, multiplicity=Multiplicity(0, 1))
    }
)
bridges5: BinaryAssociation = BinaryAssociation(
    name="bridges5",
    ends={
        Property(name="refinher3_BB6", type=refinher3_DG, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher3_DG", type=refinher3_BB, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ns7: BinaryAssociation = BinaryAssociation(
    name="ns7",
    ends={
        Property(name="refinher3_N9", type=refinher3_DG, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher3_DG8", type=refinher3_N, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ms10: BinaryAssociation = BinaryAssociation(
    name="ms10",
    ends={
        Property(name="refinher3_M", type=refinher3_DG, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher3_DG11", type=refinher3_M, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
esbars12: BinaryAssociation = BinaryAssociation(
    name="esbars12",
    ends={
        Property(name="refinher3_E14", type=refinher3_M, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher3_M13", type=refinher3_E, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foobars15: BinaryAssociation = BinaryAssociation(
    name="foobars15",
    ends={
        Property(name="refinher3_Foobar", type=refinher3_M, multiplicity=Multiplicity(1, 1)),
        Property(name="refinher3_M16", type=refinher3_Foobar, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_refinher3_E_DNamedElement = Generalization(general=DNamedElement, specific=refinher3_E)
gen_refinher3_DL_CE = Generalization(general=CE, specific=refinher3_DL)
gen_refinher3_DR_E = Generalization(general=E, specific=refinher3_DR)
gen_refinher3_DC_CE = Generalization(general=CE, specific=refinher3_DC)
gen_refinher3_A_DNamedElement = Generalization(general=DNamedElement, specific=refinher3_A)
gen_refinher3_CE_A = Generalization(general=A, specific=refinher3_CE)
gen_refinher3_CE_E = Generalization(general=E, specific=refinher3_CE)
gen_refinher3_BB_DNamedElement = Generalization(general=DNamedElement, specific=refinher3_BB)
gen_refinher3_Foobar_DNamedElement = Generalization(general=DNamedElement, specific=refinher3_Foobar)

# Domain Model
domain_model = DomainModel(
    name="refinher3",
    types={refinher3_DG, refinher3_E, DNamedElement, refinher3_N, refinher3_DNamedElement, refinher3_DL, CE, refinher3_BB, refinher3_DR, E, refinher3_DC, refinher3_M, refinher3_A, refinher3_CE, A, refinher3_Foobar},
    associations={sn0, tn1, bBridge4, bridges5, ns7, ms10, esbars12, foobars15},
    generalizations={gen_refinher3_E_DNamedElement, gen_refinher3_DL_CE, gen_refinher3_DR_E, gen_refinher3_DC_CE, gen_refinher3_A_DNamedElement, gen_refinher3_CE_A, gen_refinher3_CE_E, gen_refinher3_BB_DNamedElement, gen_refinher3_Foobar_DNamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)