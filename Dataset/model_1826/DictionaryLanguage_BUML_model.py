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
DictionaryLanguage_Author = Class(name="DictionaryLanguage::Author")
DictionaryLanguage_Library = Class(name="DictionaryLanguage::Library")
DictionaryLanguage_Dictionary = Class(name="DictionaryLanguage::Dictionary")
DictionaryLanguage_Shelf = Class(name="DictionaryLanguage::Shelf")
DictionaryLanguage_Entry = Class(name="DictionaryLanguage::Entry")

# DictionaryLanguage_Author class attributes and methods
DictionaryLanguage_Author_email: Property = Property(name="email", type=StringType)
DictionaryLanguage_Author.attributes={DictionaryLanguage_Author_email}

# DictionaryLanguage_Library class attributes and methods
DictionaryLanguage_Library_name: Property = Property(name="name", type=StringType)
DictionaryLanguage_Library.attributes={DictionaryLanguage_Library_name}

# DictionaryLanguage_Dictionary class attributes and methods
DictionaryLanguage_Dictionary_title: Property = Property(name="title", type=StringType)
DictionaryLanguage_Dictionary.attributes={DictionaryLanguage_Dictionary_title}

# DictionaryLanguage_Shelf class attributes and methods
DictionaryLanguage_Shelf_description: Property = Property(name="description", type=StringType)
DictionaryLanguage_Shelf.attributes={DictionaryLanguage_Shelf_description}

# DictionaryLanguage_Entry class attributes and methods
DictionaryLanguage_Entry_content: Property = Property(name="content", type=StringType)
DictionaryLanguage_Entry_level: Property = Property(name="level", type=StringType)
DictionaryLanguage_Entry.attributes={DictionaryLanguage_Entry_content, DictionaryLanguage_Entry_level}

# Relationships
library0: BinaryAssociation = BinaryAssociation(
    name="library0",
    ends={
        Property(name="Library", type=DictionaryLanguage_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=DictionaryLanguage_Library, multiplicity=Multiplicity(1, 1))
    }
)
dictionary1: BinaryAssociation = BinaryAssociation(
    name="dictionary1",
    ends={
        Property(name="Dictionary", type=DictionaryLanguage_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="author2", type=DictionaryLanguage_Dictionary, multiplicity=Multiplicity(0, 9999))
    }
)
shelf3: BinaryAssociation = BinaryAssociation(
    name="shelf3",
    ends={
        Property(name="Shelf", type=DictionaryLanguage_Dictionary, multiplicity=Multiplicity(1, 1)),
        Property(name="dictionary", type=DictionaryLanguage_Shelf, multiplicity=Multiplicity(1, 1))
    }
)
author4: BinaryAssociation = BinaryAssociation(
    name="author4",
    ends={
        Property(name="Author", type=DictionaryLanguage_Dictionary, multiplicity=Multiplicity(1, 1)),
        Property(name="dictionary5", type=DictionaryLanguage_Author, multiplicity=Multiplicity(1, 1))
    }
)
entry6: BinaryAssociation = BinaryAssociation(
    name="entry6",
    ends={
        Property(name="DictionaryLanguage_Entry", type=DictionaryLanguage_Dictionary, multiplicity=Multiplicity(1, 1)),
        Property(name="DictionaryLanguage_Dictionary", type=DictionaryLanguage_Entry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
shelf7: BinaryAssociation = BinaryAssociation(
    name="shelf7",
    ends={
        Property(name="DictionaryLanguage_Shelf", type=DictionaryLanguage_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="DictionaryLanguage_Library", type=DictionaryLanguage_Shelf, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
author8: BinaryAssociation = BinaryAssociation(
    name="author8",
    ends={
        Property(name="Author9", type=DictionaryLanguage_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library", type=DictionaryLanguage_Author, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dictionary10: BinaryAssociation = BinaryAssociation(
    name="dictionary10",
    ends={
        Property(name="Dictionary11", type=DictionaryLanguage_Shelf, multiplicity=Multiplicity(1, 1)),
        Property(name="shelf", type=DictionaryLanguage_Dictionary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="DictionaryLanguage",
    types={DictionaryLanguage_Author, DictionaryLanguage_Library, DictionaryLanguage_Dictionary, DictionaryLanguage_Shelf, DictionaryLanguage_Entry},
    associations={library0, dictionary1, shelf3, author4, entry6, shelf7, author8, dictionary10},
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