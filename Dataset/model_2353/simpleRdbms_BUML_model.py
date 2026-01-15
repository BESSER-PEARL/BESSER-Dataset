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
simpleRdbms_Column = Class(name="simpleRdbms::Column")
simpleRdbms_Key = Class(name="simpleRdbms::Key")
simpleRdbms_ForeignKey = Class(name="simpleRdbms::ForeignKey")
simpleRdbms_Schema = Class(name="simpleRdbms::Schema")
RModelElement = Class(name="RModelElement")
simpleRdbms_Table = Class(name="simpleRdbms::Table")
simpleRdbms_RModelElement = Class(name="simpleRdbms::RModelElement")

# simpleRdbms_Column class attributes and methods
simpleRdbms_Column_type: Property = Property(name="type", type=StringType)
simpleRdbms_Column.attributes={simpleRdbms_Column_type}

# simpleRdbms_Key class attributes and methods

# simpleRdbms_ForeignKey class attributes and methods

# simpleRdbms_Schema class attributes and methods

# RModelElement class attributes and methods

# simpleRdbms_Table class attributes and methods

# simpleRdbms_RModelElement class attributes and methods
simpleRdbms_RModelElement_kind: Property = Property(name="kind", type=StringType)
simpleRdbms_RModelElement_name: Property = Property(name="name", type=StringType)
simpleRdbms_RModelElement.attributes={simpleRdbms_RModelElement_kind, simpleRdbms_RModelElement_name}

# Relationships
schema1: BinaryAssociation = BinaryAssociation(
    name="schema1",
    ends={
        Property(name="Schema", type=simpleRdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=simpleRdbms_Schema, multiplicity=Multiplicity(1, 1))
    }
)
column2: BinaryAssociation = BinaryAssociation(
    name="column2",
    ends={
        Property(name="Column", type=simpleRdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=simpleRdbms_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key3: BinaryAssociation = BinaryAssociation(
    name="key3",
    ends={
        Property(name="Key", type=simpleRdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner4", type=simpleRdbms_Key, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreignKey5: BinaryAssociation = BinaryAssociation(
    name="foreignKey5",
    ends={
        Property(name="ForeignKey", type=simpleRdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner6", type=simpleRdbms_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="Table", type=simpleRdbms_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema", type=simpleRdbms_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
column15: BinaryAssociation = BinaryAssociation(
    name="column15",
    ends={
        Property(name="Column16", type=simpleRdbms_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="key", type=simpleRdbms_Column, multiplicity=Multiplicity(1, 1))
    }
)
owner17: BinaryAssociation = BinaryAssociation(
    name="owner17",
    ends={
        Property(name="Table19", type=simpleRdbms_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="key18", type=simpleRdbms_Table, multiplicity=Multiplicity(1, 1))
    }
)
column20: BinaryAssociation = BinaryAssociation(
    name="column20",
    ends={
        Property(name="Column21", type=simpleRdbms_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKey", type=simpleRdbms_Column, multiplicity=Multiplicity(1, 1))
    }
)
owner7: BinaryAssociation = BinaryAssociation(
    name="owner7",
    ends={
        Property(name="Table8", type=simpleRdbms_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column", type=simpleRdbms_Table, multiplicity=Multiplicity(1, 1))
    }
)
key9: BinaryAssociation = BinaryAssociation(
    name="key9",
    ends={
        Property(name="Key11", type=simpleRdbms_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column10", type=simpleRdbms_Key, multiplicity=Multiplicity(0, 9999))
    }
)
foreignKey12: BinaryAssociation = BinaryAssociation(
    name="foreignKey12",
    ends={
        Property(name="ForeignKey14", type=simpleRdbms_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column13", type=simpleRdbms_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
refersTo22: BinaryAssociation = BinaryAssociation(
    name="refersTo22",
    ends={
        Property(name="simpleRdbms_Key", type=simpleRdbms_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleRdbms_ForeignKey", type=simpleRdbms_Key, multiplicity=Multiplicity(1, 1))
    }
)
owner23: BinaryAssociation = BinaryAssociation(
    name="owner23",
    ends={
        Property(name="Table25", type=simpleRdbms_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKey24", type=simpleRdbms_Table, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_simpleRdbms_Table_RModelElement = Generalization(general=RModelElement, specific=simpleRdbms_Table)
gen_simpleRdbms_Schema_RModelElement = Generalization(general=RModelElement, specific=simpleRdbms_Schema)
gen_simpleRdbms_Key_RModelElement = Generalization(general=RModelElement, specific=simpleRdbms_Key)
gen_simpleRdbms_ForeignKey_RModelElement = Generalization(general=RModelElement, specific=simpleRdbms_ForeignKey)
gen_simpleRdbms_Column_RModelElement = Generalization(general=RModelElement, specific=simpleRdbms_Column)

# Domain Model
domain_model = DomainModel(
    name="simpleRdbms",
    types={simpleRdbms_Column, simpleRdbms_Key, simpleRdbms_ForeignKey, simpleRdbms_Schema, RModelElement, simpleRdbms_Table, simpleRdbms_RModelElement},
    associations={schema1, column2, key3, foreignKey5, tables0, column15, owner17, column20, owner7, key9, foreignKey12, refersTo22, owner23},
    generalizations={gen_simpleRdbms_Table_RModelElement, gen_simpleRdbms_Schema_RModelElement, gen_simpleRdbms_Key_RModelElement, gen_simpleRdbms_ForeignKey_RModelElement, gen_simpleRdbms_Column_RModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)