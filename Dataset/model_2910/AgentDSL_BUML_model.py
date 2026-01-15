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
agentDSL_TypeDef = Class(name="agentDSL::TypeDef")
Type = Class(name="Type")
agentDSL_JAVAID = Class(name="agentDSL::JAVAID")
agentDSL_Model = Class(name="agentDSL::Model")
agentDSL_Type = Class(name="agentDSL::Type")
agentDSL_Outcome = Class(name="agentDSL::Outcome")
agentDSL_Entity = Class(name="agentDSL::Entity")
agentDSL_Attribute = Class(name="agentDSL::Attribute")
agentDSL_Task = Class(name="agentDSL::Task")
agentDSL_Goal = Class(name="agentDSL::Goal")
agentDSL_Function = Class(name="agentDSL::Function")

# agentDSL_TypeDef class attributes and methods

# Type class attributes and methods

# agentDSL_JAVAID class attributes and methods
agentDSL_JAVAID_name: Property = Property(name="name", type=StringType)
agentDSL_JAVAID.attributes={agentDSL_JAVAID_name}

# agentDSL_Model class attributes and methods

# agentDSL_Type class attributes and methods
agentDSL_Type_name: Property = Property(name="name", type=StringType)
agentDSL_Type.attributes={agentDSL_Type_name}

# agentDSL_Outcome class attributes and methods

# agentDSL_Entity class attributes and methods

# agentDSL_Attribute class attributes and methods
agentDSL_Attribute_many: Property = Property(name="many", type=BooleanType)
agentDSL_Attribute_name: Property = Property(name="name", type=StringType)
agentDSL_Attribute.attributes={agentDSL_Attribute_name, agentDSL_Attribute_many}

# agentDSL_Task class attributes and methods

# agentDSL_Goal class attributes and methods
agentDSL_Goal_name: Property = Property(name="name", type=StringType)
agentDSL_Goal.attributes={agentDSL_Goal_name}

# agentDSL_Function class attributes and methods

# Relationships
mappedType1: BinaryAssociation = BinaryAssociation(
    name="mappedType1",
    ends={
        Property(name="agentDSL_JAVAID", type=agentDSL_TypeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="agentDSL_TypeDef", type=agentDSL_JAVAID, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="agentDSL_Type", type=agentDSL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="agentDSL_Model", type=agentDSL_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outcome8: BinaryAssociation = BinaryAssociation(
    name="outcome8",
    ends={
        Property(name="agentDSL_Outcome", type=agentDSL_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="agentDSL_Task9", type=agentDSL_Outcome, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
superEntity3: BinaryAssociation = BinaryAssociation(
    name="superEntity3",
    ends={
        Property(name="agentDSL_Entity", type=agentDSL_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="agentDSL_Entity2", type=agentDSL_Entity, multiplicity=Multiplicity(0, 1))
    }
)
attributes4: BinaryAssociation = BinaryAssociation(
    name="attributes4",
    ends={
        Property(name="agentDSL_Attribute", type=agentDSL_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="agentDSL_Entity5", type=agentDSL_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes6: BinaryAssociation = BinaryAssociation(
    name="attributes6",
    ends={
        Property(name="agentDSL_Attribute7", type=agentDSL_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="agentDSL_Task", type=agentDSL_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type20: BinaryAssociation = BinaryAssociation(
    name="type20",
    ends={
        Property(name="agentDSL_Type22", type=agentDSL_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="agentDSL_Attribute21", type=agentDSL_Type, multiplicity=Multiplicity(0, 1))
    }
)
attributes10: BinaryAssociation = BinaryAssociation(
    name="attributes10",
    ends={
        Property(name="agentDSL_Attribute12", type=agentDSL_Outcome, multiplicity=Multiplicity(1, 1)),
        Property(name="agentDSL_Outcome11", type=agentDSL_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
goal13: BinaryAssociation = BinaryAssociation(
    name="goal13",
    ends={
        Property(name="agentDSL_Goal", type=agentDSL_Outcome, multiplicity=Multiplicity(1, 1)),
        Property(name="agentDSL_Outcome14", type=agentDSL_Goal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes15: BinaryAssociation = BinaryAssociation(
    name="attributes15",
    ends={
        Property(name="agentDSL_Attribute17", type=agentDSL_Goal, multiplicity=Multiplicity(1, 1)),
        Property(name="agentDSL_Goal16", type=agentDSL_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes18: BinaryAssociation = BinaryAssociation(
    name="attributes18",
    ends={
        Property(name="agentDSL_Attribute19", type=agentDSL_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="agentDSL_Function", type=agentDSL_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_agentDSL_TypeDef_Type = Generalization(general=Type, specific=agentDSL_TypeDef)
gen_agentDSL_Outcome_Type = Generalization(general=Type, specific=agentDSL_Outcome)
gen_agentDSL_Entity_Type = Generalization(general=Type, specific=agentDSL_Entity)
gen_agentDSL_Task_Type = Generalization(general=Type, specific=agentDSL_Task)
gen_agentDSL_Function_Type = Generalization(general=Type, specific=agentDSL_Function)

# Domain Model
domain_model = DomainModel(
    name="agentDSL",
    types={agentDSL_TypeDef, Type, agentDSL_JAVAID, agentDSL_Model, agentDSL_Type, agentDSL_Outcome, agentDSL_Entity, agentDSL_Attribute, agentDSL_Task, agentDSL_Goal, agentDSL_Function},
    associations={mappedType1, types0, outcome8, superEntity3, attributes4, attributes6, type20, attributes10, goal13, attributes15, attributes18},
    generalizations={gen_agentDSL_TypeDef_Type, gen_agentDSL_Outcome_Type, gen_agentDSL_Entity_Type, gen_agentDSL_Task_Type, gen_agentDSL_Function_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)