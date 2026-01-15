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
ProgressState: Enumeration = Enumeration(
    name="ProgressState",
    literals={
            EnumerationLiteral(name="NOT_STARTED"),
			EnumerationLiteral(name="RUNNING"),
			EnumerationLiteral(name="STOPPED"),
			EnumerationLiteral(name="COMPLETED")
    }
)

ProblemType: Enumeration = Enumeration(
    name="ProblemType",
    literals={
            EnumerationLiteral(name="ERROR"),
			EnumerationLiteral(name="ASSERTION"),
			EnumerationLiteral(name="ASSUMPTION")
    }
)

TestState: Enumeration = Enumeration(
    name="TestState",
    literals={
            EnumerationLiteral(name="NOT_RUN"),
			EnumerationLiteral(name="IGNORED"),
			EnumerationLiteral(name="PASS"),
			EnumerationLiteral(name="FAILURE"),
			EnumerationLiteral(name="ERROR")
    }
)

# Classes
model_TestElement = Class(name="model::TestElement", is_abstract=True)
TestElement = Class(name="TestElement")
model_TestCaseElement = Class(name="model::TestCaseElement")
model_TestRoot = Class(name="model::TestRoot")
TestContainer = Class(name="TestContainer")
model_TestContainer = Class(name="model::TestContainer")
model_TestProblem = Class(name="model::TestProblem")
model_TraceElement = Class(name="model::TraceElement", is_abstract=True)
model_ComparisonProblem = Class(name="model::ComparisonProblem")
TestProblem = Class(name="TestProblem")
model_Metadata = Class(name="model::Metadata")
model_TraceStackframe = Class(name="model::TraceStackframe")
model_TraceException = Class(name="model::TraceException")
TraceElement = Class(name="TraceElement")

# model_TestElement class attributes and methods
model_TestElement_name: Property = Property(name="name", type=StringType)
model_TestElement_description: Property = Property(name="description", type=StringType)
model_TestElement_testState: Property = Property(name="testState", type=StringType)
model_TestElement_elementUnderTest: Property = Property(name="elementUnderTest", type=StringType)
model_TestElement_progressState: Property = Property(name="progressState", type=StringType)
model_TestElement_startTimestamp: Property = Property(name="startTimestamp", type=StringType)
model_TestElement_endTimestamp: Property = Property(name="endTimestamp", type=StringType)
model_TestElement_target: Property = Property(name="target", type=StringType)
model_TestElement_m_isRunning: Method = Method(name="isRunning", parameters={}, type=BooleanType)
model_TestElement_m_isErrorOrFailure: Method = Method(name="isErrorOrFailure", parameters={}, type=BooleanType)
model_TestElement_m_hasWrongAssumption: Method = Method(name="hasWrongAssumption", parameters={}, type=BooleanType)
model_TestElement_m_getDuration: Method = Method(name="getDuration", parameters={}, type=StringType)
model_TestElement_m_getImageDescriptor: Method = Method(name="getImageDescriptor", parameters={}, type=StringType)
model_TestElement_m_open: Method = Method(name="open", parameters={})
model_TestElement_m_getRoot: Method = Method(name="getRoot", parameters={}, type=StringType)
model_TestElement.attributes={model_TestElement_progressState, model_TestElement_endTimestamp, model_TestElement_testState, model_TestElement_elementUnderTest, model_TestElement_name, model_TestElement_startTimestamp, model_TestElement_target, model_TestElement_description}
model_TestElement.methods={model_TestElement_m_getRoot, model_TestElement_m_isErrorOrFailure, model_TestElement_m_getDuration, model_TestElement_m_getImageDescriptor, model_TestElement_m_isRunning, model_TestElement_m_open, model_TestElement_m_hasWrongAssumption}

# TestElement class attributes and methods

# model_TestCaseElement class attributes and methods

# model_TestRoot class attributes and methods
model_TestRoot_testRunner: Property = Property(name="testRunner", type=StringType)
model_TestRoot.attributes={model_TestRoot_testRunner}

# TestContainer class attributes and methods

