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
bibtex_Article = Class(name="bibtex_Article")
bibtex_Entries = Class(name="bibtex_Entries", is_abstract=True)
bibtex_Bibtex = Class(name="bibtex_Bibtex")
bibtex_Book = Class(name="bibtex_Book")
Entries = Class(name="Entries")
AuthoredEntry = Class(name="AuthoredEntry")
DatedEntry = Class(name="DatedEntry")
MonthEntry = Class(name="MonthEntry")
bibtex_DatedEntry = Class(name="bibtex_DatedEntry", is_abstract=True)
bibtex_AuthoredEntry = Class(name="bibtex_AuthoredEntry", is_abstract=True)
bibtex_Author = Class(name="bibtex_Author")
bibtex_MonthEntry = Class(name="bibtex_MonthEntry", is_abstract=True)

# bibtex_Article class attributes and methods
bibtex_Article_journal: Property = Property(name="journal", type=StringType)
bibtex_Article_volume: Property = Property(name="volume", type=IntegerType)
bibtex_Article_number: Property = Property(name="number", type=IntegerType)
bibtex_Article_pages: Property = Property(name="pages", type=IntegerType)
bibtex_Article_note: Property = Property(name="note", type=StringType)
bibtex_Article.attributes={bibtex_Article_number, bibtex_Article_volume, bibtex_Article_journal, bibtex_Article_pages, bibtex_Article_note}

# bibtex_Entries class attributes and methods

# bibtex_Bibtex class attributes and methods

# bibtex_Book class attributes and methods
bibtex_Book_publisher: Property = Property(name="publisher", type=StringType)
bibtex_Book_volume: Property = Property(name="volume", type=IntegerType)
bibtex_Book_series: Property = Property(name="series", type=IntegerType)
bibtex_Book_address: Property = Property(name="address", type=StringType)
bibtex_Book_edition: Property = Property(name="edition", type=IntegerType)
bibtex_Book.attributes={bibtex_Book_edition, bibtex_Book_series, bibtex_Book_address, bibtex_Book_publisher, bibtex_Book_volume}

# Entries class attributes and methods

# AuthoredEntry class attributes and methods

# DatedEntry class attributes and methods

# MonthEntry class attributes and methods

# bibtex_DatedEntry class attributes and methods
bibtex_DatedEntry_year: Property = Property(name="year", type=IntegerType)
bibtex_DatedEntry.attributes={bibtex_DatedEntry_year}

# bibtex_AuthoredEntry class attributes and methods

# bibtex_Author class attributes and methods
bibtex_Author_name: Property = Property(name="name", type=StringType)
bibtex_Author_surname: Property = Property(name="surname", type=StringType)
bibtex_Author.attributes={bibtex_Author_surname, bibtex_Author_name}

# bibtex_MonthEntry class attributes and methods
bibtex_MonthEntry_month: Property = Property(name="month", type=StringType)
bibtex_MonthEntry.attributes={bibtex_MonthEntry_month}

# Relationships
entries0: BinaryAssociation = BinaryAssociation(
    name="entries0",
    ends={
        Property(name="bibtex_Entries", type=bibtex_Bibtex, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Bibtex", type=bibtex_Entries, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
has1: BinaryAssociation = BinaryAssociation(
    name="has1",
    ends={
        Property(name="bibtex_AuthoredEntry", type=bibtex_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="bibtex_Author", type=bibtex_AuthoredEntry, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_bibtex_Book_Entries = Generalization(general=Entries, specific=bibtex_Book)
gen_bibtex_Article_Entries = Generalization(general=Entries, specific=bibtex_Article)
gen_bibtex_Article_AuthoredEntry = Generalization(general=AuthoredEntry, specific=bibtex_Article)
gen_bibtex_Article_DatedEntry = Generalization(general=DatedEntry, specific=bibtex_Article)
gen_bibtex_Article_MonthEntry = Generalization(general=MonthEntry, specific=bibtex_Article)
gen_bibtex_Book_AuthoredEntry = Generalization(general=AuthoredEntry, specific=bibtex_Book)
gen_bibtex_Book_DatedEntry = Generalization(general=DatedEntry, specific=bibtex_Book)
gen_bibtex_Book_MonthEntry = Generalization(general=MonthEntry, specific=bibtex_Book)
gen_bibtex_AuthoredEntry_Entries = Generalization(general=Entries, specific=bibtex_AuthoredEntry)
gen_bibtex_DatedEntry_Entries = Generalization(general=Entries, specific=bibtex_DatedEntry)
gen_bibtex_MonthEntry_Entries = Generalization(general=Entries, specific=bibtex_MonthEntry)

# Domain Model
domain_model = DomainModel(
    name="bibtex",
    types={bibtex_Article, bibtex_Entries, bibtex_Bibtex, bibtex_Book, Entries, AuthoredEntry, DatedEntry, MonthEntry, bibtex_DatedEntry, bibtex_AuthoredEntry, bibtex_Author, bibtex_MonthEntry},
    associations={entries0, has1},
    generalizations={gen_bibtex_Book_Entries, gen_bibtex_Article_Entries, gen_bibtex_Article_AuthoredEntry, gen_bibtex_Article_DatedEntry, gen_bibtex_Article_MonthEntry, gen_bibtex_Book_AuthoredEntry, gen_bibtex_Book_DatedEntry, gen_bibtex_Book_MonthEntry, gen_bibtex_AuthoredEntry_Entries, gen_bibtex_DatedEntry_Entries, gen_bibtex_MonthEntry_Entries},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)