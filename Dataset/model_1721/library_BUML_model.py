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
library_Chapter = Class(name="library::Chapter")
library_Library = Class(name="library::Library")
library_Book = Class(name="library::Book")
library_Content = Class(name="library::Content")
library_Text = Class(name="library::Text")
library_Image = Class(name="library::Image")

# library_Chapter class attributes and methods
library_Chapter_name: Property = Property(name="name", type=StringType)
library_Chapter_pages: Property = Property(name="pages", type=IntegerType)
library_Chapter.attributes={library_Chapter_pages, library_Chapter_name}

# library_Library class attributes and methods
library_Library_name: Property = Property(name="name", type=StringType)
library_Library.attributes={library_Library_name}

# library_Book class attributes and methods
library_Book_name: Property = Property(name="name", type=StringType)
library_Book.attributes={library_Book_name}

# library_Content class attributes and methods

# library_Text class attributes and methods

# library_Image class attributes and methods

# Relationships
chapters1: BinaryAssociation = BinaryAssociation(
    name="chapters1",
    ends={
        Property(name="library_Chapter", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Book2", type=library_Chapter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="library_Book", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content3: BinaryAssociation = BinaryAssociation(
    name="content3",
    ends={
        Property(name="library_Content", type=library_Chapter, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Chapter4", type=library_Content, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
text5: BinaryAssociation = BinaryAssociation(
    name="text5",
    ends={
        Property(name="library_Text", type=library_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Content6", type=library_Text, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
images7: BinaryAssociation = BinaryAssociation(
    name="images7",
    ends={
        Property(name="library_Image", type=library_Content, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Content8", type=library_Image, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Chapter, library_Library, library_Book, library_Content, library_Text, library_Image},
    associations={chapters1, books0, content3, text5, images7},
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