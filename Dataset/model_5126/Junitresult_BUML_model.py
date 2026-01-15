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
junitresult_Skipped = Class(name="junitresult::Skipped")
junitresult_Failure = Class(name="junitresult::Failure")
junitresult_Error = Class(name="junitresult::Error")
junitresult_Testsuite = Class(name="junitresult::Testsuite")
AbstractAggregatedTest = Class(name="AbstractAggregatedTest")
junitresult_Property = Class(name="junitresult::Property")
junitresult_Testcase = Class(name="junitresult::Testcase")
NegativeResult = Class(name="NegativeResult")
junitresult_NegativeResult = Class(name="junitresult::NegativeResult", is_abstract=True)
junitresult_Testrun = Class(name="junitresult::Testrun")
junitresult_AbstractAggregatedTest = Class(name="junitresult::AbstractAggregatedTest", is_abstract=True)
JunitResult = Class(name="JunitResult")
junitresult_Testsuites = Class(name="junitresult::Testsuites")
junitresult_JunitResult = Class(name="junitresult::JunitResult", is_abstract=True)

# junitresult_Skipped class attributes and methods

# junitresult_Failure class attributes and methods

# junitresult_Error class attributes and methods

# junitresult_Testsuite class attributes and methods
junitresult_Testsuite_system_out: Property = Property(name="system_out", type=StringType)
junitresult_Testsuite_system_err: Property = Property(name="system_err", type=StringType)
junitresult_Testsuite_hostname: Property = Property(name="hostname", type=StringType)
junitresult_Testsuite_timestamp: Property = Property(name="timestamp", type=DateType)
junitresult_Testsuite_time: Property = Property(name="time", type=FloatType)
junitresult_Testsuite_id: Property = Property(name="id", type=IntegerType)
junitresult_Testsuite_package: Property = Property(name="package", type=StringType)
junitresult_Testsuite_disabled: Property = Property(name="disabled", type=IntegerType)
junitresult_Testsuite_skipped: Property = Property(name="skipped", type=IntegerType)
junitresult_Testsuite.attributes={junitresult_Testsuite_hostname, junitresult_Testsuite_timestamp, junitresult_Testsuite_system_out, junitresult_Testsuite_id, junitresult_Testsuite_time, junitresult_Testsuite_disabled, junitresult_Testsuite_package, junitresult_Testsuite_skipped, junitresult_Testsuite_system_err}

# AbstractAggregatedTest class attributes and methods

# junitresult_Property class attributes and methods
junitresult_Property_name: Property = Property(name="name", type=StringType)
junitresult_Property_value: Property = Property(name="value", type=StringType)
junitresult_Property.attributes={junitresult_Property_value, junitresult_Property_name}

# junitresult_Testcase class attributes and methods
junitresult_Testcase_name: Property = Property(name="name", type=StringType)
junitresult_Testcase_classname: Property = Property(name="classname", type=StringType)
junitresult_Testcase_time: Property = Property(name="time", type=FloatType)
junitresult_Testcase_system_out: Property = Property(name="system_out", type=StringType)
junitresult_Testcase_system_err: Property = Property(name="system_err", type=StringType)
junitresult_Testcase_status: Property = Property(name="status", type=StringType)
junitresult_Testcase_assertions: Property = Property(name="assertions", type=StringType)
junitresult_Testcase.attributes={junitresult_Testcase_assertions, junitresult_Testcase_system_out, junitresult_Testcase_time, junitresult_Testcase_classname, junitresult_Testcase_status, junitresult_Testcase_name, junitresult_Testcase_system_err}

# NegativeResult class attributes and methods

# junitresult_NegativeResult class attributes and methods
junitresult_NegativeResult_message: Property = Property(name="message", type=StringType)
junitresult_NegativeResult_type: Property = Property(name="type", type=StringType)
junitresult_NegativeResult_value: Property = Property(name="value", type=StringType)
junitresult_NegativeResult.attributes={junitresult_NegativeResult_type, junitresult_NegativeResult_value, junitresult_NegativeResult_message}

# junitresult_Testrun class attributes and methods
junitresult_Testrun_project: Property = Property(name="project", type=StringType)
junitresult_Testrun_started: Property = Property(name="started", type=IntegerType)
junitresult_Testrun_ignored: Property = Property(name="ignored", type=IntegerType)
junitresult_Testrun.attributes={junitresult_Testrun_started, junitresult_Testrun_project, junitresult_Testrun_ignored}

