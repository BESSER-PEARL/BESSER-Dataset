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
model_Person = Class(name="model::Person")
model_Book = Class(name="model::Book")
model_PersonBNode = Class(name="model::PersonBNode")
model_BookBNode = Class(name="model::BookBNode")
model_BNode = Class(name="model::BNode")
model_Library = Class(name="model::Library")
model_Location = Class(name="model::Location")
model_ETypes = Class(name="model::ETypes")
model_MappedLibrary = Class(name="model::MappedLibrary")
model_TargetObject = Class(name="model::TargetObject")
model_PrimaryObject = Class(name="model::PrimaryObject")
model_Movie = Class(name="model::Movie")
model_Actor = Class(name="model::Actor")

# model_Person class attributes and methods
model_Person_name: Property = Property(name="name", type=StringType)
model_Person.attributes={model_Person_name}

# model_Book class attributes and methods
model_Book_title: Property = Property(name="title", type=StringType)
model_Book_tags: Property = Property(name="tags", type=StringType)
model_Book_data: Property = Property(name="data", type=StringType)
model_Book.attributes={model_Book_tags, model_Book_data, model_Book_title}

# model_PersonBNode class attributes and methods
model_PersonBNode_name: Property = Property(name="name", type=StringType)
model_PersonBNode.attributes={model_PersonBNode_name}

# model_BookBNode class attributes and methods
model_BookBNode_title: Property = Property(name="title", type=StringType)
model_BookBNode.attributes={model_BookBNode_title}

# model_BNode class attributes and methods
model_BNode_id: Property = Property(name="id", type=IntegerType)
model_BNode.attributes={model_BNode_id}

# model_Library class attributes and methods

# model_Location class attributes and methods
model_Location_address: Property = Property(name="address", type=StringType)
model_Location_id: Property = Property(name="id", type=StringType)
model_Location.attributes={model_Location_id, model_Location_address}

# model_ETypes class attributes and methods
model_ETypes_eChar: Property = Property(name="eChar", type=StringType)
model_ETypes_eDate: Property = Property(name="eDate", type=DateType)
model_ETypes_eBigDecimal: Property = Property(name="eBigDecimal", type=StringType)
model_ETypes_eBigInteger: Property = Property(name="eBigInteger", type=StringType)
model_ETypes_eBoolean: Property = Property(name="eBoolean", type=BooleanType)
model_ETypes_eByte: Property = Property(name="eByte", type=StringType)
model_ETypes_eByteArray: Property = Property(name="eByteArray", type=StringType)
model_ETypes_eDouble: Property = Property(name="eDouble", type=FloatType)
model_ETypes_eFloat: Property = Property(name="eFloat", type=FloatType)
model_ETypes_eInt: Property = Property(name="eInt", type=IntegerType)
model_ETypes_eLong: Property = Property(name="eLong", type=StringType)
model_ETypes_eShort: Property = Property(name="eShort", type=StringType)
model_ETypes_eString: Property = Property(name="eString", type=StringType)
model_ETypes_uris: Property = Property(name="uris", type=StringType)
model_ETypes.attributes={model_ETypes_eByteArray, model_ETypes_eBoolean, model_ETypes_eChar, model_ETypes_eBigInteger, model_ETypes_eFloat, model_ETypes_eInt, model_ETypes_uris, model_ETypes_eLong, model_ETypes_eDouble, model_ETypes_eString, model_ETypes_eShort, model_ETypes_eBigDecimal, model_ETypes_eByte, model_ETypes_eDate}

# model_MappedLibrary class attributes and methods
model_MappedLibrary_books: Property = Property(name="books", type=StringType)
model_MappedLibrary.attributes={model_MappedLibrary_books}

# model_TargetObject class attributes and methods
model_TargetObject_id: Property = Property(name="id", type=IntegerType)
model_TargetObject_singleAttribute: Property = Property(name="singleAttribute", type=StringType)
model_TargetObject_arrayAttribute: Property = Property(name="arrayAttribute", type=StringType)
model_TargetObject.attributes={model_TargetObject_arrayAttribute, model_TargetObject_singleAttribute, model_TargetObject_id}