# model_TestContainer class attributes and methods
model_TestContainer_m_getMergedTestState: Method = Method(name="getMergedTestState", parameters={}, type=StringType)
model_TestContainer_m_getErrorCount: Method = Method(name="getErrorCount", parameters={}, type=IntegerType)
model_TestContainer_m_getFailureCount: Method = Method(name="getFailureCount", parameters={}, type=IntegerType)
model_TestContainer_m_getTestCaseCount: Method = Method(name="getTestCaseCount", parameters={}, type=IntegerType)
model_TestContainer_m_getCompletedCount: Method = Method(name="getCompletedCount", parameters={}, type=IntegerType)
model_TestContainer_m_getIgnoredCount: Method = Method(name="getIgnoredCount", parameters={}, type=IntegerType)
model_TestContainer_m_getAssumptionMismatchCount: Method = Method(name="getAssumptionMismatchCount", parameters={}, type=IntegerType)
model_TestContainer_m_updateProgressState: Method = Method(name="updateProgressState", parameters={})
model_TestContainer.methods={model_TestContainer_m_getErrorCount, model_TestContainer_m_updateProgressState, model_TestContainer_m_getIgnoredCount, model_TestContainer_m_getCompletedCount, model_TestContainer_m_getTestCaseCount, model_TestContainer_m_getFailureCount, model_TestContainer_m_getAssumptionMismatchCount, model_TestContainer_m_getMergedTestState}

# model_TestProblem class attributes and methods
model_TestProblem_message: Property = Property(name="message", type=StringType)
model_TestProblem_problemType: Property = Property(name="problemType", type=StringType)
model_TestProblem_m_getTestElement: Method = Method(name="getTestElement", parameters={}, type=TestElement)
model_TestProblem.attributes={model_TestProblem_message, model_TestProblem_problemType}
model_TestProblem.methods={model_TestProblem_m_getTestElement}

# model_TraceElement class attributes and methods
model_TraceElement_message: Property = Property(name="message", type=StringType)
model_TraceElement_m_getImageDescriptor: Method = Method(name="getImageDescriptor", parameters={}, type=StringType)
model_TraceElement_m_open: Method = Method(name="open", parameters={})
model_TraceElement_m_getProblem: Method = Method(name="getProblem", parameters={}, type=TestProblem)
model_TraceElement.attributes={model_TraceElement_message}
model_TraceElement.methods={model_TraceElement_m_open, model_TraceElement_m_getProblem, model_TraceElement_m_getImageDescriptor}

# model_ComparisonProblem class attributes and methods
model_ComparisonProblem_expected: Property = Property(name="expected", type=StringType)
model_ComparisonProblem_actual: Property = Property(name="actual", type=StringType)
model_ComparisonProblem.attributes={model_ComparisonProblem_actual, model_ComparisonProblem_expected}

# TestProblem class attributes and methods

# model_Metadata class attributes and methods
model_Metadata_key: Property = Property(name="key", type=StringType)
model_Metadata_value: Property = Property(name="value", type=StringType)
model_Metadata.attributes={model_Metadata_key, model_Metadata_value}

# model_TraceStackframe class attributes and methods

# model_TraceException class attributes and methods

# TraceElement class attributes and methods

# Relationships
children2: BinaryAssociation = BinaryAssociation(
    name="children2",
    ends={
        Property(name="TestElement", type=model_TestContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=model_TestElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent0: BinaryAssociation = BinaryAssociation(
    name="parent0",
    ends={
        Property(name="TestContainer", type=model_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=model_TestContainer, multiplicity=Multiplicity(0, 1))
    }
)
problem1: BinaryAssociation = BinaryAssociation(
    name="problem1",
    ends={
        Property(name="model_TestProblem", type=model_TestElement, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TestElement", type=model_TestProblem, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trace3: BinaryAssociation = BinaryAssociation(
    name="trace3",
    ends={
        Property(name="model_TraceElement", type=model_TestProblem, multiplicity=Multiplicity(1, 1)),
        Property(name="model_TestProblem4", type=model_TraceElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_model_TestContainer_TestElement = Generalization(general=TestElement, specific=model_TestContainer)
gen_model_TestCaseElement_TestElement = Generalization(general=TestElement, specific=model_TestCaseElement)
gen_model_TestRoot_TestContainer = Generalization(general=TestContainer, specific=model_TestRoot)
gen_model_ComparisonProblem_TestProblem = Generalization(general=TestProblem, specific=model_ComparisonProblem)
gen_model_TraceStackframe_TraceElement = Generalization(general=TraceElement, specific=model_TraceStackframe)
gen_model_TraceException_TraceElement = Generalization(general=TraceElement, specific=model_TraceException)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_TestElement, TestElement, model_TestCaseElement, model_TestRoot, TestContainer, model_TestContainer, model_TestProblem, model_TraceElement, model_ComparisonProblem, TestProblem, model_Metadata, model_TraceStackframe, model_TraceException, TraceElement, ProgressState, ProblemType, TestState},
    associations={children2, parent0, problem1, trace3},
    generalizations={gen_model_TestContainer_TestElement, gen_model_TestCaseElement_TestElement, gen_model_TestRoot_TestContainer, gen_model_ComparisonProblem_TestProblem, gen_model_TraceStackframe_TraceElement, gen_model_TraceException_TraceElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)