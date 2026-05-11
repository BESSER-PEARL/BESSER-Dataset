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
XPath_LocatedElement = Class(name="XPath_LocatedElement", is_abstract=True)
XPath_NamedElement = Class(name="XPath_NamedElement", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
XPath_Expression = Class(name="XPath_Expression", is_abstract=True)
XPath_VariableExp = Class(name="XPath_VariableExp")
Expression = Class(name="Expression")
NamedElement = Class(name="NamedElement")
XPath_PathExpression = Class(name="XPath_PathExpression")
XPath_Step = Class(name="XPath_Step")
XPath_Axis = Class(name="XPath_Axis", is_abstract=True)
XPath_NodeTest = Class(name="XPath_NodeTest", is_abstract=True)
XPath_Predicate = Class(name="XPath_Predicate")
XPath_LiteralExp = Class(name="XPath_LiteralExp", is_abstract=True)
XPath_IntegerExp = Class(name="XPath_IntegerExp")
LiteralExp = Class(name="LiteralExp")
XPath_StringExp = Class(name="XPath_StringExp")
XPath_NameTest = Class(name="XPath_NameTest")
NodeTest = Class(name="NodeTest")
XPath_WildCardTest = Class(name="XPath_WildCardTest")
XPath_IsNodeTest = Class(name="XPath_IsNodeTest")
XPath_IsTextTest = Class(name="XPath_IsTextTest")
XPath_AncestorAxis = Class(name="XPath_AncestorAxis")
Axis = Class(name="Axis")
XPath_AncestorOrSelfAxis = Class(name="XPath_AncestorOrSelfAxis")
XPath_AttributeAxis = Class(name="XPath_AttributeAxis")
XPath_ChildAxis = Class(name="XPath_ChildAxis")
XPath_DescendantAxis = Class(name="XPath_DescendantAxis")
XPath_DescendantOrSelfAxis = Class(name="XPath_DescendantOrSelfAxis")
XPath_FollowingAxis = Class(name="XPath_FollowingAxis")
XPath_FollowingSiblingAxis = Class(name="XPath_FollowingSiblingAxis")
XPath_NamespaceAxis = Class(name="XPath_NamespaceAxis")
XPath_ParentAxis = Class(name="XPath_ParentAxis")
XPath_PrecedingAxis = Class(name="XPath_PrecedingAxis")
XPath_PrecedingSiblingAxis = Class(name="XPath_PrecedingSiblingAxis")
XPath_SelfAxis = Class(name="XPath_SelfAxis")
XPath_OperatorCallExp = Class(name="XPath_OperatorCallExp")
XPath_FunctionCallExp = Class(name="XPath_FunctionCallExp")

# XPath_LocatedElement class attributes and methods
XPath_LocatedElement_location: Property = Property(name="location", type=StringType)
XPath_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
XPath_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
XPath_LocatedElement.attributes={XPath_LocatedElement_commentsBefore, XPath_LocatedElement_commentsAfter, XPath_LocatedElement_location}

# XPath_NamedElement class attributes and methods
XPath_NamedElement_name: Property = Property(name="name", type=StringType)
XPath_NamedElement.attributes={XPath_NamedElement_name}

# LocatedElement class attributes and methods

# XPath_Expression class attributes and methods

# XPath_VariableExp class attributes and methods

# Expression class attributes and methods

# NamedElement class attributes and methods

# XPath_PathExpression class attributes and methods
XPath_PathExpression_isAbsolute: Property = Property(name="isAbsolute", type=StringType)
XPath_PathExpression.attributes={XPath_PathExpression_isAbsolute}

# XPath_Step class attributes and methods

# XPath_Axis class attributes and methods

# XPath_NodeTest class attributes and methods

# XPath_Predicate class attributes and methods

# XPath_LiteralExp class attributes and methods

# XPath_IntegerExp class attributes and methods
XPath_IntegerExp_symbol: Property = Property(name="symbol", type=StringType)
XPath_IntegerExp.attributes={XPath_IntegerExp_symbol}

# LiteralExp class attributes and methods

# XPath_StringExp class attributes and methods
XPath_StringExp_symbol: Property = Property(name="symbol", type=StringType)
XPath_StringExp.attributes={XPath_StringExp_symbol}

# XPath_NameTest class attributes and methods

# NodeTest class attributes and methods

# XPath_WildCardTest class attributes and methods

# XPath_IsNodeTest class attributes and methods

# XPath_IsTextTest class attributes and methods

# XPath_AncestorAxis class attributes and methods

# Axis class attributes and methods

# XPath_AncestorOrSelfAxis class attributes and methods

# XPath_AttributeAxis class attributes and methods

# XPath_ChildAxis class attributes and methods

# XPath_DescendantAxis class attributes and methods

# XPath_DescendantOrSelfAxis class attributes and methods

# XPath_FollowingAxis class attributes and methods

# XPath_FollowingSiblingAxis class attributes and methods

# XPath_NamespaceAxis class attributes and methods

# XPath_ParentAxis class attributes and methods

# XPath_PrecedingAxis class attributes and methods

# XPath_PrecedingSiblingAxis class attributes and methods

# XPath_SelfAxis class attributes and methods

# XPath_OperatorCallExp class attributes and methods

# XPath_FunctionCallExp class attributes and methods

# Relationships
steps0: BinaryAssociation = BinaryAssociation(
    name="steps0",
    ends={
        Property(name="XPath_Step", type=XPath_PathExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="XPath_PathExpression", type=XPath_Step, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
axis1: BinaryAssociation = BinaryAssociation(
    name="axis1",
    ends={
        Property(name="XPath_Axis", type=XPath_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="XPath_Step2", type=XPath_Axis, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nodeTest3: BinaryAssociation = BinaryAssociation(
    name="nodeTest3",
    ends={
        Property(name="XPath_NodeTest", type=XPath_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="XPath_Step4", type=XPath_NodeTest, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
predicates5: BinaryAssociation = BinaryAssociation(
    name="predicates5",
    ends={
        Property(name="XPath_Predicate", type=XPath_Step, multiplicity=Multiplicity(1, 1)),
        Property(name="XPath_Step6", type=XPath_Predicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression7: BinaryAssociation = BinaryAssociation(
    name="expression7",
    ends={
        Property(name="XPath_Expression", type=XPath_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="XPath_Predicate8", type=XPath_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments14: BinaryAssociation = BinaryAssociation(
    name="arguments14",
    ends={
        Property(name="XPath_Expression15", type=XPath_FunctionCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="XPath_FunctionCallExp", type=XPath_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left9: BinaryAssociation = BinaryAssociation(
    name="left9",
    ends={
        Property(name="XPath_Expression10", type=XPath_OperatorCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="XPath_OperatorCallExp", type=XPath_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right11: BinaryAssociation = BinaryAssociation(
    name="right11",
    ends={
        Property(name="XPath_Expression13", type=XPath_OperatorCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="XPath_OperatorCallExp12", type=XPath_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_XPath_NamedElement_LocatedElement = Generalization(general=LocatedElement, specific=XPath_NamedElement)
gen_XPath_Expression_LocatedElement = Generalization(general=LocatedElement, specific=XPath_Expression)
gen_XPath_VariableExp_Expression = Generalization(general=Expression, specific=XPath_VariableExp)
gen_XPath_VariableExp_NamedElement = Generalization(general=NamedElement, specific=XPath_VariableExp)
gen_XPath_PathExpression_Expression = Generalization(general=Expression, specific=XPath_PathExpression)
gen_XPath_Step_LocatedElement = Generalization(general=LocatedElement, specific=XPath_Step)
gen_XPath_Predicate_LocatedElement = Generalization(general=LocatedElement, specific=XPath_Predicate)
gen_XPath_LiteralExp_Expression = Generalization(general=Expression, specific=XPath_LiteralExp)
gen_XPath_IntegerExp_LiteralExp = Generalization(general=LiteralExp, specific=XPath_IntegerExp)
gen_XPath_StringExp_LiteralExp = Generalization(general=LiteralExp, specific=XPath_StringExp)
gen_XPath_NodeTest_LocatedElement = Generalization(general=LocatedElement, specific=XPath_NodeTest)
gen_XPath_NameTest_NodeTest = Generalization(general=NodeTest, specific=XPath_NameTest)
gen_XPath_NameTest_NamedElement = Generalization(general=NamedElement, specific=XPath_NameTest)
gen_XPath_WildCardTest_NodeTest = Generalization(general=NodeTest, specific=XPath_WildCardTest)
gen_XPath_IsNodeTest_NodeTest = Generalization(general=NodeTest, specific=XPath_IsNodeTest)
gen_XPath_IsTextTest_NodeTest = Generalization(general=NodeTest, specific=XPath_IsTextTest)
gen_XPath_Axis_LocatedElement = Generalization(general=LocatedElement, specific=XPath_Axis)
gen_XPath_AncestorAxis_Axis = Generalization(general=Axis, specific=XPath_AncestorAxis)
gen_XPath_AncestorOrSelfAxis_Axis = Generalization(general=Axis, specific=XPath_AncestorOrSelfAxis)
gen_XPath_AttributeAxis_Axis = Generalization(general=Axis, specific=XPath_AttributeAxis)
gen_XPath_ChildAxis_Axis = Generalization(general=Axis, specific=XPath_ChildAxis)
gen_XPath_DescendantAxis_Axis = Generalization(general=Axis, specific=XPath_DescendantAxis)
gen_XPath_DescendantOrSelfAxis_Axis = Generalization(general=Axis, specific=XPath_DescendantOrSelfAxis)
gen_XPath_FollowingAxis_Axis = Generalization(general=Axis, specific=XPath_FollowingAxis)
gen_XPath_FollowingSiblingAxis_Axis = Generalization(general=Axis, specific=XPath_FollowingSiblingAxis)
gen_XPath_NamespaceAxis_Axis = Generalization(general=Axis, specific=XPath_NamespaceAxis)
gen_XPath_ParentAxis_Axis = Generalization(general=Axis, specific=XPath_ParentAxis)
gen_XPath_PrecedingAxis_Axis = Generalization(general=Axis, specific=XPath_PrecedingAxis)
gen_XPath_PrecedingSiblingAxis_Axis = Generalization(general=Axis, specific=XPath_PrecedingSiblingAxis)
gen_XPath_SelfAxis_Axis = Generalization(general=Axis, specific=XPath_SelfAxis)
gen_XPath_OperatorCallExp_Expression = Generalization(general=Expression, specific=XPath_OperatorCallExp)
gen_XPath_OperatorCallExp_NamedElement = Generalization(general=NamedElement, specific=XPath_OperatorCallExp)
gen_XPath_FunctionCallExp_Expression = Generalization(general=Expression, specific=XPath_FunctionCallExp)
gen_XPath_FunctionCallExp_NamedElement = Generalization(general=NamedElement, specific=XPath_FunctionCallExp)

# Domain Model
domain_model = DomainModel(
    name="XPath",
    types={XPath_LocatedElement, XPath_NamedElement, LocatedElement, XPath_Expression, XPath_VariableExp, Expression, NamedElement, XPath_PathExpression, XPath_Step, XPath_Axis, XPath_NodeTest, XPath_Predicate, XPath_LiteralExp, XPath_IntegerExp, LiteralExp, XPath_StringExp, XPath_NameTest, NodeTest, XPath_WildCardTest, XPath_IsNodeTest, XPath_IsTextTest, XPath_AncestorAxis, Axis, XPath_AncestorOrSelfAxis, XPath_AttributeAxis, XPath_ChildAxis, XPath_DescendantAxis, XPath_DescendantOrSelfAxis, XPath_FollowingAxis, XPath_FollowingSiblingAxis, XPath_NamespaceAxis, XPath_ParentAxis, XPath_PrecedingAxis, XPath_PrecedingSiblingAxis, XPath_SelfAxis, XPath_OperatorCallExp, XPath_FunctionCallExp},
    associations={steps0, axis1, nodeTest3, predicates5, expression7, arguments14, left9, right11},
    generalizations={gen_XPath_NamedElement_LocatedElement, gen_XPath_Expression_LocatedElement, gen_XPath_VariableExp_Expression, gen_XPath_VariableExp_NamedElement, gen_XPath_PathExpression_Expression, gen_XPath_Step_LocatedElement, gen_XPath_Predicate_LocatedElement, gen_XPath_LiteralExp_Expression, gen_XPath_IntegerExp_LiteralExp, gen_XPath_StringExp_LiteralExp, gen_XPath_NodeTest_LocatedElement, gen_XPath_NameTest_NodeTest, gen_XPath_NameTest_NamedElement, gen_XPath_WildCardTest_NodeTest, gen_XPath_IsNodeTest_NodeTest, gen_XPath_IsTextTest_NodeTest, gen_XPath_Axis_LocatedElement, gen_XPath_AncestorAxis_Axis, gen_XPath_AncestorOrSelfAxis_Axis, gen_XPath_AttributeAxis_Axis, gen_XPath_ChildAxis_Axis, gen_XPath_DescendantAxis_Axis, gen_XPath_DescendantOrSelfAxis_Axis, gen_XPath_FollowingAxis_Axis, gen_XPath_FollowingSiblingAxis_Axis, gen_XPath_NamespaceAxis_Axis, gen_XPath_ParentAxis_Axis, gen_XPath_PrecedingAxis_Axis, gen_XPath_PrecedingSiblingAxis_Axis, gen_XPath_SelfAxis_Axis, gen_XPath_OperatorCallExp_Expression, gen_XPath_OperatorCallExp_NamedElement, gen_XPath_FunctionCallExp_Expression, gen_XPath_FunctionCallExp_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)