# model_PrimaryObject class attributes and methods
model_PrimaryObject_id: Property = Property(name="id", type=IntegerType)
model_PrimaryObject_name: Property = Property(name="name", type=StringType)
model_PrimaryObject_unsettableAttribute: Property = Property(name="unsettableAttribute", type=StringType)
model_PrimaryObject_unsettableAttributeWithDefault: Property = Property(name="unsettableAttributeWithDefault", type=StringType)
model_PrimaryObject_featureMapReferenceCollection: Property = Property(name="featureMapReferenceCollection", type=StringType)
model_PrimaryObject_featureMapAttributeType1: Property = Property(name="featureMapAttributeType1", type=StringType)
model_PrimaryObject_featureMapAttributeType2: Property = Property(name="featureMapAttributeType2", type=StringType)
model_PrimaryObject_featureMapAttributeCollection: Property = Property(name="featureMapAttributeCollection", type=StringType)
model_PrimaryObject.attributes={model_PrimaryObject_name, model_PrimaryObject_featureMapAttributeCollection, model_PrimaryObject_featureMapReferenceCollection, model_PrimaryObject_featureMapAttributeType1, model_PrimaryObject_unsettableAttributeWithDefault, model_PrimaryObject_unsettableAttribute, model_PrimaryObject_featureMapAttributeType2, model_PrimaryObject_id}

# model_Movie class attributes and methods
model_Movie_id: Property = Property(name="id", type=IntegerType)
model_Movie_title: Property = Property(name="title", type=StringType)
model_Movie.attributes={model_Movie_id, model_Movie_title}

# model_Actor class attributes and methods
model_Actor_id: Property = Property(name="id", type=IntegerType)
model_Actor_name: Property = Property(name="name", type=StringType)
model_Actor.attributes={model_Actor_name, model_Actor_id}

