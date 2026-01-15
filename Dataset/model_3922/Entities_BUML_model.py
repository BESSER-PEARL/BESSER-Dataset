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
entities_Model = Class(name="entities::Model")
entities_Package = Class(name="entities::Package")
entities_TypeDef = Class(name="entities::TypeDef")
PackagedType = Class(name="PackagedType")
entities_PackagedType = Class(name="entities::PackagedType")
entities_Type = Class(name="entities::Type")
entities_SimpleType = Class(name="entities::SimpleType")
Type = Class(name="Type")
entities_Property = Class(name="entities::Property")
entities_Entity = Class(name="entities::Entity")
entities_JAVAID = Class(name="entities::JAVAID")

# entities_Model class attributes and methods

# entities_Package class attributes and methods

# entities_TypeDef class attributes and methods
entities_TypeDef_name: Property = Property(name="name", type=StringType)
entities_TypeDef.attributes={entities_TypeDef_name}

# PackagedType class attributes and methods

# entities_PackagedType class attributes and methods
entities_PackagedType_name: Property = Property(name="name", type=StringType)
entities_PackagedType.attributes={entities_PackagedType_name}

# entities_Type class attributes and methods

# entities_SimpleType class attributes and methods

# Type class attributes and methods

# entities_Property class attributes and methods
entities_Property_name: Property = Property(name="name", type=StringType)
entities_Property_many: Property = Property(name="many", type=BooleanType)
entities_Property.attributes={entities_Property_name, entities_Property_many}

# entities_Entity class attributes and methods

# entities_JAVAID class attributes and methods
entities_JAVAID_name: Property = Property(name="name", type=StringType)
entities_JAVAID.attributes={entities_JAVAID_name}

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="entities_Package", type=entities_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Model", type=entities_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties2: BinaryAssociation = BinaryAssociation(
    name="properties2",
    ends={
        Property(name="entities_PackagedType", type=entities_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Package3", type=entities_PackagedType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type4: BinaryAssociation = BinaryAssociation(
    name="type4",
    ends={
        Property(name="entities_Type", type=entities_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Property", type=entities_Type, multiplicity=Multiplicity(0, 1))
    }
)
extends6: BinaryAssociation = BinaryAssociation(
    name="extends6",
    ends={
        Property(name="entities_Entity", type=entities_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Entity5", type=entities_Entity, multiplicity=Multiplicity(0, 1))
    }
)
properties7: BinaryAssociation = BinaryAssociation(
    name="properties7",
    ends={
        Property(name="entities_Property9", type=entities_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Entity8", type=entities_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package10: BinaryAssociation = BinaryAssociation(
    name="package10",
    ends={
        Property(name="entities_Package12", type=entities_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Entity11", type=entities_Package, multiplicity=Multiplicity(0, 1))
    }
)
mappedType1: BinaryAssociation = BinaryAssociation(
    name="mappedType1",
    ends={
        Property(name="entities_JAVAID", type=entities_TypeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_TypeDef", type=entities_JAVAID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_entities_Package_PackagedType = Generalization(general=PackagedType, specific=entities_Package)
gen_entities_Type_PackagedType = Generalization(general=PackagedType, specific=entities_Type)
gen_entities_SimpleType_Type = Generalization(general=Type, specific=entities_SimpleType)
gen_entities_Entity_Type = Generalization(general=Type, specific=entities_Entity)

# Domain Model
domain_model = DomainModel(
    name="entities",
    types={entities_Model, entities_Package, entities_TypeDef, PackagedType, entities_PackagedType, entities_Type, entities_SimpleType, Type, entities_Property, entities_Entity, entities_JAVAID},
    associations={elements0, properties2, type4, extends6, properties7, package10, mappedType1},
    generalizations={gen_entities_Package_PackagedType, gen_entities_Type_PackagedType, gen_entities_SimpleType_Type, gen_entities_Entity_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)