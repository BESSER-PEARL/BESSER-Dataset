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
database_Table = Class(name="database::Table")
RefTable = Class(name="RefTable")
database_RefColumn = Class(name="database::RefColumn", is_abstract=True)
database_RefPKey = Class(name="database::RefPKey", is_abstract=True)
database_FKey = Class(name="database::FKey")
RefFKey = Class(name="RefFKey")
database_Column = Class(name="database::Column")
database_RefTable = Class(name="database::RefTable", is_abstract=True)
RefColumn = Class(name="RefColumn")
database_RefFKey = Class(name="database::RefFKey", is_abstract=True)
database_RefProcedure = Class(name="database::RefProcedure", is_abstract=True)
database_RefDatabase = Class(name="database::RefDatabase", is_abstract=True)
database_Procedure = Class(name="database::Procedure")
RefProcedure = Class(name="RefProcedure")
database_RefParameter = Class(name="database::RefParameter", is_abstract=True)
database_Parameter = Class(name="database::Parameter")
RefParameter = Class(name="RefParameter")
database_RefType = Class(name="database::RefType", is_abstract=True)
database_Database = Class(name="database::Database")
RefDatabase = Class(name="RefDatabase")
database_PKey = Class(name="database::PKey")
RefPKey = Class(name="RefPKey")
database_Type = Class(name="database::Type")
RefType = Class(name="RefType")

# database_Table class attributes and methods
database_Table_name: Property = Property(name="name", type=StringType)
database_Table.attributes={database_Table_name}

# RefTable class attributes and methods

# database_RefColumn class attributes and methods

# database_RefPKey class attributes and methods

# database_FKey class attributes and methods
database_FKey_name: Property = Property(name="name", type=StringType)
database_FKey.attributes={database_FKey_name}

# RefFKey class attributes and methods

# database_Column class attributes and methods
database_Column_name: Property = Property(name="name", type=StringType)
database_Column.attributes={database_Column_name}

# database_RefTable class attributes and methods

# RefColumn class attributes and methods

# database_RefFKey class attributes and methods

# database_RefProcedure class attributes and methods

# database_RefDatabase class attributes and methods

# database_Procedure class attributes and methods
database_Procedure_name: Property = Property(name="name", type=StringType)
database_Procedure.attributes={database_Procedure_name}

# RefProcedure class attributes and methods

# database_RefParameter class attributes and methods

# database_Parameter class attributes and methods
database_Parameter_name: Property = Property(name="name", type=StringType)
database_Parameter.attributes={database_Parameter_name}

# RefParameter class attributes and methods

# database_RefType class attributes and methods

# database_Database class attributes and methods
database_Database_name: Property = Property(name="name", type=StringType)
database_Database.attributes={database_Database_name}

# RefDatabase class attributes and methods

# database_PKey class attributes and methods
database_PKey_name: Property = Property(name="name", type=StringType)
database_PKey.attributes={database_PKey_name}

# RefPKey class attributes and methods

# database_Type class attributes and methods
database_Type_name: Property = Property(name="name", type=StringType)
database_Type.attributes={database_Type_name}

# RefType class attributes and methods

# Relationships
columns0: BinaryAssociation = BinaryAssociation(
    name="columns0",
    ends={
        Property(name="database_RefColumn", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Table", type=database_RefColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pkeys1: BinaryAssociation = BinaryAssociation(
    name="pkeys1",
    ends={
        Property(name="database_RefPKey", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Table2", type=database_RefPKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns5: BinaryAssociation = BinaryAssociation(
    name="columns5",
    ends={
        Property(name="database_Column", type=database_FKey, multiplicity=Multiplicity(1, 1)),
        Property(name="database_FKey", type=database_Column, multiplicity=Multiplicity(1, 9999))
    }
)
reference6: BinaryAssociation = BinaryAssociation(
    name="reference6",
    ends={
        Property(name="database_RefTable", type=database_FKey, multiplicity=Multiplicity(1, 1)),
        Property(name="database_FKey7", type=database_RefTable, multiplicity=Multiplicity(1, 1))
    }
)
fkeys3: BinaryAssociation = BinaryAssociation(
    name="fkeys3",
    ends={
        Property(name="database_RefFKey", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Table4", type=database_RefFKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables10: BinaryAssociation = BinaryAssociation(
    name="tables10",
    ends={
        Property(name="database_RefTable11", type=database_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Database", type=database_RefTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procedures12: BinaryAssociation = BinaryAssociation(
    name="procedures12",
    ends={
        Property(name="database_RefProcedure", type=database_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Database13", type=database_RefProcedure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters14: BinaryAssociation = BinaryAssociation(
    name="parameters14",
    ends={
        Property(name="database_RefParameter", type=database_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Procedure", type=database_RefParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
return15: BinaryAssociation = BinaryAssociation(
    name="return15",
    ends={
        Property(name="database_RefType17", type=database_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Procedure16", type=database_RefType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type8: BinaryAssociation = BinaryAssociation(
    name="type8",
    ends={
        Property(name="database_RefType", type=database_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Column9", type=database_RefType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
columns20: BinaryAssociation = BinaryAssociation(
    name="columns20",
    ends={
        Property(name="database_Column21", type=database_PKey, multiplicity=Multiplicity(1, 1)),
        Property(name="database_PKey", type=database_Column, multiplicity=Multiplicity(1, 9999))
    }
)
type18: BinaryAssociation = BinaryAssociation(
    name="type18",
    ends={
        Property(name="database_RefType19", type=database_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Parameter", type=database_RefType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_database_Table_RefTable = Generalization(general=RefTable, specific=database_Table)
gen_database_FKey_RefFKey = Generalization(general=RefFKey, specific=database_FKey)
gen_database_Column_RefColumn = Generalization(general=RefColumn, specific=database_Column)
gen_database_Procedure_RefProcedure = Generalization(general=RefProcedure, specific=database_Procedure)
gen_database_Parameter_RefParameter = Generalization(general=RefParameter, specific=database_Parameter)
gen_database_Database_RefDatabase = Generalization(general=RefDatabase, specific=database_Database)
gen_database_PKey_RefPKey = Generalization(general=RefPKey, specific=database_PKey)
gen_database_Type_RefType = Generalization(general=RefType, specific=database_Type)

# Domain Model
domain_model = DomainModel(
    name="database",
    types={database_Table, RefTable, database_RefColumn, database_RefPKey, database_FKey, RefFKey, database_Column, database_RefTable, RefColumn, database_RefFKey, database_RefProcedure, database_RefDatabase, database_Procedure, RefProcedure, database_RefParameter, database_Parameter, RefParameter, database_RefType, database_Database, RefDatabase, database_PKey, RefPKey, database_Type, RefType},
    associations={columns0, pkeys1, columns5, reference6, fkeys3, tables10, procedures12, parameters14, return15, type8, columns20, type18},
    generalizations={gen_database_Table_RefTable, gen_database_FKey_RefFKey, gen_database_Column_RefColumn, gen_database_Procedure_RefProcedure, gen_database_Parameter_RefParameter, gen_database_Database_RefDatabase, gen_database_PKey_RefPKey, gen_database_Type_RefType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)