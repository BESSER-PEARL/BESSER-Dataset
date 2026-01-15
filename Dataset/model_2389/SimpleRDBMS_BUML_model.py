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
simpleRDBMS_ForeignKey = Class(name="simpleRDBMS::ForeignKey")
simpleRDBMS_Key = Class(name="simpleRDBMS::Key")
simpleRDBMS_NamedElement = Class(name="simpleRDBMS::NamedElement", is_abstract=True)
simpleRDBMS_Schema = Class(name="simpleRDBMS::Schema")
NamedElement = Class(name="NamedElement")
simpleRDBMS_Table = Class(name="simpleRDBMS::Table")
simpleRDBMS_Column = Class(name="simpleRDBMS::Column")
simpleRDBMS_RDBMSModel = Class(name="simpleRDBMS::RDBMSModel")

# simpleRDBMS_ForeignKey class attributes and methods

# simpleRDBMS_Key class attributes and methods

# simpleRDBMS_NamedElement class attributes and methods
simpleRDBMS_NamedElement_name: Property = Property(name="name", type=StringType)
simpleRDBMS_NamedElement.attributes={simpleRDBMS_NamedElement_name}

# simpleRDBMS_Schema class attributes and methods

# NamedElement class attributes and methods

# simpleRDBMS_Table class attributes and methods

# simpleRDBMS_Column class attributes and methods

# simpleRDBMS_RDBMSModel class attributes and methods

# Relationships
foreignKeys3: BinaryAssociation = BinaryAssociation(
    name="foreignKeys3",
    ends={
        Property(name="simpleRDBMS_ForeignKey", type=simpleRDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleRDBMS_Table4", type=simpleRDBMS_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key5: BinaryAssociation = BinaryAssociation(
    name="key5",
    ends={
        Property(name="simpleRDBMS_Key", type=simpleRDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleRDBMS_Table6", type=simpleRDBMS_Key, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
column7: BinaryAssociation = BinaryAssociation(
    name="column7",
    ends={
        Property(name="simpleRDBMS_Column9", type=simpleRDBMS_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleRDBMS_ForeignKey8", type=simpleRDBMS_Column, multiplicity=Multiplicity(1, 1))
    }
)
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="simpleRDBMS_Table", type=simpleRDBMS_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleRDBMS_Schema", type=simpleRDBMS_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns1: BinaryAssociation = BinaryAssociation(
    name="columns1",
    ends={
        Property(name="simpleRDBMS_Column", type=simpleRDBMS_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleRDBMS_Table2", type=simpleRDBMS_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referTo10: BinaryAssociation = BinaryAssociation(
    name="referTo10",
    ends={
        Property(name="simpleRDBMS_Key12", type=simpleRDBMS_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleRDBMS_ForeignKey11", type=simpleRDBMS_Key, multiplicity=Multiplicity(1, 1))
    }
)
schemas13: BinaryAssociation = BinaryAssociation(
    name="schemas13",
    ends={
        Property(name="simpleRDBMS_Schema14", type=simpleRDBMS_RDBMSModel, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleRDBMS_RDBMSModel", type=simpleRDBMS_Schema, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
column15: BinaryAssociation = BinaryAssociation(
    name="column15",
    ends={
        Property(name="simpleRDBMS_Column17", type=simpleRDBMS_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleRDBMS_Key16", type=simpleRDBMS_Column, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_simpleRDBMS_Column_NamedElement = Generalization(general=NamedElement, specific=simpleRDBMS_Column)
gen_simpleRDBMS_ForeignKey_NamedElement = Generalization(general=NamedElement, specific=simpleRDBMS_ForeignKey)
gen_simpleRDBMS_Schema_NamedElement = Generalization(general=NamedElement, specific=simpleRDBMS_Schema)
gen_simpleRDBMS_Table_NamedElement = Generalization(general=NamedElement, specific=simpleRDBMS_Table)
gen_simpleRDBMS_Key_NamedElement = Generalization(general=NamedElement, specific=simpleRDBMS_Key)

# Domain Model
domain_model = DomainModel(
    name="simpleRDBMS",
    types={simpleRDBMS_ForeignKey, simpleRDBMS_Key, simpleRDBMS_NamedElement, simpleRDBMS_Schema, NamedElement, simpleRDBMS_Table, simpleRDBMS_Column, simpleRDBMS_RDBMSModel},
    associations={foreignKeys3, key5, column7, tables0, columns1, referTo10, schemas13, column15},
    generalizations={gen_simpleRDBMS_Column_NamedElement, gen_simpleRDBMS_ForeignKey_NamedElement, gen_simpleRDBMS_Schema_NamedElement, gen_simpleRDBMS_Table_NamedElement, gen_simpleRDBMS_Key_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)