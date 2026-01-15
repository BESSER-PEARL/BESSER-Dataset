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
relationalMetaModel_RelationalSchema = Class(name="relationalMetaModel::RelationalSchema")
relationalMetaModel_RelationalTable = Class(name="relationalMetaModel::RelationalTable")
relationalMetaModel_RelationalForeignKey = Class(name="relationalMetaModel::RelationalForeignKey")

# relationalMetaModel_RelationalSchema class attributes and methods
relationalMetaModel_RelationalSchema_Name: Property = Property(name="Name", type=StringType)
relationalMetaModel_RelationalSchema.attributes={relationalMetaModel_RelationalSchema_Name}

# relationalMetaModel_RelationalTable class attributes and methods
relationalMetaModel_RelationalTable_Name: Property = Property(name="Name", type=StringType)
relationalMetaModel_RelationalTable.attributes={relationalMetaModel_RelationalTable_Name}

# relationalMetaModel_RelationalForeignKey class attributes and methods
relationalMetaModel_RelationalForeignKey_Name: Property = Property(name="Name", type=StringType)
relationalMetaModel_RelationalForeignKey.attributes={relationalMetaModel_RelationalForeignKey_Name}

# Relationships
Tables0: BinaryAssociation = BinaryAssociation(
    name="Tables0",
    ends={
        Property(name="RelationalTable", type=relationalMetaModel_RelationalSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="Schema", type=relationalMetaModel_RelationalTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Schema1: BinaryAssociation = BinaryAssociation(
    name="Schema1",
    ends={
        Property(name="RelationalSchema", type=relationalMetaModel_RelationalTable, multiplicity=Multiplicity(1, 1)),
        Property(name="Tables", type=relationalMetaModel_RelationalSchema, multiplicity=Multiplicity(1, 1))
    }
)
ForeignKeys2: BinaryAssociation = BinaryAssociation(
    name="ForeignKeys2",
    ends={
        Property(name="RelationalForeignKey", type=relationalMetaModel_RelationalTable, multiplicity=Multiplicity(1, 1)),
        Property(name="OwnedByTable", type=relationalMetaModel_RelationalForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ReferencedBy3: BinaryAssociation = BinaryAssociation(
    name="ReferencedBy3",
    ends={
        Property(name="RelationalForeignKey4", type=relationalMetaModel_RelationalTable, multiplicity=Multiplicity(1, 1)),
        Property(name="ReferencedTable", type=relationalMetaModel_RelationalForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
OwnedByTable5: BinaryAssociation = BinaryAssociation(
    name="OwnedByTable5",
    ends={
        Property(name="RelationalTable6", type=relationalMetaModel_RelationalForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="ForeignKeys", type=relationalMetaModel_RelationalTable, multiplicity=Multiplicity(1, 1))
    }
)
ReferencedTable7: BinaryAssociation = BinaryAssociation(
    name="ReferencedTable7",
    ends={
        Property(name="RelationalTable8", type=relationalMetaModel_RelationalForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="ReferencedBy", type=relationalMetaModel_RelationalTable, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="relationalMetaModel",
    types={relationalMetaModel_RelationalSchema, relationalMetaModel_RelationalTable, relationalMetaModel_RelationalForeignKey},
    associations={Tables0, Schema1, ForeignKeys2, ReferencedBy3, OwnedByTable5, ReferencedTable7},
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