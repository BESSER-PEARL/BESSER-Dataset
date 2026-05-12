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
relationaldatabase_NamedElement = Class(name="relationaldatabase_NamedElement", is_abstract=True)
Taggable = Class(name="Taggable")
relationaldatabase_DatabaseModel = Class(name="relationaldatabase_DatabaseModel")
NamedElement = Class(name="NamedElement")
relationaldatabase_Table = Class(name="relationaldatabase_Table")
relationaldatabase_DataType = Class(name="relationaldatabase_DataType")
relationaldatabase_Tag = Class(name="relationaldatabase_Tag")
relationaldatabase_Configuration = Class(name="relationaldatabase_Configuration")
relationaldatabase_Column = Class(name="relationaldatabase_Column")
relationaldatabase_ForeignKey = Class(name="relationaldatabase_ForeignKey")
relationaldatabase_Taggable = Class(name="relationaldatabase_Taggable")

# relationaldatabase_NamedElement class attributes and methods
relationaldatabase_NamedElement_name: Property = Property(name="name", type=StringType)
relationaldatabase_NamedElement_documentation: Property = Property(name="documentation", type=StringType)
relationaldatabase_NamedElement.attributes={relationaldatabase_NamedElement_name, relationaldatabase_NamedElement_documentation}

# Taggable class attributes and methods

# relationaldatabase_DatabaseModel class attributes and methods

# NamedElement class attributes and methods

# relationaldatabase_Table class attributes and methods

# relationaldatabase_DataType class attributes and methods

# relationaldatabase_Tag class attributes and methods
relationaldatabase_Tag_name: Property = Property(name="name", type=StringType)
relationaldatabase_Tag_documentation: Property = Property(name="documentation", type=StringType)
relationaldatabase_Tag.attributes={relationaldatabase_Tag_documentation, relationaldatabase_Tag_name}

# relationaldatabase_Configuration class attributes and methods

# relationaldatabase_Column class attributes and methods
relationaldatabase_Column_nullable: Property = Property(name="nullable", type=BooleanType)
relationaldatabase_Column_primaryKey: Property = Property(name="primaryKey", type=BooleanType)
relationaldatabase_Column_size: Property = Property(name="size", type=StringType)
relationaldatabase_Column_scale: Property = Property(name="scale", type=StringType)
relationaldatabase_Column_arrayDimensions: Property = Property(name="arrayDimensions", type=IntegerType)
relationaldatabase_Column_unique: Property = Property(name="unique", type=BooleanType)
relationaldatabase_Column.attributes={relationaldatabase_Column_arrayDimensions, relationaldatabase_Column_primaryKey, relationaldatabase_Column_size, relationaldatabase_Column_nullable, relationaldatabase_Column_scale, relationaldatabase_Column_unique}

# relationaldatabase_ForeignKey class attributes and methods
relationaldatabase_ForeignKey_sourceLowerBoundary: Property = Property(name="sourceLowerBoundary", type=StringType)
relationaldatabase_ForeignKey_sourceUpperBoundary: Property = Property(name="sourceUpperBoundary", type=StringType)
relationaldatabase_ForeignKey_targetLowerBoundary: Property = Property(name="targetLowerBoundary", type=StringType)
relationaldatabase_ForeignKey_targetUpperBoundary: Property = Property(name="targetUpperBoundary", type=StringType)
relationaldatabase_ForeignKey.attributes={relationaldatabase_ForeignKey_targetLowerBoundary, relationaldatabase_ForeignKey_sourceLowerBoundary, relationaldatabase_ForeignKey_targetUpperBoundary, relationaldatabase_ForeignKey_sourceUpperBoundary}