# junitresult_AbstractAggregatedTest class attributes and methods
junitresult_AbstractAggregatedTest_name: Property = Property(name="name", type=StringType)
junitresult_AbstractAggregatedTest_tests: Property = Property(name="tests", type=IntegerType)
junitresult_AbstractAggregatedTest_failures: Property = Property(name="failures", type=IntegerType)
junitresult_AbstractAggregatedTest_errors: Property = Property(name="errors", type=IntegerType)
junitresult_AbstractAggregatedTest.attributes={junitresult_AbstractAggregatedTest_name, junitresult_AbstractAggregatedTest_errors, junitresult_AbstractAggregatedTest_failures, junitresult_AbstractAggregatedTest_tests}

# JunitResult class attributes and methods

# junitresult_Testsuites class attributes and methods
junitresult_Testsuites_time: Property = Property(name="time", type=FloatType)
junitresult_Testsuites_disabled: Property = Property(name="disabled", type=IntegerType)
junitresult_Testsuites.attributes={junitresult_Testsuites_time, junitresult_Testsuites_disabled}

# junitresult_JunitResult class attributes and methods

# Relationships
skipped3: BinaryAssociation = BinaryAssociation(
    name="skipped3",
    ends={
        Property(name="junitresult_Skipped", type=junitresult_Testcase, multiplicity=Multiplicity(1, 1)),
        Property(name="junitresult_Testcase4", type=junitresult_Skipped, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
failures5: BinaryAssociation = BinaryAssociation(
    name="failures5",
    ends={
        Property(name="junitresult_Failure", type=junitresult_Testcase, multiplicity=Multiplicity(1, 1)),
        Property(name="junitresult_Testcase6", type=junitresult_Failure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
errors7: BinaryAssociation = BinaryAssociation(
    name="errors7",
    ends={
        Property(name="junitresult_Error", type=junitresult_Testcase, multiplicity=Multiplicity(1, 1)),
        Property(name="junitresult_Testcase8", type=junitresult_Error, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties0: BinaryAssociation = BinaryAssociation(
    name="properties0",
    ends={
        Property(name="junitresult_Property", type=junitresult_Testsuite, multiplicity=Multiplicity(1, 1)),
        Property(name="junitresult_Testsuite", type=junitresult_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
testcases1: BinaryAssociation = BinaryAssociation(
    name="testcases1",
    ends={
        Property(name="junitresult_Testcase", type=junitresult_Testsuite, multiplicity=Multiplicity(1, 1)),
        Property(name="junitresult_Testsuite2", type=junitresult_Testcase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
testsuites9: BinaryAssociation = BinaryAssociation(
    name="testsuites9",
    ends={
        Property(name="junitresult_Testsuite10", type=junitresult_AbstractAggregatedTest, multiplicity=Multiplicity(1, 1)),
        Property(name="junitresult_AbstractAggregatedTest", type=junitresult_Testsuite, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_junitresult_Testsuite_AbstractAggregatedTest = Generalization(general=AbstractAggregatedTest, specific=junitresult_Testsuite)
gen_junitresult_Error_NegativeResult = Generalization(general=NegativeResult, specific=junitresult_Error)
gen_junitresult_Failure_NegativeResult = Generalization(general=NegativeResult, specific=junitresult_Failure)
gen_junitresult_Testrun_AbstractAggregatedTest = Generalization(general=AbstractAggregatedTest, specific=junitresult_Testrun)
gen_junitresult_AbstractAggregatedTest_JunitResult = Generalization(general=JunitResult, specific=junitresult_AbstractAggregatedTest)
gen_junitresult_Testsuites_AbstractAggregatedTest = Generalization(general=AbstractAggregatedTest, specific=junitresult_Testsuites)
gen_junitresult_Skipped_NegativeResult = Generalization(general=NegativeResult, specific=junitresult_Skipped)

# Domain Model
domain_model = DomainModel(
    name="junitresult",
    types={junitresult_Skipped, junitresult_Failure, junitresult_Error, junitresult_Testsuite, AbstractAggregatedTest, junitresult_Property, junitresult_Testcase, NegativeResult, junitresult_NegativeResult, junitresult_Testrun, junitresult_AbstractAggregatedTest, JunitResult, junitresult_Testsuites, junitresult_JunitResult},
    associations={skipped3, failures5, errors7, properties0, testcases1, testsuites9},
    generalizations={gen_junitresult_Testsuite_AbstractAggregatedTest, gen_junitresult_Error_NegativeResult, gen_junitresult_Failure_NegativeResult, gen_junitresult_Testrun_AbstractAggregatedTest, gen_junitresult_AbstractAggregatedTest_JunitResult, gen_junitresult_Testsuites_AbstractAggregatedTest, gen_junitresult_Skipped_NegativeResult},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)