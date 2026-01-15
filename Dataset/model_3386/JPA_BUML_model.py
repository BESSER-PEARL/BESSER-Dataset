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
Fetch: Enumeration = Enumeration(
    name="Fetch",
    literals={
            EnumerationLiteral(name="LAZY"),
			EnumerationLiteral(name="EAGER")
    }
)

Cascade: Enumeration = Enumeration(
    name="Cascade",
    literals={
            EnumerationLiteral(name="PERSIST"),
			EnumerationLiteral(name="REMOVE"),
			EnumerationLiteral(name="REFRESH"),
			EnumerationLiteral(name="MERGE"),
			EnumerationLiteral(name="ALL")
    }
)

# Classes
JPA_Property = Class(name="JPA::Property")
JPA_Anotation = Class(name="JPA::Anotation")
JPA_PersistenceUnit = Class(name="JPA::PersistenceUnit")
JPA_Entity = Class(name="JPA::Entity")
JPA_Column = Class(name="JPA::Column")
JPA_OneToOne = Class(name="JPA::OneToOne")
JPA_EntityPk = Class(name="JPA::EntityPk")
Anotation = Class(name="Anotation")
JPA_Table = Class(name="JPA::Table")
JPA_OneToMany = Class(name="JPA::OneToMany")
JPA_ManyToOne = Class(name="JPA::ManyToOne")
JPA_ManyToMany = Class(name="JPA::ManyToMany")

# JPA_Property class attributes and methods
JPA_Property_name: Property = Property(name="name", type=StringType)
JPA_Property_comment: Property = Property(name="comment", type=StringType)
JPA_Property.attributes={JPA_Property_name, JPA_Property_comment}

# JPA_Anotation class attributes and methods

# JPA_PersistenceUnit class attributes and methods

# JPA_Entity class attributes and methods
JPA_Entity_comment: Property = Property(name="comment", type=StringType)
JPA_Entity_name: Property = Property(name="name", type=StringType)
JPA_Entity.attributes={JPA_Entity_name, JPA_Entity_comment}

# JPA_Column class attributes and methods
JPA_Column_name: Property = Property(name="name", type=StringType)
JPA_Column_type: Property = Property(name="type", type=StringType)
JPA_Column_nullable: Property = Property(name="nullable", type=BooleanType)
JPA_Column_fetch: Property = Property(name="fetch", type=StringType)
JPA_Column.attributes={JPA_Column_nullable, JPA_Column_fetch, JPA_Column_name, JPA_Column_type}

# JPA_OneToOne class attributes and methods
JPA_OneToOne_name: Property = Property(name="name", type=StringType)
JPA_OneToOne_referencedPropertyName: Property = Property(name="referencedPropertyName", type=StringType)
JPA_OneToOne_referencedEntityName: Property = Property(name="referencedEntityName", type=StringType)
JPA_OneToOne_type: Property = Property(name="type", type=StringType)
JPA_OneToOne.attributes={JPA_OneToOne_name, JPA_OneToOne_referencedPropertyName, JPA_OneToOne_type, JPA_OneToOne_referencedEntityName}

# JPA_EntityPk class attributes and methods
JPA_EntityPk_name: Property = Property(name="name", type=StringType)
JPA_EntityPk.attributes={JPA_EntityPk_name}

# Anotation class attributes and methods

# JPA_Table class attributes and methods
JPA_Table_name: Property = Property(name="name", type=StringType)
JPA_Table.attributes={JPA_Table_name}

# JPA_OneToMany class attributes and methods
JPA_OneToMany_name: Property = Property(name="name", type=StringType)
JPA_OneToMany_referencedEntityName: Property = Property(name="referencedEntityName", type=StringType)
JPA_OneToMany_type: Property = Property(name="type", type=StringType)
JPA_OneToMany.attributes={JPA_OneToMany_type, JPA_OneToMany_name, JPA_OneToMany_referencedEntityName}

# JPA_ManyToOne class attributes and methods
JPA_ManyToOne_name: Property = Property(name="name", type=StringType)
JPA_ManyToOne_referencedPropertyName: Property = Property(name="referencedPropertyName", type=StringType)
JPA_ManyToOne_referencedEntityName: Property = Property(name="referencedEntityName", type=StringType)
JPA_ManyToOne_type: Property = Property(name="type", type=StringType)
JPA_ManyToOne.attributes={JPA_ManyToOne_name, JPA_ManyToOne_type, JPA_ManyToOne_referencedEntityName, JPA_ManyToOne_referencedPropertyName}

# JPA_ManyToMany class attributes and methods

# Relationships
properties1: BinaryAssociation = BinaryAssociation(
    name="properties1",
    ends={
        Property(name="JPA_Property", type=JPA_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="JPA_Entity2", type=JPA_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anotations3: BinaryAssociation = BinaryAssociation(
    name="anotations3",
    ends={
        Property(name="JPA_Anotation", type=JPA_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="JPA_Entity4", type=JPA_Anotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entities0: BinaryAssociation = BinaryAssociation(
    name="entities0",
    ends={
        Property(name="JPA_Entity", type=JPA_PersistenceUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="JPA_PersistenceUnit", type=JPA_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
anotations5: BinaryAssociation = BinaryAssociation(
    name="anotations5",
    ends={
        Property(name="JPA_Anotation7", type=JPA_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="JPA_Property6", type=JPA_Anotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties8: BinaryAssociation = BinaryAssociation(
    name="properties8",
    ends={
        Property(name="JPA_Property9", type=JPA_EntityPk, multiplicity=Multiplicity(1, 1)),
        Property(name="JPA_EntityPk", type=JPA_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_JPA_Column_Anotation = Generalization(general=Anotation, specific=JPA_Column)
gen_JPA_OneToOne_Anotation = Generalization(general=Anotation, specific=JPA_OneToOne)
gen_JPA_EntityPk_Anotation = Generalization(general=Anotation, specific=JPA_EntityPk)
gen_JPA_Table_Anotation = Generalization(general=Anotation, specific=JPA_Table)
gen_JPA_OneToMany_Anotation = Generalization(general=Anotation, specific=JPA_OneToMany)
gen_JPA_ManyToOne_Anotation = Generalization(general=Anotation, specific=JPA_ManyToOne)
gen_JPA_ManyToMany_Anotation = Generalization(general=Anotation, specific=JPA_ManyToMany)

# Domain Model
domain_model = DomainModel(
    name="JPA",
    types={JPA_Property, JPA_Anotation, JPA_PersistenceUnit, JPA_Entity, JPA_Column, JPA_OneToOne, JPA_EntityPk, Anotation, JPA_Table, JPA_OneToMany, JPA_ManyToOne, JPA_ManyToMany, Fetch, Cascade},
    associations={properties1, anotations3, entities0, anotations5, properties8},
    generalizations={gen_JPA_Column_Anotation, gen_JPA_OneToOne_Anotation, gen_JPA_EntityPk_Anotation, gen_JPA_Table_Anotation, gen_JPA_OneToMany_Anotation, gen_JPA_ManyToOne_Anotation, gen_JPA_ManyToMany_Anotation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)