# relationaldatabase_Taggable class attributes and methods

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="relationaldatabase_Table", type=relationaldatabase_DatabaseModel, multiplicity=Multiplicity(1, 1)),
        Property(name="relationaldatabase_DatabaseModel", type=relationaldatabase_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataTypes1: BinaryAssociation = BinaryAssociation(
    name="dataTypes1",
    ends={
        Property(name="relationaldatabase_DataType", type=relationaldatabase_DatabaseModel, multiplicity=Multiplicity(1, 1)),
        Property(name="relationaldatabase_DatabaseModel2", type=relationaldatabase_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tags3: BinaryAssociation = BinaryAssociation(
    name="tags3",
    ends={
        Property(name="relationaldatabase_Tag", type=relationaldatabase_DatabaseModel, multiplicity=Multiplicity(1, 1)),
        Property(name="relationaldatabase_DatabaseModel4", type=relationaldatabase_Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configuration5: BinaryAssociation = BinaryAssociation(
    name="configuration5",
    ends={
        Property(name="relationaldatabase_Configuration", type=relationaldatabase_DatabaseModel, multiplicity=Multiplicity(1, 1)),
        Property(name="relationaldatabase_DatabaseModel6", type=relationaldatabase_Configuration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columns7: BinaryAssociation = BinaryAssociation(
    name="columns7",
    ends={
        Property(name="relationaldatabase_Column", type=relationaldatabase_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="relationaldatabase_Table8", type=relationaldatabase_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreignKeys9: BinaryAssociation = BinaryAssociation(
    name="foreignKeys9",
    ends={
        Property(name="relationaldatabase_ForeignKey", type=relationaldatabase_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="relationaldatabase_Table10", type=relationaldatabase_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataType11: BinaryAssociation = BinaryAssociation(
    name="dataType11",
    ends={
        Property(name="relationaldatabase_DataType13", type=relationaldatabase_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="relationaldatabase_Column12", type=relationaldatabase_DataType, multiplicity=Multiplicity(1, 1))
    }
)
sourceColumns14: BinaryAssociation = BinaryAssociation(
    name="sourceColumns14",
    ends={
        Property(name="relationaldatabase_Column16", type=relationaldatabase_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="relationaldatabase_ForeignKey15", type=relationaldatabase_Column, multiplicity=Multiplicity(1, 9999))
    }
)
targetColumns17: BinaryAssociation = BinaryAssociation(
    name="targetColumns17",
    ends={
        Property(name="relationaldatabase_Column19", type=relationaldatabase_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="relationaldatabase_ForeignKey18", type=relationaldatabase_Column, multiplicity=Multiplicity(1, 9999))
    }
)
targetTable20: BinaryAssociation = BinaryAssociation(
    name="targetTable20",
    ends={
        Property(name="relationaldatabase_Table22", type=relationaldatabase_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="relationaldatabase_ForeignKey21", type=relationaldatabase_Table, multiplicity=Multiplicity(0, 1))
    }
)
tag23: BinaryAssociation = BinaryAssociation(
    name="tag23",
    ends={
        Property(name="relationaldatabase_Tag24", type=relationaldatabase_Taggable, multiplicity=Multiplicity(1, 1)),
        Property(name="relationaldatabase_Taggable", type=relationaldatabase_Tag, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_relationaldatabase_NamedElement_Taggable = Generalization(general=Taggable, specific=relationaldatabase_NamedElement)
gen_relationaldatabase_DatabaseModel_NamedElement = Generalization(general=NamedElement, specific=relationaldatabase_DatabaseModel)
gen_relationaldatabase_Table_NamedElement = Generalization(general=NamedElement, specific=relationaldatabase_Table)
gen_relationaldatabase_Column_NamedElement = Generalization(general=NamedElement, specific=relationaldatabase_Column)
gen_relationaldatabase_ForeignKey_NamedElement = Generalization(general=NamedElement, specific=relationaldatabase_ForeignKey)
gen_relationaldatabase_DataType_NamedElement = Generalization(general=NamedElement, specific=relationaldatabase_DataType)

# Domain Model
domain_model = DomainModel(
    name="relationaldatabase",
    types={relationaldatabase_NamedElement, Taggable, relationaldatabase_DatabaseModel, NamedElement, relationaldatabase_Table, relationaldatabase_DataType, relationaldatabase_Tag, relationaldatabase_Configuration, relationaldatabase_Column, relationaldatabase_ForeignKey, relationaldatabase_Taggable},
    associations={tables0, dataTypes1, tags3, configuration5, columns7, foreignKeys9, dataType11, sourceColumns14, targetColumns17, targetTable20, tag23},
    generalizations={gen_relationaldatabase_NamedElement_Taggable, gen_relationaldatabase_DatabaseModel_NamedElement, gen_relationaldatabase_Table_NamedElement, gen_relationaldatabase_Column_NamedElement, gen_relationaldatabase_ForeignKey_NamedElement, gen_relationaldatabase_DataType_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)