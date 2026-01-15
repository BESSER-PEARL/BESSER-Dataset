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
NamedElement = Class(name="NamedElement")
libraryModel_ecore_Author = Class(name="libraryModel::ecore::Author")
libraryModel_ecore_LibraryModel = Class(name="libraryModel::ecore::LibraryModel")
libraryModel_ecore_Book = Class(name="libraryModel::ecore::Book")
libraryModel_ecore_Picture = Class(name="libraryModel::ecore::Picture")
libraryModel_ecore_NamedElement = Class(name="libraryModel::ecore::NamedElement")

# NamedElement class attributes and methods

# libraryModel_ecore_Author class attributes and methods

# libraryModel_ecore_LibraryModel class attributes and methods
libraryModel_ecore_LibraryModel_m_printLibrary: Method = Method(name="printLibrary", parameters={})
libraryModel_ecore_LibraryModel.methods={libraryModel_ecore_LibraryModel_m_printLibrary}

# libraryModel_ecore_Book class attributes and methods

# libraryModel_ecore_Picture class attributes and methods
libraryModel_ecore_Picture_pageNumber: Property = Property(name="pageNumber", type=StringType)
libraryModel_ecore_Picture.attributes={libraryModel_ecore_Picture_pageNumber}

# libraryModel_ecore_NamedElement class attributes and methods
libraryModel_ecore_NamedElement_Name: Property = Property(name="Name", type=StringType)
libraryModel_ecore_NamedElement.attributes={libraryModel_ecore_NamedElement_Name}

# Relationships
authors0: BinaryAssociation = BinaryAssociation(
    name="authors0",
    ends={
        Property(name="libraryModel_ecore_Author", type=libraryModel_ecore_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryModel_ecore_Book", type=libraryModel_ecore_Author, multiplicity=Multiplicity(0, 9999))
    }
)
library4: BinaryAssociation = BinaryAssociation(
    name="library4",
    ends={
        Property(name="LibraryModel5", type=libraryModel_ecore_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=libraryModel_ecore_LibraryModel, multiplicity=Multiplicity(0, 1))
    }
)
library1: BinaryAssociation = BinaryAssociation(
    name="library1",
    ends={
        Property(name="LibraryModel", type=libraryModel_ecore_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="book", type=libraryModel_ecore_LibraryModel, multiplicity=Multiplicity(0, 1))
    }
)
pictures2: BinaryAssociation = BinaryAssociation(
    name="pictures2",
    ends={
        Property(name="Picture", type=libraryModel_ecore_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="book3", type=libraryModel_ecore_Picture, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
book6: BinaryAssociation = BinaryAssociation(
    name="book6",
    ends={
        Property(name="Book", type=libraryModel_ecore_LibraryModel, multiplicity=Multiplicity(1, 1)),
        Property(name="library", type=libraryModel_ecore_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authors7: BinaryAssociation = BinaryAssociation(
    name="authors7",
    ends={
        Property(name="Author", type=libraryModel_ecore_LibraryModel, multiplicity=Multiplicity(1, 1)),
        Property(name="library8", type=libraryModel_ecore_Author, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
book9: BinaryAssociation = BinaryAssociation(
    name="book9",
    ends={
        Property(name="Book10", type=libraryModel_ecore_Picture, multiplicity=Multiplicity(1, 1)),
        Property(name="pictures", type=libraryModel_ecore_Book, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_libraryModel_ecore_Book_NamedElement = Generalization(general=NamedElement, specific=libraryModel_ecore_Book)
gen_libraryModel_ecore_Author_NamedElement = Generalization(general=NamedElement, specific=libraryModel_ecore_Author)
gen_libraryModel_ecore_Picture_NamedElement = Generalization(general=NamedElement, specific=libraryModel_ecore_Picture)

# Domain Model
domain_model = DomainModel(
    name="libraryModel_ecore",
    types={NamedElement, libraryModel_ecore_Author, libraryModel_ecore_LibraryModel, libraryModel_ecore_Book, libraryModel_ecore_Picture, libraryModel_ecore_NamedElement},
    associations={authors0, library4, library1, pictures2, book6, authors7, book9},
    generalizations={gen_libraryModel_ecore_Book_NamedElement, gen_libraryModel_ecore_Author_NamedElement, gen_libraryModel_ecore_Picture_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)