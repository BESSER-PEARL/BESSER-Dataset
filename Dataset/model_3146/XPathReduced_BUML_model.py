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
XPath_LocatedElement = Class(name="XPath::LocatedElement", is_abstract=True)
XPath_NamedElement = Class(name="XPath::NamedElement", is_abstract=True)
LocatedElement = Class(name="LocatedElement")
XPath_Expression = Class(name="XPath::Expression", is_abstract=True)
XPath_VariableExp = Class(name="XPath::VariableExp")
Expression = Class(name="Expression")
NamedElement = Class(name="NamedElement")
XPath_LiteralExp = Class(name="XPath::LiteralExp", is_abstract=True)
XPath_StringExp = Class(name="XPath::StringExp")
XPath_OperatorCallExp = Class(name="XPath::OperatorCallExp")
XPath_IntegerExp = Class(name="XPath::IntegerExp")
LiteralExp = Class(name="LiteralExp")

# XPath_LocatedElement class attributes and methods
XPath_LocatedElement_location: Property = Property(name="location", type=StringType)
XPath_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
XPath_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
XPath_LocatedElement.attributes={XPath_LocatedElement_location, XPath_LocatedElement_commentsBefore, XPath_LocatedElement_commentsAfter}

# XPath_NamedElement class attributes and methods
XPath_NamedElement_name: Property = Property(name="name", type=StringType)
XPath_NamedElement.attributes={XPath_NamedElement_name}

# LocatedElement class attributes and methods

# XPath_Expression class attributes and methods

# XPath_VariableExp class attributes and methods

# Expression class attributes and methods

# NamedElement class attributes and methods

# XPath_LiteralExp class attributes and methods

# XPath_StringExp class attributes and methods
XPath_StringExp_symbol: Property = Property(name="symbol", type=StringType)
XPath_StringExp.attributes={XPath_StringExp_symbol}

# XPath_OperatorCallExp class attributes and methods

# XPath_IntegerExp class attributes and methods
XPath_IntegerExp_symbol: Property = Property(name="symbol", type=StringType)
XPath_IntegerExp.attributes={XPath_IntegerExp_symbol}

# LiteralExp class attributes and methods

# Relationships
left0: BinaryAssociation = BinaryAssociation(
    name="left0",
    ends={
        Property(name="XPath_Expression", type=XPath_OperatorCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="XPath_OperatorCallExp", type=XPath_Expression, multiplicity=Multiplicity(1, 1))
    }
)
right1: BinaryAssociation = BinaryAssociation(
    name="right1",
    ends={
        Property(name="XPath_Expression3", type=XPath_OperatorCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="XPath_OperatorCallExp2", type=XPath_Expression, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_XPath_NamedElement_LocatedElement = Generalization(general=LocatedElement, specific=XPath_NamedElement)
gen_XPath_Expression_LocatedElement = Generalization(general=LocatedElement, specific=XPath_Expression)
gen_XPath_VariableExp_Expression = Generalization(general=Expression, specific=XPath_VariableExp)
gen_XPath_VariableExp_NamedElement = Generalization(general=NamedElement, specific=XPath_VariableExp)
gen_XPath_LiteralExp_Expression = Generalization(general=Expression, specific=XPath_LiteralExp)
gen_XPath_StringExp_LiteralExp = Generalization(general=LiteralExp, specific=XPath_StringExp)
gen_XPath_OperatorCallExp_NamedElement = Generalization(general=NamedElement, specific=XPath_OperatorCallExp)
gen_XPath_OperatorCallExp_LocatedElement = Generalization(general=LocatedElement, specific=XPath_OperatorCallExp)
gen_XPath_IntegerExp_LiteralExp = Generalization(general=LiteralExp, specific=XPath_IntegerExp)

# Domain Model
domain_model = DomainModel(
    name="XPath",
    types={XPath_LocatedElement, XPath_NamedElement, LocatedElement, XPath_Expression, XPath_VariableExp, Expression, NamedElement, XPath_LiteralExp, XPath_StringExp, XPath_OperatorCallExp, XPath_IntegerExp, LiteralExp},
    associations={left0, right1},
    generalizations={gen_XPath_NamedElement_LocatedElement, gen_XPath_Expression_LocatedElement, gen_XPath_VariableExp_Expression, gen_XPath_VariableExp_NamedElement, gen_XPath_LiteralExp_Expression, gen_XPath_StringExp_LiteralExp, gen_XPath_OperatorCallExp_NamedElement, gen_XPath_OperatorCallExp_LocatedElement, gen_XPath_IntegerExp_LiteralExp},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)