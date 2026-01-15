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
TestMM1_Action = Class(name="TestMM1::Action")
TestMM1_Test = Class(name="TestMM1::Test")

# TestMM1_Action class attributes and methods
TestMM1_Action_id: Property = Property(name="id", type=StringType)
TestMM1_Action_type: Property = Property(name="type", type=StringType)
TestMM1_Action_xpath: Property = Property(name="xpath", type=StringType)
TestMM1_Action_value: Property = Property(name="value", type=StringType)
TestMM1_Action_description: Property = Property(name="description", type=StringType)
TestMM1_Action.attributes={TestMM1_Action_value, TestMM1_Action_type, TestMM1_Action_id, TestMM1_Action_description, TestMM1_Action_xpath}

# TestMM1_Test class attributes and methods
TestMM1_Test_id: Property = Property(name="id", type=StringType)
TestMM1_Test.attributes={TestMM1_Test_id}

# Relationships
act0: BinaryAssociation = BinaryAssociation(
    name="act0",
    ends={
        Property(name="Action", type=TestMM1_Test, multiplicity=Multiplicity(1, 1)),
        Property(name="te", type=TestMM1_Action, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
te1: BinaryAssociation = BinaryAssociation(
    name="te1",
    ends={
        Property(name="Test", type=TestMM1_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="act", type=TestMM1_Test, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="TestMM1",
    types={TestMM1_Action, TestMM1_Test, ActionType},
    associations={act0, te1},
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