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
rdbmsMM_Column = Class(name="rdbmsMM::Column")
RModelElement = Class(name="RModelElement")
rdbmsMM_Table = Class(name="rdbmsMM::Table")
rdbmsMM_Key = Class(name="rdbmsMM::Key")
rdbmsMM_ForeignKey = Class(name="rdbmsMM::ForeignKey")
rdbmsMM_Schema = Class(name="rdbmsMM::Schema")
rdbmsMM_RModelElement = Class(name="rdbmsMM::RModelElement", is_abstract=True)

# rdbmsMM_Column class attributes and methods
rdbmsMM_Column_type: Property = Property(name="type", type=StringType)
rdbmsMM_Column.attributes={rdbmsMM_Column_type}

# RModelElement class attributes and methods

# rdbmsMM_Table class attributes and methods

# rdbmsMM_Key class attributes and methods

# rdbmsMM_ForeignKey class attributes and methods

# rdbmsMM_Schema class attributes and methods

# rdbmsMM_RModelElement class attributes and methods
rdbmsMM_RModelElement_kind: Property = Property(name="kind", type=StringType)
rdbmsMM_RModelElement_name: Property = Property(name="name", type=StringType)
rdbmsMM_RModelElement.attributes={rdbmsMM_RModelElement_name, rdbmsMM_RModelElement_kind}

# Relationships
owner12: BinaryAssociation = BinaryAssociation(
    name="owner12",
    ends={
        Property(name="Table13", type=rdbmsMM_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="key", type=rdbmsMM_Table, multiplicity=Multiplicity(1, 1))
    }
)
owner0: BinaryAssociation = BinaryAssociation(
    name="owner0",
    ends={
        Property(name="Table", type=rdbmsMM_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column", type=rdbmsMM_Table, multiplicity=Multiplicity(1, 1))
    }
)
key1: BinaryAssociation = BinaryAssociation(
    name="key1",
    ends={
        Property(name="Key", type=rdbmsMM_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column2", type=rdbmsMM_Key, multiplicity=Multiplicity(1, 9999))
    }
)
foreignKey3: BinaryAssociation = BinaryAssociation(
    name="foreignKey3",
    ends={
        Property(name="ForeignKey", type=rdbmsMM_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column4", type=rdbmsMM_ForeignKey, multiplicity=Multiplicity(1, 9999))
    }
)
schema5: BinaryAssociation = BinaryAssociation(
    name="schema5",
    ends={
        Property(name="rdbmsMM_Schema", type=rdbmsMM_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmsMM_ForeignKey", type=rdbmsMM_Schema, multiplicity=Multiplicity(1, 1))
    }
)
refersTo6: BinaryAssociation = BinaryAssociation(
    name="refersTo6",
    ends={
        Property(name="Key7", type=rdbmsMM_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="referedBy", type=rdbmsMM_Key, multiplicity=Multiplicity(1, 1))
    }
)
owner8: BinaryAssociation = BinaryAssociation(
    name="owner8",
    ends={
        Property(name="Table9", type=rdbmsMM_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKey", type=rdbmsMM_Table, multiplicity=Multiplicity(1, 1))
    }
)
column10: BinaryAssociation = BinaryAssociation(
    name="column10",
    ends={
        Property(name="Column", type=rdbmsMM_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKey11", type=rdbmsMM_Column, multiplicity=Multiplicity(0, 9999))
    }
)
key24: BinaryAssociation = BinaryAssociation(
    name="key24",
    ends={
        Property(name="Key26", type=rdbmsMM_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner25", type=rdbmsMM_Key, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
column14: BinaryAssociation = BinaryAssociation(
    name="column14",
    ends={
        Property(name="Column16", type=rdbmsMM_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="key15", type=rdbmsMM_Column, multiplicity=Multiplicity(0, 9999))
    }
)
referedBy17: BinaryAssociation = BinaryAssociation(
    name="referedBy17",
    ends={
        Property(name="ForeignKey18", type=rdbmsMM_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="refersTo", type=rdbmsMM_ForeignKey, multiplicity=Multiplicity(1, 9999))
    }
)
tables19: BinaryAssociation = BinaryAssociation(
    name="tables19",
    ends={
        Property(name="Table20", type=rdbmsMM_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema", type=rdbmsMM_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schema21: BinaryAssociation = BinaryAssociation(
    name="schema21",
    ends={
        Property(name="Schema", type=rdbmsMM_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=rdbmsMM_Schema, multiplicity=Multiplicity(1, 1))
    }
)
column22: BinaryAssociation = BinaryAssociation(
    name="column22",
    ends={
        Property(name="Column23", type=rdbmsMM_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=rdbmsMM_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreignKey27: BinaryAssociation = BinaryAssociation(
    name="foreignKey27",
    ends={
        Property(name="ForeignKey29", type=rdbmsMM_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner28", type=rdbmsMM_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_rdbmsMM_Column_RModelElement = Generalization(general=RModelElement, specific=rdbmsMM_Column)
gen_rdbmsMM_Key_RModelElement = Generalization(general=RModelElement, specific=rdbmsMM_Key)
gen_rdbmsMM_ForeignKey_RModelElement = Generalization(general=RModelElement, specific=rdbmsMM_ForeignKey)
gen_rdbmsMM_Schema_RModelElement = Generalization(general=RModelElement, specific=rdbmsMM_Schema)
gen_rdbmsMM_Table_RModelElement = Generalization(general=RModelElement, specific=rdbmsMM_Table)

# Domain Model
domain_model = DomainModel(
    name="rdbmsMM",
    types={rdbmsMM_Column, RModelElement, rdbmsMM_Table, rdbmsMM_Key, rdbmsMM_ForeignKey, rdbmsMM_Schema, rdbmsMM_RModelElement},
    associations={owner12, owner0, key1, foreignKey3, schema5, refersTo6, owner8, column10, key24, column14, referedBy17, tables19, schema21, column22, foreignKey27},
    generalizations={gen_rdbmsMM_Column_RModelElement, gen_rdbmsMM_Key_RModelElement, gen_rdbmsMM_ForeignKey_RModelElement, gen_rdbmsMM_Schema_RModelElement, gen_rdbmsMM_Table_RModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)