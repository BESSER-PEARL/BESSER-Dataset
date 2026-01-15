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
Trmodel_loader = Class(name="Trmodel::loader")
Trmodel_Operation = Class(name="Trmodel::Operation", is_abstract=True)
Trmodel_LoadModel = Class(name="Trmodel::LoadModel")
Trmodel_Table = Class(name="Trmodel::Table")
Trmodel_Column = Class(name="Trmodel::Column")
Trmodel_Add = Class(name="Trmodel::Add")
Operation = Class(name="Operation")
Trmodel_Delete = Class(name="Trmodel::Delete")
Trmodel_Update = Class(name="Trmodel::Update")

# Trmodel_loader class attributes and methods

# Trmodel_Operation class attributes and methods

# Trmodel_LoadModel class attributes and methods
Trmodel_LoadModel_url: Property = Property(name="url", type=StringType)
Trmodel_LoadModel.attributes={Trmodel_LoadModel_url}

# Trmodel_Table class attributes and methods
Trmodel_Table_Name: Property = Property(name="Name", type=StringType)
Trmodel_Table.attributes={Trmodel_Table_Name}

# Trmodel_Column class attributes and methods
Trmodel_Column_Name: Property = Property(name="Name", type=StringType)
Trmodel_Column_tableName: Property = Property(name="tableName", type=StringType)
Trmodel_Column.attributes={Trmodel_Column_tableName, Trmodel_Column_Name}

# Trmodel_Add class attributes and methods

# Operation class attributes and methods

# Trmodel_Delete class attributes and methods

# Trmodel_Update class attributes and methods
Trmodel_Update_newName: Property = Property(name="newName", type=StringType)
Trmodel_Update.attributes={Trmodel_Update_newName}

# Relationships
operation0: BinaryAssociation = BinaryAssociation(
    name="operation0",
    ends={
        Property(name="Trmodel_Operation", type=Trmodel_loader, multiplicity=Multiplicity(1, 1)),
        Property(name="Trmodel_loader", type=Trmodel_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
loadmodel1: BinaryAssociation = BinaryAssociation(
    name="loadmodel1",
    ends={
        Property(name="Trmodel_LoadModel", type=Trmodel_loader, multiplicity=Multiplicity(1, 1)),
        Property(name="Trmodel_loader2", type=Trmodel_LoadModel, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
table3: BinaryAssociation = BinaryAssociation(
    name="table3",
    ends={
        Property(name="Trmodel_Table", type=Trmodel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Trmodel_Operation4", type=Trmodel_Table, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
column5: BinaryAssociation = BinaryAssociation(
    name="column5",
    ends={
        Property(name="Trmodel_Column", type=Trmodel_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Trmodel_Operation6", type=Trmodel_Column, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_Trmodel_Add_Operation = Generalization(general=Operation, specific=Trmodel_Add)
gen_Trmodel_Delete_Operation = Generalization(general=Operation, specific=Trmodel_Delete)
gen_Trmodel_Update_Operation = Generalization(general=Operation, specific=Trmodel_Update)

# Domain Model
domain_model = DomainModel(
    name="Trmodel",
    types={Trmodel_loader, Trmodel_Operation, Trmodel_LoadModel, Trmodel_Table, Trmodel_Column, Trmodel_Add, Operation, Trmodel_Delete, Trmodel_Update},
    associations={operation0, loadmodel1, table3, column5},
    generalizations={gen_Trmodel_Add_Operation, gen_Trmodel_Delete_Operation, gen_Trmodel_Update_Operation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)