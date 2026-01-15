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
simplerdbms_Key = Class(name="simplerdbms::Key")
simplerdbms_Column = Class(name="simplerdbms::Column")
RModelElement = Class(name="RModelElement")
simplerdbms_Table = Class(name="simplerdbms::Table")
simplerdbms_ForeignKey = Class(name="simplerdbms::ForeignKey")
simplerdbms_Primary_Key = Class(name="simplerdbms::Primary::Key")
Key = Class(name="Key")
simplerdbms_RModelElement = Class(name="simplerdbms::RModelElement", is_abstract=True)
simplerdbms_Schema = Class(name="simplerdbms::Schema")

# simplerdbms_Key class attributes and methods

# simplerdbms_Column class attributes and methods
simplerdbms_Column_type: Property = Property(name="type", type=StringType)
simplerdbms_Column.attributes={simplerdbms_Column_type}

# RModelElement class attributes and methods

# simplerdbms_Table class attributes and methods

# simplerdbms_ForeignKey class attributes and methods

# simplerdbms_Primary_Key class attributes and methods

# Key class attributes and methods

# simplerdbms_RModelElement class attributes and methods
simplerdbms_RModelElement_name: Property = Property(name="name", type=StringType)
simplerdbms_RModelElement_kind: Property = Property(name="kind", type=StringType)
simplerdbms_RModelElement.attributes={simplerdbms_RModelElement_kind, simplerdbms_RModelElement_name}

# simplerdbms_Schema class attributes and methods

# Relationships
owner0: BinaryAssociation = BinaryAssociation(
    name="owner0",
    ends={
        Property(name="Table", type=simplerdbms_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=simplerdbms_Table, multiplicity=Multiplicity(1, 1))
    }
)
foreignKeys1: BinaryAssociation = BinaryAssociation(
    name="foreignKeys1",
    ends={
        Property(name="ForeignKey", type=simplerdbms_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns2", type=simplerdbms_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
keys3: BinaryAssociation = BinaryAssociation(
    name="keys3",
    ends={
        Property(name="Key", type=simplerdbms_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns4", type=simplerdbms_Key, multiplicity=Multiplicity(0, 9999))
    }
)
refersTo5: BinaryAssociation = BinaryAssociation(
    name="refersTo5",
    ends={
        Property(name="simplerdbms_Key", type=simplerdbms_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="simplerdbms_ForeignKey", type=simplerdbms_Key, multiplicity=Multiplicity(1, 1))
    }
)
columns6: BinaryAssociation = BinaryAssociation(
    name="columns6",
    ends={
        Property(name="Column", type=simplerdbms_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKeys", type=simplerdbms_Column, multiplicity=Multiplicity(0, 9999))
    }
)
owner7: BinaryAssociation = BinaryAssociation(
    name="owner7",
    ends={
        Property(name="Table9", type=simplerdbms_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKeys8", type=simplerdbms_Table, multiplicity=Multiplicity(1, 1))
    }
)
k_owner10: BinaryAssociation = BinaryAssociation(
    name="k_owner10",
    ends={
        Property(name="Table11", type=simplerdbms_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="keys", type=simplerdbms_Table, multiplicity=Multiplicity(1, 1))
    }
)
columns12: BinaryAssociation = BinaryAssociation(
    name="columns12",
    ends={
        Property(name="Column14", type=simplerdbms_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="keys13", type=simplerdbms_Column, multiplicity=Multiplicity(0, 9999))
    }
)
pk_owner15: BinaryAssociation = BinaryAssociation(
    name="pk_owner15",
    ends={
        Property(name="Table16", type=simplerdbms_Primary_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="primary_key", type=simplerdbms_Table, multiplicity=Multiplicity(1, 1))
    }
)
tables17: BinaryAssociation = BinaryAssociation(
    name="tables17",
    ends={
        Property(name="Table18", type=simplerdbms_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema", type=simplerdbms_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns19: BinaryAssociation = BinaryAssociation(
    name="columns19",
    ends={
        Property(name="Column20", type=simplerdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=simplerdbms_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schema21: BinaryAssociation = BinaryAssociation(
    name="schema21",
    ends={
        Property(name="Schema", type=simplerdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=simplerdbms_Schema, multiplicity=Multiplicity(1, 1))
    }
)
keys22: BinaryAssociation = BinaryAssociation(
    name="keys22",
    ends={
        Property(name="Key23", type=simplerdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="k_owner", type=simplerdbms_Key, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreignKeys24: BinaryAssociation = BinaryAssociation(
    name="foreignKeys24",
    ends={
        Property(name="ForeignKey26", type=simplerdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner25", type=simplerdbms_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primary_key27: BinaryAssociation = BinaryAssociation(
    name="primary_key27",
    ends={
        Property(name="Primary_Key", type=simplerdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="pk_owner", type=simplerdbms_Primary_Key, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_simplerdbms_Column_RModelElement = Generalization(general=RModelElement, specific=simplerdbms_Column)
gen_simplerdbms_Primary_Key_Key = Generalization(general=Key, specific=simplerdbms_Primary_Key)
gen_simplerdbms_ForeignKey_RModelElement = Generalization(general=RModelElement, specific=simplerdbms_ForeignKey)
gen_simplerdbms_Key_RModelElement = Generalization(general=RModelElement, specific=simplerdbms_Key)
gen_simplerdbms_Schema_RModelElement = Generalization(general=RModelElement, specific=simplerdbms_Schema)
gen_simplerdbms_Table_RModelElement = Generalization(general=RModelElement, specific=simplerdbms_Table)

# Domain Model
domain_model = DomainModel(
    name="simplerdbms",
    types={simplerdbms_Key, simplerdbms_Column, RModelElement, simplerdbms_Table, simplerdbms_ForeignKey, simplerdbms_Primary_Key, Key, simplerdbms_RModelElement, simplerdbms_Schema},
    associations={owner0, foreignKeys1, keys3, refersTo5, columns6, owner7, k_owner10, columns12, pk_owner15, tables17, columns19, schema21, keys22, foreignKeys24, primary_key27},
    generalizations={gen_simplerdbms_Column_RModelElement, gen_simplerdbms_Primary_Key_Key, gen_simplerdbms_ForeignKey_RModelElement, gen_simplerdbms_Key_RModelElement, gen_simplerdbms_Schema_RModelElement, gen_simplerdbms_Table_RModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)