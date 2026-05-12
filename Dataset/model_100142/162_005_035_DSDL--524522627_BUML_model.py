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
dSDL_Attribute = Class(name="dSDL_Attribute")
dSDL_Type = Class(name="dSDL_Type")
dSDL_Property = Class(name="dSDL_Property")
dSDL_Integer = Class(name="dSDL_Integer")
Type = Class(name="Type")
dSDL_Varchar = Class(name="dSDL_Varchar")
dSDL_Text = Class(name="dSDL_Text")
dSDL_DateTime = Class(name="dSDL_DateTime")
dSDL_PrimaryKey = Class(name="dSDL_PrimaryKey")
Property_ = Class(name="Property")
dSDL_AutoIncrement = Class(name="dSDL_AutoIncrement")
dSDL_Database = Class(name="dSDL_Database")
dSDL_Nullable = Class(name="dSDL_Nullable")
dSDL_ForeignKey = Class(name="dSDL_ForeignKey")
dSDL_Table = Class(name="dSDL_Table")

# dSDL_Attribute class attributes and methods
dSDL_Attribute_attributeName: Property = Property(name="attributeName", type=StringType)
dSDL_Attribute.attributes={dSDL_Attribute_attributeName}

# dSDL_Type class attributes and methods

# dSDL_Property class attributes and methods

# dSDL_Integer class attributes and methods
dSDL_Integer_integer: Property = Property(name="integer", type=StringType)
dSDL_Integer_length: Property = Property(name="length", type=IntegerType)
dSDL_Integer.attributes={dSDL_Integer_integer, dSDL_Integer_length}

# Type class attributes and methods

# dSDL_Varchar class attributes and methods
dSDL_Varchar_varchar: Property = Property(name="varchar", type=StringType)
dSDL_Varchar_length: Property = Property(name="length", type=IntegerType)
dSDL_Varchar.attributes={dSDL_Varchar_length, dSDL_Varchar_varchar}

# dSDL_Text class attributes and methods
dSDL_Text_text: Property = Property(name="text", type=StringType)
dSDL_Text.attributes={dSDL_Text_text}

# dSDL_DateTime class attributes and methods
dSDL_DateTime_date: Property = Property(name="date", type=StringType)
dSDL_DateTime.attributes={dSDL_DateTime_date}

# dSDL_PrimaryKey class attributes and methods
dSDL_PrimaryKey_primaryKey: Property = Property(name="primaryKey", type=BooleanType)
dSDL_PrimaryKey.attributes={dSDL_PrimaryKey_primaryKey}

# Property class attributes and methods

# dSDL_AutoIncrement class attributes and methods
dSDL_AutoIncrement_autoIncrement: Property = Property(name="autoIncrement", type=BooleanType)
dSDL_AutoIncrement.attributes={dSDL_AutoIncrement_autoIncrement}

# dSDL_Database class attributes and methods
dSDL_Database_name: Property = Property(name="name", type=StringType)
dSDL_Database.attributes={dSDL_Database_name}

# dSDL_Nullable class attributes and methods
dSDL_Nullable_nullable: Property = Property(name="nullable", type=BooleanType)
dSDL_Nullable.attributes={dSDL_Nullable_nullable}

# dSDL_ForeignKey class attributes and methods
dSDL_ForeignKey_tableName: Property = Property(name="tableName", type=StringType)
dSDL_ForeignKey_attributeName: Property = Property(name="attributeName", type=StringType)
dSDL_ForeignKey.attributes={dSDL_ForeignKey_attributeName, dSDL_ForeignKey_tableName}

# dSDL_Table class attributes and methods
dSDL_Table_name: Property = Property(name="name", type=StringType)
dSDL_Table.attributes={dSDL_Table_name}

# Relationships
attribute1: BinaryAssociation = BinaryAssociation(
    name="attribute1",
    ends={
        Property(name="dSDL_Attribute", type=dSDL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="dSDL_Table2", type=dSDL_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type3: BinaryAssociation = BinaryAssociation(
    name="type3",
    ends={
        Property(name="dSDL_Type", type=dSDL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="dSDL_Attribute4", type=dSDL_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
property5: BinaryAssociation = BinaryAssociation(
    name="property5",
    ends={
        Property(name="dSDL_Property", type=dSDL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="dSDL_Attribute6", type=dSDL_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table0: BinaryAssociation = BinaryAssociation(
    name="table0",
    ends={
        Property(name="dSDL_Table", type=dSDL_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="dSDL_Database", type=dSDL_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_dSDL_Integer_Type = Generalization(general=Type, specific=dSDL_Integer)
gen_dSDL_Varchar_Type = Generalization(general=Type, specific=dSDL_Varchar)
gen_dSDL_Text_Type = Generalization(general=Type, specific=dSDL_Text)
gen_dSDL_DateTime_Type = Generalization(general=Type, specific=dSDL_DateTime)
gen_dSDL_PrimaryKey_Property = Generalization(general=Property_, specific=dSDL_PrimaryKey)
gen_dSDL_AutoIncrement_Property = Generalization(general=Property_, specific=dSDL_AutoIncrement)
gen_dSDL_Nullable_Property = Generalization(general=Property_, specific=dSDL_Nullable)
gen_dSDL_ForeignKey_Property = Generalization(general=Property_, specific=dSDL_ForeignKey)

# Domain Model
domain_model = DomainModel(
    name="dSDL",
    types={dSDL_Attribute, dSDL_Type, dSDL_Property, dSDL_Integer, Type, dSDL_Varchar, dSDL_Text, dSDL_DateTime, dSDL_PrimaryKey, Property_, dSDL_AutoIncrement, dSDL_Database, dSDL_Nullable, dSDL_ForeignKey, dSDL_Table},
    associations={attribute1, type3, property5, table0},
    generalizations={gen_dSDL_Integer_Type, gen_dSDL_Varchar_Type, gen_dSDL_Text_Type, gen_dSDL_DateTime_Type, gen_dSDL_PrimaryKey_Property, gen_dSDL_AutoIncrement_Property, gen_dSDL_Nullable_Property, gen_dSDL_ForeignKey_Property},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)