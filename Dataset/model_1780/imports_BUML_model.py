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
imports_BookType = Class(name="imports::BookType")
imports_DocumentRoot = Class(name="imports::DocumentRoot")
imports_EStringToStringMapEntry = Class(name="imports::EStringToStringMapEntry")
imports_RootElementType = Class(name="imports::RootElementType")

# imports_BookType class attributes and methods
imports_BookType_author: Property = Property(name="author", type=StringType)
imports_BookType_title: Property = Property(name="title", type=StringType)
imports_BookType_isbn: Property = Property(name="isbn", type=StringType)
imports_BookType.attributes={imports_BookType_author, imports_BookType_isbn, imports_BookType_title}

# imports_DocumentRoot class attributes and methods
imports_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
imports_DocumentRoot.attributes={imports_DocumentRoot_mixed}

# imports_EStringToStringMapEntry class attributes and methods

# imports_RootElementType class attributes and methods
imports_RootElementType_importURI: Property = Property(name="importURI", type=StringType)
imports_RootElementType.attributes={imports_RootElementType_importURI}

# Relationships
rootElement4: BinaryAssociation = BinaryAssociation(
    name="rootElement4",
    ends={
        Property(name="imports_DocumentRoot5", type=imports_RootElementType, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="imports_RootElementType", type=imports_DocumentRoot, multiplicity=Multiplicity(1, 1))
    }
)
xMLNSPrefixMap0: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap0",
    ends={
        Property(name="imports_EStringToStringMapEntry", type=imports_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="imports_DocumentRoot", type=imports_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation1: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation1",
    ends={
        Property(name="imports_EStringToStringMapEntry3", type=imports_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="imports_DocumentRoot2", type=imports_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
book6: BinaryAssociation = BinaryAssociation(
    name="book6",
    ends={
        Property(name="imports_BookType", type=imports_RootElementType, multiplicity=Multiplicity(1, 1)),
        Property(name="imports_RootElementType7", type=imports_BookType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="imports",
    types={imports_BookType, imports_DocumentRoot, imports_EStringToStringMapEntry, imports_RootElementType},
    associations={rootElement4, xMLNSPrefixMap0, xSISchemaLocation1, book6},
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