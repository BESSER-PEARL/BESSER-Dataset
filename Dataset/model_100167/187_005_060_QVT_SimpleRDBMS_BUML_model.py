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
SimpleRDBMS_RModelElement = Class(name="SimpleRDBMS_RModelElement", is_abstract=True)
SimpleRDBMS_Schema = Class(name="SimpleRDBMS_Schema")
RModelElement = Class(name="RModelElement")
Table = Class(name="Table")
SimpleRDBMS_Table = Class(name="SimpleRDBMS_Table")
Schema = Class(name="Schema")
Column = Class(name="Column")
Key = Class(name="Key")
ForeignKey = Class(name="ForeignKey")
SimpleRDBMS_Column = Class(name="SimpleRDBMS_Column")
SimpleRDBMS_Key = Class(name="SimpleRDBMS_Key")
SimpleRDBMS_ForeignKey = Class(name="SimpleRDBMS_ForeignKey")

# SimpleRDBMS_RModelElement class attributes and methods
SimpleRDBMS_RModelElement_kind: Property = Property(name="kind", type=StringType)
SimpleRDBMS_RModelElement_name: Property = Property(name="name", type=StringType)
SimpleRDBMS_RModelElement.attributes={SimpleRDBMS_RModelElement_kind, SimpleRDBMS_RModelElement_name}

# SimpleRDBMS_Schema class attributes and methods

# RModelElement class attributes and methods

# Table class attributes and methods

# SimpleRDBMS_Table class attributes and methods

# Schema class attributes and methods

# Column class attributes and methods

# Key class attributes and methods

# ForeignKey class attributes and methods

# SimpleRDBMS_Column class attributes and methods
SimpleRDBMS_Column_type: Property = Property(name="type", type=StringType)
SimpleRDBMS_Column.attributes={SimpleRDBMS_Column_type}

# SimpleRDBMS_Key class attributes and methods

# SimpleRDBMS_ForeignKey class attributes and methods

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="Table", type=SimpleRDBMS_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema", type=Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schema1: BinaryAssociation = BinaryAssociation(
    name="schema1",
    ends={
        Property(name="Schema", type=SimpleRDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=Schema, multiplicity=Multiplicity(1, 1))
    }
)
column2: BinaryAssociation = BinaryAssociation(
    name="column2",
    ends={
        Property(name="Column", type=SimpleRDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key3: BinaryAssociation = BinaryAssociation(
    name="key3",
    ends={
        Property(name="Key", type=SimpleRDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner4", type=Key, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreignKey5: BinaryAssociation = BinaryAssociation(
    name="foreignKey5",
    ends={
        Property(name="ForeignKey", type=SimpleRDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner6", type=ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner7: BinaryAssociation = BinaryAssociation(
    name="owner7",
    ends={
        Property(name="Table8", type=SimpleRDBMS_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
key9: BinaryAssociation = BinaryAssociation(
    name="key9",
    ends={
        Property(name="Key11", type=SimpleRDBMS_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column10", type=Key, multiplicity=Multiplicity(0, 9999))
    }
)
foreignKey12: BinaryAssociation = BinaryAssociation(
    name="foreignKey12",
    ends={
        Property(name="ForeignKey14", type=SimpleRDBMS_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column13", type=ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
owner15: BinaryAssociation = BinaryAssociation(
    name="owner15",
    ends={
        Property(name="Table16", type=SimpleRDBMS_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="key", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
column17: BinaryAssociation = BinaryAssociation(
    name="column17",
    ends={
        Property(name="Column19", type=SimpleRDBMS_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="key18", type=Column, multiplicity=Multiplicity(0, 9999))
    }
)
refersToOpposite20: BinaryAssociation = BinaryAssociation(
    name="refersToOpposite20",
    ends={
        Property(name="ForeignKey21", type=SimpleRDBMS_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="refersTo", type=ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
column22: BinaryAssociation = BinaryAssociation(
    name="column22",
    ends={
        Property(name="Column23", type=SimpleRDBMS_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKey", type=Column, multiplicity=Multiplicity(0, 9999))
    }
)
owner24: BinaryAssociation = BinaryAssociation(
    name="owner24",
    ends={
        Property(name="Table26", type=SimpleRDBMS_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKey25", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
refersTo27: BinaryAssociation = BinaryAssociation(
    name="refersTo27",
    ends={
        Property(name="Key28", type=SimpleRDBMS_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="refersToOpposite", type=Key, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_SimpleRDBMS_Schema_RModelElement = Generalization(general=RModelElement, specific=SimpleRDBMS_Schema)
gen_SimpleRDBMS_Table_RModelElement = Generalization(general=RModelElement, specific=SimpleRDBMS_Table)
gen_SimpleRDBMS_Column_RModelElement = Generalization(general=RModelElement, specific=SimpleRDBMS_Column)
gen_SimpleRDBMS_Key_RModelElement = Generalization(general=RModelElement, specific=SimpleRDBMS_Key)
gen_SimpleRDBMS_ForeignKey_RModelElement = Generalization(general=RModelElement, specific=SimpleRDBMS_ForeignKey)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={SimpleRDBMS_RModelElement, SimpleRDBMS_Schema, RModelElement, Table, SimpleRDBMS_Table, Schema, Column, Key, ForeignKey, SimpleRDBMS_Column, SimpleRDBMS_Key, SimpleRDBMS_ForeignKey},
    associations={tables0, schema1, column2, key3, foreignKey5, owner7, key9, foreignKey12, owner15, column17, refersToOpposite20, column22, owner24, refersTo27},
    generalizations={gen_SimpleRDBMS_Schema_RModelElement, gen_SimpleRDBMS_Table_RModelElement, gen_SimpleRDBMS_Column_RModelElement, gen_SimpleRDBMS_Key_RModelElement, gen_SimpleRDBMS_ForeignKey_RModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)