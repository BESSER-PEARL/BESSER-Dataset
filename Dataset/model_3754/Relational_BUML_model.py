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
            EnumerationLiteral(name="VARCHAR"),
			EnumerationLiteral(name="NUMERIC"),
			EnumerationLiteral(name="DATE"),
			EnumerationLiteral(name="TIME"),
			EnumerationLiteral(name="FLOAT"),
			EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="CHAR")
    }
)

# Classes
relational_DataBase = Class(name="relational::DataBase")
relational_Schema = Class(name="relational::Schema")
relational_PrimaryKey = Class(name="relational::PrimaryKey")
Field = Class(name="Field")
relational_ForeignKey = Class(name="relational::ForeignKey")
relational_Table = Class(name="relational::Table")
relational_Field = Class(name="relational::Field", is_abstract=True)
relational_Column = Class(name="relational::Column")

# relational_DataBase class attributes and methods
relational_DataBase_uri: Property = Property(name="uri", type=StringType)
relational_DataBase_port: Property = Property(name="port", type=IntegerType)
relational_DataBase.attributes={relational_DataBase_uri, relational_DataBase_port}

# relational_Schema class attributes and methods
relational_Schema_name: Property = Property(name="name", type=StringType)
relational_Schema.attributes={relational_Schema_name}

# relational_PrimaryKey class attributes and methods
relational_PrimaryKey_id: Property = Property(name="id", type=StringType)
relational_PrimaryKey.attributes={relational_PrimaryKey_id}

# Field class attributes and methods

# relational_ForeignKey class attributes and methods

# relational_Table class attributes and methods
relational_Table_name: Property = Property(name="name", type=StringType)
relational_Table.attributes={relational_Table_name}

# relational_Field class attributes and methods
relational_Field_name: Property = Property(name="name", type=StringType)
relational_Field.attributes={relational_Field_name}

# relational_Column class attributes and methods
relational_Column_type: Property = Property(name="type", type=StringType)
relational_Column.attributes={relational_Column_type}

# Relationships
schemas0: BinaryAssociation = BinaryAssociation(
    name="schemas0",
    ends={
        Property(name="relational_Schema", type=relational_DataBase, multiplicity=Multiplicity(1, 1)),
        Property(name="relational_DataBase", type=relational_Schema, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables1: BinaryAssociation = BinaryAssociation(
    name="tables1",
    ends={
        Property(name="relational_Table", type=relational_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="relational_Schema2", type=relational_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields3: BinaryAssociation = BinaryAssociation(
    name="fields3",
    ends={
        Property(name="relational_Field", type=relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="relational_Table4", type=relational_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference5: BinaryAssociation = BinaryAssociation(
    name="reference5",
    ends={
        Property(name="relational_Table6", type=relational_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="relational_ForeignKey", type=relational_Table, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_relational_PrimaryKey_Field = Generalization(general=Field, specific=relational_PrimaryKey)
gen_relational_ForeignKey_Field = Generalization(general=Field, specific=relational_ForeignKey)
gen_relational_Column_Field = Generalization(general=Field, specific=relational_Column)

# Domain Model
domain_model = DomainModel(
    name="relational",
    types={relational_DataBase, relational_Schema, relational_PrimaryKey, Field, relational_ForeignKey, relational_Table, relational_Field, relational_Column, Type},
    associations={schemas0, tables1, fields3, reference5},
    generalizations={gen_relational_PrimaryKey_Field, gen_relational_ForeignKey_Field, gen_relational_Column_Field},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)