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
maven_GroupAndArtifact = Class(name="maven_GroupAndArtifact")
maven_MapEntry = Class(name="maven_MapEntry")
GroupAndArtifact = Class(name="GroupAndArtifact")
maven_MavenProvider = Class(name="maven_MavenProvider")
Provider = Class(name="Provider")
maven_Scopes = Class(name="maven_Scopes")
maven_Scope = Class(name="maven_Scope")
maven_Mappings = Class(name="maven_Mappings")
maven_Transform = Class(name="maven_Transform")

# maven_GroupAndArtifact class attributes and methods
maven_GroupAndArtifact_artifactId: Property = Property(name="artifactId", type=StringType)
maven_GroupAndArtifact_groupId: Property = Property(name="groupId", type=StringType)
maven_GroupAndArtifact_m_isMatchFor: Method = Method(name="isMatchFor", parameters={Parameter(name='maven_artifact', type=StringType), Parameter(name='maven_group', type=StringType)}, type=BooleanType)
maven_GroupAndArtifact.attributes={maven_GroupAndArtifact_artifactId, maven_GroupAndArtifact_groupId}
maven_GroupAndArtifact.methods={maven_GroupAndArtifact_m_isMatchFor}

# maven_MapEntry class attributes and methods
maven_MapEntry_name: Property = Property(name="name", type=StringType)
maven_MapEntry.attributes={maven_MapEntry_name}

# GroupAndArtifact class attributes and methods

# maven_MavenProvider class attributes and methods
maven_MavenProvider_transitive: Property = Property(name="transitive", type=BooleanType)
maven_MavenProvider_m_getComponentName: Method = Method(name="getComponentName", parameters={Parameter(name='maven_artifactId', type=StringType), Parameter(name='maven_groupId', type=StringType)}, type=StringType)
maven_MavenProvider_m_getMapEntry: Method = Method(name="getMapEntry", parameters={Parameter(name='maven_name', type=StringType)}, type=StringType)
maven_MavenProvider.attributes={maven_MavenProvider_transitive}
maven_MavenProvider.methods={maven_MavenProvider_m_getMapEntry, maven_MavenProvider_m_getComponentName}

# Provider class attributes and methods

# maven_Scopes class attributes and methods

# maven_Scope class attributes and methods
maven_Scope_name: Property = Property(name="name", type=StringType)
maven_Scope_exclude: Property = Property(name="exclude", type=BooleanType)
maven_Scope.attributes={maven_Scope_exclude, maven_Scope_name}

# maven_Mappings class attributes and methods

# maven_Transform class attributes and methods

# Relationships
mappings5: BinaryAssociation = BinaryAssociation(
    name="mappings5",
    ends={
        Property(name="maven_Mappings6", type=maven_MavenProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="maven_MavenProvider", type=maven_Mappings, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scopes7: BinaryAssociation = BinaryAssociation(
    name="scopes7",
    ends={
        Property(name="maven_Scopes", type=maven_MavenProvider, multiplicity=Multiplicity(1, 1)),
        Property(name="maven_MavenProvider8", type=maven_Scopes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scope9: BinaryAssociation = BinaryAssociation(
    name="scope9",
    ends={
        Property(name="maven_Scope", type=maven_Scopes, multiplicity=Multiplicity(1, 1)),
        Property(name="maven_Scopes10", type=maven_Scope, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aliases0: BinaryAssociation = BinaryAssociation(
    name="aliases0",
    ends={
        Property(name="maven_GroupAndArtifact", type=maven_MapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="maven_MapEntry", type=maven_GroupAndArtifact, multiplicity=Multiplicity(0, 9999))
    }
)
entries1: BinaryAssociation = BinaryAssociation(
    name="entries1",
    ends={
        Property(name="maven_MapEntry2", type=maven_Mappings, multiplicity=Multiplicity(1, 1)),
        Property(name="maven_Mappings", type=maven_MapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rules3: BinaryAssociation = BinaryAssociation(
    name="rules3",
    ends={
        Property(name="maven_Transform", type=maven_Mappings, multiplicity=Multiplicity(1, 1)),
        Property(name="maven_Mappings4", type=maven_Transform, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_maven_MapEntry_GroupAndArtifact = Generalization(general=GroupAndArtifact, specific=maven_MapEntry)
gen_maven_MavenProvider_Provider = Generalization(general=Provider, specific=maven_MavenProvider)

# Domain Model
domain_model = DomainModel(
    name="maven",
    types={maven_GroupAndArtifact, maven_MapEntry, GroupAndArtifact, maven_MavenProvider, Provider, maven_Scopes, maven_Scope, maven_Mappings, maven_Transform},
    associations={mappings5, scopes7, scope9, aliases0, entries1, rules3},
    generalizations={gen_maven_MapEntry_GroupAndArtifact, gen_maven_MavenProvider_Provider},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)