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
GenreTypes: Enumeration = Enumeration(
    name="GenreTypes",
    literals={
            EnumerationLiteral(name="Comedy"),
			EnumerationLiteral(name="Documentary"),
			EnumerationLiteral(name="Drama"),
			EnumerationLiteral(name="Horror"),
			EnumerationLiteral(name="Romance"),
			EnumerationLiteral(name="SciFi"),
			EnumerationLiteral(name="Thriller"),
			EnumerationLiteral(name="NewRelease"),
			EnumerationLiteral(name="Action"),
			EnumerationLiteral(name="Animation"),
			EnumerationLiteral(name="Family"),
			EnumerationLiteral(name="Classics")
    }
)

# Classes
movies_Movie = Class(name="movies::Movie")
movies_Copy = Class(name="movies::Copy")
movies_CriticsReview = Class(name="movies::CriticsReview")
movies_CustomerReview = Class(name="movies::CustomerReview")
CriticsReview = Class(name="CriticsReview")
movies_MoviesDB = Class(name="movies::MoviesDB")
movies_Place = Class(name="movies::Place")

# movies_Movie class attributes and methods
movies_Movie_actors: Property = Property(name="actors", type=StringType)
movies_Movie_title: Property = Property(name="title", type=StringType)
movies_Movie_director: Property = Property(name="director", type=StringType)
movies_Movie_genre: Property = Property(name="genre", type=StringType)
movies_Movie_summary: Property = Property(name="summary", type=StringType)
movies_Movie.attributes={movies_Movie_actors, movies_Movie_summary, movies_Movie_genre, movies_Movie_title, movies_Movie_director}

# movies_Copy class attributes and methods
movies_Copy_id: Property = Property(name="id", type=StringType)
movies_Copy.attributes={movies_Copy_id}

# movies_CriticsReview class attributes and methods
movies_CriticsReview_rating: Property = Property(name="rating", type=StringType)
movies_CriticsReview_reviewedBy: Property = Property(name="reviewedBy", type=StringType)
movies_CriticsReview.attributes={movies_CriticsReview_reviewedBy, movies_CriticsReview_rating}

# movies_CustomerReview class attributes and methods
movies_CustomerReview_comment: Property = Property(name="comment", type=StringType)
movies_CustomerReview.attributes={movies_CustomerReview_comment}

# CriticsReview class attributes and methods

# movies_MoviesDB class attributes and methods
movies_MoviesDB_comment: Property = Property(name="comment", type=StringType)
movies_MoviesDB.attributes={movies_MoviesDB_comment}

# movies_Place class attributes and methods
movies_Place_id: Property = Property(name="id", type=StringType)
movies_Place_name: Property = Property(name="name", type=StringType)
movies_Place.attributes={movies_Place_id, movies_Place_name}

# Relationships
copies0: BinaryAssociation = BinaryAssociation(
    name="copies0",
    ends={
        Property(name="movies_Copy", type=movies_Movie, multiplicity=Multiplicity(1, 1)),
        Property(name="movies_Movie", type=movies_Copy, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
review1: BinaryAssociation = BinaryAssociation(
    name="review1",
    ends={
        Property(name="movies_CriticsReview", type=movies_Movie, multiplicity=Multiplicity(1, 1)),
        Property(name="movies_Movie2", type=movies_CriticsReview, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
place7: BinaryAssociation = BinaryAssociation(
    name="place7",
    ends={
        Property(name="movies_Place9", type=movies_Copy, multiplicity=Multiplicity(1, 1)),
        Property(name="movies_Copy8", type=movies_Place, multiplicity=Multiplicity(0, 1))
    }
)
movies3: BinaryAssociation = BinaryAssociation(
    name="movies3",
    ends={
        Property(name="movies_Movie4", type=movies_MoviesDB, multiplicity=Multiplicity(1, 1)),
        Property(name="movies_MoviesDB", type=movies_Movie, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
places5: BinaryAssociation = BinaryAssociation(
    name="places5",
    ends={
        Property(name="movies_Place", type=movies_MoviesDB, multiplicity=Multiplicity(1, 1)),
        Property(name="movies_MoviesDB6", type=movies_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_movies_CustomerReview_CriticsReview = Generalization(general=CriticsReview, specific=movies_CustomerReview)

# Domain Model
domain_model = DomainModel(
    name="movies",
    types={movies_Movie, movies_Copy, movies_CriticsReview, movies_CustomerReview, CriticsReview, movies_MoviesDB, movies_Place, GenreTypes},
    associations={copies0, review1, place7, movies3, places5},
    generalizations={gen_movies_CustomerReview_CriticsReview},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)