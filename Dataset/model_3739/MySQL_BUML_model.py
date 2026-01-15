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
MySQL_Table = Class(name="MySQL::Table")
Column = Class(name="Column")
DataBase = Class(name="DataBase")
MySQL_Column = Class(name="MySQL::Column")
MySQL_NamedElement = Class(name="MySQL::NamedElement", is_abstract=True)
MySQL_DataBase = Class(name="MySQL::DataBase")
NamedElement = Class(name="NamedElement")
Table = Class(name="Table")
MySQL_EnumSet = Class(name="MySQL::EnumSet")
EnumItem = Class(name="EnumItem")
MySQL_EnumItem = Class(name="MySQL::EnumItem")
MySQL_ForeignColumn = Class(name="MySQL::ForeignColumn")
MySQL_IntegerColumn = Class(name="MySQL::IntegerColumn")
MySQL_EnumColumn = Class(name="MySQL::EnumColumn")
EnumSet = Class(name="EnumSet")

# MySQL_Table class attributes and methods

# Column class attributes and methods

# DataBase class attributes and methods

# MySQL_Column class attributes and methods
MySQL_Column_type: Property = Property(name="type", type=StringType)
MySQL_Column_isPrimaryKey: Property = Property(name="isPrimaryKey", type=StringType)
MySQL_Column_defaultValue: Property = Property(name="defaultValue", type=StringType)
MySQL_Column_comment: Property = Property(name="comment", type=StringType)
MySQL_Column.attributes={MySQL_Column_type, MySQL_Column_isPrimaryKey, MySQL_Column_comment, MySQL_Column_defaultValue}

# MySQL_NamedElement class attributes and methods
MySQL_NamedElement_name: Property = Property(name="name", type=StringType)
MySQL_NamedElement.attributes={MySQL_NamedElement_name}

# MySQL_DataBase class attributes and methods

# NamedElement class attributes and methods

# Table class attributes and methods

# MySQL_EnumSet class attributes and methods

# EnumItem class attributes and methods

# MySQL_EnumItem class attributes and methods

# MySQL_ForeignColumn class attributes and methods

# MySQL_IntegerColumn class attributes and methods
MySQL_IntegerColumn_isAutoIncrement: Property = Property(name="isAutoIncrement", type=StringType)
MySQL_IntegerColumn.attributes={MySQL_IntegerColumn_isAutoIncrement}

# MySQL_EnumColumn class attributes and methods

# EnumSet class attributes and methods

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="1", type=Table, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="#", type=MySQL_DataBase, multiplicity=Multiplicity(1, 1))
    }
)
columns1: BinaryAssociation = BinaryAssociation(
    name="columns1",
    ends={
        Property(name="#3", type=MySQL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
database4: BinaryAssociation = BinaryAssociation(
    name="database4",
    ends={
        Property(name="#6", type=MySQL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="15", type=DataBase, multiplicity=Multiplicity(1, 1))
    }
)
enumItems11: BinaryAssociation = BinaryAssociation(
    name="enumItems11",
    ends={
        Property(name="#13", type=MySQL_EnumSet, multiplicity=Multiplicity(1, 1)),
        Property(name="112", type=EnumItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumSet14: BinaryAssociation = BinaryAssociation(
    name="enumSet14",
    ends={
        Property(name="#16", type=MySQL_EnumItem, multiplicity=Multiplicity(1, 1)),
        Property(name="115", type=EnumSet, multiplicity=Multiplicity(1, 1))
    }
)
refers17: BinaryAssociation = BinaryAssociation(
    name="refers17",
    ends={
        Property(name="Table", type=MySQL_ForeignColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="MySQL_ForeignColumn", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
table7: BinaryAssociation = BinaryAssociation(
    name="table7",
    ends={
        Property(name="#9", type=MySQL_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="18", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
enumSet10: BinaryAssociation = BinaryAssociation(
    name="enumSet10",
    ends={
        Property(name="EnumSet", type=MySQL_EnumColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="MySQL_EnumColumn", type=EnumSet, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_MySQL_Table_NamedElement = Generalization(general=NamedElement, specific=MySQL_Table)
gen_MySQL_Column_NamedElement = Generalization(general=NamedElement, specific=MySQL_Column)
gen_MySQL_DataBase_NamedElement = Generalization(general=NamedElement, specific=MySQL_DataBase)
gen_MySQL_EnumItem_NamedElement = Generalization(general=NamedElement, specific=MySQL_EnumItem)
gen_MySQL_ForeignColumn_Column = Generalization(general=Column, specific=MySQL_ForeignColumn)
gen_MySQL_IntegerColumn_Column = Generalization(general=Column, specific=MySQL_IntegerColumn)
gen_MySQL_EnumColumn_Column = Generalization(general=Column, specific=MySQL_EnumColumn)

# Domain Model
domain_model = DomainModel(
    name="MySQL",
    types={MySQL_Table, Column, DataBase, MySQL_Column, MySQL_NamedElement, MySQL_DataBase, NamedElement, Table, MySQL_EnumSet, EnumItem, MySQL_EnumItem, MySQL_ForeignColumn, MySQL_IntegerColumn, MySQL_EnumColumn, EnumSet},
    associations={tables0, columns1, database4, enumItems11, enumSet14, refers17, table7, enumSet10},
    generalizations={gen_MySQL_Table_NamedElement, gen_MySQL_Column_NamedElement, gen_MySQL_DataBase_NamedElement, gen_MySQL_EnumItem_NamedElement, gen_MySQL_ForeignColumn_Column, gen_MySQL_IntegerColumn_Column, gen_MySQL_EnumColumn_Column},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)