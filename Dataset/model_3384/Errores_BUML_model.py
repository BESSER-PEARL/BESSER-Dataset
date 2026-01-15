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
errors_Errores = Class(name="errors::Errores")
errors_Error = Class(name="errors::Error")
errors_ForeignError = Class(name="errors::ForeignError")
Error = Class(name="Error")
errors_Table = Class(name="errors::Table")
errors_ColumnFk = Class(name="errors::ColumnFk")
errors_CheckError = Class(name="errors::CheckError")
errors_ColumnCk = Class(name="errors::ColumnCk")
errors_ValueCk = Class(name="errors::ValueCk")

# errors_Errores class attributes and methods

# errors_Error class attributes and methods

# errors_ForeignError class attributes and methods
errors_ForeignError_nameFk: Property = Property(name="nameFk", type=StringType)
errors_ForeignError_porcent: Property = Property(name="porcent", type=StringType)
errors_ForeignError.attributes={errors_ForeignError_porcent, errors_ForeignError_nameFk}

# Error class attributes and methods

# errors_Table class attributes and methods
errors_Table_nameTable: Property = Property(name="nameTable", type=StringType)
errors_Table.attributes={errors_Table_nameTable}

# errors_ColumnFk class attributes and methods
errors_ColumnFk_nameColumn: Property = Property(name="nameColumn", type=StringType)
errors_ColumnFk.attributes={errors_ColumnFk_nameColumn}

# errors_CheckError class attributes and methods
errors_CheckError_nameTable: Property = Property(name="nameTable", type=StringType)
errors_CheckError_nameCk: Property = Property(name="nameCk", type=StringType)
errors_CheckError_porcent: Property = Property(name="porcent", type=StringType)
errors_CheckError.attributes={errors_CheckError_nameTable, errors_CheckError_porcent, errors_CheckError_nameCk}

# errors_ColumnCk class attributes and methods
errors_ColumnCk_columnName: Property = Property(name="columnName", type=StringType)
errors_ColumnCk.attributes={errors_ColumnCk_columnName}

# errors_ValueCk class attributes and methods
errors_ValueCk_value: Property = Property(name="value", type=StringType)
errors_ValueCk.attributes={errors_ValueCk_value}

# Relationships
errores0: BinaryAssociation = BinaryAssociation(
    name="errores0",
    ends={
        Property(name="errors_Error", type=errors_Errores, multiplicity=Multiplicity(1, 1)),
        Property(name="errors_Errores", type=errors_Error, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tableCont1: BinaryAssociation = BinaryAssociation(
    name="tableCont1",
    ends={
        Property(name="errors_Table", type=errors_ForeignError, multiplicity=Multiplicity(1, 1)),
        Property(name="errors_ForeignError", type=errors_Table, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tableRef2: BinaryAssociation = BinaryAssociation(
    name="tableRef2",
    ends={
        Property(name="errors_Table4", type=errors_ForeignError, multiplicity=Multiplicity(1, 1)),
        Property(name="errors_ForeignError3", type=errors_Table, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columnCont5: BinaryAssociation = BinaryAssociation(
    name="columnCont5",
    ends={
        Property(name="errors_ColumnFk", type=errors_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="errors_Table6", type=errors_ColumnFk, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns7: BinaryAssociation = BinaryAssociation(
    name="columns7",
    ends={
        Property(name="errors_ColumnCk", type=errors_CheckError, multiplicity=Multiplicity(1, 1)),
        Property(name="errors_CheckError", type=errors_ColumnCk, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values8: BinaryAssociation = BinaryAssociation(
    name="values8",
    ends={
        Property(name="errors_ValueCk", type=errors_ColumnCk, multiplicity=Multiplicity(1, 1)),
        Property(name="errors_ColumnCk9", type=errors_ValueCk, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_errors_ForeignError_Error = Generalization(general=Error, specific=errors_ForeignError)
gen_errors_CheckError_Error = Generalization(general=Error, specific=errors_CheckError)

# Domain Model
domain_model = DomainModel(
    name="errors",
    types={errors_Errores, errors_Error, errors_ForeignError, Error, errors_Table, errors_ColumnFk, errors_CheckError, errors_ColumnCk, errors_ValueCk},
    associations={errores0, tableCont1, tableRef2, columnCont5, columns7, values8},
    generalizations={gen_errors_ForeignError_Error, gen_errors_CheckError_Error},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)