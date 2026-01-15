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
testing_Adapter = Class(name="testing::Adapter")
testing_Transition = Class(name="testing::Transition")
testing_TestCase = Class(name="testing::TestCase")
testing_TestSuite = Class(name="testing::TestSuite")
testing_TestCoverage = Class(name="testing::TestCoverage")

# testing_Adapter class attributes and methods

# testing_Transition class attributes and methods
testing_Transition_name: Property = Property(name="name", type=StringType)
testing_Transition_type: Property = Property(name="type", type=StringType)
testing_Transition.attributes={testing_Transition_type, testing_Transition_name}

# testing_TestCase class attributes and methods
testing_TestCase_input: Property = Property(name="input", type=StringType)
testing_TestCase_output: Property = Property(name="output", type=StringType)
testing_TestCase.attributes={testing_TestCase_output, testing_TestCase_input}

# testing_TestSuite class attributes and methods
testing_TestSuite_sutName: Property = Property(name="sutName", type=StringType)
testing_TestSuite.attributes={testing_TestSuite_sutName}

# testing_TestCoverage class attributes and methods

# Relationships
adapter1: BinaryAssociation = BinaryAssociation(
    name="adapter1",
    ends={
        Property(name="testing_Adapter", type=testing_TestSuite, multiplicity=Multiplicity(1, 1)),
        Property(name="testing_TestSuite2", type=testing_Adapter, multiplicity=Multiplicity(0, 1))
    }
)
transitions3: BinaryAssociation = BinaryAssociation(
    name="transitions3",
    ends={
        Property(name="testing_Transition", type=testing_Adapter, multiplicity=Multiplicity(1, 1)),
        Property(name="testing_Adapter4", type=testing_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
testCoverages0: BinaryAssociation = BinaryAssociation(
    name="testCoverages0",
    ends={
        Property(name="testing_TestCoverage", type=testing_TestSuite, multiplicity=Multiplicity(1, 1)),
        Property(name="testing_TestSuite", type=testing_TestCoverage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
testCases5: BinaryAssociation = BinaryAssociation(
    name="testCases5",
    ends={
        Property(name="testing_TestCase", type=testing_TestCoverage, multiplicity=Multiplicity(1, 1)),
        Property(name="testing_TestCoverage6", type=testing_TestCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="testing",
    types={testing_Adapter, testing_Transition, testing_TestCase, testing_TestSuite, testing_TestCoverage},
    associations={adapter1, transitions3, testCoverages0, testCases5},
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