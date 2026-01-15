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
SeverityKind: Enumeration = Enumeration(
    name="SeverityKind",
    literals={
            EnumerationLiteral(name="error"),
			EnumerationLiteral(name="warning"),
			EnumerationLiteral(name="fatal")
    }
)

# Classes
imperativeocl_AssertExp = Class(name="imperativeocl::AssertExp")
imperativeocl_AltExp = Class(name="imperativeocl::AltExp")
ImperativeExpression = Class(name="ImperativeExpression")
imperativeocl_ContinueExp = Class(name="imperativeocl::ContinueExp")
LogExp = Class(name="LogExp")
imperativeocl_AssignExp = Class(name="imperativeocl::AssignExp")
imperativeocl_BlockExp = Class(name="imperativeocl::BlockExp")
imperativeocl_BreakExp = Class(name="imperativeocl::BreakExp")
imperativeocl_CatchExp = Class(name="imperativeocl::CatchExp")
imperativeocl_ComputeExp = Class(name="imperativeocl::ComputeExp")
imperativeocl_ListType = Class(name="imperativeocl::ListType")
imperativeocl_LogExp = Class(name="imperativeocl::LogExp")
imperativeocl_DictLiteralExp = Class(name="imperativeocl::DictLiteralExp")
DictLiteralPart = Class(name="DictLiteralPart")
imperativeocl_DictLiteralPart = Class(name="imperativeocl::DictLiteralPart")
imperativeocl_DictionaryType = Class(name="imperativeocl::DictionaryType")
imperativeocl_ForExp = Class(name="imperativeocl::ForExp")
ImperativeLoopExp = Class(name="ImperativeLoopExp")
imperativeocl_ImperativeExpression = Class(name="imperativeocl::ImperativeExpression", is_abstract=True)
imperativeocl_ImperativeIterateExp = Class(name="imperativeocl::ImperativeIterateExp")
imperativeocl_ImperativeLoopExp = Class(name="imperativeocl::ImperativeLoopExp", is_abstract=True)
imperativeocl_InstantiationExp = Class(name="imperativeocl::InstantiationExp")
imperativeocl_OrderedTupleLiteralExp = Class(name="imperativeocl::OrderedTupleLiteralExp")
OrderedTupleLiteralPart = Class(name="OrderedTupleLiteralPart")
imperativeocl_OrderedTupleLiteralPart = Class(name="imperativeocl::OrderedTupleLiteralPart")
imperativeocl_OrderedTupleType = Class(name="imperativeocl::OrderedTupleType")
imperativeocl_RaiseExp = Class(name="imperativeocl::RaiseExp")
imperativeocl_ReturnExp = Class(name="imperativeocl::ReturnExp")
imperativeocl_SwitchExp = Class(name="imperativeocl::SwitchExp")
AltExp = Class(name="AltExp")
imperativeocl_TemplateParameterType = Class(name="imperativeocl::TemplateParameterType")
imperativeocl_TryExp = Class(name="imperativeocl::TryExp")
CatchExp = Class(name="CatchExp")
imperativeocl_Typedef = Class(name="imperativeocl::Typedef")
imperativeocl_UnlinkExp = Class(name="imperativeocl::UnlinkExp")
imperativeocl_UnpackExp = Class(name="imperativeocl::UnpackExp")
imperativeocl_VariableInitExp = Class(name="imperativeocl::VariableInitExp")
imperativeocl_WhileExp = Class(name="imperativeocl::WhileExp")

# imperativeocl_AssertExp class attributes and methods
imperativeocl_AssertExp_severity: Property = Property(name="severity", type=StringType)
imperativeocl_AssertExp.attributes={imperativeocl_AssertExp_severity}

# imperativeocl_AltExp class attributes and methods

# ImperativeExpression class attributes and methods

# imperativeocl_ContinueExp class attributes and methods

# LogExp class attributes and methods

# imperativeocl_AssignExp class attributes and methods
imperativeocl_AssignExp_isReset: Property = Property(name="isReset", type=StringType)
imperativeocl_AssignExp.attributes={imperativeocl_AssignExp_isReset}

# imperativeocl_BlockExp class attributes and methods

# imperativeocl_BreakExp class attributes and methods

# imperativeocl_CatchExp class attributes and methods

# imperativeocl_ComputeExp class attributes and methods

# imperativeocl_ListType class attributes and methods

# imperativeocl_LogExp class attributes and methods

# imperativeocl_DictLiteralExp class attributes and methods

# DictLiteralPart class attributes and methods

# imperativeocl_DictLiteralPart class attributes and methods

# imperativeocl_DictionaryType class attributes and methods

# imperativeocl_ForExp class attributes and methods

# ImperativeLoopExp class attributes and methods

# imperativeocl_ImperativeExpression class attributes and methods

# imperativeocl_ImperativeIterateExp class attributes and methods

# imperativeocl_ImperativeLoopExp class attributes and methods

# imperativeocl_InstantiationExp class attributes and methods

# imperativeocl_OrderedTupleLiteralExp class attributes and methods

# OrderedTupleLiteralPart class attributes and methods

# imperativeocl_OrderedTupleLiteralPart class attributes and methods

# imperativeocl_OrderedTupleType class attributes and methods

# imperativeocl_RaiseExp class attributes and methods

# imperativeocl_ReturnExp class attributes and methods

# imperativeocl_SwitchExp class attributes and methods

# AltExp class attributes and methods

