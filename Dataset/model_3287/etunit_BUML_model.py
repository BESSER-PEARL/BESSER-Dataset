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
Etunit_TestcaseType = Class(name="Etunit::TestcaseType")
Etunit_TestsuiteType = Class(name="Etunit::TestsuiteType")
Etunit_TestsuitesType = Class(name="Etunit::TestsuitesType")
Etunit_ErrorType = Class(name="Etunit::ErrorType")
Etunit_FailureType = Class(name="Etunit::FailureType")
Etunit_PropertiesType = Class(name="Etunit::PropertiesType")
Etunit_PropertyType = Class(name="Etunit::PropertyType")
Etunit_SkippedType = Class(name="Etunit::SkippedType")

# Etunit_DocumentRoot class attributes and methods
Etunit_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
Etunit_DocumentRoot_systemErr: Property = Property(name="systemErr", type=StringType)
Etunit_DocumentRoot_systemOut: Property = Property(name="systemOut", type=StringType)
Etunit_DocumentRoot.attributes={Etunit_DocumentRoot_systemErr, Etunit_DocumentRoot_mixed, Etunit_DocumentRoot_systemOut}

# Etunit_EStringToStringMapEntry class attributes and methods

# Etunit_TestcaseType class attributes and methods
Etunit_TestcaseType_systemErr: Property = Property(name="systemErr", type=StringType)
Etunit_TestcaseType_assertions: Property = Property(name="assertions", type=StringType)
Etunit_TestcaseType_classname: Property = Property(name="classname", type=StringType)
Etunit_TestcaseType_name: Property = Property(name="name", type=StringType)
Etunit_TestcaseType_status: Property = Property(name="status", type=StringType)
Etunit_TestcaseType_time: Property = Property(name="time", type=StringType)
Etunit_TestcaseType_systemOut: Property = Property(name="systemOut", type=StringType)
Etunit_TestcaseType.attributes={Etunit_TestcaseType_time, Etunit_TestcaseType_assertions, Etunit_TestcaseType_systemErr, Etunit_TestcaseType_name, Etunit_TestcaseType_status, Etunit_TestcaseType_systemOut, Etunit_TestcaseType_classname}

# Etunit_TestsuiteType class attributes and methods
Etunit_TestsuiteType_systemOut: Property = Property(name="systemOut", type=StringType)
Etunit_TestsuiteType_systemErr: Property = Property(name="systemErr", type=StringType)
Etunit_TestsuiteType_disabled: Property = Property(name="disabled", type=StringType)
Etunit_TestsuiteType_errors: Property = Property(name="errors", type=StringType)
Etunit_TestsuiteType_time: Property = Property(name="time", type=StringType)
Etunit_TestsuiteType_timestamp: Property = Property(name="timestamp", type=StringType)
Etunit_TestsuiteType_failures: Property = Property(name="failures", type=StringType)
Etunit_TestsuiteType_hostname: Property = Property(name="hostname", type=StringType)
Etunit_TestsuiteType_id: Property = Property(name="id", type=StringType)
Etunit_TestsuiteType_name: Property = Property(name="name", type=StringType)
Etunit_TestsuiteType_package: Property = Property(name="package", type=StringType)
Etunit_TestsuiteType_skipped: Property = Property(name="skipped", type=StringType)
Etunit_TestsuiteType_tests: Property = Property(name="tests", type=StringType)
Etunit_TestsuiteType.attributes={Etunit_TestsuiteType_name, Etunit_TestsuiteType_hostname, Etunit_TestsuiteType_skipped, Etunit_TestsuiteType_errors, Etunit_TestsuiteType_id, Etunit_TestsuiteType_failures, Etunit_TestsuiteType_time, Etunit_TestsuiteType_timestamp, Etunit_TestsuiteType_systemErr, Etunit_TestsuiteType_disabled, Etunit_TestsuiteType_tests, Etunit_TestsuiteType_systemOut, Etunit_TestsuiteType_package}

# Etunit_TestsuitesType class attributes and methods
Etunit_TestsuitesType_disabled: Property = Property(name="disabled", type=StringType)
Etunit_TestsuitesType_errors: Property = Property(name="errors", type=StringType)
Etunit_TestsuitesType_failures: Property = Property(name="failures", type=StringType)
Etunit_TestsuitesType_name: Property = Property(name="name", type=StringType)
Etunit_TestsuitesType_tests: Property = Property(name="tests", type=StringType)
Etunit_TestsuitesType_time: Property = Property(name="time", type=StringType)
Etunit_TestsuitesType.attributes={Etunit_TestsuitesType_failures, Etunit_TestsuitesType_name, Etunit_TestsuitesType_time, Etunit_TestsuitesType_errors, Etunit_TestsuitesType_disabled, Etunit_TestsuitesType_tests}

# Etunit_ErrorType class attributes and methods
Etunit_ErrorType_mixed: Property = Property(name="mixed", type=StringType)
Etunit_ErrorType_message: Property = Property(name="message", type=StringType)
Etunit_ErrorType_type: Property = Property(name="type", type=StringType)
Etunit_ErrorType.attributes={Etunit_ErrorType_message, Etunit_ErrorType_mixed, Etunit_ErrorType_type}

# Etunit_FailureType class attributes and methods
Etunit_FailureType_mixed: Property = Property(name="mixed", type=StringType)
Etunit_FailureType_message: Property = Property(name="message", type=StringType)
Etunit_FailureType_type: Property = Property(name="type", type=StringType)
Etunit_FailureType.attributes={Etunit_FailureType_message, Etunit_FailureType_type, Etunit_FailureType_mixed}

