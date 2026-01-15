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
TestMM2_Metadata = Class(name="TestMM2::Metadata")
TestMM2_Test = Class(name="TestMM2::Test")

# TestMM2_Metadata class attributes and methods
TestMM2_Metadata_user: Property = Property(name="user", type=StringType)
TestMM2_Metadata_webpage: Property = Property(name="webpage", type=StringType)
TestMM2_Metadata_date: Property = Property(name="date", type=StringType)
TestMM2_Metadata_taglist: Property = Property(name="taglist", type=StringType)
TestMM2_Metadata.attributes={TestMM2_Metadata_taglist, TestMM2_Metadata_webpage, TestMM2_Metadata_date, TestMM2_Metadata_user}

# TestMM2_Test class attributes and methods
TestMM2_Test_id: Property = Property(name="id", type=StringType)
TestMM2_Test.attributes={TestMM2_Test_id}

# Relationships
md0: BinaryAssociation = BinaryAssociation(
    name="md0",
    ends={
        Property(name="Metadata", type=TestMM2_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="te", type=TestMM2_Metadata, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
te1: BinaryAssociation = BinaryAssociation(
    name="te1",
    ends={
        Property(name="Test", type=TestMM2_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="md", type=TestMM2_Test, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="TestMM2",
    types={TestMM2_Metadata, TestMM2_Test},
    associations={md0, te1},
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