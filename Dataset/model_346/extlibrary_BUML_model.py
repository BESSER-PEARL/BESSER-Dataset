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
extlibrary_Book = Class(name="extlibrary::Book")
CirculatingItem = Class(name="CirculatingItem")
extlibrary_Writer = Class(name="extlibrary::Writer")
extlibrary_Person = Class(name="extlibrary::Person")
Person = Class(name="Person")
extlibrary_Lendable = Class(name="extlibrary::Lendable", is_abstract=True)
extlibrary_Library = Class(name="extlibrary::Library")
Addressable = Class(name="Addressable")
extlibrary_Employee = Class(name="extlibrary::Employee")
extlibrary_Borrower = Class(name="extlibrary::Borrower")
extlibrary_Item = Class(name="extlibrary::Item", is_abstract=True)
extlibrary_VideoCassette = Class(name="extlibrary::VideoCassette")
extlibrary_Addressable = Class(name="extlibrary::Addressable", is_abstract=True)
extlibrary_CirculatingItem = Class(name="extlibrary::CirculatingItem", is_abstract=True)
Item = Class(name="Item")
Lendable = Class(name="Lendable")
extlibrary_Periodical = Class(name="extlibrary::Periodical")
extlibrary_AudioVisualItem = Class(name="extlibrary::AudioVisualItem", is_abstract=True)
extlibrary_BookOnTape = Class(name="extlibrary::BookOnTape")
AudioVisualItem = Class(name="AudioVisualItem")

# extlibrary_Book class attributes and methods
extlibrary_Book_title: Property = Property(name="title", type=StringType)
extlibrary_Book_pages: Property = Property(name="pages", type=IntegerType)
extlibrary_Book_category: Property = Property(name="category", type=StringType)
extlibrary_Book.attributes={extlibrary_Book_title, extlibrary_Book_pages, extlibrary_Book_category}

# CirculatingItem class attributes and methods

# extlibrary_Writer class attributes and methods
extlibrary_Writer_name: Property = Property(name="name", type=StringType)
extlibrary_Writer.attributes={extlibrary_Writer_name}

# extlibrary_Person class attributes and methods
extlibrary_Person_firstName: Property = Property(name="firstName", type=StringType)
extlibrary_Person_lastName: Property = Property(name="lastName", type=StringType)
extlibrary_Person.attributes={extlibrary_Person_firstName, extlibrary_Person_lastName}

# Person class attributes and methods

# extlibrary_Lendable class attributes and methods
extlibrary_Lendable_copies: Property = Property(name="copies", type=IntegerType)
extlibrary_Lendable.attributes={extlibrary_Lendable_copies}

# extlibrary_Library class attributes and methods
extlibrary_Library_name: Property = Property(name="name", type=StringType)
extlibrary_Library.attributes={extlibrary_Library_name}

# Addressable class attributes and methods

# extlibrary_Employee class attributes and methods

# extlibrary_Borrower class attributes and methods

# extlibrary_Item class attributes and methods
extlibrary_Item_publicationDate: Property = Property(name="publicationDate", type=DateType)
extlibrary_Item.attributes={extlibrary_Item_publicationDate}

# extlibrary_VideoCassette class attributes and methods

# extlibrary_Addressable class attributes and methods
extlibrary_Addressable_address: Property = Property(name="address", type=StringType)
extlibrary_Addressable.attributes={extlibrary_Addressable_address}

# extlibrary_CirculatingItem class attributes and methods

# Item class attributes and methods

# Lendable class attributes and methods

# extlibrary_Periodical class attributes and methods
extlibrary_Periodical_title: Property = Property(name="title", type=StringType)
extlibrary_Periodical_issuesPerYear: Property = Property(name="issuesPerYear", type=IntegerType)
extlibrary_Periodical.attributes={extlibrary_Periodical_title, extlibrary_Periodical_issuesPerYear}

# extlibrary_AudioVisualItem class attributes and methods
extlibrary_AudioVisualItem_title: Property = Property(name="title", type=StringType)
extlibrary_AudioVisualItem_minutesLength: Property = Property(name="minutesLength", type=IntegerType)
extlibrary_AudioVisualItem_damaged: Property = Property(name="damaged", type=BooleanType)
extlibrary_AudioVisualItem.attributes={extlibrary_AudioVisualItem_minutesLength, extlibrary_AudioVisualItem_damaged, extlibrary_AudioVisualItem_title}

# extlibrary_BookOnTape class attributes and methods

# AudioVisualItem class attributes and methods

