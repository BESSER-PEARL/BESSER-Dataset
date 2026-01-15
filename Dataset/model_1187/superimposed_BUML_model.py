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
superimposed_VariableDeclaration = Class(name="superimposed::VariableDeclaration")
superimposed_OclExpression = Class(name="superimposed::OclExpression", is_abstract=True)
OperatorCallExp = Class(name="OperatorCallExp")
superimposed_OclType = Class(name="superimposed::OclType")
superimposed_VariableExp = Class(name="superimposed::VariableExp")
OclExpression = Class(name="OclExpression")
superimposed_OclUndefinedExp = Class(name="superimposed::OclUndefinedExp")
superimposed_LetExp = Class(name="superimposed::LetExp")
superimposed_OperationCallExp = Class(name="superimposed::OperationCallExp")
PropertyCallExp = Class(name="PropertyCallExp")
superimposed_CollectionOperationCallExp = Class(name="superimposed::CollectionOperationCallExp")
OperationCallExp = Class(name="OperationCallExp")
superimposed_NavigationCallExp = Class(name="superimposed::NavigationCallExp")
superimposed_IfExp = Class(name="superimposed::IfExp")
superimposed_OperatorCallExp = Class(name="superimposed::OperatorCallExp", is_abstract=True)
superimposed_OclModelElement = Class(name="superimposed::OclModelElement")
superimposed_BinaryOperatorCallExp = Class(name="superimposed::BinaryOperatorCallExp")
OclType = Class(name="OclType")
superimposed_UnaryOperatorCallExp = Class(name="superimposed::UnaryOperatorCallExp")
superimposed_PropertyCallExp = Class(name="superimposed::PropertyCallExp", is_abstract=True)
superimposed_LoopExp = Class(name="superimposed::LoopExp", is_abstract=True)
superimposed_IteratorExp = Class(name="superimposed::IteratorExp")
LoopExp = Class(name="LoopExp")
superimposed_Iterator = Class(name="superimposed::Iterator")
VariableDeclaration = Class(name="VariableDeclaration")
superimposed_PrimitiveExp = Class(name="superimposed::PrimitiveExp", is_abstract=True)
superimposed_StringExp = Class(name="superimposed::StringExp")
PrimitiveExp = Class(name="PrimitiveExp")
superimposed_BooleanExp = Class(name="superimposed::BooleanExp")
superimposed_NumericExp = Class(name="superimposed::NumericExp", is_abstract=True)
superimposed_RealExp = Class(name="superimposed::RealExp")
NumericExp = Class(name="NumericExp")
superimposed_IntegerExp = Class(name="superimposed::IntegerExp")
superimposed_OclModel = Class(name="superimposed::OclModel")
superimposed_CollectionExp = Class(name="superimposed::CollectionExp", is_abstract=True)
superimposed_SetExp = Class(name="superimposed::SetExp")
CollectionExp = Class(name="CollectionExp")

# superimposed_VariableDeclaration class attributes and methods
superimposed_VariableDeclaration_name: Property = Property(name="name", type=StringType)
superimposed_VariableDeclaration.attributes={superimposed_VariableDeclaration_name}

# superimposed_OclExpression class attributes and methods

# OperatorCallExp class attributes and methods

# superimposed_OclType class attributes and methods

# superimposed_VariableExp class attributes and methods

# OclExpression class attributes and methods

# superimposed_OclUndefinedExp class attributes and methods

# superimposed_LetExp class attributes and methods

# superimposed_OperationCallExp class attributes and methods
superimposed_OperationCallExp_name: Property = Property(name="name", type=StringType)
superimposed_OperationCallExp.attributes={superimposed_OperationCallExp_name}

# PropertyCallExp class attributes and methods

# superimposed_CollectionOperationCallExp class attributes and methods

# OperationCallExp class attributes and methods