# imperativeocl_TemplateParameterType class attributes and methods
imperativeocl_TemplateParameterType_specification: Property = Property(name="specification", type=StringType)
imperativeocl_TemplateParameterType.attributes={imperativeocl_TemplateParameterType_specification}

# imperativeocl_TryExp class attributes and methods

# CatchExp class attributes and methods

# imperativeocl_Typedef class attributes and methods

# imperativeocl_UnlinkExp class attributes and methods

# imperativeocl_UnpackExp class attributes and methods

# imperativeocl_VariableInitExp class attributes and methods
imperativeocl_VariableInitExp_withResult: Property = Property(name="withResult", type=StringType)
imperativeocl_VariableInitExp.attributes={imperativeocl_VariableInitExp_withResult}

# imperativeocl_WhileExp class attributes and methods

# Relationships
log0: BinaryAssociation = BinaryAssociation(
    name="log0",
    ends={
        Property(name="LogExp", type=imperativeocl_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AssertExp", type=LogExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part1: BinaryAssociation = BinaryAssociation(
    name="part1",
    ends={
        Property(name="DictLiteralPart", type=imperativeocl_DictLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_DictLiteralExp", type=DictLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
part2: BinaryAssociation = BinaryAssociation(
    name="part2",
    ends={
        Property(name="OrderedTupleLiteralPart", type=imperativeocl_OrderedTupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_OrderedTupleLiteralExp", type=OrderedTupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
alternativePart3: BinaryAssociation = BinaryAssociation(
    name="alternativePart3",
    ends={
        Property(name="AltExp", type=imperativeocl_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_SwitchExp", type=AltExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catchClause4: BinaryAssociation = BinaryAssociation(
    name="catchClause4",
    ends={
        Property(name="CatchExp", type=imperativeocl_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_TryExp", type=CatchExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_imperativeocl_AssertExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_AssertExp)
gen_imperativeocl_AltExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_AltExp)
gen_imperativeocl_ContinueExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_ContinueExp)
gen_imperativeocl_AssignExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_AssignExp)
gen_imperativeocl_BlockExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_BlockExp)
gen_imperativeocl_BreakExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_BreakExp)
gen_imperativeocl_CatchExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_CatchExp)
gen_imperativeocl_ComputeExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_ComputeExp)
gen_imperativeocl_ForExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=imperativeocl_ForExp)
gen_imperativeocl_ImperativeIterateExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=imperativeocl_ImperativeIterateExp)
gen_imperativeocl_InstantiationExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_InstantiationExp)
gen_imperativeocl_RaiseExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_RaiseExp)
gen_imperativeocl_ReturnExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_ReturnExp)
gen_imperativeocl_TryExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_TryExp)
gen_imperativeocl_UnlinkExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_UnlinkExp)
gen_imperativeocl_UnpackExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_UnpackExp)
gen_imperativeocl_VariableInitExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_VariableInitExp)
gen_imperativeocl_WhileExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_WhileExp)

# Domain Model
domain_model = DomainModel(
    name="imperativeocl",
    types={imperativeocl_AssertExp, imperativeocl_AltExp, ImperativeExpression, imperativeocl_ContinueExp, LogExp, imperativeocl_AssignExp, imperativeocl_BlockExp, imperativeocl_BreakExp, imperativeocl_CatchExp, imperativeocl_ComputeExp, imperativeocl_ListType, imperativeocl_LogExp, imperativeocl_DictLiteralExp, DictLiteralPart, imperativeocl_DictLiteralPart, imperativeocl_DictionaryType, imperativeocl_ForExp, ImperativeLoopExp, imperativeocl_ImperativeExpression, imperativeocl_ImperativeIterateExp, imperativeocl_ImperativeLoopExp, imperativeocl_InstantiationExp, imperativeocl_OrderedTupleLiteralExp, OrderedTupleLiteralPart, imperativeocl_OrderedTupleLiteralPart, imperativeocl_OrderedTupleType, imperativeocl_RaiseExp, imperativeocl_ReturnExp, imperativeocl_SwitchExp, AltExp, imperativeocl_TemplateParameterType, imperativeocl_TryExp, CatchExp, imperativeocl_Typedef, imperativeocl_UnlinkExp, imperativeocl_UnpackExp, imperativeocl_VariableInitExp, imperativeocl_WhileExp, SeverityKind},
    associations={log0, part1, part2, alternativePart3, catchClause4},
    generalizations={gen_imperativeocl_AssertExp_ImperativeExpression, gen_imperativeocl_AltExp_ImperativeExpression, gen_imperativeocl_ContinueExp_ImperativeExpression, gen_imperativeocl_AssignExp_ImperativeExpression, gen_imperativeocl_BlockExp_ImperativeExpression, gen_imperativeocl_BreakExp_ImperativeExpression, gen_imperativeocl_CatchExp_ImperativeExpression, gen_imperativeocl_ComputeExp_ImperativeExpression, gen_imperativeocl_ForExp_ImperativeLoopExp, gen_imperativeocl_ImperativeIterateExp_ImperativeLoopExp, gen_imperativeocl_InstantiationExp_ImperativeExpression, gen_imperativeocl_RaiseExp_ImperativeExpression, gen_imperativeocl_ReturnExp_ImperativeExpression, gen_imperativeocl_TryExp_ImperativeExpression, gen_imperativeocl_UnlinkExp_ImperativeExpression, gen_imperativeocl_UnpackExp_ImperativeExpression, gen_imperativeocl_VariableInitExp_ImperativeExpression, gen_imperativeocl_WhileExp_ImperativeExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)