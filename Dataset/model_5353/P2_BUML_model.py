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
RepositoryType: Enumeration = Enumeration(
    name="RepositoryType",
    literals={
            EnumerationLiteral(name="Metadata"),
			EnumerationLiteral(name="Artifact"),
			EnumerationLiteral(name="Combined")
    }
)

VersionSegment: Enumeration = Enumeration(
    name="VersionSegment",
    literals={
            EnumerationLiteral(name="Major"),
			EnumerationLiteral(name="Minor"),
			EnumerationLiteral(name="Micro"),
			EnumerationLiteral(name="Qualifier")
    }
)

RequirementType: Enumeration = Enumeration(
    name="RequirementType",
    literals={
            EnumerationLiteral(name="NONE"),
			EnumerationLiteral(name="FEATURE"),
			EnumerationLiteral(name="PROJECT")
    }
)

# Classes
p2_Configuration = Class(name="p2::Configuration")
p2_ProfileDefinition = Class(name="p2::ProfileDefinition")
ModelElement = Class(name="ModelElement")
p2_Requirement = Class(name="p2::Requirement")
p2_Repository = Class(name="p2::Repository")
p2_RepositoryList = Class(name="p2::RepositoryList")

# p2_Configuration class attributes and methods
p2_Configuration_wS: Property = Property(name="wS", type=StringType)
p2_Configuration_oS: Property = Property(name="oS", type=StringType)
p2_Configuration_arch: Property = Property(name="arch", type=StringType)
p2_Configuration.attributes={p2_Configuration_wS, p2_Configuration_arch, p2_Configuration_oS}

# p2_ProfileDefinition class attributes and methods
p2_ProfileDefinition_includeSourceBundles: Property = Property(name="includeSourceBundles", type=BooleanType)
p2_ProfileDefinition_m_setRequirements: Method = Method(name="setRequirements", parameters={Parameter(name='requirements')})
p2_ProfileDefinition_m_setRepositories: Method = Method(name="setRepositories", parameters={Parameter(name='repositories')})
p2_ProfileDefinition.attributes={p2_ProfileDefinition_includeSourceBundles}
p2_ProfileDefinition.methods={p2_ProfileDefinition_m_setRequirements, p2_ProfileDefinition_m_setRepositories}

# ModelElement class attributes and methods

# p2_Requirement class attributes and methods
p2_Requirement_iD: Property = Property(name="iD", type=StringType)
p2_Requirement_name: Property = Property(name="name", type=StringType)
p2_Requirement_namespace: Property = Property(name="namespace", type=StringType)
p2_Requirement_versionRange: Property = Property(name="versionRange", type=StringType)
p2_Requirement_optional: Property = Property(name="optional", type=BooleanType)
p2_Requirement_greedy: Property = Property(name="greedy", type=BooleanType)
p2_Requirement_filter: Property = Property(name="filter", type=StringType)
p2_Requirement_type: Property = Property(name="type", type=StringType)
p2_Requirement_m_setVersionRange: Method = Method(name="setVersionRange", parameters={Parameter(name='segment'), Parameter(name='version')})
p2_Requirement.attributes={p2_Requirement_versionRange, p2_Requirement_greedy, p2_Requirement_type, p2_Requirement_optional, p2_Requirement_name, p2_Requirement_namespace, p2_Requirement_iD, p2_Requirement_filter}
p2_Requirement.methods={p2_Requirement_m_setVersionRange}

# p2_Repository class attributes and methods
p2_Repository_type: Property = Property(name="type", type=StringType)
p2_Repository_uRL: Property = Property(name="uRL", type=StringType)
p2_Repository.attributes={p2_Repository_uRL, p2_Repository_type}

# p2_RepositoryList class attributes and methods
p2_RepositoryList_name: Property = Property(name="name", type=StringType)
p2_RepositoryList.attributes={p2_RepositoryList_name}

# Relationships
requirements0: BinaryAssociation = BinaryAssociation(
    name="requirements0",
    ends={
        Property(name="p2_Requirement", type=p2_ProfileDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_ProfileDefinition", type=p2_Requirement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repositories1: BinaryAssociation = BinaryAssociation(
    name="repositories1",
    ends={
        Property(name="p2_Repository", type=p2_ProfileDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_ProfileDefinition2", type=p2_Repository, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repositories3: BinaryAssociation = BinaryAssociation(
    name="repositories3",
    ends={
        Property(name="p2_Repository4", type=p2_RepositoryList, multiplicity=Multiplicity(1, 1)),
        Property(name="p2_RepositoryList", type=p2_Repository, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_p2_Configuration_ModelElement = Generalization(general=ModelElement, specific=p2_Configuration)
gen_p2_Requirement_ModelElement = Generalization(general=ModelElement, specific=p2_Requirement)
gen_p2_ProfileDefinition_ModelElement = Generalization(general=ModelElement, specific=p2_ProfileDefinition)
gen_p2_RepositoryList_ModelElement = Generalization(general=ModelElement, specific=p2_RepositoryList)
gen_p2_Repository_ModelElement = Generalization(general=ModelElement, specific=p2_Repository)

# Domain Model
domain_model = DomainModel(
    name="p2",
    types={p2_Configuration, p2_ProfileDefinition, ModelElement, p2_Requirement, p2_Repository, p2_RepositoryList, RepositoryType, VersionSegment, RequirementType},
    associations={requirements0, repositories1, repositories3},
    generalizations={gen_p2_Configuration_ModelElement, gen_p2_Requirement_ModelElement, gen_p2_ProfileDefinition_ModelElement, gen_p2_RepositoryList_ModelElement, gen_p2_Repository_ModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)