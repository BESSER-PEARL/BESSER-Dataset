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
library_Library = Class(name="library::Library")
library_LibraryContent = Class(name="library::LibraryContent", is_abstract=True)
library_Book = Class(name="library::Book")
LibraryContent = Class(name="LibraryContent")
library_Magazine = Class(name="library::Magazine")

# library_Library class attributes and methods
library_Library_name: Property = Property(name="name", type=StringType)
library_Library.attributes={library_Library_name}

# library_LibraryContent class attributes and methods
library_LibraryContent_name: Property = Property(name="name", type=StringType)
library_LibraryContent_author: Property = Property(name="author", type=StringType)
library_LibraryContent.attributes={library_LibraryContent_name, library_LibraryContent_author}

# library_Book class attributes and methods

# LibraryContent class attributes and methods

# library_Magazine class attributes and methods

# Relationships
librarycontent0: BinaryAssociation = BinaryAssociation(
    name="librarycontent0",
    ends={
        Property(name="library_LibraryContent", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_LibraryContent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_library_Book_LibraryContent = Generalization(general=LibraryContent, specific=library_Book)
gen_library_Magazine_LibraryContent = Generalization(general=LibraryContent, specific=library_Magazine)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Library, library_LibraryContent, library_Book, LibraryContent, library_Magazine},
    associations={librarycontent0},
    generalizations={gen_library_Book_LibraryContent, gen_library_Magazine_LibraryContent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)