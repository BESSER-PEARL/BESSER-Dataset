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

# Enumerations
ActionType: Enumeration = Enumeration(
    name="ActionType",
    literals={
            EnumerationLiteral(name="comment"),
			EnumerationLiteral(name="copy"),
			EnumerationLiteral(name="click"),
			EnumerationLiteral(name="insert")
    }
)

# Classes
TestMM_Test = Class(name="TestMM::Test")
TestMM_Metadata = Class(name="TestMM::Metadata")
TestMM_Action = Class(name="TestMM::Action")

# TestMM_Test class attributes and methods
TestMM_Test_id: Property = Property(name="id", type=StringType)
TestMM_Test.attributes={TestMM_Test_id}

# TestMM_Metadata class attributes and methods
TestMM_Metadata_user: Property = Property(name="user", type=StringType)
TestMM_Metadata_webpage: Property = Property(name="webpage", type=StringType)
TestMM_Metadata_date: Property = Property(name="date", type=StringType)
TestMM_Metadata_taglist: Property = Property(name="taglist", type=StringType)
TestMM_Metadata.attributes={TestMM_Metadata_taglist, TestMM_Metadata_user, TestMM_Metadata_date, TestMM_Metadata_webpage}

# TestMM_Action class attributes and methods
TestMM_Action_id: Property = Property(name="id", type=StringType)
TestMM_Action_type: Property = Property(name="type", type=StringType)
TestMM_Action_xpath: Property = Property(name="xpath", type=StringType)
TestMM_Action_value: Property = Property(name="value", type=StringType)
TestMM_Action_description: Property = Property(name="description", type=StringType)
TestMM_Action.attributes={TestMM_Action_id, TestMM_Action_description, TestMM_Action_xpath, TestMM_Action_type, TestMM_Action_value}

# Relationships
md0: BinaryAssociation = BinaryAssociation(
    name="md0",
    ends={
        Property(name="Metadata", type=TestMM_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="te", type=TestMM_Metadata, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
act1: BinaryAssociation = BinaryAssociation(
    name="act1",
    ends={
        Property(name="te2", type=TestMM_Action, multiplicity=Multiplicity(1, 9999), is_composite=True),
        Property(name="Action", type=TestMM_Test, multiplicity=Multiplicity(1, 1))
    }
)
te3: BinaryAssociation = BinaryAssociation(
    name="te3",
    ends={
        Property(name="md", type=TestMM_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="Test", type=TestMM_Metadata, multiplicity=Multiplicity(1, 1))
    }
)
te4: BinaryAssociation = BinaryAssociation(
    name="te4",
    ends={
        Property(name="Test5", type=TestMM_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="act", type=TestMM_Test, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="TestMM",
    types={TestMM_Test, TestMM_Metadata, TestMM_Action, ActionType},
    associations={md0, act1, te3, te4},
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