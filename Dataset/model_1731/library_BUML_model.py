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
library_MultimediaItem = Class(name="library::MultimediaItem", is_abstract=True)
library_DVD = Class(name="library::DVD")
MultimediaItem = Class(name="MultimediaItem")
library_LibraryShelf = Class(name="library::LibraryShelf")
library_Item = Class(name="library::Item", is_abstract=True)
library_Book = Class(name="library::Book")
Item = Class(name="Item")
library_BlueRay = Class(name="library::BlueRay")
library_CD = Class(name="library::CD")

# library_MultimediaItem class attributes and methods
library_MultimediaItem_length: Property = Property(name="length", type=FloatType)
library_MultimediaItem.attributes={library_MultimediaItem_length}

# library_DVD class attributes and methods

# MultimediaItem class attributes and methods

# library_LibraryShelf class attributes and methods
library_LibraryShelf_name: Property = Property(name="name", type=StringType)
library_LibraryShelf.attributes={library_LibraryShelf_name}

# library_Item class attributes and methods
library_Item_title: Property = Property(name="title", type=StringType)
library_Item_pubDate: Property = Property(name="pubDate", type=DateType)
library_Item.attributes={library_Item_pubDate, library_Item_title}

# library_Book class attributes and methods
library_Book_numPages: Property = Property(name="numPages", type=IntegerType)
library_Book.attributes={library_Book_numPages}

# Item class attributes and methods

# library_BlueRay class attributes and methods

# library_CD class attributes and methods

# Relationships
items0: BinaryAssociation = BinaryAssociation(
    name="items0",
    ends={
        Property(name="library_Item", type=library_LibraryShelf, multiplicity=Multiplicity(1, 1)),
        Property(name="library_LibraryShelf", type=library_Item, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_library_MultimediaItem_Item = Generalization(general=Item, specific=library_MultimediaItem)
gen_library_DVD_MultimediaItem = Generalization(general=MultimediaItem, specific=library_DVD)
gen_library_Book_Item = Generalization(general=Item, specific=library_Book)
gen_library_BlueRay_MultimediaItem = Generalization(general=MultimediaItem, specific=library_BlueRay)
gen_library_CD_MultimediaItem = Generalization(general=MultimediaItem, specific=library_CD)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_MultimediaItem, library_DVD, MultimediaItem, library_LibraryShelf, library_Item, library_Book, Item, library_BlueRay, library_CD},
    associations={items0},
    generalizations={gen_library_MultimediaItem_Item, gen_library_DVD_MultimediaItem, gen_library_Book_Item, gen_library_BlueRay_MultimediaItem, gen_library_CD_MultimediaItem},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)