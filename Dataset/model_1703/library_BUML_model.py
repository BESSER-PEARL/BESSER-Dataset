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
AnnotationColor: Enumeration = Enumeration(
    name="AnnotationColor",
    literals={
            EnumerationLiteral(name="Yellow"),
			EnumerationLiteral(name="Green"),
			EnumerationLiteral(name="Blue"),
			EnumerationLiteral(name="Red"),
			EnumerationLiteral(name="Purple"),
			EnumerationLiteral(name="Underline")
    }
)

# Classes
library_Library = Class(name="library::Library")
library_Bookmark = Class(name="library::Bookmark")
library_Book = Class(name="library::Book")
library_TextAnnotation = Class(name="library::TextAnnotation")
library_Metadata = Class(name="library::Metadata")
Bookmark = Class(name="Bookmark")

# library_Library class attributes and methods
library_Library_version: Property = Property(name="version", type=StringType)
library_Library.attributes={library_Library_version}

# library_Bookmark class attributes and methods
library_Bookmark_id: Property = Property(name="id", type=StringType)
library_Bookmark_location: Property = Property(name="location", type=StringType)
library_Bookmark_page: Property = Property(name="page", type=IntegerType)
library_Bookmark_href: Property = Property(name="href", type=StringType)
library_Bookmark_timestamp: Property = Property(name="timestamp", type=DateType)
library_Bookmark_text: Property = Property(name="text", type=StringType)
library_Bookmark.attributes={library_Bookmark_page, library_Bookmark_id, library_Bookmark_timestamp, library_Bookmark_location, library_Bookmark_href, library_Bookmark_text}

# library_Book class attributes and methods
library_Book_bookURN: Property = Property(name="bookURN", type=StringType)
library_Book_bookURL: Property = Property(name="bookURL", type=StringType)
library_Book_collection: Property = Property(name="collection", type=StringType)
library_Book_title: Property = Property(name="title", type=StringType)
library_Book_author: Property = Property(name="author", type=StringType)
library_Book_lastHref: Property = Property(name="lastHref", type=StringType)
library_Book_lastLocation: Property = Property(name="lastLocation", type=StringType)
library_Book_lastOpened: Property = Property(name="lastOpened", type=StringType)
library_Book.attributes={library_Book_bookURN, library_Book_lastLocation, library_Book_lastHref, library_Book_title, library_Book_collection, library_Book_bookURL, library_Book_author, library_Book_lastOpened}

# library_TextAnnotation class attributes and methods
library_TextAnnotation_color: Property = Property(name="color", type=StringType)
library_TextAnnotation_comment: Property = Property(name="comment", type=StringType)
library_TextAnnotation.attributes={library_TextAnnotation_comment, library_TextAnnotation_color}

# library_Metadata class attributes and methods
library_Metadata_key: Property = Property(name="key", type=StringType)
library_Metadata_value: Property = Property(name="value", type=StringType)
library_Metadata.attributes={library_Metadata_key, library_Metadata_value}

# Bookmark class attributes and methods

# Relationships
bookmarks1: BinaryAssociation = BinaryAssociation(
    name="bookmarks1",
    ends={
        Property(name="library_Bookmark", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Book2", type=library_Bookmark, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="library_Book", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metadata3: BinaryAssociation = BinaryAssociation(
    name="metadata3",
    ends={
        Property(name="library_Metadata", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Book4", type=library_Metadata, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_library_TextAnnotation_Bookmark = Generalization(general=Bookmark, specific=library_TextAnnotation)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Library, library_Bookmark, library_Book, library_TextAnnotation, library_Metadata, Bookmark, AnnotationColor},
    associations={bookmarks1, books0, metadata3},
    generalizations={gen_library_TextAnnotation_Bookmark},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)