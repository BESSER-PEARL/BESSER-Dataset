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
entities_Expression = Class(name="entities::Expression")
entities_AssignmentStatement = Class(name="entities::AssignmentStatement")
Statement = Class(name="Statement")
entities_Entity = Class(name="entities::Entity")
entities_Field = Class(name="entities::Field")
entities_Statement = Class(name="entities::Statement")
entities_IntConstant = Class(name="entities::IntConstant")
Expression = Class(name="Expression")
entities_StringConstant = Class(name="entities::StringConstant")
entities_PrintStatement = Class(name="entities::PrintStatement")
entities_FieldType = Class(name="entities::FieldType")
entities_BasicType = Class(name="entities::BasicType")
FieldType = Class(name="FieldType")
entities_EntityType = Class(name="entities::EntityType")
entities_BoolConstant = Class(name="entities::BoolConstant")
entities_FieldRef = Class(name="entities::FieldRef")

# entities_Model class attributes and methods

# entities_Expression class attributes and methods

# entities_AssignmentStatement class attributes and methods

# Statement class attributes and methods

# entities_Entity class attributes and methods
entities_Entity_name: Property = Property(name="name", type=StringType)
entities_Entity.attributes={entities_Entity_name}

# entities_Field class attributes and methods
entities_Field_name: Property = Property(name="name", type=StringType)
entities_Field.attributes={entities_Field_name}

# entities_Statement class attributes and methods

# entities_IntConstant class attributes and methods
entities_IntConstant_value: Property = Property(name="value", type=IntegerType)
entities_IntConstant.attributes={entities_IntConstant_value}

# Expression class attributes and methods

# entities_StringConstant class attributes and methods
entities_StringConstant_value: Property = Property(name="value", type=StringType)
entities_StringConstant.attributes={entities_StringConstant_value}

# entities_PrintStatement class attributes and methods

# entities_FieldType class attributes and methods

# entities_BasicType class attributes and methods
entities_BasicType_typeName: Property = Property(name="typeName", type=StringType)
entities_BasicType.attributes={entities_BasicType_typeName}

# FieldType class attributes and methods

# entities_EntityType class attributes and methods

# entities_BoolConstant class attributes and methods
entities_BoolConstant_value: Property = Property(name="value", type=StringType)
entities_BoolConstant.attributes={entities_BoolConstant_value}

# entities_FieldRef class attributes and methods

# Relationships
expr8: BinaryAssociation = BinaryAssociation(
    name="expr8",
    ends={
        Property(name="entities_Expression", type=entities_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Statement9", type=entities_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entities0: BinaryAssociation = BinaryAssociation(
    name="entities0",
    ends={
        Property(name="entities_Entity", type=entities_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Model", type=entities_Entity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superType2: BinaryAssociation = BinaryAssociation(
    name="superType2",
    ends={
        Property(name="entities_Entity3", type=entities_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Entity1", type=entities_Entity, multiplicity=Multiplicity(0, 1))
    }
)
fields4: BinaryAssociation = BinaryAssociation(
    name="fields4",
    ends={
        Property(name="entities_Field", type=entities_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Entity5", type=entities_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements6: BinaryAssociation = BinaryAssociation(
    name="statements6",
    ends={
        Property(name="entities_Statement", type=entities_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Entity7", type=entities_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entity14: BinaryAssociation = BinaryAssociation(
    name="entity14",
    ends={
        Property(name="entities_EntityType", type=entities_Entity, multiplicity=Multiplicity(0, 1)),
        Property(name="entities_Entity15", type=entities_EntityType, multiplicity=Multiplicity(1, 1))
    }
)
assignee10: BinaryAssociation = BinaryAssociation(
    name="assignee10",
    ends={
        Property(name="entities_Field11", type=entities_AssignmentStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_AssignmentStatement", type=entities_Field, multiplicity=Multiplicity(0, 1))
    }
)
type12: BinaryAssociation = BinaryAssociation(
    name="type12",
    ends={
        Property(name="entities_FieldType", type=entities_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_Field13", type=entities_FieldType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
field16: BinaryAssociation = BinaryAssociation(
    name="field16",
    ends={
        Property(name="entities_Field17", type=entities_FieldRef, multiplicity=Multiplicity(1, 1)),
        Property(name="entities_FieldRef", type=entities_Field, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_entities_AssignmentStatement_Statement = Generalization(general=Statement, specific=entities_AssignmentStatement)
gen_entities_IntConstant_Expression = Generalization(general=Expression, specific=entities_IntConstant)
gen_entities_StringConstant_Expression = Generalization(general=Expression, specific=entities_StringConstant)
gen_entities_PrintStatement_Statement = Generalization(general=Statement, specific=entities_PrintStatement)
gen_entities_BasicType_FieldType = Generalization(general=FieldType, specific=entities_BasicType)
gen_entities_EntityType_FieldType = Generalization(general=FieldType, specific=entities_EntityType)
gen_entities_BoolConstant_Expression = Generalization(general=Expression, specific=entities_BoolConstant)
gen_entities_FieldRef_Expression = Generalization(general=Expression, specific=entities_FieldRef)

# Domain Model
domain_model = DomainModel(
    name="entities",
    types={entities_Model, entities_Expression, entities_AssignmentStatement, Statement, entities_Entity, entities_Field, entities_Statement, entities_IntConstant, Expression, entities_StringConstant, entities_PrintStatement, entities_FieldType, entities_BasicType, FieldType, entities_EntityType, entities_BoolConstant, entities_FieldRef},
    associations={expr8, entities0, superType2, fields4, statements6, entity14, assignee10, type12, field16},
    generalizations={gen_entities_AssignmentStatement_Statement, gen_entities_IntConstant_Expression, gen_entities_StringConstant_Expression, gen_entities_PrintStatement_Statement, gen_entities_BasicType_FieldType, gen_entities_EntityType_FieldType, gen_entities_BoolConstant_Expression, gen_entities_FieldRef_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)