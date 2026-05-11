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
MySQL_NamedElement = Class(name="MySQL_NamedElement", is_abstract=True)
MySQL_DataBase = Class(name="MySQL_DataBase")
NamedElement = Class(name="NamedElement")
Table = Class(name="Table")
MySQL_Table = Class(name="MySQL_Table")
Column = Class(name="Column")
DataBase = Class(name="DataBase")
MySQL_Column = Class(name="MySQL_Column")
MySQL_EnumColumn = Class(name="MySQL_EnumColumn")
EnumSet = Class(name="EnumSet")
MySQL_EnumSet = Class(name="MySQL_EnumSet")
EnumItem = Class(name="EnumItem")
MySQL_EnumItem = Class(name="MySQL_EnumItem")
MySQL_ForeignColumn = Class(name="MySQL_ForeignColumn")
MySQL_IntegerColumn = Class(name="MySQL_IntegerColumn")

# MySQL_NamedElement class attributes and methods
MySQL_NamedElement_name: Property = Property(name="name", type=StringType)
MySQL_NamedElement.attributes={MySQL_NamedElement_name}

# MySQL_DataBase class attributes and methods

# NamedElement class attributes and methods

# Table class attributes and methods

# MySQL_Table class attributes and methods

# Column class attributes and methods

# DataBase class attributes and methods

# MySQL_Column class attributes and methods
MySQL_Column_type: Property = Property(name="type", type=StringType)
MySQL_Column_isPrimaryKey: Property = Property(name="isPrimaryKey", type=StringType)
MySQL_Column_defaultValue: Property = Property(name="defaultValue", type=StringType)
MySQL_Column_comment: Property = Property(name="comment", type=StringType)
MySQL_Column.attributes={MySQL_Column_type, MySQL_Column_comment, MySQL_Column_isPrimaryKey, MySQL_Column_defaultValue}

# MySQL_EnumColumn class attributes and methods

# EnumSet class attributes and methods

# MySQL_EnumSet class attributes and methods

# EnumItem class attributes and methods

# MySQL_EnumItem class attributes and methods

# MySQL_ForeignColumn class attributes and methods

# MySQL_IntegerColumn class attributes and methods
MySQL_IntegerColumn_isAutoIncrement: Property = Property(name="isAutoIncrement", type=StringType)
MySQL_IntegerColumn.attributes={MySQL_IntegerColumn_isAutoIncrement}

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="Table", type=MySQL_DataBase, multiplicity=Multiplicity(1, 1)),
        Property(name="database", type=Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns1: BinaryAssociation = BinaryAssociation(
    name="columns1",
    ends={
        Property(name="Column", type=MySQL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
database2: BinaryAssociation = BinaryAssociation(
    name="database2",
    ends={
        Property(name="DataBase", type=MySQL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=DataBase, multiplicity=Multiplicity(1, 1))
    }
)
enumSet5: BinaryAssociation = BinaryAssociation(
    name="enumSet5",
    ends={
        Property(name="EnumSet", type=MySQL_EnumColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="MySQL_EnumColumn", type=EnumSet, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
enumItems6: BinaryAssociation = BinaryAssociation(
    name="enumItems6",
    ends={
        Property(name="EnumItem", type=MySQL_EnumSet, multiplicity=Multiplicity(1, 1)),
        Property(name="enumSet", type=EnumItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumSet7: BinaryAssociation = BinaryAssociation(
    name="enumSet7",
    ends={
        Property(name="EnumSet8", type=MySQL_EnumItem, multiplicity=Multiplicity(1, 1)),
        Property(name="enumItems", type=EnumSet, multiplicity=Multiplicity(1, 1))
    }
)
refers9: BinaryAssociation = BinaryAssociation(
    name="refers9",
    ends={
        Property(name="Table10", type=MySQL_ForeignColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="MySQL_ForeignColumn", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
table3: BinaryAssociation = BinaryAssociation(
    name="table3",
    ends={
        Property(name="Table4", type=MySQL_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=Table, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_MySQL_DataBase_NamedElement = Generalization(general=NamedElement, specific=MySQL_DataBase)
gen_MySQL_Table_NamedElement = Generalization(general=NamedElement, specific=MySQL_Table)
gen_MySQL_Column_NamedElement = Generalization(general=NamedElement, specific=MySQL_Column)
gen_MySQL_EnumColumn_Column = Generalization(general=Column, specific=MySQL_EnumColumn)
gen_MySQL_EnumItem_NamedElement = Generalization(general=NamedElement, specific=MySQL_EnumItem)
gen_MySQL_ForeignColumn_Column = Generalization(general=Column, specific=MySQL_ForeignColumn)
gen_MySQL_IntegerColumn_Column = Generalization(general=Column, specific=MySQL_IntegerColumn)

# Domain Model
domain_model = DomainModel(
    name="MySQL",
    types={MySQL_NamedElement, MySQL_DataBase, NamedElement, Table, MySQL_Table, Column, DataBase, MySQL_Column, MySQL_EnumColumn, EnumSet, MySQL_EnumSet, EnumItem, MySQL_EnumItem, MySQL_ForeignColumn, MySQL_IntegerColumn},
    associations={tables0, columns1, database2, enumSet5, enumItems6, enumSet7, refers9, table3},
    generalizations={gen_MySQL_DataBase_NamedElement, gen_MySQL_Table_NamedElement, gen_MySQL_Column_NamedElement, gen_MySQL_EnumColumn_Column, gen_MySQL_EnumItem_NamedElement, gen_MySQL_ForeignColumn_Column, gen_MySQL_IntegerColumn_Column},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)