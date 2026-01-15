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
Etunit_DocumentRoot = Class(name="Etunit::DocumentRoot")
Etunit_EStringToStringMapEntry = Class(name="Etunit::EStringToStringMapEntry")
Etunit_Testsuite = Class(name="Etunit::Testsuite")
Etunit_TestsuitesType = Class(name="Etunit::TestsuitesType")
Etunit_ErrorType = Class(name="Etunit::ErrorType")
Etunit_FailureType = Class(name="Etunit::FailureType")
Etunit_TestcaseType = Class(name="Etunit::TestcaseType")
Etunit_TestsuiteType = Class(name="Etunit::TestsuiteType")
Testsuite = Class(name="Testsuite")

# Etunit_DocumentRoot class attributes and methods
Etunit_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
Etunit_DocumentRoot.attributes={Etunit_DocumentRoot_mixed}

# Etunit_EStringToStringMapEntry class attributes and methods

# Etunit_Testsuite class attributes and methods
Etunit_Testsuite_errors: Property = Property(name="errors", type=StringType)
Etunit_Testsuite_failures: Property = Property(name="failures", type=StringType)
Etunit_Testsuite_name: Property = Property(name="name", type=StringType)
Etunit_Testsuite_skipped: Property = Property(name="skipped", type=StringType)
Etunit_Testsuite_tests: Property = Property(name="tests", type=StringType)
Etunit_Testsuite_time: Property = Property(name="time", type=StringType)
Etunit_Testsuite_timestamp: Property = Property(name="timestamp", type=StringType)
Etunit_Testsuite.attributes={Etunit_Testsuite_skipped, Etunit_Testsuite_time, Etunit_Testsuite_name, Etunit_Testsuite_errors, Etunit_Testsuite_failures, Etunit_Testsuite_timestamp, Etunit_Testsuite_tests}

# Etunit_TestsuitesType class attributes and methods

# Etunit_ErrorType class attributes and methods
Etunit_ErrorType_mixed: Property = Property(name="mixed", type=StringType)
Etunit_ErrorType_expected: Property = Property(name="expected", type=StringType)
Etunit_ErrorType_actual: Property = Property(name="actual", type=StringType)
Etunit_ErrorType.attributes={Etunit_ErrorType_mixed, Etunit_ErrorType_expected, Etunit_ErrorType_actual}

# Etunit_FailureType class attributes and methods
Etunit_FailureType_mixed: Property = Property(name="mixed", type=StringType)
Etunit_FailureType_expected: Property = Property(name="expected", type=StringType)
Etunit_FailureType_actual: Property = Property(name="actual", type=StringType)
Etunit_FailureType.attributes={Etunit_FailureType_expected, Etunit_FailureType_actual, Etunit_FailureType_mixed}

# Etunit_TestcaseType class attributes and methods
Etunit_TestcaseType_classname: Property = Property(name="classname", type=StringType)
Etunit_TestcaseType_name: Property = Property(name="name", type=StringType)
Etunit_TestcaseType_time: Property = Property(name="time", type=StringType)
Etunit_TestcaseType.attributes={Etunit_TestcaseType_name, Etunit_TestcaseType_time, Etunit_TestcaseType_classname}

# Etunit_TestsuiteType class attributes and methods

# Testsuite class attributes and methods

# Relationships
xMLNSPrefixMap0: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap0",
    ends={
        Property(name="Etunit_EStringToStringMapEntry", type=Etunit_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Etunit_DocumentRoot", type=Etunit_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation1: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation1",
    ends={
        Property(name="Etunit_EStringToStringMapEntry3", type=Etunit_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Etunit_DocumentRoot2", type=Etunit_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
testsuite4: BinaryAssociation = BinaryAssociation(
    name="testsuite4",
    ends={
        Property(name="Etunit_Testsuite", type=Etunit_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Etunit_DocumentRoot5", type=Etunit_Testsuite, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
testsuites6: BinaryAssociation = BinaryAssociation(
    name="testsuites6",
    ends={
        Property(name="Etunit_TestsuitesType", type=Etunit_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Etunit_DocumentRoot7", type=Etunit_TestsuitesType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
error8: BinaryAssociation = BinaryAssociation(
    name="error8",
    ends={
        Property(name="Etunit_ErrorType", type=Etunit_TestcaseType, multiplicity=Multiplicity(1, 1)),
        Property(name="Etunit_TestcaseType", type=Etunit_ErrorType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
failure9: BinaryAssociation = BinaryAssociation(
    name="failure9",
    ends={
        Property(name="Etunit_FailureType", type=Etunit_TestcaseType, multiplicity=Multiplicity(1, 1)),
        Property(name="Etunit_TestcaseType10", type=Etunit_FailureType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
testcase11: BinaryAssociation = BinaryAssociation(
    name="testcase11",
    ends={
        Property(name="Etunit_TestcaseType13", type=Etunit_Testsuite, multiplicity=Multiplicity(1, 1)),
        Property(name="Etunit_Testsuite12", type=Etunit_TestcaseType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
testsuite14: BinaryAssociation = BinaryAssociation(
    name="testsuite14",
    ends={
        Property(name="Etunit_TestsuiteType", type=Etunit_TestsuitesType, multiplicity=Multiplicity(1, 1)),
        Property(name="Etunit_TestsuitesType15", type=Etunit_TestsuiteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Etunit_TestsuiteType_Testsuite = Generalization(general=Testsuite, specific=Etunit_TestsuiteType)

# Domain Model
domain_model = DomainModel(
    name="Etunit",
    types={Etunit_DocumentRoot, Etunit_EStringToStringMapEntry, Etunit_Testsuite, Etunit_TestsuitesType, Etunit_ErrorType, Etunit_FailureType, Etunit_TestcaseType, Etunit_TestsuiteType, Testsuite},
    associations={xMLNSPrefixMap0, xSISchemaLocation1, testsuite4, testsuites6, error8, failure9, testcase11, testsuite14},
    generalizations={gen_Etunit_TestsuiteType_Testsuite},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)