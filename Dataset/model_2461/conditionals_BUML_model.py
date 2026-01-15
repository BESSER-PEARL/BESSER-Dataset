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
operators_Type = Class(name="operators::Type")
operators_OperationCallExp = Class(name="operators::OperationCallExp")
OclExpression = Class(name="OclExpression")
operators_IfExp = Class(name="operators::IfExp")
operators_OclExpression = Class(name="operators::OclExpression", is_abstract=True)
operators_OclType = Class(name="operators::OclType")

# operators_Type class attributes and methods
operators_Type_m_isSameType: Method = Method(name="isSameType", parameters={Parameter(name='t')}, type=BooleanType)
operators_Type_m_isSuperTypeOf: Method = Method(name="isSuperTypeOf", parameters={Parameter(name='t')}, type=BooleanType)
operators_Type.methods={operators_Type_m_isSuperTypeOf, operators_Type_m_isSameType}

# operators_OperationCallExp class attributes and methods
operators_OperationCallExp_name: Property = Property(name="name", type=StringType)
operators_OperationCallExp.attributes={operators_OperationCallExp_name}

# OclExpression class attributes and methods

# operators_IfExp class attributes and methods

# operators_OclExpression class attributes and methods

# operators_OclType class attributes and methods

# Relationships
type_0: BinaryAssociation = BinaryAssociation(
    name="type_0",
    ends={
        Property(name="operators_Type", type=operators_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_OclExpression", type=operators_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source1: BinaryAssociation = BinaryAssociation(
    name="source1",
    ends={
        Property(name="operators_OclExpression2", type=operators_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_OperationCallExp", type=operators_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments3: BinaryAssociation = BinaryAssociation(
    name="arguments3",
    ends={
        Property(name="operators_OclExpression5", type=operators_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_OperationCallExp4", type=operators_OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thenExpression6: BinaryAssociation = BinaryAssociation(
    name="thenExpression6",
    ends={
        Property(name="operators_OclExpression7", type=operators_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_IfExp", type=operators_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition8: BinaryAssociation = BinaryAssociation(
    name="condition8",
    ends={
        Property(name="operators_OclExpression10", type=operators_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_IfExp9", type=operators_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression11: BinaryAssociation = BinaryAssociation(
    name="elseExpression11",
    ends={
        Property(name="operators_OclExpression13", type=operators_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="operators_IfExp12", type=operators_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_operators_OperationCallExp_OclExpression = Generalization(general=OclExpression, specific=operators_OperationCallExp)
gen_operators_IfExp_OclExpression = Generalization(general=OclExpression, specific=operators_IfExp)
gen_operators_OclType_OclExpression = Generalization(general=OclExpression, specific=operators_OclType)

# Domain Model
domain_model = DomainModel(
    name="operators",
    types={operators_Type, operators_OperationCallExp, OclExpression, operators_IfExp, operators_OclExpression, operators_OclType},
    associations={type_0, source1, arguments3, thenExpression6, condition8, elseExpression11},
    generalizations={gen_operators_OperationCallExp_OclExpression, gen_operators_IfExp_OclExpression, gen_operators_OclType_OclExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)