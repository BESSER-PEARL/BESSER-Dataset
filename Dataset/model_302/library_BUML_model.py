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
library_Book = Class(name="library::Book")
CirculatingItem = Class(name="CirculatingItem")
library_Writer = Class(name="library::Writer")
library_Library = Class(name="library::Library")
Addressable = Class(name="Addressable")
library_Employee = Class(name="library::Employee")
library_Borrower = Class(name="library::Borrower")
library_Item = Class(name="library::Item", is_abstract=True)
Person = Class(name="Person")
library_Lendable = Class(name="library::Lendable", is_abstract=True)
library_CirculatingItem = Class(name="library::CirculatingItem", is_abstract=True)
Item = Class(name="Item")
Lendable = Class(name="Lendable")
library_Periodical = Class(name="library::Periodical", is_abstract=True)
library_AudioVisualItem = Class(name="library::AudioVisualItem", is_abstract=True)
library_BookOnTape = Class(name="library::BookOnTape")
AudioVisualItem = Class(name="AudioVisualItem")
library_Person = Class(name="library::Person")
library_VideoCassette = Class(name="library::VideoCassette")
library_Addressable = Class(name="library::Addressable", is_abstract=True)

# library_Book class attributes and methods
library_Book_title: Property = Property(name="title", type=StringType)
library_Book_pages: Property = Property(name="pages", type=IntegerType)
library_Book_category: Property = Property(name="category", type=StringType)
library_Book.attributes={library_Book_pages, library_Book_category, library_Book_title}

# CirculatingItem class attributes and methods

# library_Writer class attributes and methods
library_Writer_name: Property = Property(name="name", type=StringType)
library_Writer.attributes={library_Writer_name}

# library_Library class attributes and methods
library_Library_name: Property = Property(name="name", type=StringType)
library_Library_people: Property = Property(name="people", type=StringType)
library_Library.attributes={library_Library_people, library_Library_name}

# Addressable class attributes and methods

# library_Employee class attributes and methods

# library_Borrower class attributes and methods

# library_Item class attributes and methods
library_Item_publicationDate: Property = Property(name="publicationDate", type=DateType)
library_Item.attributes={library_Item_publicationDate}

# Person class attributes and methods

# library_Lendable class attributes and methods
library_Lendable_copies: Property = Property(name="copies", type=IntegerType)
library_Lendable.attributes={library_Lendable_copies}

# library_CirculatingItem class attributes and methods

# Item class attributes and methods

# Lendable class attributes and methods

# library_Periodical class attributes and methods
library_Periodical_title: Property = Property(name="title", type=StringType)
library_Periodical_issuesPerYear: Property = Property(name="issuesPerYear", type=IntegerType)
library_Periodical.attributes={library_Periodical_title, library_Periodical_issuesPerYear}

# library_AudioVisualItem class attributes and methods
library_AudioVisualItem_title: Property = Property(name="title", type=StringType)
library_AudioVisualItem_minutesLength: Property = Property(name="minutesLength", type=IntegerType)
library_AudioVisualItem_damaged: Property = Property(name="damaged", type=BooleanType)
library_AudioVisualItem.attributes={library_AudioVisualItem_title, library_AudioVisualItem_damaged, library_AudioVisualItem_minutesLength}

# library_BookOnTape class attributes and methods

# AudioVisualItem class attributes and methods

# library_Person class attributes and methods
library_Person_firstName: Property = Property(name="firstName", type=StringType)
library_Person_lastName: Property = Property(name="lastName", type=StringType)
library_Person.attributes={library_Person_firstName, library_Person_lastName}

# library_VideoCassette class attributes and methods

# library_Addressable class attributes and methods
library_Addressable_address: Property = Property(name="address", type=StringType)
library_Addressable.attributes={library_Addressable_address}

