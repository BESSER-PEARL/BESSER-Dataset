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
Operand = Class(name="Operand")
hydraconstraints_Model = Class(name="hydraconstraints::Model")
hydraconstraints_Constraint = Class(name="hydraconstraints::Constraint")
hydraconstraints_BoolOperand = Class(name="hydraconstraints::BoolOperand", is_abstract=True)
hydraconstraints_Operand = Class(name="hydraconstraints::Operand", is_abstract=True)
hydraconstraints_LessOrEqual = Class(name="hydraconstraints::LessOrEqual")
hydraconstraints_BoolPriorityOperand1 = Class(name="hydraconstraints::BoolPriorityOperand1")
hydraconstraints_BoolPriorityOperand2 = Class(name="hydraconstraints::BoolPriorityOperand2")
hydraconstraints_LogicalOperator = Class(name="hydraconstraints::LogicalOperator", is_abstract=True)
BoolOperand = Class(name="BoolOperand")
hydraconstraints_UnaryOp = Class(name="hydraconstraints::UnaryOp", is_abstract=True)
LogicalOperator = Class(name="LogicalOperator")
hydraconstraints_Neg = Class(name="hydraconstraints::Neg")
UnaryOp = Class(name="UnaryOp")
hydraconstraints_BinaryOp = Class(name="hydraconstraints::BinaryOp", is_abstract=True)
hydraconstraints_And = Class(name="hydraconstraints::And")
BinaryOp = Class(name="BinaryOp")
hydraconstraints_Or = Class(name="hydraconstraints::Or")
hydraconstraints_Implies = Class(name="hydraconstraints::Implies")
hydraconstraints_Xor = Class(name="hydraconstraints::Xor")
hydraconstraints_Comparison = Class(name="hydraconstraints::Comparison", is_abstract=True)
hydraconstraints_NumPriorityOperand2 = Class(name="hydraconstraints::NumPriorityOperand2")
hydraconstraints_More = Class(name="hydraconstraints::More")
Comparison = Class(name="Comparison")
hydraconstraints_MoreOrEqual = Class(name="hydraconstraints::MoreOrEqual")
hydraconstraints_NotEqual = Class(name="hydraconstraints::NotEqual")
hydraconstraints_Less = Class(name="hydraconstraints::Less")
hydraconstraints_Equal = Class(name="hydraconstraints::Equal")
hydraconstraints_NumOperand = Class(name="hydraconstraints::NumOperand", is_abstract=True)
hydraconstraints_NumPriorityOperand1 = Class(name="hydraconstraints::NumPriorityOperand1")
hydraconstraints_NumOperator = Class(name="hydraconstraints::NumOperator", is_abstract=True)
NumOperand = Class(name="NumOperand")
hydraconstraints_Plus = Class(name="hydraconstraints::Plus")
NumOperator = Class(name="NumOperator")
hydraconstraints_Mul = Class(name="hydraconstraints::Mul")
hydraconstraints_Minus = Class(name="hydraconstraints::Minus")
hydraconstraints_Div = Class(name="hydraconstraints::Div")
hydraconstraints_NumOperandChoices = Class(name="hydraconstraints::NumOperandChoices", is_abstract=True)
hydraconstraints_MultipleFeature = Class(name="hydraconstraints::MultipleFeature")
NumOperandChoices = Class(name="NumOperandChoices")
hydraconstraints_SimpleFeature = Class(name="hydraconstraints::SimpleFeature")
BoolOperandChoices = Class(name="BoolOperandChoices")
hydraconstraints_BoolOperandChoices = Class(name="hydraconstraints::BoolOperandChoices", is_abstract=True)
hydraconstraints_Context = Class(name="hydraconstraints::Context")
hydraconstraints_Selection = Class(name="hydraconstraints::Selection", is_abstract=True)
hydraconstraints_Any = Class(name="hydraconstraints::Any")
Selection = Class(name="Selection")
hydraconstraints_All = Class(name="hydraconstraints::All")
hydraconstraints_Number = Class(name="hydraconstraints::Number")

# Operand class attributes and methods

