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
rdbms_Column = Class(name="rdbms::Column")
RModelElement = Class(name="RModelElement")
rdbms_Table = Class(name="rdbms::Table")
rdbms_ForeignKey = Class(name="rdbms::ForeignKey")
rdbms_Key = Class(name="rdbms::Key")
rdbms_RModelElement = Class(name="rdbms::RModelElement", is_abstract=True)
rdbms_Schema = Class(name="rdbms::Schema")

# rdbms_Column class attributes and methods
rdbms_Column_type: Property = Property(name="type", type=StringType)
rdbms_Column.attributes={rdbms_Column_type}

# RModelElement class attributes and methods

# rdbms_Table class attributes and methods

# rdbms_ForeignKey class attributes and methods

# rdbms_Key class attributes and methods

# rdbms_RModelElement class attributes and methods
rdbms_RModelElement_name: Property = Property(name="name", type=StringType)
rdbms_RModelElement_kind: Property = Property(name="kind", type=StringType)
rdbms_RModelElement.attributes={rdbms_RModelElement_kind, rdbms_RModelElement_name}

# rdbms_Schema class attributes and methods

# Relationships
columns5: BinaryAssociation = BinaryAssociation(
    name="columns5",
    ends={
        Property(name="Column", type=rdbms_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKeys", type=rdbms_Column, multiplicity=Multiplicity(0, 9999))
    }
)
owner0: BinaryAssociation = BinaryAssociation(
    name="owner0",
    ends={
        Property(name="Table", type=rdbms_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=rdbms_Table, multiplicity=Multiplicity(1, 1))
    }
)
foreignKeys1: BinaryAssociation = BinaryAssociation(
    name="foreignKeys1",
    ends={
        Property(name="ForeignKey", type=rdbms_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns2", type=rdbms_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
keys3: BinaryAssociation = BinaryAssociation(
    name="keys3",
    ends={
        Property(name="Key", type=rdbms_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column", type=rdbms_Key, multiplicity=Multiplicity(0, 9999))
    }
)
refersTo4: BinaryAssociation = BinaryAssociation(
    name="refersTo4",
    ends={
        Property(name="rdbms_Key", type=rdbms_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbms_ForeignKey", type=rdbms_Key, multiplicity=Multiplicity(1, 1))
    }
)
columns16: BinaryAssociation = BinaryAssociation(
    name="columns16",
    ends={
        Property(name="Column17", type=rdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=rdbms_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schema18: BinaryAssociation = BinaryAssociation(
    name="schema18",
    ends={
        Property(name="Schema", type=rdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=rdbms_Schema, multiplicity=Multiplicity(1, 1))
    }
)
keys19: BinaryAssociation = BinaryAssociation(
    name="keys19",
    ends={
        Property(name="Key21", type=rdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner20", type=rdbms_Key, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner6: BinaryAssociation = BinaryAssociation(
    name="owner6",
    ends={
        Property(name="Table8", type=rdbms_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKeys7", type=rdbms_Table, multiplicity=Multiplicity(1, 1))
    }
)
owner9: BinaryAssociation = BinaryAssociation(
    name="owner9",
    ends={
        Property(name="Table10", type=rdbms_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="keys", type=rdbms_Table, multiplicity=Multiplicity(1, 1))
    }
)
column11: BinaryAssociation = BinaryAssociation(
    name="column11",
    ends={
        Property(name="Column13", type=rdbms_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="keys12", type=rdbms_Column, multiplicity=Multiplicity(0, 9999))
    }
)
tables14: BinaryAssociation = BinaryAssociation(
    name="tables14",
    ends={
        Property(name="Table15", type=rdbms_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema", type=rdbms_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreignKeys22: BinaryAssociation = BinaryAssociation(
    name="foreignKeys22",
    ends={
        Property(name="ForeignKey24", type=rdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner23", type=rdbms_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_rdbms_Column_RModelElement = Generalization(general=RModelElement, specific=rdbms_Column)
gen_rdbms_ForeignKey_RModelElement = Generalization(general=RModelElement, specific=rdbms_ForeignKey)
gen_rdbms_Key_RModelElement = Generalization(general=RModelElement, specific=rdbms_Key)
gen_rdbms_Schema_RModelElement = Generalization(general=RModelElement, specific=rdbms_Schema)
gen_rdbms_Table_RModelElement = Generalization(general=RModelElement, specific=rdbms_Table)

# Domain Model
domain_model = DomainModel(
    name="rdbms",
    types={rdbms_Column, RModelElement, rdbms_Table, rdbms_ForeignKey, rdbms_Key, rdbms_RModelElement, rdbms_Schema},
    associations={columns5, owner0, foreignKeys1, keys3, refersTo4, columns16, schema18, keys19, owner6, owner9, column11, tables14, foreignKeys22},
    generalizations={gen_rdbms_Column_RModelElement, gen_rdbms_ForeignKey_RModelElement, gen_rdbms_Key_RModelElement, gen_rdbms_Schema_RModelElement, gen_rdbms_Table_RModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)