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
junitmodel_JUnitTestCase = Class(name="junitmodel::JUnitTestCase")
TestCaseElement = Class(name="TestCaseElement")
junitmodel_JUnitTestSuite = Class(name="junitmodel::JUnitTestSuite")
TestContainer = Class(name="TestContainer")
junitmodel_JUnitRoot = Class(name="junitmodel::JUnitRoot")
TestRoot = Class(name="TestRoot")
junitmodel_JUnitProblem = Class(name="junitmodel::JUnitProblem")
TestProblem = Class(name="TestProblem")
junitmodel_JUnitComparisonProblem = Class(name="junitmodel::JUnitComparisonProblem")
JUnitProblem = Class(name="JUnitProblem")
ComparisonProblem = Class(name="ComparisonProblem")
junitmodel_JUnitTraceStackframe = Class(name="junitmodel::JUnitTraceStackframe")
TraceStackframe = Class(name="TraceStackframe")

# junitmodel_JUnitTestCase class attributes and methods

# TestCaseElement class attributes and methods

# junitmodel_JUnitTestSuite class attributes and methods

# TestContainer class attributes and methods

# junitmodel_JUnitRoot class attributes and methods

# TestRoot class attributes and methods

# junitmodel_JUnitProblem class attributes and methods
junitmodel_JUnitProblem_lastTraceWasFiltered: Property = Property(name="lastTraceWasFiltered", type=BooleanType)
junitmodel_JUnitProblem.attributes={junitmodel_JUnitProblem_lastTraceWasFiltered}

# TestProblem class attributes and methods

# junitmodel_JUnitComparisonProblem class attributes and methods

# JUnitProblem class attributes and methods

# ComparisonProblem class attributes and methods

# junitmodel_JUnitTraceStackframe class attributes and methods

# TraceStackframe class attributes and methods

# Generalizations
gen_junitmodel_JUnitTestCase_TestCaseElement = Generalization(general=TestCaseElement, specific=junitmodel_JUnitTestCase)
gen_junitmodel_JUnitTestSuite_TestContainer = Generalization(general=TestContainer, specific=junitmodel_JUnitTestSuite)
gen_junitmodel_JUnitRoot_TestRoot = Generalization(general=TestRoot, specific=junitmodel_JUnitRoot)
gen_junitmodel_JUnitProblem_TestProblem = Generalization(general=TestProblem, specific=junitmodel_JUnitProblem)
gen_junitmodel_JUnitComparisonProblem_JUnitProblem = Generalization(general=JUnitProblem, specific=junitmodel_JUnitComparisonProblem)
gen_junitmodel_JUnitComparisonProblem_ComparisonProblem = Generalization(general=ComparisonProblem, specific=junitmodel_JUnitComparisonProblem)
gen_junitmodel_JUnitTraceStackframe_TraceStackframe = Generalization(general=TraceStackframe, specific=junitmodel_JUnitTraceStackframe)

# Domain Model
domain_model = DomainModel(
    name="junitmodel",
    types={junitmodel_JUnitTestCase, TestCaseElement, junitmodel_JUnitTestSuite, TestContainer, junitmodel_JUnitRoot, TestRoot, junitmodel_JUnitProblem, TestProblem, junitmodel_JUnitComparisonProblem, JUnitProblem, ComparisonProblem, junitmodel_JUnitTraceStackframe, TraceStackframe},
    associations={},
    generalizations={gen_junitmodel_JUnitTestCase_TestCaseElement, gen_junitmodel_JUnitTestSuite_TestContainer, gen_junitmodel_JUnitRoot_TestRoot, gen_junitmodel_JUnitProblem_TestProblem, gen_junitmodel_JUnitComparisonProblem_JUnitProblem, gen_junitmodel_JUnitComparisonProblem_ComparisonProblem, gen_junitmodel_JUnitTraceStackframe_TraceStackframe},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)