# Relationships
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="Book", type=model_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=model_Book, multiplicity=Multiplicity(0, 9999))
    }
)
authors1: BinaryAssociation = BinaryAssociation(
    name="authors1",
    ends={
        Property(name="Person", type=model_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=model_Person, multiplicity=Multiplicity(0, 9999))
    }
)
books2: BinaryAssociation = BinaryAssociation(
    name="books2",
    ends={
        Property(name="model_BookBNode", type=model_PersonBNode, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PersonBNode", type=model_BookBNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
latestBook11: BinaryAssociation = BinaryAssociation(
    name="latestBook11",
    ends={
        Property(name="model_Book13", type=model_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Library12", type=model_Book, multiplicity=Multiplicity(0, 1))
    }
)
authors3: BinaryAssociation = BinaryAssociation(
    name="authors3",
    ends={
        Property(name="model_PersonBNode5", type=model_BookBNode, multiplicity=Multiplicity(1, 1)),
        Property(name="model_BookBNode4", type=model_PersonBNode, multiplicity=Multiplicity(0, 9999))
    }
)
child7: BinaryAssociation = BinaryAssociation(
    name="child7",
    ends={
        Property(name="model_BNode", type=model_BNode, multiplicity=Multiplicity(1, 1)),
        Property(name="model_BNode6", type=model_BNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books8: BinaryAssociation = BinaryAssociation(
    name="books8",
    ends={
        Property(name="model_Book", type=model_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Library", type=model_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
location9: BinaryAssociation = BinaryAssociation(
    name="location9",
    ends={
        Property(name="model_Location", type=model_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Library10", type=model_Location, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
featuredBook14: BinaryAssociation = BinaryAssociation(
    name="featuredBook14",
    ends={
        Property(name="model_Book16", type=model_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Location15", type=model_Book, multiplicity=Multiplicity(0, 1))
    }
)
location17: BinaryAssociation = BinaryAssociation(
    name="location17",
    ends={
        Property(name="model_Location18", type=model_MappedLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MappedLibrary", type=model_Location, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rareBooks19: BinaryAssociation = BinaryAssociation(
    name="rareBooks19",
    ends={
        Property(name="model_Book21", type=model_MappedLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MappedLibrary20", type=model_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
regularBooks22: BinaryAssociation = BinaryAssociation(
    name="regularBooks22",
    ends={
        Property(name="model_Book24", type=model_MappedLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MappedLibrary23", type=model_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
multipleContainmentReferenceProxies41: BinaryAssociation = BinaryAssociation(
    name="multipleContainmentReferenceProxies41",
    ends={
        Property(name="model_PrimaryObject42", type=model_TargetObject, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="model_TargetObject43", type=model_PrimaryObject, multiplicity=Multiplicity(1, 1))
    }
)
unsettableReference25: BinaryAssociation = BinaryAssociation(
    name="unsettableReference25",
    ends={
        Property(name="model_TargetObject", type=model_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PrimaryObject", type=model_TargetObject, multiplicity=Multiplicity(0, 1))
    }
)
singleNonContainmentReference26: BinaryAssociation = BinaryAssociation(
    name="singleNonContainmentReference26",
    ends={
        Property(name="model_TargetObject28", type=model_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PrimaryObject27", type=model_TargetObject, multiplicity=Multiplicity(0, 1))
    }
)
multipleNonContainmentReference29: BinaryAssociation = BinaryAssociation(
    name="multipleNonContainmentReference29",
    ends={
        Property(name="model_TargetObject31", type=model_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PrimaryObject30", type=model_TargetObject, multiplicity=Multiplicity(0, 9999))
    }
)
singleContainmentReferenceNoProxies32: BinaryAssociation = BinaryAssociation(
    name="singleContainmentReferenceNoProxies32",
    ends={
        Property(name="model_TargetObject34", type=model_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PrimaryObject33", type=model_TargetObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multipleContainmentReferenceNoProxies35: BinaryAssociation = BinaryAssociation(
    name="multipleContainmentReferenceNoProxies35",
    ends={
        Property(name="model_TargetObject37", type=model_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PrimaryObject36", type=model_TargetObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
singleContainmentReferenceProxies38: BinaryAssociation = BinaryAssociation(
    name="singleContainmentReferenceProxies38",
    ends={
        Property(name="model_TargetObject40", type=model_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PrimaryObject39", type=model_TargetObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
featureMapReferenceType244: BinaryAssociation = BinaryAssociation(
    name="featureMapReferenceType244",
    ends={
        Property(name="model_TargetObject46", type=model_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PrimaryObject45", type=model_TargetObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
featureMapReferenceType147: BinaryAssociation = BinaryAssociation(
    name="featureMapReferenceType147",
    ends={
        Property(name="model_TargetObject49", type=model_PrimaryObject, multiplicity=Multiplicity(1, 1)),
        Property(name="model_PrimaryObject48", type=model_TargetObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actors50: BinaryAssociation = BinaryAssociation(
    name="actors50",
    ends={
        Property(name="Actor", type=model_Movie, multiplicity=Multiplicity(1, 1)),
        Property(name="actorOf", type=model_Actor, multiplicity=Multiplicity(0, 9999))
    }
)
actorOf51: BinaryAssociation = BinaryAssociation(
    name="actorOf51",
    ends={
        Property(name="Movie", type=model_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="actors", type=model_Movie, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Person, model_Book, model_PersonBNode, model_BookBNode, model_BNode, model_Library, model_Location, model_ETypes, model_MappedLibrary, model_TargetObject, model_PrimaryObject, model_Movie, model_Actor},
    associations={books0, authors1, books2, latestBook11, authors3, child7, books8, location9, featuredBook14, location17, rareBooks19, regularBooks22, multipleContainmentReferenceProxies41, unsettableReference25, singleNonContainmentReference26, multipleNonContainmentReference29, singleContainmentReferenceNoProxies32, multipleContainmentReferenceNoProxies35, singleContainmentReferenceProxies38, featureMapReferenceType244, featureMapReferenceType147, actors50, actorOf51},
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