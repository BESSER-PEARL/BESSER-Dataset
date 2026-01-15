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
ExecutionOrder: Enumeration = Enumeration(
    name="ExecutionOrder",
    literals={
            EnumerationLiteral(name="l2r"),
			EnumerationLiteral(name="r2l"),
			EnumerationLiteral(name="interleaved")
    }
)

# Classes
members_Member = Class(name="members::Member")
kernel_statements_StatementListContainer = Class(name="kernel::statements::StatementListContainer", is_abstract=True)
Statement = Class(name="Statement")
kernel_statements_StatementContainer = Class(name="kernel::statements::StatementContainer", is_abstract=True)
kernel_statements_Condition = Class(name="kernel::statements::Condition")
statements_Statement = Class(name="statements::Statement")
statements_StatementContainer = Class(name="statements::StatementContainer")
statements_Conditional = Class(name="statements::Conditional")
kernel_commons_NamedElement = Class(name="kernel::commons::NamedElement", is_abstract=True)
kernel_statements_Statement = Class(name="kernel::statements::Statement", is_abstract=True)
commons_LabellableElement = Class(name="commons::LabellableElement")
kernel_statements_ProcedureCall = Class(name="kernel::statements::ProcedureCall")
procedures_ProcedureCall = Class(name="procedures::ProcedureCall")
references_ElementReference = Class(name="references::ElementReference")
Argument = Class(name="Argument")
ReturnSite = Class(name="ReturnSite")
kernel_statements_ExpressionStatement = Class(name="kernel::statements::ExpressionStatement")
kernel_statements_WhileLoop = Class(name="kernel::statements::WhileLoop")
kernel_statements_Block = Class(name="kernel::statements::Block")
statements_StatementListContainer = Class(name="statements::StatementListContainer")
kernel_statements_Jump = Class(name="kernel::statements::Jump", is_abstract=True)
LabellableElement = Class(name="LabellableElement")
kernel_statements_Goto = Class(name="kernel::statements::Goto")
Jump = Class(name="Jump")
kernel_statements_NonDeterministicBlock = Class(name="kernel::statements::NonDeterministicBlock")
kernel_statements_ParallelBlock = Class(name="kernel::statements::ParallelBlock")
kernel_statements_Abort = Class(name="kernel::statements::Abort")
kernel_statements_ExceptionHandlerStatement = Class(name="kernel::statements::ExceptionHandlerStatement")
kernel_statements_StatementWithException = Class(name="kernel::statements::StatementWithException")
ExceptionHandlerStatement = Class(name="ExceptionHandlerStatement")
kernel_statements_Conditional = Class(name="kernel::statements::Conditional", is_abstract=True)
Expression = Class(name="Expression")
kernel_expressions_SubExpression = Class(name="kernel::expressions::SubExpression", is_abstract=True)
ElementReference = Class(name="ElementReference")
kernel_expressions_Defines = Class(name="kernel::expressions::Defines")
Definition = Class(name="Definition")
kernel_expressions_Affects = Class(name="kernel::expressions::Affects")
kernel_expressions_Uses = Class(name="kernel::expressions::Uses")
Usage = Class(name="Usage")
kernel_expressions_Definition = Class(name="kernel::expressions::Definition", is_abstract=True)
kernel_expressions_Usage = Class(name="kernel::expressions::Usage", is_abstract=True)
kernel_statements_Skip = Class(name="kernel::statements::Skip")
kernel_statements_Return = Class(name="kernel::statements::Return")
kernel_procedures_Procedure = Class(name="kernel::procedures::Procedure")
procedures_Procedure = Class(name="procedures::Procedure")
references_ReferenceableElement = Class(name="references::ReferenceableElement")
Member = Class(name="Member")
Parameter_ = Class(name="Parameter")
ProcedureCall = Class(name="ProcedureCall")
Start = Class(name="Start")
End = Class(name="End")
kernel_procedures_MainProcedure = Class(name="kernel::procedures::MainProcedure")
kernel_expressions_Expression = Class(name="kernel::expressions::Expression")
SubExpression = Class(name="SubExpression")
kernel_members_Member = Class(name="kernel::members::Member", is_abstract=True)
kernel_dataitems_DataItem = Class(name="kernel::dataitems::DataItem")
kernel_containers_KernelRoot = Class(name="kernel::containers::KernelRoot", is_abstract=True)
kernel_containers_CompilationUnit = Class(name="kernel::containers::CompilationUnit")
KernelRoot = Class(name="KernelRoot")
MainProcedure = Class(name="MainProcedure")
kernel_references_ElementReference = Class(name="kernel::references::ElementReference", is_abstract=True)
ReferenceableElement = Class(name="ReferenceableElement")
commons_Variable = Class(name="commons::Variable")
kernel_parameters_Parameter = Class(name="kernel::parameters::Parameter")
DataItem = Class(name="DataItem")
kernel_references_ReferenceableElement = Class(name="kernel::references::ReferenceableElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
kernel_references_Reference = Class(name="kernel::references::Reference", is_abstract=True)
kernel_references_Argument = Class(name="kernel::references::Argument")

# members_Member class attributes and methods

# kernel_statements_StatementListContainer class attributes and methods

# Statement class attributes and methods

# kernel_statements_StatementContainer class attributes and methods

# kernel_statements_Condition class attributes and methods

# statements_Statement class attributes and methods

# statements_StatementContainer class attributes and methods

# statements_Conditional class attributes and methods

# kernel_commons_NamedElement class attributes and methods
kernel_commons_NamedElement_name: Property = Property(name="name", type=StringType)
kernel_commons_NamedElement.attributes={kernel_commons_NamedElement_name}

# kernel_statements_Statement class attributes and methods

# commons_LabellableElement class attributes and methods

# kernel_statements_ProcedureCall class attributes and methods

# procedures_ProcedureCall class attributes and methods

# references_ElementReference class attributes and methods

# Argument class attributes and methods

# ReturnSite class attributes and methods

# kernel_statements_ExpressionStatement class attributes and methods

# kernel_statements_WhileLoop class attributes and methods

# kernel_statements_Block class attributes and methods

# statements_StatementListContainer class attributes and methods

# kernel_statements_Jump class attributes and methods

# LabellableElement class attributes and methods

# kernel_statements_Goto class attributes and methods

# Jump class attributes and methods

# kernel_statements_NonDeterministicBlock class attributes and methods

# kernel_statements_ParallelBlock class attributes and methods
kernel_statements_ParallelBlock_order: Property = Property(name="order", type=StringType)
kernel_statements_ParallelBlock.attributes={kernel_statements_ParallelBlock_order}

# kernel_statements_Abort class attributes and methods

# kernel_statements_ExceptionHandlerStatement class attributes and methods

# kernel_statements_StatementWithException class attributes and methods

# ExceptionHandlerStatement class attributes and methods

# kernel_statements_Conditional class attributes and methods

# Expression class attributes and methods

# kernel_expressions_SubExpression class attributes and methods

# ElementReference class attributes and methods

# kernel_expressions_Defines class attributes and methods

# Definition class attributes and methods

# kernel_expressions_Affects class attributes and methods

# kernel_expressions_Uses class attributes and methods

# Usage class attributes and methods

# kernel_expressions_Definition class attributes and methods

# kernel_expressions_Usage class attributes and methods

# kernel_statements_Skip class attributes and methods

# kernel_statements_Return class attributes and methods

# kernel_procedures_Procedure class attributes and methods

# procedures_Procedure class attributes and methods

# references_ReferenceableElement class attributes and methods

# Member class attributes and methods

# Parameter class attributes and methods

# ProcedureCall class attributes and methods

# Start class attributes and methods

# End class attributes and methods

# kernel_procedures_MainProcedure class attributes and methods

# kernel_expressions_Expression class attributes and methods
kernel_expressions_Expression_m_getDefinedVariables: Method = Method(name="getDefinedVariables", parameters={}, type=StringType)
kernel_expressions_Expression_m_getUsedVariables: Method = Method(name="getUsedVariables", parameters={}, type=StringType)
kernel_expressions_Expression.methods={kernel_expressions_Expression_m_getUsedVariables, kernel_expressions_Expression_m_getDefinedVariables}

# SubExpression class attributes and methods

# kernel_members_Member class attributes and methods

# kernel_dataitems_DataItem class attributes and methods

# kernel_containers_KernelRoot class attributes and methods

# kernel_containers_CompilationUnit class attributes and methods

# KernelRoot class attributes and methods

# MainProcedure class attributes and methods

# kernel_references_ElementReference class attributes and methods

# ReferenceableElement class attributes and methods

# commons_Variable class attributes and methods

# kernel_parameters_Parameter class attributes and methods
kernel_parameters_Parameter_correspondingArgument: Property = Property(name="correspondingArgument", type=StringType)
kernel_parameters_Parameter_byReference: Property = Property(name="byReference", type=BooleanType)
kernel_parameters_Parameter.attributes={kernel_parameters_Parameter_byReference, kernel_parameters_Parameter_correspondingArgument}

# DataItem class attributes and methods

# kernel_references_ReferenceableElement class attributes and methods

# NamedElement class attributes and methods

# kernel_references_Reference class attributes and methods

# kernel_references_Argument class attributes and methods
kernel_references_Argument_m_getCorrespondingParameter: Method = Method(name="getCorrespondingParameter", parameters={}, type=StringType)
kernel_references_Argument.methods={kernel_references_Argument_m_getCorrespondingParameter}

# Relationships
statements0: BinaryAssociation = BinaryAssociation(
    name="statements0",
    ends={
        Property(name="Statement", type=kernel_statements_StatementListContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="kernel_statements_StatementListContainer", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statement1: BinaryAssociation = BinaryAssociation(
    name="statement1",
    ends={
        Property(name="Statement2", type=kernel_statements_StatementContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="kernel_statements_StatementContainer", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseStatement3: BinaryAssociation = BinaryAssociation(
    name="elseStatement3",
    ends={
        Property(name="Statement4", type=kernel_statements_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="kernel_statements_Condition", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
arguments8: BinaryAssociation = BinaryAssociation(
    name="arguments8",
    ends={
        Property(name="Argument", type=kernel_statements_ProcedureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="kernel_statements_ProcedureCall", type=Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnSite9: BinaryAssociation = BinaryAssociation(
    name="returnSite9",
    ends={
        Property(name="ReturnSite", type=kernel_statements_ProcedureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="kernel_statements_ProcedureCall10", type=ReturnSite, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression11: BinaryAssociation = BinaryAssociation(
    name="expression11",
    ends={
        Property(name="Expression12", type=kernel_statements_ExpressionStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="kernel_statements_ExpressionStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target5: BinaryAssociation = BinaryAssociation(
    name="target5",
    ends={
        Property(name="LabellableElement", type=kernel_statements_Jump, multiplicity=Multiplicity(1, 1)),
        Property(name="kernel_statements_Jump", type=LabellableElement, multiplicity=Multiplicity(1, 1))
    }
)
exceptionStatements6: BinaryAssociation = BinaryAssociation(
    name="exceptionStatements6",
    ends={
        Property(name="ExceptionHandlerStatement", type=kernel_statements_StatementWithException, multiplicity=Multiplicity(1, 1)),
        Property(name="kernel_statements_StatementWithException", type=ExceptionHandlerStatement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
condition7: BinaryAssociation = BinaryAssociation(
    name="condition7",
    ends={
        Property(name="Expression", type=kernel_statements_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="kernel_statements_Conditional", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reaches31: BinaryAssociation = BinaryAssociation(
    name="reaches31",
    ends={
        Property(name="Usage", type=kernel_expressions_Definition, multiplicity=Multiplicity(1, 1)),
        Property(name="kernel_expressions_Definition", type=Usage, multiplicity=Multiplicity(0, 9999))
    }
)
members13: BinaryAssociation = BinaryAssociation(
    name="members13",
    ends={
        Property(name="Member", type=kernel_procedures_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="kernel_procedures_Procedure", type=Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters14: BinaryAssociation = BinaryAssociation(
    name="parameters14",
    ends={
        Property(name="Parameter", type=kernel_procedures_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="kernel_procedures_Procedure15", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
callers16: BinaryAssociation = BinaryAssociation(
    name="callers16",
    ends={
        Property(name="ProcedureCall", type=kernel_procedures_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="kernel_procedures_Procedure17", type=ProcedureCall, multiplicity=Multiplicity(0, 9999))
    }
)
start18: BinaryAssociation = BinaryAssociation(
    name="start18",
    ends={
        Property(name="Start", type=kernel_procedures_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="kernel_procedures_Procedure19", type=Start, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
end20: BinaryAssociation = BinaryAssociation(
    name="end20",
    ends={
        Property(name="End", type=kernel_procedures_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="kernel_procedures_Procedure21", type=End, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
members22: BinaryAssociation = BinaryAssociation(
    name="members22",
    ends={
        Property(name="Member23", type=kernel_procedures_MainProcedure, multiplicity=Multiplicity(1, 1)),
        Property(name="kernel_procedures_MainProcedure", type=Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
start24: BinaryAssociation = BinaryAssociation(
    name="start24",
    ends={
        Property(name="Start26", type=kernel_procedures_MainProcedure, multiplicity=Multiplicity(1, 1)),
        Property(name="kernel_procedures_MainProcedure25", type=Start, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
end27: BinaryAssociation = BinaryAssociation(
    name="end27",
    ends={
        Property(name="End29", type=kernel_procedures_MainProcedure, multiplicity=Multiplicity(1, 1)),
        Property(name="kernel_procedures_MainProcedure28", type=End, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
children30: BinaryAssociation = BinaryAssociation(
    name="children30",
    ends={
        Property(name="SubExpression", type=kernel_expressions_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="kernel_expressions_Expression", type=SubExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
end39: BinaryAssociation = BinaryAssociation(
    name="end39",
    ends={
        Property(name="End41", type=kernel_containers_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="kernel_containers_CompilationUnit40", type=End, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
mainProcedure32: BinaryAssociation = BinaryAssociation(
    name="mainProcedure32",
    ends={
        Property(name="MainProcedure", type=kernel_containers_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="kernel_containers_CompilationUnit", type=MainProcedure, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declarations33: BinaryAssociation = BinaryAssociation(
    name="declarations33",
    ends={
        Property(name="Member35", type=kernel_containers_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="kernel_containers_CompilationUnit34", type=Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
start36: BinaryAssociation = BinaryAssociation(
    name="start36",
    ends={
        Property(name="Start38", type=kernel_containers_CompilationUnit, multiplicity=Multiplicity(1, 1)),
        Property(name="kernel_containers_CompilationUnit37", type=Start, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target42: BinaryAssociation = BinaryAssociation(
    name="target42",
    ends={
        Property(name="ReferenceableElement", type=kernel_references_ElementReference, multiplicity=Multiplicity(1, 1)),
        Property(name="kernel_references_ElementReference", type=ReferenceableElement, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_kernel_statements_Statement_members_Member = Generalization(general=members_Member, specific=kernel_statements_Statement)
gen_kernel_statements_Condition_statements_Statement = Generalization(general=statements_Statement, specific=kernel_statements_Condition)
gen_kernel_statements_Condition_statements_StatementContainer = Generalization(general=statements_StatementContainer, specific=kernel_statements_Condition)
gen_kernel_statements_Condition_statements_Conditional = Generalization(general=statements_Conditional, specific=kernel_statements_Condition)
gen_kernel_statements_Statement_commons_LabellableElement = Generalization(general=commons_LabellableElement, specific=kernel_statements_Statement)
gen_kernel_statements_ProcedureCall_statements_Statement = Generalization(general=statements_Statement, specific=kernel_statements_ProcedureCall)
gen_kernel_statements_ProcedureCall_procedures_ProcedureCall = Generalization(general=procedures_ProcedureCall, specific=kernel_statements_ProcedureCall)
gen_kernel_statements_ProcedureCall_references_ElementReference = Generalization(general=references_ElementReference, specific=kernel_statements_ProcedureCall)
gen_kernel_statements_ExpressionStatement_Statement = Generalization(general=Statement, specific=kernel_statements_ExpressionStatement)
gen_kernel_statements_WhileLoop_statements_Statement = Generalization(general=statements_Statement, specific=kernel_statements_WhileLoop)
gen_kernel_statements_WhileLoop_statements_StatementContainer = Generalization(general=statements_StatementContainer, specific=kernel_statements_WhileLoop)
gen_kernel_statements_WhileLoop_statements_Conditional = Generalization(general=statements_Conditional, specific=kernel_statements_WhileLoop)
gen_kernel_statements_Block_statements_Statement = Generalization(general=statements_Statement, specific=kernel_statements_Block)
gen_kernel_statements_Block_statements_StatementListContainer = Generalization(general=statements_StatementListContainer, specific=kernel_statements_Block)
gen_kernel_statements_Jump_Statement = Generalization(general=Statement, specific=kernel_statements_Jump)
gen_kernel_statements_Goto_Jump = Generalization(general=Jump, specific=kernel_statements_Goto)
gen_kernel_statements_NonDeterministicBlock_statements_Statement = Generalization(general=statements_Statement, specific=kernel_statements_NonDeterministicBlock)
gen_kernel_statements_NonDeterministicBlock_statements_StatementListContainer = Generalization(general=statements_StatementListContainer, specific=kernel_statements_NonDeterministicBlock)
gen_kernel_statements_ParallelBlock_statements_Statement = Generalization(general=statements_Statement, specific=kernel_statements_ParallelBlock)
gen_kernel_statements_ParallelBlock_statements_StatementListContainer = Generalization(general=statements_StatementListContainer, specific=kernel_statements_ParallelBlock)
gen_kernel_statements_Abort_Statement = Generalization(general=Statement, specific=kernel_statements_Abort)
gen_kernel_statements_ExceptionHandlerStatement_commons_LabellableElement = Generalization(general=commons_LabellableElement, specific=kernel_statements_ExceptionHandlerStatement)
gen_kernel_statements_ExceptionHandlerStatement_statements_StatementContainer = Generalization(general=statements_StatementContainer, specific=kernel_statements_ExceptionHandlerStatement)
gen_kernel_statements_StatementWithException_statements_Statement = Generalization(general=statements_Statement, specific=kernel_statements_StatementWithException)
gen_kernel_statements_StatementWithException_statements_StatementContainer = Generalization(general=statements_StatementContainer, specific=kernel_statements_StatementWithException)
gen_kernel_expressions_SubExpression_ElementReference = Generalization(general=ElementReference, specific=kernel_expressions_SubExpression)
gen_kernel_expressions_Defines_Definition = Generalization(general=Definition, specific=kernel_expressions_Defines)
gen_kernel_expressions_Affects_Definition = Generalization(general=Definition, specific=kernel_expressions_Affects)
gen_kernel_expressions_Uses_Usage = Generalization(general=Usage, specific=kernel_expressions_Uses)
gen_kernel_expressions_Definition_SubExpression = Generalization(general=SubExpression, specific=kernel_expressions_Definition)
gen_kernel_expressions_Usage_SubExpression = Generalization(general=SubExpression, specific=kernel_expressions_Usage)
gen_kernel_statements_Skip_Statement = Generalization(general=Statement, specific=kernel_statements_Skip)
gen_kernel_statements_Return_Statement = Generalization(general=Statement, specific=kernel_statements_Return)
gen_kernel_procedures_Procedure_commons_LabellableElement = Generalization(general=commons_LabellableElement, specific=kernel_procedures_Procedure)
gen_kernel_procedures_Procedure_procedures_Procedure = Generalization(general=procedures_Procedure, specific=kernel_procedures_Procedure)
gen_kernel_procedures_Procedure_members_Member = Generalization(general=members_Member, specific=kernel_procedures_Procedure)
gen_kernel_procedures_Procedure_references_ReferenceableElement = Generalization(general=references_ReferenceableElement, specific=kernel_procedures_Procedure)
gen_kernel_procedures_MainProcedure_LabellableElement = Generalization(general=LabellableElement, specific=kernel_procedures_MainProcedure)
gen_kernel_expressions_Expression_LabellableElement = Generalization(general=LabellableElement, specific=kernel_expressions_Expression)
gen_kernel_dataitems_DataItem_references_ReferenceableElement = Generalization(general=references_ReferenceableElement, specific=kernel_dataitems_DataItem)
gen_kernel_containers_KernelRoot_LabellableElement = Generalization(general=LabellableElement, specific=kernel_containers_KernelRoot)
gen_kernel_containers_CompilationUnit_KernelRoot = Generalization(general=KernelRoot, specific=kernel_containers_CompilationUnit)
gen_kernel_dataitems_DataItem_members_Member = Generalization(general=members_Member, specific=kernel_dataitems_DataItem)
gen_kernel_dataitems_DataItem_commons_Variable = Generalization(general=commons_Variable, specific=kernel_dataitems_DataItem)
gen_kernel_parameters_Parameter_DataItem = Generalization(general=DataItem, specific=kernel_parameters_Parameter)
gen_kernel_references_ReferenceableElement_NamedElement = Generalization(general=NamedElement, specific=kernel_references_ReferenceableElement)
gen_kernel_references_Argument_ElementReference = Generalization(general=ElementReference, specific=kernel_references_Argument)

# Domain Model
domain_model = DomainModel(
    name="kernel",
    types={members_Member, kernel_statements_StatementListContainer, Statement, kernel_statements_StatementContainer, kernel_statements_Condition, statements_Statement, statements_StatementContainer, statements_Conditional, kernel_commons_NamedElement, kernel_statements_Statement, commons_LabellableElement, kernel_statements_ProcedureCall, procedures_ProcedureCall, references_ElementReference, Argument, ReturnSite, kernel_statements_ExpressionStatement, kernel_statements_WhileLoop, kernel_statements_Block, statements_StatementListContainer, kernel_statements_Jump, LabellableElement, kernel_statements_Goto, Jump, kernel_statements_NonDeterministicBlock, kernel_statements_ParallelBlock, kernel_statements_Abort, kernel_statements_ExceptionHandlerStatement, kernel_statements_StatementWithException, ExceptionHandlerStatement, kernel_statements_Conditional, Expression, kernel_expressions_SubExpression, ElementReference, kernel_expressions_Defines, Definition, kernel_expressions_Affects, kernel_expressions_Uses, Usage, kernel_expressions_Definition, kernel_expressions_Usage, kernel_statements_Skip, kernel_statements_Return, kernel_procedures_Procedure, procedures_Procedure, references_ReferenceableElement, Member, Parameter_, ProcedureCall, Start, End, kernel_procedures_MainProcedure, kernel_expressions_Expression, SubExpression, kernel_members_Member, kernel_dataitems_DataItem, kernel_containers_KernelRoot, kernel_containers_CompilationUnit, KernelRoot, MainProcedure, kernel_references_ElementReference, ReferenceableElement, commons_Variable, kernel_parameters_Parameter, DataItem, kernel_references_ReferenceableElement, NamedElement, kernel_references_Reference, kernel_references_Argument, ExecutionOrder},
    associations={statements0, statement1, elseStatement3, arguments8, returnSite9, expression11, target5, exceptionStatements6, condition7, reaches31, members13, parameters14, callers16, start18, end20, members22, start24, end27, children30, end39, mainProcedure32, declarations33, start36, target42},
    generalizations={gen_kernel_statements_Statement_members_Member, gen_kernel_statements_Condition_statements_Statement, gen_kernel_statements_Condition_statements_StatementContainer, gen_kernel_statements_Condition_statements_Conditional, gen_kernel_statements_Statement_commons_LabellableElement, gen_kernel_statements_ProcedureCall_statements_Statement, gen_kernel_statements_ProcedureCall_procedures_ProcedureCall, gen_kernel_statements_ProcedureCall_references_ElementReference, gen_kernel_statements_ExpressionStatement_Statement, gen_kernel_statements_WhileLoop_statements_Statement, gen_kernel_statements_WhileLoop_statements_StatementContainer, gen_kernel_statements_WhileLoop_statements_Conditional, gen_kernel_statements_Block_statements_Statement, gen_kernel_statements_Block_statements_StatementListContainer, gen_kernel_statements_Jump_Statement, gen_kernel_statements_Goto_Jump, gen_kernel_statements_NonDeterministicBlock_statements_Statement, gen_kernel_statements_NonDeterministicBlock_statements_StatementListContainer, gen_kernel_statements_ParallelBlock_statements_Statement, gen_kernel_statements_ParallelBlock_statements_StatementListContainer, gen_kernel_statements_Abort_Statement, gen_kernel_statements_ExceptionHandlerStatement_commons_LabellableElement, gen_kernel_statements_ExceptionHandlerStatement_statements_StatementContainer, gen_kernel_statements_StatementWithException_statements_Statement, gen_kernel_statements_StatementWithException_statements_StatementContainer, gen_kernel_expressions_SubExpression_ElementReference, gen_kernel_expressions_Defines_Definition, gen_kernel_expressions_Affects_Definition, gen_kernel_expressions_Uses_Usage, gen_kernel_expressions_Definition_SubExpression, gen_kernel_expressions_Usage_SubExpression, gen_kernel_statements_Skip_Statement, gen_kernel_statements_Return_Statement, gen_kernel_procedures_Procedure_commons_LabellableElement, gen_kernel_procedures_Procedure_procedures_Procedure, gen_kernel_procedures_Procedure_members_Member, gen_kernel_procedures_Procedure_references_ReferenceableElement, gen_kernel_procedures_MainProcedure_LabellableElement, gen_kernel_expressions_Expression_LabellableElement, gen_kernel_dataitems_DataItem_references_ReferenceableElement, gen_kernel_containers_KernelRoot_LabellableElement, gen_kernel_containers_CompilationUnit_KernelRoot, gen_kernel_dataitems_DataItem_members_Member, gen_kernel_dataitems_DataItem_commons_Variable, gen_kernel_parameters_Parameter_DataItem, gen_kernel_references_ReferenceableElement_NamedElement, gen_kernel_references_Argument_ElementReference},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)