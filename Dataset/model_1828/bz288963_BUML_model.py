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
Booktype: Enumeration = Enumeration(
    name="Booktype",
    literals={
            EnumerationLiteral(name="science"),
			EnumerationLiteral(name="novel")
    }
)

# Classes
bz288963_Book = Class(name="bz288963::Book")
bz288963_Paragraph = Class(name="bz288963::Paragraph")
bz288963_DocumentRoot = Class(name="bz288963::DocumentRoot")
bz288963_EStringToStringMapEntry = Class(name="bz288963::EStringToStringMapEntry")
Paragraph = Class(name="Paragraph")
bz288963_Footnote = Class(name="bz288963::Footnote")
bz288963_Indentedpara = Class(name="bz288963::Indentedpara")

# bz288963_Book class attributes and methods
bz288963_Book_id: Property = Property(name="id", type=StringType)
bz288963_Book_selfdef: Property = Property(name="selfdef", type=StringType)
bz288963_Book_type: Property = Property(name="type", type=StringType)
bz288963_Book.attributes={bz288963_Book_id, bz288963_Book_selfdef, bz288963_Book_type}

# bz288963_Paragraph class attributes and methods
bz288963_Paragraph_number: Property = Property(name="number", type=StringType)
bz288963_Paragraph_title: Property = Property(name="title", type=StringType)
bz288963_Paragraph.attributes={bz288963_Paragraph_number, bz288963_Paragraph_title}

# bz288963_DocumentRoot class attributes and methods
bz288963_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
bz288963_DocumentRoot.attributes={bz288963_DocumentRoot_mixed}

# bz288963_EStringToStringMapEntry class attributes and methods

# Paragraph class attributes and methods

# bz288963_Footnote class attributes and methods

# bz288963_Indentedpara class attributes and methods
bz288963_Indentedpara_indentSpace: Property = Property(name="indentSpace", type=StringType)
bz288963_Indentedpara.attributes={bz288963_Indentedpara_indentSpace}

# Relationships
citation1: BinaryAssociation = BinaryAssociation(
    name="citation1",
    ends={
        Property(name="bz288963_Book", type=bz288963_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="bz288963_Book0", type=bz288963_Book, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
paralist2: BinaryAssociation = BinaryAssociation(
    name="paralist2",
    ends={
        Property(name="bz288963_Paragraph", type=bz288963_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="bz288963_Book3", type=bz288963_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xMLNSPrefixMap4: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap4",
    ends={
        Property(name="bz288963_EStringToStringMapEntry", type=bz288963_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bz288963_DocumentRoot", type=bz288963_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation5: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation5",
    ends={
        Property(name="bz288963_EStringToStringMapEntry7", type=bz288963_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bz288963_DocumentRoot6", type=bz288963_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
book8: BinaryAssociation = BinaryAssociation(
    name="book8",
    ends={
        Property(name="bz288963_Book10", type=bz288963_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bz288963_DocumentRoot9", type=bz288963_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
footnote11: BinaryAssociation = BinaryAssociation(
    name="footnote11",
    ends={
        Property(name="bz288963_Footnote", type=bz288963_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bz288963_DocumentRoot12", type=bz288963_Footnote, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
indentedpara13: BinaryAssociation = BinaryAssociation(
    name="indentedpara13",
    ends={
        Property(name="bz288963_Indentedpara", type=bz288963_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bz288963_DocumentRoot14", type=bz288963_Indentedpara, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
paragraph15: BinaryAssociation = BinaryAssociation(
    name="paragraph15",
    ends={
        Property(name="bz288963_Paragraph17", type=bz288963_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="bz288963_DocumentRoot16", type=bz288963_Paragraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_bz288963_Footnote_Paragraph = Generalization(general=Paragraph, specific=bz288963_Footnote)
gen_bz288963_Indentedpara_Paragraph = Generalization(general=Paragraph, specific=bz288963_Indentedpara)

# Domain Model
domain_model = DomainModel(
    name="bz288963",
    types={bz288963_Book, bz288963_Paragraph, bz288963_DocumentRoot, bz288963_EStringToStringMapEntry, Paragraph, bz288963_Footnote, bz288963_Indentedpara, Booktype},
    associations={citation1, paralist2, xMLNSPrefixMap4, xSISchemaLocation5, book8, footnote11, indentedpara13, paragraph15},
    generalizations={gen_bz288963_Footnote_Paragraph, gen_bz288963_Indentedpara_Paragraph},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)