# Relationships
employees2: BinaryAssociation = BinaryAssociation(
    name="employees2",
    ends={
        Property(name="library_Employee", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library3", type=library_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
author0: BinaryAssociation = BinaryAssociation(
    name="author0",
    ends={
        Property(name="Writer", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=library_Writer, multiplicity=Multiplicity(1, 1))
    }
)
writers1: BinaryAssociation = BinaryAssociation(
    name="writers1",
    ends={
        Property(name="library_Writer", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
borrowers4: BinaryAssociation = BinaryAssociation(
    name="borrowers4",
    ends={
        Property(name="library_Borrower", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library5", type=library_Borrower, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stock6: BinaryAssociation = BinaryAssociation(
    name="stock6",
    ends={
        Property(name="library_Item", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library7", type=library_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books8: BinaryAssociation = BinaryAssociation(
    name="books8",
    ends={
        Property(name="library_Book", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library9", type=library_Book, multiplicity=Multiplicity(0, 9999))
    }
)
branches11: BinaryAssociation = BinaryAssociation(
    name="branches11",
    ends={
        Property(name="Library", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="parentBranch", type=library_Library, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentBranch13: BinaryAssociation = BinaryAssociation(
    name="parentBranch13",
    ends={
        Property(name="Library14", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="branches", type=library_Library, multiplicity=Multiplicity(0, 1))
    }
)
books15: BinaryAssociation = BinaryAssociation(
    name="books15",
    ends={
        Property(name="Book", type=library_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=library_Book, multiplicity=Multiplicity(0, 9999))
    }
)
borrowers16: BinaryAssociation = BinaryAssociation(
    name="borrowers16",
    ends={
        Property(name="Borrower", type=library_Lendable, multiplicity=Multiplicity(1, 1)),
        Property(name="borrowed", type=library_Borrower, multiplicity=Multiplicity(0, 9999))
    }
)
borrowed23: BinaryAssociation = BinaryAssociation(
    name="borrowed23",
    ends={
        Property(name="borrowers", type=library_Lendable, multiplicity=Multiplicity(0, 9999)),
        Property(name="Lendable", type=library_Borrower, multiplicity=Multiplicity(1, 1))
    }
)
reader17: BinaryAssociation = BinaryAssociation(
    name="reader17",
    ends={
        Property(name="library_Person", type=library_BookOnTape, multiplicity=Multiplicity(1, 1)),
        Property(name="library_BookOnTape", type=library_Person, multiplicity=Multiplicity(0, 1))
    }
)
author18: BinaryAssociation = BinaryAssociation(
    name="author18",
    ends={
        Property(name="library_Writer20", type=library_BookOnTape, multiplicity=Multiplicity(1, 1)),
        Property(name="library_BookOnTape19", type=library_Writer, multiplicity=Multiplicity(0, 1))
    }
)
cast21: BinaryAssociation = BinaryAssociation(
    name="cast21",
    ends={
        Property(name="library_Person22", type=library_VideoCassette, multiplicity=Multiplicity(1, 1)),
        Property(name="library_VideoCassette", type=library_Person, multiplicity=Multiplicity(0, 9999))
    }
)
manager25: BinaryAssociation = BinaryAssociation(
    name="manager25",
    ends={
        Property(name="library_Employee26", type=library_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Employee24", type=library_Employee, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_library_Book_CirculatingItem = Generalization(general=CirculatingItem, specific=library_Book)
gen_library_Library_Addressable = Generalization(general=Addressable, specific=library_Library)
gen_library_Writer_Person = Generalization(general=Person, specific=library_Writer)
gen_library_CirculatingItem_Item = Generalization(general=Item, specific=library_CirculatingItem)
gen_library_CirculatingItem_Lendable = Generalization(general=Lendable, specific=library_CirculatingItem)
gen_library_Periodical_Item = Generalization(general=Item, specific=library_Periodical)
gen_library_AudioVisualItem_CirculatingItem = Generalization(general=CirculatingItem, specific=library_AudioVisualItem)
gen_library_BookOnTape_AudioVisualItem = Generalization(general=AudioVisualItem, specific=library_BookOnTape)
gen_library_VideoCassette_AudioVisualItem = Generalization(general=AudioVisualItem, specific=library_VideoCassette)
gen_library_Borrower_Person = Generalization(general=Person, specific=library_Borrower)
gen_library_Person_Addressable = Generalization(general=Addressable, specific=library_Person)
gen_library_Employee_Person = Generalization(general=Person, specific=library_Employee)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Book, CirculatingItem, library_Writer, library_Library, Addressable, library_Employee, library_Borrower, library_Item, Person, library_Lendable, library_CirculatingItem, Item, Lendable, library_Periodical, library_AudioVisualItem, library_BookOnTape, AudioVisualItem, library_Person, library_VideoCassette, library_Addressable, BookCategory},
    associations={employees2, author0, writers1, borrowers4, stock6, books8, branches11, parentBranch13, books15, borrowers16, borrowed23, reader17, author18, cast21, manager25},
    generalizations={gen_library_Book_CirculatingItem, gen_library_Library_Addressable, gen_library_Writer_Person, gen_library_CirculatingItem_Item, gen_library_CirculatingItem_Lendable, gen_library_Periodical_Item, gen_library_AudioVisualItem_CirculatingItem, gen_library_BookOnTape_AudioVisualItem, gen_library_VideoCassette_AudioVisualItem, gen_library_Borrower_Person, gen_library_Person_Addressable, gen_library_Employee_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)