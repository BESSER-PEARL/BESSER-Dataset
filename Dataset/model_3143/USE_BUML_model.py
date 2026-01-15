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
SimpleTypes: Enumeration = Enumeration(
    name="SimpleTypes",
    literals={
            EnumerationLiteral(name="Integer"),
			EnumerationLiteral(name="Real"),
			EnumerationLiteral(name="Boolean"),
			EnumerationLiteral(name="String")
    }
)

CollectionTypes: Enumeration = Enumeration(
    name="CollectionTypes",
    literals={
            EnumerationLiteral(name="Set"),
			EnumerationLiteral(name="Bag"),
			EnumerationLiteral(name="Sequence")
    }
)

AssocKind: Enumeration = Enumeration(
    name="AssocKind",
    literals={
            EnumerationLiteral(name="Association"),
			EnumerationLiteral(name="Composition"),
			EnumerationLiteral(name="Aggregation")
    }
)

# Classes
USE_Attribute = Class(name="USE::Attribute")
USE_Operation = Class(name="USE::Operation")
USE_OCLExpression = Class(name="USE::OCLExpression")
USE_Model = Class(name="USE::Model")
USE_Enumeration = Class(name="USE::Enumeration")
USE_Association = Class(name="USE::Association")
USE_Class = Class(name="USE::Class")
USE_EnumerationType = Class(name="USE::EnumerationType")
Type = Class(name="Type")
USE_Type = Class(name="USE::Type", is_abstract=True)
USE_Parameter = Class(name="USE::Parameter")
USE_ReferenceType = Class(name="USE::ReferenceType")
USE_Literal = Class(name="USE::Literal")
USE_CollectionType = Class(name="USE::CollectionType")
USE_SimpleType = Class(name="USE::SimpleType")
USE_Role = Class(name="USE::Role")

# USE_Attribute class attributes and methods
USE_Attribute_name: Property = Property(name="name", type=StringType)
USE_Attribute.attributes={USE_Attribute_name}

# USE_Operation class attributes and methods
USE_Operation_name: Property = Property(name="name", type=StringType)
USE_Operation.attributes={USE_Operation_name}

# USE_OCLExpression class attributes and methods
USE_OCLExpression_expr: Property = Property(name="expr", type=StringType)
USE_OCLExpression.attributes={USE_OCLExpression_expr}

# USE_Model class attributes and methods
USE_Model_name: Property = Property(name="name", type=StringType)
USE_Model.attributes={USE_Model_name}

# USE_Enumeration class attributes and methods
USE_Enumeration_name: Property = Property(name="name", type=StringType)
USE_Enumeration.attributes={USE_Enumeration_name}

# USE_Association class attributes and methods
USE_Association_name: Property = Property(name="name", type=StringType)
USE_Association_kind: Property = Property(name="kind", type=StringType)
USE_Association.attributes={USE_Association_name, USE_Association_kind}

# USE_Class class attributes and methods
USE_Class_name: Property = Property(name="name", type=StringType)
USE_Class_abstract: Property = Property(name="abstract", type=BooleanType)
USE_Class.attributes={USE_Class_abstract, USE_Class_name}

# USE_EnumerationType class attributes and methods

# Type class attributes and methods

# USE_Type class attributes and methods

# USE_Parameter class attributes and methods
USE_Parameter_name: Property = Property(name="name", type=StringType)
USE_Parameter.attributes={USE_Parameter_name}

# USE_ReferenceType class attributes and methods

# USE_Literal class attributes and methods
USE_Literal_name: Property = Property(name="name", type=StringType)
USE_Literal.attributes={USE_Literal_name}

# USE_CollectionType class attributes and methods
USE_CollectionType_type: Property = Property(name="type", type=StringType)
USE_CollectionType.attributes={USE_CollectionType_type}

# USE_SimpleType class attributes and methods
USE_SimpleType_type: Property = Property(name="type", type=StringType)
USE_SimpleType.attributes={USE_SimpleType_type}

# USE_Role class attributes and methods
USE_Role_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
USE_Role_name: Property = Property(name="name", type=StringType)
USE_Role_ordered: Property = Property(name="ordered", type=BooleanType)
USE_Role_upperBound: Property = Property(name="upperBound", type=IntegerType)
USE_Role.attributes={USE_Role_upperBound, USE_Role_name, USE_Role_ordered, USE_Role_lowerBound}

