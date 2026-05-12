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
document = Class(name="document")
album = Class(name="album")
song = Class(name="song")
person = Class(name="person")
orgnazition = Class(name="orgnazition")
author = Class(name="author")
publishments = Class(name="publishments")
publisher = Class(name="publisher")
conference_paper = Class(name="conference_paper")
journal_article = Class(name="journal_article")
book = Class(name="book")
book_chapters = Class(name="book_chapters")

# document class attributes and methods

# album class attributes and methods
album_title: Property = Property(name="title", type=StringType)
album_publishDate: Property = Property(name="publishDate", type=StringType)
album_cover: Property = Property(name="cover", type=StringType)
album_albumID: Property = Property(name="albumID", type=StringType)
album_duration: Property = Property(name="duration", type=StringType)
album_publisher: Property = Property(name="publisher", type=orgnazition)
album_price: Property = Property(name="price", type=StringType)
album_genre: Property = Property(name="genre", type=StringType)
album_artists: Property = Property(name="artists", type=person)
album_rightsReserve: Property = Property(name="rightsReserve", type=orgnazition)
album.attributes={album_price, album_genre, album_artists, album_publishDate, album_albumID, album_title, album_publisher, album_rightsReserve, album_duration, album_cover}

# song class attributes and methods
song_title: Property = Property(name="title", type=StringType)
song_duration: Property = Property(name="duration", type=StringType)
song_belongsTo: Property = Property(name="belongsTo", type=album)
song_year: Property = Property(name="year", type=IntegerType)
song_cover: Property = Property(name="cover", type=StringType)
song_artistLyrics: Property = Property(name="artistLyrics", type=person)
song_price: Property = Property(name="price", type=StringType)
song_genre: Property = Property(name="genre", type=StringType)
song_artistCompose: Property = Property(name="artistCompose", type=person)
song_artistVocal: Property = Property(name="artistVocal", type=person)
song_rightsReserve: Property = Property(name="rightsReserve", type=orgnazition)
song_trackID: Property = Property(name="trackID", type=IntegerType)
song_songID: Property = Property(name="songID", type=StringType)
song_artistPerform: Property = Property(name="artistPerform", type=person)
song.attributes={song_artistCompose, song_artistVocal, song_artistPerform, song_artistLyrics, song_title, song_duration, song_belongsTo, song_trackID, song_genre, song_rightsReserve, song_songID, song_cover, song_price, song_year}

# person class attributes and methods
person_name: Property = Property(name="name", type=StringType)
person_birthday: Property = Property(name="birthday", type=StringType)
person_portrait: Property = Property(name="portrait", type=StringType)
person_gender: Property = Property(name="gender", type=BooleanType)
person_personID: Property = Property(name="personID", type=StringType)
person_belongsTo: Property = Property(name="belongsTo", type=orgnazition)
person.attributes={person_birthday, person_name, person_personID, person_belongsTo, person_portrait, person_gender}

# orgnazition class attributes and methods
orgnazition_name: Property = Property(name="name", type=StringType)
orgnazition_establishedDate: Property = Property(name="establishedDate", type=StringType)
orgnazition_icon: Property = Property(name="icon", type=StringType)
orgnazition_orgID: Property = Property(name="orgID", type=StringType)
orgnazition_president: Property = Property(name="president", type=person)
orgnazition.attributes={orgnazition_name, orgnazition_orgID, orgnazition_establishedDate, orgnazition_president, orgnazition_icon}

# author class attributes and methods
author_GivenName: Property = Property(name="GivenName", type=StringType)
author_FamilyName: Property = Property(name="FamilyName", type=StringType)
author_Mail: Property = Property(name="Mail", type=StringType)
author_Phone: Property = Property(name="Phone", type=StringType)
author_Address: Property = Property(name="Address", type=StringType)
author.attributes={author_Address, author_FamilyName, author_GivenName, author_Mail, author_Phone}

# publishments class attributes and methods
publishments_Title: Property = Property(name="Title", type=StringType)
publishments_Publisher: Property = Property(name="Publisher", type=publisher)
publishments_AuthoredBy: Property = Property(name="AuthoredBy", type=author)
publishments_Year: Property = Property(name="Year", type=IntegerType)
publishments.attributes={publishments_Title, publishments_AuthoredBy, publishments_Publisher, publishments_Year}

# publisher class attributes and methods
publisher_OrgName: Property = Property(name="OrgName", type=StringType)
publisher_EstablishedYear: Property = Property(name="EstablishedYear", type=IntegerType)
publisher_OrgContact: Property = Property(name="OrgContact", type=StringType)
publisher_OrgAddress: Property = Property(name="OrgAddress", type=StringType)
publisher.attributes={publisher_OrgContact, publisher_OrgAddress, publisher_EstablishedYear, publisher_OrgName}

# conference_paper class attributes and methods
conference_paper_Title: Property = Property(name="Title", type=StringType)
conference_paper_AuthoredBy: Property = Property(name="AuthoredBy", type=author)
conference_paper_Year: Property = Property(name="Year", type=IntegerType)
conference_paper_Publisher: Property = Property(name="Publisher", type=publisher)
conference_paper_ConferenceName: Property = Property(name="ConferenceName", type=StringType)
conference_paper_Location: Property = Property(name="Location", type=StringType)
conference_paper.attributes={conference_paper_Title, conference_paper_Publisher, conference_paper_Year, conference_paper_Location, conference_paper_AuthoredBy, conference_paper_ConferenceName}

# journal_article class attributes and methods
journal_article_Title: Property = Property(name="Title", type=StringType)
journal_article_Year: Property = Property(name="Year", type=IntegerType)
journal_article_Publisher: Property = Property(name="Publisher", type=publisher)
journal_article_JournalName: Property = Property(name="JournalName", type=StringType)
journal_article_AuthoredBy: Property = Property(name="AuthoredBy", type=author)
journal_article_Volume: Property = Property(name="Volume", type=IntegerType)
journal_article_Pages: Property = Property(name="Pages", type=IntegerType)
journal_article.attributes={journal_article_Publisher, journal_article_AuthoredBy, journal_article_Pages, journal_article_Title, journal_article_JournalName, journal_article_Year, journal_article_Volume}

# book class attributes and methods
book_Title: Property = Property(name="Title", type=StringType)
book_AuthoredBy: Property = Property(name="AuthoredBy", type=author)
book_Year: Property = Property(name="Year", type=IntegerType)
book_Publisher: Property = Property(name="Publisher", type=publisher)
book_Region: Property = Property(name="Region", type=StringType)
book_Price: Property = Property(name="Price", type=FloatType)
book_RefTo: Property = Property(name="RefTo", type=publishments)
book.attributes={book_Price, book_RefTo, book_Title, book_Publisher, book_AuthoredBy, book_Year, book_Region}

# book_chapters class attributes and methods

# Relationships
conference_paper_publishments: BinaryAssociation = BinaryAssociation(
    name="conference_paper_publishments",
    ends={
        Property(name="publishments0", type=publishments, multiplicity=Multiplicity(0, 1)),
        Property(name="conference_paper1", type=conference_paper, multiplicity=Multiplicity(0, 1))
    }
)
publishments_book: BinaryAssociation = BinaryAssociation(
    name="publishments_book",
    ends={
        Property(name="book2", type=book, multiplicity=Multiplicity(0, 1)),
        Property(name="publishments3", type=publishments, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_GI0DkPa8EemEXt2Xl4w_3Q",
    types={document, album, song, person, orgnazition, author, publishments, publisher, conference_paper, journal_article, book, book_chapters},
    associations={conference_paper_publishments, publishments_book},
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