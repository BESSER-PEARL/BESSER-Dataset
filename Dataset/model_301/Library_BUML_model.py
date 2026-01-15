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
Library_Book = Class(name="Library::Book")
CirculatingItem = Class(name="CirculatingItem")
Library_Item = Class(name="Library::Item", is_abstract=True)
Person = Class(name="Person")
Library_Writer = Class(name="Library::Writer")
Library_Library = Class(name="Library::Library")
Addressable = Class(name="Addressable")
Library_Employee = Class(name="Library::Employee")
Library_Borrower = Class(name="Library::Borrower")
Library_AudioVisualItem = Class(name="Library::AudioVisualItem", is_abstract=True)
Library_BookOnTape = Class(name="Library::BookOnTape")
AudioVisualItem = Class(name="AudioVisualItem")
Library_Person = Class(name="Library::Person")
Library_VideoCassette = Class(name="Library::VideoCassette")
Library_Lendable = Class(name="Library::Lendable", is_abstract=True)
Library_CirculatingItem = Class(name="Library::CirculatingItem", is_abstract=True)
Item = Class(name="Item")
Lendable = Class(name="Lendable")
Library_Periodical = Class(name="Library::Periodical", is_abstract=True)
Library_Addressable = Class(name="Library::Addressable", is_abstract=True)

# Library_Book class attributes and methods
Library_Book_title: Property = Property(name="title", type=StringType)
Library_Book_pages: Property = Property(name="pages", type=IntegerType)
Library_Book_category: Property = Property(name="category", type=StringType)
Library_Book.attributes={Library_Book_category, Library_Book_title, Library_Book_pages}

# CirculatingItem class attributes and methods

# Library_Item class attributes and methods
Library_Item_publicationDate: Property = Property(name="publicationDate", type=DateType)
Library_Item.attributes={Library_Item_publicationDate}

# Person class attributes and methods

# Library_Writer class attributes and methods
Library_Writer_name: Property = Property(name="name", type=StringType)
Library_Writer.attributes={Library_Writer_name}

# Library_Library class attributes and methods
Library_Library_people: Property = Property(name="people", type=StringType)
Library_Library_name: Property = Property(name="name", type=StringType)
Library_Library.attributes={Library_Library_people, Library_Library_name}

# Addressable class attributes and methods

# Library_Employee class attributes and methods

# Library_Borrower class attributes and methods

# Library_AudioVisualItem class attributes and methods
Library_AudioVisualItem_title: Property = Property(name="title", type=StringType)
Library_AudioVisualItem_minutesLength: Property = Property(name="minutesLength", type=IntegerType)
Library_AudioVisualItem_damaged: Property = Property(name="damaged", type=BooleanType)
Library_AudioVisualItem.attributes={Library_AudioVisualItem_title, Library_AudioVisualItem_damaged, Library_AudioVisualItem_minutesLength}

# Library_BookOnTape class attributes and methods

# AudioVisualItem class attributes and methods

# Library_Person class attributes and methods
Library_Person_firstName: Property = Property(name="firstName", type=StringType)
Library_Person_lastName: Property = Property(name="lastName", type=StringType)
Library_Person.attributes={Library_Person_lastName, Library_Person_firstName}

# Library_VideoCassette class attributes and methods

# Library_Lendable class attributes and methods
Library_Lendable_copies: Property = Property(name="copies", type=IntegerType)
Library_Lendable.attributes={Library_Lendable_copies}

# Library_CirculatingItem class attributes and methods

# Item class attributes and methods

# Lendable class attributes and methods

# Library_Periodical class attributes and methods
Library_Periodical_issuesPerYear: Property = Property(name="issuesPerYear", type=IntegerType)
Library_Periodical_title: Property = Property(name="title", type=StringType)
Library_Periodical.attributes={Library_Periodical_issuesPerYear, Library_Periodical_title}

# Library_Addressable class attributes and methods
Library_Addressable_address: Property = Property(name="address", type=StringType)
Library_Addressable.attributes={Library_Addressable_address}

