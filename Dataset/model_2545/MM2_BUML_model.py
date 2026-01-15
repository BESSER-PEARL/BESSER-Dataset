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
testmerge_D = Class(name="testmerge::D")
testmerge_C = Class(name="testmerge::C")
testmerge_E = Class(name="testmerge::E")
testmerge_F = Class(name="testmerge::F")

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
        Property(name="1", type=testmerge_D, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=testmerge_C, multiplicity=Multiplicity(0, 1))
    }
)
toD2: BinaryAssociation = BinaryAssociation(
    name="toD2",
    ends={
        Property(name="4", type=testmerge_C, multiplicity=Multiplicity(1, 1)),
        Property(name="3", type=testmerge_D, multiplicity=Multiplicity(0, 1))
    }
)
toE5: BinaryAssociation = BinaryAssociation(
    name="toE5",
    ends={
        Property(name="testmerge_E", type=testmerge_C, multiplicity=Multiplicity(1, 1)),
        Property(name="testmerge_C", type=testmerge_E, multiplicity=Multiplicity(1, 42), is_composite=True)
    }
)
toF6: BinaryAssociation = BinaryAssociation(
    name="toF6",
    ends={
        Property(name="testmerge_F", type=testmerge_C, multiplicity=Multiplicity(1, 1)),
        Property(name="testmerge_C7", type=testmerge_F, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="testmerge",
    types={testmerge_D, testmerge_C, testmerge_E, testmerge_F},
    associations={toC0, toD2, toE5, toF6},
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