# superimposed_NavigationCallExp class attributes and methods
superimposed_NavigationCallExp_name: Property = Property(name="name", type=StringType)
superimposed_NavigationCallExp.attributes={superimposed_NavigationCallExp_name}

# superimposed_IfExp class attributes and methods

# superimposed_OperatorCallExp class attributes and methods
superimposed_OperatorCallExp_name: Property = Property(name="name", type=StringType)
superimposed_OperatorCallExp.attributes={superimposed_OperatorCallExp_name}

# superimposed_OclModelElement class attributes and methods
superimposed_OclModelElement_name: Property = Property(name="name", type=StringType)
superimposed_OclModelElement.attributes={superimposed_OclModelElement_name}

# superimposed_BinaryOperatorCallExp class attributes and methods

# OclType class attributes and methods

# superimposed_UnaryOperatorCallExp class attributes and methods

# superimposed_PropertyCallExp class attributes and methods

# superimposed_LoopExp class attributes and methods

# superimposed_IteratorExp class attributes and methods
superimposed_IteratorExp_name: Property = Property(name="name", type=StringType)
superimposed_IteratorExp.attributes={superimposed_IteratorExp_name}

# LoopExp class attributes and methods

# superimposed_Iterator class attributes and methods

# VariableDeclaration class attributes and methods

# superimposed_PrimitiveExp class attributes and methods

# superimposed_StringExp class attributes and methods
superimposed_StringExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
superimposed_StringExp.attributes={superimposed_StringExp_stringSymbol}

# PrimitiveExp class attributes and methods

# superimposed_BooleanExp class attributes and methods
superimposed_BooleanExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
superimposed_BooleanExp.attributes={superimposed_BooleanExp_booleanSymbol}

# superimposed_NumericExp class attributes and methods

# superimposed_RealExp class attributes and methods
superimposed_RealExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
superimposed_RealExp.attributes={superimposed_RealExp_realSymbol}

# NumericExp class attributes and methods

# superimposed_IntegerExp class attributes and methods
superimposed_IntegerExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
superimposed_IntegerExp.attributes={superimposed_IntegerExp_integerSymbol}

# superimposed_OclModel class attributes and methods
superimposed_OclModel_name: Property = Property(name="name", type=StringType)
superimposed_OclModel.attributes={superimposed_OclModel_name}

# superimposed_CollectionExp class attributes and methods

# superimposed_SetExp class attributes and methods

# CollectionExp class attributes and methods

