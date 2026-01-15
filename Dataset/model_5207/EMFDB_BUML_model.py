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
emfdb_D = Class(name="emfdb::D")
emfdb_E = Class(name="emfdb::E")

# emfdb_A class attributes and methods
emfdb_A_string: Property = Property(name="string", type=StringType)
emfdb_A.attributes={emfdb_A_string}

# emfdb_B class attributes and methods
emfdb_B_string: Property = Property(name="string", type=StringType)
emfdb_B.attributes={emfdb_B_string}

# emfdb_C class attributes and methods
emfdb_C_key: Property = Property(name="key", type=StringType)
emfdb_C_value: Property = Property(name="value", type=StringType)
emfdb_C.attributes={emfdb_C_value, emfdb_C_key}

# emfdb_D class attributes and methods
emfdb_D_name: Property = Property(name="name", type=StringType)
emfdb_D.attributes={emfdb_D_name}

# emfdb_E class attributes and methods
emfdb_E_name: Property = Property(name="name", type=StringType)
emfdb_E.attributes={emfdb_E_name}

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
d3: BinaryAssociation = BinaryAssociation(
    name="d3",
    ends={
        Property(name="emfdb_D", type=emfdb_B, multiplicity=Multiplicity(1, 1)),
        Property(name="emfdb_B4", type=emfdb_D, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elist5: BinaryAssociation = BinaryAssociation(
    name="elist5",
    ends={
        Property(name="emfdb_E", type=emfdb_D, multiplicity=Multiplicity(1, 1)),
        Property(name="emfdb_D6", type=emfdb_E, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="emfdb",
    types={emfdb_A, emfdb_B, emfdb_C, emfdb_D, emfdb_E},
    associations={blist0, cmap1, d3, elist5},
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