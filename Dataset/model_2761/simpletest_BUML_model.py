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
simpletest_B = Class(name="simpletest::B")
simpletest_L = Class(name="simpletest::L")
simpletest_N = Class(name="simpletest::N", is_abstract=True)
simpletest_A = Class(name="simpletest::A")
N = Class(name="N")
simpletest_X = Class(name="simpletest::X")

# simpletest_B class attributes and methods

# simpletest_L class attributes and methods

# simpletest_N class attributes and methods
simpletest_N_name: Property = Property(name="name", type=StringType)
simpletest_N.attributes={simpletest_N_name}

# simpletest_A class attributes and methods

# N class attributes and methods

# simpletest_X class attributes and methods

# Relationships
bs0: BinaryAssociation = BinaryAssociation(
    name="bs0",
    ends={
        Property(name="simpletest_B", type=simpletest_A, multiplicity=Multiplicity(1, 1)),
        Property(name="simpletest_A", type=simpletest_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ls1: BinaryAssociation = BinaryAssociation(
    name="ls1",
    ends={
        Property(name="simpletest_L", type=simpletest_A, multiplicity=Multiplicity(1, 1)),
        Property(name="simpletest_A2", type=simpletest_L, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
as3: BinaryAssociation = BinaryAssociation(
    name="as3",
    ends={
        Property(name="simpletest_A4", type=simpletest_X, multiplicity=Multiplicity(1, 1)),
        Property(name="simpletest_X", type=simpletest_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
a5: BinaryAssociation = BinaryAssociation(
    name="a5",
    ends={
        Property(name="simpletest_A7", type=simpletest_L, multiplicity=Multiplicity(1, 1)),
        Property(name="simpletest_L6", type=simpletest_A, multiplicity=Multiplicity(0, 1))
    }
)
b8: BinaryAssociation = BinaryAssociation(
    name="b8",
    ends={
        Property(name="simpletest_B10", type=simpletest_L, multiplicity=Multiplicity(1, 1)),
        Property(name="simpletest_L9", type=simpletest_B, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_simpletest_B_N = Generalization(general=N, specific=simpletest_B)
gen_simpletest_A_N = Generalization(general=N, specific=simpletest_A)
gen_simpletest_L_N = Generalization(general=N, specific=simpletest_L)

# Domain Model
domain_model = DomainModel(
    name="simpletest",
    types={simpletest_B, simpletest_L, simpletest_N, simpletest_A, N, simpletest_X},
    associations={bs0, ls1, as3, a5, b8},
    generalizations={gen_simpletest_B_N, gen_simpletest_A_N, gen_simpletest_L_N},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)