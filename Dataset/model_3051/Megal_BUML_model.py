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
megal_MegalRelationship = Class(name="megal::MegalRelationship")
MegalDeclaration = Class(name="MegalDeclaration")
megal_MegalRelationshipType = Class(name="megal::MegalRelationshipType")
megal_MegalPair = Class(name="megal::MegalPair")
megal_MegalAnnotation = Class(name="megal::MegalAnnotation")
megal_Selection = Class(name="megal::Selection")
megal_MegalElement = Class(name="megal::MegalElement", is_abstract=True)
megal_MegalFile = Class(name="megal::MegalFile")
MegalElement = Class(name="MegalElement")
megal_MegalDeclaration = Class(name="megal::MegalDeclaration", is_abstract=True)
megal_MegalLink = Class(name="megal::MegalLink")
megal_MegalEntity = Class(name="megal::MegalEntity")
megal_MegalNamed = Class(name="megal::MegalNamed", is_abstract=True)
megal_MegalEntityType = Class(name="megal::MegalEntityType")
MegalNamed = Class(name="MegalNamed")
megal_QueryParam = Class(name="megal::QueryParam")
QueryEntry = Class(name="QueryEntry")
megal_QueryEntry = Class(name="megal::QueryEntry", is_abstract=True)
megal_QueryStatement = Class(name="megal::QueryStatement")
megal_QueryPos = Class(name="megal::QueryPos")
megal_QueryReference = Class(name="megal::QueryReference")
megal_QueryString = Class(name="megal::QueryString")
megal_QueryEntity = Class(name="megal::QueryEntity")

# megal_MegalRelationship class attributes and methods

# MegalDeclaration class attributes and methods

# megal_MegalRelationshipType class attributes and methods
megal_MegalRelationshipType_leftBoth: Property = Property(name="leftBoth", type=BooleanType)
megal_MegalRelationshipType_rightBoth: Property = Property(name="rightBoth", type=BooleanType)
megal_MegalRelationshipType_leftMany: Property = Property(name="leftMany", type=BooleanType)
megal_MegalRelationshipType_rightMany: Property = Property(name="rightMany", type=BooleanType)
megal_MegalRelationshipType.attributes={megal_MegalRelationshipType_leftMany, megal_MegalRelationshipType_rightBoth, megal_MegalRelationshipType_leftBoth, megal_MegalRelationshipType_rightMany}

# megal_MegalPair class attributes and methods

# megal_MegalAnnotation class attributes and methods
megal_MegalAnnotation_key: Property = Property(name="key", type=StringType)
megal_MegalAnnotation.attributes={megal_MegalAnnotation_key}

# megal_Selection class attributes and methods

# megal_MegalElement class attributes and methods

# megal_MegalFile class attributes and methods
megal_MegalFile_name: Property = Property(name="name", type=StringType)
megal_MegalFile.attributes={megal_MegalFile_name}

# MegalElement class attributes and methods

# megal_MegalDeclaration class attributes and methods

# megal_MegalLink class attributes and methods
megal_MegalLink_to: Property = Property(name="to", type=StringType)
megal_MegalLink.attributes={megal_MegalLink_to}

# megal_MegalEntity class attributes and methods
megal_MegalEntity_many: Property = Property(name="many", type=BooleanType)
megal_MegalEntity.attributes={megal_MegalEntity_many}

# megal_MegalNamed class attributes and methods
megal_MegalNamed_name: Property = Property(name="name", type=StringType)
megal_MegalNamed.attributes={megal_MegalNamed_name}

# megal_MegalEntityType class attributes and methods

# MegalNamed class attributes and methods

# megal_QueryParam class attributes and methods
megal_QueryParam_name: Property = Property(name="name", type=StringType)
megal_QueryParam.attributes={megal_QueryParam_name}

# QueryEntry class attributes and methods

# megal_QueryEntry class attributes and methods

# megal_QueryStatement class attributes and methods

# megal_QueryPos class attributes and methods
megal_QueryPos_value: Property = Property(name="value", type=IntegerType)
megal_QueryPos.attributes={megal_QueryPos_value}

# megal_QueryReference class attributes and methods

# megal_QueryString class attributes and methods
megal_QueryString_value: Property = Property(name="value", type=StringType)
megal_QueryString.attributes={megal_QueryString_value}

# megal_QueryEntity class attributes and methods

