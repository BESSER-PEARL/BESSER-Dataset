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
SMTlib2extended_VariableExpression = Class(name="SMTlib2extended::VariableExpression")
Expression = Class(name="Expression")
SMTlib2extended_ConstExpression = Class(name="SMTlib2extended::ConstExpression", is_abstract=True)
SMTlib2extended_ConstBooleanExpression = Class(name="SMTlib2extended::ConstBooleanExpression")
ConstExpression = Class(name="ConstExpression")
SMTlib2extended_Instance = Class(name="SMTlib2extended::Instance")
SMTlib2extended_Variable = Class(name="SMTlib2extended::Variable")
SMTlib2extended_ConstIntegerExpression = Class(name="SMTlib2extended::ConstIntegerExpression")
SMTlib2extended_Expression = Class(name="SMTlib2extended::Expression")
SMTlib2extended_NamedElement = Class(name="SMTlib2extended::NamedElement")
NamedElement = Class(name="NamedElement")
SMTlib2extended_Predicate = Class(name="SMTlib2extended::Predicate")
Variable = Class(name="Variable")
SMTlib2extended_Bitvector = Class(name="SMTlib2extended::Bitvector")
NAryExpression = Class(name="NAryExpression")
SMTlib2extended_OrExpression = Class(name="SMTlib2extended::OrExpression")
SMTlib2extended_ConcatExpression = Class(name="SMTlib2extended::ConcatExpression")
SMTlib2extended_BinaryExpression = Class(name="SMTlib2extended::BinaryExpression")
SMTlib2extended_AddExpression = Class(name="SMTlib2extended::AddExpression")
BinaryExpression = Class(name="BinaryExpression")
SMTlib2extended_DivExpression = Class(name="SMTlib2extended::DivExpression")
SMTlib2extended_SubExpression = Class(name="SMTlib2extended::SubExpression")
SMTlib2extended_MulExpression = Class(name="SMTlib2extended::MulExpression")
SMTlib2extended_BitstringExpression = Class(name="SMTlib2extended::BitstringExpression")
SMTlib2extended_NAryExpression = Class(name="SMTlib2extended::NAryExpression")
SMTlib2extended_AndExpression = Class(name="SMTlib2extended::AndExpression")
SMTlib2extended_LessEqualsExpression = Class(name="SMTlib2extended::LessEqualsExpression")
SMTlib2extended_NandExpression = Class(name="SMTlib2extended::NandExpression")
SMTlib2extended_UnaryExpression = Class(name="SMTlib2extended::UnaryExpression")
SMTlib2extended_NotExpression = Class(name="SMTlib2extended::NotExpression")
UnaryExpression = Class(name="UnaryExpression")
SMTlib2extended_OneHotExpression = Class(name="SMTlib2extended::OneHotExpression")
SMTlib2extended_ExtractIndexExpression = Class(name="SMTlib2extended::ExtractIndexExpression")
SMTlib2extended_BvNotExpression = Class(name="SMTlib2extended::BvNotExpression")
SMTlib2extended_BvOrExpression = Class(name="SMTlib2extended::BvOrExpression")
SMTlib2extended_ModExpression = Class(name="SMTlib2extended::ModExpression")
SMTlib2extended_EqualsExpression = Class(name="SMTlib2extended::EqualsExpression")
SMTlib2extended_GreaterExpression = Class(name="SMTlib2extended::GreaterExpression")
SMTlib2extended_GreaterEqualsExpression = Class(name="SMTlib2extended::GreaterEqualsExpression")
SMTlib2extended_ImpliesExpression = Class(name="SMTlib2extended::ImpliesExpression")
SMTlib2extended_LessExpression = Class(name="SMTlib2extended::LessExpression")
SMTlib2extended_CardExpression = Class(name="SMTlib2extended::CardExpression")
SMTlib2extended_CardEqExpression = Class(name="SMTlib2extended::CardEqExpression")
CardExpression = Class(name="CardExpression")
SMTlib2extended_CardGeExpression = Class(name="SMTlib2extended::CardGeExpression")
SMTlib2extended_CardGtExpression = Class(name="SMTlib2extended::CardGtExpression")
SMTlib2extended_CardLeExpression = Class(name="SMTlib2extended::CardLeExpression")
SMTlib2extended_CardLtExpression = Class(name="SMTlib2extended::CardLtExpression")
SMTlib2extended_BvAndExpression = Class(name="SMTlib2extended::BvAndExpression")
SMTlib2extended_BvXorExpression = Class(name="SMTlib2extended::BvXorExpression")
SMTlib2extended_IteExpression = Class(name="SMTlib2extended::IteExpression")

