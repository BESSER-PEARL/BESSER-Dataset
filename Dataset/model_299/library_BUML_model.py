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
BookCategory: Enumeration = Enumeration(
    name="BookCategory",
    literals={
            EnumerationLiteral(name="Mystery"),
			EnumerationLiteral(name="ScienceFiction"),
			EnumerationLiteral(name="Biography")
    }
)

# Classes
library_Library = Class(name="library::Library")
library_Writer = Class(name="library::Writer")
library_Book = Class(name="library::Book")
library_Community = Class(name="library::Community")
library_Opinion = Class(name="library::Opinion")
library_CommunityRole = Class(name="library::CommunityRole")
library_Review = Class(name="library::Review")
library_Chapter = Class(name="library::Chapter")

# library_Library class attributes and methods
library_Library_name: Property = Property(name="name", type=StringType)
library_Library.attributes={library_Library_name}

# library_Writer class attributes and methods
library_Writer_name: Property = Property(name="name", type=StringType)
library_Writer.attributes={library_Writer_name}

# library_Book class attributes and methods
library_Book_category: Property = Property(name="category", type=StringType)
library_Book_title: Property = Property(name="title", type=StringType)
library_Book_pages: Property = Property(name="pages", type=IntegerType)
library_Book.attributes={library_Book_pages, library_Book_title, library_Book_category}

# library_Community class attributes and methods
library_Community_name: Property = Property(name="name", type=StringType)
library_Community.attributes={library_Community_name}

# library_Opinion class attributes and methods
library_Opinion_text: Property = Property(name="text", type=StringType)
library_Opinion_context: Property = Property(name="context", type=StringType)
library_Opinion.attributes={library_Opinion_context, library_Opinion_text}

# library_CommunityRole class attributes and methods
library_CommunityRole_role: Property = Property(name="role", type=StringType)
library_CommunityRole.attributes={library_CommunityRole_role}

# library_Review class attributes and methods
library_Review_title: Property = Property(name="title", type=StringType)
library_Review_positive: Property = Property(name="positive", type=BooleanType)
library_Review.attributes={library_Review_title, library_Review_positive}

# library_Chapter class attributes and methods
library_Chapter_name: Property = Property(name="name", type=StringType)
library_Chapter.attributes={library_Chapter_name}

# Relationships
writers0: BinaryAssociation = BinaryAssociation(
    name="writers0",
    ends={
        Property(name="library_Writer", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books1: BinaryAssociation = BinaryAssociation(
    name="books1",
    ends={
        Property(name="library_Book", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library2", type=library_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
communities3: BinaryAssociation = BinaryAssociation(
    name="communities3",
    ends={
        Property(name="Community", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library", type=library_Community, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books4: BinaryAssociation = BinaryAssociation(
    name="books4",
    ends={
        Property(name="Book", type=library_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=library_Book, multiplicity=Multiplicity(0, 9999))
    }
)
brochures5: BinaryAssociation = BinaryAssociation(
    name="brochures5",
    ends={
        Property(name="library_Book7", type=library_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Writer6", type=library_Book, multiplicity=Multiplicity(0, 2), is_composite=True)
    }
)
opinions8: BinaryAssociation = BinaryAssociation(
    name="opinions8",
    ends={
        Property(name="Opinion", type=library_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="writer", type=library_Opinion, multiplicity=Multiplicity(0, 2), is_composite=True)
    }
)
participates9: BinaryAssociation = BinaryAssociation(
    name="participates9",
    ends={
        Property(name="CommunityRole", type=library_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="participants", type=library_CommunityRole, multiplicity=Multiplicity(0, 9999))
    }
)
author10: BinaryAssociation = BinaryAssociation(
    name="author10",
    ends={
        Property(name="Writer", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=library_Writer, multiplicity=Multiplicity(1, 1))
    }
)
reviews11: BinaryAssociation = BinaryAssociation(
    name="reviews11",
    ends={
        Property(name="Review", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="book", type=library_Review, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
chapters12: BinaryAssociation = BinaryAssociation(
    name="chapters12",
    ends={
        Property(name="library_Chapter", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Book13", type=library_Chapter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
opinions14: BinaryAssociation = BinaryAssociation(
    name="opinions14",
    ends={
        Property(name="Opinion16", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="book15", type=library_Opinion, multiplicity=Multiplicity(0, 2))
    }
)
book17: BinaryAssociation = BinaryAssociation(
    name="book17",
    ends={
        Property(name="Book18", type=library_Review, multiplicity=Multiplicity(1, 1)),
        Property(name="reviews", type=library_Book, multiplicity=Multiplicity(1, 1))
    }
)
writer19: BinaryAssociation = BinaryAssociation(
    name="writer19",
    ends={
        Property(name="Writer20", type=library_Opinion, multiplicity=Multiplicity(1, 1)),
        Property(name="opinions", type=library_Writer, multiplicity=Multiplicity(1, 1))
    }
)
book21: BinaryAssociation = BinaryAssociation(
    name="book21",
    ends={
        Property(name="Book23", type=library_Opinion, multiplicity=Multiplicity(1, 1)),
        Property(name="opinions22", type=library_Book, multiplicity=Multiplicity(1, 1))
    }
)
community27: BinaryAssociation = BinaryAssociation(
    name="community27",
    ends={
        Property(name="Community28", type=library_CommunityRole, multiplicity=Multiplicity(1, 1)),
        Property(name="roles", type=library_Community, multiplicity=Multiplicity(0, 1))
    }
)
participants29: BinaryAssociation = BinaryAssociation(
    name="participants29",
    ends={
        Property(name="Writer30", type=library_CommunityRole, multiplicity=Multiplicity(1, 1)),
        Property(name="participates", type=library_Writer, multiplicity=Multiplicity(0, 9999))
    }
)
roles24: BinaryAssociation = BinaryAssociation(
    name="roles24",
    ends={
        Property(name="CommunityRole25", type=library_Community, multiplicity=Multiplicity(1, 1)),
        Property(name="community", type=library_CommunityRole, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
library26: BinaryAssociation = BinaryAssociation(
    name="library26",
    ends={
        Property(name="Library", type=library_Community, multiplicity=Multiplicity(1, 1)),
        Property(name="communities", type=library_Library, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Library, library_Writer, library_Book, library_Community, library_Opinion, library_CommunityRole, library_Review, library_Chapter, BookCategory},
    associations={writers0, books1, communities3, books4, brochures5, opinions8, participates9, author10, reviews11, chapters12, opinions14, book17, writer19, book21, community27, participants29, roles24, library26},
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