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
mnoq_Foo = Class(name="mnoq::Foo")
mnoq_O = Class(name="mnoq::O")
mnoq_N = Class(name="mnoq::N")
mnoq_M = Class(name="mnoq::M")
mnoq_Q = Class(name="mnoq::Q")

# mnoq_Foo class attributes and methods

# mnoq_O class attributes and methods
mnoq_O_x: Property = Property(name="x", type=IntegerType)
mnoq_O.attributes={mnoq_O_x}

# mnoq_N class attributes and methods
mnoq_N_x: Property = Property(name="x", type=IntegerType)
mnoq_N.attributes={mnoq_N_x}

# mnoq_M class attributes and methods
mnoq_M_x: Property = Property(name="x", type=IntegerType)
mnoq_M.attributes={mnoq_M_x}

# mnoq_Q class attributes and methods
mnoq_Q_x: Property = Property(name="x", type=IntegerType)
mnoq_Q.attributes={mnoq_Q_x}

# Relationships
ns0: BinaryAssociation = BinaryAssociation(
    name="ns0",
    ends={
        Property(name="1", type=mnoq_Q, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=mnoq_N, multiplicity=Multiplicity(0, 9999))
    }
)
mms2: BinaryAssociation = BinaryAssociation(
    name="mms2",
    ends={
        Property(name="4", type=mnoq_N, multiplicity=Multiplicity(1, 1)),
        Property(name="3", type=mnoq_M, multiplicity=Multiplicity(0, 9999))
    }
)
qs5: BinaryAssociation = BinaryAssociation(
    name="qs5",
    ends={
        Property(name="7", type=mnoq_N, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=mnoq_Q, multiplicity=Multiplicity(0, 9999))
    }
)
foo8: BinaryAssociation = BinaryAssociation(
    name="foo8",
    ends={
        Property(name="mnoq_Foo", type=mnoq_N, multiplicity=Multiplicity(1, 1)),
        Property(name="mnoq_N", type=mnoq_Foo, multiplicity=Multiplicity(0, 1))
    }
)
nns9: BinaryAssociation = BinaryAssociation(
    name="nns9",
    ends={
        Property(name="11", type=mnoq_M, multiplicity=Multiplicity(1, 1)),
        Property(name="10", type=mnoq_N, multiplicity=Multiplicity(0, 9999))
    }
)
o12: BinaryAssociation = BinaryAssociation(
    name="o12",
    ends={
        Property(name="mnoq_O", type=mnoq_M, multiplicity=Multiplicity(1, 1)),
        Property(name="mnoq_M", type=mnoq_O, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="mnoq",
    types={mnoq_Foo, mnoq_O, mnoq_N, mnoq_M, mnoq_Q},
    associations={ns0, mms2, qs5, foo8, nns9, o12},
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