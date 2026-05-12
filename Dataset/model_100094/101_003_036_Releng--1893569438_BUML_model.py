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
BuildType: Enumeration = Enumeration(
    name="BuildType",
    literals={
            EnumerationLiteral(name="N"),
			EnumerationLiteral(name="I"),
			EnumerationLiteral(name="S"),
			EnumerationLiteral(name="R"),
			EnumerationLiteral(name="M")
    }
)

# Classes
releng_Server = Class(name="releng_Server")
releng_BuildJob = Class(name="releng_BuildJob")
releng_Repository = Class(name="releng_Repository")
releng_Criterion = Class(name="releng_Criterion")
releng_CompositeRepository = Class(name="releng_CompositeRepository")
Repository = Class(name="Repository")
releng_Promotion = Class(name="releng_Promotion")

# releng_Server class attributes and methods
releng_Server_name: Property = Property(name="name", type=StringType)
releng_Server.attributes={releng_Server_name}

# releng_BuildJob class attributes and methods
releng_BuildJob_name: Property = Property(name="name", type=StringType)
releng_BuildJob_sourceBranch: Property = Property(name="sourceBranch", type=StringType)
releng_BuildJob_buckminsterComponent: Property = Property(name="buckminsterComponent", type=StringType)
releng_BuildJob_types: Property = Property(name="types", type=StringType)
releng_BuildJob.attributes={releng_BuildJob_types, releng_BuildJob_sourceBranch, releng_BuildJob_name, releng_BuildJob_buckminsterComponent}

# releng_Repository class attributes and methods
releng_Repository_location: Property = Property(name="location", type=StringType)
releng_Repository.attributes={releng_Repository_location}

# releng_Criterion class attributes and methods
releng_Criterion_description: Property = Property(name="description", type=StringType)
releng_Criterion.attributes={releng_Criterion_description}

# releng_CompositeRepository class attributes and methods

# Repository class attributes and methods

# releng_Promotion class attributes and methods
releng_Promotion_buildType: Property = Property(name="buildType", type=StringType)
releng_Promotion.attributes={releng_Promotion_buildType}

# Relationships
buildJobs0: BinaryAssociation = BinaryAssociation(
    name="buildJobs0",
    ends={
        Property(name="releng_BuildJob", type=releng_Server, multiplicity=Multiplicity(1, 1)),
        Property(name="releng_Server", type=releng_BuildJob, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
repositories1: BinaryAssociation = BinaryAssociation(
    name="repositories1",
    ends={
        Property(name="releng_Repository", type=releng_Server, multiplicity=Multiplicity(1, 1)),
        Property(name="releng_Server2", type=releng_Repository, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
build7: BinaryAssociation = BinaryAssociation(
    name="build7",
    ends={
        Property(name="BuildJob", type=releng_Promotion, multiplicity=Multiplicity(1, 1)),
        Property(name="promotions", type=releng_BuildJob, multiplicity=Multiplicity(0, 1))
    }
)
target8: BinaryAssociation = BinaryAssociation(
    name="target8",
    ends={
        Property(name="releng_Repository9", type=releng_Promotion, multiplicity=Multiplicity(1, 1)),
        Property(name="releng_Promotion", type=releng_Repository, multiplicity=Multiplicity(1, 1))
    }
)
criteria10: BinaryAssociation = BinaryAssociation(
    name="criteria10",
    ends={
        Property(name="releng_Criterion", type=releng_Promotion, multiplicity=Multiplicity(1, 1)),
        Property(name="releng_Promotion11", type=releng_Criterion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements12: BinaryAssociation = BinaryAssociation(
    name="elements12",
    ends={
        Property(name="releng_Repository13", type=releng_CompositeRepository, multiplicity=Multiplicity(1, 1)),
        Property(name="releng_CompositeRepository", type=releng_Repository, multiplicity=Multiplicity(1, 9999))
    }
)
result3: BinaryAssociation = BinaryAssociation(
    name="result3",
    ends={
        Property(name="releng_Repository5", type=releng_BuildJob, multiplicity=Multiplicity(1, 1)),
        Property(name="releng_BuildJob4", type=releng_Repository, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
promotions6: BinaryAssociation = BinaryAssociation(
    name="promotions6",
    ends={
        Property(name="Promotion", type=releng_BuildJob, multiplicity=Multiplicity(1, 1)),
        Property(name="build", type=releng_Promotion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_releng_CompositeRepository_Repository = Generalization(general=Repository, specific=releng_CompositeRepository)

# Domain Model
domain_model = DomainModel(
    name="releng",
    types={releng_Server, releng_BuildJob, releng_Repository, releng_Criterion, releng_CompositeRepository, Repository, releng_Promotion, BuildType},
    associations={buildJobs0, repositories1, build7, target8, criteria10, elements12, result3, promotions6},
    generalizations={gen_releng_CompositeRepository_Repository},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)