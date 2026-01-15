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
extlibraryprofile_Book = Class(name="extlibraryprofile::Book")
CirculatingItem = Class(name="CirculatingItem")
extlibraryprofile_CirculatingItem = Class(name="extlibraryprofile::CirculatingItem", is_abstract=True)
Item = Class(name="Item")
Lendable = Class(name="Lendable")
extlibraryprofile_Item = Class(name="extlibraryprofile::Item", is_abstract=True)
extlibraryprofile_Lendable = Class(name="extlibraryprofile::Lendable", is_abstract=True)
extlibraryprofile_Library = Class(name="extlibraryprofile::Library")
Addressable = Class(name="Addressable")
extlibraryprofile_Package = Class(name="extlibraryprofile::Package")
extlibraryprofile_Addressable = Class(name="extlibraryprofile::Addressable", is_abstract=True)
extlibraryprofile_Writer = Class(name="extlibraryprofile::Writer")
Person = Class(name="Person")
extlibraryprofile_BookOnTape = Class(name="extlibraryprofile::BookOnTape")
extlibraryprofile_Person = Class(name="extlibraryprofile::Person", is_abstract=True)
extlibraryprofile_Class = Class(name="extlibraryprofile::Class")
extlibraryprofile_VideoCassete = Class(name="extlibraryprofile::VideoCassete")
AudioVisualItem = Class(name="AudioVisualItem")
extlibraryprofile_AudioVisualItem = Class(name="extlibraryprofile::AudioVisualItem", is_abstract=True)
extlibraryprofile_Periodical = Class(name="extlibraryprofile::Periodical")
extlibraryprofile_Borrower = Class(name="extlibraryprofile::Borrower")
extlibraryprofile_Employee = Class(name="extlibraryprofile::Employee")
extlibraryprofile_Borrows = Class(name="extlibraryprofile::Borrows")
extlibraryprofile_Dependency = Class(name="extlibraryprofile::Dependency")

# extlibraryprofile_Book class attributes and methods
extlibraryprofile_Book_pages: Property = Property(name="pages", type=StringType)
extlibraryprofile_Book_category: Property = Property(name="category", type=StringType)
extlibraryprofile_Book.attributes={extlibraryprofile_Book_category, extlibraryprofile_Book_pages}

# CirculatingItem class attributes and methods

# extlibraryprofile_CirculatingItem class attributes and methods

# Item class attributes and methods

# Lendable class attributes and methods

# extlibraryprofile_Item class attributes and methods
extlibraryprofile_Item_title: Property = Property(name="title", type=StringType)
extlibraryprofile_Item_publicationDate: Property = Property(name="publicationDate", type=StringType)
extlibraryprofile_Item.attributes={extlibraryprofile_Item_publicationDate, extlibraryprofile_Item_title}

# extlibraryprofile_Lendable class attributes and methods
extlibraryprofile_Lendable_copies: Property = Property(name="copies", type=StringType)
extlibraryprofile_Lendable.attributes={extlibraryprofile_Lendable_copies}

# extlibraryprofile_Library class attributes and methods
extlibraryprofile_Library_name: Property = Property(name="name", type=StringType)
extlibraryprofile_Library.attributes={extlibraryprofile_Library_name}

# Addressable class attributes and methods

# extlibraryprofile_Package class attributes and methods

# extlibraryprofile_Addressable class attributes and methods
extlibraryprofile_Addressable_address: Property = Property(name="address", type=StringType)
extlibraryprofile_Addressable.attributes={extlibraryprofile_Addressable_address}

# extlibraryprofile_Writer class attributes and methods
extlibraryprofile_Writer_name: Property = Property(name="name", type=StringType)
extlibraryprofile_Writer.attributes={extlibraryprofile_Writer_name}

# Person class attributes and methods

# extlibraryprofile_BookOnTape class attributes and methods

# extlibraryprofile_Person class attributes and methods
extlibraryprofile_Person_firstName: Property = Property(name="firstName", type=StringType)
extlibraryprofile_Person_lastName: Property = Property(name="lastName", type=StringType)
extlibraryprofile_Person.attributes={extlibraryprofile_Person_firstName, extlibraryprofile_Person_lastName}

# extlibraryprofile_Class class attributes and methods

# extlibraryprofile_VideoCassete class attributes and methods

# AudioVisualItem class attributes and methods

# extlibraryprofile_AudioVisualItem class attributes and methods
extlibraryprofile_AudioVisualItem_minutesLength: Property = Property(name="minutesLength", type=StringType)
extlibraryprofile_AudioVisualItem_damaged: Property = Property(name="damaged", type=StringType)
extlibraryprofile_AudioVisualItem.attributes={extlibraryprofile_AudioVisualItem_minutesLength, extlibraryprofile_AudioVisualItem_damaged}

# extlibraryprofile_Periodical class attributes and methods
extlibraryprofile_Periodical_issuesPerYear: Property = Property(name="issuesPerYear", type=StringType)
extlibraryprofile_Periodical.attributes={extlibraryprofile_Periodical_issuesPerYear}

# extlibraryprofile_Borrower class attributes and methods

# extlibraryprofile_Employee class attributes and methods

# extlibraryprofile_Borrows class attributes and methods

# extlibraryprofile_Dependency class attributes and methods

