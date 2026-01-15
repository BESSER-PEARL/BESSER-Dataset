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
BookType: Enumeration = Enumeration(
    name="BookType",
    literals={
            EnumerationLiteral(name="Child"),
			EnumerationLiteral(name="Parent")
    }
)

# Classes
emftest_ParentBook = Class(name="emftest::ParentBook")
emftest_BookCollection = Class(name="emftest::BookCollection")
emftest_Book = Class(name="emftest::Book", is_abstract=True)
emftest_Author = Class(name="emftest::Author")
emftest_ChildBook = Class(name="emftest::ChildBook")
Book = Class(name="Book")
emftest_Library = Class(name="emftest::Library")

# emftest_ParentBook class attributes and methods

# emftest_BookCollection class attributes and methods

# emftest_Book class attributes and methods
emftest_Book_title: Property = Property(name="title", type=StringType)
emftest_Book_pages: Property = Property(name="pages", type=IntegerType)
emftest_Book.attributes={emftest_Book_pages, emftest_Book_title}

# emftest_Author class attributes and methods
emftest_Author_name: Property = Property(name="name", type=StringType)
emftest_Author_m_writeBook: Method = Method(name="writeBook", parameters={Parameter(name='pages'), Parameter(name='title'), Parameter(name='type')}, type=Book)
emftest_Author.attributes={emftest_Author_name}
emftest_Author.methods={emftest_Author_m_writeBook}

# emftest_ChildBook class attributes and methods

# Book class attributes and methods

# emftest_Library class attributes and methods

# Relationships
books1: BinaryAssociation = BinaryAssociation(
    name="books1",
    ends={
        Property(name="emftest_Book2", type=emftest_BookCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="emftest_BookCollection", type=emftest_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors0: BinaryAssociation = BinaryAssociation(
    name="authors0",
    ends={
        Property(name="emftest_Author", type=emftest_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="emftest_Book", type=emftest_Author, multiplicity=Multiplicity(1, 9999))
    }
)
collections3: BinaryAssociation = BinaryAssociation(
    name="collections3",
    ends={
        Property(name="emftest_BookCollection4", type=emftest_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="emftest_Library", type=emftest_BookCollection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books5: BinaryAssociation = BinaryAssociation(
    name="books5",
    ends={
        Property(name="emftest_Book7", type=emftest_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="emftest_Author6", type=emftest_Book, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_emftest_ParentBook_Book = Generalization(general=Book, specific=emftest_ParentBook)
gen_emftest_ChildBook_Book = Generalization(general=Book, specific=emftest_ChildBook)

# Domain Model
domain_model = DomainModel(
    name="emftest",
    types={emftest_ParentBook, emftest_BookCollection, emftest_Book, emftest_Author, emftest_ChildBook, Book, emftest_Library, BookType},
    associations={books1, authors0, collections3, books5},
    generalizations={gen_emftest_ParentBook_Book, gen_emftest_ChildBook_Book},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)