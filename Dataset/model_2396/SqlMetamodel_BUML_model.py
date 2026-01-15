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
TypeData: Enumeration = Enumeration(
    name="TypeData",
    literals={
            EnumerationLiteral(name="INT"),
			EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="DOUBLE"),
			EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="FLOAT"),
			EnumerationLiteral(name="DATE")
    }
)

# Classes
SqlMetamodel_Schema = Class(name="SqlMetamodel::Schema")
SqlMetamodel_Table = Class(name="SqlMetamodel::Table")
SqlMetamodel_Constraint = Class(name="SqlMetamodel::Constraint")
SqlMetamodel_PrimaryKey = Class(name="SqlMetamodel::PrimaryKey")
SqlMetamodel_ForeingKey = Class(name="SqlMetamodel::ForeingKey")
Constraint = Class(name="Constraint")
SqlMetamodel_Column = Class(name="SqlMetamodel::Column")

# SqlMetamodel_Schema class attributes and methods
SqlMetamodel_Schema_name: Property = Property(name="name", type=StringType)
SqlMetamodel_Schema.attributes={SqlMetamodel_Schema_name}

# SqlMetamodel_Table class attributes and methods
SqlMetamodel_Table_name: Property = Property(name="name", type=StringType)
SqlMetamodel_Table.attributes={SqlMetamodel_Table_name}

# SqlMetamodel_Constraint class attributes and methods
SqlMetamodel_Constraint_name: Property = Property(name="name", type=StringType)
SqlMetamodel_Constraint.attributes={SqlMetamodel_Constraint_name}

# SqlMetamodel_PrimaryKey class attributes and methods

# SqlMetamodel_ForeingKey class attributes and methods

# Constraint class attributes and methods

# SqlMetamodel_Column class attributes and methods
SqlMetamodel_Column_name: Property = Property(name="name", type=StringType)
SqlMetamodel_Column_type: Property = Property(name="type", type=StringType)
SqlMetamodel_Column_nullable: Property = Property(name="nullable", type=BooleanType)
SqlMetamodel_Column.attributes={SqlMetamodel_Column_nullable, SqlMetamodel_Column_name, SqlMetamodel_Column_type}

# Relationships
table0: BinaryAssociation = BinaryAssociation(
    name="table0",
    ends={
        Property(name="SqlMetamodel_Table", type=SqlMetamodel_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="SqlMetamodel_Schema", type=SqlMetamodel_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraint3: BinaryAssociation = BinaryAssociation(
    name="constraint3",
    ends={
        Property(name="SqlMetamodel_Constraint", type=SqlMetamodel_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="SqlMetamodel_Table4", type=SqlMetamodel_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryKey5: BinaryAssociation = BinaryAssociation(
    name="primaryKey5",
    ends={
        Property(name="SqlMetamodel_PrimaryKey", type=SqlMetamodel_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="SqlMetamodel_Table6", type=SqlMetamodel_PrimaryKey, multiplicity=Multiplicity(1, 1))
    }
)
refTable7: BinaryAssociation = BinaryAssociation(
    name="refTable7",
    ends={
        Property(name="SqlMetamodel_Table8", type=SqlMetamodel_ForeingKey, multiplicity=Multiplicity(1, 1)),
        Property(name="SqlMetamodel_ForeingKey", type=SqlMetamodel_Table, multiplicity=Multiplicity(1, 1))
    }
)
column1: BinaryAssociation = BinaryAssociation(
    name="column1",
    ends={
        Property(name="SqlMetamodel_Column", type=SqlMetamodel_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="SqlMetamodel_Table2", type=SqlMetamodel_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_SqlMetamodel_ForeingKey_Constraint = Generalization(general=Constraint, specific=SqlMetamodel_ForeingKey)
gen_SqlMetamodel_PrimaryKey_Constraint = Generalization(general=Constraint, specific=SqlMetamodel_PrimaryKey)

# Domain Model
domain_model = DomainModel(
    name="SqlMetamodel",
    types={SqlMetamodel_Schema, SqlMetamodel_Table, SqlMetamodel_Constraint, SqlMetamodel_PrimaryKey, SqlMetamodel_ForeingKey, Constraint, SqlMetamodel_Column, TypeData},
    associations={table0, constraint3, primaryKey5, refTable7, column1},
    generalizations={gen_SqlMetamodel_ForeingKey_Constraint, gen_SqlMetamodel_PrimaryKey_Constraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)