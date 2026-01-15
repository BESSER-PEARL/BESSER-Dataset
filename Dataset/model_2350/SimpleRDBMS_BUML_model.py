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
simplerdbms_Column = Class(name="simplerdbms::Column")
RModelElement = Class(name="RModelElement")
simplerdbms_ForeignKey = Class(name="simplerdbms::ForeignKey")
simplerdbms_Key = Class(name="simplerdbms::Key")
simplerdbms_Schema = Class(name="simplerdbms::Schema")
simplerdbms_Table = Class(name="simplerdbms::Table")
simplerdbms_RModelElement = Class(name="simplerdbms::RModelElement", is_abstract=True)

# simplerdbms_Column class attributes and methods
simplerdbms_Column_type: Property = Property(name="type", type=StringType)
simplerdbms_Column.attributes={simplerdbms_Column_type}

# RModelElement class attributes and methods

# simplerdbms_ForeignKey class attributes and methods

# simplerdbms_Key class attributes and methods

# simplerdbms_Schema class attributes and methods

# simplerdbms_Table class attributes and methods

# simplerdbms_RModelElement class attributes and methods
simplerdbms_RModelElement_name: Property = Property(name="name", type=StringType)
simplerdbms_RModelElement_kind: Property = Property(name="kind", type=StringType)
simplerdbms_RModelElement.attributes={simplerdbms_RModelElement_name, simplerdbms_RModelElement_kind}

# Relationships
owner0: BinaryAssociation = BinaryAssociation(
    name="owner0",
    ends={
        Property(name="simplerdbms_Table", type=simplerdbms_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="simplerdbms_Column", type=simplerdbms_Table, multiplicity=Multiplicity(1, 1))
    }
)
foreignKeys1: BinaryAssociation = BinaryAssociation(
    name="foreignKeys1",
    ends={
        Property(name="ForeignKey", type=simplerdbms_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column", type=simplerdbms_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
key2: BinaryAssociation = BinaryAssociation(
    name="key2",
    ends={
        Property(name="Key", type=simplerdbms_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column3", type=simplerdbms_Key, multiplicity=Multiplicity(0, 9999))
    }
)
refersTo4: BinaryAssociation = BinaryAssociation(
    name="refersTo4",
    ends={
        Property(name="simplerdbms_Key", type=simplerdbms_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="simplerdbms_ForeignKey", type=simplerdbms_Key, multiplicity=Multiplicity(1, 1))
    }
)
column5: BinaryAssociation = BinaryAssociation(
    name="column5",
    ends={
        Property(name="Column", type=simplerdbms_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKeys", type=simplerdbms_Column, multiplicity=Multiplicity(0, 9999))
    }
)
owner6: BinaryAssociation = BinaryAssociation(
    name="owner6",
    ends={
        Property(name="simplerdbms_Table8", type=simplerdbms_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="simplerdbms_ForeignKey7", type=simplerdbms_Table, multiplicity=Multiplicity(1, 1))
    }
)
schema9: BinaryAssociation = BinaryAssociation(
    name="schema9",
    ends={
        Property(name="simplerdbms_Schema", type=simplerdbms_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="simplerdbms_ForeignKey10", type=simplerdbms_Schema, multiplicity=Multiplicity(1, 1))
    }
)
column12: BinaryAssociation = BinaryAssociation(
    name="column12",
    ends={
        Property(name="Column13", type=simplerdbms_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="key", type=simplerdbms_Column, multiplicity=Multiplicity(0, 9999))
    }
)
tables14: BinaryAssociation = BinaryAssociation(
    name="tables14",
    ends={
        Property(name="Table15", type=simplerdbms_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema", type=simplerdbms_Table, multiplicity=Multiplicity(0, 9999))
    }
)
column16: BinaryAssociation = BinaryAssociation(
    name="column16",
    ends={
        Property(name="simplerdbms_Column18", type=simplerdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="simplerdbms_Table17", type=simplerdbms_Column, multiplicity=Multiplicity(0, 9999))
    }
)
schema19: BinaryAssociation = BinaryAssociation(
    name="schema19",
    ends={
        Property(name="Schema", type=simplerdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=simplerdbms_Schema, multiplicity=Multiplicity(1, 1))
    }
)
theKey20: BinaryAssociation = BinaryAssociation(
    name="theKey20",
    ends={
        Property(name="Key21", type=simplerdbms_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=simplerdbms_Key, multiplicity=Multiplicity(0, 9999))
    }
)
owner11: BinaryAssociation = BinaryAssociation(
    name="owner11",
    ends={
        Property(name="Table", type=simplerdbms_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="theKey", type=simplerdbms_Table, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_simplerdbms_Column_RModelElement = Generalization(general=RModelElement, specific=simplerdbms_Column)
gen_simplerdbms_ForeignKey_RModelElement = Generalization(general=RModelElement, specific=simplerdbms_ForeignKey)
gen_simplerdbms_Key_RModelElement = Generalization(general=RModelElement, specific=simplerdbms_Key)
gen_simplerdbms_Schema_RModelElement = Generalization(general=RModelElement, specific=simplerdbms_Schema)
gen_simplerdbms_Table_RModelElement = Generalization(general=RModelElement, specific=simplerdbms_Table)

# Domain Model
domain_model = DomainModel(
    name="simplerdbms",
    types={simplerdbms_Column, RModelElement, simplerdbms_ForeignKey, simplerdbms_Key, simplerdbms_Schema, simplerdbms_Table, simplerdbms_RModelElement},
    associations={owner0, foreignKeys1, key2, refersTo4, column5, owner6, schema9, column12, tables14, column16, schema19, theKey20, owner11},
    generalizations={gen_simplerdbms_Column_RModelElement, gen_simplerdbms_ForeignKey_RModelElement, gen_simplerdbms_Key_RModelElement, gen_simplerdbms_Schema_RModelElement, gen_simplerdbms_Table_RModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)