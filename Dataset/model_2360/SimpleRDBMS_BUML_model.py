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
RdbmsModelElement = Class(name="RdbmsModelElement")
SimpleRDBMS_RdbmsTable = Class(name="SimpleRDBMS::RdbmsTable")
SimpleRDBMS_RdbmsKey = Class(name="SimpleRDBMS::RdbmsKey")
SimpleRDBMS_RdbmsForeignKey = Class(name="SimpleRDBMS::RdbmsForeignKey")
SimpleRDBMS_RdbmsColumn = Class(name="SimpleRDBMS::RdbmsColumn")
SimpleRDBMS_RdbmsModelElement = Class(name="SimpleRDBMS::RdbmsModelElement")
SimpleRDBMS_RdbmsSchema = Class(name="SimpleRDBMS::RdbmsSchema")

# RdbmsModelElement class attributes and methods

# SimpleRDBMS_RdbmsTable class attributes and methods

# SimpleRDBMS_RdbmsKey class attributes and methods

# SimpleRDBMS_RdbmsForeignKey class attributes and methods

# SimpleRDBMS_RdbmsColumn class attributes and methods
SimpleRDBMS_RdbmsColumn_rdbmsType: Property = Property(name="rdbmsType", type=StringType)
SimpleRDBMS_RdbmsColumn.attributes={SimpleRDBMS_RdbmsColumn_rdbmsType}

# SimpleRDBMS_RdbmsModelElement class attributes and methods
SimpleRDBMS_RdbmsModelElement_rdbmsName: Property = Property(name="rdbmsName", type=StringType)
SimpleRDBMS_RdbmsModelElement_rdbmsKind: Property = Property(name="rdbmsKind", type=StringType)
SimpleRDBMS_RdbmsModelElement_id: Property = Property(name="id", type=StringType)
SimpleRDBMS_RdbmsModelElement.attributes={SimpleRDBMS_RdbmsModelElement_id, SimpleRDBMS_RdbmsModelElement_rdbmsName, SimpleRDBMS_RdbmsModelElement_rdbmsKind}

# SimpleRDBMS_RdbmsSchema class attributes and methods

