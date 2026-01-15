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
comicBookCollection2_ComicBookCollection = Class(name="comicBookCollection2::ComicBookCollection")
comicBookCollection2_Editor = Class(name="comicBookCollection2::Editor")
comicBookCollection2_Writer = Class(name="comicBookCollection2::Writer")
comicBookCollection2_Publisher = Class(name="comicBookCollection2::Publisher")
comicBookCollection2_Series = Class(name="comicBookCollection2::Series")
comicBookCollection2_Book = Class(name="comicBookCollection2::Book")
comicBookCollection2_Artist = Class(name="comicBookCollection2::Artist")

# comicBookCollection2_ComicBookCollection class attributes and methods

# comicBookCollection2_Editor class attributes and methods
comicBookCollection2_Editor_name: Property = Property(name="name", type=StringType)
comicBookCollection2_Editor.attributes={comicBookCollection2_Editor_name}

# comicBookCollection2_Writer class attributes and methods
comicBookCollection2_Writer_name: Property = Property(name="name", type=StringType)
comicBookCollection2_Writer.attributes={comicBookCollection2_Writer_name}

# comicBookCollection2_Publisher class attributes and methods
comicBookCollection2_Publisher_publishersName: Property = Property(name="publishersName", type=StringType)
comicBookCollection2_Publisher.attributes={comicBookCollection2_Publisher_publishersName}

# comicBookCollection2_Series class attributes and methods
comicBookCollection2_Series_seriesName: Property = Property(name="seriesName", type=StringType)
comicBookCollection2_Series.attributes={comicBookCollection2_Series_seriesName}

# comicBookCollection2_Book class attributes and methods
comicBookCollection2_Book_name: Property = Property(name="name", type=StringType)
comicBookCollection2_Book_publicationDate: Property = Property(name="publicationDate", type=StringType)
comicBookCollection2_Book.attributes={comicBookCollection2_Book_publicationDate, comicBookCollection2_Book_name}

# comicBookCollection2_Artist class attributes and methods
comicBookCollection2_Artist_name: Property = Property(name="name", type=StringType)
comicBookCollection2_Artist.attributes={comicBookCollection2_Artist_name}

