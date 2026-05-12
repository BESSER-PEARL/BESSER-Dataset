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
RequirementSourceConf_RequirementsContainer = Class(name="RequirementSourceConf_RequirementsContainer")
RequirementSourceConf_RequirementSources = Class(name="RequirementSourceConf_RequirementSources")
RequirementSourceConf_RequirementSource = Class(name="RequirementSourceConf_RequirementSource")
RequirementSourceConf_EStringToStringMapEntry = Class(name="RequirementSourceConf_EStringToStringMapEntry")
RequirementSourceConf_MappingElement = Class(name="RequirementSourceConf_MappingElement")
RequirementSourceConf_Scope = Class(name="RequirementSourceConf_Scope")

# RequirementSourceConf_RequirementsContainer class attributes and methods

# RequirementSourceConf_RequirementSources class attributes and methods

# RequirementSourceConf_RequirementSource class attributes and methods
RequirementSourceConf_RequirementSource_name: Property = Property(name="name", type=StringType)
RequirementSourceConf_RequirementSource_connectorId: Property = Property(name="connectorId", type=StringType)
RequirementSourceConf_RequirementSource_dataModelURI: Property = Property(name="dataModelURI", type=StringType)
RequirementSourceConf_RequirementSource_repositoryURI: Property = Property(name="repositoryURI", type=StringType)
RequirementSourceConf_RequirementSource_destinationURI: Property = Property(name="destinationURI", type=StringType)
RequirementSourceConf_RequirementSource.attributes={RequirementSourceConf_RequirementSource_repositoryURI, RequirementSourceConf_RequirementSource_dataModelURI, RequirementSourceConf_RequirementSource_name, RequirementSourceConf_RequirementSource_destinationURI, RequirementSourceConf_RequirementSource_connectorId}

# RequirementSourceConf_EStringToStringMapEntry class attributes and methods

# RequirementSourceConf_MappingElement class attributes and methods

# RequirementSourceConf_Scope class attributes and methods

# Relationships
requirementSources0: BinaryAssociation = BinaryAssociation(
    name="requirementSources0",
    ends={
        Property(name="RequirementSourceConf_RequirementSource", type=RequirementSourceConf_RequirementSources, multiplicity=Multiplicity(1, 1)),
        Property(name="RequirementSourceConf_RequirementSources", type=RequirementSourceConf_RequirementSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contents1: BinaryAssociation = BinaryAssociation(
    name="contents1",
    ends={
        Property(name="RequirementSourceConf_RequirementsContainer", type=RequirementSourceConf_RequirementSource, multiplicity=Multiplicity(1, 1)),
        Property(name="RequirementSourceConf_RequirementSource2", type=RequirementSourceConf_RequirementsContainer, multiplicity=Multiplicity(0, 1))
    }
)
properties3: BinaryAssociation = BinaryAssociation(
    name="properties3",
    ends={
        Property(name="RequirementSourceConf_EStringToStringMapEntry", type=RequirementSourceConf_RequirementSource, multiplicity=Multiplicity(1, 1)),
        Property(name="RequirementSourceConf_RequirementSource4", type=RequirementSourceConf_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mappings5: BinaryAssociation = BinaryAssociation(
    name="mappings5",
    ends={
        Property(name="RequirementSourceConf_MappingElement", type=RequirementSourceConf_RequirementSource, multiplicity=Multiplicity(1, 1)),
        Property(name="RequirementSourceConf_RequirementSource6", type=RequirementSourceConf_MappingElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultScope7: BinaryAssociation = BinaryAssociation(
    name="defaultScope7",
    ends={
        Property(name="RequirementSourceConf_Scope", type=RequirementSourceConf_RequirementSource, multiplicity=Multiplicity(1, 1)),
        Property(name="RequirementSourceConf_RequirementSource8", type=RequirementSourceConf_Scope, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="RequirementSourceConf",
    types={RequirementSourceConf_RequirementsContainer, RequirementSourceConf_RequirementSources, RequirementSourceConf_RequirementSource, RequirementSourceConf_EStringToStringMapEntry, RequirementSourceConf_MappingElement, RequirementSourceConf_Scope},
    associations={requirementSources0, contents1, properties3, mappings5, defaultScope7},
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