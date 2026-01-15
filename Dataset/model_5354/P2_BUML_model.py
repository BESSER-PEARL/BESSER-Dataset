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
UnitVerificationState: Enumeration = Enumeration(
    name="UnitVerificationState",
    literals={
            EnumerationLiteral(name="UNKNOWN"),
			EnumerationLiteral(name="VERIFIED"),
			EnumerationLiteral(name="UPGRADED")
    }
)

# Classes
p2_DocumentRoot = Class(name="p2::DocumentRoot")
p2_UnitType = Class(name="p2::UnitType")
p2_RepositoryType = Class(name="p2::RepositoryType")
p2_EStringToStringMapEntry = Class(name="p2::EStringToStringMapEntry")
p2_TargetType = Class(name="p2::TargetType")
p2_LocationsType = Class(name="p2::LocationsType")
p2_LocationType = Class(name="p2::LocationType")
p2_IMetadataRepositoryManager = Class(name="p2::IMetadataRepositoryManager", is_abstract=True)
p2_IMetadataRepository = Class(name="p2::IMetadataRepository", is_abstract=True)
p2_IArtifactRepositoryManager = Class(name="p2::IArtifactRepositoryManager", is_abstract=True)
p2_IArtifactRepository = Class(name="p2::IArtifactRepository", is_abstract=True)

# p2_DocumentRoot class attributes and methods
p2_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
p2_DocumentRoot.attributes={p2_DocumentRoot_mixed}

# p2_UnitType class attributes and methods
p2_UnitType_id: Property = Property(name="id", type=StringType)
p2_UnitType_version: Property = Property(name="version", type=StringType)
p2_UnitType_state: Property = Property(name="state", type=StringType)
p2_UnitType_m_verifyIU: Method = Method(name="verifyIU", parameters={})
p2_UnitType.attributes={p2_UnitType_version, p2_UnitType_id, p2_UnitType_state}
p2_UnitType.methods={p2_UnitType_m_verifyIU}

# p2_RepositoryType class attributes and methods
p2_RepositoryType_location: Property = Property(name="location", type=StringType)
p2_RepositoryType.attributes={p2_RepositoryType_location}

# p2_EStringToStringMapEntry class attributes and methods

# p2_TargetType class attributes and methods
p2_TargetType_sequenceNumber: Property = Property(name="sequenceNumber", type=StringType)
p2_TargetType_name: Property = Property(name="name", type=StringType)
p2_TargetType_m_metadataRepositoryManager: Method = Method(name="metadataRepositoryManager", parameters={}, type=StringType)
p2_TargetType_m_artifactRepositoryManager: Method = Method(name="artifactRepositoryManager", parameters={}, type=StringType)
p2_TargetType.attributes={p2_TargetType_sequenceNumber, p2_TargetType_name}
p2_TargetType.methods={p2_TargetType_m_metadataRepositoryManager, p2_TargetType_m_artifactRepositoryManager}

# p2_LocationsType class attributes and methods

# p2_LocationType class attributes and methods
p2_LocationType_includeAllPlatforms: Property = Property(name="includeAllPlatforms", type=StringType)
p2_LocationType_includeConfigurePhase: Property = Property(name="includeConfigurePhase", type=StringType)
p2_LocationType_includeMode: Property = Property(name="includeMode", type=StringType)
p2_LocationType_includeSource: Property = Property(name="includeSource", type=StringType)
p2_LocationType_type: Property = Property(name="type", type=StringType)
p2_LocationType_m_metadataRepository: Method = Method(name="metadataRepository", parameters={}, type=StringType)
p2_LocationType_m_artifactRepository: Method = Method(name="artifactRepository", parameters={}, type=StringType)
p2_LocationType.attributes={p2_LocationType_type, p2_LocationType_includeConfigurePhase, p2_LocationType_includeSource, p2_LocationType_includeMode, p2_LocationType_includeAllPlatforms}
p2_LocationType.methods={p2_LocationType_m_artifactRepository, p2_LocationType_m_metadataRepository}

# p2_IMetadataRepositoryManager class attributes and methods

# p2_IMetadataRepository class attributes and methods

# p2_IArtifactRepositoryManager class attributes and methods

# p2_IArtifactRepository class attributes and methods

# Relationships
unit7: BinaryAssociation = BinaryAssociation(
    name="unit7",
    ends={
        Property(name="p2_UnitType", type=p2_LocationType, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_LocationType8", type=p2_UnitType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
repository9: BinaryAssociation = BinaryAssociation(
    name="repository9",
    ends={
        Property(name="p2_RepositoryType", type=p2_LocationType, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_LocationType10", type=p2_RepositoryType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
xMLNSPrefixMap0: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap0",
    ends={
        Property(name="p2_EStringToStringMapEntry", type=p2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_DocumentRoot", type=p2_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation1: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation1",
    ends={
        Property(name="p2_EStringToStringMapEntry3", type=p2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_DocumentRoot2", type=p2_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target4: BinaryAssociation = BinaryAssociation(
    name="target4",
    ends={
        Property(name="p2_TargetType", type=p2_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_DocumentRoot5", type=p2_TargetType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
location6: BinaryAssociation = BinaryAssociation(
    name="location6",
    ends={
        Property(name="p2_LocationType", type=p2_LocationsType, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_LocationsType", type=p2_LocationType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
locations11: BinaryAssociation = BinaryAssociation(
    name="locations11",
    ends={
        Property(name="p2_LocationsType13", type=p2_TargetType, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_TargetType12", type=p2_LocationsType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="p2",
    types={p2_DocumentRoot, p2_UnitType, p2_RepositoryType, p2_EStringToStringMapEntry, p2_TargetType, p2_LocationsType, p2_LocationType, p2_IMetadataRepositoryManager, p2_IMetadataRepository, p2_IArtifactRepositoryManager, p2_IArtifactRepository, UnitVerificationState},
    associations={unit7, repository9, xMLNSPrefixMap0, xSISchemaLocation1, target4, location6, locations11},
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