# Etunit_PropertiesType class attributes and methods

# Etunit_PropertyType class attributes and methods
Etunit_PropertyType_name: Property = Property(name="name", type=StringType)
Etunit_PropertyType_value: Property = Property(name="value", type=StringType)
Etunit_PropertyType.attributes={Etunit_PropertyType_name, Etunit_PropertyType_value}

# Etunit_SkippedType class attributes and methods
Etunit_SkippedType_mixed: Property = Property(name="mixed", type=StringType)
Etunit_SkippedType_message: Property = Property(name="message", type=StringType)
Etunit_SkippedType.attributes={Etunit_SkippedType_message, Etunit_SkippedType_mixed}

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
testcase14: BinaryAssociation = BinaryAssociation(
    name="testcase14",
    ends={
        Property(name="Etunit_TestcaseType", type=Etunit_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Etunit_DocumentRoot15", type=Etunit_TestcaseType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
testsuite16: BinaryAssociation = BinaryAssociation(
    name="testsuite16",
    ends={
        Property(name="Etunit_TestsuiteType", type=Etunit_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Etunit_DocumentRoot17", type=Etunit_TestsuiteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
testsuites18: BinaryAssociation = BinaryAssociation(
    name="testsuites18",
    ends={
        Property(name="Etunit_TestsuitesType", type=Etunit_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Etunit_DocumentRoot19", type=Etunit_TestsuitesType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
error4: BinaryAssociation = BinaryAssociation(
    name="error4",
    ends={
        Property(name="Etunit_ErrorType", type=Etunit_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Etunit_DocumentRoot5", type=Etunit_ErrorType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failure6: BinaryAssociation = BinaryAssociation(
    name="failure6",
    ends={
        Property(name="Etunit_FailureType", type=Etunit_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Etunit_DocumentRoot7", type=Etunit_FailureType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties8: BinaryAssociation = BinaryAssociation(
    name="properties8",
    ends={
        Property(name="Etunit_PropertiesType", type=Etunit_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Etunit_DocumentRoot9", type=Etunit_PropertiesType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property10: BinaryAssociation = BinaryAssociation(
    name="property10",
    ends={
        Property(name="Etunit_PropertyType", type=Etunit_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Etunit_DocumentRoot11", type=Etunit_PropertyType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
skipped12: BinaryAssociation = BinaryAssociation(
    name="skipped12",
    ends={
        Property(name="Etunit_SkippedType", type=Etunit_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="Etunit_DocumentRoot13", type=Etunit_SkippedType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property20: BinaryAssociation = BinaryAssociation(
    name="property20",
    ends={
        Property(name="Etunit_PropertyType22", type=Etunit_PropertiesType, multiplicity=Multiplicity(1, 1)),
        Property(name="Etunit_PropertiesType21", type=Etunit_PropertyType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
skipped23: BinaryAssociation = BinaryAssociation(
    name="skipped23",
    ends={
        Property(name="Etunit_SkippedType25", type=Etunit_TestcaseType, multiplicity=Multiplicity(1, 1)),
        Property(name="Etunit_TestcaseType24", type=Etunit_SkippedType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
error26: BinaryAssociation = BinaryAssociation(
    name="error26",
    ends={
        Property(name="Etunit_ErrorType28", type=Etunit_TestcaseType, multiplicity=Multiplicity(1, 1)),
        Property(name="Etunit_TestcaseType27", type=Etunit_ErrorType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
failure29: BinaryAssociation = BinaryAssociation(
    name="failure29",
    ends={
        Property(name="Etunit_FailureType31", type=Etunit_TestcaseType, multiplicity=Multiplicity(1, 1)),
        Property(name="Etunit_TestcaseType30", type=Etunit_FailureType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties35: BinaryAssociation = BinaryAssociation(
    name="properties35",
    ends={
        Property(name="Etunit_PropertiesType37", type=Etunit_TestsuiteType, multiplicity=Multiplicity(1, 1)),
        Property(name="Etunit_TestsuiteType36", type=Etunit_PropertiesType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
testcase38: BinaryAssociation = BinaryAssociation(
    name="testcase38",
    ends={
        Property(name="Etunit_TestcaseType40", type=Etunit_TestsuiteType, multiplicity=Multiplicity(1, 1)),
        Property(name="Etunit_TestsuiteType39", type=Etunit_TestcaseType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
testsuite32: BinaryAssociation = BinaryAssociation(
    name="testsuite32",
    ends={
        Property(name="Etunit_TestsuiteType34", type=Etunit_TestsuitesType, multiplicity=Multiplicity(1, 1)),
        Property(name="Etunit_TestsuitesType33", type=Etunit_TestsuiteType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Etunit",
    types={Etunit_DocumentRoot, Etunit_EStringToStringMapEntry, Etunit_TestcaseType, Etunit_TestsuiteType, Etunit_TestsuitesType, Etunit_ErrorType, Etunit_FailureType, Etunit_PropertiesType, Etunit_PropertyType, Etunit_SkippedType},
    associations={xMLNSPrefixMap0, xSISchemaLocation1, testcase14, testsuite16, testsuites18, error4, failure6, properties8, property10, skipped12, property20, skipped23, error26, failure29, properties35, testcase38, testsuite32},
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