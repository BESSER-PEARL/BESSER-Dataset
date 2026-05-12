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
relational_Column = Class(name="relational_Column")
relational_Table = Class(name="relational_Table")
relational_Key = Class(name="relational_Key")
relational_ForeignKey = Class(name="relational_ForeignKey")

# relational_Column class attributes and methods
relational_Column_name: Property = Property(name="name", type=StringType)
relational_Column_type: Property = Property(name="type", type=StringType)
relational_Column.attributes={relational_Column_name, relational_Column_type}

# relational_Table class attributes and methods
relational_Table_name: Property = Property(name="name", type=StringType)
relational_Table.attributes={relational_Table_name}

# relational_Key class attributes and methods
relational_Key_name: Property = Property(name="name", type=StringType)
relational_Key.attributes={relational_Key_name}

# relational_ForeignKey class attributes and methods

# Relationships
column0: BinaryAssociation = BinaryAssociation(
    name="column0",
    ends={
        Property(name="relational_Column", type=relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="relational_Table", type=relational_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key1: BinaryAssociation = BinaryAssociation(
    name="key1",
    ends={
        Property(name="Key", type=relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=relational_Key, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
foreignKey2: BinaryAssociation = BinaryAssociation(
    name="foreignKey2",
    ends={
        Property(name="ForeignKey", type=relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table3", type=relational_ForeignKey, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
column4: BinaryAssociation = BinaryAssociation(
    name="column4",
    ends={
        Property(name="relational_Column5", type=relational_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="relational_Key", type=relational_Column, multiplicity=Multiplicity(0, 9999))
    }
)
referredBy6: BinaryAssociation = BinaryAssociation(
    name="referredBy6",
    ends={
        Property(name="ForeignKey7", type=relational_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="refersTo", type=relational_ForeignKey, multiplicity=Multiplicity(0, 1))
    }
)
table8: BinaryAssociation = BinaryAssociation(
    name="table8",
    ends={
        Property(name="Table", type=relational_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="key", type=relational_Table, multiplicity=Multiplicity(1, 1))
    }
)
refersTo11: BinaryAssociation = BinaryAssociation(
    name="refersTo11",
    ends={
        Property(name="relational_Key13", type=relational_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="relational_ForeignKey12", type=relational_Key, multiplicity=Multiplicity(1, 1))
    }
)
table14: BinaryAssociation = BinaryAssociation(
    name="table14",
    ends={
        Property(name="relational_Table16", type=relational_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="relational_ForeignKey15", type=relational_Table, multiplicity=Multiplicity(1, 1))
    }
)
column9: BinaryAssociation = BinaryAssociation(
    name="column9",
    ends={
        Property(name="relational_Column10", type=relational_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="relational_ForeignKey", type=relational_Column, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="relational",
    types={relational_Column, relational_Table, relational_Key, relational_ForeignKey},
    associations={column0, key1, foreignKey2, column4, referredBy6, table8, refersTo11, table14, column9},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)