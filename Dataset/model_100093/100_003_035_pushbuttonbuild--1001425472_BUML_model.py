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
JreType: Enumeration = Enumeration(
    name="JreType",
    literals={
            EnumerationLiteral(name="J2SE14"),
			EnumerationLiteral(name="J2SE15")
    }
)

# Classes
pushbuttonbuild_BuildType = Class(name="pushbuttonbuild_BuildType")
pushbuttonbuild_ExtraZIPType = Class(name="pushbuttonbuild_ExtraZIPType")
pushbuttonbuild_DocumentRoot = Class(name="pushbuttonbuild_DocumentRoot")
pushbuttonbuild_EStringToStringMapEntry = Class(name="pushbuttonbuild_EStringToStringMapEntry")

# pushbuttonbuild_BuildType class attributes and methods
pushbuttonbuild_BuildType_isIncubation: Property = Property(name="isIncubation", type=StringType)
pushbuttonbuild_BuildType_jre: Property = Property(name="jre", type=StringType)
pushbuttonbuild_BuildType_newsgroupPublisherName: Property = Property(name="newsgroupPublisherName", type=StringType)
pushbuttonbuild_BuildType_newsgroupPublisherEmail: Property = Property(name="newsgroupPublisherEmail", type=StringType)
pushbuttonbuild_BuildType_parentProjectName: Property = Property(name="parentProjectName", type=StringType)
pushbuttonbuild_BuildType_projectNamespace: Property = Property(name="projectNamespace", type=StringType)
pushbuttonbuild_BuildType_shortName: Property = Property(name="shortName", type=StringType)
pushbuttonbuild_BuildType_testsAreJarred: Property = Property(name="testsAreJarred", type=StringType)
pushbuttonbuild_BuildType.attributes={pushbuttonbuild_BuildType_testsAreJarred, pushbuttonbuild_BuildType_isIncubation, pushbuttonbuild_BuildType_projectNamespace, pushbuttonbuild_BuildType_newsgroupPublisherEmail, pushbuttonbuild_BuildType_shortName, pushbuttonbuild_BuildType_newsgroupPublisherName, pushbuttonbuild_BuildType_parentProjectName, pushbuttonbuild_BuildType_jre}

# pushbuttonbuild_ExtraZIPType class attributes and methods
pushbuttonbuild_ExtraZIPType_name: Property = Property(name="name", type=StringType)
pushbuttonbuild_ExtraZIPType.attributes={pushbuttonbuild_ExtraZIPType_name}

# pushbuttonbuild_DocumentRoot class attributes and methods
pushbuttonbuild_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
pushbuttonbuild_DocumentRoot.attributes={pushbuttonbuild_DocumentRoot_mixed}

# pushbuttonbuild_EStringToStringMapEntry class attributes and methods

# Relationships
extraZIP0: BinaryAssociation = BinaryAssociation(
    name="extraZIP0",
    ends={
        Property(name="pushbuttonbuild_ExtraZIPType", type=pushbuttonbuild_BuildType, multiplicity=Multiplicity(1, 1)),
        Property(name="pushbuttonbuild_BuildType", type=pushbuttonbuild_ExtraZIPType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap1: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap1",
    ends={
        Property(name="pushbuttonbuild_EStringToStringMapEntry", type=pushbuttonbuild_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="pushbuttonbuild_DocumentRoot", type=pushbuttonbuild_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation2: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation2",
    ends={
        Property(name="pushbuttonbuild_EStringToStringMapEntry4", type=pushbuttonbuild_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="pushbuttonbuild_DocumentRoot3", type=pushbuttonbuild_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
build5: BinaryAssociation = BinaryAssociation(
    name="build5",
    ends={
        Property(name="pushbuttonbuild_BuildType7", type=pushbuttonbuild_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="pushbuttonbuild_DocumentRoot6", type=pushbuttonbuild_BuildType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extraZIP8: BinaryAssociation = BinaryAssociation(
    name="extraZIP8",
    ends={
        Property(name="pushbuttonbuild_ExtraZIPType10", type=pushbuttonbuild_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="pushbuttonbuild_DocumentRoot9", type=pushbuttonbuild_ExtraZIPType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="pushbuttonbuild",
    types={pushbuttonbuild_BuildType, pushbuttonbuild_ExtraZIPType, pushbuttonbuild_DocumentRoot, pushbuttonbuild_EStringToStringMapEntry, JreType},
    associations={extraZIP0, xMLNSPrefixMap1, xSISchemaLocation2, build5, extraZIP8},
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