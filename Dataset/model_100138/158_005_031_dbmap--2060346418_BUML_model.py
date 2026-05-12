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
dbmap_DBMapData = Class(name="dbmap_DBMapData")
AbstractExternalData = Class(name="AbstractExternalData")
dbmap_VarTable = Class(name="dbmap_VarTable")
dbmap_AbstractDBDataMapTable = Class(name="dbmap_AbstractDBDataMapTable")
dbmap_AbstaceDBInOutTable = Class(name="dbmap_AbstaceDBInOutTable")
AbstractDBDataMapTable = Class(name="AbstractDBDataMapTable")
AbstaceDBInOutTable = Class(name="AbstaceDBInOutTable")
dbmap_FilterEntry = Class(name="dbmap_FilterEntry")
dbmap_InputTable = Class(name="dbmap_InputTable")
dbmap_OutputTable = Class(name="dbmap_OutputTable")
dbmap_DBMapperTableEntry = Class(name="dbmap_DBMapperTableEntry")

# dbmap_DBMapData class attributes and methods

# AbstractExternalData class attributes and methods

# dbmap_VarTable class attributes and methods

# dbmap_AbstractDBDataMapTable class attributes and methods
dbmap_AbstractDBDataMapTable_name: Property = Property(name="name", type=StringType)
dbmap_AbstractDBDataMapTable_minimized: Property = Property(name="minimized", type=BooleanType)
dbmap_AbstractDBDataMapTable_readonly: Property = Property(name="readonly", type=BooleanType)
dbmap_AbstractDBDataMapTable_tableName: Property = Property(name="tableName", type=StringType)
dbmap_AbstractDBDataMapTable.attributes={dbmap_AbstractDBDataMapTable_readonly, dbmap_AbstractDBDataMapTable_tableName, dbmap_AbstractDBDataMapTable_name, dbmap_AbstractDBDataMapTable_minimized}

# dbmap_AbstaceDBInOutTable class attributes and methods

# AbstractDBDataMapTable class attributes and methods

# AbstaceDBInOutTable class attributes and methods

# dbmap_FilterEntry class attributes and methods
dbmap_FilterEntry_name: Property = Property(name="name", type=StringType)
dbmap_FilterEntry_expression: Property = Property(name="expression", type=StringType)
dbmap_FilterEntry.attributes={dbmap_FilterEntry_name, dbmap_FilterEntry_expression}

# dbmap_InputTable class attributes and methods
dbmap_InputTable_joinType: Property = Property(name="joinType", type=StringType)
dbmap_InputTable_alias: Property = Property(name="alias", type=StringType)
dbmap_InputTable.attributes={dbmap_InputTable_joinType, dbmap_InputTable_alias}

# dbmap_OutputTable class attributes and methods

# dbmap_DBMapperTableEntry class attributes and methods
dbmap_DBMapperTableEntry_name: Property = Property(name="name", type=StringType)
dbmap_DBMapperTableEntry_expression: Property = Property(name="expression", type=StringType)
dbmap_DBMapperTableEntry_type: Property = Property(name="type", type=StringType)
dbmap_DBMapperTableEntry_nullable: Property = Property(name="nullable", type=BooleanType)
dbmap_DBMapperTableEntry_join: Property = Property(name="join", type=BooleanType)
dbmap_DBMapperTableEntry_operator: Property = Property(name="operator", type=StringType)
dbmap_DBMapperTableEntry.attributes={dbmap_DBMapperTableEntry_operator, dbmap_DBMapperTableEntry_nullable, dbmap_DBMapperTableEntry_type, dbmap_DBMapperTableEntry_name, dbmap_DBMapperTableEntry_join, dbmap_DBMapperTableEntry_expression}

# Relationships
VarTables0: BinaryAssociation = BinaryAssociation(
    name="VarTables0",
    ends={
        Property(name="dbmap_VarTable", type=dbmap_DBMapData, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmap_DBMapData", type=dbmap_VarTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
DBMapperTableEntries5: BinaryAssociation = BinaryAssociation(
    name="DBMapperTableEntries5",
    ends={
        Property(name="dbmap_DBMapperTableEntry", type=dbmap_AbstractDBDataMapTable, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmap_AbstractDBDataMapTable", type=dbmap_DBMapperTableEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
FilterEntries6: BinaryAssociation = BinaryAssociation(
    name="FilterEntries6",
    ends={
        Property(name="dbmap_FilterEntry", type=dbmap_OutputTable, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmap_OutputTable7", type=dbmap_FilterEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
InputTables1: BinaryAssociation = BinaryAssociation(
    name="InputTables1",
    ends={
        Property(name="dbmap_InputTable", type=dbmap_DBMapData, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmap_DBMapData2", type=dbmap_InputTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
OutputTables3: BinaryAssociation = BinaryAssociation(
    name="OutputTables3",
    ends={
        Property(name="dbmap_OutputTable", type=dbmap_DBMapData, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmap_DBMapData4", type=dbmap_OutputTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_dbmap_DBMapData_AbstractExternalData = Generalization(general=AbstractExternalData, specific=dbmap_DBMapData)
gen_dbmap_AbstaceDBInOutTable_AbstractDBDataMapTable = Generalization(general=AbstractDBDataMapTable, specific=dbmap_AbstaceDBInOutTable)
gen_dbmap_VarTable_AbstractDBDataMapTable = Generalization(general=AbstractDBDataMapTable, specific=dbmap_VarTable)
gen_dbmap_InputTable_AbstaceDBInOutTable = Generalization(general=AbstaceDBInOutTable, specific=dbmap_InputTable)
gen_dbmap_OutputTable_AbstaceDBInOutTable = Generalization(general=AbstaceDBInOutTable, specific=dbmap_OutputTable)

# Domain Model
domain_model = DomainModel(
    name="dbmap",
    types={dbmap_DBMapData, AbstractExternalData, dbmap_VarTable, dbmap_AbstractDBDataMapTable, dbmap_AbstaceDBInOutTable, AbstractDBDataMapTable, AbstaceDBInOutTable, dbmap_FilterEntry, dbmap_InputTable, dbmap_OutputTable, dbmap_DBMapperTableEntry},
    associations={VarTables0, DBMapperTableEntries5, FilterEntries6, InputTables1, OutputTables3},
    generalizations={gen_dbmap_DBMapData_AbstractExternalData, gen_dbmap_AbstaceDBInOutTable_AbstractDBDataMapTable, gen_dbmap_VarTable_AbstractDBDataMapTable, gen_dbmap_InputTable_AbstaceDBInOutTable, gen_dbmap_OutputTable_AbstaceDBInOutTable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)