# Relationships
first11: BinaryAssociation = BinaryAssociation(
    name="first11",
    ends={
        Property(name="megal_MegalEntity13", type=megal_MegalLink, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_MegalLink12", type=megal_MegalEntity, multiplicity=Multiplicity(0, 1))
    }
)
second14: BinaryAssociation = BinaryAssociation(
    name="second14",
    ends={
        Property(name="megal_MegalEntity16", type=megal_MegalLink, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_MegalLink15", type=megal_MegalEntity, multiplicity=Multiplicity(0, 1))
    }
)
type17: BinaryAssociation = BinaryAssociation(
    name="type17",
    ends={
        Property(name="megal_MegalRelationshipType", type=megal_MegalRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_MegalRelationship", type=megal_MegalRelationshipType, multiplicity=Multiplicity(1, 1))
    }
)
left18: BinaryAssociation = BinaryAssociation(
    name="left18",
    ends={
        Property(name="megal_MegalEntity20", type=megal_MegalRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_MegalRelationship19", type=megal_MegalEntity, multiplicity=Multiplicity(1, 1))
    }
)
right21: BinaryAssociation = BinaryAssociation(
    name="right21",
    ends={
        Property(name="megal_MegalEntity23", type=megal_MegalRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_MegalRelationship22", type=megal_MegalEntity, multiplicity=Multiplicity(1, 1))
    }
)
set24: BinaryAssociation = BinaryAssociation(
    name="set24",
    ends={
        Property(name="megal_MegalEntity25", type=megal_MegalPair, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_MegalPair", type=megal_MegalEntity, multiplicity=Multiplicity(1, 1))
    }
)
first26: BinaryAssociation = BinaryAssociation(
    name="first26",
    ends={
        Property(name="megal_MegalEntity28", type=megal_MegalPair, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_MegalPair27", type=megal_MegalEntity, multiplicity=Multiplicity(1, 1))
    }
)
selection0: BinaryAssociation = BinaryAssociation(
    name="selection0",
    ends={
        Property(name="megal_Selection", type=megal_MegalAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_MegalAnnotation", type=megal_Selection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations1: BinaryAssociation = BinaryAssociation(
    name="annotations1",
    ends={
        Property(name="megal_MegalAnnotation2", type=megal_MegalElement, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_MegalElement", type=megal_MegalAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations3: BinaryAssociation = BinaryAssociation(
    name="declarations3",
    ends={
        Property(name="megal_MegalDeclaration", type=megal_MegalFile, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_MegalFile", type=megal_MegalDeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindings4: BinaryAssociation = BinaryAssociation(
    name="bindings4",
    ends={
        Property(name="megal_MegalLink", type=megal_MegalFile, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_MegalFile5", type=megal_MegalLink, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports7: BinaryAssociation = BinaryAssociation(
    name="imports7",
    ends={
        Property(name="megal_MegalFile8", type=megal_MegalFile, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_MegalFile6", type=megal_MegalFile, multiplicity=Multiplicity(0, 9999))
    }
)
link9: BinaryAssociation = BinaryAssociation(
    name="link9",
    ends={
        Property(name="megal_MegalEntity", type=megal_MegalLink, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_MegalLink10", type=megal_MegalEntity, multiplicity=Multiplicity(1, 1))
    }
)
type46: BinaryAssociation = BinaryAssociation(
    name="type46",
    ends={
        Property(name="megal_MegalEntityType48", type=megal_MegalEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_MegalEntity47", type=megal_MegalEntityType, multiplicity=Multiplicity(1, 1))
    }
)
params50: BinaryAssociation = BinaryAssociation(
    name="params50",
    ends={
        Property(name="megal_MegalEntity51", type=megal_MegalEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_MegalEntity49", type=megal_MegalEntity, multiplicity=Multiplicity(0, 9999))
    }
)
second29: BinaryAssociation = BinaryAssociation(
    name="second29",
    ends={
        Property(name="megal_MegalEntity31", type=megal_MegalPair, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_MegalPair30", type=megal_MegalEntity, multiplicity=Multiplicity(1, 1))
    }
)
supertype33: BinaryAssociation = BinaryAssociation(
    name="supertype33",
    ends={
        Property(name="megal_MegalEntityType", type=megal_MegalEntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_MegalEntityType32", type=megal_MegalEntityType, multiplicity=Multiplicity(0, 1))
    }
)
left34: BinaryAssociation = BinaryAssociation(
    name="left34",
    ends={
        Property(name="megal_MegalEntityType36", type=megal_MegalRelationshipType, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_MegalRelationshipType35", type=megal_MegalEntityType, multiplicity=Multiplicity(1, 1))
    }
)
right37: BinaryAssociation = BinaryAssociation(
    name="right37",
    ends={
        Property(name="megal_MegalEntityType39", type=megal_MegalRelationshipType, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_MegalRelationshipType38", type=megal_MegalEntityType, multiplicity=Multiplicity(1, 1))
    }
)
leftParams40: BinaryAssociation = BinaryAssociation(
    name="leftParams40",
    ends={
        Property(name="megal_MegalEntity42", type=megal_MegalRelationshipType, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_MegalRelationshipType41", type=megal_MegalEntity, multiplicity=Multiplicity(0, 9999))
    }
)
rightParams43: BinaryAssociation = BinaryAssociation(
    name="rightParams43",
    ends={
        Property(name="megal_MegalEntity45", type=megal_MegalRelationshipType, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_MegalRelationshipType44", type=megal_MegalEntity, multiplicity=Multiplicity(0, 9999))
    }
)
object62: BinaryAssociation = BinaryAssociation(
    name="object62",
    ends={
        Property(name="megal_QueryEntry64", type=megal_QueryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_QueryStatement63", type=megal_QueryEntry, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type65: BinaryAssociation = BinaryAssociation(
    name="type65",
    ends={
        Property(name="megal_MegalEntityType66", type=megal_QueryParam, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_QueryParam", type=megal_MegalEntityType, multiplicity=Multiplicity(0, 1))
    }
)
select52: BinaryAssociation = BinaryAssociation(
    name="select52",
    ends={
        Property(name="megal_QueryEntry", type=megal_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_Selection53", type=megal_QueryEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
query54: BinaryAssociation = BinaryAssociation(
    name="query54",
    ends={
        Property(name="megal_QueryStatement", type=megal_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_Selection55", type=megal_QueryStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subject56: BinaryAssociation = BinaryAssociation(
    name="subject56",
    ends={
        Property(name="megal_QueryEntry58", type=megal_QueryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_QueryStatement57", type=megal_QueryEntry, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
predicate59: BinaryAssociation = BinaryAssociation(
    name="predicate59",
    ends={
        Property(name="megal_MegalRelationshipType61", type=megal_QueryStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_QueryStatement60", type=megal_MegalRelationshipType, multiplicity=Multiplicity(1, 1))
    }
)
ref67: BinaryAssociation = BinaryAssociation(
    name="ref67",
    ends={
        Property(name="megal_QueryParam68", type=megal_QueryReference, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_QueryReference", type=megal_QueryParam, multiplicity=Multiplicity(0, 1))
    }
)
entity69: BinaryAssociation = BinaryAssociation(
    name="entity69",
    ends={
        Property(name="megal_MegalEntity70", type=megal_QueryEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="megal_QueryEntity", type=megal_MegalEntity, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_megal_MegalDeclaration_MegalElement = Generalization(general=MegalElement, specific=megal_MegalDeclaration)
gen_megal_MegalRelationship_MegalDeclaration = Generalization(general=MegalDeclaration, specific=megal_MegalRelationship)
gen_megal_MegalPair_MegalDeclaration = Generalization(general=MegalDeclaration, specific=megal_MegalPair)
gen_megal_MegalFile_MegalElement = Generalization(general=MegalElement, specific=megal_MegalFile)
gen_megal_MegalLink_MegalElement = Generalization(general=MegalElement, specific=megal_MegalLink)
gen_megal_MegalEntity_MegalNamed = Generalization(general=MegalNamed, specific=megal_MegalEntity)
gen_megal_MegalNamed_MegalDeclaration = Generalization(general=MegalDeclaration, specific=megal_MegalNamed)
gen_megal_MegalEntityType_MegalNamed = Generalization(general=MegalNamed, specific=megal_MegalEntityType)
gen_megal_MegalRelationshipType_MegalNamed = Generalization(general=MegalNamed, specific=megal_MegalRelationshipType)
gen_megal_QueryParam_QueryEntry = Generalization(general=QueryEntry, specific=megal_QueryParam)
gen_megal_QueryPos_QueryEntry = Generalization(general=QueryEntry, specific=megal_QueryPos)
gen_megal_QueryReference_QueryEntry = Generalization(general=QueryEntry, specific=megal_QueryReference)
gen_megal_QueryString_QueryEntry = Generalization(general=QueryEntry, specific=megal_QueryString)
gen_megal_QueryEntity_QueryEntry = Generalization(general=QueryEntry, specific=megal_QueryEntity)

# Domain Model
domain_model = DomainModel(
    name="megal",
    types={megal_MegalRelationship, MegalDeclaration, megal_MegalRelationshipType, megal_MegalPair, megal_MegalAnnotation, megal_Selection, megal_MegalElement, megal_MegalFile, MegalElement, megal_MegalDeclaration, megal_MegalLink, megal_MegalEntity, megal_MegalNamed, megal_MegalEntityType, MegalNamed, megal_QueryParam, QueryEntry, megal_QueryEntry, megal_QueryStatement, megal_QueryPos, megal_QueryReference, megal_QueryString, megal_QueryEntity},
    associations={first11, second14, type17, left18, right21, set24, first26, selection0, annotations1, declarations3, bindings4, imports7, link9, type46, params50, second29, supertype33, left34, right37, leftParams40, rightParams43, object62, type65, select52, query54, subject56, predicate59, ref67, entity69},
    generalizations={gen_megal_MegalDeclaration_MegalElement, gen_megal_MegalRelationship_MegalDeclaration, gen_megal_MegalPair_MegalDeclaration, gen_megal_MegalFile_MegalElement, gen_megal_MegalLink_MegalElement, gen_megal_MegalEntity_MegalNamed, gen_megal_MegalNamed_MegalDeclaration, gen_megal_MegalEntityType_MegalNamed, gen_megal_MegalRelationshipType_MegalNamed, gen_megal_QueryParam_QueryEntry, gen_megal_QueryPos_QueryEntry, gen_megal_QueryReference_QueryEntry, gen_megal_QueryString_QueryEntry, gen_megal_QueryEntity_QueryEntry},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)