# SMTlib2extended_VariableExpression class attributes and methods

# Expression class attributes and methods

# SMTlib2extended_ConstExpression class attributes and methods

# SMTlib2extended_ConstBooleanExpression class attributes and methods
SMTlib2extended_ConstBooleanExpression_value: Property = Property(name="value", type=BooleanType)
SMTlib2extended_ConstBooleanExpression.attributes={SMTlib2extended_ConstBooleanExpression_value}

# ConstExpression class attributes and methods

# SMTlib2extended_Instance class attributes and methods

# SMTlib2extended_Variable class attributes and methods

# SMTlib2extended_ConstIntegerExpression class attributes and methods
SMTlib2extended_ConstIntegerExpression_value: Property = Property(name="value", type=IntegerType)
SMTlib2extended_ConstIntegerExpression_width: Property = Property(name="width", type=IntegerType)
SMTlib2extended_ConstIntegerExpression.attributes={SMTlib2extended_ConstIntegerExpression_value, SMTlib2extended_ConstIntegerExpression_width}

# SMTlib2extended_Expression class attributes and methods

# SMTlib2extended_NamedElement class attributes and methods
SMTlib2extended_NamedElement_name: Property = Property(name="name", type=StringType)
SMTlib2extended_NamedElement.attributes={SMTlib2extended_NamedElement_name}

# NamedElement class attributes and methods

# SMTlib2extended_Predicate class attributes and methods

# Variable class attributes and methods

# SMTlib2extended_Bitvector class attributes and methods
SMTlib2extended_Bitvector_width: Property = Property(name="width", type=IntegerType)
SMTlib2extended_Bitvector.attributes={SMTlib2extended_Bitvector_width}

# NAryExpression class attributes and methods

# SMTlib2extended_OrExpression class attributes and methods

# SMTlib2extended_ConcatExpression class attributes and methods

# SMTlib2extended_BinaryExpression class attributes and methods

# SMTlib2extended_AddExpression class attributes and methods

# BinaryExpression class attributes and methods

# SMTlib2extended_DivExpression class attributes and methods

# SMTlib2extended_SubExpression class attributes and methods

# SMTlib2extended_MulExpression class attributes and methods

# SMTlib2extended_BitstringExpression class attributes and methods
SMTlib2extended_BitstringExpression_value: Property = Property(name="value", type=StringType)
SMTlib2extended_BitstringExpression.attributes={SMTlib2extended_BitstringExpression_value}

# SMTlib2extended_NAryExpression class attributes and methods

# SMTlib2extended_AndExpression class attributes and methods

# SMTlib2extended_LessEqualsExpression class attributes and methods

# SMTlib2extended_NandExpression class attributes and methods

# SMTlib2extended_UnaryExpression class attributes and methods

# SMTlib2extended_NotExpression class attributes and methods

# UnaryExpression class attributes and methods

# SMTlib2extended_OneHotExpression class attributes and methods

# SMTlib2extended_ExtractIndexExpression class attributes and methods
SMTlib2extended_ExtractIndexExpression_start: Property = Property(name="start", type=IntegerType)
SMTlib2extended_ExtractIndexExpression_end: Property = Property(name="end", type=IntegerType)
SMTlib2extended_ExtractIndexExpression.attributes={SMTlib2extended_ExtractIndexExpression_end, SMTlib2extended_ExtractIndexExpression_start}

# SMTlib2extended_BvNotExpression class attributes and methods

# SMTlib2extended_BvOrExpression class attributes and methods

# SMTlib2extended_ModExpression class attributes and methods

# SMTlib2extended_EqualsExpression class attributes and methods

# SMTlib2extended_GreaterExpression class attributes and methods

# SMTlib2extended_GreaterEqualsExpression class attributes and methods

# SMTlib2extended_ImpliesExpression class attributes and methods

# SMTlib2extended_LessExpression class attributes and methods

# SMTlib2extended_CardExpression class attributes and methods
SMTlib2extended_CardExpression_k: Property = Property(name="k", type=IntegerType)
SMTlib2extended_CardExpression.attributes={SMTlib2extended_CardExpression_k}

# SMTlib2extended_CardEqExpression class attributes and methods

# CardExpression class attributes and methods

# SMTlib2extended_CardGeExpression class attributes and methods