# Relationships
editors3: BinaryAssociation = BinaryAssociation(
    name="editors3",
    ends={
        Property(name="comicBookCollection2_Editor", type=comicBookCollection2_ComicBookCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="comicBookCollection2_ComicBookCollection4", type=comicBookCollection2_Editor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writers5: BinaryAssociation = BinaryAssociation(
    name="writers5",
    ends={
        Property(name="comicBookCollection2_Writer", type=comicBookCollection2_ComicBookCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="comicBookCollection2_ComicBookCollection6", type=comicBookCollection2_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
publishingCompanies7: BinaryAssociation = BinaryAssociation(
    name="publishingCompanies7",
    ends={
        Property(name="comicBookCollection2_Publisher", type=comicBookCollection2_ComicBookCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="comicBookCollection2_ComicBookCollection8", type=comicBookCollection2_Publisher, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
series9: BinaryAssociation = BinaryAssociation(
    name="series9",
    ends={
        Property(name="comicBookCollection2_Series", type=comicBookCollection2_ComicBookCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="comicBookCollection2_ComicBookCollection10", type=comicBookCollection2_Series, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
booksPublished11: BinaryAssociation = BinaryAssociation(
    name="booksPublished11",
    ends={
        Property(name="Book", type=comicBookCollection2_Publisher, multiplicity=Multiplicity(1, 1)),
        Property(name="publisher", type=comicBookCollection2_Book, multiplicity=Multiplicity(0, 9999))
    }
)
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="comicBookCollection2_Book", type=comicBookCollection2_ComicBookCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="comicBookCollection2_ComicBookCollection", type=comicBookCollection2_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artists1: BinaryAssociation = BinaryAssociation(
    name="artists1",
    ends={
        Property(name="comicBookCollection2_Artist", type=comicBookCollection2_ComicBookCollection, multiplicity=Multiplicity(1, 1)),
        Property(name="comicBookCollection2_ComicBookCollection2", type=comicBookCollection2_Artist, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
artists14: BinaryAssociation = BinaryAssociation(
    name="artists14",
    ends={
        Property(name="Artist", type=comicBookCollection2_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="booksArtistFor", type=comicBookCollection2_Artist, multiplicity=Multiplicity(1, 9999))
    }
)
editors15: BinaryAssociation = BinaryAssociation(
    name="editors15",
    ends={
        Property(name="Editor", type=comicBookCollection2_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="booksEditorFor", type=comicBookCollection2_Editor, multiplicity=Multiplicity(1, 9999))
    }
)
writers16: BinaryAssociation = BinaryAssociation(
    name="writers16",
    ends={
        Property(name="Writer", type=comicBookCollection2_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="booksWriterFor", type=comicBookCollection2_Writer, multiplicity=Multiplicity(1, 9999))
    }
)
coverArtist17: BinaryAssociation = BinaryAssociation(
    name="coverArtist17",
    ends={
        Property(name="Artist18", type=comicBookCollection2_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="booksCoverArtistFor", type=comicBookCollection2_Artist, multiplicity=Multiplicity(1, 1))
    }
)
publisher19: BinaryAssociation = BinaryAssociation(
    name="publisher19",
    ends={
        Property(name="Publisher", type=comicBookCollection2_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="booksPublished", type=comicBookCollection2_Publisher, multiplicity=Multiplicity(1, 1))
    }
)
seriesPartOf20: BinaryAssociation = BinaryAssociation(
    name="seriesPartOf20",
    ends={
        Property(name="Series", type=comicBookCollection2_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="booksInSeries", type=comicBookCollection2_Series, multiplicity=Multiplicity(1, 1))
    }
)
booksInSeries12: BinaryAssociation = BinaryAssociation(
    name="booksInSeries12",
    ends={
        Property(name="Book13", type=comicBookCollection2_Series, multiplicity=Multiplicity(1, 1)),
        Property(name="seriesPartOf", type=comicBookCollection2_Book, multiplicity=Multiplicity(0, 9999))
    }
)
booksEditorFor25: BinaryAssociation = BinaryAssociation(
    name="booksEditorFor25",
    ends={
        Property(name="Book26", type=comicBookCollection2_Editor, multiplicity=Multiplicity(1, 1)),
        Property(name="editors", type=comicBookCollection2_Book, multiplicity=Multiplicity(0, 9999))
    }
)
booksWriterFor27: BinaryAssociation = BinaryAssociation(
    name="booksWriterFor27",
    ends={
        Property(name="Book28", type=comicBookCollection2_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="writers", type=comicBookCollection2_Book, multiplicity=Multiplicity(0, 9999))
    }
)
booksArtistFor21: BinaryAssociation = BinaryAssociation(
    name="booksArtistFor21",
    ends={
        Property(name="Book22", type=comicBookCollection2_Artist, multiplicity=Multiplicity(1, 1)),
        Property(name="artists", type=comicBookCollection2_Book, multiplicity=Multiplicity(0, 9999))
    }
)
booksCoverArtistFor23: BinaryAssociation = BinaryAssociation(
    name="booksCoverArtistFor23",
    ends={
        Property(name="Book24", type=comicBookCollection2_Artist, multiplicity=Multiplicity(1, 1)),
        Property(name="coverArtist", type=comicBookCollection2_Book, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="comicBookCollection2",
    types={comicBookCollection2_ComicBookCollection, comicBookCollection2_Editor, comicBookCollection2_Writer, comicBookCollection2_Publisher, comicBookCollection2_Series, comicBookCollection2_Book, comicBookCollection2_Artist},
    associations={editors3, writers5, publishingCompanies7, series9, booksPublished11, books0, artists1, artists14, editors15, writers16, coverArtist17, publisher19, seriesPartOf20, booksInSeries12, booksEditorFor25, booksWriterFor27, booksArtistFor21, booksCoverArtistFor23},
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