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
dbmddandroid_DBScheme = Class(name="dbmddandroid::DBScheme")
NamedElement = Class(name="NamedElement")
dbmddandroid_Table = Class(name="dbmddandroid::Table")
dbmddandroid_Relation = Class(name="dbmddandroid::Relation")
dbmddandroid_Column = Class(name="dbmddandroid::Column")
dbmddandroid_NamedElement = Class(name="dbmddandroid::NamedElement", is_abstract=True)

# dbmddandroid_DBScheme class attributes and methods

# NamedElement class attributes and methods

# dbmddandroid_Table class attributes and methods

# dbmddandroid_Relation class attributes and methods
dbmddandroid_Relation_minSourceMultiplicity: Property = Property(name="minSourceMultiplicity", type=IntegerType)
dbmddandroid_Relation_maxSourceMultiplicity: Property = Property(name="maxSourceMultiplicity", type=IntegerType)
dbmddandroid_Relation_minTargetMultiplicity: Property = Property(name="minTargetMultiplicity", type=IntegerType)
dbmddandroid_Relation_maxTargetMultiplicity: Property = Property(name="maxTargetMultiplicity", type=IntegerType)
dbmddandroid_Relation.attributes={dbmddandroid_Relation_maxTargetMultiplicity, dbmddandroid_Relation_minSourceMultiplicity, dbmddandroid_Relation_minTargetMultiplicity, dbmddandroid_Relation_maxSourceMultiplicity}

# dbmddandroid_Column class attributes and methods
dbmddandroid_Column_type: Property = Property(name="type", type=StringType)
dbmddandroid_Column.attributes={dbmddandroid_Column_type}

# dbmddandroid_NamedElement class attributes and methods
dbmddandroid_NamedElement_name: Property = Property(name="name", type=StringType)
dbmddandroid_NamedElement.attributes={dbmddandroid_NamedElement_name}

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="dbmddandroid_Table", type=dbmddandroid_DBScheme, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmddandroid_DBScheme", type=dbmddandroid_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations1: BinaryAssociation = BinaryAssociation(
    name="relations1",
    ends={
        Property(name="dbmddandroid_Relation", type=dbmddandroid_DBScheme, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmddandroid_DBScheme2", type=dbmddandroid_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns3: BinaryAssociation = BinaryAssociation(
    name="columns3",
    ends={
        Property(name="dbmddandroid_Column", type=dbmddandroid_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="dbmddandroid_Table4", type=dbmddandroid_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outRelation5: BinaryAssociation = BinaryAssociation(
    name="outRelation5",
    ends={
        Property(name="Relation", type=dbmddandroid_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=dbmddandroid_Relation, multiplicity=Multiplicity(0, 9999))
    }
)
inRelation6: BinaryAssociation = BinaryAssociation(
    name="inRelation6",
    ends={
        Property(name="Relation7", type=dbmddandroid_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=dbmddandroid_Relation, multiplicity=Multiplicity(0, 9999))
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="Table", type=dbmddandroid_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="outRelation", type=dbmddandroid_Table, multiplicity=Multiplicity(1, 1))
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="Table10", type=dbmddandroid_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="inRelation", type=dbmddandroid_Table, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_dbmddandroid_DBScheme_NamedElement = Generalization(general=NamedElement, specific=dbmddandroid_DBScheme)
gen_dbmddandroid_Table_NamedElement = Generalization(general=NamedElement, specific=dbmddandroid_Table)
gen_dbmddandroid_Column_NamedElement = Generalization(general=NamedElement, specific=dbmddandroid_Column)

# Domain Model
domain_model = DomainModel(
    name="dbmddandroid",
    types={dbmddandroid_DBScheme, NamedElement, dbmddandroid_Table, dbmddandroid_Relation, dbmddandroid_Column, dbmddandroid_NamedElement},
    associations={tables0, relations1, columns3, outRelation5, inRelation6, source8, target9},
    generalizations={gen_dbmddandroid_DBScheme_NamedElement, gen_dbmddandroid_Table_NamedElement, gen_dbmddandroid_Column_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)