# SMTlib2extended_CardGtExpression class attributes and methods

# SMTlib2extended_CardLeExpression class attributes and methods

# SMTlib2extended_CardLtExpression class attributes and methods

# SMTlib2extended_BvAndExpression class attributes and methods

# SMTlib2extended_BvXorExpression class attributes and methods

# SMTlib2extended_IteExpression class attributes and methods

# Relationships
variable3: BinaryAssociation = BinaryAssociation(
    name="variable3",
    ends={
        Property(name="SMTlib2extended_Variable4", type=SMTlib2extended_VariableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="SMTlib2extended_VariableExpression", type=SMTlib2extended_Variable, multiplicity=Multiplicity(1, 1))
    }
)
variables0: BinaryAssociation = BinaryAssociation(
    name="variables0",
    ends={
        Property(name="SMTlib2extended_Variable", type=SMTlib2extended_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="SMTlib2extended_Instance", type=SMTlib2extended_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assertions1: BinaryAssociation = BinaryAssociation(
    name="assertions1",
    ends={
        Property(name="SMTlib2extended_Expression", type=SMTlib2extended_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="SMTlib2extended_Instance2", type=SMTlib2extended_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lhs7: BinaryAssociation = BinaryAssociation(
    name="lhs7",
    ends={
        Property(name="SMTlib2extended_Expression8", type=SMTlib2extended_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="SMTlib2extended_BinaryExpression", type=SMTlib2extended_Expression, multiplicity=Multiplicity(1, 1))
    }
)
rhs9: BinaryAssociation = BinaryAssociation(
    name="rhs9",
    ends={
        Property(name="SMTlib2extended_Expression11", type=SMTlib2extended_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="SMTlib2extended_BinaryExpression10", type=SMTlib2extended_Expression, multiplicity=Multiplicity(1, 1))
    }
)
expressions5: BinaryAssociation = BinaryAssociation(
    name="expressions5",
    ends={
        Property(name="SMTlib2extended_Expression6", type=SMTlib2extended_NAryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="SMTlib2extended_NAryExpression", type=SMTlib2extended_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
expr12: BinaryAssociation = BinaryAssociation(
    name="expr12",
    ends={
        Property(name="SMTlib2extended_Expression13", type=SMTlib2extended_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="SMTlib2extended_UnaryExpression", type=SMTlib2extended_Expression, multiplicity=Multiplicity(1, 1))
    }
)
elseexpr19: BinaryAssociation = BinaryAssociation(
    name="elseexpr19",
    ends={
        Property(name="SMTlib2extended_Expression21", type=SMTlib2extended_IteExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="SMTlib2extended_IteExpression20", type=SMTlib2extended_Expression, multiplicity=Multiplicity(1, 1))
    }
)
expressions22: BinaryAssociation = BinaryAssociation(
    name="expressions22",
    ends={
        Property(name="SMTlib2extended_Expression23", type=SMTlib2extended_CardExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="SMTlib2extended_CardExpression", type=SMTlib2extended_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
condition14: BinaryAssociation = BinaryAssociation(
    name="condition14",
    ends={
        Property(name="SMTlib2extended_Expression15", type=SMTlib2extended_IteExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="SMTlib2extended_IteExpression", type=SMTlib2extended_Expression, multiplicity=Multiplicity(1, 1))
    }
)
thenexpr16: BinaryAssociation = BinaryAssociation(
    name="thenexpr16",
    ends={
        Property(name="SMTlib2extended_Expression18", type=SMTlib2extended_IteExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="SMTlib2extended_IteExpression17", type=SMTlib2extended_Expression, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_SMTlib2extended_Bitvector_Variable = Generalization(general=Variable, specific=SMTlib2extended_Bitvector)
gen_SMTlib2extended_Expression_NamedElement = Generalization(general=NamedElement, specific=SMTlib2extended_Expression)
gen_SMTlib2extended_VariableExpression_Expression = Generalization(general=Expression, specific=SMTlib2extended_VariableExpression)
gen_SMTlib2extended_ConstExpression_Expression = Generalization(general=Expression, specific=SMTlib2extended_ConstExpression)
gen_SMTlib2extended_ConstBooleanExpression_ConstExpression = Generalization(general=ConstExpression, specific=SMTlib2extended_ConstBooleanExpression)
gen_SMTlib2extended_ConstIntegerExpression_ConstExpression = Generalization(general=ConstExpression, specific=SMTlib2extended_ConstIntegerExpression)
gen_SMTlib2extended_Variable_NamedElement = Generalization(general=NamedElement, specific=SMTlib2extended_Variable)
gen_SMTlib2extended_Predicate_Variable = Generalization(general=Variable, specific=SMTlib2extended_Predicate)
gen_SMTlib2extended_AndExpression_NAryExpression = Generalization(general=NAryExpression, specific=SMTlib2extended_AndExpression)
gen_SMTlib2extended_OrExpression_NAryExpression = Generalization(general=NAryExpression, specific=SMTlib2extended_OrExpression)
gen_SMTlib2extended_ConcatExpression_NAryExpression = Generalization(general=NAryExpression, specific=SMTlib2extended_ConcatExpression)
gen_SMTlib2extended_BinaryExpression_Expression = Generalization(general=Expression, specific=SMTlib2extended_BinaryExpression)
gen_SMTlib2extended_AddExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=SMTlib2extended_AddExpression)
gen_SMTlib2extended_DivExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=SMTlib2extended_DivExpression)
gen_SMTlib2extended_SubExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=SMTlib2extended_SubExpression)
gen_SMTlib2extended_MulExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=SMTlib2extended_MulExpression)
gen_SMTlib2extended_BitstringExpression_ConstExpression = Generalization(general=ConstExpression, specific=SMTlib2extended_BitstringExpression)
gen_SMTlib2extended_NAryExpression_Expression = Generalization(general=Expression, specific=SMTlib2extended_NAryExpression)
gen_SMTlib2extended_LessEqualsExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=SMTlib2extended_LessEqualsExpression)
gen_SMTlib2extended_NandExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=SMTlib2extended_NandExpression)
gen_SMTlib2extended_UnaryExpression_Expression = Generalization(general=Expression, specific=SMTlib2extended_UnaryExpression)
gen_SMTlib2extended_NotExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=SMTlib2extended_NotExpression)
gen_SMTlib2extended_OneHotExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=SMTlib2extended_OneHotExpression)
gen_SMTlib2extended_ExtractIndexExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=SMTlib2extended_ExtractIndexExpression)
gen_SMTlib2extended_BvNotExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=SMTlib2extended_BvNotExpression)
gen_SMTlib2extended_BvOrExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=SMTlib2extended_BvOrExpression)
gen_SMTlib2extended_ModExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=SMTlib2extended_ModExpression)
gen_SMTlib2extended_EqualsExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=SMTlib2extended_EqualsExpression)
gen_SMTlib2extended_GreaterExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=SMTlib2extended_GreaterExpression)
gen_SMTlib2extended_GreaterEqualsExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=SMTlib2extended_GreaterEqualsExpression)
gen_SMTlib2extended_ImpliesExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=SMTlib2extended_ImpliesExpression)
gen_SMTlib2extended_LessExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=SMTlib2extended_LessExpression)
gen_SMTlib2extended_CardExpression_Expression = Generalization(general=Expression, specific=SMTlib2extended_CardExpression)
gen_SMTlib2extended_CardEqExpression_CardExpression = Generalization(general=CardExpression, specific=SMTlib2extended_CardEqExpression)
gen_SMTlib2extended_CardGeExpression_CardExpression = Generalization(general=CardExpression, specific=SMTlib2extended_CardGeExpression)
gen_SMTlib2extended_CardGtExpression_CardExpression = Generalization(general=CardExpression, specific=SMTlib2extended_CardGtExpression)
gen_SMTlib2extended_CardLeExpression_CardExpression = Generalization(general=CardExpression, specific=SMTlib2extended_CardLeExpression)
gen_SMTlib2extended_CardLtExpression_CardExpression = Generalization(general=CardExpression, specific=SMTlib2extended_CardLtExpression)
gen_SMTlib2extended_BvAndExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=SMTlib2extended_BvAndExpression)
gen_SMTlib2extended_BvXorExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=SMTlib2extended_BvXorExpression)
gen_SMTlib2extended_IteExpression_Expression = Generalization(general=Expression, specific=SMTlib2extended_IteExpression)