# Relationships
initExpression0: BinaryAssociation = BinaryAssociation(
    name="initExpression0",
    ends={
        Property(name="superimposed_OclExpression", type=superimposed_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="superimposed_VariableDeclaration", type=superimposed_OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type1: BinaryAssociation = BinaryAssociation(
    name="type1",
    ends={
        Property(name="superimposed_OclType", type=superimposed_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="superimposed_VariableDeclaration2", type=superimposed_OclType, multiplicity=Multiplicity(1, 1))
    }
)
varDcl3: BinaryAssociation = BinaryAssociation(
    name="varDcl3",
    ends={
        Property(name="superimposed_VariableDeclaration4", type=superimposed_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="superimposed_VariableExp", type=superimposed_VariableDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
variable5: BinaryAssociation = BinaryAssociation(
    name="variable5",
    ends={
        Property(name="superimposed_VariableDeclaration6", type=superimposed_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="superimposed_LetExp", type=superimposed_VariableDeclaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_7: BinaryAssociation = BinaryAssociation(
    name="in_7",
    ends={
        Property(name="superimposed_OclExpression9", type=superimposed_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="superimposed_LetExp8", type=superimposed_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments10: BinaryAssociation = BinaryAssociation(
    name="arguments10",
    ends={
        Property(name="superimposed_OclExpression11", type=superimposed_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="superimposed_OperationCallExp", type=superimposed_OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thenExpression12: BinaryAssociation = BinaryAssociation(
    name="thenExpression12",
    ends={
        Property(name="superimposed_OclExpression13", type=superimposed_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="superimposed_IfExp", type=superimposed_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition14: BinaryAssociation = BinaryAssociation(
    name="condition14",
    ends={
        Property(name="superimposed_OclExpression16", type=superimposed_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="superimposed_IfExp15", type=superimposed_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression17: BinaryAssociation = BinaryAssociation(
    name="elseExpression17",
    ends={
        Property(name="superimposed_OclExpression19", type=superimposed_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="superimposed_IfExp18", type=superimposed_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source20: BinaryAssociation = BinaryAssociation(
    name="source20",
    ends={
        Property(name="superimposed_OclExpression21", type=superimposed_BinaryOperatorCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="superimposed_BinaryOperatorCallExp", type=superimposed_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
argument22: BinaryAssociation = BinaryAssociation(
    name="argument22",
    ends={
        Property(name="superimposed_OclExpression24", type=superimposed_BinaryOperatorCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="superimposed_BinaryOperatorCallExp23", type=superimposed_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source25: BinaryAssociation = BinaryAssociation(
    name="source25",
    ends={
        Property(name="superimposed_OclExpression26", type=superimposed_UnaryOperatorCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="superimposed_UnaryOperatorCallExp", type=superimposed_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source27: BinaryAssociation = BinaryAssociation(
    name="source27",
    ends={
        Property(name="superimposed_OclExpression28", type=superimposed_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="superimposed_PropertyCallExp", type=superimposed_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body29: BinaryAssociation = BinaryAssociation(
    name="body29",
    ends={
        Property(name="superimposed_OclExpression30", type=superimposed_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="superimposed_LoopExp", type=superimposed_OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iteratorVar31: BinaryAssociation = BinaryAssociation(
    name="iteratorVar31",
    ends={
        Property(name="superimposed_Iterator", type=superimposed_IteratorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="superimposed_IteratorExp", type=superimposed_Iterator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
model32: BinaryAssociation = BinaryAssociation(
    name="model32",
    ends={
        Property(name="superimposed_OclModel", type=superimposed_OclModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="superimposed_OclModelElement", type=superimposed_OclModel, multiplicity=Multiplicity(1, 1))
    }
)
elements33: BinaryAssociation = BinaryAssociation(
    name="elements33",
    ends={
        Property(name="superimposed_OclExpression34", type=superimposed_CollectionExp, multiplicity=Multiplicity(1, 1)),
        Property(name="superimposed_CollectionExp", type=superimposed_OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_superimposed_BinaryOperatorCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=superimposed_BinaryOperatorCallExp)
gen_superimposed_VariableExp_OclExpression = Generalization(general=OclExpression, specific=superimposed_VariableExp)
gen_superimposed_OclUndefinedExp_OclExpression = Generalization(general=OclExpression, specific=superimposed_OclUndefinedExp)
gen_superimposed_LetExp_OclExpression = Generalization(general=OclExpression, specific=superimposed_LetExp)
gen_superimposed_OperationCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=superimposed_OperationCallExp)
gen_superimposed_CollectionOperationCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=superimposed_CollectionOperationCallExp)
gen_superimposed_NavigationCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=superimposed_NavigationCallExp)
gen_superimposed_IfExp_OclExpression = Generalization(general=OclExpression, specific=superimposed_IfExp)
gen_superimposed_OperatorCallExp_OclExpression = Generalization(general=OclExpression, specific=superimposed_OperatorCallExp)
gen_superimposed_OclModelElement_OclType = Generalization(general=OclType, specific=superimposed_OclModelElement)
gen_superimposed_UnaryOperatorCallExp_OperatorCallExp = Generalization(general=OperatorCallExp, specific=superimposed_UnaryOperatorCallExp)
gen_superimposed_PropertyCallExp_OclExpression = Generalization(general=OclExpression, specific=superimposed_PropertyCallExp)
gen_superimposed_LoopExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=superimposed_LoopExp)
gen_superimposed_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=superimposed_IteratorExp)
gen_superimposed_Iterator_VariableDeclaration = Generalization(general=VariableDeclaration, specific=superimposed_Iterator)
gen_superimposed_PrimitiveExp_OclExpression = Generalization(general=OclExpression, specific=superimposed_PrimitiveExp)
gen_superimposed_StringExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=superimposed_StringExp)
gen_superimposed_BooleanExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=superimposed_BooleanExp)
gen_superimposed_NumericExp_PrimitiveExp = Generalization(general=PrimitiveExp, specific=superimposed_NumericExp)
gen_superimposed_RealExp_NumericExp = Generalization(general=NumericExp, specific=superimposed_RealExp)
gen_superimposed_IntegerExp_NumericExp = Generalization(general=NumericExp, specific=superimposed_IntegerExp)
gen_superimposed_OclType_OclExpression = Generalization(general=OclExpression, specific=superimposed_OclType)
gen_superimposed_CollectionExp_OclExpression = Generalization(general=OclExpression, specific=superimposed_CollectionExp)
gen_superimposed_SetExp_CollectionExp = Generalization(general=CollectionExp, specific=superimposed_SetExp)

# Domain Model
domain_model = DomainModel(
    name="superimposed",
    types={superimposed_VariableDeclaration, superimposed_OclExpression, OperatorCallExp, superimposed_OclType, superimposed_VariableExp, OclExpression, superimposed_OclUndefinedExp, superimposed_LetExp, superimposed_OperationCallExp, PropertyCallExp, superimposed_CollectionOperationCallExp, OperationCallExp, superimposed_NavigationCallExp, superimposed_IfExp, superimposed_OperatorCallExp, superimposed_OclModelElement, superimposed_BinaryOperatorCallExp, OclType, superimposed_UnaryOperatorCallExp, superimposed_PropertyCallExp, superimposed_LoopExp, superimposed_IteratorExp, LoopExp, superimposed_Iterator, VariableDeclaration, superimposed_PrimitiveExp, superimposed_StringExp, PrimitiveExp, superimposed_BooleanExp, superimposed_NumericExp, superimposed_RealExp, NumericExp, superimposed_IntegerExp, superimposed_OclModel, superimposed_CollectionExp, superimposed_SetExp, CollectionExp},
    associations={initExpression0, type1, varDcl3, variable5, in_7, arguments10, thenExpression12, condition14, elseExpression17, source20, argument22, source25, source27, body29, iteratorVar31, model32, elements33},
    generalizations={gen_superimposed_BinaryOperatorCallExp_OperatorCallExp, gen_superimposed_VariableExp_OclExpression, gen_superimposed_OclUndefinedExp_OclExpression, gen_superimposed_LetExp_OclExpression, gen_superimposed_OperationCallExp_PropertyCallExp, gen_superimposed_CollectionOperationCallExp_OperationCallExp, gen_superimposed_NavigationCallExp_PropertyCallExp, gen_superimposed_IfExp_OclExpression, gen_superimposed_OperatorCallExp_OclExpression, gen_superimposed_OclModelElement_OclType, gen_superimposed_UnaryOperatorCallExp_OperatorCallExp, gen_superimposed_PropertyCallExp_OclExpression, gen_superimposed_LoopExp_PropertyCallExp, gen_superimposed_IteratorExp_LoopExp, gen_superimposed_Iterator_VariableDeclaration, gen_superimposed_PrimitiveExp_OclExpression, gen_superimposed_StringExp_PrimitiveExp, gen_superimposed_BooleanExp_PrimitiveExp, gen_superimposed_NumericExp_PrimitiveExp, gen_superimposed_RealExp_NumericExp, gen_superimposed_IntegerExp_NumericExp, gen_superimposed_OclType_OclExpression, gen_superimposed_CollectionExp_OclExpression, gen_superimposed_SetExp_CollectionExp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)