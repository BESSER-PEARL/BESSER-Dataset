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
DbMddAndroid_Table = Class(name="DbMddAndroid::Table")
DbMddAndroid_Relation = Class(name="DbMddAndroid::Relation")
DbMddAndroid_Column = Class(name="DbMddAndroid::Column")
DbMddAndroid_DBScheme = Class(name="DbMddAndroid::DBScheme")
NamedElement = Class(name="NamedElement")
DbMddAndroid_NamedElement = Class(name="DbMddAndroid::NamedElement", is_abstract=True)

# DbMddAndroid_Table class attributes and methods

# DbMddAndroid_Relation class attributes and methods
DbMddAndroid_Relation_minSourceMultiplicity: Property = Property(name="minSourceMultiplicity", type=IntegerType)
DbMddAndroid_Relation_maxSourceMultiplicity: Property = Property(name="maxSourceMultiplicity", type=IntegerType)
DbMddAndroid_Relation_minTargetMultiplicity: Property = Property(name="minTargetMultiplicity", type=IntegerType)
DbMddAndroid_Relation_maxTargetMultiplicity: Property = Property(name="maxTargetMultiplicity", type=IntegerType)
DbMddAndroid_Relation.attributes={DbMddAndroid_Relation_minSourceMultiplicity, DbMddAndroid_Relation_maxTargetMultiplicity, DbMddAndroid_Relation_minTargetMultiplicity, DbMddAndroid_Relation_maxSourceMultiplicity}

# DbMddAndroid_Column class attributes and methods
DbMddAndroid_Column_type: Property = Property(name="type", type=StringType)
DbMddAndroid_Column.attributes={DbMddAndroid_Column_type}

# DbMddAndroid_DBScheme class attributes and methods

# NamedElement class attributes and methods

# DbMddAndroid_NamedElement class attributes and methods
DbMddAndroid_NamedElement_name: Property = Property(name="name", type=StringType)
DbMddAndroid_NamedElement.attributes={DbMddAndroid_NamedElement_name}

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="DbMddAndroid_Table", type=DbMddAndroid_DBScheme, multiplicity=Multiplicity(1, 1)),
        Property(name="DbMddAndroid_DBScheme", type=DbMddAndroid_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relations1: BinaryAssociation = BinaryAssociation(
    name="relations1",
    ends={
        Property(name="DbMddAndroid_Relation", type=DbMddAndroid_DBScheme, multiplicity=Multiplicity(1, 1)),
        Property(name="DbMddAndroid_DBScheme2", type=DbMddAndroid_Relation, multiplicity=Multiplicity(0, 9999))
    }
)
columns3: BinaryAssociation = BinaryAssociation(
    name="columns3",
    ends={
        Property(name="DbMddAndroid_Column", type=DbMddAndroid_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DbMddAndroid_Table4", type=DbMddAndroid_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryKey5: BinaryAssociation = BinaryAssociation(
    name="primaryKey5",
    ends={
        Property(name="DbMddAndroid_Column7", type=DbMddAndroid_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="DbMddAndroid_Table6", type=DbMddAndroid_Column, multiplicity=Multiplicity(0, 1))
    }
)
source11: BinaryAssociation = BinaryAssociation(
    name="source11",
    ends={
        Property(name="outRelation", type=DbMddAndroid_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="Table", type=DbMddAndroid_Relation, multiplicity=Multiplicity(1, 1))
    }
)
target12: BinaryAssociation = BinaryAssociation(
    name="target12",
    ends={
        Property(name="Table13", type=DbMddAndroid_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="inRelation", type=DbMddAndroid_Table, multiplicity=Multiplicity(1, 1))
    }
)
outRelation8: BinaryAssociation = BinaryAssociation(
    name="outRelation8",
    ends={
        Property(name="Relation", type=DbMddAndroid_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=DbMddAndroid_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inRelation9: BinaryAssociation = BinaryAssociation(
    name="inRelation9",
    ends={
        Property(name="Relation10", type=DbMddAndroid_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=DbMddAndroid_Relation, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_DbMddAndroid_Table_NamedElement = Generalization(general=NamedElement, specific=DbMddAndroid_Table)
gen_DbMddAndroid_DBScheme_NamedElement = Generalization(general=NamedElement, specific=DbMddAndroid_DBScheme)
gen_DbMddAndroid_Column_NamedElement = Generalization(general=NamedElement, specific=DbMddAndroid_Column)

# Domain Model
domain_model = DomainModel(
    name="DbMddAndroid",
    types={DbMddAndroid_Table, DbMddAndroid_Relation, DbMddAndroid_Column, DbMddAndroid_DBScheme, NamedElement, DbMddAndroid_NamedElement},
    associations={tables0, relations1, columns3, primaryKey5, source11, target12, outRelation8, inRelation9},
    generalizations={gen_DbMddAndroid_Table_NamedElement, gen_DbMddAndroid_DBScheme_NamedElement, gen_DbMddAndroid_Column_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)