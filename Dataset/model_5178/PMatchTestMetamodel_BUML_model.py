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
pmtest_A = Class(name="pmtest::A")
pmtest_D = Class(name="pmtest::D")
pmtest_B = Class(name="pmtest::B")
A = Class(name="A")
pmtest_C = Class(name="pmtest::C")

# pmtest_A class attributes and methods
pmtest_A_i: Property = Property(name="i", type=IntegerType)
pmtest_A.attributes={pmtest_A_i}

# pmtest_D class attributes and methods
pmtest_D_j: Property = Property(name="j", type=IntegerType)
pmtest_D.attributes={pmtest_D_j}

# pmtest_B class attributes and methods

# A class attributes and methods

# pmtest_C class attributes and methods

# Relationships
t1: BinaryAssociation = BinaryAssociation(
    name="t1",
    ends={
        Property(name="A", type=pmtest_A, multiplicity=Multiplicity(1, 1)),
        Property(name="s", type=pmtest_A, multiplicity=Multiplicity(0, 9999))
    }
)
s3: BinaryAssociation = BinaryAssociation(
    name="s3",
    ends={
        Property(name="A4", type=pmtest_A, multiplicity=Multiplicity(1, 1)),
        Property(name="t", type=pmtest_A, multiplicity=Multiplicity(0, 9999))
    }
)
d5: BinaryAssociation = BinaryAssociation(
    name="d5",
    ends={
        Property(name="pmtest_D", type=pmtest_A, multiplicity=Multiplicity(1, 1)),
        Property(name="pmtest_A", type=pmtest_D, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_pmtest_B_A = Generalization(general=A, specific=pmtest_B)
gen_pmtest_C_A = Generalization(general=A, specific=pmtest_C)

# Domain Model
domain_model = DomainModel(
    name="pmtest",
    types={pmtest_A, pmtest_D, pmtest_B, A, pmtest_C},
    associations={t1, s3, d5},
    generalizations={gen_pmtest_B_A, gen_pmtest_C_A},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)