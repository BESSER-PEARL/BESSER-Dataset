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
emapsample_Book = Class(name="emapsample::Book")
emapsample_EStringToStringMapEntry = Class(name="emapsample::EStringToStringMapEntry")
emapsample_WriterToNameMapEntry = Class(name="emapsample::WriterToNameMapEntry")
emapsample_StringToWriterMapEntry = Class(name="emapsample::StringToWriterMapEntry")
emapsample_BookStore = Class(name="emapsample::BookStore")
Identifiable = Class(name="Identifiable")
emapsample_WriterToBookMapEntry = Class(name="emapsample::WriterToBookMapEntry")
emapsample_Writer = Class(name="emapsample::Writer")

# emapsample_Book class attributes and methods
emapsample_Book_title: Property = Property(name="title", type=StringType)
emapsample_Book.attributes={emapsample_Book_title}

# emapsample_EStringToStringMapEntry class attributes and methods

# emapsample_WriterToNameMapEntry class attributes and methods
emapsample_WriterToNameMapEntry_value: Property = Property(name="value", type=StringType)
emapsample_WriterToNameMapEntry.attributes={emapsample_WriterToNameMapEntry_value}

# emapsample_StringToWriterMapEntry class attributes and methods
emapsample_StringToWriterMapEntry_key: Property = Property(name="key", type=StringType)
emapsample_StringToWriterMapEntry.attributes={emapsample_StringToWriterMapEntry_key}

# emapsample_BookStore class attributes and methods
emapsample_BookStore_name: Property = Property(name="name", type=StringType)
emapsample_BookStore.attributes={emapsample_BookStore_name}

# Identifiable class attributes and methods

# emapsample_WriterToBookMapEntry class attributes and methods

# emapsample_Writer class attributes and methods
emapsample_Writer_name: Property = Property(name="name", type=StringType)
emapsample_Writer.attributes={emapsample_Writer_name}

# Relationships
booksByWriter1: BinaryAssociation = BinaryAssociation(
    name="booksByWriter1",
    ends={
        Property(name="emapsample_WriterToBookMapEntry", type=emapsample_BookStore, multiplicity=Multiplicity(1, 1)),
        Property(name="emapsample_BookStore", type=emapsample_WriterToBookMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyWords2: BinaryAssociation = BinaryAssociation(
    name="keyWords2",
    ends={
        Property(name="emapsample_EStringToStringMapEntry", type=emapsample_BookStore, multiplicity=Multiplicity(1, 1)),
        Property(name="emapsample_BookStore3", type=emapsample_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
namesByWriter4: BinaryAssociation = BinaryAssociation(
    name="namesByWriter4",
    ends={
        Property(name="emapsample_WriterToNameMapEntry", type=emapsample_BookStore, multiplicity=Multiplicity(1, 1)),
        Property(name="emapsample_BookStore5", type=emapsample_WriterToNameMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writers0: BinaryAssociation = BinaryAssociation(
    name="writers0",
    ends={
        Property(name="emapsample_StringToWriterMapEntry", type=emapsample_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="emapsample_Book", type=emapsample_StringToWriterMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key8: BinaryAssociation = BinaryAssociation(
    name="key8",
    ends={
        Property(name="emapsample_Writer10", type=emapsample_WriterToBookMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="emapsample_WriterToBookMapEntry9", type=emapsample_Writer, multiplicity=Multiplicity(1, 1))
    }
)
value6: BinaryAssociation = BinaryAssociation(
    name="value6",
    ends={
        Property(name="emapsample_Writer", type=emapsample_StringToWriterMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="emapsample_StringToWriterMapEntry7", type=emapsample_Writer, multiplicity=Multiplicity(1, 1))
    }
)
value11: BinaryAssociation = BinaryAssociation(
    name="value11",
    ends={
        Property(name="emapsample_Book13", type=emapsample_WriterToBookMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="emapsample_WriterToBookMapEntry12", type=emapsample_Book, multiplicity=Multiplicity(1, 1))
    }
)
key14: BinaryAssociation = BinaryAssociation(
    name="key14",
    ends={
        Property(name="emapsample_Writer16", type=emapsample_WriterToNameMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="emapsample_WriterToNameMapEntry15", type=emapsample_Writer, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_emapsample_BookStore_Identifiable = Generalization(general=Identifiable, specific=emapsample_BookStore)
gen_emapsample_Writer_Identifiable = Generalization(general=Identifiable, specific=emapsample_Writer)

# Domain Model
domain_model = DomainModel(
    name="emapsample",
    types={emapsample_Book, emapsample_EStringToStringMapEntry, emapsample_WriterToNameMapEntry, emapsample_StringToWriterMapEntry, emapsample_BookStore, Identifiable, emapsample_WriterToBookMapEntry, emapsample_Writer},
    associations={booksByWriter1, keyWords2, namesByWriter4, writers0, key8, value6, value11, key14},
    generalizations={gen_emapsample_BookStore_Identifiable, gen_emapsample_Writer_Identifiable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)