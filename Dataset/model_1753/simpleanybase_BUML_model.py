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
simpleany_Description = Class(name="simpleany::Description")
simpleany_DocumentRoot = Class(name="simpleany::DocumentRoot")
simpleany_BookType = Class(name="simpleany::BookType")
simpleany_EStringToStringMapEntry = Class(name="simpleany::EStringToStringMapEntry")
simpleany_LibraryType = Class(name="simpleany::LibraryType")

# simpleany_Description class attributes and methods
simpleany_Description_mixed: Property = Property(name="mixed", type=StringType)
simpleany_Description_keyword: Property = Property(name="keyword", type=StringType)
simpleany_Description.attributes={simpleany_Description_keyword, simpleany_Description_mixed}

# simpleany_DocumentRoot class attributes and methods
simpleany_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
simpleany_DocumentRoot.attributes={simpleany_DocumentRoot_mixed}

# simpleany_BookType class attributes and methods
simpleany_BookType_name: Property = Property(name="name", type=StringType)
simpleany_BookType_title: Property = Property(name="title", type=StringType)
simpleany_BookType_author: Property = Property(name="author", type=StringType)
simpleany_BookType.attributes={simpleany_BookType_name, simpleany_BookType_author, simpleany_BookType_title}

# simpleany_EStringToStringMapEntry class attributes and methods

# simpleany_LibraryType class attributes and methods

# Relationships
description0: BinaryAssociation = BinaryAssociation(
    name="description0",
    ends={
        Property(name="simpleany_Description", type=simpleany_BookType, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleany_BookType", type=simpleany_Description, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
description2: BinaryAssociation = BinaryAssociation(
    name="description2",
    ends={
        Property(name="simpleany_Description3", type=simpleany_Description, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleany_Description1", type=simpleany_Description, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
book10: BinaryAssociation = BinaryAssociation(
    name="book10",
    ends={
        Property(name="simpleany_BookType12", type=simpleany_LibraryType, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleany_LibraryType11", type=simpleany_BookType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap4: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap4",
    ends={
        Property(name="simpleany_EStringToStringMapEntry", type=simpleany_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleany_DocumentRoot", type=simpleany_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation5: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation5",
    ends={
        Property(name="simpleany_EStringToStringMapEntry7", type=simpleany_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleany_DocumentRoot6", type=simpleany_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
library8: BinaryAssociation = BinaryAssociation(
    name="library8",
    ends={
        Property(name="simpleany_LibraryType", type=simpleany_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleany_DocumentRoot9", type=simpleany_LibraryType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="simpleany",
    types={simpleany_Description, simpleany_DocumentRoot, simpleany_BookType, simpleany_EStringToStringMapEntry, simpleany_LibraryType},
    associations={description0, description2, book10, xMLNSPrefixMap4, xSISchemaLocation5, library8},
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