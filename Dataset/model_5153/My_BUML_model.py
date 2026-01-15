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
example_A = Class(name="example::A")
example_B = Class(name="example::B")

# example_A class attributes and methods

# example_B class attributes and methods

# Relationships
b711: BinaryAssociation = BinaryAssociation(
    name="b711",
    ends={
        Property(name="B12", type=example_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a7", type=example_B, multiplicity=Multiplicity(0, 1))
    }
)
b813: BinaryAssociation = BinaryAssociation(
    name="b813",
    ends={
        Property(name="B14", type=example_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a8", type=example_B, multiplicity=Multiplicity(1, 9999))
    }
)
b915: BinaryAssociation = BinaryAssociation(
    name="b915",
    ends={
        Property(name="B16", type=example_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a9", type=example_B, multiplicity=Multiplicity(0, 9999))
    }
)
b1017: BinaryAssociation = BinaryAssociation(
    name="b1017",
    ends={
        Property(name="B18", type=example_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a10", type=example_B, multiplicity=Multiplicity(1, 1))
    }
)
b1119: BinaryAssociation = BinaryAssociation(
    name="b1119",
    ends={
        Property(name="B20", type=example_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a11", type=example_B, multiplicity=Multiplicity(0, 1))
    }
)
b1221: BinaryAssociation = BinaryAssociation(
    name="b1221",
    ends={
        Property(name="B22", type=example_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a12", type=example_B, multiplicity=Multiplicity(1, 9999))
    }
)
b1323: BinaryAssociation = BinaryAssociation(
    name="b1323",
    ends={
        Property(name="B24", type=example_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a13", type=example_B, multiplicity=Multiplicity(0, 9999))
    }
)
b1425: BinaryAssociation = BinaryAssociation(
    name="b1425",
    ends={
        Property(name="B26", type=example_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a14", type=example_B, multiplicity=Multiplicity(1, 1))
    }
)
b1527: BinaryAssociation = BinaryAssociation(
    name="b1527",
    ends={
        Property(name="B28", type=example_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a15", type=example_B, multiplicity=Multiplicity(0, 1))
    }
)
b1629: BinaryAssociation = BinaryAssociation(
    name="b1629",
    ends={
        Property(name="B30", type=example_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a16", type=example_B, multiplicity=Multiplicity(1, 9999))
    }
)
b10: BinaryAssociation = BinaryAssociation(
    name="b10",
    ends={
        Property(name="B", type=example_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a1", type=example_B, multiplicity=Multiplicity(0, 9999))
    }
)
b21: BinaryAssociation = BinaryAssociation(
    name="b21",
    ends={
        Property(name="B2", type=example_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a2", type=example_B, multiplicity=Multiplicity(1, 1))
    }
)
b33: BinaryAssociation = BinaryAssociation(
    name="b33",
    ends={
        Property(name="B4", type=example_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a3", type=example_B, multiplicity=Multiplicity(0, 1))
    }
)
b45: BinaryAssociation = BinaryAssociation(
    name="b45",
    ends={
        Property(name="B6", type=example_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a4", type=example_B, multiplicity=Multiplicity(1, 9999))
    }
)
b57: BinaryAssociation = BinaryAssociation(
    name="b57",
    ends={
        Property(name="B8", type=example_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a5", type=example_B, multiplicity=Multiplicity(0, 9999))
    }
)
b69: BinaryAssociation = BinaryAssociation(
    name="b69",
    ends={
        Property(name="B10", type=example_A, multiplicity=Multiplicity(1, 1)),
        Property(name="a6", type=example_B, multiplicity=Multiplicity(1, 1))
    }
)
a640: BinaryAssociation = BinaryAssociation(
    name="a640",
    ends={
        Property(name="b6", type=example_A, multiplicity=Multiplicity(1, 1)),
        Property(name="A41", type=example_B, multiplicity=Multiplicity(1, 1))
    }
)
a742: BinaryAssociation = BinaryAssociation(
    name="a742",
    ends={
        Property(name="A43", type=example_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b7", type=example_A, multiplicity=Multiplicity(1, 1))
    }
)
a844: BinaryAssociation = BinaryAssociation(
    name="a844",
    ends={
        Property(name="A45", type=example_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b8", type=example_A, multiplicity=Multiplicity(1, 1))
    }
)
a946: BinaryAssociation = BinaryAssociation(
    name="a946",
    ends={
        Property(name="A47", type=example_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b9", type=example_A, multiplicity=Multiplicity(0, 1))
    }
)
a1048: BinaryAssociation = BinaryAssociation(
    name="a1048",
    ends={
        Property(name="A49", type=example_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b10", type=example_A, multiplicity=Multiplicity(0, 1))
    }
)
a1150: BinaryAssociation = BinaryAssociation(
    name="a1150",
    ends={
        Property(name="A51", type=example_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b11", type=example_A, multiplicity=Multiplicity(0, 1))
    }
)
a1252: BinaryAssociation = BinaryAssociation(
    name="a1252",
    ends={
        Property(name="A53", type=example_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b12", type=example_A, multiplicity=Multiplicity(0, 1))
    }
)
a1354: BinaryAssociation = BinaryAssociation(
    name="a1354",
    ends={
        Property(name="A55", type=example_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b13", type=example_A, multiplicity=Multiplicity(1, 9999))
    }
)
a1456: BinaryAssociation = BinaryAssociation(
    name="a1456",
    ends={
        Property(name="A57", type=example_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b14", type=example_A, multiplicity=Multiplicity(1, 9999))
    }
)
a131: BinaryAssociation = BinaryAssociation(
    name="a131",
    ends={
        Property(name="A", type=example_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b1", type=example_A, multiplicity=Multiplicity(0, 9999))
    }
)
a232: BinaryAssociation = BinaryAssociation(
    name="a232",
    ends={
        Property(name="A33", type=example_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b2", type=example_A, multiplicity=Multiplicity(0, 9999))
    }
)
a334: BinaryAssociation = BinaryAssociation(
    name="a334",
    ends={
        Property(name="A35", type=example_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b3", type=example_A, multiplicity=Multiplicity(0, 9999))
    }
)
a436: BinaryAssociation = BinaryAssociation(
    name="a436",
    ends={
        Property(name="A37", type=example_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b4", type=example_A, multiplicity=Multiplicity(0, 9999))
    }
)
a538: BinaryAssociation = BinaryAssociation(
    name="a538",
    ends={
        Property(name="A39", type=example_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b5", type=example_A, multiplicity=Multiplicity(1, 1))
    }
)
a1558: BinaryAssociation = BinaryAssociation(
    name="a1558",
    ends={
        Property(name="A59", type=example_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b15", type=example_A, multiplicity=Multiplicity(1, 9999))
    }
)
a1660: BinaryAssociation = BinaryAssociation(
    name="a1660",
    ends={
        Property(name="A61", type=example_B, multiplicity=Multiplicity(1, 1)),
        Property(name="b16", type=example_A, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="example",
    types={example_A, example_B},
    associations={b711, b813, b915, b1017, b1119, b1221, b1323, b1425, b1527, b1629, b10, b21, b33, b45, b57, b69, a640, a742, a844, a946, a1048, a1150, a1252, a1354, a1456, a131, a232, a334, a436, a538, a1558, a1660},
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