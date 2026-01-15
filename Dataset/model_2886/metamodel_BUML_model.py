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
metamodel_Model = Class(name="metamodel::Model")
metamodel_Type = Class(name="metamodel::Type", is_abstract=True)
metamodel_DatabaseConnection = Class(name="metamodel::DatabaseConnection")
metamodel_idFeature = Class(name="metamodel::idFeature")
metamodel_Datatype = Class(name="metamodel::Datatype")
Type = Class(name="Type")
metamodel_Entity = Class(name="metamodel::Entity")
metamodel_Feature = Class(name="metamodel::Feature")
metamodel_Relation = Class(name="metamodel::Relation", is_abstract=True)
metamodel_AssociationEntity = Class(name="metamodel::AssociationEntity")
metamodel_OneToOne = Class(name="metamodel::OneToOne")
Relation = Class(name="Relation")
metamodel_OneToMany = Class(name="metamodel::OneToMany")
metamodel_ManyToMany = Class(name="metamodel::ManyToMany")
Feature = Class(name="Feature")

# metamodel_Model class attributes and methods
metamodel_Model_name: Property = Property(name="name", type=StringType)
metamodel_Model.attributes={metamodel_Model_name}

# metamodel_Type class attributes and methods
metamodel_Type_name: Property = Property(name="name", type=StringType)
metamodel_Type.attributes={metamodel_Type_name}

# metamodel_DatabaseConnection class attributes and methods
metamodel_DatabaseConnection_jdbcDriver: Property = Property(name="jdbcDriver", type=StringType)
metamodel_DatabaseConnection_jdbcUrl: Property = Property(name="jdbcUrl", type=StringType)
metamodel_DatabaseConnection_jdbcUser: Property = Property(name="jdbcUser", type=StringType)
metamodel_DatabaseConnection_jdbcPassword: Property = Property(name="jdbcPassword", type=StringType)
metamodel_DatabaseConnection_persistenceUnit: Property = Property(name="persistenceUnit", type=StringType)
metamodel_DatabaseConnection_jdbcPrefix: Property = Property(name="jdbcPrefix", type=StringType)
metamodel_DatabaseConnection.attributes={metamodel_DatabaseConnection_persistenceUnit, metamodel_DatabaseConnection_jdbcUrl, metamodel_DatabaseConnection_jdbcUser, metamodel_DatabaseConnection_jdbcDriver, metamodel_DatabaseConnection_jdbcPrefix, metamodel_DatabaseConnection_jdbcPassword}

# metamodel_idFeature class attributes and methods
metamodel_idFeature_generationType: Property = Property(name="generationType", type=StringType)
metamodel_idFeature.attributes={metamodel_idFeature_generationType}

# metamodel_Datatype class attributes and methods

# Type class attributes and methods

# metamodel_Entity class attributes and methods

# metamodel_Feature class attributes and methods
metamodel_Feature_name: Property = Property(name="name", type=StringType)
metamodel_Feature_nullable: Property = Property(name="nullable", type=BooleanType)
metamodel_Feature_xmltransient: Property = Property(name="xmltransient", type=BooleanType)
metamodel_Feature.attributes={metamodel_Feature_xmltransient, metamodel_Feature_nullable, metamodel_Feature_name}

# metamodel_Relation class attributes and methods
metamodel_Relation_optional: Property = Property(name="optional", type=BooleanType)
metamodel_Relation_unidirectional: Property = Property(name="unidirectional", type=BooleanType)
metamodel_Relation.attributes={metamodel_Relation_optional, metamodel_Relation_unidirectional}

# metamodel_AssociationEntity class attributes and methods

# metamodel_OneToOne class attributes and methods

# Relation class attributes and methods

# metamodel_OneToMany class attributes and methods

# metamodel_ManyToMany class attributes and methods

# Feature class attributes and methods

