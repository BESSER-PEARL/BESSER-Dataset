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
SqlDataType: Enumeration = Enumeration(
    name="SqlDataType",
    literals={
            EnumerationLiteral(name="VARCHAR"),
			EnumerationLiteral(name="CHAR"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="DATE")
    }
)

# Classes
relational_Schema = Class(name="relational_Schema")
relational_PrimaryKey = Class(name="relational_PrimaryKey")
Key = Class(name="Key")
relational_ForeignKey = Class(name="relational_ForeignKey")
relational_RelationalEntity = Class(name="relational_RelationalEntity", is_abstract=True)
relational_Key = Class(name="relational_Key", is_abstract=True)
relational_View = Class(name="relational_View")
Table = Class(name="Table")
relational_Table = Class(name="relational_Table")
RelationalEntity = Class(name="RelationalEntity")
relational_Column = Class(name="relational_Column")

# relational_Schema class attributes and methods

# relational_PrimaryKey class attributes and methods

# Key class attributes and methods

# relational_ForeignKey class attributes and methods

# relational_RelationalEntity class attributes and methods

# relational_Key class attributes and methods

# relational_View class attributes and methods

# Table class attributes and methods

# relational_Table class attributes and methods

# RelationalEntity class attributes and methods

# relational_Column class attributes and methods

# Generalizations
gen_relational_Schema_RelationalEntity = Generalization(general=RelationalEntity, specific=relational_Schema)
gen_relational_PrimaryKey_Key = Generalization(general=Key, specific=relational_PrimaryKey)
gen_relational_ForeignKey_Key = Generalization(general=Key, specific=relational_ForeignKey)
gen_relational_Key_RelationalEntity = Generalization(general=RelationalEntity, specific=relational_Key)
gen_relational_View_Table = Generalization(general=Table, specific=relational_View)
gen_relational_Table_RelationalEntity = Generalization(general=RelationalEntity, specific=relational_Table)
gen_relational_Column_RelationalEntity = Generalization(general=RelationalEntity, specific=relational_Column)

# Domain Model
domain_model = DomainModel(
    name="relational",
    types={relational_Schema, relational_PrimaryKey, Key, relational_ForeignKey, relational_RelationalEntity, relational_Key, relational_View, Table, relational_Table, RelationalEntity, relational_Column, SqlDataType},
    associations={},
    generalizations={gen_relational_Schema_RelationalEntity, gen_relational_PrimaryKey_Key, gen_relational_ForeignKey_Key, gen_relational_Key_RelationalEntity, gen_relational_View_Table, gen_relational_Table_RelationalEntity, gen_relational_Column_RelationalEntity},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)