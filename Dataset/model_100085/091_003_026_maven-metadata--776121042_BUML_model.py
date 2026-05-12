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
metadata_DocumentRoot = Class(name="metadata_DocumentRoot")
metadata_EStringToStringMapEntry = Class(name="metadata_EStringToStringMapEntry")
metadata_MetaData = Class(name="metadata_MetaData")
metadata_Versioning = Class(name="metadata_Versioning")
metadata_Versions = Class(name="metadata_Versions")

# metadata_DocumentRoot class attributes and methods
metadata_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
metadata_DocumentRoot.attributes={metadata_DocumentRoot_mixed}

# metadata_EStringToStringMapEntry class attributes and methods

# metadata_MetaData class attributes and methods
metadata_MetaData_groupId: Property = Property(name="groupId", type=StringType)
metadata_MetaData_artifactId: Property = Property(name="artifactId", type=StringType)
metadata_MetaData_version: Property = Property(name="version", type=StringType)
metadata_MetaData.attributes={metadata_MetaData_artifactId, metadata_MetaData_version, metadata_MetaData_groupId}

# metadata_Versioning class attributes and methods
metadata_Versioning_release: Property = Property(name="release", type=StringType)
metadata_Versioning_latest: Property = Property(name="latest", type=StringType)
metadata_Versioning_lastUpdated: Property = Property(name="lastUpdated", type=StringType)
metadata_Versioning.attributes={metadata_Versioning_lastUpdated, metadata_Versioning_release, metadata_Versioning_latest}

# metadata_Versions class attributes and methods
metadata_Versions_version: Property = Property(name="version", type=StringType)
metadata_Versions.attributes={metadata_Versions_version}

# Relationships
xMLNSPrefixMap0: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap0",
    ends={
        Property(name="metadata_EStringToStringMapEntry", type=metadata_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="metadata_DocumentRoot", type=metadata_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation1: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation1",
    ends={
        Property(name="metadata_EStringToStringMapEntry3", type=metadata_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="metadata_DocumentRoot2", type=metadata_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metadata4: BinaryAssociation = BinaryAssociation(
    name="metadata4",
    ends={
        Property(name="metadata_MetaData", type=metadata_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="metadata_DocumentRoot5", type=metadata_MetaData, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
versioning6: BinaryAssociation = BinaryAssociation(
    name="versioning6",
    ends={
        Property(name="metadata_Versioning", type=metadata_MetaData, multiplicity=Multiplicity(1, 1)),
        Property(name="metadata_MetaData7", type=metadata_Versioning, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
versions8: BinaryAssociation = BinaryAssociation(
    name="versions8",
    ends={
        Property(name="metadata_Versions", type=metadata_Versioning, multiplicity=Multiplicity(1, 1)),
        Property(name="metadata_Versioning9", type=metadata_Versions, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="metadata",
    types={metadata_DocumentRoot, metadata_EStringToStringMapEntry, metadata_MetaData, metadata_Versioning, metadata_Versions},
    associations={xMLNSPrefixMap0, xSISchemaLocation1, metadata4, versioning6, versions8},
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