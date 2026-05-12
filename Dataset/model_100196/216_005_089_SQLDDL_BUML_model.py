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
SQLDDL_Database = Class(name="SQLDDL_Database")
NamedElement = Class(name="NamedElement")
Table = Class(name="Table")
SQLDDL_Table = Class(name="SQLDDL_Table")
Database = Class(name="Database")
SQLDDL_LocatedElement = Class(name="SQLDDL_LocatedElement", is_abstract=True)
SQLDDL_NamedElement = Class(name="SQLDDL_NamedElement", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
SQLDDL_TableElement = Class(name="SQLDDL_TableElement", is_abstract=True)
SQLDDL_Column = Class(name="SQLDDL_Column")
Type = Class(name="Type")
ForeignKey = Class(name="ForeignKey")
TableElement = Class(name="TableElement")
Parameter_ = Class(name="Parameter")
Column = Class(name="Column")
SQLDDL_SimpleKey = Class(name="SQLDDL_SimpleKey")
SQLDDL_PrimaryKey = Class(name="SQLDDL_PrimaryKey")
SQLDDL_ForeignKey = Class(name="SQLDDL_ForeignKey")
Value = Class(name="Value")
Key = Class(name="Key")
SQLDDL_Key = Class(name="SQLDDL_Key", is_abstract=True)
SQLDDL_Parameter = Class(name="SQLDDL_Parameter")
SQLDDL_Value = Class(name="SQLDDL_Value", is_abstract=True)
SQLDDL_IntegerVal = Class(name="SQLDDL_IntegerVal")
SQLDDL_NullVal = Class(name="SQLDDL_NullVal")
SQLDDL_Type = Class(name="SQLDDL_Type")
SQLDDL_StringVal = Class(name="SQLDDL_StringVal")

# SQLDDL_Database class attributes and methods

# NamedElement class attributes and methods

# Table class attributes and methods

# SQLDDL_Table class attributes and methods

# Database class attributes and methods

# SQLDDL_LocatedElement class attributes and methods
SQLDDL_LocatedElement_location: Property = Property(name="location", type=StringType)
SQLDDL_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
SQLDDL_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
SQLDDL_LocatedElement.attributes={SQLDDL_LocatedElement_location, SQLDDL_LocatedElement_commentsBefore, SQLDDL_LocatedElement_commentsAfter}

# SQLDDL_NamedElement class attributes and methods
SQLDDL_NamedElement_name: Property = Property(name="name", type=StringType)
SQLDDL_NamedElement.attributes={SQLDDL_NamedElement_name}

# LocatedElement class attributes and methods

# SQLDDL_TableElement class attributes and methods

# SQLDDL_Column class attributes and methods
SQLDDL_Column_name: Property = Property(name="name", type=StringType)
SQLDDL_Column_canBeNull: Property = Property(name="canBeNull", type=StringType)
SQLDDL_Column.attributes={SQLDDL_Column_name, SQLDDL_Column_canBeNull}

# Type class attributes and methods

# ForeignKey class attributes and methods

# TableElement class attributes and methods

# Parameter class attributes and methods

# Column class attributes and methods

# SQLDDL_SimpleKey class attributes and methods

# SQLDDL_PrimaryKey class attributes and methods

# SQLDDL_ForeignKey class attributes and methods

# Value class attributes and methods

# Key class attributes and methods

# SQLDDL_Key class attributes and methods
SQLDDL_Key_isUnique: Property = Property(name="isUnique", type=StringType)
SQLDDL_Key_name: Property = Property(name="name", type=StringType)
SQLDDL_Key.attributes={SQLDDL_Key_name, SQLDDL_Key_isUnique}

# SQLDDL_Parameter class attributes and methods

# SQLDDL_Value class attributes and methods

# SQLDDL_IntegerVal class attributes and methods
SQLDDL_IntegerVal_value: Property = Property(name="value", type=StringType)
SQLDDL_IntegerVal.attributes={SQLDDL_IntegerVal_value}

# SQLDDL_NullVal class attributes and methods

# SQLDDL_Type class attributes and methods
SQLDDL_Type_length: Property = Property(name="length", type=StringType)
SQLDDL_Type_isUnsigned: Property = Property(name="isUnsigned", type=StringType)
SQLDDL_Type.attributes={SQLDDL_Type_length, SQLDDL_Type_isUnsigned}

# SQLDDL_StringVal class attributes and methods
SQLDDL_StringVal_value: Property = Property(name="value", type=StringType)
SQLDDL_StringVal.attributes={SQLDDL_StringVal_value}

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="Table", type=SQLDDL_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="database", type=Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
database1: BinaryAssociation = BinaryAssociation(
    name="database1",
    ends={
        Property(name="Database", type=SQLDDL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=Database, multiplicity=Multiplicity(1, 1))
    }
)
table6: BinaryAssociation = BinaryAssociation(
    name="table6",
    ends={
        Property(name="Table7", type=SQLDDL_TableElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
referencedBy8: BinaryAssociation = BinaryAssociation(
    name="referencedBy8",
    ends={
        Property(name="ForeignKey9", type=SQLDDL_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="referencedColumns", type=ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
type10: BinaryAssociation = BinaryAssociation(
    name="type10",
    ends={
        Property(name="Type", type=SQLDDL_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="SQLDDL_Column", type=Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referencedBy2: BinaryAssociation = BinaryAssociation(
    name="referencedBy2",
    ends={
        Property(name="ForeignKey", type=SQLDDL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="referencedTable", type=ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
elements3: BinaryAssociation = BinaryAssociation(
    name="elements3",
    ends={
        Property(name="TableElement", type=SQLDDL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=TableElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters4: BinaryAssociation = BinaryAssociation(
    name="parameters4",
    ends={
        Property(name="Parameter", type=SQLDDL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table5", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns14: BinaryAssociation = BinaryAssociation(
    name="columns14",
    ends={
        Property(name="Column", type=SQLDDL_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="keys", type=Column, multiplicity=Multiplicity(1, 9999))
    }
)
default11: BinaryAssociation = BinaryAssociation(
    name="default11",
    ends={
        Property(name="Value", type=SQLDDL_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="SQLDDL_Column12", type=Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
keys13: BinaryAssociation = BinaryAssociation(
    name="keys13",
    ends={
        Property(name="Key", type=SQLDDL_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=Key, multiplicity=Multiplicity(0, 9999))
    }
)
table20: BinaryAssociation = BinaryAssociation(
    name="table20",
    ends={
        Property(name="Table21", type=SQLDDL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
value22: BinaryAssociation = BinaryAssociation(
    name="value22",
    ends={
        Property(name="Value23", type=SQLDDL_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="SQLDDL_Parameter", type=Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referencedTable15: BinaryAssociation = BinaryAssociation(
    name="referencedTable15",
    ends={
        Property(name="Table16", type=SQLDDL_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="referencedBy", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
referencedColumns17: BinaryAssociation = BinaryAssociation(
    name="referencedColumns17",
    ends={
        Property(name="Column19", type=SQLDDL_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="referencedBy18", type=Column, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_SQLDDL_NamedElement_LocatedElement = Generalization(general=LocatedElement, specific=SQLDDL_NamedElement)
gen_SQLDDL_Database_NamedElement = Generalization(general=NamedElement, specific=SQLDDL_Database)
gen_SQLDDL_Table_NamedElement = Generalization(general=NamedElement, specific=SQLDDL_Table)
gen_SQLDDL_TableElement_LocatedElement = Generalization(general=LocatedElement, specific=SQLDDL_TableElement)
gen_SQLDDL_Column_TableElement = Generalization(general=TableElement, specific=SQLDDL_Column)
gen_SQLDDL_SimpleKey_Key = Generalization(general=Key, specific=SQLDDL_SimpleKey)
gen_SQLDDL_PrimaryKey_Key = Generalization(general=Key, specific=SQLDDL_PrimaryKey)
gen_SQLDDL_ForeignKey_Key = Generalization(general=Key, specific=SQLDDL_ForeignKey)
gen_SQLDDL_Key_TableElement = Generalization(general=TableElement, specific=SQLDDL_Key)
gen_SQLDDL_Parameter_NamedElement = Generalization(general=NamedElement, specific=SQLDDL_Parameter)
gen_SQLDDL_Value_LocatedElement = Generalization(general=LocatedElement, specific=SQLDDL_Value)
gen_SQLDDL_IntegerVal_Value = Generalization(general=Value, specific=SQLDDL_IntegerVal)
gen_SQLDDL_NullVal_Value = Generalization(general=Value, specific=SQLDDL_NullVal)
gen_SQLDDL_Type_NamedElement = Generalization(general=NamedElement, specific=SQLDDL_Type)
gen_SQLDDL_StringVal_Value = Generalization(general=Value, specific=SQLDDL_StringVal)

# Domain Model
domain_model = DomainModel(
    name="SQLDDL",
    types={SQLDDL_Database, NamedElement, Table, SQLDDL_Table, Database, SQLDDL_LocatedElement, SQLDDL_NamedElement, LocatedElement, SQLDDL_TableElement, SQLDDL_Column, Type, ForeignKey, TableElement, Parameter_, Column, SQLDDL_SimpleKey, SQLDDL_PrimaryKey, SQLDDL_ForeignKey, Value, Key, SQLDDL_Key, SQLDDL_Parameter, SQLDDL_Value, SQLDDL_IntegerVal, SQLDDL_NullVal, SQLDDL_Type, SQLDDL_StringVal},
    associations={tables0, database1, table6, referencedBy8, type10, referencedBy2, elements3, parameters4, columns14, default11, keys13, table20, value22, referencedTable15, referencedColumns17},
    generalizations={gen_SQLDDL_NamedElement_LocatedElement, gen_SQLDDL_Database_NamedElement, gen_SQLDDL_Table_NamedElement, gen_SQLDDL_TableElement_LocatedElement, gen_SQLDDL_Column_TableElement, gen_SQLDDL_SimpleKey_Key, gen_SQLDDL_PrimaryKey_Key, gen_SQLDDL_ForeignKey_Key, gen_SQLDDL_Key_TableElement, gen_SQLDDL_Parameter_NamedElement, gen_SQLDDL_Value_LocatedElement, gen_SQLDDL_IntegerVal_Value, gen_SQLDDL_NullVal_Value, gen_SQLDDL_Type_NamedElement, gen_SQLDDL_StringVal_Value},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)