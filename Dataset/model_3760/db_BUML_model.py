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
            EnumerationLiteral(name="NewRelease"),
			EnumerationLiteral(name="Action"),
			EnumerationLiteral(name="Animation"),
			EnumerationLiteral(name="Family"),
			EnumerationLiteral(name="Classics"),
			EnumerationLiteral(name="Comedy"),
			EnumerationLiteral(name="Documentary"),
			EnumerationLiteral(name="Drama"),
			EnumerationLiteral(name="Horror"),
			EnumerationLiteral(name="Romance"),
			EnumerationLiteral(name="SciFi"),
			EnumerationLiteral(name="Thriller")
    }
)

# Classes
db_CriticsReviewType = Class(name="db::CriticsReviewType")
db_CustomerReviewType = Class(name="db::CustomerReviewType")
CriticsReviewType = Class(name="CriticsReviewType")
db_DocumentRoot = Class(name="db::DocumentRoot")
db_EStringToStringMapEntry = Class(name="db::EStringToStringMapEntry")
db_CustomerType = Class(name="db::CustomerType")
db_MovieDBType = Class(name="db::MovieDBType")
db_MovieType = Class(name="db::MovieType")

# db_CriticsReviewType class attributes and methods
db_CriticsReviewType_rating: Property = Property(name="rating", type=StringType)
db_CriticsReviewType_reviewedBy: Property = Property(name="reviewedBy", type=StringType)
db_CriticsReviewType.attributes={db_CriticsReviewType_rating, db_CriticsReviewType_reviewedBy}

# db_CustomerReviewType class attributes and methods
db_CustomerReviewType_comment: Property = Property(name="comment", type=StringType)
db_CustomerReviewType.attributes={db_CustomerReviewType_comment}

# CriticsReviewType class attributes and methods

# db_DocumentRoot class attributes and methods
db_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
db_DocumentRoot_language: Property = Property(name="language", type=StringType)
db_DocumentRoot_specialFeatures: Property = Property(name="specialFeatures", type=StringType)
db_DocumentRoot.attributes={db_DocumentRoot_specialFeatures, db_DocumentRoot_language, db_DocumentRoot_mixed}

# db_EStringToStringMapEntry class attributes and methods

# db_CustomerType class attributes and methods

# db_MovieDBType class attributes and methods
db_MovieDBType_movieDBFeatureMap: Property = Property(name="movieDBFeatureMap", type=StringType)
db_MovieDBType_comment: Property = Property(name="comment", type=StringType)
db_MovieDBType.attributes={db_MovieDBType_comment, db_MovieDBType_movieDBFeatureMap}

# db_MovieType class attributes and methods
db_MovieType_title: Property = Property(name="title", type=StringType)
db_MovieType_actors: Property = Property(name="actors", type=StringType)
db_MovieType_director: Property = Property(name="director", type=StringType)
db_MovieType_genre: Property = Property(name="genre", type=StringType)
db_MovieType_summary: Property = Property(name="summary", type=StringType)
db_MovieType_criticsReviewGroup: Property = Property(name="criticsReviewGroup", type=StringType)
db_MovieType_any: Property = Property(name="any", type=StringType)
db_MovieType_iD: Property = Property(name="iD", type=StringType)
db_MovieType.attributes={db_MovieType_director, db_MovieType_summary, db_MovieType_title, db_MovieType_any, db_MovieType_criticsReviewGroup, db_MovieType_actors, db_MovieType_iD, db_MovieType_genre}

# Relationships
xMLNSPrefixMap0: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap0",
    ends={
        Property(name="db_EStringToStringMapEntry", type=db_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="db_DocumentRoot", type=db_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation1: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation1",
    ends={
        Property(name="db_EStringToStringMapEntry3", type=db_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="db_DocumentRoot2", type=db_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
checkedOutBy4: BinaryAssociation = BinaryAssociation(
    name="checkedOutBy4",
    ends={
        Property(name="db_CustomerType", type=db_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="db_DocumentRoot5", type=db_CustomerType, multiplicity=Multiplicity(0, 9999))
    }
)
customerReview8: BinaryAssociation = BinaryAssociation(
    name="customerReview8",
    ends={
        Property(name="db_CustomerReviewType", type=db_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="db_DocumentRoot9", type=db_CustomerReviewType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
movieDB10: BinaryAssociation = BinaryAssociation(
    name="movieDB10",
    ends={
        Property(name="db_MovieDBType", type=db_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="db_DocumentRoot11", type=db_MovieDBType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
criticsReview6: BinaryAssociation = BinaryAssociation(
    name="criticsReview6",
    ends={
        Property(name="db_CriticsReviewType", type=db_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="db_DocumentRoot7", type=db_CriticsReviewType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
movie12: BinaryAssociation = BinaryAssociation(
    name="movie12",
    ends={
        Property(name="db_MovieType", type=db_MovieDBType, multiplicity=Multiplicity(1, 1)),
        Property(name="db_MovieDBType13", type=db_MovieType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
checkedOutBy17: BinaryAssociation = BinaryAssociation(
    name="checkedOutBy17",
    ends={
        Property(name="db_CustomerType19", type=db_MovieType, multiplicity=Multiplicity(1, 1)),
        Property(name="db_MovieType18", type=db_CustomerType, multiplicity=Multiplicity(1, 1))
    }
)
criticsReview14: BinaryAssociation = BinaryAssociation(
    name="criticsReview14",
    ends={
        Property(name="db_CriticsReviewType16", type=db_MovieType, multiplicity=Multiplicity(1, 1)),
        Property(name="db_MovieType15", type=db_CriticsReviewType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_db_CustomerReviewType_CriticsReviewType = Generalization(general=CriticsReviewType, specific=db_CustomerReviewType)

# Domain Model
domain_model = DomainModel(
    name="db",
    types={db_CriticsReviewType, db_CustomerReviewType, CriticsReviewType, db_DocumentRoot, db_EStringToStringMapEntry, db_CustomerType, db_MovieDBType, db_MovieType, GenreTypes},
    associations={xMLNSPrefixMap0, xSISchemaLocation1, checkedOutBy4, customerReview8, movieDB10, criticsReview6, movie12, checkedOutBy17, criticsReview14},
    generalizations={gen_db_CustomerReviewType_CriticsReviewType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)