# Relationships
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="metamodel_Type", type=metamodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Model", type=metamodel_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connector1: BinaryAssociation = BinaryAssociation(
    name="connector1",
    ends={
        Property(name="metamodel_DatabaseConnection", type=metamodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Model2", type=metamodel_DatabaseConnection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedBy5: BinaryAssociation = BinaryAssociation(
    name="ownedBy5",
    ends={
        Property(name="Relation6", type=metamodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="slave", type=metamodel_Relation, multiplicity=Multiplicity(0, 9999))
    }
)
featuresId7: BinaryAssociation = BinaryAssociation(
    name="featuresId7",
    ends={
        Property(name="metamodel_idFeature", type=metamodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Entity8", type=metamodel_idFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inherits10: BinaryAssociation = BinaryAssociation(
    name="inherits10",
    ends={
        Property(name="Entity", type=metamodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="bequeathesTo", type=metamodel_Entity, multiplicity=Multiplicity(0, 1))
    }
)
bequeathesTo12: BinaryAssociation = BinaryAssociation(
    name="bequeathesTo12",
    ends={
        Property(name="Entity13", type=metamodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="inherits", type=metamodel_Entity, multiplicity=Multiplicity(0, 9999))
    }
)
type14: BinaryAssociation = BinaryAssociation(
    name="type14",
    ends={
        Property(name="metamodel_Type16", type=metamodel_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Feature15", type=metamodel_Type, multiplicity=Multiplicity(0, 1))
    }
)
features3: BinaryAssociation = BinaryAssociation(
    name="features3",
    ends={
        Property(name="metamodel_Feature", type=metamodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Entity", type=metamodel_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owns4: BinaryAssociation = BinaryAssociation(
    name="owns4",
    ends={
        Property(name="Relation", type=metamodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=metamodel_Relation, multiplicity=Multiplicity(0, 9999))
    }
)
associates21: BinaryAssociation = BinaryAssociation(
    name="associates21",
    ends={
        Property(name="AssociationEntity", type=metamodel_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="relation", type=metamodel_AssociationEntity, multiplicity=Multiplicity(0, 1))
    }
)
owner17: BinaryAssociation = BinaryAssociation(
    name="owner17",
    ends={
        Property(name="Entity18", type=metamodel_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="owns", type=metamodel_Entity, multiplicity=Multiplicity(1, 1))
    }
)
slave19: BinaryAssociation = BinaryAssociation(
    name="slave19",
    ends={
        Property(name="Entity20", type=metamodel_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedBy", type=metamodel_Entity, multiplicity=Multiplicity(1, 1))
    }
)
relation24: BinaryAssociation = BinaryAssociation(
    name="relation24",
    ends={
        Property(name="Relation25", type=metamodel_AssociationEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="associates", type=metamodel_Relation, multiplicity=Multiplicity(1, 1))
    }
)
features22: BinaryAssociation = BinaryAssociation(
    name="features22",
    ends={
        Property(name="metamodel_Feature23", type=metamodel_AssociationEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_AssociationEntity", type=metamodel_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_metamodel_Datatype_Type = Generalization(general=Type, specific=metamodel_Datatype)
gen_metamodel_Entity_Type = Generalization(general=Type, specific=metamodel_Entity)
gen_metamodel_OneToOne_Relation = Generalization(general=Relation, specific=metamodel_OneToOne)
gen_metamodel_OneToMany_Relation = Generalization(general=Relation, specific=metamodel_OneToMany)
gen_metamodel_ManyToMany_Relation = Generalization(general=Relation, specific=metamodel_ManyToMany)
gen_metamodel_idFeature_Feature = Generalization(general=Feature, specific=metamodel_idFeature)
gen_metamodel_Relation_Type = Generalization(general=Type, specific=metamodel_Relation)
gen_metamodel_AssociationEntity_Type = Generalization(general=Type, specific=metamodel_AssociationEntity)

# Domain Model
domain_model = DomainModel(
    name="metamodel",
    types={metamodel_Model, metamodel_Type, metamodel_DatabaseConnection, metamodel_idFeature, metamodel_Datatype, Type, metamodel_Entity, metamodel_Feature, metamodel_Relation, metamodel_AssociationEntity, metamodel_OneToOne, Relation, metamodel_OneToMany, metamodel_ManyToMany, Feature},
    associations={types0, connector1, ownedBy5, featuresId7, inherits10, bequeathesTo12, type14, features3, owns4, associates21, owner17, slave19, relation24, features22},
    generalizations={gen_metamodel_Datatype_Type, gen_metamodel_Entity_Type, gen_metamodel_OneToOne_Relation, gen_metamodel_OneToMany_Relation, gen_metamodel_ManyToMany_Relation, gen_metamodel_idFeature_Feature, gen_metamodel_Relation_Type, gen_metamodel_AssociationEntity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)