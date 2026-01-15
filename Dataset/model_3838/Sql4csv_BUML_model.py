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
sql4csv_SQL4CSV = Class(name="sql4csv::SQL4CSV")
sql4csv_Program = Class(name="sql4csv::Program")
sql4csv_Query = Class(name="sql4csv::Query")
sql4csv_Column = Class(name="sql4csv::Column")
sql4csv_Condition = Class(name="sql4csv::Condition")
sql4csv_Equality = Class(name="sql4csv::Equality")
Condition = Class(name="Condition")
sql4csv_EObject = Class(name="sql4csv::EObject")
sql4csv_Table = Class(name="sql4csv::Table")
sql4csv_ColumnEquality = Class(name="sql4csv::ColumnEquality")
sql4csv_ValueEquality = Class(name="sql4csv::ValueEquality")
sql4csv_AndCondition = Class(name="sql4csv::AndCondition")
BinaryCondition = Class(name="BinaryCondition")
sql4csv_OrCondition = Class(name="sql4csv::OrCondition")
sql4csv_BinaryCondition = Class(name="sql4csv::BinaryCondition")

# sql4csv_SQL4CSV class attributes and methods

# sql4csv_Program class attributes and methods

# sql4csv_Query class attributes and methods

# sql4csv_Column class attributes and methods
sql4csv_Column_name: Property = Property(name="name", type=StringType)
sql4csv_Column.attributes={sql4csv_Column_name}

# sql4csv_Condition class attributes and methods

# sql4csv_Equality class attributes and methods

# Condition class attributes and methods

# sql4csv_EObject class attributes and methods

# sql4csv_Table class attributes and methods
sql4csv_Table_name: Property = Property(name="name", type=StringType)
sql4csv_Table.attributes={sql4csv_Table_name}

# sql4csv_ColumnEquality class attributes and methods

# sql4csv_ValueEquality class attributes and methods
sql4csv_ValueEquality_right: Property = Property(name="right", type=StringType)
sql4csv_ValueEquality.attributes={sql4csv_ValueEquality_right}

# sql4csv_AndCondition class attributes and methods

# BinaryCondition class attributes and methods

# sql4csv_OrCondition class attributes and methods

# sql4csv_BinaryCondition class attributes and methods

# Relationships
program0: BinaryAssociation = BinaryAssociation(
    name="program0",
    ends={
        Property(name="sql4csv_Program", type=sql4csv_SQL4CSV, multiplicity=Multiplicity(1, 1)),
        Property(name="sql4csv_SQL4CSV", type=sql4csv_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
queries1: BinaryAssociation = BinaryAssociation(
    name="queries1",
    ends={
        Property(name="sql4csv_Query", type=sql4csv_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="sql4csv_Program2", type=sql4csv_Query, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables10: BinaryAssociation = BinaryAssociation(
    name="tables10",
    ends={
        Property(name="sql4csv_Table12", type=sql4csv_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="sql4csv_Query11", type=sql4csv_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditions13: BinaryAssociation = BinaryAssociation(
    name="conditions13",
    ends={
        Property(name="sql4csv_Condition", type=sql4csv_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="sql4csv_Query14", type=sql4csv_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
table15: BinaryAssociation = BinaryAssociation(
    name="table15",
    ends={
        Property(name="sql4csv_Table17", type=sql4csv_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="sql4csv_Column16", type=sql4csv_Table, multiplicity=Multiplicity(0, 1))
    }
)
left18: BinaryAssociation = BinaryAssociation(
    name="left18",
    ends={
        Property(name="sql4csv_Column19", type=sql4csv_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="sql4csv_Equality", type=sql4csv_Column, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
column3: BinaryAssociation = BinaryAssociation(
    name="column3",
    ends={
        Property(name="sql4csv_Column", type=sql4csv_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="sql4csv_Query4", type=sql4csv_Column, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columns5: BinaryAssociation = BinaryAssociation(
    name="columns5",
    ends={
        Property(name="sql4csv_Column7", type=sql4csv_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="sql4csv_Query6", type=sql4csv_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table8: BinaryAssociation = BinaryAssociation(
    name="table8",
    ends={
        Property(name="sql4csv_Table", type=sql4csv_Query, multiplicity=Multiplicity(1, 1)),
        Property(name="sql4csv_Query9", type=sql4csv_Table, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right24: BinaryAssociation = BinaryAssociation(
    name="right24",
    ends={
        Property(name="sql4csv_Condition26", type=sql4csv_BinaryCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sql4csv_BinaryCondition25", type=sql4csv_Condition, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right27: BinaryAssociation = BinaryAssociation(
    name="right27",
    ends={
        Property(name="sql4csv_Column28", type=sql4csv_ColumnEquality, multiplicity=Multiplicity(1, 1)),
        Property(name="sql4csv_ColumnEquality", type=sql4csv_Column, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right20: BinaryAssociation = BinaryAssociation(
    name="right20",
    ends={
        Property(name="sql4csv_EObject", type=sql4csv_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="sql4csv_Equality21", type=sql4csv_EObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left22: BinaryAssociation = BinaryAssociation(
    name="left22",
    ends={
        Property(name="sql4csv_Equality23", type=sql4csv_BinaryCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="sql4csv_BinaryCondition", type=sql4csv_Equality, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_sql4csv_Equality_Condition = Generalization(general=Condition, specific=sql4csv_Equality)
gen_sql4csv_AndCondition_BinaryCondition = Generalization(general=BinaryCondition, specific=sql4csv_AndCondition)
gen_sql4csv_OrCondition_BinaryCondition = Generalization(general=BinaryCondition, specific=sql4csv_OrCondition)
gen_sql4csv_BinaryCondition_Condition = Generalization(general=Condition, specific=sql4csv_BinaryCondition)

# Domain Model
domain_model = DomainModel(
    name="sql4csv",
    types={sql4csv_SQL4CSV, sql4csv_Program, sql4csv_Query, sql4csv_Column, sql4csv_Condition, sql4csv_Equality, Condition, sql4csv_EObject, sql4csv_Table, sql4csv_ColumnEquality, sql4csv_ValueEquality, sql4csv_AndCondition, BinaryCondition, sql4csv_OrCondition, sql4csv_BinaryCondition},
    associations={program0, queries1, tables10, conditions13, table15, left18, column3, columns5, table8, right24, right27, right20, left22},
    generalizations={gen_sql4csv_Equality_Condition, gen_sql4csv_AndCondition_BinaryCondition, gen_sql4csv_OrCondition_BinaryCondition, gen_sql4csv_BinaryCondition_Condition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)