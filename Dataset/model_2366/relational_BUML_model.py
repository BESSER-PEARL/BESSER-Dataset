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
Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="NUMERIC"),
			EnumerationLiteral(name="VARCHAR"),
			EnumerationLiteral(name="DATE"),
			EnumerationLiteral(name="TIME"),
			EnumerationLiteral(name="FLOAT"),
			EnumerationLiteral(name="CHAR")
    }
)

# Classes
relational_Database = Class(name="relational::Database")
ModelElement = Class(name="ModelElement")
relational_Schema = Class(name="relational::Schema")
relational_Table = Class(name="relational::Table")
relational_Column = Class(name="relational::Column")
relational_ForeignKey = Class(name="relational::ForeignKey")
relational_ModelElement = Class(name="relational::ModelElement", is_abstract=True)

# relational_Database class attributes and methods
relational_Database_name: Property = Property(name="name", type=StringType)
relational_Database_url: Property = Property(name="url", type=StringType)
relational_Database.attributes={relational_Database_url, relational_Database_name}

# ModelElement class attributes and methods

# relational_Schema class attributes and methods
relational_Schema_name: Property = Property(name="name", type=StringType)
relational_Schema.attributes={relational_Schema_name}

# relational_Table class attributes and methods
relational_Table_name: Property = Property(name="name", type=StringType)
relational_Table.attributes={relational_Table_name}

# relational_Column class attributes and methods
relational_Column_name: Property = Property(name="name", type=StringType)
relational_Column_type: Property = Property(name="type", type=StringType)
relational_Column_isPrimaryKey: Property = Property(name="isPrimaryKey", type=BooleanType)
relational_Column_isUnique: Property = Property(name="isUnique", type=BooleanType)
relational_Column.attributes={relational_Column_name, relational_Column_type, relational_Column_isPrimaryKey, relational_Column_isUnique}

# relational_ForeignKey class attributes and methods
relational_ForeignKey_name: Property = Property(name="name", type=StringType)
relational_ForeignKey.attributes={relational_ForeignKey_name}

# relational_ModelElement class attributes and methods
relational_ModelElement_comment: Property = Property(name="comment", type=StringType)
relational_ModelElement.attributes={relational_ModelElement_comment}

# Relationships
ownedSchemas0: BinaryAssociation = BinaryAssociation(
    name="ownedSchemas0",
    ends={
        Property(name="Schema", type=relational_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=relational_Schema, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTables1: BinaryAssociation = BinaryAssociation(
    name="ownedTables1",
    ends={
        Property(name="Table", type=relational_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="owner2", type=relational_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner3: BinaryAssociation = BinaryAssociation(
    name="owner3",
    ends={
        Property(name="Database", type=relational_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedSchemas", type=relational_Database, multiplicity=Multiplicity(1, 1))
    }
)
ownedColumns4: BinaryAssociation = BinaryAssociation(
    name="ownedColumns4",
    ends={
        Property(name="Column", type=relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner5", type=relational_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedForeignKeys6: BinaryAssociation = BinaryAssociation(
    name="ownedForeignKeys6",
    ends={
        Property(name="ForeignKey", type=relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignTable", type=relational_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner7: BinaryAssociation = BinaryAssociation(
    name="owner7",
    ends={
        Property(name="Schema8", type=relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTables", type=relational_Schema, multiplicity=Multiplicity(1, 1))
    }
)
foreignTable9: BinaryAssociation = BinaryAssociation(
    name="foreignTable9",
    ends={
        Property(name="Table10", type=relational_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedForeignKeys", type=relational_Table, multiplicity=Multiplicity(1, 1))
    }
)
sourceTable11: BinaryAssociation = BinaryAssociation(
    name="sourceTable11",
    ends={
        Property(name="relational_Table", type=relational_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="relational_ForeignKey", type=relational_Table, multiplicity=Multiplicity(1, 1))
    }
)
owner12: BinaryAssociation = BinaryAssociation(
    name="owner12",
    ends={
        Property(name="Table13", type=relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedColumns", type=relational_Table, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_relational_Database_ModelElement = Generalization(general=ModelElement, specific=relational_Database)
gen_relational_Schema_ModelElement = Generalization(general=ModelElement, specific=relational_Schema)
gen_relational_Table_ModelElement = Generalization(general=ModelElement, specific=relational_Table)
gen_relational_ForeignKey_ModelElement = Generalization(general=ModelElement, specific=relational_ForeignKey)
gen_relational_Column_ModelElement = Generalization(general=ModelElement, specific=relational_Column)

# Domain Model
domain_model = DomainModel(
    name="relational",
    types={relational_Database, ModelElement, relational_Schema, relational_Table, relational_Column, relational_ForeignKey, relational_ModelElement, Type},
    associations={ownedSchemas0, ownedTables1, owner3, ownedColumns4, ownedForeignKeys6, owner7, foreignTable9, sourceTable11, owner12},
    generalizations={gen_relational_Database_ModelElement, gen_relational_Schema_ModelElement, gen_relational_Table_ModelElement, gen_relational_ForeignKey_ModelElement, gen_relational_Column_ModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)