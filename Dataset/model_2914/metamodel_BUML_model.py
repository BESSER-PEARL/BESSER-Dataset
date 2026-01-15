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
metamodel_Validation_ValueRestriction = Class(name="metamodel::Validation::ValueRestriction")
metamodel_ValueRestriction_Value = Class(name="metamodel::ValueRestriction::Value")
metamodel_TransientVariable = Class(name="metamodel::TransientVariable")
metamodel_PlainVariable = Class(name="metamodel::PlainVariable")
Variable = Class(name="Variable")
metamodel_Entity = Class(name="metamodel::Entity")
Type = Class(name="Type")
metamodel_Variable = Class(name="metamodel::Variable", is_abstract=True)
metamodel_ConnectionToEntity = Class(name="metamodel::ConnectionToEntity")
metamodel_EntityObserver = Class(name="metamodel::EntityObserver")
metamodel_ActsAs = Class(name="metamodel::ActsAs")
metamodel_Type = Class(name="metamodel::Type", is_abstract=True)
metamodel_Datatype = Class(name="metamodel::Datatype")
metamodel_Extension_MQPublishing = Class(name="metamodel::Extension::MQPublishing")
metamodel_Controller = Class(name="metamodel::Controller")
metamodel_StaticVariable = Class(name="metamodel::StaticVariable")
metamodel_View = Class(name="metamodel::View")
metamodel_Model = Class(name="metamodel::Model")

# metamodel_Validation_ValueRestriction class attributes and methods

# metamodel_ValueRestriction_Value class attributes and methods
metamodel_ValueRestriction_Value_value: Property = Property(name="value", type=StringType)
metamodel_ValueRestriction_Value.attributes={metamodel_ValueRestriction_Value_value}

# metamodel_TransientVariable class attributes and methods

# metamodel_PlainVariable class attributes and methods

# Variable class attributes and methods

# metamodel_Entity class attributes and methods
metamodel_Entity_base: Property = Property(name="base", type=StringType)
metamodel_Entity.attributes={metamodel_Entity_base}

# Type class attributes and methods

# metamodel_Variable class attributes and methods
metamodel_Variable_name: Property = Property(name="name", type=StringType)
metamodel_Variable.attributes={metamodel_Variable_name}

# metamodel_ConnectionToEntity class attributes and methods
metamodel_ConnectionToEntity_name: Property = Property(name="name", type=StringType)
metamodel_ConnectionToEntity_cardinalityMany: Property = Property(name="cardinalityMany", type=BooleanType)
metamodel_ConnectionToEntity.attributes={metamodel_ConnectionToEntity_name, metamodel_ConnectionToEntity_cardinalityMany}

# metamodel_EntityObserver class attributes and methods

# metamodel_ActsAs class attributes and methods
metamodel_ActsAs_actsAsWhat: Property = Property(name="actsAsWhat", type=StringType)
metamodel_ActsAs.attributes={metamodel_ActsAs_actsAsWhat}

# metamodel_Type class attributes and methods
metamodel_Type_name: Property = Property(name="name", type=StringType)
metamodel_Type.attributes={metamodel_Type_name}

# metamodel_Datatype class attributes and methods

# metamodel_Extension_MQPublishing class attributes and methods
metamodel_Extension_MQPublishing_queue: Property = Property(name="queue", type=StringType)
metamodel_Extension_MQPublishing.attributes={metamodel_Extension_MQPublishing_queue}

# metamodel_Controller class attributes and methods

# metamodel_StaticVariable class attributes and methods

# metamodel_View class attributes and methods

# metamodel_Model class attributes and methods

