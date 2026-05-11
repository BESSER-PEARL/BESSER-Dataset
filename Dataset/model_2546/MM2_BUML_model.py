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
testmerge_D = Class(name="testmerge_D")
testmerge_C = Class(name="testmerge_C")
testmerge_E = Class(name="testmerge_E")
testmerge_F = Class(name="testmerge_F")

# testmerge_D class attributes and methods
testmerge_D_emfDataType: Property = Property(name="emfDataType", type=StringType)
testmerge_D.attributes={testmerge_D_emfDataType}

# testmerge_C class attributes and methods
testmerge_C_dataType: Property = Property(name="dataType", type=StringType)
testmerge_C.attributes={testmerge_C_dataType}

# testmerge_E class attributes and methods

# testmerge_F class attributes and methods

# Relationships
toC0: BinaryAssociation = BinaryAssociation(
    name="toC0",
    ends={
        Property(name="C", type=testmerge_D, multiplicity=Multiplicity(1, 1)),
        Property(name="toD", type=testmerge_C, multiplicity=Multiplicity(0, 1))
    }
)
toD1: BinaryAssociation = BinaryAssociation(
    name="toD1",
    ends={
        Property(name="D", type=testmerge_C, multiplicity=Multiplicity(1, 1)),
        Property(name="toC", type=testmerge_D, multiplicity=Multiplicity(0, 1))
    }
)
toE2: BinaryAssociation = BinaryAssociation(
    name="toE2",
    ends={
        Property(name="testmerge_E", type=testmerge_C, multiplicity=Multiplicity(1, 1)),
        Property(name="testmerge_C", type=testmerge_E, multiplicity=Multiplicity(1, 42), is_composite=True)
    }
)
toF3: BinaryAssociation = BinaryAssociation(
    name="toF3",
    ends={
        Property(name="testmerge_F", type=testmerge_C, multiplicity=Multiplicity(1, 1)),
        Property(name="testmerge_C4", type=testmerge_F, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="testmerge",
    types={testmerge_D, testmerge_C, testmerge_E, testmerge_F},
    associations={toC0, toD1, toE2, toF3},
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