# hydraconstraints_Model class attributes and methods
hydraconstraints_Model_featureList: Property = Property(name="featureList", type=StringType)
hydraconstraints_Model_m_featureModelExists: Method = Method(name="featureModelExists", parameters={Parameter(name='context'), Parameter(name='diagnostics')}, type=BooleanType)
hydraconstraints_Model.attributes={hydraconstraints_Model_featureList}
hydraconstraints_Model.methods={hydraconstraints_Model_m_featureModelExists}

# hydraconstraints_Constraint class attributes and methods

# hydraconstraints_BoolOperand class attributes and methods

# hydraconstraints_Operand class attributes and methods
hydraconstraints_Operand_m_evaluate: Method = Method(name="evaluate", parameters={Parameter(name='modelDirection'), Parameter(name='featureContext')}, type=IntegerType)
hydraconstraints_Operand.methods={hydraconstraints_Operand_m_evaluate}

# hydraconstraints_LessOrEqual class attributes and methods

# hydraconstraints_BoolPriorityOperand1 class attributes and methods

# hydraconstraints_BoolPriorityOperand2 class attributes and methods

# hydraconstraints_LogicalOperator class attributes and methods

# BoolOperand class attributes and methods

# hydraconstraints_UnaryOp class attributes and methods

# LogicalOperator class attributes and methods

# hydraconstraints_Neg class attributes and methods

# UnaryOp class attributes and methods

# hydraconstraints_BinaryOp class attributes and methods

# hydraconstraints_And class attributes and methods

# BinaryOp class attributes and methods

# hydraconstraints_Or class attributes and methods

# hydraconstraints_Implies class attributes and methods

# hydraconstraints_Xor class attributes and methods

# hydraconstraints_Comparison class attributes and methods

# hydraconstraints_NumPriorityOperand2 class attributes and methods

# hydraconstraints_More class attributes and methods

# Comparison class attributes and methods

# hydraconstraints_MoreOrEqual class attributes and methods

# hydraconstraints_NotEqual class attributes and methods

# hydraconstraints_Less class attributes and methods

# hydraconstraints_Equal class attributes and methods

# hydraconstraints_NumOperand class attributes and methods

# hydraconstraints_NumPriorityOperand1 class attributes and methods

# hydraconstraints_NumOperator class attributes and methods

# NumOperand class attributes and methods

# hydraconstraints_Plus class attributes and methods

# NumOperator class attributes and methods

# hydraconstraints_Mul class attributes and methods

# hydraconstraints_Minus class attributes and methods

# hydraconstraints_Div class attributes and methods

# hydraconstraints_NumOperandChoices class attributes and methods

