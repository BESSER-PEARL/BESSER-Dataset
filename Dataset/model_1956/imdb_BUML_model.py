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
Genre: Enumeration = Enumeration(
    name="Genre",
    literals={
            EnumerationLiteral(name="Adventure"),
			EnumerationLiteral(name="SciFi")
    }
)

StaffListType: Enumeration = Enumeration(
    name="StaffListType",
    literals={
            EnumerationLiteral(name="titles"),
			EnumerationLiteral(name="characters")
    }
)

# Classes
imdb_db = Class(name="imdb::db")
imdb_Person = Class(name="imdb::Person")
imdb_Movie = Class(name="imdb::Movie")
imdb_StaffList = Class(name="imdb::StaffList")
imdb_User = Class(name="imdb::User")

# imdb_db class attributes and methods
imdb_db_bestOf2014: Property = Property(name="bestOf2014", type=StringType)
imdb_db_m_sam: Method = Method(name="sam", parameters={}, type=StringType)
imdb_db.attributes={imdb_db_bestOf2014}
imdb_db.methods={imdb_db_m_sam}

# imdb_Person class attributes and methods
imdb_Person_name: Property = Property(name="name", type=StringType)
imdb_Person.attributes={imdb_Person_name}

# imdb_Movie class attributes and methods
imdb_Movie_age: Property = Property(name="age", type=IntegerType)
imdb_Movie_title: Property = Property(name="title", type=StringType)
imdb_Movie_releaseDate: Property = Property(name="releaseDate", type=DateType)
imdb_Movie_runtime: Property = Property(name="runtime", type=IntegerType)
imdb_Movie_poster: Property = Property(name="poster", type=StringType)
imdb_Movie_rating: Property = Property(name="rating", type=FloatType)
imdb_Movie_userReviews: Property = Property(name="userReviews", type=IntegerType)
imdb_Movie_criticReviews: Property = Property(name="criticReviews", type=IntegerType)
imdb_Movie_userRatings: Property = Property(name="userRatings", type=IntegerType)
imdb_Movie_synopsis: Property = Property(name="synopsis", type=StringType)
imdb_Movie_metaScore: Property = Property(name="metaScore", type=IntegerType)
imdb_Movie_metacriticReviews: Property = Property(name="metacriticReviews", type=IntegerType)
imdb_Movie_genres: Property = Property(name="genres", type=StringType)
imdb_Movie.attributes={imdb_Movie_runtime, imdb_Movie_releaseDate, imdb_Movie_title, imdb_Movie_criticReviews, imdb_Movie_userRatings, imdb_Movie_rating, imdb_Movie_userReviews, imdb_Movie_genres, imdb_Movie_age, imdb_Movie_synopsis, imdb_Movie_metaScore, imdb_Movie_poster, imdb_Movie_metacriticReviews}

# imdb_StaffList class attributes and methods
imdb_StaffList_coverPhoto: Property = Property(name="coverPhoto", type=StringType)
imdb_StaffList_name: Property = Property(name="name", type=StringType)
imdb_StaffList_elements: Property = Property(name="elements", type=StringType)
imdb_StaffList_elementType: Property = Property(name="elementType", type=StringType)
imdb_StaffList_createdDate: Property = Property(name="createdDate", type=DateType)
imdb_StaffList.attributes={imdb_StaffList_elementType, imdb_StaffList_coverPhoto, imdb_StaffList_elements, imdb_StaffList_name, imdb_StaffList_createdDate}

# imdb_User class attributes and methods
imdb_User_username: Property = Property(name="username", type=StringType)
imdb_User_watchlist: Property = Property(name="watchlist", type=StringType)
imdb_User.attributes={imdb_User_username, imdb_User_watchlist}

# Relationships
allDirectors7: BinaryAssociation = BinaryAssociation(
    name="allDirectors7",
    ends={
        Property(name="imdb_Person8", type=imdb_db, multiplicity=Multiplicity(1, 1)),
        Property(name="imdb_db", type=imdb_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allWriters9: BinaryAssociation = BinaryAssociation(
    name="allWriters9",
    ends={
        Property(name="imdb_Person11", type=imdb_db, multiplicity=Multiplicity(1, 1)),
        Property(name="imdb_db10", type=imdb_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allActors12: BinaryAssociation = BinaryAssociation(
    name="allActors12",
    ends={
        Property(name="imdb_Person14", type=imdb_db, multiplicity=Multiplicity(1, 1)),
        Property(name="imdb_db13", type=imdb_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allMovies15: BinaryAssociation = BinaryAssociation(
    name="allMovies15",
    ends={
        Property(name="imdb_Movie17", type=imdb_db, multiplicity=Multiplicity(1, 1)),
        Property(name="imdb_db16", type=imdb_Movie, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
director0: BinaryAssociation = BinaryAssociation(
    name="director0",
    ends={
        Property(name="imdb_Person", type=imdb_Movie, multiplicity=Multiplicity(1, 1)),
        Property(name="imdb_Movie", type=imdb_Person, multiplicity=Multiplicity(0, 1))
    }
)
writers1: BinaryAssociation = BinaryAssociation(
    name="writers1",
    ends={
        Property(name="imdb_Person3", type=imdb_Movie, multiplicity=Multiplicity(1, 1)),
        Property(name="imdb_Movie2", type=imdb_Person, multiplicity=Multiplicity(0, 9999))
    }
)
actors4: BinaryAssociation = BinaryAssociation(
    name="actors4",
    ends={
        Property(name="imdb_Person6", type=imdb_Movie, multiplicity=Multiplicity(1, 1)),
        Property(name="imdb_Movie5", type=imdb_Person, multiplicity=Multiplicity(0, 9999))
    }
)
allStaffLists18: BinaryAssociation = BinaryAssociation(
    name="allStaffLists18",
    ends={
        Property(name="imdb_StaffList", type=imdb_db, multiplicity=Multiplicity(1, 1)),
        Property(name="imdb_db19", type=imdb_StaffList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
allUsers20: BinaryAssociation = BinaryAssociation(
    name="allUsers20",
    ends={
        Property(name="imdb_User", type=imdb_db, multiplicity=Multiplicity(1, 1)),
        Property(name="imdb_db21", type=imdb_User, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
user22: BinaryAssociation = BinaryAssociation(
    name="user22",
    ends={
        Property(name="imdb_User24", type=imdb_StaffList, multiplicity=Multiplicity(1, 1)),
        Property(name="imdb_StaffList23", type=imdb_User, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="imdb",
    types={imdb_db, imdb_Person, imdb_Movie, imdb_StaffList, imdb_User, Genre, StaffListType},
    associations={allDirectors7, allWriters9, allActors12, allMovies15, director0, writers1, actors4, allStaffLists18, allUsers20, user22},
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