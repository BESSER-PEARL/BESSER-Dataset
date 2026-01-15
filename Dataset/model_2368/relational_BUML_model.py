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
relational_4relational2UML_Column = Class(name="relational::4relational2UML::Column")
relational_4relational2UML_ForeignKey = Class(name="relational::4relational2UML::ForeignKey")
relational_4relational2UML_Database = Class(name="relational::4relational2UML::Database")
ModelElement = Class(name="ModelElement")
relational_4relational2UML_Schema = Class(name="relational::4relational2UML::Schema")
relational_4relational2UML_Table = Class(name="relational::4relational2UML::Table")
relational_4relational2UML_ModelElement = Class(name="relational::4relational2UML::ModelElement", is_abstract=True)

# relational_4relational2UML_Column class attributes and methods
relational_4relational2UML_Column_name: Property = Property(name="name", type=StringType)
relational_4relational2UML_Column_type: Property = Property(name="type", type=StringType)
relational_4relational2UML_Column_isPrimaryKey: Property = Property(name="isPrimaryKey", type=BooleanType)
relational_4relational2UML_Column_isUnique: Property = Property(name="isUnique", type=BooleanType)
relational_4relational2UML_Column.attributes={relational_4relational2UML_Column_isUnique, relational_4relational2UML_Column_name, relational_4relational2UML_Column_isPrimaryKey, relational_4relational2UML_Column_type}

# relational_4relational2UML_ForeignKey class attributes and methods
relational_4relational2UML_ForeignKey_name: Property = Property(name="name", type=StringType)
relational_4relational2UML_ForeignKey.attributes={relational_4relational2UML_ForeignKey_name}

# relational_4relational2UML_Database class attributes and methods
relational_4relational2UML_Database_name: Property = Property(name="name", type=StringType)
relational_4relational2UML_Database_url: Property = Property(name="url", type=StringType)
relational_4relational2UML_Database.attributes={relational_4relational2UML_Database_name, relational_4relational2UML_Database_url}

# ModelElement class attributes and methods

# relational_4relational2UML_Schema class attributes and methods
relational_4relational2UML_Schema_name: Property = Property(name="name", type=StringType)
relational_4relational2UML_Schema.attributes={relational_4relational2UML_Schema_name}

# relational_4relational2UML_Table class attributes and methods
relational_4relational2UML_Table_name: Property = Property(name="name", type=StringType)
relational_4relational2UML_Table.attributes={relational_4relational2UML_Table_name}

# relational_4relational2UML_ModelElement class attributes and methods
relational_4relational2UML_ModelElement_comment: Property = Property(name="comment", type=StringType)
relational_4relational2UML_ModelElement.attributes={relational_4relational2UML_ModelElement_comment}

# Relationships
ownedColumns4: BinaryAssociation = BinaryAssociation(
    name="ownedColumns4",
    ends={
        Property(name="Column", type=relational_4relational2UML_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner5", type=relational_4relational2UML_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedForeignKeys6: BinaryAssociation = BinaryAssociation(
    name="ownedForeignKeys6",
    ends={
        Property(name="ForeignKey", type=relational_4relational2UML_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignTable", type=relational_4relational2UML_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner7: BinaryAssociation = BinaryAssociation(
    name="owner7",
    ends={
        Property(name="Schema8", type=relational_4relational2UML_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTables", type=relational_4relational2UML_Schema, multiplicity=Multiplicity(1, 1))
    }
)
ownedSchemas0: BinaryAssociation = BinaryAssociation(
    name="ownedSchemas0",
    ends={
        Property(name="Schema", type=relational_4relational2UML_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=relational_4relational2UML_Schema, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreignTable9: BinaryAssociation = BinaryAssociation(
    name="foreignTable9",
    ends={
        Property(name="Table10", type=relational_4relational2UML_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedForeignKeys", type=relational_4relational2UML_Table, multiplicity=Multiplicity(1, 1))
    }
)
ownedTables1: BinaryAssociation = BinaryAssociation(
    name="ownedTables1",
    ends={
        Property(name="Table", type=relational_4relational2UML_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="owner2", type=relational_4relational2UML_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner3: BinaryAssociation = BinaryAssociation(
    name="owner3",
    ends={
        Property(name="Database", type=relational_4relational2UML_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedSchemas", type=relational_4relational2UML_Database, multiplicity=Multiplicity(1, 1))
    }
)
sourceTable11: BinaryAssociation = BinaryAssociation(
    name="sourceTable11",
    ends={
        Property(name="relational_4relational2UML_Table", type=relational_4relational2UML_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="relational_4relational2UML_ForeignKey", type=relational_4relational2UML_Table, multiplicity=Multiplicity(1, 1))
    }
)
owner12: BinaryAssociation = BinaryAssociation(
    name="owner12",
    ends={
        Property(name="Table13", type=relational_4relational2UML_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedColumns", type=relational_4relational2UML_Table, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_relational_4relational2UML_Database_ModelElement = Generalization(general=ModelElement, specific=relational_4relational2UML_Database)
gen_relational_4relational2UML_ForeignKey_ModelElement = Generalization(general=ModelElement, specific=relational_4relational2UML_ForeignKey)
gen_relational_4relational2UML_Schema_ModelElement = Generalization(general=ModelElement, specific=relational_4relational2UML_Schema)
gen_relational_4relational2UML_Table_ModelElement = Generalization(general=ModelElement, specific=relational_4relational2UML_Table)
gen_relational_4relational2UML_Column_ModelElement = Generalization(general=ModelElement, specific=relational_4relational2UML_Column)

# Domain Model
domain_model = DomainModel(
    name="relational_4relational2UML",
    types={relational_4relational2UML_Column, relational_4relational2UML_ForeignKey, relational_4relational2UML_Database, ModelElement, relational_4relational2UML_Schema, relational_4relational2UML_Table, relational_4relational2UML_ModelElement, Type},
    associations={ownedColumns4, ownedForeignKeys6, owner7, ownedSchemas0, foreignTable9, ownedTables1, owner3, sourceTable11, owner12},
    generalizations={gen_relational_4relational2UML_Database_ModelElement, gen_relational_4relational2UML_ForeignKey_ModelElement, gen_relational_4relational2UML_Schema_ModelElement, gen_relational_4relational2UML_Table_ModelElement, gen_relational_4relational2UML_Column_ModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)