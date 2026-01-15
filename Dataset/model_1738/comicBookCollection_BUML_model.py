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
comicBookCollection_ComicBookCollection = Class(name="comicBookCollection::ComicBookCollection")
comicBookCollection_Publisher = Class(name="comicBookCollection::Publisher")
comicBookCollection_Series = Class(name="comicBookCollection::Series")
comicBookCollection_Book = Class(name="comicBookCollection::Book")
comicBookCollection_Person = Class(name="comicBookCollection::Person")

# comicBookCollection_ComicBookCollection class attributes and methods

# comicBookCollection_Publisher class attributes and methods
comicBookCollection_Publisher_publishingName: Property = Property(name="publishingName", type=StringType)
comicBookCollection_Publisher.attributes={comicBookCollection_Publisher_publishingName}

# comicBookCollection_Series class attributes and methods
comicBookCollection_Series_seriesTitle: Property = Property(name="seriesTitle", type=StringType)
comicBookCollection_Series.attributes={comicBookCollection_Series_seriesTitle}

# comicBookCollection_Book class attributes and methods
comicBookCollection_Book_title: Property = Property(name="title", type=StringType)
comicBookCollection_Book_publicationDate: Property = Property(name="publicationDate", type=StringType)
comicBookCollection_Book.attributes={comicBookCollection_Book_title, comicBookCollection_Book_publicationDate}

# comicBookCollection_Person class attributes and methods
comicBookCollection_Person_name: Property = Property(name="name", type=StringType)
comicBookCollection_Person.attributes={comicBookCollection_Person_name}

# Relationships
publishers0: BinaryAssociation = BinaryAssociation(
    name="publishers0",
    ends={
        Property(name="comicBookCollection_Publisher", type=comicBookCollection_ComicBookCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="comicBookCollection_ComicBookCollection", type=comicBookCollection_Publisher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
series1: BinaryAssociation = BinaryAssociation(
    name="series1",
    ends={
        Property(name="comicBookCollection_Series", type=comicBookCollection_Publisher, multiplicity=Multiplicity(1, 1)),
        Property(name="comicBookCollection_Publisher2", type=comicBookCollection_Series, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
booksInSeries3: BinaryAssociation = BinaryAssociation(
    name="booksInSeries3",
    ends={
        Property(name="comicBookCollection_Book", type=comicBookCollection_Series, multiplicity=Multiplicity(1, 1)),
        Property(name="comicBookCollection_Series4", type=comicBookCollection_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writers5: BinaryAssociation = BinaryAssociation(
    name="writers5",
    ends={
        Property(name="comicBookCollection_Person", type=comicBookCollection_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="comicBookCollection_Book6", type=comicBookCollection_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
editors7: BinaryAssociation = BinaryAssociation(
    name="editors7",
    ends={
        Property(name="comicBookCollection_Person9", type=comicBookCollection_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="comicBookCollection_Book8", type=comicBookCollection_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artists10: BinaryAssociation = BinaryAssociation(
    name="artists10",
    ends={
        Property(name="comicBookCollection_Person12", type=comicBookCollection_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="comicBookCollection_Book11", type=comicBookCollection_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
coverArtist13: BinaryAssociation = BinaryAssociation(
    name="coverArtist13",
    ends={
        Property(name="comicBookCollection_Person15", type=comicBookCollection_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="comicBookCollection_Book14", type=comicBookCollection_Person, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="comicBookCollection",
    types={comicBookCollection_ComicBookCollection, comicBookCollection_Publisher, comicBookCollection_Series, comicBookCollection_Book, comicBookCollection_Person},
    associations={publishers0, series1, booksInSeries3, writers5, editors7, artists10, coverArtist13},
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