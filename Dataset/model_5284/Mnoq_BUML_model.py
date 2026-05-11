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
mnoq_Foo = Class(name="mnoq_Foo")
mnoq_O = Class(name="mnoq_O")
mnoq_Q = Class(name="mnoq_Q")
mnoq_N = Class(name="mnoq_N")
mnoq_M = Class(name="mnoq_M")

# mnoq_Foo class attributes and methods

# mnoq_O class attributes and methods
mnoq_O_x: Property = Property(name="x", type=IntegerType)
mnoq_O.attributes={mnoq_O_x}

# mnoq_Q class attributes and methods
mnoq_Q_x: Property = Property(name="x", type=IntegerType)
mnoq_Q.attributes={mnoq_Q_x}

# mnoq_N class attributes and methods
mnoq_N_x: Property = Property(name="x", type=IntegerType)
mnoq_N.attributes={mnoq_N_x}

# mnoq_M class attributes and methods
mnoq_M_x: Property = Property(name="x", type=IntegerType)
mnoq_M.attributes={mnoq_M_x}

# Relationships
ns0: BinaryAssociation = BinaryAssociation(
    name="ns0",
    ends={
        Property(name="N", type=mnoq_Q, multiplicity=Multiplicity(1, 1)),
        Property(name="qs", type=mnoq_N, multiplicity=Multiplicity(0, 9999))
    }
)
mms1: BinaryAssociation = BinaryAssociation(
    name="mms1",
    ends={
        Property(name="M", type=mnoq_N, multiplicity=Multiplicity(1, 1)),
        Property(name="nns", type=mnoq_M, multiplicity=Multiplicity(0, 9999))
    }
)
qs2: BinaryAssociation = BinaryAssociation(
    name="qs2",
    ends={
        Property(name="Q", type=mnoq_N, multiplicity=Multiplicity(1, 1)),
        Property(name="ns", type=mnoq_Q, multiplicity=Multiplicity(0, 9999))
    }
)
foo3: BinaryAssociation = BinaryAssociation(
    name="foo3",
    ends={
        Property(name="mnoq_Foo", type=mnoq_N, multiplicity=Multiplicity(1, 1)),
        Property(name="mnoq_N", type=mnoq_Foo, multiplicity=Multiplicity(0, 1))
    }
)
nns4: BinaryAssociation = BinaryAssociation(
    name="nns4",
    ends={
        Property(name="N5", type=mnoq_M, multiplicity=Multiplicity(1, 1)),
        Property(name="mms", type=mnoq_N, multiplicity=Multiplicity(0, 9999))
    }
)
o6: BinaryAssociation = BinaryAssociation(
    name="o6",
    ends={
        Property(name="mnoq_O", type=mnoq_M, multiplicity=Multiplicity(1, 1)),
        Property(name="mnoq_M", type=mnoq_O, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="mnoq",
    types={mnoq_Foo, mnoq_O, mnoq_Q, mnoq_N, mnoq_M},
    associations={ns0, mms1, qs2, foo3, nns4, o6},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)