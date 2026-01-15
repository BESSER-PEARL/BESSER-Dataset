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
comicBooks_ComicBookCollection = Class(name="comicBooks::ComicBookCollection")
comicBooks_Book = Class(name="comicBooks::Book")
comicBooks_Editor = Class(name="comicBooks::Editor")
comicBooks_Writer = Class(name="comicBooks::Writer")
comicBooks_Publisher = Class(name="comicBooks::Publisher")
comicBooks_Artist = Class(name="comicBooks::Artist")
comicBooks_Series = Class(name="comicBooks::Series")

# comicBooks_ComicBookCollection class attributes and methods

# comicBooks_Book class attributes and methods
comicBooks_Book_name: Property = Property(name="name", type=StringType)
comicBooks_Book_publicationDate: Property = Property(name="publicationDate", type=StringType)
comicBooks_Book.attributes={comicBooks_Book_name, comicBooks_Book_publicationDate}

# comicBooks_Editor class attributes and methods
comicBooks_Editor_name: Property = Property(name="name", type=StringType)
comicBooks_Editor.attributes={comicBooks_Editor_name}

# comicBooks_Writer class attributes and methods
comicBooks_Writer_name: Property = Property(name="name", type=StringType)
comicBooks_Writer.attributes={comicBooks_Writer_name}

# comicBooks_Publisher class attributes and methods
comicBooks_Publisher_publishersName: Property = Property(name="publishersName", type=StringType)
comicBooks_Publisher.attributes={comicBooks_Publisher_publishersName}

# comicBooks_Artist class attributes and methods
comicBooks_Artist_name: Property = Property(name="name", type=StringType)
comicBooks_Artist.attributes={comicBooks_Artist_name}

# comicBooks_Series class attributes and methods
comicBooks_Series_seriesName: Property = Property(name="seriesName", type=StringType)
comicBooks_Series.attributes={comicBooks_Series_seriesName}

# Relationships
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="comicBooks_Book", type=comicBooks_ComicBookCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="comicBooks_ComicBookCollection", type=comicBooks_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
editors3: BinaryAssociation = BinaryAssociation(
    name="editors3",
    ends={
        Property(name="comicBooks_Editor", type=comicBooks_ComicBookCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="comicBooks_ComicBookCollection4", type=comicBooks_Editor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writers5: BinaryAssociation = BinaryAssociation(
    name="writers5",
    ends={
        Property(name="comicBooks_Writer", type=comicBooks_ComicBookCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="comicBooks_ComicBookCollection6", type=comicBooks_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artists1: BinaryAssociation = BinaryAssociation(
    name="artists1",
    ends={
        Property(name="comicBooks_Artist", type=comicBooks_ComicBookCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="comicBooks_ComicBookCollection2", type=comicBooks_Artist, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
series9: BinaryAssociation = BinaryAssociation(
    name="series9",
    ends={
        Property(name="comicBooks_Series", type=comicBooks_ComicBookCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="comicBooks_ComicBookCollection10", type=comicBooks_Series, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
booksPublished11: BinaryAssociation = BinaryAssociation(
    name="booksPublished11",
    ends={
        Property(name="Book", type=comicBooks_Publisher, multiplicity=Multiplicity(1, 1)),
        Property(name="publisher", type=comicBooks_Book, multiplicity=Multiplicity(0, 9999))
    }
)
publishingCompanies7: BinaryAssociation = BinaryAssociation(
    name="publishingCompanies7",
    ends={
        Property(name="comicBooks_Publisher", type=comicBooks_ComicBookCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="comicBooks_ComicBookCollection8", type=comicBooks_Publisher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artists14: BinaryAssociation = BinaryAssociation(
    name="artists14",
    ends={
        Property(name="Artist", type=comicBooks_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="booksArtistFor", type=comicBooks_Artist, multiplicity=Multiplicity(1, 9999))
    }
)
booksInSeries12: BinaryAssociation = BinaryAssociation(
    name="booksInSeries12",
    ends={
        Property(name="Book13", type=comicBooks_Series, multiplicity=Multiplicity(1, 1)),
        Property(name="seriesPartOf", type=comicBooks_Book, multiplicity=Multiplicity(0, 9999))
    }
)
writers16: BinaryAssociation = BinaryAssociation(
    name="writers16",
    ends={
        Property(name="Writer", type=comicBooks_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="booksWriterFor", type=comicBooks_Writer, multiplicity=Multiplicity(1, 9999))
    }
)
coverArtist17: BinaryAssociation = BinaryAssociation(
    name="coverArtist17",
    ends={
        Property(name="Artist18", type=comicBooks_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="booksCoverArtistFor", type=comicBooks_Artist, multiplicity=Multiplicity(1, 1))
    }
)
publisher19: BinaryAssociation = BinaryAssociation(
    name="publisher19",
    ends={
        Property(name="Publisher", type=comicBooks_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="booksPublished", type=comicBooks_Publisher, multiplicity=Multiplicity(1, 1))
    }
)
editors15: BinaryAssociation = BinaryAssociation(
    name="editors15",
    ends={
        Property(name="Editor", type=comicBooks_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="booksEditorFor", type=comicBooks_Editor, multiplicity=Multiplicity(1, 9999))
    }
)
booksArtistFor21: BinaryAssociation = BinaryAssociation(
    name="booksArtistFor21",
    ends={
        Property(name="Book22", type=comicBooks_Artist, multiplicity=Multiplicity(1, 1)),
        Property(name="artists", type=comicBooks_Book, multiplicity=Multiplicity(0, 9999))
    }
)
booksCoverArtistFor23: BinaryAssociation = BinaryAssociation(
    name="booksCoverArtistFor23",
    ends={
        Property(name="Book24", type=comicBooks_Artist, multiplicity=Multiplicity(1, 1)),
        Property(name="coverArtist", type=comicBooks_Book, multiplicity=Multiplicity(0, 9999))
    }
)
seriesPartOf20: BinaryAssociation = BinaryAssociation(
    name="seriesPartOf20",
    ends={
        Property(name="Series", type=comicBooks_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="booksInSeries", type=comicBooks_Series, multiplicity=Multiplicity(1, 1))
    }
)
booksEditorFor25: BinaryAssociation = BinaryAssociation(
    name="booksEditorFor25",
    ends={
        Property(name="Book26", type=comicBooks_Editor, multiplicity=Multiplicity(1, 1)),
        Property(name="editors", type=comicBooks_Book, multiplicity=Multiplicity(0, 9999))
    }
)
booksWriterFor27: BinaryAssociation = BinaryAssociation(
    name="booksWriterFor27",
    ends={
        Property(name="Book28", type=comicBooks_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="writers", type=comicBooks_Book, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="comicBooks",
    types={comicBooks_ComicBookCollection, comicBooks_Book, comicBooks_Editor, comicBooks_Writer, comicBooks_Publisher, comicBooks_Artist, comicBooks_Series},
    associations={books0, editors3, writers5, artists1, series9, booksPublished11, publishingCompanies7, artists14, booksInSeries12, writers16, coverArtist17, publisher19, editors15, booksArtistFor21, booksCoverArtistFor23, seriesPartOf20, booksEditorFor25, booksWriterFor27},
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