# Relationships
author0: BinaryAssociation = BinaryAssociation(
    name="author0",
    ends={
        Property(name="Writer", type=extlibrary_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=extlibrary_Writer, multiplicity=Multiplicity(1, 1))
    }
)
parentBranch13: BinaryAssociation = BinaryAssociation(
    name="parentBranch13",
    ends={
        Property(name="Library14", type=extlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="branches", type=extlibrary_Library, multiplicity=Multiplicity(0, 1))
    }
)
casts15: BinaryAssociation = BinaryAssociation(
    name="casts15",
    ends={
        Property(name="extlibrary_Person", type=extlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Library16", type=extlibrary_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
readers17: BinaryAssociation = BinaryAssociation(
    name="readers17",
    ends={
        Property(name="extlibrary_Person19", type=extlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Library18", type=extlibrary_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books20: BinaryAssociation = BinaryAssociation(
    name="books20",
    ends={
        Property(name="Book", type=extlibrary_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=extlibrary_Book, multiplicity=Multiplicity(0, 9999))
    }
)
writers1: BinaryAssociation = BinaryAssociation(
    name="writers1",
    ends={
        Property(name="extlibrary_Writer", type=extlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Library", type=extlibrary_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
employees2: BinaryAssociation = BinaryAssociation(
    name="employees2",
    ends={
        Property(name="extlibrary_Employee", type=extlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Library3", type=extlibrary_Employee, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
borrowers4: BinaryAssociation = BinaryAssociation(
    name="borrowers4",
    ends={
        Property(name="extlibrary_Borrower", type=extlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Library5", type=extlibrary_Borrower, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stock6: BinaryAssociation = BinaryAssociation(
    name="stock6",
    ends={
        Property(name="extlibrary_Item", type=extlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Library7", type=extlibrary_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books8: BinaryAssociation = BinaryAssociation(
    name="books8",
    ends={
        Property(name="extlibrary_Book", type=extlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Library9", type=extlibrary_Book, multiplicity=Multiplicity(0, 9999))
    }
)
branches11: BinaryAssociation = BinaryAssociation(
    name="branches11",
    ends={
        Property(name="Library", type=extlibrary_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="parentBranch", type=extlibrary_Library, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cast27: BinaryAssociation = BinaryAssociation(
    name="cast27",
    ends={
        Property(name="extlibrary_Person28", type=extlibrary_VideoCassette, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_VideoCassette", type=extlibrary_Person, multiplicity=Multiplicity(0, 9999))
    }
)
borrowed29: BinaryAssociation = BinaryAssociation(
    name="borrowed29",
    ends={
        Property(name="Lendable", type=extlibrary_Borrower, multiplicity=Multiplicity(1, 1)),
        Property(name="borrowers", type=extlibrary_Lendable, multiplicity=Multiplicity(0, 9999))
    }
)
manager31: BinaryAssociation = BinaryAssociation(
    name="manager31",
    ends={
        Property(name="extlibrary_Employee32", type=extlibrary_Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_Employee30", type=extlibrary_Employee, multiplicity=Multiplicity(0, 1))
    }
)
borrowers21: BinaryAssociation = BinaryAssociation(
    name="borrowers21",
    ends={
        Property(name="Borrower", type=extlibrary_Lendable, multiplicity=Multiplicity(1, 1)),
        Property(name="borrowed", type=extlibrary_Borrower, multiplicity=Multiplicity(0, 9999))
    }
)
reader22: BinaryAssociation = BinaryAssociation(
    name="reader22",
    ends={
        Property(name="extlibrary_Person23", type=extlibrary_BookOnTape, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_BookOnTape", type=extlibrary_Person, multiplicity=Multiplicity(0, 1))
    }
)
author24: BinaryAssociation = BinaryAssociation(
    name="author24",
    ends={
        Property(name="extlibrary_Writer26", type=extlibrary_BookOnTape, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibrary_BookOnTape25", type=extlibrary_Writer, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_extlibrary_Book_CirculatingItem = Generalization(general=CirculatingItem, specific=extlibrary_Book)
gen_extlibrary_Writer_Person = Generalization(general=Person, specific=extlibrary_Writer)
gen_extlibrary_Library_Addressable = Generalization(general=Addressable, specific=extlibrary_Library)
gen_extlibrary_VideoCassette_AudioVisualItem = Generalization(general=AudioVisualItem, specific=extlibrary_VideoCassette)
gen_extlibrary_Borrower_Person = Generalization(general=Person, specific=extlibrary_Borrower)
gen_extlibrary_Person_Addressable = Generalization(general=Addressable, specific=extlibrary_Person)
gen_extlibrary_Employee_Person = Generalization(general=Person, specific=extlibrary_Employee)
gen_extlibrary_CirculatingItem_Item = Generalization(general=Item, specific=extlibrary_CirculatingItem)
gen_extlibrary_CirculatingItem_Lendable = Generalization(general=Lendable, specific=extlibrary_CirculatingItem)
gen_extlibrary_Periodical_Item = Generalization(general=Item, specific=extlibrary_Periodical)
gen_extlibrary_AudioVisualItem_CirculatingItem = Generalization(general=CirculatingItem, specific=extlibrary_AudioVisualItem)
gen_extlibrary_BookOnTape_AudioVisualItem = Generalization(general=AudioVisualItem, specific=extlibrary_BookOnTape)

# Domain Model
domain_model = DomainModel(
    name="extlibrary",
    types={extlibrary_Book, CirculatingItem, extlibrary_Writer, extlibrary_Person, Person, extlibrary_Lendable, extlibrary_Library, Addressable, extlibrary_Employee, extlibrary_Borrower, extlibrary_Item, extlibrary_VideoCassette, extlibrary_Addressable, extlibrary_CirculatingItem, Item, Lendable, extlibrary_Periodical, extlibrary_AudioVisualItem, extlibrary_BookOnTape, AudioVisualItem, BookCategory},
    associations={author0, parentBranch13, casts15, readers17, books20, writers1, employees2, borrowers4, stock6, books8, branches11, cast27, borrowed29, manager31, borrowers21, reader22, author24},
    generalizations={gen_extlibrary_Book_CirculatingItem, gen_extlibrary_Writer_Person, gen_extlibrary_Library_Addressable, gen_extlibrary_VideoCassette_AudioVisualItem, gen_extlibrary_Borrower_Person, gen_extlibrary_Person_Addressable, gen_extlibrary_Employee_Person, gen_extlibrary_CirculatingItem_Item, gen_extlibrary_CirculatingItem_Lendable, gen_extlibrary_Periodical_Item, gen_extlibrary_AudioVisualItem_CirculatingItem, gen_extlibrary_BookOnTape_AudioVisualItem},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)