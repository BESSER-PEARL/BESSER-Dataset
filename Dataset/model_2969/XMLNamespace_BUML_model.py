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
SpaceType: Enumeration = Enumeration(
    name="SpaceType",
    literals={
            EnumerationLiteral(name="default"),
			EnumerationLiteral(name="preserve")
    }
)

# Classes
namespace_EStringToStringMapEntry = Class(name="namespace::EStringToStringMapEntry")
namespace_XMLNamespaceDocumentRoot = Class(name="namespace::XMLNamespaceDocumentRoot")

# namespace_EStringToStringMapEntry class attributes and methods

# namespace_XMLNamespaceDocumentRoot class attributes and methods
namespace_XMLNamespaceDocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
namespace_XMLNamespaceDocumentRoot_space: Property = Property(name="space", type=StringType)
namespace_XMLNamespaceDocumentRoot_base: Property = Property(name="base", type=StringType)
namespace_XMLNamespaceDocumentRoot_id: Property = Property(name="id", type=StringType)
namespace_XMLNamespaceDocumentRoot_lang: Property = Property(name="lang", type=StringType)
namespace_XMLNamespaceDocumentRoot.attributes={namespace_XMLNamespaceDocumentRoot_space, namespace_XMLNamespaceDocumentRoot_base, namespace_XMLNamespaceDocumentRoot_lang, namespace_XMLNamespaceDocumentRoot_mixed, namespace_XMLNamespaceDocumentRoot_id}

# Relationships
xMLNSPrefixMap0: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap0",
    ends={
        Property(name="namespace_EStringToStringMapEntry", type=namespace_XMLNamespaceDocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace_XMLNamespaceDocumentRoot", type=namespace_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation1: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation1",
    ends={
        Property(name="namespace_EStringToStringMapEntry3", type=namespace_XMLNamespaceDocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace_XMLNamespaceDocumentRoot2", type=namespace_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="namespace",
    types={namespace_EStringToStringMapEntry, namespace_XMLNamespaceDocumentRoot, SpaceType},
    associations={xMLNSPrefixMap0, xSISchemaLocation1},
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