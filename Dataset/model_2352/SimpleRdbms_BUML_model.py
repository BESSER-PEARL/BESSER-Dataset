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
SimpleRDBMS_Table = Class(name="SimpleRDBMS::Table")
RModelElement = Class(name="RModelElement")
SimpleRDBMS_Column = Class(name="SimpleRDBMS::Column")
SimpleRDBMS_ForeignKey = Class(name="SimpleRDBMS::ForeignKey")
SimpleRDBMS_Key = Class(name="SimpleRDBMS::Key")
SimpleRDBMS_Schema = Class(name="SimpleRDBMS::Schema")
SimpleRDBMS_RModelElement = Class(name="SimpleRDBMS::RModelElement")

# SimpleRDBMS_Table class attributes and methods

# RModelElement class attributes and methods

# SimpleRDBMS_Column class attributes and methods
SimpleRDBMS_Column_type: Property = Property(name="type", type=StringType)
SimpleRDBMS_Column.attributes={SimpleRDBMS_Column_type}

# SimpleRDBMS_ForeignKey class attributes and methods

# SimpleRDBMS_Key class attributes and methods

# SimpleRDBMS_Schema class attributes and methods

# SimpleRDBMS_RModelElement class attributes and methods
SimpleRDBMS_RModelElement_kind: Property = Property(name="kind", type=StringType)
SimpleRDBMS_RModelElement_name: Property = Property(name="name", type=StringType)
SimpleRDBMS_RModelElement.attributes={SimpleRDBMS_RModelElement_name, SimpleRDBMS_RModelElement_kind}

# Relationships
column0: BinaryAssociation = BinaryAssociation(
    name="column0",
    ends={
        Property(name="Column", type=SimpleRDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=SimpleRDBMS_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreignKey1: BinaryAssociation = BinaryAssociation(
    name="foreignKey1",
    ends={
        Property(name="ForeignKey", type=SimpleRDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner2", type=SimpleRDBMS_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
_key3: BinaryAssociation = BinaryAssociation(
    name="_key3",
    ends={
        Property(name="Key", type=SimpleRDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner4", type=SimpleRDBMS_Key, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreignKey10: BinaryAssociation = BinaryAssociation(
    name="foreignKey10",
    ends={
        Property(name="column11", type=SimpleRDBMS_ForeignKey, multiplicity=Multiplicity(0, 9999)),
        Property(name="ForeignKey12", type=SimpleRDBMS_Column, multiplicity=Multiplicity(1, 1))
    }
)
column13: BinaryAssociation = BinaryAssociation(
    name="column13",
    ends={
        Property(name="Column14", type=SimpleRDBMS_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="_key", type=SimpleRDBMS_Column, multiplicity=Multiplicity(0, 9999))
    }
)
owner15: BinaryAssociation = BinaryAssociation(
    name="owner15",
    ends={
        Property(name="Table17", type=SimpleRDBMS_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="_key16", type=SimpleRDBMS_Table, multiplicity=Multiplicity(0, 1))
    }
)
column18: BinaryAssociation = BinaryAssociation(
    name="column18",
    ends={
        Property(name="Column19", type=SimpleRDBMS_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKey", type=SimpleRDBMS_Column, multiplicity=Multiplicity(0, 9999))
    }
)
schema5: BinaryAssociation = BinaryAssociation(
    name="schema5",
    ends={
        Property(name="Schema", type=SimpleRDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=SimpleRDBMS_Schema, multiplicity=Multiplicity(0, 1))
    }
)
owner6: BinaryAssociation = BinaryAssociation(
    name="owner6",
    ends={
        Property(name="Table", type=SimpleRDBMS_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column", type=SimpleRDBMS_Table, multiplicity=Multiplicity(0, 1))
    }
)
_key7: BinaryAssociation = BinaryAssociation(
    name="_key7",
    ends={
        Property(name="Key9", type=SimpleRDBMS_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column8", type=SimpleRDBMS_Key, multiplicity=Multiplicity(0, 9999))
    }
)
tables24: BinaryAssociation = BinaryAssociation(
    name="tables24",
    ends={
        Property(name="Table25", type=SimpleRDBMS_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema", type=SimpleRDBMS_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refersTo20: BinaryAssociation = BinaryAssociation(
    name="refersTo20",
    ends={
        Property(name="SimpleRDBMS_Key", type=SimpleRDBMS_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleRDBMS_ForeignKey", type=SimpleRDBMS_Key, multiplicity=Multiplicity(0, 1))
    }
)
owner21: BinaryAssociation = BinaryAssociation(
    name="owner21",
    ends={
        Property(name="Table23", type=SimpleRDBMS_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKey22", type=SimpleRDBMS_Table, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_SimpleRDBMS_Table_RModelElement = Generalization(general=RModelElement, specific=SimpleRDBMS_Table)
gen_SimpleRDBMS_Key_RModelElement = Generalization(general=RModelElement, specific=SimpleRDBMS_Key)
gen_SimpleRDBMS_ForeignKey_RModelElement = Generalization(general=RModelElement, specific=SimpleRDBMS_ForeignKey)
gen_SimpleRDBMS_Column_RModelElement = Generalization(general=RModelElement, specific=SimpleRDBMS_Column)
gen_SimpleRDBMS_Schema_RModelElement = Generalization(general=RModelElement, specific=SimpleRDBMS_Schema)

# Domain Model
domain_model = DomainModel(
    name="SimpleRDBMS",
    types={SimpleRDBMS_Table, RModelElement, SimpleRDBMS_Column, SimpleRDBMS_ForeignKey, SimpleRDBMS_Key, SimpleRDBMS_Schema, SimpleRDBMS_RModelElement},
    associations={column0, foreignKey1, _key3, foreignKey10, column13, owner15, column18, schema5, owner6, _key7, tables24, refersTo20, owner21},
    generalizations={gen_SimpleRDBMS_Table_RModelElement, gen_SimpleRDBMS_Key_RModelElement, gen_SimpleRDBMS_ForeignKey_RModelElement, gen_SimpleRDBMS_Column_RModelElement, gen_SimpleRDBMS_Schema_RModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)