# hydraconstraints_MultipleFeature class attributes and methods
hydraconstraints_MultipleFeature_featureName: Property = Property(name="featureName", type=StringType)
hydraconstraints_MultipleFeature_m_isMultipleFeature: Method = Method(name="isMultipleFeature", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
hydraconstraints_MultipleFeature.attributes={hydraconstraints_MultipleFeature_featureName}
hydraconstraints_MultipleFeature.methods={hydraconstraints_MultipleFeature_m_isMultipleFeature}

# NumOperandChoices class attributes and methods

# hydraconstraints_SimpleFeature class attributes and methods
hydraconstraints_SimpleFeature_featureName: Property = Property(name="featureName", type=StringType)
hydraconstraints_SimpleFeature_m_isSimpleFeature: Method = Method(name="isSimpleFeature", parameters={Parameter(name='diagnostics'), Parameter(name='context')}, type=BooleanType)
hydraconstraints_SimpleFeature.attributes={hydraconstraints_SimpleFeature_featureName}
hydraconstraints_SimpleFeature.methods={hydraconstraints_SimpleFeature_m_isSimpleFeature}

# BoolOperandChoices class attributes and methods

# hydraconstraints_BoolOperandChoices class attributes and methods

# hydraconstraints_Context class attributes and methods

# hydraconstraints_Selection class attributes and methods

# hydraconstraints_Any class attributes and methods

# Selection class attributes and methods

# hydraconstraints_All class attributes and methods

# hydraconstraints_Number class attributes and methods
hydraconstraints_Number_numValue: Property = Property(name="numValue", type=IntegerType)
hydraconstraints_Number.attributes={hydraconstraints_Number_numValue}

# Relationships
constraints0: BinaryAssociation = BinaryAssociation(
    name="constraints0",
    ends={
        Property(name="hydraconstraints_Constraint", type=hydraconstraints_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="hydraconstraints_Model", type=hydraconstraints_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operators1: BinaryAssociation = BinaryAssociation(
    name="operators1",
    ends={
        Property(name="hydraconstraints_BoolOperand", type=hydraconstraints_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="hydraconstraints_Constraint2", type=hydraconstraints_BoolOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
boolPriorityOp13: BinaryAssociation = BinaryAssociation(
    name="boolPriorityOp13",
    ends={
        Property(name="hydraconstraints_BoolOperand4", type=hydraconstraints_BoolPriorityOperand1, multiplicity=Multiplicity(1, 1)),
        Property(name="hydraconstraints_BoolPriorityOperand1", type=hydraconstraints_BoolOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
boolPriorityOp25: BinaryAssociation = BinaryAssociation(
    name="boolPriorityOp25",
    ends={
        Property(name="hydraconstraints_BoolOperand6", type=hydraconstraints_BoolPriorityOperand2, multiplicity=Multiplicity(1, 1)),
        Property(name="hydraconstraints_BoolPriorityOperand2", type=hydraconstraints_BoolOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
unaryOp7: BinaryAssociation = BinaryAssociation(
    name="unaryOp7",
    ends={
        Property(name="hydraconstraints_BoolPriorityOperand28", type=hydraconstraints_UnaryOp, multiplicity=Multiplicity(1, 1)),
        Property(name="hydraconstraints_UnaryOp", type=hydraconstraints_BoolPriorityOperand2, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
binaryOp19: BinaryAssociation = BinaryAssociation(
    name="binaryOp19",
    ends={
        Property(name="hydraconstraints_BoolPriorityOperand110", type=hydraconstraints_BinaryOp, multiplicity=Multiplicity(1, 1)),
        Property(name="hydraconstraints_BinaryOp", type=hydraconstraints_BoolPriorityOperand1, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
binaryOp211: BinaryAssociation = BinaryAssociation(
    name="binaryOp211",
    ends={
        Property(name="hydraconstraints_BoolPriorityOperand213", type=hydraconstraints_BinaryOp, multiplicity=Multiplicity(1, 1)),
        Property(name="hydraconstraints_BinaryOp12", type=hydraconstraints_BoolPriorityOperand2, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
compOp114: BinaryAssociation = BinaryAssociation(
    name="compOp114",
    ends={
        Property(name="hydraconstraints_NumPriorityOperand2", type=hydraconstraints_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="hydraconstraints_Comparison", type=hydraconstraints_NumPriorityOperand2, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
compOp215: BinaryAssociation = BinaryAssociation(
    name="compOp215",
    ends={
        Property(name="hydraconstraints_NumPriorityOperand217", type=hydraconstraints_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="hydraconstraints_Comparison16", type=hydraconstraints_NumPriorityOperand2, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contextOp129: BinaryAssociation = BinaryAssociation(
    name="contextOp129",
    ends={
        Property(name="hydraconstraints_MultipleFeature", type=hydraconstraints_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="hydraconstraints_Context30", type=hydraconstraints_MultipleFeature, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
numPriorityOp218: BinaryAssociation = BinaryAssociation(
    name="numPriorityOp218",
    ends={
        Property(name="hydraconstraints_NumOperand", type=hydraconstraints_NumPriorityOperand2, multiplicity=Multiplicity(1, 1)),
        Property(name="hydraconstraints_NumPriorityOperand219", type=hydraconstraints_NumOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
numPriorityOp120: BinaryAssociation = BinaryAssociation(
    name="numPriorityOp120",
    ends={
        Property(name="hydraconstraints_NumOperand21", type=hydraconstraints_NumPriorityOperand1, multiplicity=Multiplicity(1, 1)),
        Property(name="hydraconstraints_NumPriorityOperand1", type=hydraconstraints_NumOperand, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
numOp122: BinaryAssociation = BinaryAssociation(
    name="numOp122",
    ends={
        Property(name="hydraconstraints_NumPriorityOperand123", type=hydraconstraints_NumOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="hydraconstraints_NumOperator", type=hydraconstraints_NumPriorityOperand1, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
numOp224: BinaryAssociation = BinaryAssociation(
    name="numOp224",
    ends={
        Property(name="hydraconstraints_NumPriorityOperand226", type=hydraconstraints_NumOperator, multiplicity=Multiplicity(1, 1)),
        Property(name="hydraconstraints_NumOperator25", type=hydraconstraints_NumPriorityOperand2, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
contextOp227: BinaryAssociation = BinaryAssociation(
    name="contextOp227",
    ends={
        Property(name="hydraconstraints_Constraint28", type=hydraconstraints_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="hydraconstraints_Context", type=hydraconstraints_Constraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
selectionOp31: BinaryAssociation = BinaryAssociation(
    name="selectionOp31",
    ends={
        Property(name="hydraconstraints_Context32", type=hydraconstraints_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="hydraconstraints_Selection", type=hydraconstraints_Context, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_hydraconstraints_BoolOperand_Operand = Generalization(general=Operand, specific=hydraconstraints_BoolOperand)
gen_hydraconstraints_LessOrEqual_Comparison = Generalization(general=Comparison, specific=hydraconstraints_LessOrEqual)
gen_hydraconstraints_LogicalOperator_BoolOperand = Generalization(general=BoolOperand, specific=hydraconstraints_LogicalOperator)
gen_hydraconstraints_UnaryOp_LogicalOperator = Generalization(general=LogicalOperator, specific=hydraconstraints_UnaryOp)
gen_hydraconstraints_Neg_UnaryOp = Generalization(general=UnaryOp, specific=hydraconstraints_Neg)
gen_hydraconstraints_BinaryOp_LogicalOperator = Generalization(general=LogicalOperator, specific=hydraconstraints_BinaryOp)
gen_hydraconstraints_And_BinaryOp = Generalization(general=BinaryOp, specific=hydraconstraints_And)
gen_hydraconstraints_Or_BinaryOp = Generalization(general=BinaryOp, specific=hydraconstraints_Or)
gen_hydraconstraints_Implies_BinaryOp = Generalization(general=BinaryOp, specific=hydraconstraints_Implies)
gen_hydraconstraints_Xor_BinaryOp = Generalization(general=BinaryOp, specific=hydraconstraints_Xor)
gen_hydraconstraints_Comparison_LogicalOperator = Generalization(general=LogicalOperator, specific=hydraconstraints_Comparison)
gen_hydraconstraints_More_Comparison = Generalization(general=Comparison, specific=hydraconstraints_More)
gen_hydraconstraints_MoreOrEqual_Comparison = Generalization(general=Comparison, specific=hydraconstraints_MoreOrEqual)
gen_hydraconstraints_NotEqual_Comparison = Generalization(general=Comparison, specific=hydraconstraints_NotEqual)
gen_hydraconstraints_Less_Comparison = Generalization(general=Comparison, specific=hydraconstraints_Less)
gen_hydraconstraints_Equal_Comparison = Generalization(general=Comparison, specific=hydraconstraints_Equal)
gen_hydraconstraints_NumOperand_Operand = Generalization(general=Operand, specific=hydraconstraints_NumOperand)
gen_hydraconstraints_NumOperator_NumOperand = Generalization(general=NumOperand, specific=hydraconstraints_NumOperator)
gen_hydraconstraints_Plus_NumOperator = Generalization(general=NumOperator, specific=hydraconstraints_Plus)
gen_hydraconstraints_Mul_NumOperator = Generalization(general=NumOperator, specific=hydraconstraints_Mul)
gen_hydraconstraints_Minus_NumOperator = Generalization(general=NumOperator, specific=hydraconstraints_Minus)
gen_hydraconstraints_Div_NumOperator = Generalization(general=NumOperator, specific=hydraconstraints_Div)
gen_hydraconstraints_NumOperandChoices_NumOperand = Generalization(general=NumOperand, specific=hydraconstraints_NumOperandChoices)
gen_hydraconstraints_MultipleFeature_NumOperandChoices = Generalization(general=NumOperandChoices, specific=hydraconstraints_MultipleFeature)
gen_hydraconstraints_SimpleFeature_BoolOperandChoices = Generalization(general=BoolOperandChoices, specific=hydraconstraints_SimpleFeature)
gen_hydraconstraints_BoolOperandChoices_BoolOperand = Generalization(general=BoolOperand, specific=hydraconstraints_BoolOperandChoices)
gen_hydraconstraints_Context_BoolOperandChoices = Generalization(general=BoolOperandChoices, specific=hydraconstraints_Context)
gen_hydraconstraints_Context_NumOperandChoices = Generalization(general=NumOperandChoices, specific=hydraconstraints_Context)
gen_hydraconstraints_Selection_BoolOperandChoices = Generalization(general=BoolOperandChoices, specific=hydraconstraints_Selection)
gen_hydraconstraints_Any_Selection = Generalization(general=Selection, specific=hydraconstraints_Any)
gen_hydraconstraints_All_Selection = Generalization(general=Selection, specific=hydraconstraints_All)
gen_hydraconstraints_Number_NumOperandChoices = Generalization(general=NumOperandChoices, specific=hydraconstraints_Number)

# Domain Model
domain_model = DomainModel(
    name="hydraconstraints",
    types={Operand, hydraconstraints_Model, hydraconstraints_Constraint, hydraconstraints_BoolOperand, hydraconstraints_Operand, hydraconstraints_LessOrEqual, hydraconstraints_BoolPriorityOperand1, hydraconstraints_BoolPriorityOperand2, hydraconstraints_LogicalOperator, BoolOperand, hydraconstraints_UnaryOp, LogicalOperator, hydraconstraints_Neg, UnaryOp, hydraconstraints_BinaryOp, hydraconstraints_And, BinaryOp, hydraconstraints_Or, hydraconstraints_Implies, hydraconstraints_Xor, hydraconstraints_Comparison, hydraconstraints_NumPriorityOperand2, hydraconstraints_More, Comparison, hydraconstraints_MoreOrEqual, hydraconstraints_NotEqual, hydraconstraints_Less, hydraconstraints_Equal, hydraconstraints_NumOperand, hydraconstraints_NumPriorityOperand1, hydraconstraints_NumOperator, NumOperand, hydraconstraints_Plus, NumOperator, hydraconstraints_Mul, hydraconstraints_Minus, hydraconstraints_Div, hydraconstraints_NumOperandChoices, hydraconstraints_MultipleFeature, NumOperandChoices, hydraconstraints_SimpleFeature, BoolOperandChoices, hydraconstraints_BoolOperandChoices, hydraconstraints_Context, hydraconstraints_Selection, hydraconstraints_Any, Selection, hydraconstraints_All, hydraconstraints_Number},
    associations={constraints0, operators1, boolPriorityOp13, boolPriorityOp25, unaryOp7, binaryOp19, binaryOp211, compOp114, compOp215, contextOp129, numPriorityOp218, numPriorityOp120, numOp122, numOp224, contextOp227, selectionOp31},
    generalizations={gen_hydraconstraints_BoolOperand_Operand, gen_hydraconstraints_LessOrEqual_Comparison, gen_hydraconstraints_LogicalOperator_BoolOperand, gen_hydraconstraints_UnaryOp_LogicalOperator, gen_hydraconstraints_Neg_UnaryOp, gen_hydraconstraints_BinaryOp_LogicalOperator, gen_hydraconstraints_And_BinaryOp, gen_hydraconstraints_Or_BinaryOp, gen_hydraconstraints_Implies_BinaryOp, gen_hydraconstraints_Xor_BinaryOp, gen_hydraconstraints_Comparison_LogicalOperator, gen_hydraconstraints_More_Comparison, gen_hydraconstraints_MoreOrEqual_Comparison, gen_hydraconstraints_NotEqual_Comparison, gen_hydraconstraints_Less_Comparison, gen_hydraconstraints_Equal_Comparison, gen_hydraconstraints_NumOperand_Operand, gen_hydraconstraints_NumOperator_NumOperand, gen_hydraconstraints_Plus_NumOperator, gen_hydraconstraints_Mul_NumOperator, gen_hydraconstraints_Minus_NumOperator, gen_hydraconstraints_Div_NumOperator, gen_hydraconstraints_NumOperandChoices_NumOperand, gen_hydraconstraints_MultipleFeature_NumOperandChoices, gen_hydraconstraints_SimpleFeature_BoolOperandChoices, gen_hydraconstraints_BoolOperandChoices_BoolOperand, gen_hydraconstraints_Context_BoolOperandChoices, gen_hydraconstraints_Context_NumOperandChoices, gen_hydraconstraints_Selection_BoolOperandChoices, gen_hydraconstraints_Any_Selection, gen_hydraconstraints_All_Selection, gen_hydraconstraints_Number_NumOperandChoices},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)