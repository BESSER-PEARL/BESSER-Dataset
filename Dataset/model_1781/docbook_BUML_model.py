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
docbook_ChapterType = Class(name="docbook::ChapterType")
docbook_BookType = Class(name="docbook::BookType")
docbook_Sect1Type = Class(name="docbook::Sect1Type")
docbook_DocumentRoot = Class(name="docbook::DocumentRoot")
docbook_EStringToStringMapEntry = Class(name="docbook::EStringToStringMapEntry")

# docbook_ChapterType class attributes and methods
docbook_ChapterType_mixed: Property = Property(name="mixed", type=StringType)
docbook_ChapterType_title: Property = Property(name="title", type=StringType)
docbook_ChapterType_para: Property = Property(name="para", type=StringType)
docbook_ChapterType.attributes={docbook_ChapterType_title, docbook_ChapterType_mixed, docbook_ChapterType_para}

# docbook_BookType class attributes and methods
docbook_BookType_title: Property = Property(name="title", type=StringType)
docbook_BookType_info: Property = Property(name="info", type=StringType)
docbook_BookType.attributes={docbook_BookType_title, docbook_BookType_info}

# docbook_Sect1Type class attributes and methods
docbook_Sect1Type_mixed: Property = Property(name="mixed", type=StringType)
docbook_Sect1Type_title: Property = Property(name="title", type=StringType)
docbook_Sect1Type_para: Property = Property(name="para", type=StringType)
docbook_Sect1Type.attributes={docbook_Sect1Type_title, docbook_Sect1Type_mixed, docbook_Sect1Type_para}

# docbook_DocumentRoot class attributes and methods
docbook_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
docbook_DocumentRoot_info: Property = Property(name="info", type=StringType)
docbook_DocumentRoot_para: Property = Property(name="para", type=StringType)
docbook_DocumentRoot_title: Property = Property(name="title", type=StringType)
docbook_DocumentRoot.attributes={docbook_DocumentRoot_title, docbook_DocumentRoot_mixed, docbook_DocumentRoot_info, docbook_DocumentRoot_para}

# docbook_EStringToStringMapEntry class attributes and methods

# Relationships
chapter0: BinaryAssociation = BinaryAssociation(
    name="chapter0",
    ends={
        Property(name="docbook_ChapterType", type=docbook_BookType, multiplicity=Multiplicity(1, 1)),
        Property(name="docbook_BookType", type=docbook_ChapterType, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
sect11: BinaryAssociation = BinaryAssociation(
    name="sect11",
    ends={
        Property(name="docbook_Sect1Type", type=docbook_ChapterType, multiplicity=Multiplicity(1, 1)),
        Property(name="docbook_ChapterType2", type=docbook_Sect1Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap3: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap3",
    ends={
        Property(name="docbook_EStringToStringMapEntry", type=docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="docbook_DocumentRoot", type=docbook_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation4: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation4",
    ends={
        Property(name="docbook_EStringToStringMapEntry6", type=docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="docbook_DocumentRoot5", type=docbook_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
book7: BinaryAssociation = BinaryAssociation(
    name="book7",
    ends={
        Property(name="docbook_BookType9", type=docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="docbook_DocumentRoot8", type=docbook_BookType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
chapter10: BinaryAssociation = BinaryAssociation(
    name="chapter10",
    ends={
        Property(name="docbook_ChapterType12", type=docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="docbook_DocumentRoot11", type=docbook_ChapterType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sect113: BinaryAssociation = BinaryAssociation(
    name="sect113",
    ends={
        Property(name="docbook_Sect1Type15", type=docbook_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="docbook_DocumentRoot14", type=docbook_Sect1Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="docbook",
    types={docbook_ChapterType, docbook_BookType, docbook_Sect1Type, docbook_DocumentRoot, docbook_EStringToStringMapEntry},
    associations={chapter0, sect11, xMLNSPrefixMap3, xSISchemaLocation4, book7, chapter10, sect113},
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