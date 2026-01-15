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
relationaldatabase_NamedElement = Class(name="relationaldatabase::NamedElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
relationaldatabase_RelationalDatabase = Class(name="relationaldatabase::RelationalDatabase")
relationaldatabase_Table = Class(name="relationaldatabase::Table")
relationaldatabase_Column = Class(name="relationaldatabase::Column")
relationaldatabase_ForeignKey = Class(name="relationaldatabase::ForeignKey")

# relationaldatabase_NamedElement class attributes and methods
relationaldatabase_NamedElement_name: Property = Property(name="name", type=StringType)
relationaldatabase_NamedElement.attributes={relationaldatabase_NamedElement_name}

# NamedElement class attributes and methods

# relationaldatabase_RelationalDatabase class attributes and methods

# relationaldatabase_Table class attributes and methods

# relationaldatabase_Column class attributes and methods

# relationaldatabase_ForeignKey class attributes and methods

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="relationaldatabase_Table", type=relationaldatabase_RelationalDatabase, multiplicity=Multiplicity(1, 1)),
        Property(name="relationaldatabase_RelationalDatabase", type=relationaldatabase_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreignKeysAsColumn9: BinaryAssociation = BinaryAssociation(
    name="foreignKeysAsColumn9",
    ends={
        Property(name="ForeignKey10", type=relationaldatabase_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="tableColumn", type=relationaldatabase_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
foreignKeysAsForeignColumn11: BinaryAssociation = BinaryAssociation(
    name="foreignKeysAsForeignColumn11",
    ends={
        Property(name="ForeignKey12", type=relationaldatabase_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignColumn", type=relationaldatabase_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
columns1: BinaryAssociation = BinaryAssociation(
    name="columns1",
    ends={
        Property(name="Column", type=relationaldatabase_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=relationaldatabase_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
primaryKey2: BinaryAssociation = BinaryAssociation(
    name="primaryKey2",
    ends={
        Property(name="Column3", type=relationaldatabase_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tableAsPrimaryKey", type=relationaldatabase_Column, multiplicity=Multiplicity(1, 1))
    }
)
foreignKeys4: BinaryAssociation = BinaryAssociation(
    name="foreignKeys4",
    ends={
        Property(name="ForeignKey", type=relationaldatabase_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table5", type=relationaldatabase_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table6: BinaryAssociation = BinaryAssociation(
    name="table6",
    ends={
        Property(name="Table", type=relationaldatabase_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=relationaldatabase_Table, multiplicity=Multiplicity(1, 1))
    }
)
tableAsPrimaryKey7: BinaryAssociation = BinaryAssociation(
    name="tableAsPrimaryKey7",
    ends={
        Property(name="Table8", type=relationaldatabase_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="primaryKey", type=relationaldatabase_Table, multiplicity=Multiplicity(0, 1))
    }
)
tableColumn13: BinaryAssociation = BinaryAssociation(
    name="tableColumn13",
    ends={
        Property(name="Column14", type=relationaldatabase_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKeysAsColumn", type=relationaldatabase_Column, multiplicity=Multiplicity(1, 1))
    }
)
foreignColumn15: BinaryAssociation = BinaryAssociation(
    name="foreignColumn15",
    ends={
        Property(name="Column16", type=relationaldatabase_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKeysAsForeignColumn", type=relationaldatabase_Column, multiplicity=Multiplicity(1, 1))
    }
)
table17: BinaryAssociation = BinaryAssociation(
    name="table17",
    ends={
        Property(name="Table18", type=relationaldatabase_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKeys", type=relationaldatabase_Table, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_relationaldatabase_Table_NamedElement = Generalization(general=NamedElement, specific=relationaldatabase_Table)
gen_relationaldatabase_ForeignKey_NamedElement = Generalization(general=NamedElement, specific=relationaldatabase_ForeignKey)
gen_relationaldatabase_Column_NamedElement = Generalization(general=NamedElement, specific=relationaldatabase_Column)

# Domain Model
domain_model = DomainModel(
    name="relationaldatabase",
    types={relationaldatabase_NamedElement, NamedElement, relationaldatabase_RelationalDatabase, relationaldatabase_Table, relationaldatabase_Column, relationaldatabase_ForeignKey},
    associations={tables0, foreignKeysAsColumn9, foreignKeysAsForeignColumn11, columns1, primaryKey2, foreignKeys4, table6, tableAsPrimaryKey7, tableColumn13, foreignColumn15, table17},
    generalizations={gen_relationaldatabase_Table_NamedElement, gen_relationaldatabase_ForeignKey_NamedElement, gen_relationaldatabase_Column_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)