# Relationships
restrictsTo10: BinaryAssociation = BinaryAssociation(
    name="restrictsTo10",
    ends={
        Property(name="metamodel_ValueRestriction_Value", type=metamodel_Validation_ValueRestriction, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Validation_ValueRestriction", type=metamodel_ValueRestriction_Value, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
otherEntity11: BinaryAssociation = BinaryAssociation(
    name="otherEntity11",
    ends={
        Property(name="metamodel_Entity13", type=metamodel_ConnectionToEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_ConnectionToEntity12", type=metamodel_Entity, multiplicity=Multiplicity(1, 1))
    }
)
type14: BinaryAssociation = BinaryAssociation(
    name="type14",
    ends={
        Property(name="metamodel_Type", type=metamodel_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Variable15", type=metamodel_Type, multiplicity=Multiplicity(1, 1))
    }
)
hasAttribute0: BinaryAssociation = BinaryAssociation(
    name="hasAttribute0",
    ends={
        Property(name="metamodel_Variable", type=metamodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Entity", type=metamodel_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
belongsToEntity1: BinaryAssociation = BinaryAssociation(
    name="belongsToEntity1",
    ends={
        Property(name="metamodel_ConnectionToEntity", type=metamodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Entity2", type=metamodel_ConnectionToEntity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasEntity3: BinaryAssociation = BinaryAssociation(
    name="hasEntity3",
    ends={
        Property(name="metamodel_ConnectionToEntity5", type=metamodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Entity4", type=metamodel_ConnectionToEntity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isObservedBy6: BinaryAssociation = BinaryAssociation(
    name="isObservedBy6",
    ends={
        Property(name="metamodel_EntityObserver", type=metamodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Entity7", type=metamodel_EntityObserver, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actsAs8: BinaryAssociation = BinaryAssociation(
    name="actsAs8",
    ends={
        Property(name="metamodel_ActsAs", type=metamodel_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Entity9", type=metamodel_ActsAs, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
validatedBy16: BinaryAssociation = BinaryAssociation(
    name="validatedBy16",
    ends={
        Property(name="metamodel_Validation_ValueRestriction18", type=metamodel_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Variable17", type=metamodel_Validation_ValueRestriction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extendedBy19: BinaryAssociation = BinaryAssociation(
    name="extendedBy19",
    ends={
        Property(name="metamodel_Extension_MQPublishing", type=metamodel_EntityObserver, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_EntityObserver20", type=metamodel_Extension_MQPublishing, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
belongsTo21: BinaryAssociation = BinaryAssociation(
    name="belongsTo21",
    ends={
        Property(name="metamodel_Controller", type=metamodel_View, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_View", type=metamodel_Controller, multiplicity=Multiplicity(1, 1))
    }
)
hasControllers22: BinaryAssociation = BinaryAssociation(
    name="hasControllers22",
    ends={
        Property(name="metamodel_Controller23", type=metamodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Model", type=metamodel_Controller, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasViews24: BinaryAssociation = BinaryAssociation(
    name="hasViews24",
    ends={
        Property(name="metamodel_View26", type=metamodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Model25", type=metamodel_View, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasEntities27: BinaryAssociation = BinaryAssociation(
    name="hasEntities27",
    ends={
        Property(name="metamodel_Entity29", type=metamodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Model28", type=metamodel_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types30: BinaryAssociation = BinaryAssociation(
    name="types30",
    ends={
        Property(name="metamodel_Type32", type=metamodel_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="metamodel_Model31", type=metamodel_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_metamodel_TransientVariable_Variable = Generalization(general=Variable, specific=metamodel_TransientVariable)
gen_metamodel_PlainVariable_Variable = Generalization(general=Variable, specific=metamodel_PlainVariable)
gen_metamodel_Entity_Type = Generalization(general=Type, specific=metamodel_Entity)
gen_metamodel_Datatype_Type = Generalization(general=Type, specific=metamodel_Datatype)
gen_metamodel_Controller_Type = Generalization(general=Type, specific=metamodel_Controller)
gen_metamodel_StaticVariable_Variable = Generalization(general=Variable, specific=metamodel_StaticVariable)
gen_metamodel_View_Type = Generalization(general=Type, specific=metamodel_View)
gen_metamodel_Model_Type = Generalization(general=Type, specific=metamodel_Model)

# Domain Model
domain_model = DomainModel(
    name="metamodel",
    types={metamodel_Validation_ValueRestriction, metamodel_ValueRestriction_Value, metamodel_TransientVariable, metamodel_PlainVariable, Variable, metamodel_Entity, Type, metamodel_Variable, metamodel_ConnectionToEntity, metamodel_EntityObserver, metamodel_ActsAs, metamodel_Type, metamodel_Datatype, metamodel_Extension_MQPublishing, metamodel_Controller, metamodel_StaticVariable, metamodel_View, metamodel_Model},
    associations={restrictsTo10, otherEntity11, type14, hasAttribute0, belongsToEntity1, hasEntity3, isObservedBy6, actsAs8, validatedBy16, extendedBy19, belongsTo21, hasControllers22, hasViews24, hasEntities27, types30},
    generalizations={gen_metamodel_TransientVariable_Variable, gen_metamodel_PlainVariable_Variable, gen_metamodel_Entity_Type, gen_metamodel_Datatype_Type, gen_metamodel_Controller_Type, gen_metamodel_StaticVariable_Variable, gen_metamodel_View_Type, gen_metamodel_Model_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)