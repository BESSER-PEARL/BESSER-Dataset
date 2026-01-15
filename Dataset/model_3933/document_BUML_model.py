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
document_Chapter = Class(name="document::Chapter")
document_Section = Class(name="document::Section")
document_Table = Class(name="document::Table")
document_Entry = Class(name="document::Entry", is_abstract=True)
document_FullEntry = Class(name="document::FullEntry")
Entry = Class(name="Entry")
document_BasicEntry = Class(name="document::BasicEntry")

# document_Chapter class attributes and methods

# document_Section class attributes and methods

# document_Table class attributes and methods

# document_Entry class attributes and methods
document_Entry_isBold: Property = Property(name="isBold", type=BooleanType)
document_Entry_isItalic: Property = Property(name="isItalic", type=BooleanType)
document_Entry_text: Property = Property(name="text", type=StringType)
document_Entry.attributes={document_Entry_text, document_Entry_isBold, document_Entry_isItalic}

# document_FullEntry class attributes and methods

# Entry class attributes and methods

# document_BasicEntry class attributes and methods

# Relationships
sections0: BinaryAssociation = BinaryAssociation(
    name="sections0",
    ends={
        Property(name="document_Section", type=document_Chapter, multiplicity=Multiplicity(1, 1)),
        Property(name="document_Chapter", type=document_Section, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables1: BinaryAssociation = BinaryAssociation(
    name="tables1",
    ends={
        Property(name="document_Table", type=document_Section, multiplicity=Multiplicity(1, 1)),
        Property(name="document_Section2", type=document_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entries3: BinaryAssociation = BinaryAssociation(
    name="entries3",
    ends={
        Property(name="document_Entry", type=document_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="document_Table4", type=document_Entry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_document_FullEntry_Entry = Generalization(general=Entry, specific=document_FullEntry)
gen_document_BasicEntry_Entry = Generalization(general=Entry, specific=document_BasicEntry)

# Domain Model
domain_model = DomainModel(
    name="document",
    types={document_Chapter, document_Section, document_Table, document_Entry, document_FullEntry, Entry, document_BasicEntry},
    associations={sections0, tables1, entries3},
    generalizations={gen_document_FullEntry_Entry, gen_document_BasicEntry_Entry},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)