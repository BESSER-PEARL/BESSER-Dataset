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
databaseMetamodel_Column = Class(name="databaseMetamodel::Column")
databaseMetamodel_Database = Class(name="databaseMetamodel::Database")
databaseMetamodel_Relation = Class(name="databaseMetamodel::Relation")

# databaseMetamodel_Column class attributes and methods
databaseMetamodel_Column_hasFKOrder: Property = Property(name="hasFKOrder", type=IntegerType)
databaseMetamodel_Column_name: Property = Property(name="name", type=StringType)
databaseMetamodel_Column_type: Property = Property(name="type", type=StringType)
databaseMetamodel_Column_hasPKOrder: Property = Property(name="hasPKOrder", type=IntegerType)
databaseMetamodel_Column.attributes={databaseMetamodel_Column_hasPKOrder, databaseMetamodel_Column_type, databaseMetamodel_Column_hasFKOrder, databaseMetamodel_Column_name}

# databaseMetamodel_Database class attributes and methods

# databaseMetamodel_Relation class attributes and methods
databaseMetamodel_Relation_name: Property = Property(name="name", type=StringType)
databaseMetamodel_Relation_isJoinTable: Property = Property(name="isJoinTable", type=BooleanType)
databaseMetamodel_Relation_isSelfJoinTable: Property = Property(name="isSelfJoinTable", type=BooleanType)
databaseMetamodel_Relation.attributes={databaseMetamodel_Relation_isSelfJoinTable, databaseMetamodel_Relation_isJoinTable, databaseMetamodel_Relation_name}

# Relationships
hasColumns1: BinaryAssociation = BinaryAssociation(
    name="hasColumns1",
    ends={
        Property(name="databaseMetamodel_Column", type=databaseMetamodel_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="databaseMetamodel_Relation2", type=databaseMetamodel_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
hasPrimaryKey3: BinaryAssociation = BinaryAssociation(
    name="hasPrimaryKey3",
    ends={
        Property(name="databaseMetamodel_Column5", type=databaseMetamodel_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="databaseMetamodel_Relation4", type=databaseMetamodel_Column, multiplicity=Multiplicity(1, 9999))
    }
)
hasForeignKey6: BinaryAssociation = BinaryAssociation(
    name="hasForeignKey6",
    ends={
        Property(name="databaseMetamodel_Column8", type=databaseMetamodel_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="databaseMetamodel_Relation7", type=databaseMetamodel_Column, multiplicity=Multiplicity(0, 9999))
    }
)
referencesRelation10: BinaryAssociation = BinaryAssociation(
    name="referencesRelation10",
    ends={
        Property(name="databaseMetamodel_Relation11", type=databaseMetamodel_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="databaseMetamodel_Relation9", type=databaseMetamodel_Relation, multiplicity=Multiplicity(0, 2))
    }
)
relation0: BinaryAssociation = BinaryAssociation(
    name="relation0",
    ends={
        Property(name="databaseMetamodel_Relation", type=databaseMetamodel_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="databaseMetamodel_Database", type=databaseMetamodel_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isForeinKeyToColumn13: BinaryAssociation = BinaryAssociation(
    name="isForeinKeyToColumn13",
    ends={
        Property(name="databaseMetamodel_Column14", type=databaseMetamodel_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="databaseMetamodel_Column12", type=databaseMetamodel_Column, multiplicity=Multiplicity(0, 9999))
    }
)
isForeignKeyToRelation15: BinaryAssociation = BinaryAssociation(
    name="isForeignKeyToRelation15",
    ends={
        Property(name="databaseMetamodel_Relation17", type=databaseMetamodel_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="databaseMetamodel_Column16", type=databaseMetamodel_Relation, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="databaseMetamodel",
    types={databaseMetamodel_Column, databaseMetamodel_Database, databaseMetamodel_Relation},
    associations={hasColumns1, hasPrimaryKey3, hasForeignKey6, referencesRelation10, relation0, isForeinKeyToColumn13, isForeignKeyToRelation15},
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