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
xunit_TestCase = Class(name="xunit::TestCase")
xunit_Assertion = Class(name="xunit::Assertion")
xunit_ExpectedValue = Class(name="xunit::ExpectedValue")
xunit_Action = Class(name="xunit::Action")
xunit_DataValue = Class(name="xunit::DataValue")
xunit_NamedElement = Class(name="xunit::NamedElement")
xunit_TestSuite = Class(name="xunit::TestSuite")
NamedElement = Class(name="NamedElement")
DataValue = Class(name="DataValue")

# xunit_TestCase class attributes and methods

# xunit_Assertion class attributes and methods
xunit_Assertion_type: Property = Property(name="type", type=StringType)
xunit_Assertion.attributes={xunit_Assertion_type}

# xunit_ExpectedValue class attributes and methods

# xunit_Action class attributes and methods
xunit_Action_desc: Property = Property(name="desc", type=StringType)
xunit_Action.attributes={xunit_Action_desc}

# xunit_DataValue class attributes and methods
xunit_DataValue_value: Property = Property(name="value", type=StringType)
xunit_DataValue.attributes={xunit_DataValue_value}

# xunit_NamedElement class attributes and methods
xunit_NamedElement_name: Property = Property(name="name", type=StringType)
xunit_NamedElement.attributes={xunit_NamedElement_name}

# xunit_TestSuite class attributes and methods

# NamedElement class attributes and methods

# DataValue class attributes and methods

# Relationships
testCase0: BinaryAssociation = BinaryAssociation(
    name="testCase0",
    ends={
        Property(name="xunit_TestCase", type=xunit_TestSuite, multiplicity=Multiplicity(1, 1)),
        Property(name="xunit_TestSuite", type=xunit_TestCase, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
assertion1: BinaryAssociation = BinaryAssociation(
    name="assertion1",
    ends={
        Property(name="xunit_Assertion", type=xunit_TestCase, multiplicity=Multiplicity(1, 1)),
        Property(name="xunit_TestCase2", type=xunit_Assertion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
testSuite3: BinaryAssociation = BinaryAssociation(
    name="testSuite3",
    ends={
        Property(name="xunit_TestSuite5", type=xunit_TestCase, multiplicity=Multiplicity(1, 1)),
        Property(name="xunit_TestCase4", type=xunit_TestSuite, multiplicity=Multiplicity(0, 1))
    }
)
expectedValue6: BinaryAssociation = BinaryAssociation(
    name="expectedValue6",
    ends={
        Property(name="xunit_ExpectedValue", type=xunit_Assertion, multiplicity=Multiplicity(1, 1)),
        Property(name="xunit_Assertion7", type=xunit_ExpectedValue, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action8: BinaryAssociation = BinaryAssociation(
    name="action8",
    ends={
        Property(name="xunit_Action", type=xunit_Assertion, multiplicity=Multiplicity(1, 1)),
        Property(name="xunit_Assertion9", type=xunit_Action, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
testCase10: BinaryAssociation = BinaryAssociation(
    name="testCase10",
    ends={
        Property(name="xunit_TestCase12", type=xunit_Assertion, multiplicity=Multiplicity(1, 1)),
        Property(name="xunit_Assertion11", type=xunit_TestCase, multiplicity=Multiplicity(0, 1))
    }
)
assertion13: BinaryAssociation = BinaryAssociation(
    name="assertion13",
    ends={
        Property(name="xunit_Assertion15", type=xunit_ExpectedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="xunit_ExpectedValue14", type=xunit_Assertion, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_xunit_TestCase_NamedElement = Generalization(general=NamedElement, specific=xunit_TestCase)
gen_xunit_Assertion_NamedElement = Generalization(general=NamedElement, specific=xunit_Assertion)
gen_xunit_TestSuite_NamedElement = Generalization(general=NamedElement, specific=xunit_TestSuite)
gen_xunit_ExpectedValue_DataValue = Generalization(general=DataValue, specific=xunit_ExpectedValue)

# Domain Model
domain_model = DomainModel(
    name="xunit",
    types={xunit_TestCase, xunit_Assertion, xunit_ExpectedValue, xunit_Action, xunit_DataValue, xunit_NamedElement, xunit_TestSuite, NamedElement, DataValue},
    associations={testCase0, assertion1, testSuite3, expectedValue6, action8, testCase10, assertion13},
    generalizations={gen_xunit_TestCase_NamedElement, gen_xunit_Assertion_NamedElement, gen_xunit_TestSuite_NamedElement, gen_xunit_ExpectedValue_DataValue},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)