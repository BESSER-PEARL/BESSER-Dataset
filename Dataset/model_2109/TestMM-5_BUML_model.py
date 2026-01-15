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
            EnumerationLiteral(name="insert"),
			EnumerationLiteral(name="comment"),
			EnumerationLiteral(name="copy"),
			EnumerationLiteral(name="click")
    }
)

# Classes
TestMM5_TestSet = Class(name="TestMM5::TestSet")
TestMM5_Test = Class(name="TestMM5::Test")
TestMM5_Metadata = Class(name="TestMM5::Metadata")
TestMM5_Action = Class(name="TestMM5::Action")

# TestMM5_TestSet class attributes and methods
TestMM5_TestSet_name: Property = Property(name="name", type=StringType)
TestMM5_TestSet.attributes={TestMM5_TestSet_name}

# TestMM5_Test class attributes and methods
TestMM5_Test_id: Property = Property(name="id", type=StringType)
TestMM5_Test.attributes={TestMM5_Test_id}

# TestMM5_Metadata class attributes and methods
TestMM5_Metadata_user: Property = Property(name="user", type=StringType)
TestMM5_Metadata_webpage: Property = Property(name="webpage", type=StringType)
TestMM5_Metadata_date: Property = Property(name="date", type=StringType)
TestMM5_Metadata_taglist: Property = Property(name="taglist", type=StringType)
TestMM5_Metadata.attributes={TestMM5_Metadata_date, TestMM5_Metadata_taglist, TestMM5_Metadata_user, TestMM5_Metadata_webpage}

# TestMM5_Action class attributes and methods
TestMM5_Action_xpath: Property = Property(name="xpath", type=StringType)
TestMM5_Action_value: Property = Property(name="value", type=StringType)
TestMM5_Action_description: Property = Property(name="description", type=StringType)
TestMM5_Action_id: Property = Property(name="id", type=StringType)
TestMM5_Action_type: Property = Property(name="type", type=StringType)
TestMM5_Action.attributes={TestMM5_Action_xpath, TestMM5_Action_type, TestMM5_Action_value, TestMM5_Action_id, TestMM5_Action_description}

# Relationships
ts0: BinaryAssociation = BinaryAssociation(
    name="ts0",
    ends={
        Property(name="Test", type=TestMM5_TestSet, multiplicity=Multiplicity(1, 1)),
        Property(name="tst", type=TestMM5_Test, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tst1: BinaryAssociation = BinaryAssociation(
    name="tst1",
    ends={
        Property(name="TestSet", type=TestMM5_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="ts", type=TestMM5_TestSet, multiplicity=Multiplicity(1, 1))
    }
)
md2: BinaryAssociation = BinaryAssociation(
    name="md2",
    ends={
        Property(name="Metadata", type=TestMM5_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="te", type=TestMM5_Metadata, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
te5: BinaryAssociation = BinaryAssociation(
    name="te5",
    ends={
        Property(name="Test6", type=TestMM5_Metadata, multiplicity=Multiplicity(1, 1)),
        Property(name="md", type=TestMM5_Test, multiplicity=Multiplicity(1, 1))
    }
)
act3: BinaryAssociation = BinaryAssociation(
    name="act3",
    ends={
        Property(name="Action", type=TestMM5_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="te4", type=TestMM5_Action, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
te7: BinaryAssociation = BinaryAssociation(
    name="te7",
    ends={
        Property(name="Test8", type=TestMM5_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="act", type=TestMM5_Test, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="TestMM5",
    types={TestMM5_TestSet, TestMM5_Test, TestMM5_Metadata, TestMM5_Action, ActionType},
    associations={ts0, tst1, md2, te5, act3, te7},
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