# Relationships
base_Class0: BinaryAssociation = BinaryAssociation(
    name="base_Class0",
    ends={
        Property(name="extlibraryprofile_Class", type=extlibraryprofile_Item, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibraryprofile_Item", type=extlibraryprofile_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Package1: BinaryAssociation = BinaryAssociation(
    name="base_Package1",
    ends={
        Property(name="extlibraryprofile_Package", type=extlibraryprofile_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibraryprofile_Library", type=extlibraryprofile_Package, multiplicity=Multiplicity(1, 1))
    }
)
bookOnTape2: BinaryAssociation = BinaryAssociation(
    name="bookOnTape2",
    ends={
        Property(name="extlibraryprofile_BookOnTape", type=extlibraryprofile_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibraryprofile_Writer", type=extlibraryprofile_BookOnTape, multiplicity=Multiplicity(1, 1))
    }
)
videoCassete3: BinaryAssociation = BinaryAssociation(
    name="videoCassete3",
    ends={
        Property(name="extlibraryprofile_VideoCassete", type=extlibraryprofile_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibraryprofile_Person", type=extlibraryprofile_VideoCassete, multiplicity=Multiplicity(0, 9999))
    }
)
bookOnTape14: BinaryAssociation = BinaryAssociation(
    name="bookOnTape14",
    ends={
        Property(name="extlibraryprofile_BookOnTape6", type=extlibraryprofile_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibraryprofile_Person5", type=extlibraryprofile_BookOnTape, multiplicity=Multiplicity(1, 1))
    }
)
base_Class7: BinaryAssociation = BinaryAssociation(
    name="base_Class7",
    ends={
        Property(name="extlibraryprofile_Class9", type=extlibraryprofile_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibraryprofile_Person8", type=extlibraryprofile_Class, multiplicity=Multiplicity(1, 1))
    }
)
base_Dependency10: BinaryAssociation = BinaryAssociation(
    name="base_Dependency10",
    ends={
        Property(name="extlibraryprofile_Dependency", type=extlibraryprofile_Borrows, multiplicity=Multiplicity(1, 1)),
        Property(name="extlibraryprofile_Borrows", type=extlibraryprofile_Dependency, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_extlibraryprofile_Book_CirculatingItem = Generalization(general=CirculatingItem, specific=extlibraryprofile_Book)
gen_extlibraryprofile_CirculatingItem_Item = Generalization(general=Item, specific=extlibraryprofile_CirculatingItem)
gen_extlibraryprofile_CirculatingItem_Lendable = Generalization(general=Lendable, specific=extlibraryprofile_CirculatingItem)
gen_extlibraryprofile_Library_Addressable = Generalization(general=Addressable, specific=extlibraryprofile_Library)
gen_extlibraryprofile_Writer_Person = Generalization(general=Person, specific=extlibraryprofile_Writer)
gen_extlibraryprofile_Person_Addressable = Generalization(general=Addressable, specific=extlibraryprofile_Person)
gen_extlibraryprofile_VideoCassete_AudioVisualItem = Generalization(general=AudioVisualItem, specific=extlibraryprofile_VideoCassete)
gen_extlibraryprofile_AudioVisualItem_CirculatingItem = Generalization(general=CirculatingItem, specific=extlibraryprofile_AudioVisualItem)
gen_extlibraryprofile_BookOnTape_AudioVisualItem = Generalization(general=AudioVisualItem, specific=extlibraryprofile_BookOnTape)
gen_extlibraryprofile_Periodical_Item = Generalization(general=Item, specific=extlibraryprofile_Periodical)
gen_extlibraryprofile_Borrower_Person = Generalization(general=Person, specific=extlibraryprofile_Borrower)
gen_extlibraryprofile_Employee_Person = Generalization(general=Person, specific=extlibraryprofile_Employee)

# Domain Model
domain_model = DomainModel(
    name="extlibraryprofile",
    types={extlibraryprofile_Book, CirculatingItem, extlibraryprofile_CirculatingItem, Item, Lendable, extlibraryprofile_Item, extlibraryprofile_Lendable, extlibraryprofile_Library, Addressable, extlibraryprofile_Package, extlibraryprofile_Addressable, extlibraryprofile_Writer, Person, extlibraryprofile_BookOnTape, extlibraryprofile_Person, extlibraryprofile_Class, extlibraryprofile_VideoCassete, AudioVisualItem, extlibraryprofile_AudioVisualItem, extlibraryprofile_Periodical, extlibraryprofile_Borrower, extlibraryprofile_Employee, extlibraryprofile_Borrows, extlibraryprofile_Dependency, BookCategory},
    associations={base_Class0, base_Package1, bookOnTape2, videoCassete3, bookOnTape14, base_Class7, base_Dependency10},
    generalizations={gen_extlibraryprofile_Book_CirculatingItem, gen_extlibraryprofile_CirculatingItem_Item, gen_extlibraryprofile_CirculatingItem_Lendable, gen_extlibraryprofile_Library_Addressable, gen_extlibraryprofile_Writer_Person, gen_extlibraryprofile_Person_Addressable, gen_extlibraryprofile_VideoCassete_AudioVisualItem, gen_extlibraryprofile_AudioVisualItem_CirculatingItem, gen_extlibraryprofile_BookOnTape_AudioVisualItem, gen_extlibraryprofile_Periodical_Item, gen_extlibraryprofile_Borrower_Person, gen_extlibraryprofile_Employee_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)