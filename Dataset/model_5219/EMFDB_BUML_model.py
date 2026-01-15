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
emfdb_A = Class(name="emfdb::A")
emfdb_B = Class(name="emfdb::B")
emfdb_C = Class(name="emfdb::C")

# emfdb_A class attributes and methods
emfdb_A_string: Property = Property(name="string", type=StringType)
emfdb_A.attributes={emfdb_A_string}

# emfdb_B class attributes and methods
emfdb_B_string: Property = Property(name="string", type=StringType)
emfdb_B.attributes={emfdb_B_string}

# emfdb_C class attributes and methods
emfdb_C_value: Property = Property(name="value", type=StringType)
emfdb_C_key: Property = Property(name="key", type=StringType)
emfdb_C.attributes={emfdb_C_value, emfdb_C_key}

# Relationships
blist0: BinaryAssociation = BinaryAssociation(
    name="blist0",
    ends={
        Property(name="emfdb_B", type=emfdb_A, multiplicity=Multiplicity(1, 1)),
        Property(name="emfdb_A", type=emfdb_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cmap1: BinaryAssociation = BinaryAssociation(
    name="cmap1",
    ends={
        Property(name="emfdb_C", type=emfdb_A, multiplicity=Multiplicity(1, 1)),
        Property(name="emfdb_A2", type=emfdb_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="emfdb",
    types={emfdb_A, emfdb_B, emfdb_C},
    associations={blist0, cmap1},
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