# Relationships
superClasses1: BinaryAssociation = BinaryAssociation(
    name="superClasses1",
    ends={
        Property(name="USE_Class", type=USE_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="USE_Class0", type=USE_Class, multiplicity=Multiplicity(0, 9999))
    }
)
attributes2: BinaryAssociation = BinaryAssociation(
    name="attributes2",
    ends={
        Property(name="USE_Attribute", type=USE_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="USE_Class3", type=USE_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations4: BinaryAssociation = BinaryAssociation(
    name="operations4",
    ends={
        Property(name="USE_Operation", type=USE_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="USE_Class5", type=USE_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invariants6: BinaryAssociation = BinaryAssociation(
    name="invariants6",
    ends={
        Property(name="USE_OCLExpression", type=USE_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="USE_Class7", type=USE_OCLExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes8: BinaryAssociation = BinaryAssociation(
    name="classes8",
    ends={
        Property(name="USE_Class9", type=USE_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="USE_Model", type=USE_Class, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
enumerations10: BinaryAssociation = BinaryAssociation(
    name="enumerations10",
    ends={
        Property(name="USE_Enumeration", type=USE_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="USE_Model11", type=USE_Enumeration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associations12: BinaryAssociation = BinaryAssociation(
    name="associations12",
    ends={
        Property(name="USE_Association", type=USE_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="USE_Model13", type=USE_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters16: BinaryAssociation = BinaryAssociation(
    name="parameters16",
    ends={
        Property(name="USE_Operation17", type=USE_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="USE_Parameter", type=USE_Operation, multiplicity=Multiplicity(1, 1))
    }
)
implementation18: BinaryAssociation = BinaryAssociation(
    name="implementation18",
    ends={
        Property(name="USE_OCLExpression20", type=USE_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="USE_Operation19", type=USE_OCLExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type21: BinaryAssociation = BinaryAssociation(
    name="type21",
    ends={
        Property(name="USE_Type23", type=USE_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="USE_Operation22", type=USE_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
preCondition24: BinaryAssociation = BinaryAssociation(
    name="preCondition24",
    ends={
        Property(name="USE_OCLExpression26", type=USE_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="USE_Operation25", type=USE_OCLExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postCondition27: BinaryAssociation = BinaryAssociation(
    name="postCondition27",
    ends={
        Property(name="USE_OCLExpression29", type=USE_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="USE_Operation28", type=USE_OCLExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type30: BinaryAssociation = BinaryAssociation(
    name="type30",
    ends={
        Property(name="USE_Type32", type=USE_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="USE_Parameter31", type=USE_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type14: BinaryAssociation = BinaryAssociation(
    name="type14",
    ends={
        Property(name="USE_Type", type=USE_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="USE_Attribute15", type=USE_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
class37: BinaryAssociation = BinaryAssociation(
    name="class37",
    ends={
        Property(name="USE_Class38", type=USE_ReferenceType, multiplicity=Multiplicity(1, 1)),
        Property(name="USE_ReferenceType", type=USE_Class, multiplicity=Multiplicity(1, 1))
    }
)
literals39: BinaryAssociation = BinaryAssociation(
    name="literals39",
    ends={
        Property(name="USE_Literal", type=USE_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="USE_Enumeration40", type=USE_Literal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enum33: BinaryAssociation = BinaryAssociation(
    name="enum33",
    ends={
        Property(name="USE_Enumeration34", type=USE_EnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="USE_EnumerationType", type=USE_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
baseType35: BinaryAssociation = BinaryAssociation(
    name="baseType35",
    ends={
        Property(name="USE_Type36", type=USE_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="USE_CollectionType", type=USE_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
className43: BinaryAssociation = BinaryAssociation(
    name="className43",
    ends={
        Property(name="USE_Class45", type=USE_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="USE_Role44", type=USE_Class, multiplicity=Multiplicity(1, 1))
    }
)
role41: BinaryAssociation = BinaryAssociation(
    name="role41",
    ends={
        Property(name="USE_Role", type=USE_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="USE_Association42", type=USE_Role, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)

# Generalizations
gen_USE_EnumerationType_Type = Generalization(general=Type, specific=USE_EnumerationType)
gen_USE_ReferenceType_Type = Generalization(general=Type, specific=USE_ReferenceType)
gen_USE_CollectionType_Type = Generalization(general=Type, specific=USE_CollectionType)
gen_USE_SimpleType_Type = Generalization(general=Type, specific=USE_SimpleType)

# Domain Model
domain_model = DomainModel(
    name="USE",
    types={USE_Attribute, USE_Operation, USE_OCLExpression, USE_Model, USE_Enumeration, USE_Association, USE_Class, USE_EnumerationType, Type, USE_Type, USE_Parameter, USE_ReferenceType, USE_Literal, USE_CollectionType, USE_SimpleType, USE_Role, SimpleTypes, CollectionTypes, AssocKind},
    associations={superClasses1, attributes2, operations4, invariants6, classes8, enumerations10, associations12, parameters16, implementation18, type21, preCondition24, postCondition27, type30, type14, class37, literals39, enum33, baseType35, className43, role41},
    generalizations={gen_USE_EnumerationType_Type, gen_USE_ReferenceType_Type, gen_USE_CollectionType_Type, gen_USE_SimpleType_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)