# Domain Model
domain_model = DomainModel(
    name="SMTlib2extended",
    types={SMTlib2extended_VariableExpression, Expression, SMTlib2extended_ConstExpression, SMTlib2extended_ConstBooleanExpression, ConstExpression, SMTlib2extended_Instance, SMTlib2extended_Variable, SMTlib2extended_ConstIntegerExpression, SMTlib2extended_Expression, SMTlib2extended_NamedElement, NamedElement, SMTlib2extended_Predicate, Variable, SMTlib2extended_Bitvector, NAryExpression, SMTlib2extended_OrExpression, SMTlib2extended_ConcatExpression, SMTlib2extended_BinaryExpression, SMTlib2extended_AddExpression, BinaryExpression, SMTlib2extended_DivExpression, SMTlib2extended_SubExpression, SMTlib2extended_MulExpression, SMTlib2extended_BitstringExpression, SMTlib2extended_NAryExpression, SMTlib2extended_AndExpression, SMTlib2extended_LessEqualsExpression, SMTlib2extended_NandExpression, SMTlib2extended_UnaryExpression, SMTlib2extended_NotExpression, UnaryExpression, SMTlib2extended_OneHotExpression, SMTlib2extended_ExtractIndexExpression, SMTlib2extended_BvNotExpression, SMTlib2extended_BvOrExpression, SMTlib2extended_ModExpression, SMTlib2extended_EqualsExpression, SMTlib2extended_GreaterExpression, SMTlib2extended_GreaterEqualsExpression, SMTlib2extended_ImpliesExpression, SMTlib2extended_LessExpression, SMTlib2extended_CardExpression, SMTlib2extended_CardEqExpression, CardExpression, SMTlib2extended_CardGeExpression, SMTlib2extended_CardGtExpression, SMTlib2extended_CardLeExpression, SMTlib2extended_CardLtExpression, SMTlib2extended_BvAndExpression, SMTlib2extended_BvXorExpression, SMTlib2extended_IteExpression},
    associations={variable3, variables0, assertions1, lhs7, rhs9, expressions5, expr12, elseexpr19, expressions22, condition14, thenexpr16},
    generalizations={gen_SMTlib2extended_Bitvector_Variable, gen_SMTlib2extended_Expression_NamedElement, gen_SMTlib2extended_VariableExpression_Expression, gen_SMTlib2extended_ConstExpression_Expression, gen_SMTlib2extended_ConstBooleanExpression_ConstExpression, gen_SMTlib2extended_ConstIntegerExpression_ConstExpression, gen_SMTlib2extended_Variable_NamedElement, gen_SMTlib2extended_Predicate_Variable, gen_SMTlib2extended_AndExpression_NAryExpression, gen_SMTlib2extended_OrExpression_NAryExpression, gen_SMTlib2extended_ConcatExpression_NAryExpression, gen_SMTlib2extended_BinaryExpression_Expression, gen_SMTlib2extended_AddExpression_BinaryExpression, gen_SMTlib2extended_DivExpression_BinaryExpression, gen_SMTlib2extended_SubExpression_BinaryExpression, gen_SMTlib2extended_MulExpression_BinaryExpression, gen_SMTlib2extended_BitstringExpression_ConstExpression, gen_SMTlib2extended_NAryExpression_Expression, gen_SMTlib2extended_LessEqualsExpression_BinaryExpression, gen_SMTlib2extended_NandExpression_BinaryExpression, gen_SMTlib2extended_UnaryExpression_Expression, gen_SMTlib2extended_NotExpression_UnaryExpression, gen_SMTlib2extended_OneHotExpression_UnaryExpression, gen_SMTlib2extended_ExtractIndexExpression_UnaryExpression, gen_SMTlib2extended_BvNotExpression_UnaryExpression, gen_SMTlib2extended_BvOrExpression_BinaryExpression, gen_SMTlib2extended_ModExpression_BinaryExpression, gen_SMTlib2extended_EqualsExpression_BinaryExpression, gen_SMTlib2extended_GreaterExpression_BinaryExpression, gen_SMTlib2extended_GreaterEqualsExpression_BinaryExpression, gen_SMTlib2extended_ImpliesExpression_BinaryExpression, gen_SMTlib2extended_LessExpression_BinaryExpression, gen_SMTlib2extended_CardExpression_Expression, gen_SMTlib2extended_CardEqExpression_CardExpression, gen_SMTlib2extended_CardGeExpression_CardExpression, gen_SMTlib2extended_CardGtExpression_CardExpression, gen_SMTlib2extended_CardLeExpression_CardExpression, gen_SMTlib2extended_CardLtExpression_CardExpression, gen_SMTlib2extended_BvAndExpression_BinaryExpression, gen_SMTlib2extended_BvXorExpression_BinaryExpression, gen_SMTlib2extended_IteExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)