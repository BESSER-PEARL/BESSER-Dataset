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
test_A = Class(name="test::A")
N = Class(name="N")
B = Class(name="B")
test_N = Class(name="test::N", is_abstract=True)
test_test2_B = Class(name="test::test2::B")

# test_A class attributes and methods

# N class attributes and methods

# B class attributes and methods

# test_N class attributes and methods
test_N_n: Property = Property(name="n", type=StringType)
test_N.attributes={test_N_n}

# test_test2_B class attributes and methods
test_test2_B_nb: Property = Property(name="nb", type=IntegerType)
test_test2_B_nb2: Property = Property(name="nb2", type=IntegerType)
test_test2_B.attributes={test_test2_B_nb, test_test2_B_nb2}

# Relationships
b0: BinaryAssociation = BinaryAssociation(
    name="b0",
    ends={
        Property(name="B", type=test_A, multiplicity=Multiplicity(1, 1)),
        Property(name="test_A", type=B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_test_A_N = Generalization(general=N, specific=test_A)
gen_test_test2_B_N = Generalization(general=N, specific=test_test2_B)

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_A, N, B, test_N, test_test2_B},
    associations={b0},
    generalizations={gen_test_A_N, gen_test_test2_B_N},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)