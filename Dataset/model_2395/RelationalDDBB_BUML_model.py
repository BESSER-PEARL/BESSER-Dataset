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

# Enumerations
BasicType: Enumeration = Enumeration(
    name="BasicType",
    literals={
            EnumerationLiteral(name="BOOL"),
			EnumerationLiteral(name="INT"),
			EnumerationLiteral(name="CHAR"),
			EnumerationLiteral(name="REAL")
    }
)

# Classes
rdpl_Schema = Class(name="rdpl::Schema")
rdpl_Table = Class(name="rdpl::Table")
rdpl_Column = Class(name="rdpl::Column")
rdpl_Record = Class(name="rdpl::Record")
rdpl_Type = Class(name="rdpl::Type")
rdpl_ForeignKey = Class(name="rdpl::ForeignKey")
rdpl_RecordElement = Class(name="rdpl::RecordElement")

# rdpl_Schema class attributes and methods
rdpl_Schema_name: Property = Property(name="name", type=StringType)
rdpl_Schema.attributes={rdpl_Schema_name}

# rdpl_Table class attributes and methods
rdpl_Table_name: Property = Property(name="name", type=StringType)
rdpl_Table.attributes={rdpl_Table_name}

# rdpl_Column class attributes and methods
rdpl_Column_name: Property = Property(name="name", type=StringType)
rdpl_Column_stype: Property = Property(name="stype", type=StringType)
rdpl_Column_ctype: Property = Property(name="ctype", type=StringType)
rdpl_Column.attributes={rdpl_Column_name, rdpl_Column_ctype, rdpl_Column_stype}

# rdpl_Record class attributes and methods

# rdpl_Type class attributes and methods
rdpl_Type_name: Property = Property(name="name", type=StringType)
rdpl_Type.attributes={rdpl_Type_name}

# rdpl_ForeignKey class attributes and methods

# rdpl_RecordElement class attributes and methods
rdpl_RecordElement_value: Property = Property(name="value", type=StringType)
rdpl_RecordElement.attributes={rdpl_RecordElement_value}

# Relationships
columns3: BinaryAssociation = BinaryAssociation(
    name="columns3",
    ends={
        Property(name="rdpl_Column", type=rdpl_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdpl_Table4", type=rdpl_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyColumns5: BinaryAssociation = BinaryAssociation(
    name="keyColumns5",
    ends={
        Property(name="rdpl_Column7", type=rdpl_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdpl_Table6", type=rdpl_Column, multiplicity=Multiplicity(0, 9999))
    }
)
content8: BinaryAssociation = BinaryAssociation(
    name="content8",
    ends={
        Property(name="rdpl_Record", type=rdpl_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdpl_Table9", type=rdpl_Record, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="rdpl_Table", type=rdpl_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="rdpl_Schema", type=rdpl_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types1: BinaryAssociation = BinaryAssociation(
    name="types1",
    ends={
        Property(name="rdpl_Type", type=rdpl_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="rdpl_Schema2", type=rdpl_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
references12: BinaryAssociation = BinaryAssociation(
    name="references12",
    ends={
        Property(name="rdpl_Table14", type=rdpl_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="rdpl_ForeignKey13", type=rdpl_Table, multiplicity=Multiplicity(1, 1))
    }
)
columns15: BinaryAssociation = BinaryAssociation(
    name="columns15",
    ends={
        Property(name="rdpl_Column17", type=rdpl_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="rdpl_ForeignKey16", type=rdpl_Column, multiplicity=Multiplicity(1, 9999))
    }
)
foreignKeys10: BinaryAssociation = BinaryAssociation(
    name="foreignKeys10",
    ends={
        Property(name="rdpl_ForeignKey", type=rdpl_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdpl_Table11", type=rdpl_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type20: BinaryAssociation = BinaryAssociation(
    name="type20",
    ends={
        Property(name="rdpl_Column22", type=rdpl_RecordElement, multiplicity=Multiplicity(1, 1)),
        Property(name="rdpl_RecordElement21", type=rdpl_Column, multiplicity=Multiplicity(1, 1))
    }
)
type23: BinaryAssociation = BinaryAssociation(
    name="type23",
    ends={
        Property(name="rdpl_Type25", type=rdpl_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="rdpl_Column24", type=rdpl_Type, multiplicity=Multiplicity(1, 1))
    }
)
elements18: BinaryAssociation = BinaryAssociation(
    name="elements18",
    ends={
        Property(name="rdpl_RecordElement", type=rdpl_Record, multiplicity=Multiplicity(1, 1)),
        Property(name="rdpl_Record19", type=rdpl_RecordElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="rdpl",
    types={rdpl_Schema, rdpl_Table, rdpl_Column, rdpl_Record, rdpl_Type, rdpl_ForeignKey, rdpl_RecordElement, BasicType},
    associations={columns3, keyColumns5, content8, tables0, types1, references12, columns15, foreignKeys10, type20, type23, elements18},
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