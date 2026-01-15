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
rootPackage_C = Class(name="rootPackage::C")
rootPackage_B = Class(name="rootPackage::B")
rootPackage_AbstractA = Class(name="rootPackage::AbstractA", is_abstract=True)
rootPackage_aSubPackage_D = Class(name="rootPackage::aSubPackage::D")
rootPackage_aSubSubPackage_E = Class(name="rootPackage::aSubSubPackage::E")
aSubSubPackage_F = Class(name="aSubSubPackage::F")
rootPackage_A = Class(name="rootPackage::A")
AbstractA = Class(name="AbstractA")
rootPackage_aSubSubPackage_F = Class(name="rootPackage::aSubSubPackage::F")

# rootPackage_C class attributes and methods
rootPackage_C_cstring: Property = Property(name="cstring", type=StringType)
rootPackage_C.attributes={rootPackage_C_cstring}

# rootPackage_B class attributes and methods
rootPackage_B_bint: Property = Property(name="bint", type=IntegerType)
rootPackage_B_stuff: Property = Property(name="stuff", type=StringType)
rootPackage_B.attributes={rootPackage_B_bint, rootPackage_B_stuff}

# rootPackage_AbstractA class attributes and methods

# rootPackage_aSubPackage_D class attributes and methods
rootPackage_aSubPackage_D_d: Property = Property(name="d", type=IntegerType)
rootPackage_aSubPackage_D.attributes={rootPackage_aSubPackage_D_d}

# rootPackage_aSubSubPackage_E class attributes and methods

# aSubSubPackage_F class attributes and methods

# rootPackage_A class attributes and methods
rootPackage_A_a: Property = Property(name="a", type=IntegerType)
rootPackage_A_a2: Property = Property(name="a2", type=BooleanType)
rootPackage_A.attributes={rootPackage_A_a2, rootPackage_A_a}

# AbstractA class attributes and methods

# rootPackage_aSubSubPackage_F class attributes and methods

# Relationships
c0: BinaryAssociation = BinaryAssociation(
    name="c0",
    ends={
        Property(name="rootPackage_C", type=rootPackage_A, multiplicity=Multiplicity(1, 1)),
        Property(name="rootPackage_A", type=rootPackage_C, multiplicity=Multiplicity(0, 1))
    }
)
b1: BinaryAssociation = BinaryAssociation(
    name="b1",
    ends={
        Property(name="rootPackage_B", type=rootPackage_A, multiplicity=Multiplicity(1, 1)),
        Property(name="rootPackage_A2", type=rootPackage_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
c3: BinaryAssociation = BinaryAssociation(
    name="c3",
    ends={
        Property(name="C", type=rootPackage_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b", type=rootPackage_C, multiplicity=Multiplicity(0, 1))
    }
)
b4: BinaryAssociation = BinaryAssociation(
    name="b4",
    ends={
        Property(name="B", type=rootPackage_C, multiplicity=Multiplicity(1, 1)),
        Property(name="c", type=rootPackage_B, multiplicity=Multiplicity(2, 3))
    }
)
f5: BinaryAssociation = BinaryAssociation(
    name="f5",
    ends={
        Property(name="aSubSubPackage_F", type=rootPackage_aSubSubPackage_E, multiplicity=Multiplicity(1, 1)),
        Property(name="rootPackage_aSubSubPackage_E", type=aSubSubPackage_F, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_rootPackage_A_AbstractA = Generalization(general=AbstractA, specific=rootPackage_A)

# Domain Model
domain_model = DomainModel(
    name="rootPackage",
    types={rootPackage_C, rootPackage_B, rootPackage_AbstractA, rootPackage_aSubPackage_D, rootPackage_aSubSubPackage_E, aSubSubPackage_F, rootPackage_A, AbstractA, rootPackage_aSubSubPackage_F},
    associations={c0, b1, c3, b4, f5},
    generalizations={gen_rootPackage_A_AbstractA},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)