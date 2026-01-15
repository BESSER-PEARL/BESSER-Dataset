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
simplerdbms_Column = Class(name="simplerdbms::Column")
RModelElement = Class(name="RModelElement")
simplerdbms_RModelElement = Class(name="simplerdbms::RModelElement", is_abstract=True)
simplerdbms_Schema = Class(name="simplerdbms::Schema")
simplerdbms_Table = Class(name="simplerdbms::Table")
simplerdbms_ForeignKey = Class(name="simplerdbms::ForeignKey")
simplerdbms_Key = Class(name="simplerdbms::Key")

# simplerdbms_Column class attributes and methods
simplerdbms_Column_type: Property = Property(name="type", type=StringType)
simplerdbms_Column.attributes={simplerdbms_Column_type}

# RModelElement class attributes and methods

# simplerdbms_RModelElement class attributes and methods
simplerdbms_RModelElement_name: Property = Property(name="name", type=StringType)
simplerdbms_RModelElement_kind: Property = Property(name="kind", type=StringType)
simplerdbms_RModelElement.attributes={simplerdbms_RModelElement_kind, simplerdbms_RModelElement_name}

# simplerdbms_Schema class attributes and methods

# simplerdbms_Table class attributes and methods

# simplerdbms_ForeignKey class attributes and methods

# simplerdbms_Key class attributes and methods

# Relationships
owner9: BinaryAssociation = BinaryAssociation(
    name="owner9",
    ends={
        Property(name="Table10", type=simplerdbms_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="keys", type=simplerdbms_Table, multiplicity=Multiplicity(1, 1))
    }
)
column11: BinaryAssociation = BinaryAssociation(
    name="column11",
    ends={
        Property(name="Column13", type=simplerdbms_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="keys12", type=simplerdbms_Column, multiplicity=Multiplicity(0, 9999))
    }
)
tables14: BinaryAssociation = BinaryAssociation(
    name="tables14",
    ends={
        Property(name="Table15", type=simplerdbms_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema", type=simplerdbms_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns16: BinaryAssociation = BinaryAssociation(
    name="columns16",
    ends={
        Property(name="Column17", type=simplerdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=simplerdbms_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
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
        Property(name="column", type=simplerdbms_Key, multiplicity=Multiplicity(0, 9999))
    }
)
refersTo4: BinaryAssociation = BinaryAssociation(
    name="refersTo4",
    ends={
        Property(name="simplerdbms_Key", type=simplerdbms_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="simplerdbms_ForeignKey", type=simplerdbms_Key, multiplicity=Multiplicity(1, 1))
    }
)
columns5: BinaryAssociation = BinaryAssociation(
    name="columns5",
    ends={
        Property(name="Column", type=simplerdbms_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKeys", type=simplerdbms_Column, multiplicity=Multiplicity(0, 9999))
    }
)
owner6: BinaryAssociation = BinaryAssociation(
    name="owner6",
    ends={
        Property(name="Table8", type=simplerdbms_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKeys7", type=simplerdbms_Table, multiplicity=Multiplicity(1, 1))
    }
)
schema18: BinaryAssociation = BinaryAssociation(
    name="schema18",
    ends={
        Property(name="Schema", type=simplerdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=simplerdbms_Schema, multiplicity=Multiplicity(1, 1))
    }
)
keys19: BinaryAssociation = BinaryAssociation(
    name="keys19",
    ends={
        Property(name="Key21", type=simplerdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner20", type=simplerdbms_Key, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreignKeys22: BinaryAssociation = BinaryAssociation(
    name="foreignKeys22",
    ends={
        Property(name="ForeignKey24", type=simplerdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner23", type=simplerdbms_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_simplerdbms_Schema_RModelElement = Generalization(general=RModelElement, specific=simplerdbms_Schema)
gen_simplerdbms_Table_RModelElement = Generalization(general=RModelElement, specific=simplerdbms_Table)
gen_simplerdbms_Column_RModelElement = Generalization(general=RModelElement, specific=simplerdbms_Column)
gen_simplerdbms_ForeignKey_RModelElement = Generalization(general=RModelElement, specific=simplerdbms_ForeignKey)
gen_simplerdbms_Key_RModelElement = Generalization(general=RModelElement, specific=simplerdbms_Key)

# Domain Model
domain_model = DomainModel(
    name="simplerdbms",
    types={simplerdbms_Column, RModelElement, simplerdbms_RModelElement, simplerdbms_Schema, simplerdbms_Table, simplerdbms_ForeignKey, simplerdbms_Key},
    associations={owner9, column11, tables14, columns16, owner0, foreignKeys1, keys3, refersTo4, columns5, owner6, schema18, keys19, foreignKeys22},
    generalizations={gen_simplerdbms_Schema_RModelElement, gen_simplerdbms_Table_RModelElement, gen_simplerdbms_Column_RModelElement, gen_simplerdbms_ForeignKey_RModelElement, gen_simplerdbms_Key_RModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)