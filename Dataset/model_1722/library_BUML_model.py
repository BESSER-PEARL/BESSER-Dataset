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
library_Book = Class(name="library::Book")
library_Library = Class(name="library::Library")
library_NonFiction = Class(name="library::NonFiction")
library_Fiction = Class(name="library::Fiction")

# library_Book class attributes and methods
library_Book_Name: Property = Property(name="Name", type=StringType)
library_Book_genre: Property = Property(name="genre", type=StringType)
library_Book.attributes={library_Book_genre, library_Book_Name}

# library_Library class attributes and methods
library_Library_Name: Property = Property(name="Name", type=StringType)
library_Library.attributes={library_Library_Name}

# library_NonFiction class attributes and methods
library_NonFiction_Name: Property = Property(name="Name", type=StringType)
library_NonFiction.attributes={library_NonFiction_Name}

# library_Fiction class attributes and methods
library_Fiction_Name: Property = Property(name="Name", type=StringType)
library_Fiction.attributes={library_Fiction_Name}

# Relationships
books1: BinaryAssociation = BinaryAssociation(
    name="books1",
    ends={
        Property(name="library_Book2", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
members0: BinaryAssociation = BinaryAssociation(
    name="members0",
    ends={
        Property(name="library_Book", type=library_NonFiction, multiplicity=Multiplicity(1, 1)),
        Property(name="library_NonFiction", type=library_Book, multiplicity=Multiplicity(0, 9999))
    }
)
members8: BinaryAssociation = BinaryAssociation(
    name="members8",
    ends={
        Property(name="library_Book10", type=library_Fiction, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Fiction9", type=library_Book, multiplicity=Multiplicity(0, 9999))
    }
)
nonfiction3: BinaryAssociation = BinaryAssociation(
    name="nonfiction3",
    ends={
        Property(name="library_NonFiction5", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library4", type=library_NonFiction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fiction6: BinaryAssociation = BinaryAssociation(
    name="fiction6",
    ends={
        Property(name="library_Fiction", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library7", type=library_Fiction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Book, library_Library, library_NonFiction, library_Fiction},
    associations={books1, members0, members8, nonfiction3, fiction6},
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