# Relationships
rdbmsOwner0: BinaryAssociation = BinaryAssociation(
    name="rdbmsOwner0",
    ends={
        Property(name="RdbmsTable", type=SimpleRDBMS_RdbmsColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmsColumn", type=SimpleRDBMS_RdbmsTable, multiplicity=Multiplicity(1, 1))
    }
)
rdbmsKey1: BinaryAssociation = BinaryAssociation(
    name="rdbmsKey1",
    ends={
        Property(name="RdbmsKey", type=SimpleRDBMS_RdbmsColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmsColumn2", type=SimpleRDBMS_RdbmsKey, multiplicity=Multiplicity(0, 9999))
    }
)
rdbmsForeignKey3: BinaryAssociation = BinaryAssociation(
    name="rdbmsForeignKey3",
    ends={
        Property(name="RdbmsForeignKey", type=SimpleRDBMS_RdbmsColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmsColumn4", type=SimpleRDBMS_RdbmsForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
rdbmsOwner5: BinaryAssociation = BinaryAssociation(
    name="rdbmsOwner5",
    ends={
        Property(name="RdbmsTable6", type=SimpleRDBMS_RdbmsForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmsForeignKey", type=SimpleRDBMS_RdbmsTable, multiplicity=Multiplicity(1, 1))
    }
)
rdbmsColumn11: BinaryAssociation = BinaryAssociation(
    name="rdbmsColumn11",
    ends={
        Property(name="RdbmsColumn12", type=SimpleRDBMS_RdbmsKey, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmsKey", type=SimpleRDBMS_RdbmsColumn, multiplicity=Multiplicity(0, 9999))
    }
)
rdbmsRefersToOpposite13: BinaryAssociation = BinaryAssociation(
    name="rdbmsRefersToOpposite13",
    ends={
        Property(name="RdbmsForeignKey14", type=SimpleRDBMS_RdbmsKey, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmsRefersTo", type=SimpleRDBMS_RdbmsForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
rdbmsOwner15: BinaryAssociation = BinaryAssociation(
    name="rdbmsOwner15",
    ends={
        Property(name="RdbmsTable17", type=SimpleRDBMS_RdbmsKey, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmsKey16", type=SimpleRDBMS_RdbmsTable, multiplicity=Multiplicity(1, 1))
    }
)
rdbmsTable18: BinaryAssociation = BinaryAssociation(
    name="rdbmsTable18",
    ends={
        Property(name="RdbmsTable19", type=SimpleRDBMS_RdbmsSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmsSchema", type=SimpleRDBMS_RdbmsTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rdbmsColumn20: BinaryAssociation = BinaryAssociation(
    name="rdbmsColumn20",
    ends={
        Property(name="RdbmsColumn21", type=SimpleRDBMS_RdbmsTable, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmsOwner", type=SimpleRDBMS_RdbmsColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rdbmsRefersTo7: BinaryAssociation = BinaryAssociation(
    name="rdbmsRefersTo7",
    ends={
        Property(name="RdbmsKey8", type=SimpleRDBMS_RdbmsForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmsRefersToOpposite", type=SimpleRDBMS_RdbmsKey, multiplicity=Multiplicity(1, 1))
    }
)
rdbmsColumn9: BinaryAssociation = BinaryAssociation(
    name="rdbmsColumn9",
    ends={
        Property(name="RdbmsColumn", type=SimpleRDBMS_RdbmsForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmsForeignKey10", type=SimpleRDBMS_RdbmsColumn, multiplicity=Multiplicity(0, 9999))
    }
)
rdbmsSchema28: BinaryAssociation = BinaryAssociation(
    name="rdbmsSchema28",
    ends={
        Property(name="RdbmsSchema", type=SimpleRDBMS_RdbmsTable, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmsTable", type=SimpleRDBMS_RdbmsSchema, multiplicity=Multiplicity(1, 1))
    }
)
rdbmsForeignKey22: BinaryAssociation = BinaryAssociation(
    name="rdbmsForeignKey22",
    ends={
        Property(name="RdbmsForeignKey24", type=SimpleRDBMS_RdbmsTable, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmsOwner23", type=SimpleRDBMS_RdbmsForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rdbmsKey25: BinaryAssociation = BinaryAssociation(
    name="rdbmsKey25",
    ends={
        Property(name="RdbmsKey27", type=SimpleRDBMS_RdbmsTable, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmsOwner26", type=SimpleRDBMS_RdbmsKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_SimpleRDBMS_RdbmsColumn_RdbmsModelElement = Generalization(general=RdbmsModelElement, specific=SimpleRDBMS_RdbmsColumn)
gen_SimpleRDBMS_RdbmsForeignKey_RdbmsModelElement = Generalization(general=RdbmsModelElement, specific=SimpleRDBMS_RdbmsForeignKey)
gen_SimpleRDBMS_RdbmsSchema_RdbmsModelElement = Generalization(general=RdbmsModelElement, specific=SimpleRDBMS_RdbmsSchema)
gen_SimpleRDBMS_RdbmsTable_RdbmsModelElement = Generalization(general=RdbmsModelElement, specific=SimpleRDBMS_RdbmsTable)
gen_SimpleRDBMS_RdbmsKey_RdbmsModelElement = Generalization(general=RdbmsModelElement, specific=SimpleRDBMS_RdbmsKey)

# Domain Model
domain_model = DomainModel(
    name="SimpleRDBMS",
    types={RdbmsModelElement, SimpleRDBMS_RdbmsTable, SimpleRDBMS_RdbmsKey, SimpleRDBMS_RdbmsForeignKey, SimpleRDBMS_RdbmsColumn, SimpleRDBMS_RdbmsModelElement, SimpleRDBMS_RdbmsSchema},
    associations={rdbmsOwner0, rdbmsKey1, rdbmsForeignKey3, rdbmsOwner5, rdbmsColumn11, rdbmsRefersToOpposite13, rdbmsOwner15, rdbmsTable18, rdbmsColumn20, rdbmsRefersTo7, rdbmsColumn9, rdbmsSchema28, rdbmsForeignKey22, rdbmsKey25},
    generalizations={gen_SimpleRDBMS_RdbmsColumn_RdbmsModelElement, gen_SimpleRDBMS_RdbmsForeignKey_RdbmsModelElement, gen_SimpleRDBMS_RdbmsSchema_RdbmsModelElement, gen_SimpleRDBMS_RdbmsTable_RdbmsModelElement, gen_SimpleRDBMS_RdbmsKey_RdbmsModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)