# Relationships
stock6: BinaryAssociation = BinaryAssociation(
    name="stock6",
    ends={
        Property(name="Library_Item", type=Library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="Library_Library7", type=Library_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books8: BinaryAssociation = BinaryAssociation(
    name="books8",
    ends={
        Property(name="Library_Book", type=Library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="Library_Library9", type=Library_Book, multiplicity=Multiplicity(0, 9999))
    }
)
branches11: BinaryAssociation = BinaryAssociation(
    name="branches11",
    ends={
        Property(name="Library", type=Library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="parentBranch", type=Library_Library, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentBranch13: BinaryAssociation = BinaryAssociation(
    name="parentBranch13",
    ends={
        Property(name="Library14", type=Library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="branches", type=Library_Library, multiplicity=Multiplicity(0, 1))
    }
)
books15: BinaryAssociation = BinaryAssociation(
    name="books15",
    ends={
        Property(name="Book", type=Library_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=Library_Book, multiplicity=Multiplicity(0, 9999))
    }
)
author0: BinaryAssociation = BinaryAssociation(
    name="author0",
    ends={
        Property(name="Writer", type=Library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=Library_Writer, multiplicity=Multiplicity(1, 1))
    }
)
writers1: BinaryAssociation = BinaryAssociation(
    name="writers1",
    ends={
        Property(name="Library_Writer", type=Library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="Library_Library", type=Library_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employees2: BinaryAssociation = BinaryAssociation(
    name="employees2",
    ends={
        Property(name="Library_Employee", type=Library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="Library_Library3", type=Library_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
borrowers4: BinaryAssociation = BinaryAssociation(
    name="borrowers4",
    ends={
        Property(name="Library_Borrower", type=Library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="Library_Library5", type=Library_Borrower, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reader17: BinaryAssociation = BinaryAssociation(
    name="reader17",
    ends={
        Property(name="Library_Person", type=Library_BookOnTape, multiplicity=Multiplicity(1, 1)),
        Property(name="Library_BookOnTape", type=Library_Person, multiplicity=Multiplicity(0, 1))
    }
)
author18: BinaryAssociation = BinaryAssociation(
    name="author18",
    ends={
        Property(name="Library_Writer20", type=Library_BookOnTape, multiplicity=Multiplicity(1, 1)),
        Property(name="Library_BookOnTape19", type=Library_Writer, multiplicity=Multiplicity(0, 1))
    }
)
cast21: BinaryAssociation = BinaryAssociation(
    name="cast21",
    ends={
        Property(name="Library_Person22", type=Library_VideoCassette, multiplicity=Multiplicity(1, 1)),
        Property(name="Library_VideoCassette", type=Library_Person, multiplicity=Multiplicity(0, 9999))
    }
)
borrowed23: BinaryAssociation = BinaryAssociation(
    name="borrowed23",
    ends={
        Property(name="Lendable", type=Library_Borrower, multiplicity=Multiplicity(1, 1)),
        Property(name="borrowers", type=Library_Lendable, multiplicity=Multiplicity(0, 9999))
    }
)
borrowers16: BinaryAssociation = BinaryAssociation(
    name="borrowers16",
    ends={
        Property(name="Borrower", type=Library_Lendable, multiplicity=Multiplicity(1, 1)),
        Property(name="borrowed", type=Library_Borrower, multiplicity=Multiplicity(0, 9999))
    }
)
manager25: BinaryAssociation = BinaryAssociation(
    name="manager25",
    ends={
        Property(name="Library_Employee26", type=Library_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="Library_Employee24", type=Library_Employee, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_Library_Book_CirculatingItem = Generalization(general=CirculatingItem, specific=Library_Book)
gen_Library_Writer_Person = Generalization(general=Person, specific=Library_Writer)
gen_Library_Library_Addressable = Generalization(general=Addressable, specific=Library_Library)
gen_Library_AudioVisualItem_CirculatingItem = Generalization(general=CirculatingItem, specific=Library_AudioVisualItem)
gen_Library_BookOnTape_AudioVisualItem = Generalization(general=AudioVisualItem, specific=Library_BookOnTape)
gen_Library_VideoCassette_AudioVisualItem = Generalization(general=AudioVisualItem, specific=Library_VideoCassette)
gen_Library_Borrower_Person = Generalization(general=Person, specific=Library_Borrower)
gen_Library_Person_Addressable = Generalization(general=Addressable, specific=Library_Person)
gen_Library_CirculatingItem_Item = Generalization(general=Item, specific=Library_CirculatingItem)
gen_Library_CirculatingItem_Lendable = Generalization(general=Lendable, specific=Library_CirculatingItem)
gen_Library_Periodical_Item = Generalization(general=Item, specific=Library_Periodical)
gen_Library_Employee_Person = Generalization(general=Person, specific=Library_Employee)

# Domain Model
domain_model = DomainModel(
    name="Library",
    types={Library_Book, CirculatingItem, Library_Item, Person, Library_Writer, Library_Library, Addressable, Library_Employee, Library_Borrower, Library_AudioVisualItem, Library_BookOnTape, AudioVisualItem, Library_Person, Library_VideoCassette, Library_Lendable, Library_CirculatingItem, Item, Lendable, Library_Periodical, Library_Addressable, BookCategory},
    associations={stock6, books8, branches11, parentBranch13, books15, author0, writers1, employees2, borrowers4, reader17, author18, cast21, borrowed23, borrowers16, manager25},
    generalizations={gen_Library_Book_CirculatingItem, gen_Library_Writer_Person, gen_Library_Library_Addressable, gen_Library_AudioVisualItem_CirculatingItem, gen_Library_BookOnTape_AudioVisualItem, gen_Library_VideoCassette_AudioVisualItem, gen_Library_Borrower_Person, gen_Library_Person_Addressable, gen_Library_CirculatingItem_Item, gen_Library_CirculatingItem_Lendable, gen_Library_Periodical_Item, gen_Library_Employee_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)