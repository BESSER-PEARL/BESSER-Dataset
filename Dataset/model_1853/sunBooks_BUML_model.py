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
BookCategoryType: Enumeration = Enumeration(
    name="BookCategoryType",
    literals={
            EnumerationLiteral(name="magazine"),
			EnumerationLiteral(name="novel"),
			EnumerationLiteral(name="fiction"),
			EnumerationLiteral(name="other")
    }
)

BookCategoryType1: Enumeration = Enumeration(
    name="BookCategoryType1",
    literals={
            EnumerationLiteral(name="magazine"),
			EnumerationLiteral(name="novel"),
			EnumerationLiteral(name="fiction"),
			EnumerationLiteral(name="other")
    }
)

# Classes
sunBooks_AuthorsType = Class(name="sunBooks::AuthorsType")
sunBooks_BooksType = Class(name="sunBooks::BooksType")
sunBooks_BookType = Class(name="sunBooks::BookType")
sunBooks_PromotionType = Class(name="sunBooks::PromotionType")
sunBooks_CollectionType = Class(name="sunBooks::CollectionType")
sunBooks_DocumentRoot = Class(name="sunBooks::DocumentRoot")
sunBooks_EStringToStringMapEntry = Class(name="sunBooks::EStringToStringMapEntry")

# sunBooks_AuthorsType class attributes and methods
sunBooks_AuthorsType_authorName: Property = Property(name="authorName", type=StringType)
sunBooks_AuthorsType.attributes={sunBooks_AuthorsType_authorName}

# sunBooks_BooksType class attributes and methods

# sunBooks_BookType class attributes and methods
sunBooks_BookType_description: Property = Property(name="description", type=StringType)
sunBooks_BookType_name: Property = Property(name="name", type=StringType)
sunBooks_BookType_iSBN: Property = Property(name="iSBN", type=StringType)
sunBooks_BookType_price: Property = Property(name="price", type=StringType)
sunBooks_BookType_publicationDate: Property = Property(name="publicationDate", type=StringType)
sunBooks_BookType_bookCategory: Property = Property(name="bookCategory", type=StringType)
sunBooks_BookType_itemId: Property = Property(name="itemId", type=StringType)
sunBooks_BookType.attributes={sunBooks_BookType_iSBN, sunBooks_BookType_description, sunBooks_BookType_bookCategory, sunBooks_BookType_publicationDate, sunBooks_BookType_name, sunBooks_BookType_price, sunBooks_BookType_itemId}

# sunBooks_PromotionType class attributes and methods
sunBooks_PromotionType_discount: Property = Property(name="discount", type=StringType)
sunBooks_PromotionType_none: Property = Property(name="none", type=StringType)
sunBooks_PromotionType.attributes={sunBooks_PromotionType_none, sunBooks_PromotionType_discount}

# sunBooks_CollectionType class attributes and methods

# sunBooks_DocumentRoot class attributes and methods
sunBooks_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
sunBooks_DocumentRoot.attributes={sunBooks_DocumentRoot_mixed}

# sunBooks_EStringToStringMapEntry class attributes and methods

# Relationships
book0: BinaryAssociation = BinaryAssociation(
    name="book0",
    ends={
        Property(name="sunBooks_BookType", type=sunBooks_BooksType, multiplicity=Multiplicity(1, 1)),
        Property(name="sunBooks_BooksType", type=sunBooks_BookType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
authors1: BinaryAssociation = BinaryAssociation(
    name="authors1",
    ends={
        Property(name="sunBooks_AuthorsType", type=sunBooks_BookType, multiplicity=Multiplicity(1, 1)),
        Property(name="sunBooks_BookType2", type=sunBooks_AuthorsType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
promotion3: BinaryAssociation = BinaryAssociation(
    name="promotion3",
    ends={
        Property(name="sunBooks_PromotionType", type=sunBooks_BookType, multiplicity=Multiplicity(1, 1)),
        Property(name="sunBooks_BookType4", type=sunBooks_PromotionType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
books5: BinaryAssociation = BinaryAssociation(
    name="books5",
    ends={
        Property(name="sunBooks_BooksType6", type=sunBooks_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="sunBooks_CollectionType", type=sunBooks_BooksType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
xMLNSPrefixMap7: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap7",
    ends={
        Property(name="sunBooks_EStringToStringMapEntry", type=sunBooks_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="sunBooks_DocumentRoot", type=sunBooks_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation8: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation8",
    ends={
        Property(name="sunBooks_EStringToStringMapEntry10", type=sunBooks_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="sunBooks_DocumentRoot9", type=sunBooks_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
collection11: BinaryAssociation = BinaryAssociation(
    name="collection11",
    ends={
        Property(name="sunBooks_CollectionType13", type=sunBooks_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="sunBooks_DocumentRoot12", type=sunBooks_CollectionType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="sunBooks",
    types={sunBooks_AuthorsType, sunBooks_BooksType, sunBooks_BookType, sunBooks_PromotionType, sunBooks_CollectionType, sunBooks_DocumentRoot, sunBooks_EStringToStringMapEntry, BookCategoryType, BookCategoryType1},
    associations={book0, authors1, promotion3, books5, xMLNSPrefixMap7, xSISchemaLocation8, collection11},
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