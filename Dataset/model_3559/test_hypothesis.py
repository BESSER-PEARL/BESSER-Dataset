import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Output_Reference,
    variables_Symbolic_Variable,
    pous_Function_Return_Value,
    types_Data_Type_Name,
    iec61131_types_Non_Generic_Type_Name,
    interfaces_Simple_Specification_Func,
    types_Non_Generic_Type_Name,
    Numeric_Type_Name,
    iec61131_types_Real_Type_Name,
    iec61131_types_Integer_Type_Name,
    Elementary_Type_Name,
    iec61131_types_Bit_String_Type_Name,
    iec61131_types_Date_Type_Name,
    iec61131_types_Numeric_Type_Name,
    Data_Type_Name,
    iec61131_types_TypeLib,
    Fbd_Network,
    iec61131_sfc_Transition_Condition,
    iec61131_sfc_Steps,
    iec61131_sfc_Transition_Name,
    iec61131_sfc_Action_Time,
    variables_Variable,
    Subscript_List,
    Multi_Element_Variable,
    iec61131_variables_Structured_Variable,
    iec61131_variables_Array_Variable,
    iec61131_sfc_Cond2_Condition,
    Cond2_Condition,
    iec61131_fbd_Fbd_Network,
    Steps,
    iec61131_sfc_Steps2,
    iec61131_sfc_Steps1,
    Transition_Name,
    sfc_Step_Types,
    sfc_Sfc_Elements,
    iec61131_sfc_Step,
    Step_Types,
    iec61131_sfc_Initial_Step,
    Sfc_Elements,
    iec61131_sfc_Transition,
    Initial_Step,
    iec61131_sfc_Timed_Qualifier,
    Action_Time,
    iec61131_sfc_ActionTime2,
    Timed_Qualifier,
    iec61131_sfc_Action_Qualifier,
    iec61131_sfc_Action_Name,
    Step_Name,
    Action_Association,
    iec61131_sfc_Step_Types,
    Action_Qualifier,
    iec61131_sfc_Action_Association,
    iec61131_sfc_Sfc_Elements,
    Action_Name,
    iec61131_sfc_Action,
    Transition_Condition,
    iec61131_sfc_Transition_Cond2,
    iec61131_sfc_Transition_Cond3,
    iec61131_sfc_Transition_Cond1,
    iec61131_sfc_Sfc_Network,
    Sfc_Network,
    iec61131_il_Il_Assign_Out_Operator,
    iec61131_il_Param_Assignment,
    Assignment_Name,
    iec61131_il_Il_Assign_Operator,
    iec61131_il_Param_Instruction,
    iec61131_il_Param_Assignments,
    Il_Assign_Out_Operator,
    iec61131_il_Il_Operand_List,
    iec61131_il_Il_Simple_Operator,
    iec61131_il_Il_Operations,
    Il_Param_List,
    Il_Assign_Operator,
    Param_Assignments,
    iec61131_il_Il_Param_Out_Assignment,
    iec61131_il_Il_Param_Assignment,
    Param_Instruction,
    iec61131_il_Il_Param_Last_Instruction,
    iec61131_il_Il_Param_Instruction,
    iec61131_il_Simple_Instr,
    Simple_Instr,
    iec61131_il_Il_Simple_Instruction,
    iec61131_il_Operands,
    Il_Param_Last_Instruction,
    Il_Param_Instruction,
    iec61131_il_Il_Param_List,
    iec61131_il_Il_Call_Operator,
    iec61131_il_Il_Jump_Operator,
    Il_Operand_List,
    Il_Simple_Operator,
    iec61131_il_Il_Expr_Operator,
    Il_Simple_Operation,
    iec61131_il_Simple_Operation2,
    iec61131_il_Simple_Operation1,
    Il_Instruction,
    Operands,
    iec61131_il_Operand1,
    iec61131_il_Operand2,
    Il_Call_Operator,
    Il_Jump_Operator,
    Simple_Instr_List,
    Il_Operand,
    il_Simple_Instr,
    il_Il_Operations,
    iec61131_il_Il_Formal_Funct_Call,
    iec61131_il_Il_Expression,
    iec61131_il_Il_Simple_Operation,
    iec61131_il_Label,
    Il_Operations,
    iec61131_il_Il_Return_Operator,
    iec61131_il_Il_Fb_Call,
    iec61131_il_Il_Jump_Operation,
    Label,
    iec61131_il_Il_Instruction,
    Il_Simple_Instruction,
    iec61131_il_Simple_Instr_List,
    Unary_Operator,
    Power_Symbol,
    Structured_Variable,
    Array_Variable,
    Function_Name,
    Primary_Expression,
    iec61131_st_Expression_Constant,
    iec61131_st_Expression_Variable_Type,
    iec61131_st_Call_Expression,
    iec61131_st_Expression_EnumValue,
    iec61131_st_Bracket_Expression,
    Add_Operator,
    Xor_Operator,
    iec61131_st_For_List,
    iec61131_st_Control_Variable,
    Statement_List,
    Selection_Statement,
    iec61131_st_If_Statement,
    Not_Operator,
    Variable,
    iec61131_variables_Symbolic_Variable,
    For_List,
    Control_Variable,
    Iteration_Statement,
    iec61131_st_Exit_Statement,
    iec61131_st_While_Statement,
    iec61131_st_Repeat_Statement,
    iec61131_st_For_Statement,
    iec61131_st_Case_List_Element,
    iec61131_st_Case_List,
    Case_List,
    iec61131_st_Case_Element,
    iec61131_st_Else_Statement,
    iec61131_st_Else_If_Statement,
    Case_Element,
    iec61131_st_Case_Statement,
    Else_Statement,
    Else_If_Statement,
    Statement,
    Param_Assignment,
    iec61131_st_Param_Type1,
    iec61131_st_Param_Type2,
    iec61131_il_Param_Assignment2,
    iec61131_il_Il_Operand,
    Subprogram_Control_Statement,
    iec61131_st_Fb_Invocation,
    iec61131_st_Return_Statement,
    iec61131_st_Iteration_Statement,
    iec61131_st_Selection_Statement,
    iec61131_st_Subprogram_Control_Statement,
    Expression_Variable,
    iec61131_st_Assignment_Statement,
    Or_Operator,
    Expression_Types,
    iec61131_st_Xor_Expression,
    iec61131_st_Power_Expression,
    iec61131_st_Unary_Expression,
    iec61131_st_Equ_Expression,
    iec61131_st_And_Expression,
    iec61131_st_Add_Expression,
    iec61131_st_Term_Expression,
    iec61131_st_Comparison,
    iec61131_st_Primary_Expression,
    iec61131_st_Expression,
    iec61131_configurations_Prog_Data_Source,
    iec61131_configurations_Prog_Conf_Element,
    Prog_Conf_Element,
    iec61131_configurations_Fb_Task,
    iec61131_configurations_Prog_Cnxn,
    iec61131_configurations_Prog_Conf_Elements,
    Task_Initialization,
    iec61131_configurations_Priority,
    iec61131_configurations_Interval,
    iec61131_configurations_Single,
    iec61131_configurations_Instance_Specific_Init,
    iec61131_configurations_Data_Sink,
    Prog_Data_Source,
    Data_Sink,
    Prog_Cnxn,
    iec61131_configurations_Prog_Source,
    iec61131_configurations_Prog_Sink,
    Data_Source,
    iec61131_configurations_Program_Output_Reference,
    configurations_Data_Sink,
    iec61131_configurations_Data_Source,
    Instance_Specific_Init,
    iec61131_configurations_Instance_Spec2,
    iec61131_configurations_Instance_Spec1,
    iec61131_configurations_Instance_Specific_Initializations,
    iec61131_types_Byte_String_Type_Name,
    Single_Element_Type_Name,
    iec61131_types_Enumerated_Type_Name,
    iec61131_types_Subrange_Type_Name,
    types_Single_Element_Type_Name,
    types_Derived_Type_Name,
    Derived_Type_Name,
    iec61131_types_Array_Type_Name,
    iec61131_types_String_Type_Name,
    iec61131_types_Single_Element_Type_Name,
    iec61131_types_Duration_Type_Name,
    iec61131_ld_Rung,
    iec61131_types_Simple_Specification,
    iec61131_variables_Subscript_List,
    Input_Reference,
    iec61131_configurations_Task_Initialization,
    iec61131_configurations_Task_Name,
    iec61131_configurations_Program_Name,
    iec61131_configurations_Access_Path,
    iec61131_configurations_Access_Name,
    Access_Path,
    iec61131_configurations_Symbolic_Path,
    iec61131_configurations_Direct_Path,
    iec61131_configurations_Access_Declaration,
    Access_Declaration,
    iec61131_configurations_Access_Declarations,
    Resource_Declaration,
    Access_Declarations,
    Instance_Specific_Initializations,
    Global_Var_Declarations,
    Single_Resource_Declaration,
    Configuration_Name,
    Prog_Conf_Elements,
    Program_Name,
    Single,
    Priority,
    Task_Name,
    iec61131_configurations_Task_Configuration,
    Program_Configuration,
    Task_Configuration,
    iec61131_configurations_Single_Resource_Declaration,
    Resource_Type_Name,
    Resource_Name,
    iec61131_configurations_Resource_Name,
    Simple_Type_Name,
    Single_Element_Type_Declaration,
    iec61131_pous_Subrange_Type_Declaration,
    iec61131_pous_Simple_Type_Declaration,
    Function_Block_Declaration,
    Function_Declaration,
    Program_Declaration,
    iec61131_pous_Library,
    Program_Access_Decl,
    iec61131_pous_Function_Block_Vars,
    iec61131_pous_Function_Vars,
    iec61131_pous_Program_Vars,
    iec61131_pous_Structure_Elements,
    Structure_Elements,
    iec61131_pous_Structure_Element_Declaration,
    Structure_Element_Declaration,
    iec61131_pous_Structure_Specification,
    Enumerated_Spec_Init,
    iec61131_pous_Enumerated_Type_Declaration,
    Subrange_Spec_Init,
    pous_Function_Block_Body,
    pous_Function_Body,
    iec61131_ld_Ladder_Diagram,
    iec61131_fbd_Function_Block_Diagram,
    iec61131_st_Statement_List,
    iec61131_il_Instruction_List,
    iec61131_pous_Other_Language,
    iec61131_pous_Function_Body,
    iec61131_pous_Function_Return_Value,
    pous_Function_Name,
    Function_Body,
    Function_Vars,
    Byte_String_Type_Name,
    iec61131_types_Double_Byte_String_Type_Name,
    iec61131_types_Single_Byte_String_Type_Name,
    String_Type_Name,
    Structure_Specification,
    iec61131_pous_Structure_Declaration,
    iec61131_pous_Type_Declaration,
    Type_Declaration,
    iec61131_pous_Structure_Type_Declaration,
    iec61131_pous_Array_Type_Declaration,
    iec61131_pous_String_Type_Declaration,
    iec61131_pous_Single_Element_Type_Declaration,
    iec61131_pous_Access_Name,
    Symbolic_Variable,
    iec61131_variables_Multi_Element_Variable,
    Access_Name,
    iec61131_pous_Program_Access_Decl,
    iec61131_pous_Function_Block_Body,
    Program_Type_Name,
    Function_Return_Value,
    Derived_Function_Name,
    Function_Block_Vars,
    Derived_Function_Block_Name,
    pous_Function_Block_Type_Name,
    types_Simple_Specification,
    iec61131_types_Generic_Type_Name,
    iec61131_types_Elementary_Type_Name,
    iec61131_types_Simple_Type_Name,
    Blocks,
    iec61131_pous_Derived_Function_Name,
    iec61131_pous_Derived_Function_Block_Name,
    Function_Block_Body,
    iec61131_sfc_Sequential_Function_Chart,
    iec61131_interfaces_Simple_Specification_Func,
    Simple_Specification_Func,
    Var1_Specification_Func,
    iec61131_interfaces_Simple_Spec_Init_Func,
    Simple_Spec_Init,
    iec61131_interfaces_Var_Name_Decl,
    Array_Type_Name,
    iec61131_interfaces_Initial_Element,
    Non_Generic_Type_Name,
    iec61131_types_Derived_Type_Name,
    Global_Var_Decl,
    Library_Element_Declaration,
    iec61131_configurations_Configuration_Declaration,
    iec61131_pous_Data_Type_Declaration,
    iec61131_pous_Program_Declaration,
    iec61131_pous_Function_Declaration,
    iec61131_pous_Function_Block_Declaration,
    iec61131_configurations_Resource_Declaration,
    iec61131_interfaces_Global_Var_Declarations,
    Located_Var_Decl,
    Program_Vars,
    iec61131_pous_Program_Access_Decls,
    iec61131_interfaces_Located_Var_Declarations,
    Subrange_Type_Name,
    Subrange,
    Double_Byte_String_Type_Name,
    Single_Byte_String_Type_Name,
    Byte_String,
    iec61131_interfaces_Double_BString,
    iec61131_interfaces_Single_BString,
    iec61131_interfaces_Range,
    Initialized_Structure,
    Array_Spec_Init,
    Var2_Init_Decl,
    iec61131_interfaces_Var_Init_Decl_Func,
    iec61131_interfaces_Structured_Var_Init_Decl,
    iec61131_interfaces_Array_Var_Init_Decl,
    Enumerated_Value,
    Enumerated_Specification,
    iec61131_interfaces_Enumerated_Specification1,
    iec61131_interfaces_Enumerated_Specification2,
    Signed_Integer,
    Subrange_Specification,
    iec61131_interfaces_Subrange_Specification2,
    iec61131_interfaces_Subrange_Specification1,
    interfaces_Var1_Specification_Func,
    Simple_Specification,
    pous_Structure_Elements,
    interfaces_Located_Var_Spec_Init,
    interfaces_Var1_Specification,
    iec61131_interfaces_Subrange_Spec_Init,
    iec61131_interfaces_Enumerated_Spec_Init,
    iec61131_interfaces_Simple_Spec_Init,
    Assignment_Symbol,
    iec61131_interfaces_Var1_Specification,
    Bool_Type_Name,
    operators_Divide_Operator,
    Multiply_Operator,
    iec61131_operators_Multiply_Symbol,
    operators_Multiply_Operator,
    operators_Add_Operator,
    operators_Arithmetic_Name,
    iec61131_operators_Divide_Name,
    iec61131_operators_Multiply_Name,
    operators_Addition_Operator,
    iec61131_operators_Addition_Symbol,
    iec61131_operators_Addition_Name,
    Comparison_Operator,
    iec61131_operators_LessEqual_Operator,
    iec61131_operators_GreaterEqual_Operator,
    iec61131_operators_Greater_Operator,
    iec61131_operators_Less_Operator,
    Il_Expr_Operator,
    iec61131_operators_Arithmetic_Name,
    iec61131_operators_Comparison_Name,
    operators_Substraction_Operator,
    iec61131_operators_Substraction_Name,
    GreaterEqual_Operator,
    iec61131_operators_GreaterEqual_Symbol,
    operators_GreaterEqual_Operator,
    Greater_Operator,
    iec61131_operators_Greater_Symbol,
    operators_Greater_Operator,
    LessEqual_Operator,
    iec61131_operators_LessEqual_Symbol,
    operators_LessEqual_Operator,
    Less_Operator,
    iec61131_operators_Less_Symbol,
    operators_Less_Operator,
    Unequal_Operator,
    iec61131_operators_Unequal_Symbol,
    operators_Unequal_Operator,
    Equal_Operator,
    iec61131_operators_Equal_Symbol,
    operators_Comparison_Name,
    iec61131_operators_Less_Name,
    iec61131_operators_GreaterEqual_Name,
    iec61131_operators_Greater_Name,
    iec61131_operators_Unequal_Name,
    iec61131_operators_LessEqual_Name,
    operators_Equal_Operator,
    iec61131_operators_Equal_Name,
    And_Operator,
    iec61131_operators_And_Name,
    iec61131_operators_And_Symbol,
    Assignment_Operator,
    iec61131_operators_Assignment_Name,
    iec61131_operators_Assignment_Symbol,
    Power_Operator,
    iec61131_operators_Power_Name,
    iec61131_operators_Power_Symbol,
    Divide_Operator,
    iec61131_operators_Divide_Symbol,
    iec61131_literals_Integer,
    iec61131_literals_BSInteger,
    iec61131_literals_Date_Literal,
    iec61131_literals_Daytime,
    iec61131_literals_Fixed_Point_Literal,
    Double_Byte_Character_Representation,
    operators_Dot_Operator,
    il_Il_Simple_Operator,
    operators_Unary_Operator,
    iec61131_operators_Substraction_Symbol,
    iec61131_operators_Not_Operator,
    il_Il_Expr_Operator,
    iec61131_operators_Modulo_Operator,
    operators_Operator,
    iec61131_operators_Xor_Operator,
    iec61131_operators_Or_Operator,
    iec61131_operators_And_Operator,
    EquUequ_Operator,
    iec61131_operators_Unequal_Operator,
    iec61131_operators_Equal_Operator,
    Dot_Operator,
    iec61131_operators_Divide_Operator,
    iec61131_operators_Multiply_Operator,
    iec61131_operators_Substraction_Operator,
    iec61131_operators_Addition_Operator,
    Operator,
    iec61131_operators_EquUequ_Operator,
    iec61131_operators_Assignment_Operator,
    iec61131_operators_Dot_Operator,
    iec61131_operators_Comparison_Operator,
    iec61131_operators_Power_Operator,
    iec61131_operators_Unary_Operator,
    iec61131_operators_Add_Operator,
    iec61131_operators_Operator,
    iec61131_literals_Double_Byte_Character_Representation,
    Common_Character_Representation,
    iec61131_literals_Single_Byte_Character_Representation,
    iec61131_literals_Common_Character_Representation,
    DT_Type_Name,
    Date_Literal,
    Date_Type_Name,
    iec61131_types_TOD_Type_Name,
    iec61131_types_DT_Type_Name,
    Single_Byte_Character_Representation,
    Character_String,
    iec61131_literals_Double_Byte_Character_String,
    iec61131_literals_Single_Byte_Character_String,
    Milliseconds,
    Seconds,
    Minutes,
    Hours,
    Unsigned_Integer,
    Fixed_Point_Literal,
    iec61131_literals_Fixed_Point,
    iec61131_literals_Interval,
    literals_Fixed_Point_Literal,
    Integer,
    Numeric_Literal,
    iec61131_literals_Integer_Literal,
    Bit_String_Type_Name,
    iec61131_types_Bool_Type_Name,
    BSInteger,
    Constant,
    iec61131_literals_Bit_String_Literal,
    iec61131_literals_Time_Literal,
    iec61131_literals_Character_String,
    iec61131_literals_Numeric_Literal,
    TOD_Type_Name,
    Daytime,
    Time_Literal,
    iec61131_literals_Date_And_Time,
    iec61131_literals_Date,
    iec61131_literals_Time_Of_Day,
    Substraction_Operator,
    Duration_Type_Name,
    Interval,
    iec61131_literals_Days,
    iec61131_literals_Minutes,
    iec61131_literals_Hours,
    iec61131_literals_Milliseconds,
    iec61131_literals_Seconds,
    sfc_Action_Time,
    literals_Time_Literal,
    iec61131_literals_Duration,
    literals_BSInteger,
    interfaces_Range,
    st_Case_List_Element,
    literals_Integer,
    iec61131_literals_Unsigned_Integer,
    iec61131_literals_Hex_Integer,
    iec61131_literals_Octal_Integer,
    iec61131_literals_Binary_Integer,
    iec61131_literals_Signed_Integer,
    il_Il_Operand,
    configurations_Prog_Data_Source,
    configurations_Data_Source,
    iec61131_configurations_Global_Var_Reference,
    iec61131_variables_Direct_Variable,
    iec61131_literals_Constant,
    iec61131_literals_Boolean_Literal,
    Fixed_Point,
    Real_Type_Name,
    iec61131_literals_Real_Literal,
    Integer_Type_Name,
    iec61131_types_Unsigned_Integer_Type_Name,
    iec61131_types_Signed_Integer_Type_Name,
    iec61131_NamedElement,
    iec61131_Commentable,
    NamedElement,
    iec61131_sfc_Step_Name,
    iec61131_variables_Variable_Name,
    Commentable,
    iec61131_configurations_Program_Configuration,
    iec61131_variables_Variable,
    iec61131_st_Statement,
    iec61131_st_Expression_Variable,
    iec61131_st_Param_Assignment,
    iec61131_st_Expression_Types,
    iec61131_Library_Element_Name,
    iec61131_Library_Element_Declaration,
    iec61131_IEC61131,
    iec61131_interfaces_Input_Declaration,
    iec61131_interfaces_Global_Var_Spec,
    iec61131_interfaces_Global_Var_Decl,
    External_Specification,
    Global_Var_Name,
    iec61131_interfaces_External_Declaration,
    iec61131_interfaces_Interface,
    RNV_Declarations,
    iec61131_interfaces_Non_Retentive_Var_Declarations,
    iec61131_interfaces_Retentive_Var_Declarations,
    External_Declaration,
    Other_Var_Declaration,
    iec61131_interfaces_External_Var_Declarations,
    Variable_Name,
    Location,
    iec61131_interfaces_Located_Var_Decl,
    Direct_Variable,
    iec61131_interfaces_Location,
    iec61131_interfaces_Located_Var_Spec_Init,
    iec61131_interfaces_External_Specification,
    iec61131_interfaces_Var_Spec,
    iec61131_interfaces_Incompl_Location,
    Var_Spec,
    iec61131_interfaces_Byte_String,
    Incompl_Location,
    iec61131_interfaces_Incompl_Located_Var_Decl,
    iec61131_interfaces_RNV_Declarations,
    Incompl_Located_Var_Decl,
    iec61131_interfaces_Incompl_Located_Var_Declarations,
    iec61131_interfaces_Var_Declarations,
    Temp_Var_Decl,
    iec61131_interfaces_Temp_Var_Declaration,
    iec61131_interfaces_Temp_Var_Decls,
    Global_Var_Spec,
    iec61131_interfaces_Global_Var_Location,
    iec61131_interfaces_Global_Var_List,
    Library_Element_Name,
    iec61131_pous_Program_Type_Name,
    iec61131_types_Data_Type_Name,
    iec61131_configurations_Configuration_Name,
    iec61131_pous_Function_Name,
    iec61131_configurations_Resource_Type_Name,
    iec61131_interfaces_Global_Var_Name,
    iec61131_interfaces_Specification,
    Specification,
    Array_Initial_Elements,
    iec61131_interfaces_Array_Initial_Elements1,
    iec61131_interfaces_Array_Initial_Elements2,
    iec61131_interfaces_Array_Initialization,
    iec61131_interfaces_Var1_List,
    Double_BString,
    Double_Byte_Character_String,
    Single_BString,
    Single_Byte_Character_String,
    Located_Var_Spec_Init,
    iec61131_interfaces_Double_Byte_String_Spec,
    iec61131_interfaces_Single_Byte_String_Spec,
    Double_Byte_String_Spec,
    Single_Byte_String_Spec,
    String_Var_Declaration,
    iec61131_interfaces_Double_Byte_String_Var_Declaration,
    iec61131_interfaces_Single_Byte_String_Var_Declaration,
    Range,
    Case_List_Element,
    iec61131_interfaces_Subrange,
    iec61131_interfaces_Array_Initial_Elements,
    interfaces_Var_Spec,
    interfaces_External_Specification,
    iec61131_pous_Function_Block_Type_Name,
    iec61131_interfaces_Array_Specification,
    iec61131_types_Structure_Type_Name,
    interfaces_Specification,
    iec61131_interfaces_Enumerated_Specification,
    iec61131_interfaces_Subrange_Specification,
    interfaces_Var2_Init_Decl,
    interfaces_Temp_Var_Decl,
    iec61131_interfaces_String_Var_Declaration,
    Function_Block_Type_Name,
    Structure_Initialization,
    Temp_Var_Declaration,
    iec61131_interfaces_Var1_Declaration,
    iec61131_interfaces_Structured_Var_Declaration,
    iec61131_interfaces_Array_Var_Declaration,
    iec61131_interfaces_Fb_Name_Decl,
    Enumerated_Type_Name,
    iec61131_interfaces_Enumerated_Value,
    iec61131_interfaces_Structure_Element_Name,
    Initial_Element,
    iec61131_interfaces_InitElement_Constant,
    iec61131_interfaces_InitElement_Array,
    iec61131_interfaces_InitElement_EnumValue,
    iec61131_interfaces_InitElement_Structure,
    Structure_Element_Name,
    iec61131_interfaces_Structure_Element_Initialization,
    Structure_Element_Initialization,
    iec61131_interfaces_Structure_Initialization,
    iec61131_interfaces_Var_Declaration,
    Structure_Type_Name,
    pous_Structure_Specification,
    iec61131_interfaces_Initialized_Structure,
    Array_Specification,
    iec61131_interfaces_Array_Specification1,
    iec61131_interfaces_Array_Specification2,
    Array_Initialization,
    iec61131_interfaces_Array_Spec_Init,
    Var_Declaration,
    iec61131_interfaces_Temp_Var_Decl,
    Var1_Specification,
    iec61131_interfaces_Var1_Specification_Func,
    Var_Init_Decl,
    iec61131_interfaces_Var2_Init_Decl,
    iec61131_interfaces_Var1_Init_Decl,
    Var1_List,
    Input_Declaration,
    iec61131_interfaces_Var_Init_Decl,
    iec61131_interfaces_Edge_Declaration,
    Io_Var_Declaration,
    iec61131_interfaces_Input_Output_Declarations,
    iec61131_interfaces_Output_Declarations,
    iec61131_interfaces_Input_Declarations,
    pous_Function_Vars,
    pous_Program_Vars,
    pous_Function_Block_Vars,
    interfaces_Interface,
    iec61131_interfaces_Function_Var_Decl,
    iec61131_interfaces_Io_Var_Declaration,
    iec61131_interfaces_Other_Var_Declaration,
    Edge,
    Direction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_output_reference_is_not_abstract():
    assert not inspect.isabstract(Output_Reference)


def test_output_reference_constructor_exists():
    assert callable(Output_Reference.__init__)


def test_output_reference_constructor_args():
    sig = inspect.signature(Output_Reference.__init__)
    params = list(sig.parameters.keys())



def test_variables_symbolic_variable_is_not_abstract():
    assert not inspect.isabstract(variables_Symbolic_Variable)


def test_variables_symbolic_variable_constructor_exists():
    assert callable(variables_Symbolic_Variable.__init__)


def test_variables_symbolic_variable_constructor_args():
    sig = inspect.signature(variables_Symbolic_Variable.__init__)
    params = list(sig.parameters.keys())



def test_pous_function_return_value_is_not_abstract():
    assert not inspect.isabstract(pous_Function_Return_Value)


def test_pous_function_return_value_constructor_exists():
    assert callable(pous_Function_Return_Value.__init__)


def test_pous_function_return_value_constructor_args():
    sig = inspect.signature(pous_Function_Return_Value.__init__)
    params = list(sig.parameters.keys())



def test_types_data_type_name_is_not_abstract():
    assert not inspect.isabstract(types_Data_Type_Name)


def test_types_data_type_name_constructor_exists():
    assert callable(types_Data_Type_Name.__init__)


def test_types_data_type_name_constructor_args():
    sig = inspect.signature(types_Data_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_non_generic_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_Non_Generic_Type_Name)


def test_iec61131_types_non_generic_type_name_constructor_exists():
    assert callable(iec61131_types_Non_Generic_Type_Name.__init__)


def test_iec61131_types_non_generic_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_Non_Generic_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_interfaces_simple_specification_func_is_not_abstract():
    assert not inspect.isabstract(interfaces_Simple_Specification_Func)


def test_interfaces_simple_specification_func_constructor_exists():
    assert callable(interfaces_Simple_Specification_Func.__init__)


def test_interfaces_simple_specification_func_constructor_args():
    sig = inspect.signature(interfaces_Simple_Specification_Func.__init__)
    params = list(sig.parameters.keys())



def test_types_non_generic_type_name_is_not_abstract():
    assert not inspect.isabstract(types_Non_Generic_Type_Name)


def test_types_non_generic_type_name_constructor_exists():
    assert callable(types_Non_Generic_Type_Name.__init__)


def test_types_non_generic_type_name_constructor_args():
    sig = inspect.signature(types_Non_Generic_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_numeric_type_name_is_not_abstract():
    assert not inspect.isabstract(Numeric_Type_Name)


def test_numeric_type_name_constructor_exists():
    assert callable(Numeric_Type_Name.__init__)


def test_numeric_type_name_constructor_args():
    sig = inspect.signature(Numeric_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_real_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_Real_Type_Name)


def test_iec61131_types_real_type_name_constructor_exists():
    assert callable(iec61131_types_Real_Type_Name.__init__)


def test_iec61131_types_real_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_Real_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_integer_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_Integer_Type_Name)


def test_iec61131_types_integer_type_name_constructor_exists():
    assert callable(iec61131_types_Integer_Type_Name.__init__)


def test_iec61131_types_integer_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_Integer_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_elementary_type_name_is_not_abstract():
    assert not inspect.isabstract(Elementary_Type_Name)


def test_elementary_type_name_constructor_exists():
    assert callable(Elementary_Type_Name.__init__)


def test_elementary_type_name_constructor_args():
    sig = inspect.signature(Elementary_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_bit_string_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_Bit_String_Type_Name)


def test_iec61131_types_bit_string_type_name_constructor_exists():
    assert callable(iec61131_types_Bit_String_Type_Name.__init__)


def test_iec61131_types_bit_string_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_Bit_String_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_date_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_Date_Type_Name)


def test_iec61131_types_date_type_name_constructor_exists():
    assert callable(iec61131_types_Date_Type_Name.__init__)


def test_iec61131_types_date_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_Date_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_numeric_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_Numeric_Type_Name)


def test_iec61131_types_numeric_type_name_constructor_exists():
    assert callable(iec61131_types_Numeric_Type_Name.__init__)


def test_iec61131_types_numeric_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_Numeric_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_data_type_name_is_not_abstract():
    assert not inspect.isabstract(Data_Type_Name)


def test_data_type_name_constructor_exists():
    assert callable(Data_Type_Name.__init__)


def test_data_type_name_constructor_args():
    sig = inspect.signature(Data_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_typelib_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_TypeLib)


def test_iec61131_types_typelib_constructor_exists():
    assert callable(iec61131_types_TypeLib.__init__)


def test_iec61131_types_typelib_constructor_args():
    sig = inspect.signature(iec61131_types_TypeLib.__init__)
    params = list(sig.parameters.keys())



def test_fbd_network_is_not_abstract():
    assert not inspect.isabstract(Fbd_Network)


def test_fbd_network_constructor_exists():
    assert callable(Fbd_Network.__init__)


def test_fbd_network_constructor_args():
    sig = inspect.signature(Fbd_Network.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_sfc_transition_condition_is_not_abstract():
    assert not inspect.isabstract(iec61131_sfc_Transition_Condition)


def test_iec61131_sfc_transition_condition_constructor_exists():
    assert callable(iec61131_sfc_Transition_Condition.__init__)


def test_iec61131_sfc_transition_condition_constructor_args():
    sig = inspect.signature(iec61131_sfc_Transition_Condition.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_sfc_steps_is_not_abstract():
    assert not inspect.isabstract(iec61131_sfc_Steps)


def test_iec61131_sfc_steps_constructor_exists():
    assert callable(iec61131_sfc_Steps.__init__)


def test_iec61131_sfc_steps_constructor_args():
    sig = inspect.signature(iec61131_sfc_Steps.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_sfc_transition_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_sfc_Transition_Name)


def test_iec61131_sfc_transition_name_constructor_exists():
    assert callable(iec61131_sfc_Transition_Name.__init__)


def test_iec61131_sfc_transition_name_constructor_args():
    sig = inspect.signature(iec61131_sfc_Transition_Name.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iec61131_sfc_transition_name_has_name():
    assert hasattr(iec61131_sfc_Transition_Name, "name")
    descriptor = None
    for klass in iec61131_sfc_Transition_Name.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iec61131_sfc_action_time_is_not_abstract():
    assert not inspect.isabstract(iec61131_sfc_Action_Time)


def test_iec61131_sfc_action_time_constructor_exists():
    assert callable(iec61131_sfc_Action_Time.__init__)


def test_iec61131_sfc_action_time_constructor_args():
    sig = inspect.signature(iec61131_sfc_Action_Time.__init__)
    params = list(sig.parameters.keys())



def test_variables_variable_is_not_abstract():
    assert not inspect.isabstract(variables_Variable)


def test_variables_variable_constructor_exists():
    assert callable(variables_Variable.__init__)


def test_variables_variable_constructor_args():
    sig = inspect.signature(variables_Variable.__init__)
    params = list(sig.parameters.keys())



def test_subscript_list_is_not_abstract():
    assert not inspect.isabstract(Subscript_List)


def test_subscript_list_constructor_exists():
    assert callable(Subscript_List.__init__)


def test_subscript_list_constructor_args():
    sig = inspect.signature(Subscript_List.__init__)
    params = list(sig.parameters.keys())



def test_multi_element_variable_is_not_abstract():
    assert not inspect.isabstract(Multi_Element_Variable)


def test_multi_element_variable_constructor_exists():
    assert callable(Multi_Element_Variable.__init__)


def test_multi_element_variable_constructor_args():
    sig = inspect.signature(Multi_Element_Variable.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_variables_structured_variable_is_not_abstract():
    assert not inspect.isabstract(iec61131_variables_Structured_Variable)


def test_iec61131_variables_structured_variable_constructor_exists():
    assert callable(iec61131_variables_Structured_Variable.__init__)


def test_iec61131_variables_structured_variable_constructor_args():
    sig = inspect.signature(iec61131_variables_Structured_Variable.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_variables_array_variable_is_not_abstract():
    assert not inspect.isabstract(iec61131_variables_Array_Variable)


def test_iec61131_variables_array_variable_constructor_exists():
    assert callable(iec61131_variables_Array_Variable.__init__)


def test_iec61131_variables_array_variable_constructor_args():
    sig = inspect.signature(iec61131_variables_Array_Variable.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_sfc_cond2_condition_is_not_abstract():
    assert not inspect.isabstract(iec61131_sfc_Cond2_Condition)


def test_iec61131_sfc_cond2_condition_constructor_exists():
    assert callable(iec61131_sfc_Cond2_Condition.__init__)


def test_iec61131_sfc_cond2_condition_constructor_args():
    sig = inspect.signature(iec61131_sfc_Cond2_Condition.__init__)
    params = list(sig.parameters.keys())



def test_cond2_condition_is_not_abstract():
    assert not inspect.isabstract(Cond2_Condition)


def test_cond2_condition_constructor_exists():
    assert callable(Cond2_Condition.__init__)


def test_cond2_condition_constructor_args():
    sig = inspect.signature(Cond2_Condition.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_fbd_fbd_network_is_not_abstract():
    assert not inspect.isabstract(iec61131_fbd_Fbd_Network)


def test_iec61131_fbd_fbd_network_constructor_exists():
    assert callable(iec61131_fbd_Fbd_Network.__init__)


def test_iec61131_fbd_fbd_network_constructor_args():
    sig = inspect.signature(iec61131_fbd_Fbd_Network.__init__)
    params = list(sig.parameters.keys())



def test_steps_is_not_abstract():
    assert not inspect.isabstract(Steps)


def test_steps_constructor_exists():
    assert callable(Steps.__init__)


def test_steps_constructor_args():
    sig = inspect.signature(Steps.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_sfc_steps2_is_not_abstract():
    assert not inspect.isabstract(iec61131_sfc_Steps2)


def test_iec61131_sfc_steps2_constructor_exists():
    assert callable(iec61131_sfc_Steps2.__init__)


def test_iec61131_sfc_steps2_constructor_args():
    sig = inspect.signature(iec61131_sfc_Steps2.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_sfc_steps1_is_not_abstract():
    assert not inspect.isabstract(iec61131_sfc_Steps1)


def test_iec61131_sfc_steps1_constructor_exists():
    assert callable(iec61131_sfc_Steps1.__init__)


def test_iec61131_sfc_steps1_constructor_args():
    sig = inspect.signature(iec61131_sfc_Steps1.__init__)
    params = list(sig.parameters.keys())



def test_transition_name_is_not_abstract():
    assert not inspect.isabstract(Transition_Name)


def test_transition_name_constructor_exists():
    assert callable(Transition_Name.__init__)


def test_transition_name_constructor_args():
    sig = inspect.signature(Transition_Name.__init__)
    params = list(sig.parameters.keys())



def test_sfc_step_types_is_not_abstract():
    assert not inspect.isabstract(sfc_Step_Types)


def test_sfc_step_types_constructor_exists():
    assert callable(sfc_Step_Types.__init__)


def test_sfc_step_types_constructor_args():
    sig = inspect.signature(sfc_Step_Types.__init__)
    params = list(sig.parameters.keys())



def test_sfc_sfc_elements_is_not_abstract():
    assert not inspect.isabstract(sfc_Sfc_Elements)


def test_sfc_sfc_elements_constructor_exists():
    assert callable(sfc_Sfc_Elements.__init__)


def test_sfc_sfc_elements_constructor_args():
    sig = inspect.signature(sfc_Sfc_Elements.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_sfc_step_is_not_abstract():
    assert not inspect.isabstract(iec61131_sfc_Step)


def test_iec61131_sfc_step_constructor_exists():
    assert callable(iec61131_sfc_Step.__init__)


def test_iec61131_sfc_step_constructor_args():
    sig = inspect.signature(iec61131_sfc_Step.__init__)
    params = list(sig.parameters.keys())



def test_step_types_is_not_abstract():
    assert not inspect.isabstract(Step_Types)


def test_step_types_constructor_exists():
    assert callable(Step_Types.__init__)


def test_step_types_constructor_args():
    sig = inspect.signature(Step_Types.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_sfc_initial_step_is_not_abstract():
    assert not inspect.isabstract(iec61131_sfc_Initial_Step)


def test_iec61131_sfc_initial_step_constructor_exists():
    assert callable(iec61131_sfc_Initial_Step.__init__)


def test_iec61131_sfc_initial_step_constructor_args():
    sig = inspect.signature(iec61131_sfc_Initial_Step.__init__)
    params = list(sig.parameters.keys())



def test_sfc_elements_is_not_abstract():
    assert not inspect.isabstract(Sfc_Elements)


def test_sfc_elements_constructor_exists():
    assert callable(Sfc_Elements.__init__)


def test_sfc_elements_constructor_args():
    sig = inspect.signature(Sfc_Elements.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_sfc_transition_is_not_abstract():
    assert not inspect.isabstract(iec61131_sfc_Transition)


def test_iec61131_sfc_transition_constructor_exists():
    assert callable(iec61131_sfc_Transition.__init__)


def test_iec61131_sfc_transition_constructor_args():
    sig = inspect.signature(iec61131_sfc_Transition.__init__)
    params = list(sig.parameters.keys())



def test_initial_step_is_not_abstract():
    assert not inspect.isabstract(Initial_Step)


def test_initial_step_constructor_exists():
    assert callable(Initial_Step.__init__)


def test_initial_step_constructor_args():
    sig = inspect.signature(Initial_Step.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_sfc_timed_qualifier_is_not_abstract():
    assert not inspect.isabstract(iec61131_sfc_Timed_Qualifier)


def test_iec61131_sfc_timed_qualifier_constructor_exists():
    assert callable(iec61131_sfc_Timed_Qualifier.__init__)


def test_iec61131_sfc_timed_qualifier_constructor_args():
    sig = inspect.signature(iec61131_sfc_Timed_Qualifier.__init__)
    params = list(sig.parameters.keys())
    assert "qualifier" in params, "Missing parameter 'qualifier'"

def test_iec61131_sfc_timed_qualifier_has_qualifier():
    assert hasattr(iec61131_sfc_Timed_Qualifier, "qualifier")
    descriptor = None
    for klass in iec61131_sfc_Timed_Qualifier.__mro__:
        if "qualifier" in klass.__dict__:
            descriptor = klass.__dict__["qualifier"]
            break
    assert isinstance(descriptor, property)



def test_action_time_is_not_abstract():
    assert not inspect.isabstract(Action_Time)


def test_action_time_constructor_exists():
    assert callable(Action_Time.__init__)


def test_action_time_constructor_args():
    sig = inspect.signature(Action_Time.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_sfc_actiontime2_is_not_abstract():
    assert not inspect.isabstract(iec61131_sfc_ActionTime2)


def test_iec61131_sfc_actiontime2_constructor_exists():
    assert callable(iec61131_sfc_ActionTime2.__init__)


def test_iec61131_sfc_actiontime2_constructor_args():
    sig = inspect.signature(iec61131_sfc_ActionTime2.__init__)
    params = list(sig.parameters.keys())



def test_timed_qualifier_is_not_abstract():
    assert not inspect.isabstract(Timed_Qualifier)


def test_timed_qualifier_constructor_exists():
    assert callable(Timed_Qualifier.__init__)


def test_timed_qualifier_constructor_args():
    sig = inspect.signature(Timed_Qualifier.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_sfc_action_qualifier_is_not_abstract():
    assert not inspect.isabstract(iec61131_sfc_Action_Qualifier)


def test_iec61131_sfc_action_qualifier_constructor_exists():
    assert callable(iec61131_sfc_Action_Qualifier.__init__)


def test_iec61131_sfc_action_qualifier_constructor_args():
    sig = inspect.signature(iec61131_sfc_Action_Qualifier.__init__)
    params = list(sig.parameters.keys())
    assert "qualifier" in params, "Missing parameter 'qualifier'"

def test_iec61131_sfc_action_qualifier_has_qualifier():
    assert hasattr(iec61131_sfc_Action_Qualifier, "qualifier")
    descriptor = None
    for klass in iec61131_sfc_Action_Qualifier.__mro__:
        if "qualifier" in klass.__dict__:
            descriptor = klass.__dict__["qualifier"]
            break
    assert isinstance(descriptor, property)



def test_iec61131_sfc_action_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_sfc_Action_Name)


def test_iec61131_sfc_action_name_constructor_exists():
    assert callable(iec61131_sfc_Action_Name.__init__)


def test_iec61131_sfc_action_name_constructor_args():
    sig = inspect.signature(iec61131_sfc_Action_Name.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iec61131_sfc_action_name_has_name():
    assert hasattr(iec61131_sfc_Action_Name, "name")
    descriptor = None
    for klass in iec61131_sfc_Action_Name.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_step_name_is_not_abstract():
    assert not inspect.isabstract(Step_Name)


def test_step_name_constructor_exists():
    assert callable(Step_Name.__init__)


def test_step_name_constructor_args():
    sig = inspect.signature(Step_Name.__init__)
    params = list(sig.parameters.keys())



def test_action_association_is_not_abstract():
    assert not inspect.isabstract(Action_Association)


def test_action_association_constructor_exists():
    assert callable(Action_Association.__init__)


def test_action_association_constructor_args():
    sig = inspect.signature(Action_Association.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_sfc_step_types_is_not_abstract():
    assert not inspect.isabstract(iec61131_sfc_Step_Types)


def test_iec61131_sfc_step_types_constructor_exists():
    assert callable(iec61131_sfc_Step_Types.__init__)


def test_iec61131_sfc_step_types_constructor_args():
    sig = inspect.signature(iec61131_sfc_Step_Types.__init__)
    params = list(sig.parameters.keys())



def test_action_qualifier_is_not_abstract():
    assert not inspect.isabstract(Action_Qualifier)


def test_action_qualifier_constructor_exists():
    assert callable(Action_Qualifier.__init__)


def test_action_qualifier_constructor_args():
    sig = inspect.signature(Action_Qualifier.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_sfc_action_association_is_not_abstract():
    assert not inspect.isabstract(iec61131_sfc_Action_Association)


def test_iec61131_sfc_action_association_constructor_exists():
    assert callable(iec61131_sfc_Action_Association.__init__)


def test_iec61131_sfc_action_association_constructor_args():
    sig = inspect.signature(iec61131_sfc_Action_Association.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_sfc_sfc_elements_is_not_abstract():
    assert not inspect.isabstract(iec61131_sfc_Sfc_Elements)


def test_iec61131_sfc_sfc_elements_constructor_exists():
    assert callable(iec61131_sfc_Sfc_Elements.__init__)


def test_iec61131_sfc_sfc_elements_constructor_args():
    sig = inspect.signature(iec61131_sfc_Sfc_Elements.__init__)
    params = list(sig.parameters.keys())



def test_action_name_is_not_abstract():
    assert not inspect.isabstract(Action_Name)


def test_action_name_constructor_exists():
    assert callable(Action_Name.__init__)


def test_action_name_constructor_args():
    sig = inspect.signature(Action_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_sfc_action_is_not_abstract():
    assert not inspect.isabstract(iec61131_sfc_Action)


def test_iec61131_sfc_action_constructor_exists():
    assert callable(iec61131_sfc_Action.__init__)


def test_iec61131_sfc_action_constructor_args():
    sig = inspect.signature(iec61131_sfc_Action.__init__)
    params = list(sig.parameters.keys())



def test_transition_condition_is_not_abstract():
    assert not inspect.isabstract(Transition_Condition)


def test_transition_condition_constructor_exists():
    assert callable(Transition_Condition.__init__)


def test_transition_condition_constructor_args():
    sig = inspect.signature(Transition_Condition.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_sfc_transition_cond2_is_not_abstract():
    assert not inspect.isabstract(iec61131_sfc_Transition_Cond2)


def test_iec61131_sfc_transition_cond2_constructor_exists():
    assert callable(iec61131_sfc_Transition_Cond2.__init__)


def test_iec61131_sfc_transition_cond2_constructor_args():
    sig = inspect.signature(iec61131_sfc_Transition_Cond2.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_sfc_transition_cond3_is_not_abstract():
    assert not inspect.isabstract(iec61131_sfc_Transition_Cond3)


def test_iec61131_sfc_transition_cond3_constructor_exists():
    assert callable(iec61131_sfc_Transition_Cond3.__init__)


def test_iec61131_sfc_transition_cond3_constructor_args():
    sig = inspect.signature(iec61131_sfc_Transition_Cond3.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_sfc_transition_cond1_is_not_abstract():
    assert not inspect.isabstract(iec61131_sfc_Transition_Cond1)


def test_iec61131_sfc_transition_cond1_constructor_exists():
    assert callable(iec61131_sfc_Transition_Cond1.__init__)


def test_iec61131_sfc_transition_cond1_constructor_args():
    sig = inspect.signature(iec61131_sfc_Transition_Cond1.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_sfc_sfc_network_is_not_abstract():
    assert not inspect.isabstract(iec61131_sfc_Sfc_Network)


def test_iec61131_sfc_sfc_network_constructor_exists():
    assert callable(iec61131_sfc_Sfc_Network.__init__)


def test_iec61131_sfc_sfc_network_constructor_args():
    sig = inspect.signature(iec61131_sfc_Sfc_Network.__init__)
    params = list(sig.parameters.keys())



def test_sfc_network_is_not_abstract():
    assert not inspect.isabstract(Sfc_Network)


def test_sfc_network_constructor_exists():
    assert callable(Sfc_Network.__init__)


def test_sfc_network_constructor_args():
    sig = inspect.signature(Sfc_Network.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_il_assign_out_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Il_Assign_Out_Operator)


def test_iec61131_il_il_assign_out_operator_constructor_exists():
    assert callable(iec61131_il_Il_Assign_Out_Operator.__init__)


def test_iec61131_il_il_assign_out_operator_constructor_args():
    sig = inspect.signature(iec61131_il_Il_Assign_Out_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_param_assignment_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Param_Assignment)


def test_iec61131_il_param_assignment_constructor_exists():
    assert callable(iec61131_il_Param_Assignment.__init__)


def test_iec61131_il_param_assignment_constructor_args():
    sig = inspect.signature(iec61131_il_Param_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_assignment_name_is_not_abstract():
    assert not inspect.isabstract(Assignment_Name)


def test_assignment_name_constructor_exists():
    assert callable(Assignment_Name.__init__)


def test_assignment_name_constructor_args():
    sig = inspect.signature(Assignment_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_il_assign_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Il_Assign_Operator)


def test_iec61131_il_il_assign_operator_constructor_exists():
    assert callable(iec61131_il_Il_Assign_Operator.__init__)


def test_iec61131_il_il_assign_operator_constructor_args():
    sig = inspect.signature(iec61131_il_Il_Assign_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_param_instruction_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Param_Instruction)


def test_iec61131_il_param_instruction_constructor_exists():
    assert callable(iec61131_il_Param_Instruction.__init__)


def test_iec61131_il_param_instruction_constructor_args():
    sig = inspect.signature(iec61131_il_Param_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_param_assignments_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Param_Assignments)


def test_iec61131_il_param_assignments_constructor_exists():
    assert callable(iec61131_il_Param_Assignments.__init__)


def test_iec61131_il_param_assignments_constructor_args():
    sig = inspect.signature(iec61131_il_Param_Assignments.__init__)
    params = list(sig.parameters.keys())



def test_il_assign_out_operator_is_not_abstract():
    assert not inspect.isabstract(Il_Assign_Out_Operator)


def test_il_assign_out_operator_constructor_exists():
    assert callable(Il_Assign_Out_Operator.__init__)


def test_il_assign_out_operator_constructor_args():
    sig = inspect.signature(Il_Assign_Out_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_il_operand_list_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Il_Operand_List)


def test_iec61131_il_il_operand_list_constructor_exists():
    assert callable(iec61131_il_Il_Operand_List.__init__)


def test_iec61131_il_il_operand_list_constructor_args():
    sig = inspect.signature(iec61131_il_Il_Operand_List.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_il_simple_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Il_Simple_Operator)


def test_iec61131_il_il_simple_operator_constructor_exists():
    assert callable(iec61131_il_Il_Simple_Operator.__init__)


def test_iec61131_il_il_simple_operator_constructor_args():
    sig = inspect.signature(iec61131_il_Il_Simple_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_il_operations_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Il_Operations)


def test_iec61131_il_il_operations_constructor_exists():
    assert callable(iec61131_il_Il_Operations.__init__)


def test_iec61131_il_il_operations_constructor_args():
    sig = inspect.signature(iec61131_il_Il_Operations.__init__)
    params = list(sig.parameters.keys())



def test_il_param_list_is_not_abstract():
    assert not inspect.isabstract(Il_Param_List)


def test_il_param_list_constructor_exists():
    assert callable(Il_Param_List.__init__)


def test_il_param_list_constructor_args():
    sig = inspect.signature(Il_Param_List.__init__)
    params = list(sig.parameters.keys())



def test_il_assign_operator_is_not_abstract():
    assert not inspect.isabstract(Il_Assign_Operator)


def test_il_assign_operator_constructor_exists():
    assert callable(Il_Assign_Operator.__init__)


def test_il_assign_operator_constructor_args():
    sig = inspect.signature(Il_Assign_Operator.__init__)
    params = list(sig.parameters.keys())



def test_param_assignments_is_not_abstract():
    assert not inspect.isabstract(Param_Assignments)


def test_param_assignments_constructor_exists():
    assert callable(Param_Assignments.__init__)


def test_param_assignments_constructor_args():
    sig = inspect.signature(Param_Assignments.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_il_param_out_assignment_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Il_Param_Out_Assignment)


def test_iec61131_il_il_param_out_assignment_constructor_exists():
    assert callable(iec61131_il_Il_Param_Out_Assignment.__init__)


def test_iec61131_il_il_param_out_assignment_constructor_args():
    sig = inspect.signature(iec61131_il_Il_Param_Out_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_il_param_assignment_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Il_Param_Assignment)


def test_iec61131_il_il_param_assignment_constructor_exists():
    assert callable(iec61131_il_Il_Param_Assignment.__init__)


def test_iec61131_il_il_param_assignment_constructor_args():
    sig = inspect.signature(iec61131_il_Il_Param_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_param_instruction_is_not_abstract():
    assert not inspect.isabstract(Param_Instruction)


def test_param_instruction_constructor_exists():
    assert callable(Param_Instruction.__init__)


def test_param_instruction_constructor_args():
    sig = inspect.signature(Param_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_il_param_last_instruction_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Il_Param_Last_Instruction)


def test_iec61131_il_il_param_last_instruction_constructor_exists():
    assert callable(iec61131_il_Il_Param_Last_Instruction.__init__)


def test_iec61131_il_il_param_last_instruction_constructor_args():
    sig = inspect.signature(iec61131_il_Il_Param_Last_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_il_param_instruction_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Il_Param_Instruction)


def test_iec61131_il_il_param_instruction_constructor_exists():
    assert callable(iec61131_il_Il_Param_Instruction.__init__)


def test_iec61131_il_il_param_instruction_constructor_args():
    sig = inspect.signature(iec61131_il_Il_Param_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_simple_instr_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Simple_Instr)


def test_iec61131_il_simple_instr_constructor_exists():
    assert callable(iec61131_il_Simple_Instr.__init__)


def test_iec61131_il_simple_instr_constructor_args():
    sig = inspect.signature(iec61131_il_Simple_Instr.__init__)
    params = list(sig.parameters.keys())



def test_simple_instr_is_not_abstract():
    assert not inspect.isabstract(Simple_Instr)


def test_simple_instr_constructor_exists():
    assert callable(Simple_Instr.__init__)


def test_simple_instr_constructor_args():
    sig = inspect.signature(Simple_Instr.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_il_simple_instruction_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Il_Simple_Instruction)


def test_iec61131_il_il_simple_instruction_constructor_exists():
    assert callable(iec61131_il_Il_Simple_Instruction.__init__)


def test_iec61131_il_il_simple_instruction_constructor_args():
    sig = inspect.signature(iec61131_il_Il_Simple_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_operands_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Operands)


def test_iec61131_il_operands_constructor_exists():
    assert callable(iec61131_il_Operands.__init__)


def test_iec61131_il_operands_constructor_args():
    sig = inspect.signature(iec61131_il_Operands.__init__)
    params = list(sig.parameters.keys())



def test_il_param_last_instruction_is_not_abstract():
    assert not inspect.isabstract(Il_Param_Last_Instruction)


def test_il_param_last_instruction_constructor_exists():
    assert callable(Il_Param_Last_Instruction.__init__)


def test_il_param_last_instruction_constructor_args():
    sig = inspect.signature(Il_Param_Last_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_il_param_instruction_is_not_abstract():
    assert not inspect.isabstract(Il_Param_Instruction)


def test_il_param_instruction_constructor_exists():
    assert callable(Il_Param_Instruction.__init__)


def test_il_param_instruction_constructor_args():
    sig = inspect.signature(Il_Param_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_il_param_list_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Il_Param_List)


def test_iec61131_il_il_param_list_constructor_exists():
    assert callable(iec61131_il_Il_Param_List.__init__)


def test_iec61131_il_il_param_list_constructor_args():
    sig = inspect.signature(iec61131_il_Il_Param_List.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_il_call_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Il_Call_Operator)


def test_iec61131_il_il_call_operator_constructor_exists():
    assert callable(iec61131_il_Il_Call_Operator.__init__)


def test_iec61131_il_il_call_operator_constructor_args():
    sig = inspect.signature(iec61131_il_Il_Call_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_il_jump_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Il_Jump_Operator)


def test_iec61131_il_il_jump_operator_constructor_exists():
    assert callable(iec61131_il_Il_Jump_Operator.__init__)


def test_iec61131_il_il_jump_operator_constructor_args():
    sig = inspect.signature(iec61131_il_Il_Jump_Operator.__init__)
    params = list(sig.parameters.keys())



def test_il_operand_list_is_not_abstract():
    assert not inspect.isabstract(Il_Operand_List)


def test_il_operand_list_constructor_exists():
    assert callable(Il_Operand_List.__init__)


def test_il_operand_list_constructor_args():
    sig = inspect.signature(Il_Operand_List.__init__)
    params = list(sig.parameters.keys())



def test_il_simple_operator_is_not_abstract():
    assert not inspect.isabstract(Il_Simple_Operator)


def test_il_simple_operator_constructor_exists():
    assert callable(Il_Simple_Operator.__init__)


def test_il_simple_operator_constructor_args():
    sig = inspect.signature(Il_Simple_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_il_expr_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Il_Expr_Operator)


def test_iec61131_il_il_expr_operator_constructor_exists():
    assert callable(iec61131_il_Il_Expr_Operator.__init__)


def test_iec61131_il_il_expr_operator_constructor_args():
    sig = inspect.signature(iec61131_il_Il_Expr_Operator.__init__)
    params = list(sig.parameters.keys())



def test_il_simple_operation_is_not_abstract():
    assert not inspect.isabstract(Il_Simple_Operation)


def test_il_simple_operation_constructor_exists():
    assert callable(Il_Simple_Operation.__init__)


def test_il_simple_operation_constructor_args():
    sig = inspect.signature(Il_Simple_Operation.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_simple_operation2_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Simple_Operation2)


def test_iec61131_il_simple_operation2_constructor_exists():
    assert callable(iec61131_il_Simple_Operation2.__init__)


def test_iec61131_il_simple_operation2_constructor_args():
    sig = inspect.signature(iec61131_il_Simple_Operation2.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_simple_operation1_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Simple_Operation1)


def test_iec61131_il_simple_operation1_constructor_exists():
    assert callable(iec61131_il_Simple_Operation1.__init__)


def test_iec61131_il_simple_operation1_constructor_args():
    sig = inspect.signature(iec61131_il_Simple_Operation1.__init__)
    params = list(sig.parameters.keys())



def test_il_instruction_is_not_abstract():
    assert not inspect.isabstract(Il_Instruction)


def test_il_instruction_constructor_exists():
    assert callable(Il_Instruction.__init__)


def test_il_instruction_constructor_args():
    sig = inspect.signature(Il_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_operands_is_not_abstract():
    assert not inspect.isabstract(Operands)


def test_operands_constructor_exists():
    assert callable(Operands.__init__)


def test_operands_constructor_args():
    sig = inspect.signature(Operands.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_operand1_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Operand1)


def test_iec61131_il_operand1_constructor_exists():
    assert callable(iec61131_il_Operand1.__init__)


def test_iec61131_il_operand1_constructor_args():
    sig = inspect.signature(iec61131_il_Operand1.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_operand2_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Operand2)


def test_iec61131_il_operand2_constructor_exists():
    assert callable(iec61131_il_Operand2.__init__)


def test_iec61131_il_operand2_constructor_args():
    sig = inspect.signature(iec61131_il_Operand2.__init__)
    params = list(sig.parameters.keys())



def test_il_call_operator_is_not_abstract():
    assert not inspect.isabstract(Il_Call_Operator)


def test_il_call_operator_constructor_exists():
    assert callable(Il_Call_Operator.__init__)


def test_il_call_operator_constructor_args():
    sig = inspect.signature(Il_Call_Operator.__init__)
    params = list(sig.parameters.keys())



def test_il_jump_operator_is_not_abstract():
    assert not inspect.isabstract(Il_Jump_Operator)


def test_il_jump_operator_constructor_exists():
    assert callable(Il_Jump_Operator.__init__)


def test_il_jump_operator_constructor_args():
    sig = inspect.signature(Il_Jump_Operator.__init__)
    params = list(sig.parameters.keys())



def test_simple_instr_list_is_not_abstract():
    assert not inspect.isabstract(Simple_Instr_List)


def test_simple_instr_list_constructor_exists():
    assert callable(Simple_Instr_List.__init__)


def test_simple_instr_list_constructor_args():
    sig = inspect.signature(Simple_Instr_List.__init__)
    params = list(sig.parameters.keys())



def test_il_operand_is_not_abstract():
    assert not inspect.isabstract(Il_Operand)


def test_il_operand_constructor_exists():
    assert callable(Il_Operand.__init__)


def test_il_operand_constructor_args():
    sig = inspect.signature(Il_Operand.__init__)
    params = list(sig.parameters.keys())



def test_il_simple_instr_is_not_abstract():
    assert not inspect.isabstract(il_Simple_Instr)


def test_il_simple_instr_constructor_exists():
    assert callable(il_Simple_Instr.__init__)


def test_il_simple_instr_constructor_args():
    sig = inspect.signature(il_Simple_Instr.__init__)
    params = list(sig.parameters.keys())



def test_il_il_operations_is_not_abstract():
    assert not inspect.isabstract(il_Il_Operations)


def test_il_il_operations_constructor_exists():
    assert callable(il_Il_Operations.__init__)


def test_il_il_operations_constructor_args():
    sig = inspect.signature(il_Il_Operations.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_il_formal_funct_call_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Il_Formal_Funct_Call)


def test_iec61131_il_il_formal_funct_call_constructor_exists():
    assert callable(iec61131_il_Il_Formal_Funct_Call.__init__)


def test_iec61131_il_il_formal_funct_call_constructor_args():
    sig = inspect.signature(iec61131_il_Il_Formal_Funct_Call.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_il_expression_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Il_Expression)


def test_iec61131_il_il_expression_constructor_exists():
    assert callable(iec61131_il_Il_Expression.__init__)


def test_iec61131_il_il_expression_constructor_args():
    sig = inspect.signature(iec61131_il_Il_Expression.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_il_simple_operation_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Il_Simple_Operation)


def test_iec61131_il_il_simple_operation_constructor_exists():
    assert callable(iec61131_il_Il_Simple_Operation.__init__)


def test_iec61131_il_il_simple_operation_constructor_args():
    sig = inspect.signature(iec61131_il_Il_Simple_Operation.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_label_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Label)


def test_iec61131_il_label_constructor_exists():
    assert callable(iec61131_il_Label.__init__)


def test_iec61131_il_label_constructor_args():
    sig = inspect.signature(iec61131_il_Label.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_iec61131_il_label_has_label():
    assert hasattr(iec61131_il_Label, "label")
    descriptor = None
    for klass in iec61131_il_Label.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_il_operations_is_not_abstract():
    assert not inspect.isabstract(Il_Operations)


def test_il_operations_constructor_exists():
    assert callable(Il_Operations.__init__)


def test_il_operations_constructor_args():
    sig = inspect.signature(Il_Operations.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_il_return_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Il_Return_Operator)


def test_iec61131_il_il_return_operator_constructor_exists():
    assert callable(iec61131_il_Il_Return_Operator.__init__)


def test_iec61131_il_il_return_operator_constructor_args():
    sig = inspect.signature(iec61131_il_Il_Return_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_il_fb_call_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Il_Fb_Call)


def test_iec61131_il_il_fb_call_constructor_exists():
    assert callable(iec61131_il_Il_Fb_Call.__init__)


def test_iec61131_il_il_fb_call_constructor_args():
    sig = inspect.signature(iec61131_il_Il_Fb_Call.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_il_jump_operation_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Il_Jump_Operation)


def test_iec61131_il_il_jump_operation_constructor_exists():
    assert callable(iec61131_il_Il_Jump_Operation.__init__)


def test_iec61131_il_il_jump_operation_constructor_args():
    sig = inspect.signature(iec61131_il_Il_Jump_Operation.__init__)
    params = list(sig.parameters.keys())



def test_label_is_not_abstract():
    assert not inspect.isabstract(Label)


def test_label_constructor_exists():
    assert callable(Label.__init__)


def test_label_constructor_args():
    sig = inspect.signature(Label.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_il_instruction_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Il_Instruction)


def test_iec61131_il_il_instruction_constructor_exists():
    assert callable(iec61131_il_Il_Instruction.__init__)


def test_iec61131_il_il_instruction_constructor_args():
    sig = inspect.signature(iec61131_il_Il_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_il_simple_instruction_is_not_abstract():
    assert not inspect.isabstract(Il_Simple_Instruction)


def test_il_simple_instruction_constructor_exists():
    assert callable(Il_Simple_Instruction.__init__)


def test_il_simple_instruction_constructor_args():
    sig = inspect.signature(Il_Simple_Instruction.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_simple_instr_list_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Simple_Instr_List)


def test_iec61131_il_simple_instr_list_constructor_exists():
    assert callable(iec61131_il_Simple_Instr_List.__init__)


def test_iec61131_il_simple_instr_list_constructor_args():
    sig = inspect.signature(iec61131_il_Simple_Instr_List.__init__)
    params = list(sig.parameters.keys())



def test_unary_operator_is_not_abstract():
    assert not inspect.isabstract(Unary_Operator)


def test_unary_operator_constructor_exists():
    assert callable(Unary_Operator.__init__)


def test_unary_operator_constructor_args():
    sig = inspect.signature(Unary_Operator.__init__)
    params = list(sig.parameters.keys())



def test_power_symbol_is_not_abstract():
    assert not inspect.isabstract(Power_Symbol)


def test_power_symbol_constructor_exists():
    assert callable(Power_Symbol.__init__)


def test_power_symbol_constructor_args():
    sig = inspect.signature(Power_Symbol.__init__)
    params = list(sig.parameters.keys())



def test_structured_variable_is_not_abstract():
    assert not inspect.isabstract(Structured_Variable)


def test_structured_variable_constructor_exists():
    assert callable(Structured_Variable.__init__)


def test_structured_variable_constructor_args():
    sig = inspect.signature(Structured_Variable.__init__)
    params = list(sig.parameters.keys())



def test_array_variable_is_not_abstract():
    assert not inspect.isabstract(Array_Variable)


def test_array_variable_constructor_exists():
    assert callable(Array_Variable.__init__)


def test_array_variable_constructor_args():
    sig = inspect.signature(Array_Variable.__init__)
    params = list(sig.parameters.keys())



def test_function_name_is_not_abstract():
    assert not inspect.isabstract(Function_Name)


def test_function_name_constructor_exists():
    assert callable(Function_Name.__init__)


def test_function_name_constructor_args():
    sig = inspect.signature(Function_Name.__init__)
    params = list(sig.parameters.keys())



def test_primary_expression_is_not_abstract():
    assert not inspect.isabstract(Primary_Expression)


def test_primary_expression_constructor_exists():
    assert callable(Primary_Expression.__init__)


def test_primary_expression_constructor_args():
    sig = inspect.signature(Primary_Expression.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_expression_constant_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Expression_Constant)


def test_iec61131_st_expression_constant_constructor_exists():
    assert callable(iec61131_st_Expression_Constant.__init__)


def test_iec61131_st_expression_constant_constructor_args():
    sig = inspect.signature(iec61131_st_Expression_Constant.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_expression_variable_type_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Expression_Variable_Type)


def test_iec61131_st_expression_variable_type_constructor_exists():
    assert callable(iec61131_st_Expression_Variable_Type.__init__)


def test_iec61131_st_expression_variable_type_constructor_args():
    sig = inspect.signature(iec61131_st_Expression_Variable_Type.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_call_expression_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Call_Expression)


def test_iec61131_st_call_expression_constructor_exists():
    assert callable(iec61131_st_Call_Expression.__init__)


def test_iec61131_st_call_expression_constructor_args():
    sig = inspect.signature(iec61131_st_Call_Expression.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_expression_enumvalue_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Expression_EnumValue)


def test_iec61131_st_expression_enumvalue_constructor_exists():
    assert callable(iec61131_st_Expression_EnumValue.__init__)


def test_iec61131_st_expression_enumvalue_constructor_args():
    sig = inspect.signature(iec61131_st_Expression_EnumValue.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_bracket_expression_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Bracket_Expression)


def test_iec61131_st_bracket_expression_constructor_exists():
    assert callable(iec61131_st_Bracket_Expression.__init__)


def test_iec61131_st_bracket_expression_constructor_args():
    sig = inspect.signature(iec61131_st_Bracket_Expression.__init__)
    params = list(sig.parameters.keys())



def test_add_operator_is_not_abstract():
    assert not inspect.isabstract(Add_Operator)


def test_add_operator_constructor_exists():
    assert callable(Add_Operator.__init__)


def test_add_operator_constructor_args():
    sig = inspect.signature(Add_Operator.__init__)
    params = list(sig.parameters.keys())



def test_xor_operator_is_not_abstract():
    assert not inspect.isabstract(Xor_Operator)


def test_xor_operator_constructor_exists():
    assert callable(Xor_Operator.__init__)


def test_xor_operator_constructor_args():
    sig = inspect.signature(Xor_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_for_list_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_For_List)


def test_iec61131_st_for_list_constructor_exists():
    assert callable(iec61131_st_For_List.__init__)


def test_iec61131_st_for_list_constructor_args():
    sig = inspect.signature(iec61131_st_For_List.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_control_variable_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Control_Variable)


def test_iec61131_st_control_variable_constructor_exists():
    assert callable(iec61131_st_Control_Variable.__init__)


def test_iec61131_st_control_variable_constructor_args():
    sig = inspect.signature(iec61131_st_Control_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iec61131_st_control_variable_has_name():
    assert hasattr(iec61131_st_Control_Variable, "name")
    descriptor = None
    for klass in iec61131_st_Control_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statement_list_is_not_abstract():
    assert not inspect.isabstract(Statement_List)


def test_statement_list_constructor_exists():
    assert callable(Statement_List.__init__)


def test_statement_list_constructor_args():
    sig = inspect.signature(Statement_List.__init__)
    params = list(sig.parameters.keys())



def test_selection_statement_is_not_abstract():
    assert not inspect.isabstract(Selection_Statement)


def test_selection_statement_constructor_exists():
    assert callable(Selection_Statement.__init__)


def test_selection_statement_constructor_args():
    sig = inspect.signature(Selection_Statement.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_if_statement_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_If_Statement)


def test_iec61131_st_if_statement_constructor_exists():
    assert callable(iec61131_st_If_Statement.__init__)


def test_iec61131_st_if_statement_constructor_args():
    sig = inspect.signature(iec61131_st_If_Statement.__init__)
    params = list(sig.parameters.keys())



def test_not_operator_is_not_abstract():
    assert not inspect.isabstract(Not_Operator)


def test_not_operator_constructor_exists():
    assert callable(Not_Operator.__init__)


def test_not_operator_constructor_args():
    sig = inspect.signature(Not_Operator.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_variables_symbolic_variable_is_not_abstract():
    assert not inspect.isabstract(iec61131_variables_Symbolic_Variable)


def test_iec61131_variables_symbolic_variable_constructor_exists():
    assert callable(iec61131_variables_Symbolic_Variable.__init__)


def test_iec61131_variables_symbolic_variable_constructor_args():
    sig = inspect.signature(iec61131_variables_Symbolic_Variable.__init__)
    params = list(sig.parameters.keys())



def test_for_list_is_not_abstract():
    assert not inspect.isabstract(For_List)


def test_for_list_constructor_exists():
    assert callable(For_List.__init__)


def test_for_list_constructor_args():
    sig = inspect.signature(For_List.__init__)
    params = list(sig.parameters.keys())



def test_control_variable_is_not_abstract():
    assert not inspect.isabstract(Control_Variable)


def test_control_variable_constructor_exists():
    assert callable(Control_Variable.__init__)


def test_control_variable_constructor_args():
    sig = inspect.signature(Control_Variable.__init__)
    params = list(sig.parameters.keys())



def test_iteration_statement_is_not_abstract():
    assert not inspect.isabstract(Iteration_Statement)


def test_iteration_statement_constructor_exists():
    assert callable(Iteration_Statement.__init__)


def test_iteration_statement_constructor_args():
    sig = inspect.signature(Iteration_Statement.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_exit_statement_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Exit_Statement)


def test_iec61131_st_exit_statement_constructor_exists():
    assert callable(iec61131_st_Exit_Statement.__init__)


def test_iec61131_st_exit_statement_constructor_args():
    sig = inspect.signature(iec61131_st_Exit_Statement.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_while_statement_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_While_Statement)


def test_iec61131_st_while_statement_constructor_exists():
    assert callable(iec61131_st_While_Statement.__init__)


def test_iec61131_st_while_statement_constructor_args():
    sig = inspect.signature(iec61131_st_While_Statement.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_repeat_statement_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Repeat_Statement)


def test_iec61131_st_repeat_statement_constructor_exists():
    assert callable(iec61131_st_Repeat_Statement.__init__)


def test_iec61131_st_repeat_statement_constructor_args():
    sig = inspect.signature(iec61131_st_Repeat_Statement.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_for_statement_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_For_Statement)


def test_iec61131_st_for_statement_constructor_exists():
    assert callable(iec61131_st_For_Statement.__init__)


def test_iec61131_st_for_statement_constructor_args():
    sig = inspect.signature(iec61131_st_For_Statement.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_case_list_element_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Case_List_Element)


def test_iec61131_st_case_list_element_constructor_exists():
    assert callable(iec61131_st_Case_List_Element.__init__)


def test_iec61131_st_case_list_element_constructor_args():
    sig = inspect.signature(iec61131_st_Case_List_Element.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_case_list_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Case_List)


def test_iec61131_st_case_list_constructor_exists():
    assert callable(iec61131_st_Case_List.__init__)


def test_iec61131_st_case_list_constructor_args():
    sig = inspect.signature(iec61131_st_Case_List.__init__)
    params = list(sig.parameters.keys())



def test_case_list_is_not_abstract():
    assert not inspect.isabstract(Case_List)


def test_case_list_constructor_exists():
    assert callable(Case_List.__init__)


def test_case_list_constructor_args():
    sig = inspect.signature(Case_List.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_case_element_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Case_Element)


def test_iec61131_st_case_element_constructor_exists():
    assert callable(iec61131_st_Case_Element.__init__)


def test_iec61131_st_case_element_constructor_args():
    sig = inspect.signature(iec61131_st_Case_Element.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_else_statement_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Else_Statement)


def test_iec61131_st_else_statement_constructor_exists():
    assert callable(iec61131_st_Else_Statement.__init__)


def test_iec61131_st_else_statement_constructor_args():
    sig = inspect.signature(iec61131_st_Else_Statement.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_else_if_statement_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Else_If_Statement)


def test_iec61131_st_else_if_statement_constructor_exists():
    assert callable(iec61131_st_Else_If_Statement.__init__)


def test_iec61131_st_else_if_statement_constructor_args():
    sig = inspect.signature(iec61131_st_Else_If_Statement.__init__)
    params = list(sig.parameters.keys())



def test_case_element_is_not_abstract():
    assert not inspect.isabstract(Case_Element)


def test_case_element_constructor_exists():
    assert callable(Case_Element.__init__)


def test_case_element_constructor_args():
    sig = inspect.signature(Case_Element.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_case_statement_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Case_Statement)


def test_iec61131_st_case_statement_constructor_exists():
    assert callable(iec61131_st_Case_Statement.__init__)


def test_iec61131_st_case_statement_constructor_args():
    sig = inspect.signature(iec61131_st_Case_Statement.__init__)
    params = list(sig.parameters.keys())



def test_else_statement_is_not_abstract():
    assert not inspect.isabstract(Else_Statement)


def test_else_statement_constructor_exists():
    assert callable(Else_Statement.__init__)


def test_else_statement_constructor_args():
    sig = inspect.signature(Else_Statement.__init__)
    params = list(sig.parameters.keys())



def test_else_if_statement_is_not_abstract():
    assert not inspect.isabstract(Else_If_Statement)


def test_else_if_statement_constructor_exists():
    assert callable(Else_If_Statement.__init__)


def test_else_if_statement_constructor_args():
    sig = inspect.signature(Else_If_Statement.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_param_assignment_is_not_abstract():
    assert not inspect.isabstract(Param_Assignment)


def test_param_assignment_constructor_exists():
    assert callable(Param_Assignment.__init__)


def test_param_assignment_constructor_args():
    sig = inspect.signature(Param_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_param_type1_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Param_Type1)


def test_iec61131_st_param_type1_constructor_exists():
    assert callable(iec61131_st_Param_Type1.__init__)


def test_iec61131_st_param_type1_constructor_args():
    sig = inspect.signature(iec61131_st_Param_Type1.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_param_type2_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Param_Type2)


def test_iec61131_st_param_type2_constructor_exists():
    assert callable(iec61131_st_Param_Type2.__init__)


def test_iec61131_st_param_type2_constructor_args():
    sig = inspect.signature(iec61131_st_Param_Type2.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_param_assignment2_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Param_Assignment2)


def test_iec61131_il_param_assignment2_constructor_exists():
    assert callable(iec61131_il_Param_Assignment2.__init__)


def test_iec61131_il_param_assignment2_constructor_args():
    sig = inspect.signature(iec61131_il_Param_Assignment2.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_il_operand_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Il_Operand)


def test_iec61131_il_il_operand_constructor_exists():
    assert callable(iec61131_il_Il_Operand.__init__)


def test_iec61131_il_il_operand_constructor_args():
    sig = inspect.signature(iec61131_il_Il_Operand.__init__)
    params = list(sig.parameters.keys())



def test_subprogram_control_statement_is_not_abstract():
    assert not inspect.isabstract(Subprogram_Control_Statement)


def test_subprogram_control_statement_constructor_exists():
    assert callable(Subprogram_Control_Statement.__init__)


def test_subprogram_control_statement_constructor_args():
    sig = inspect.signature(Subprogram_Control_Statement.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_fb_invocation_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Fb_Invocation)


def test_iec61131_st_fb_invocation_constructor_exists():
    assert callable(iec61131_st_Fb_Invocation.__init__)


def test_iec61131_st_fb_invocation_constructor_args():
    sig = inspect.signature(iec61131_st_Fb_Invocation.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_return_statement_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Return_Statement)


def test_iec61131_st_return_statement_constructor_exists():
    assert callable(iec61131_st_Return_Statement.__init__)


def test_iec61131_st_return_statement_constructor_args():
    sig = inspect.signature(iec61131_st_Return_Statement.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_iteration_statement_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Iteration_Statement)


def test_iec61131_st_iteration_statement_constructor_exists():
    assert callable(iec61131_st_Iteration_Statement.__init__)


def test_iec61131_st_iteration_statement_constructor_args():
    sig = inspect.signature(iec61131_st_Iteration_Statement.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_selection_statement_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Selection_Statement)


def test_iec61131_st_selection_statement_constructor_exists():
    assert callable(iec61131_st_Selection_Statement.__init__)


def test_iec61131_st_selection_statement_constructor_args():
    sig = inspect.signature(iec61131_st_Selection_Statement.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_subprogram_control_statement_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Subprogram_Control_Statement)


def test_iec61131_st_subprogram_control_statement_constructor_exists():
    assert callable(iec61131_st_Subprogram_Control_Statement.__init__)


def test_iec61131_st_subprogram_control_statement_constructor_args():
    sig = inspect.signature(iec61131_st_Subprogram_Control_Statement.__init__)
    params = list(sig.parameters.keys())



def test_expression_variable_is_not_abstract():
    assert not inspect.isabstract(Expression_Variable)


def test_expression_variable_constructor_exists():
    assert callable(Expression_Variable.__init__)


def test_expression_variable_constructor_args():
    sig = inspect.signature(Expression_Variable.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_assignment_statement_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Assignment_Statement)


def test_iec61131_st_assignment_statement_constructor_exists():
    assert callable(iec61131_st_Assignment_Statement.__init__)


def test_iec61131_st_assignment_statement_constructor_args():
    sig = inspect.signature(iec61131_st_Assignment_Statement.__init__)
    params = list(sig.parameters.keys())



def test_or_operator_is_not_abstract():
    assert not inspect.isabstract(Or_Operator)


def test_or_operator_constructor_exists():
    assert callable(Or_Operator.__init__)


def test_or_operator_constructor_args():
    sig = inspect.signature(Or_Operator.__init__)
    params = list(sig.parameters.keys())



def test_expression_types_is_not_abstract():
    assert not inspect.isabstract(Expression_Types)


def test_expression_types_constructor_exists():
    assert callable(Expression_Types.__init__)


def test_expression_types_constructor_args():
    sig = inspect.signature(Expression_Types.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_xor_expression_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Xor_Expression)


def test_iec61131_st_xor_expression_constructor_exists():
    assert callable(iec61131_st_Xor_Expression.__init__)


def test_iec61131_st_xor_expression_constructor_args():
    sig = inspect.signature(iec61131_st_Xor_Expression.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_power_expression_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Power_Expression)


def test_iec61131_st_power_expression_constructor_exists():
    assert callable(iec61131_st_Power_Expression.__init__)


def test_iec61131_st_power_expression_constructor_args():
    sig = inspect.signature(iec61131_st_Power_Expression.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_unary_expression_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Unary_Expression)


def test_iec61131_st_unary_expression_constructor_exists():
    assert callable(iec61131_st_Unary_Expression.__init__)


def test_iec61131_st_unary_expression_constructor_args():
    sig = inspect.signature(iec61131_st_Unary_Expression.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_equ_expression_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Equ_Expression)


def test_iec61131_st_equ_expression_constructor_exists():
    assert callable(iec61131_st_Equ_Expression.__init__)


def test_iec61131_st_equ_expression_constructor_args():
    sig = inspect.signature(iec61131_st_Equ_Expression.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_and_expression_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_And_Expression)


def test_iec61131_st_and_expression_constructor_exists():
    assert callable(iec61131_st_And_Expression.__init__)


def test_iec61131_st_and_expression_constructor_args():
    sig = inspect.signature(iec61131_st_And_Expression.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_add_expression_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Add_Expression)


def test_iec61131_st_add_expression_constructor_exists():
    assert callable(iec61131_st_Add_Expression.__init__)


def test_iec61131_st_add_expression_constructor_args():
    sig = inspect.signature(iec61131_st_Add_Expression.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_term_expression_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Term_Expression)


def test_iec61131_st_term_expression_constructor_exists():
    assert callable(iec61131_st_Term_Expression.__init__)


def test_iec61131_st_term_expression_constructor_args():
    sig = inspect.signature(iec61131_st_Term_Expression.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_comparison_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Comparison)


def test_iec61131_st_comparison_constructor_exists():
    assert callable(iec61131_st_Comparison.__init__)


def test_iec61131_st_comparison_constructor_args():
    sig = inspect.signature(iec61131_st_Comparison.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_primary_expression_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Primary_Expression)


def test_iec61131_st_primary_expression_constructor_exists():
    assert callable(iec61131_st_Primary_Expression.__init__)


def test_iec61131_st_primary_expression_constructor_args():
    sig = inspect.signature(iec61131_st_Primary_Expression.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_expression_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Expression)


def test_iec61131_st_expression_constructor_exists():
    assert callable(iec61131_st_Expression.__init__)


def test_iec61131_st_expression_constructor_args():
    sig = inspect.signature(iec61131_st_Expression.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_prog_data_source_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Prog_Data_Source)


def test_iec61131_configurations_prog_data_source_constructor_exists():
    assert callable(iec61131_configurations_Prog_Data_Source.__init__)


def test_iec61131_configurations_prog_data_source_constructor_args():
    sig = inspect.signature(iec61131_configurations_Prog_Data_Source.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_prog_conf_element_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Prog_Conf_Element)


def test_iec61131_configurations_prog_conf_element_constructor_exists():
    assert callable(iec61131_configurations_Prog_Conf_Element.__init__)


def test_iec61131_configurations_prog_conf_element_constructor_args():
    sig = inspect.signature(iec61131_configurations_Prog_Conf_Element.__init__)
    params = list(sig.parameters.keys())



def test_prog_conf_element_is_not_abstract():
    assert not inspect.isabstract(Prog_Conf_Element)


def test_prog_conf_element_constructor_exists():
    assert callable(Prog_Conf_Element.__init__)


def test_prog_conf_element_constructor_args():
    sig = inspect.signature(Prog_Conf_Element.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_fb_task_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Fb_Task)


def test_iec61131_configurations_fb_task_constructor_exists():
    assert callable(iec61131_configurations_Fb_Task.__init__)


def test_iec61131_configurations_fb_task_constructor_args():
    sig = inspect.signature(iec61131_configurations_Fb_Task.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_prog_cnxn_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Prog_Cnxn)


def test_iec61131_configurations_prog_cnxn_constructor_exists():
    assert callable(iec61131_configurations_Prog_Cnxn.__init__)


def test_iec61131_configurations_prog_cnxn_constructor_args():
    sig = inspect.signature(iec61131_configurations_Prog_Cnxn.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_prog_conf_elements_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Prog_Conf_Elements)


def test_iec61131_configurations_prog_conf_elements_constructor_exists():
    assert callable(iec61131_configurations_Prog_Conf_Elements.__init__)


def test_iec61131_configurations_prog_conf_elements_constructor_args():
    sig = inspect.signature(iec61131_configurations_Prog_Conf_Elements.__init__)
    params = list(sig.parameters.keys())



def test_task_initialization_is_not_abstract():
    assert not inspect.isabstract(Task_Initialization)


def test_task_initialization_constructor_exists():
    assert callable(Task_Initialization.__init__)


def test_task_initialization_constructor_args():
    sig = inspect.signature(Task_Initialization.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_priority_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Priority)


def test_iec61131_configurations_priority_constructor_exists():
    assert callable(iec61131_configurations_Priority.__init__)


def test_iec61131_configurations_priority_constructor_args():
    sig = inspect.signature(iec61131_configurations_Priority.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_interval_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Interval)


def test_iec61131_configurations_interval_constructor_exists():
    assert callable(iec61131_configurations_Interval.__init__)


def test_iec61131_configurations_interval_constructor_args():
    sig = inspect.signature(iec61131_configurations_Interval.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_single_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Single)


def test_iec61131_configurations_single_constructor_exists():
    assert callable(iec61131_configurations_Single.__init__)


def test_iec61131_configurations_single_constructor_args():
    sig = inspect.signature(iec61131_configurations_Single.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_instance_specific_init_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Instance_Specific_Init)


def test_iec61131_configurations_instance_specific_init_constructor_exists():
    assert callable(iec61131_configurations_Instance_Specific_Init.__init__)


def test_iec61131_configurations_instance_specific_init_constructor_args():
    sig = inspect.signature(iec61131_configurations_Instance_Specific_Init.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_data_sink_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Data_Sink)


def test_iec61131_configurations_data_sink_constructor_exists():
    assert callable(iec61131_configurations_Data_Sink.__init__)


def test_iec61131_configurations_data_sink_constructor_args():
    sig = inspect.signature(iec61131_configurations_Data_Sink.__init__)
    params = list(sig.parameters.keys())



def test_prog_data_source_is_not_abstract():
    assert not inspect.isabstract(Prog_Data_Source)


def test_prog_data_source_constructor_exists():
    assert callable(Prog_Data_Source.__init__)


def test_prog_data_source_constructor_args():
    sig = inspect.signature(Prog_Data_Source.__init__)
    params = list(sig.parameters.keys())



def test_data_sink_is_not_abstract():
    assert not inspect.isabstract(Data_Sink)


def test_data_sink_constructor_exists():
    assert callable(Data_Sink.__init__)


def test_data_sink_constructor_args():
    sig = inspect.signature(Data_Sink.__init__)
    params = list(sig.parameters.keys())



def test_prog_cnxn_is_not_abstract():
    assert not inspect.isabstract(Prog_Cnxn)


def test_prog_cnxn_constructor_exists():
    assert callable(Prog_Cnxn.__init__)


def test_prog_cnxn_constructor_args():
    sig = inspect.signature(Prog_Cnxn.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_prog_source_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Prog_Source)


def test_iec61131_configurations_prog_source_constructor_exists():
    assert callable(iec61131_configurations_Prog_Source.__init__)


def test_iec61131_configurations_prog_source_constructor_args():
    sig = inspect.signature(iec61131_configurations_Prog_Source.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_prog_sink_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Prog_Sink)


def test_iec61131_configurations_prog_sink_constructor_exists():
    assert callable(iec61131_configurations_Prog_Sink.__init__)


def test_iec61131_configurations_prog_sink_constructor_args():
    sig = inspect.signature(iec61131_configurations_Prog_Sink.__init__)
    params = list(sig.parameters.keys())



def test_data_source_is_not_abstract():
    assert not inspect.isabstract(Data_Source)


def test_data_source_constructor_exists():
    assert callable(Data_Source.__init__)


def test_data_source_constructor_args():
    sig = inspect.signature(Data_Source.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_program_output_reference_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Program_Output_Reference)


def test_iec61131_configurations_program_output_reference_constructor_exists():
    assert callable(iec61131_configurations_Program_Output_Reference.__init__)


def test_iec61131_configurations_program_output_reference_constructor_args():
    sig = inspect.signature(iec61131_configurations_Program_Output_Reference.__init__)
    params = list(sig.parameters.keys())



def test_configurations_data_sink_is_not_abstract():
    assert not inspect.isabstract(configurations_Data_Sink)


def test_configurations_data_sink_constructor_exists():
    assert callable(configurations_Data_Sink.__init__)


def test_configurations_data_sink_constructor_args():
    sig = inspect.signature(configurations_Data_Sink.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_data_source_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Data_Source)


def test_iec61131_configurations_data_source_constructor_exists():
    assert callable(iec61131_configurations_Data_Source.__init__)


def test_iec61131_configurations_data_source_constructor_args():
    sig = inspect.signature(iec61131_configurations_Data_Source.__init__)
    params = list(sig.parameters.keys())



def test_instance_specific_init_is_not_abstract():
    assert not inspect.isabstract(Instance_Specific_Init)


def test_instance_specific_init_constructor_exists():
    assert callable(Instance_Specific_Init.__init__)


def test_instance_specific_init_constructor_args():
    sig = inspect.signature(Instance_Specific_Init.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_instance_spec2_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Instance_Spec2)


def test_iec61131_configurations_instance_spec2_constructor_exists():
    assert callable(iec61131_configurations_Instance_Spec2.__init__)


def test_iec61131_configurations_instance_spec2_constructor_args():
    sig = inspect.signature(iec61131_configurations_Instance_Spec2.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_instance_spec1_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Instance_Spec1)


def test_iec61131_configurations_instance_spec1_constructor_exists():
    assert callable(iec61131_configurations_Instance_Spec1.__init__)


def test_iec61131_configurations_instance_spec1_constructor_args():
    sig = inspect.signature(iec61131_configurations_Instance_Spec1.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_instance_specific_initializations_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Instance_Specific_Initializations)


def test_iec61131_configurations_instance_specific_initializations_constructor_exists():
    assert callable(iec61131_configurations_Instance_Specific_Initializations.__init__)


def test_iec61131_configurations_instance_specific_initializations_constructor_args():
    sig = inspect.signature(iec61131_configurations_Instance_Specific_Initializations.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_byte_string_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_Byte_String_Type_Name)


def test_iec61131_types_byte_string_type_name_constructor_exists():
    assert callable(iec61131_types_Byte_String_Type_Name.__init__)


def test_iec61131_types_byte_string_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_Byte_String_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_single_element_type_name_is_not_abstract():
    assert not inspect.isabstract(Single_Element_Type_Name)


def test_single_element_type_name_constructor_exists():
    assert callable(Single_Element_Type_Name.__init__)


def test_single_element_type_name_constructor_args():
    sig = inspect.signature(Single_Element_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_enumerated_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_Enumerated_Type_Name)


def test_iec61131_types_enumerated_type_name_constructor_exists():
    assert callable(iec61131_types_Enumerated_Type_Name.__init__)


def test_iec61131_types_enumerated_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_Enumerated_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_subrange_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_Subrange_Type_Name)


def test_iec61131_types_subrange_type_name_constructor_exists():
    assert callable(iec61131_types_Subrange_Type_Name.__init__)


def test_iec61131_types_subrange_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_Subrange_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_types_single_element_type_name_is_not_abstract():
    assert not inspect.isabstract(types_Single_Element_Type_Name)


def test_types_single_element_type_name_constructor_exists():
    assert callable(types_Single_Element_Type_Name.__init__)


def test_types_single_element_type_name_constructor_args():
    sig = inspect.signature(types_Single_Element_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_types_derived_type_name_is_not_abstract():
    assert not inspect.isabstract(types_Derived_Type_Name)


def test_types_derived_type_name_constructor_exists():
    assert callable(types_Derived_Type_Name.__init__)


def test_types_derived_type_name_constructor_args():
    sig = inspect.signature(types_Derived_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_derived_type_name_is_not_abstract():
    assert not inspect.isabstract(Derived_Type_Name)


def test_derived_type_name_constructor_exists():
    assert callable(Derived_Type_Name.__init__)


def test_derived_type_name_constructor_args():
    sig = inspect.signature(Derived_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_array_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_Array_Type_Name)


def test_iec61131_types_array_type_name_constructor_exists():
    assert callable(iec61131_types_Array_Type_Name.__init__)


def test_iec61131_types_array_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_Array_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_string_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_String_Type_Name)


def test_iec61131_types_string_type_name_constructor_exists():
    assert callable(iec61131_types_String_Type_Name.__init__)


def test_iec61131_types_string_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_String_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_single_element_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_Single_Element_Type_Name)


def test_iec61131_types_single_element_type_name_constructor_exists():
    assert callable(iec61131_types_Single_Element_Type_Name.__init__)


def test_iec61131_types_single_element_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_Single_Element_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_duration_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_Duration_Type_Name)


def test_iec61131_types_duration_type_name_constructor_exists():
    assert callable(iec61131_types_Duration_Type_Name.__init__)


def test_iec61131_types_duration_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_Duration_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_ld_rung_is_not_abstract():
    assert not inspect.isabstract(iec61131_ld_Rung)


def test_iec61131_ld_rung_constructor_exists():
    assert callable(iec61131_ld_Rung.__init__)


def test_iec61131_ld_rung_constructor_args():
    sig = inspect.signature(iec61131_ld_Rung.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_simple_specification_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_Simple_Specification)


def test_iec61131_types_simple_specification_constructor_exists():
    assert callable(iec61131_types_Simple_Specification.__init__)


def test_iec61131_types_simple_specification_constructor_args():
    sig = inspect.signature(iec61131_types_Simple_Specification.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_variables_subscript_list_is_not_abstract():
    assert not inspect.isabstract(iec61131_variables_Subscript_List)


def test_iec61131_variables_subscript_list_constructor_exists():
    assert callable(iec61131_variables_Subscript_List.__init__)


def test_iec61131_variables_subscript_list_constructor_args():
    sig = inspect.signature(iec61131_variables_Subscript_List.__init__)
    params = list(sig.parameters.keys())



def test_input_reference_is_not_abstract():
    assert not inspect.isabstract(Input_Reference)


def test_input_reference_constructor_exists():
    assert callable(Input_Reference.__init__)


def test_input_reference_constructor_args():
    sig = inspect.signature(Input_Reference.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_task_initialization_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Task_Initialization)


def test_iec61131_configurations_task_initialization_constructor_exists():
    assert callable(iec61131_configurations_Task_Initialization.__init__)


def test_iec61131_configurations_task_initialization_constructor_args():
    sig = inspect.signature(iec61131_configurations_Task_Initialization.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_task_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Task_Name)


def test_iec61131_configurations_task_name_constructor_exists():
    assert callable(iec61131_configurations_Task_Name.__init__)


def test_iec61131_configurations_task_name_constructor_args():
    sig = inspect.signature(iec61131_configurations_Task_Name.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iec61131_configurations_task_name_has_name():
    assert hasattr(iec61131_configurations_Task_Name, "name")
    descriptor = None
    for klass in iec61131_configurations_Task_Name.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iec61131_configurations_program_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Program_Name)


def test_iec61131_configurations_program_name_constructor_exists():
    assert callable(iec61131_configurations_Program_Name.__init__)


def test_iec61131_configurations_program_name_constructor_args():
    sig = inspect.signature(iec61131_configurations_Program_Name.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iec61131_configurations_program_name_has_name():
    assert hasattr(iec61131_configurations_Program_Name, "name")
    descriptor = None
    for klass in iec61131_configurations_Program_Name.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iec61131_configurations_access_path_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Access_Path)


def test_iec61131_configurations_access_path_constructor_exists():
    assert callable(iec61131_configurations_Access_Path.__init__)


def test_iec61131_configurations_access_path_constructor_args():
    sig = inspect.signature(iec61131_configurations_Access_Path.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_access_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Access_Name)


def test_iec61131_configurations_access_name_constructor_exists():
    assert callable(iec61131_configurations_Access_Name.__init__)


def test_iec61131_configurations_access_name_constructor_args():
    sig = inspect.signature(iec61131_configurations_Access_Name.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iec61131_configurations_access_name_has_name():
    assert hasattr(iec61131_configurations_Access_Name, "name")
    descriptor = None
    for klass in iec61131_configurations_Access_Name.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_access_path_is_not_abstract():
    assert not inspect.isabstract(Access_Path)


def test_access_path_constructor_exists():
    assert callable(Access_Path.__init__)


def test_access_path_constructor_args():
    sig = inspect.signature(Access_Path.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_symbolic_path_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Symbolic_Path)


def test_iec61131_configurations_symbolic_path_constructor_exists():
    assert callable(iec61131_configurations_Symbolic_Path.__init__)


def test_iec61131_configurations_symbolic_path_constructor_args():
    sig = inspect.signature(iec61131_configurations_Symbolic_Path.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_direct_path_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Direct_Path)


def test_iec61131_configurations_direct_path_constructor_exists():
    assert callable(iec61131_configurations_Direct_Path.__init__)


def test_iec61131_configurations_direct_path_constructor_args():
    sig = inspect.signature(iec61131_configurations_Direct_Path.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_access_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Access_Declaration)


def test_iec61131_configurations_access_declaration_constructor_exists():
    assert callable(iec61131_configurations_Access_Declaration.__init__)


def test_iec61131_configurations_access_declaration_constructor_args():
    sig = inspect.signature(iec61131_configurations_Access_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_iec61131_configurations_access_declaration_has_direction():
    assert hasattr(iec61131_configurations_Access_Declaration, "direction")
    descriptor = None
    for klass in iec61131_configurations_Access_Declaration.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_access_declaration_is_not_abstract():
    assert not inspect.isabstract(Access_Declaration)


def test_access_declaration_constructor_exists():
    assert callable(Access_Declaration.__init__)


def test_access_declaration_constructor_args():
    sig = inspect.signature(Access_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_access_declarations_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Access_Declarations)


def test_iec61131_configurations_access_declarations_constructor_exists():
    assert callable(iec61131_configurations_Access_Declarations.__init__)


def test_iec61131_configurations_access_declarations_constructor_args():
    sig = inspect.signature(iec61131_configurations_Access_Declarations.__init__)
    params = list(sig.parameters.keys())



def test_resource_declaration_is_not_abstract():
    assert not inspect.isabstract(Resource_Declaration)


def test_resource_declaration_constructor_exists():
    assert callable(Resource_Declaration.__init__)


def test_resource_declaration_constructor_args():
    sig = inspect.signature(Resource_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_access_declarations_is_not_abstract():
    assert not inspect.isabstract(Access_Declarations)


def test_access_declarations_constructor_exists():
    assert callable(Access_Declarations.__init__)


def test_access_declarations_constructor_args():
    sig = inspect.signature(Access_Declarations.__init__)
    params = list(sig.parameters.keys())



def test_instance_specific_initializations_is_not_abstract():
    assert not inspect.isabstract(Instance_Specific_Initializations)


def test_instance_specific_initializations_constructor_exists():
    assert callable(Instance_Specific_Initializations.__init__)


def test_instance_specific_initializations_constructor_args():
    sig = inspect.signature(Instance_Specific_Initializations.__init__)
    params = list(sig.parameters.keys())



def test_global_var_declarations_is_not_abstract():
    assert not inspect.isabstract(Global_Var_Declarations)


def test_global_var_declarations_constructor_exists():
    assert callable(Global_Var_Declarations.__init__)


def test_global_var_declarations_constructor_args():
    sig = inspect.signature(Global_Var_Declarations.__init__)
    params = list(sig.parameters.keys())



def test_single_resource_declaration_is_not_abstract():
    assert not inspect.isabstract(Single_Resource_Declaration)


def test_single_resource_declaration_constructor_exists():
    assert callable(Single_Resource_Declaration.__init__)


def test_single_resource_declaration_constructor_args():
    sig = inspect.signature(Single_Resource_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_configuration_name_is_not_abstract():
    assert not inspect.isabstract(Configuration_Name)


def test_configuration_name_constructor_exists():
    assert callable(Configuration_Name.__init__)


def test_configuration_name_constructor_args():
    sig = inspect.signature(Configuration_Name.__init__)
    params = list(sig.parameters.keys())



def test_prog_conf_elements_is_not_abstract():
    assert not inspect.isabstract(Prog_Conf_Elements)


def test_prog_conf_elements_constructor_exists():
    assert callable(Prog_Conf_Elements.__init__)


def test_prog_conf_elements_constructor_args():
    sig = inspect.signature(Prog_Conf_Elements.__init__)
    params = list(sig.parameters.keys())



def test_program_name_is_not_abstract():
    assert not inspect.isabstract(Program_Name)


def test_program_name_constructor_exists():
    assert callable(Program_Name.__init__)


def test_program_name_constructor_args():
    sig = inspect.signature(Program_Name.__init__)
    params = list(sig.parameters.keys())



def test_single_is_not_abstract():
    assert not inspect.isabstract(Single)


def test_single_constructor_exists():
    assert callable(Single.__init__)


def test_single_constructor_args():
    sig = inspect.signature(Single.__init__)
    params = list(sig.parameters.keys())



def test_priority_is_not_abstract():
    assert not inspect.isabstract(Priority)


def test_priority_constructor_exists():
    assert callable(Priority.__init__)


def test_priority_constructor_args():
    sig = inspect.signature(Priority.__init__)
    params = list(sig.parameters.keys())



def test_task_name_is_not_abstract():
    assert not inspect.isabstract(Task_Name)


def test_task_name_constructor_exists():
    assert callable(Task_Name.__init__)


def test_task_name_constructor_args():
    sig = inspect.signature(Task_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_task_configuration_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Task_Configuration)


def test_iec61131_configurations_task_configuration_constructor_exists():
    assert callable(iec61131_configurations_Task_Configuration.__init__)


def test_iec61131_configurations_task_configuration_constructor_args():
    sig = inspect.signature(iec61131_configurations_Task_Configuration.__init__)
    params = list(sig.parameters.keys())



def test_program_configuration_is_not_abstract():
    assert not inspect.isabstract(Program_Configuration)


def test_program_configuration_constructor_exists():
    assert callable(Program_Configuration.__init__)


def test_program_configuration_constructor_args():
    sig = inspect.signature(Program_Configuration.__init__)
    params = list(sig.parameters.keys())



def test_task_configuration_is_not_abstract():
    assert not inspect.isabstract(Task_Configuration)


def test_task_configuration_constructor_exists():
    assert callable(Task_Configuration.__init__)


def test_task_configuration_constructor_args():
    sig = inspect.signature(Task_Configuration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_single_resource_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Single_Resource_Declaration)


def test_iec61131_configurations_single_resource_declaration_constructor_exists():
    assert callable(iec61131_configurations_Single_Resource_Declaration.__init__)


def test_iec61131_configurations_single_resource_declaration_constructor_args():
    sig = inspect.signature(iec61131_configurations_Single_Resource_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_resource_type_name_is_not_abstract():
    assert not inspect.isabstract(Resource_Type_Name)


def test_resource_type_name_constructor_exists():
    assert callable(Resource_Type_Name.__init__)


def test_resource_type_name_constructor_args():
    sig = inspect.signature(Resource_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_resource_name_is_not_abstract():
    assert not inspect.isabstract(Resource_Name)


def test_resource_name_constructor_exists():
    assert callable(Resource_Name.__init__)


def test_resource_name_constructor_args():
    sig = inspect.signature(Resource_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_resource_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Resource_Name)


def test_iec61131_configurations_resource_name_constructor_exists():
    assert callable(iec61131_configurations_Resource_Name.__init__)


def test_iec61131_configurations_resource_name_constructor_args():
    sig = inspect.signature(iec61131_configurations_Resource_Name.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iec61131_configurations_resource_name_has_name():
    assert hasattr(iec61131_configurations_Resource_Name, "name")
    descriptor = None
    for klass in iec61131_configurations_Resource_Name.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simple_type_name_is_not_abstract():
    assert not inspect.isabstract(Simple_Type_Name)


def test_simple_type_name_constructor_exists():
    assert callable(Simple_Type_Name.__init__)


def test_simple_type_name_constructor_args():
    sig = inspect.signature(Simple_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_single_element_type_declaration_is_not_abstract():
    assert not inspect.isabstract(Single_Element_Type_Declaration)


def test_single_element_type_declaration_constructor_exists():
    assert callable(Single_Element_Type_Declaration.__init__)


def test_single_element_type_declaration_constructor_args():
    sig = inspect.signature(Single_Element_Type_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_subrange_type_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Subrange_Type_Declaration)


def test_iec61131_pous_subrange_type_declaration_constructor_exists():
    assert callable(iec61131_pous_Subrange_Type_Declaration.__init__)


def test_iec61131_pous_subrange_type_declaration_constructor_args():
    sig = inspect.signature(iec61131_pous_Subrange_Type_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_simple_type_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Simple_Type_Declaration)


def test_iec61131_pous_simple_type_declaration_constructor_exists():
    assert callable(iec61131_pous_Simple_Type_Declaration.__init__)


def test_iec61131_pous_simple_type_declaration_constructor_args():
    sig = inspect.signature(iec61131_pous_Simple_Type_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_function_block_declaration_is_not_abstract():
    assert not inspect.isabstract(Function_Block_Declaration)


def test_function_block_declaration_constructor_exists():
    assert callable(Function_Block_Declaration.__init__)


def test_function_block_declaration_constructor_args():
    sig = inspect.signature(Function_Block_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_function_declaration_is_not_abstract():
    assert not inspect.isabstract(Function_Declaration)


def test_function_declaration_constructor_exists():
    assert callable(Function_Declaration.__init__)


def test_function_declaration_constructor_args():
    sig = inspect.signature(Function_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_program_declaration_is_not_abstract():
    assert not inspect.isabstract(Program_Declaration)


def test_program_declaration_constructor_exists():
    assert callable(Program_Declaration.__init__)


def test_program_declaration_constructor_args():
    sig = inspect.signature(Program_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_library_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Library)


def test_iec61131_pous_library_constructor_exists():
    assert callable(iec61131_pous_Library.__init__)


def test_iec61131_pous_library_constructor_args():
    sig = inspect.signature(iec61131_pous_Library.__init__)
    params = list(sig.parameters.keys())



def test_program_access_decl_is_not_abstract():
    assert not inspect.isabstract(Program_Access_Decl)


def test_program_access_decl_constructor_exists():
    assert callable(Program_Access_Decl.__init__)


def test_program_access_decl_constructor_args():
    sig = inspect.signature(Program_Access_Decl.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_function_block_vars_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Function_Block_Vars)


def test_iec61131_pous_function_block_vars_constructor_exists():
    assert callable(iec61131_pous_Function_Block_Vars.__init__)


def test_iec61131_pous_function_block_vars_constructor_args():
    sig = inspect.signature(iec61131_pous_Function_Block_Vars.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_function_vars_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Function_Vars)


def test_iec61131_pous_function_vars_constructor_exists():
    assert callable(iec61131_pous_Function_Vars.__init__)


def test_iec61131_pous_function_vars_constructor_args():
    sig = inspect.signature(iec61131_pous_Function_Vars.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_program_vars_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Program_Vars)


def test_iec61131_pous_program_vars_constructor_exists():
    assert callable(iec61131_pous_Program_Vars.__init__)


def test_iec61131_pous_program_vars_constructor_args():
    sig = inspect.signature(iec61131_pous_Program_Vars.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_structure_elements_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Structure_Elements)


def test_iec61131_pous_structure_elements_constructor_exists():
    assert callable(iec61131_pous_Structure_Elements.__init__)


def test_iec61131_pous_structure_elements_constructor_args():
    sig = inspect.signature(iec61131_pous_Structure_Elements.__init__)
    params = list(sig.parameters.keys())



def test_structure_elements_is_not_abstract():
    assert not inspect.isabstract(Structure_Elements)


def test_structure_elements_constructor_exists():
    assert callable(Structure_Elements.__init__)


def test_structure_elements_constructor_args():
    sig = inspect.signature(Structure_Elements.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_structure_element_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Structure_Element_Declaration)


def test_iec61131_pous_structure_element_declaration_constructor_exists():
    assert callable(iec61131_pous_Structure_Element_Declaration.__init__)


def test_iec61131_pous_structure_element_declaration_constructor_args():
    sig = inspect.signature(iec61131_pous_Structure_Element_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_structure_element_declaration_is_not_abstract():
    assert not inspect.isabstract(Structure_Element_Declaration)


def test_structure_element_declaration_constructor_exists():
    assert callable(Structure_Element_Declaration.__init__)


def test_structure_element_declaration_constructor_args():
    sig = inspect.signature(Structure_Element_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_structure_specification_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Structure_Specification)


def test_iec61131_pous_structure_specification_constructor_exists():
    assert callable(iec61131_pous_Structure_Specification.__init__)


def test_iec61131_pous_structure_specification_constructor_args():
    sig = inspect.signature(iec61131_pous_Structure_Specification.__init__)
    params = list(sig.parameters.keys())



def test_enumerated_spec_init_is_not_abstract():
    assert not inspect.isabstract(Enumerated_Spec_Init)


def test_enumerated_spec_init_constructor_exists():
    assert callable(Enumerated_Spec_Init.__init__)


def test_enumerated_spec_init_constructor_args():
    sig = inspect.signature(Enumerated_Spec_Init.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_enumerated_type_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Enumerated_Type_Declaration)


def test_iec61131_pous_enumerated_type_declaration_constructor_exists():
    assert callable(iec61131_pous_Enumerated_Type_Declaration.__init__)


def test_iec61131_pous_enumerated_type_declaration_constructor_args():
    sig = inspect.signature(iec61131_pous_Enumerated_Type_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_subrange_spec_init_is_not_abstract():
    assert not inspect.isabstract(Subrange_Spec_Init)


def test_subrange_spec_init_constructor_exists():
    assert callable(Subrange_Spec_Init.__init__)


def test_subrange_spec_init_constructor_args():
    sig = inspect.signature(Subrange_Spec_Init.__init__)
    params = list(sig.parameters.keys())



def test_pous_function_block_body_is_not_abstract():
    assert not inspect.isabstract(pous_Function_Block_Body)


def test_pous_function_block_body_constructor_exists():
    assert callable(pous_Function_Block_Body.__init__)


def test_pous_function_block_body_constructor_args():
    sig = inspect.signature(pous_Function_Block_Body.__init__)
    params = list(sig.parameters.keys())



def test_pous_function_body_is_not_abstract():
    assert not inspect.isabstract(pous_Function_Body)


def test_pous_function_body_constructor_exists():
    assert callable(pous_Function_Body.__init__)


def test_pous_function_body_constructor_args():
    sig = inspect.signature(pous_Function_Body.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_ld_ladder_diagram_is_not_abstract():
    assert not inspect.isabstract(iec61131_ld_Ladder_Diagram)


def test_iec61131_ld_ladder_diagram_constructor_exists():
    assert callable(iec61131_ld_Ladder_Diagram.__init__)


def test_iec61131_ld_ladder_diagram_constructor_args():
    sig = inspect.signature(iec61131_ld_Ladder_Diagram.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_fbd_function_block_diagram_is_not_abstract():
    assert not inspect.isabstract(iec61131_fbd_Function_Block_Diagram)


def test_iec61131_fbd_function_block_diagram_constructor_exists():
    assert callable(iec61131_fbd_Function_Block_Diagram.__init__)


def test_iec61131_fbd_function_block_diagram_constructor_args():
    sig = inspect.signature(iec61131_fbd_Function_Block_Diagram.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_statement_list_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Statement_List)


def test_iec61131_st_statement_list_constructor_exists():
    assert callable(iec61131_st_Statement_List.__init__)


def test_iec61131_st_statement_list_constructor_args():
    sig = inspect.signature(iec61131_st_Statement_List.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_il_instruction_list_is_not_abstract():
    assert not inspect.isabstract(iec61131_il_Instruction_List)


def test_iec61131_il_instruction_list_constructor_exists():
    assert callable(iec61131_il_Instruction_List.__init__)


def test_iec61131_il_instruction_list_constructor_args():
    sig = inspect.signature(iec61131_il_Instruction_List.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_other_language_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Other_Language)


def test_iec61131_pous_other_language_constructor_exists():
    assert callable(iec61131_pous_Other_Language.__init__)


def test_iec61131_pous_other_language_constructor_args():
    sig = inspect.signature(iec61131_pous_Other_Language.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_iec61131_pous_other_language_has_text():
    assert hasattr(iec61131_pous_Other_Language, "text")
    descriptor = None
    for klass in iec61131_pous_Other_Language.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_iec61131_pous_function_body_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Function_Body)


def test_iec61131_pous_function_body_constructor_exists():
    assert callable(iec61131_pous_Function_Body.__init__)


def test_iec61131_pous_function_body_constructor_args():
    sig = inspect.signature(iec61131_pous_Function_Body.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_function_return_value_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Function_Return_Value)


def test_iec61131_pous_function_return_value_constructor_exists():
    assert callable(iec61131_pous_Function_Return_Value.__init__)


def test_iec61131_pous_function_return_value_constructor_args():
    sig = inspect.signature(iec61131_pous_Function_Return_Value.__init__)
    params = list(sig.parameters.keys())



def test_pous_function_name_is_not_abstract():
    assert not inspect.isabstract(pous_Function_Name)


def test_pous_function_name_constructor_exists():
    assert callable(pous_Function_Name.__init__)


def test_pous_function_name_constructor_args():
    sig = inspect.signature(pous_Function_Name.__init__)
    params = list(sig.parameters.keys())



def test_function_body_is_not_abstract():
    assert not inspect.isabstract(Function_Body)


def test_function_body_constructor_exists():
    assert callable(Function_Body.__init__)


def test_function_body_constructor_args():
    sig = inspect.signature(Function_Body.__init__)
    params = list(sig.parameters.keys())



def test_function_vars_is_not_abstract():
    assert not inspect.isabstract(Function_Vars)


def test_function_vars_constructor_exists():
    assert callable(Function_Vars.__init__)


def test_function_vars_constructor_args():
    sig = inspect.signature(Function_Vars.__init__)
    params = list(sig.parameters.keys())



def test_byte_string_type_name_is_not_abstract():
    assert not inspect.isabstract(Byte_String_Type_Name)


def test_byte_string_type_name_constructor_exists():
    assert callable(Byte_String_Type_Name.__init__)


def test_byte_string_type_name_constructor_args():
    sig = inspect.signature(Byte_String_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_double_byte_string_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_Double_Byte_String_Type_Name)


def test_iec61131_types_double_byte_string_type_name_constructor_exists():
    assert callable(iec61131_types_Double_Byte_String_Type_Name.__init__)


def test_iec61131_types_double_byte_string_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_Double_Byte_String_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_single_byte_string_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_Single_Byte_String_Type_Name)


def test_iec61131_types_single_byte_string_type_name_constructor_exists():
    assert callable(iec61131_types_Single_Byte_String_Type_Name.__init__)


def test_iec61131_types_single_byte_string_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_Single_Byte_String_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_string_type_name_is_not_abstract():
    assert not inspect.isabstract(String_Type_Name)


def test_string_type_name_constructor_exists():
    assert callable(String_Type_Name.__init__)


def test_string_type_name_constructor_args():
    sig = inspect.signature(String_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_structure_specification_is_not_abstract():
    assert not inspect.isabstract(Structure_Specification)


def test_structure_specification_constructor_exists():
    assert callable(Structure_Specification.__init__)


def test_structure_specification_constructor_args():
    sig = inspect.signature(Structure_Specification.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_structure_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Structure_Declaration)


def test_iec61131_pous_structure_declaration_constructor_exists():
    assert callable(iec61131_pous_Structure_Declaration.__init__)


def test_iec61131_pous_structure_declaration_constructor_args():
    sig = inspect.signature(iec61131_pous_Structure_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_type_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Type_Declaration)


def test_iec61131_pous_type_declaration_constructor_exists():
    assert callable(iec61131_pous_Type_Declaration.__init__)


def test_iec61131_pous_type_declaration_constructor_args():
    sig = inspect.signature(iec61131_pous_Type_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_type_declaration_is_not_abstract():
    assert not inspect.isabstract(Type_Declaration)


def test_type_declaration_constructor_exists():
    assert callable(Type_Declaration.__init__)


def test_type_declaration_constructor_args():
    sig = inspect.signature(Type_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_structure_type_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Structure_Type_Declaration)


def test_iec61131_pous_structure_type_declaration_constructor_exists():
    assert callable(iec61131_pous_Structure_Type_Declaration.__init__)


def test_iec61131_pous_structure_type_declaration_constructor_args():
    sig = inspect.signature(iec61131_pous_Structure_Type_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_array_type_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Array_Type_Declaration)


def test_iec61131_pous_array_type_declaration_constructor_exists():
    assert callable(iec61131_pous_Array_Type_Declaration.__init__)


def test_iec61131_pous_array_type_declaration_constructor_args():
    sig = inspect.signature(iec61131_pous_Array_Type_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_string_type_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_String_Type_Declaration)


def test_iec61131_pous_string_type_declaration_constructor_exists():
    assert callable(iec61131_pous_String_Type_Declaration.__init__)


def test_iec61131_pous_string_type_declaration_constructor_args():
    sig = inspect.signature(iec61131_pous_String_Type_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_single_element_type_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Single_Element_Type_Declaration)


def test_iec61131_pous_single_element_type_declaration_constructor_exists():
    assert callable(iec61131_pous_Single_Element_Type_Declaration.__init__)


def test_iec61131_pous_single_element_type_declaration_constructor_args():
    sig = inspect.signature(iec61131_pous_Single_Element_Type_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_access_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Access_Name)


def test_iec61131_pous_access_name_constructor_exists():
    assert callable(iec61131_pous_Access_Name.__init__)


def test_iec61131_pous_access_name_constructor_args():
    sig = inspect.signature(iec61131_pous_Access_Name.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iec61131_pous_access_name_has_name():
    assert hasattr(iec61131_pous_Access_Name, "name")
    descriptor = None
    for klass in iec61131_pous_Access_Name.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_symbolic_variable_is_not_abstract():
    assert not inspect.isabstract(Symbolic_Variable)


def test_symbolic_variable_constructor_exists():
    assert callable(Symbolic_Variable.__init__)


def test_symbolic_variable_constructor_args():
    sig = inspect.signature(Symbolic_Variable.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_variables_multi_element_variable_is_not_abstract():
    assert not inspect.isabstract(iec61131_variables_Multi_Element_Variable)


def test_iec61131_variables_multi_element_variable_constructor_exists():
    assert callable(iec61131_variables_Multi_Element_Variable.__init__)


def test_iec61131_variables_multi_element_variable_constructor_args():
    sig = inspect.signature(iec61131_variables_Multi_Element_Variable.__init__)
    params = list(sig.parameters.keys())



def test_access_name_is_not_abstract():
    assert not inspect.isabstract(Access_Name)


def test_access_name_constructor_exists():
    assert callable(Access_Name.__init__)


def test_access_name_constructor_args():
    sig = inspect.signature(Access_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_program_access_decl_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Program_Access_Decl)


def test_iec61131_pous_program_access_decl_constructor_exists():
    assert callable(iec61131_pous_Program_Access_Decl.__init__)


def test_iec61131_pous_program_access_decl_constructor_args():
    sig = inspect.signature(iec61131_pous_Program_Access_Decl.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_iec61131_pous_program_access_decl_has_direction():
    assert hasattr(iec61131_pous_Program_Access_Decl, "direction")
    descriptor = None
    for klass in iec61131_pous_Program_Access_Decl.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_iec61131_pous_function_block_body_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Function_Block_Body)


def test_iec61131_pous_function_block_body_constructor_exists():
    assert callable(iec61131_pous_Function_Block_Body.__init__)


def test_iec61131_pous_function_block_body_constructor_args():
    sig = inspect.signature(iec61131_pous_Function_Block_Body.__init__)
    params = list(sig.parameters.keys())



def test_program_type_name_is_not_abstract():
    assert not inspect.isabstract(Program_Type_Name)


def test_program_type_name_constructor_exists():
    assert callable(Program_Type_Name.__init__)


def test_program_type_name_constructor_args():
    sig = inspect.signature(Program_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_function_return_value_is_not_abstract():
    assert not inspect.isabstract(Function_Return_Value)


def test_function_return_value_constructor_exists():
    assert callable(Function_Return_Value.__init__)


def test_function_return_value_constructor_args():
    sig = inspect.signature(Function_Return_Value.__init__)
    params = list(sig.parameters.keys())



def test_derived_function_name_is_not_abstract():
    assert not inspect.isabstract(Derived_Function_Name)


def test_derived_function_name_constructor_exists():
    assert callable(Derived_Function_Name.__init__)


def test_derived_function_name_constructor_args():
    sig = inspect.signature(Derived_Function_Name.__init__)
    params = list(sig.parameters.keys())



def test_function_block_vars_is_not_abstract():
    assert not inspect.isabstract(Function_Block_Vars)


def test_function_block_vars_constructor_exists():
    assert callable(Function_Block_Vars.__init__)


def test_function_block_vars_constructor_args():
    sig = inspect.signature(Function_Block_Vars.__init__)
    params = list(sig.parameters.keys())



def test_derived_function_block_name_is_not_abstract():
    assert not inspect.isabstract(Derived_Function_Block_Name)


def test_derived_function_block_name_constructor_exists():
    assert callable(Derived_Function_Block_Name.__init__)


def test_derived_function_block_name_constructor_args():
    sig = inspect.signature(Derived_Function_Block_Name.__init__)
    params = list(sig.parameters.keys())



def test_pous_function_block_type_name_is_not_abstract():
    assert not inspect.isabstract(pous_Function_Block_Type_Name)


def test_pous_function_block_type_name_constructor_exists():
    assert callable(pous_Function_Block_Type_Name.__init__)


def test_pous_function_block_type_name_constructor_args():
    sig = inspect.signature(pous_Function_Block_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_types_simple_specification_is_not_abstract():
    assert not inspect.isabstract(types_Simple_Specification)


def test_types_simple_specification_constructor_exists():
    assert callable(types_Simple_Specification.__init__)


def test_types_simple_specification_constructor_args():
    sig = inspect.signature(types_Simple_Specification.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_generic_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_Generic_Type_Name)


def test_iec61131_types_generic_type_name_constructor_exists():
    assert callable(iec61131_types_Generic_Type_Name.__init__)


def test_iec61131_types_generic_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_Generic_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_elementary_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_Elementary_Type_Name)


def test_iec61131_types_elementary_type_name_constructor_exists():
    assert callable(iec61131_types_Elementary_Type_Name.__init__)


def test_iec61131_types_elementary_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_Elementary_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_simple_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_Simple_Type_Name)


def test_iec61131_types_simple_type_name_constructor_exists():
    assert callable(iec61131_types_Simple_Type_Name.__init__)


def test_iec61131_types_simple_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_Simple_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_blocks_is_not_abstract():
    assert not inspect.isabstract(Blocks)


def test_blocks_constructor_exists():
    assert callable(Blocks.__init__)


def test_blocks_constructor_args():
    sig = inspect.signature(Blocks.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_derived_function_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Derived_Function_Name)


def test_iec61131_pous_derived_function_name_constructor_exists():
    assert callable(iec61131_pous_Derived_Function_Name.__init__)


def test_iec61131_pous_derived_function_name_constructor_args():
    sig = inspect.signature(iec61131_pous_Derived_Function_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_derived_function_block_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Derived_Function_Block_Name)


def test_iec61131_pous_derived_function_block_name_constructor_exists():
    assert callable(iec61131_pous_Derived_Function_Block_Name.__init__)


def test_iec61131_pous_derived_function_block_name_constructor_args():
    sig = inspect.signature(iec61131_pous_Derived_Function_Block_Name.__init__)
    params = list(sig.parameters.keys())



def test_function_block_body_is_not_abstract():
    assert not inspect.isabstract(Function_Block_Body)


def test_function_block_body_constructor_exists():
    assert callable(Function_Block_Body.__init__)


def test_function_block_body_constructor_args():
    sig = inspect.signature(Function_Block_Body.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_sfc_sequential_function_chart_is_not_abstract():
    assert not inspect.isabstract(iec61131_sfc_Sequential_Function_Chart)


def test_iec61131_sfc_sequential_function_chart_constructor_exists():
    assert callable(iec61131_sfc_Sequential_Function_Chart.__init__)


def test_iec61131_sfc_sequential_function_chart_constructor_args():
    sig = inspect.signature(iec61131_sfc_Sequential_Function_Chart.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_simple_specification_func_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Simple_Specification_Func)


def test_iec61131_interfaces_simple_specification_func_constructor_exists():
    assert callable(iec61131_interfaces_Simple_Specification_Func.__init__)


def test_iec61131_interfaces_simple_specification_func_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Simple_Specification_Func.__init__)
    params = list(sig.parameters.keys())



def test_simple_specification_func_is_not_abstract():
    assert not inspect.isabstract(Simple_Specification_Func)


def test_simple_specification_func_constructor_exists():
    assert callable(Simple_Specification_Func.__init__)


def test_simple_specification_func_constructor_args():
    sig = inspect.signature(Simple_Specification_Func.__init__)
    params = list(sig.parameters.keys())



def test_var1_specification_func_is_not_abstract():
    assert not inspect.isabstract(Var1_Specification_Func)


def test_var1_specification_func_constructor_exists():
    assert callable(Var1_Specification_Func.__init__)


def test_var1_specification_func_constructor_args():
    sig = inspect.signature(Var1_Specification_Func.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_simple_spec_init_func_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Simple_Spec_Init_Func)


def test_iec61131_interfaces_simple_spec_init_func_constructor_exists():
    assert callable(iec61131_interfaces_Simple_Spec_Init_Func.__init__)


def test_iec61131_interfaces_simple_spec_init_func_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Simple_Spec_Init_Func.__init__)
    params = list(sig.parameters.keys())



def test_simple_spec_init_is_not_abstract():
    assert not inspect.isabstract(Simple_Spec_Init)


def test_simple_spec_init_constructor_exists():
    assert callable(Simple_Spec_Init.__init__)


def test_simple_spec_init_constructor_args():
    sig = inspect.signature(Simple_Spec_Init.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_var_name_decl_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Var_Name_Decl)


def test_iec61131_interfaces_var_name_decl_constructor_exists():
    assert callable(iec61131_interfaces_Var_Name_Decl.__init__)


def test_iec61131_interfaces_var_name_decl_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Var_Name_Decl.__init__)
    params = list(sig.parameters.keys())



def test_array_type_name_is_not_abstract():
    assert not inspect.isabstract(Array_Type_Name)


def test_array_type_name_constructor_exists():
    assert callable(Array_Type_Name.__init__)


def test_array_type_name_constructor_args():
    sig = inspect.signature(Array_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_initial_element_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Initial_Element)


def test_iec61131_interfaces_initial_element_constructor_exists():
    assert callable(iec61131_interfaces_Initial_Element.__init__)


def test_iec61131_interfaces_initial_element_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Initial_Element.__init__)
    params = list(sig.parameters.keys())



def test_non_generic_type_name_is_not_abstract():
    assert not inspect.isabstract(Non_Generic_Type_Name)


def test_non_generic_type_name_constructor_exists():
    assert callable(Non_Generic_Type_Name.__init__)


def test_non_generic_type_name_constructor_args():
    sig = inspect.signature(Non_Generic_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_derived_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_Derived_Type_Name)


def test_iec61131_types_derived_type_name_constructor_exists():
    assert callable(iec61131_types_Derived_Type_Name.__init__)


def test_iec61131_types_derived_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_Derived_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_global_var_decl_is_not_abstract():
    assert not inspect.isabstract(Global_Var_Decl)


def test_global_var_decl_constructor_exists():
    assert callable(Global_Var_Decl.__init__)


def test_global_var_decl_constructor_args():
    sig = inspect.signature(Global_Var_Decl.__init__)
    params = list(sig.parameters.keys())



def test_library_element_declaration_is_not_abstract():
    assert not inspect.isabstract(Library_Element_Declaration)


def test_library_element_declaration_constructor_exists():
    assert callable(Library_Element_Declaration.__init__)


def test_library_element_declaration_constructor_args():
    sig = inspect.signature(Library_Element_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_configuration_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Configuration_Declaration)


def test_iec61131_configurations_configuration_declaration_constructor_exists():
    assert callable(iec61131_configurations_Configuration_Declaration.__init__)


def test_iec61131_configurations_configuration_declaration_constructor_args():
    sig = inspect.signature(iec61131_configurations_Configuration_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_data_type_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Data_Type_Declaration)


def test_iec61131_pous_data_type_declaration_constructor_exists():
    assert callable(iec61131_pous_Data_Type_Declaration.__init__)


def test_iec61131_pous_data_type_declaration_constructor_args():
    sig = inspect.signature(iec61131_pous_Data_Type_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_program_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Program_Declaration)


def test_iec61131_pous_program_declaration_constructor_exists():
    assert callable(iec61131_pous_Program_Declaration.__init__)


def test_iec61131_pous_program_declaration_constructor_args():
    sig = inspect.signature(iec61131_pous_Program_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_function_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Function_Declaration)


def test_iec61131_pous_function_declaration_constructor_exists():
    assert callable(iec61131_pous_Function_Declaration.__init__)


def test_iec61131_pous_function_declaration_constructor_args():
    sig = inspect.signature(iec61131_pous_Function_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_function_block_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Function_Block_Declaration)


def test_iec61131_pous_function_block_declaration_constructor_exists():
    assert callable(iec61131_pous_Function_Block_Declaration.__init__)


def test_iec61131_pous_function_block_declaration_constructor_args():
    sig = inspect.signature(iec61131_pous_Function_Block_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_resource_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Resource_Declaration)


def test_iec61131_configurations_resource_declaration_constructor_exists():
    assert callable(iec61131_configurations_Resource_Declaration.__init__)


def test_iec61131_configurations_resource_declaration_constructor_args():
    sig = inspect.signature(iec61131_configurations_Resource_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_global_var_declarations_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Global_Var_Declarations)


def test_iec61131_interfaces_global_var_declarations_constructor_exists():
    assert callable(iec61131_interfaces_Global_Var_Declarations.__init__)


def test_iec61131_interfaces_global_var_declarations_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Global_Var_Declarations.__init__)
    params = list(sig.parameters.keys())
    assert "retain" in params, "Missing parameter 'retain'"
    assert "constant" in params, "Missing parameter 'constant'"

def test_iec61131_interfaces_global_var_declarations_has_retain():
    assert hasattr(iec61131_interfaces_Global_Var_Declarations, "retain")
    descriptor = None
    for klass in iec61131_interfaces_Global_Var_Declarations.__mro__:
        if "retain" in klass.__dict__:
            descriptor = klass.__dict__["retain"]
            break
    assert isinstance(descriptor, property)

def test_iec61131_interfaces_global_var_declarations_has_constant():
    assert hasattr(iec61131_interfaces_Global_Var_Declarations, "constant")
    descriptor = None
    for klass in iec61131_interfaces_Global_Var_Declarations.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_located_var_decl_is_not_abstract():
    assert not inspect.isabstract(Located_Var_Decl)


def test_located_var_decl_constructor_exists():
    assert callable(Located_Var_Decl.__init__)


def test_located_var_decl_constructor_args():
    sig = inspect.signature(Located_Var_Decl.__init__)
    params = list(sig.parameters.keys())



def test_program_vars_is_not_abstract():
    assert not inspect.isabstract(Program_Vars)


def test_program_vars_constructor_exists():
    assert callable(Program_Vars.__init__)


def test_program_vars_constructor_args():
    sig = inspect.signature(Program_Vars.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_program_access_decls_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Program_Access_Decls)


def test_iec61131_pous_program_access_decls_constructor_exists():
    assert callable(iec61131_pous_Program_Access_Decls.__init__)


def test_iec61131_pous_program_access_decls_constructor_args():
    sig = inspect.signature(iec61131_pous_Program_Access_Decls.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_located_var_declarations_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Located_Var_Declarations)


def test_iec61131_interfaces_located_var_declarations_constructor_exists():
    assert callable(iec61131_interfaces_Located_Var_Declarations.__init__)


def test_iec61131_interfaces_located_var_declarations_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Located_Var_Declarations.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"
    assert "retain" in params, "Missing parameter 'retain'"

def test_iec61131_interfaces_located_var_declarations_has_constant():
    assert hasattr(iec61131_interfaces_Located_Var_Declarations, "constant")
    descriptor = None
    for klass in iec61131_interfaces_Located_Var_Declarations.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)

def test_iec61131_interfaces_located_var_declarations_has_retain():
    assert hasattr(iec61131_interfaces_Located_Var_Declarations, "retain")
    descriptor = None
    for klass in iec61131_interfaces_Located_Var_Declarations.__mro__:
        if "retain" in klass.__dict__:
            descriptor = klass.__dict__["retain"]
            break
    assert isinstance(descriptor, property)



def test_subrange_type_name_is_not_abstract():
    assert not inspect.isabstract(Subrange_Type_Name)


def test_subrange_type_name_constructor_exists():
    assert callable(Subrange_Type_Name.__init__)


def test_subrange_type_name_constructor_args():
    sig = inspect.signature(Subrange_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_subrange_is_not_abstract():
    assert not inspect.isabstract(Subrange)


def test_subrange_constructor_exists():
    assert callable(Subrange.__init__)


def test_subrange_constructor_args():
    sig = inspect.signature(Subrange.__init__)
    params = list(sig.parameters.keys())



def test_double_byte_string_type_name_is_not_abstract():
    assert not inspect.isabstract(Double_Byte_String_Type_Name)


def test_double_byte_string_type_name_constructor_exists():
    assert callable(Double_Byte_String_Type_Name.__init__)


def test_double_byte_string_type_name_constructor_args():
    sig = inspect.signature(Double_Byte_String_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_single_byte_string_type_name_is_not_abstract():
    assert not inspect.isabstract(Single_Byte_String_Type_Name)


def test_single_byte_string_type_name_constructor_exists():
    assert callable(Single_Byte_String_Type_Name.__init__)


def test_single_byte_string_type_name_constructor_args():
    sig = inspect.signature(Single_Byte_String_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_byte_string_is_not_abstract():
    assert not inspect.isabstract(Byte_String)


def test_byte_string_constructor_exists():
    assert callable(Byte_String.__init__)


def test_byte_string_constructor_args():
    sig = inspect.signature(Byte_String.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_double_bstring_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Double_BString)


def test_iec61131_interfaces_double_bstring_constructor_exists():
    assert callable(iec61131_interfaces_Double_BString.__init__)


def test_iec61131_interfaces_double_bstring_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Double_BString.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_single_bstring_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Single_BString)


def test_iec61131_interfaces_single_bstring_constructor_exists():
    assert callable(iec61131_interfaces_Single_BString.__init__)


def test_iec61131_interfaces_single_bstring_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Single_BString.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_range_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Range)


def test_iec61131_interfaces_range_constructor_exists():
    assert callable(iec61131_interfaces_Range.__init__)


def test_iec61131_interfaces_range_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Range.__init__)
    params = list(sig.parameters.keys())



def test_initialized_structure_is_not_abstract():
    assert not inspect.isabstract(Initialized_Structure)


def test_initialized_structure_constructor_exists():
    assert callable(Initialized_Structure.__init__)


def test_initialized_structure_constructor_args():
    sig = inspect.signature(Initialized_Structure.__init__)
    params = list(sig.parameters.keys())



def test_array_spec_init_is_not_abstract():
    assert not inspect.isabstract(Array_Spec_Init)


def test_array_spec_init_constructor_exists():
    assert callable(Array_Spec_Init.__init__)


def test_array_spec_init_constructor_args():
    sig = inspect.signature(Array_Spec_Init.__init__)
    params = list(sig.parameters.keys())



def test_var2_init_decl_is_not_abstract():
    assert not inspect.isabstract(Var2_Init_Decl)


def test_var2_init_decl_constructor_exists():
    assert callable(Var2_Init_Decl.__init__)


def test_var2_init_decl_constructor_args():
    sig = inspect.signature(Var2_Init_Decl.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_var_init_decl_func_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Var_Init_Decl_Func)


def test_iec61131_interfaces_var_init_decl_func_constructor_exists():
    assert callable(iec61131_interfaces_Var_Init_Decl_Func.__init__)


def test_iec61131_interfaces_var_init_decl_func_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Var_Init_Decl_Func.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_structured_var_init_decl_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Structured_Var_Init_Decl)


def test_iec61131_interfaces_structured_var_init_decl_constructor_exists():
    assert callable(iec61131_interfaces_Structured_Var_Init_Decl.__init__)


def test_iec61131_interfaces_structured_var_init_decl_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Structured_Var_Init_Decl.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_array_var_init_decl_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Array_Var_Init_Decl)


def test_iec61131_interfaces_array_var_init_decl_constructor_exists():
    assert callable(iec61131_interfaces_Array_Var_Init_Decl.__init__)


def test_iec61131_interfaces_array_var_init_decl_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Array_Var_Init_Decl.__init__)
    params = list(sig.parameters.keys())



def test_enumerated_value_is_not_abstract():
    assert not inspect.isabstract(Enumerated_Value)


def test_enumerated_value_constructor_exists():
    assert callable(Enumerated_Value.__init__)


def test_enumerated_value_constructor_args():
    sig = inspect.signature(Enumerated_Value.__init__)
    params = list(sig.parameters.keys())



def test_enumerated_specification_is_not_abstract():
    assert not inspect.isabstract(Enumerated_Specification)


def test_enumerated_specification_constructor_exists():
    assert callable(Enumerated_Specification.__init__)


def test_enumerated_specification_constructor_args():
    sig = inspect.signature(Enumerated_Specification.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_enumerated_specification1_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Enumerated_Specification1)


def test_iec61131_interfaces_enumerated_specification1_constructor_exists():
    assert callable(iec61131_interfaces_Enumerated_Specification1.__init__)


def test_iec61131_interfaces_enumerated_specification1_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Enumerated_Specification1.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_enumerated_specification2_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Enumerated_Specification2)


def test_iec61131_interfaces_enumerated_specification2_constructor_exists():
    assert callable(iec61131_interfaces_Enumerated_Specification2.__init__)


def test_iec61131_interfaces_enumerated_specification2_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Enumerated_Specification2.__init__)
    params = list(sig.parameters.keys())



def test_signed_integer_is_not_abstract():
    assert not inspect.isabstract(Signed_Integer)


def test_signed_integer_constructor_exists():
    assert callable(Signed_Integer.__init__)


def test_signed_integer_constructor_args():
    sig = inspect.signature(Signed_Integer.__init__)
    params = list(sig.parameters.keys())



def test_subrange_specification_is_not_abstract():
    assert not inspect.isabstract(Subrange_Specification)


def test_subrange_specification_constructor_exists():
    assert callable(Subrange_Specification.__init__)


def test_subrange_specification_constructor_args():
    sig = inspect.signature(Subrange_Specification.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_subrange_specification2_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Subrange_Specification2)


def test_iec61131_interfaces_subrange_specification2_constructor_exists():
    assert callable(iec61131_interfaces_Subrange_Specification2.__init__)


def test_iec61131_interfaces_subrange_specification2_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Subrange_Specification2.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_subrange_specification1_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Subrange_Specification1)


def test_iec61131_interfaces_subrange_specification1_constructor_exists():
    assert callable(iec61131_interfaces_Subrange_Specification1.__init__)


def test_iec61131_interfaces_subrange_specification1_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Subrange_Specification1.__init__)
    params = list(sig.parameters.keys())



def test_interfaces_var1_specification_func_is_not_abstract():
    assert not inspect.isabstract(interfaces_Var1_Specification_Func)


def test_interfaces_var1_specification_func_constructor_exists():
    assert callable(interfaces_Var1_Specification_Func.__init__)


def test_interfaces_var1_specification_func_constructor_args():
    sig = inspect.signature(interfaces_Var1_Specification_Func.__init__)
    params = list(sig.parameters.keys())



def test_simple_specification_is_not_abstract():
    assert not inspect.isabstract(Simple_Specification)


def test_simple_specification_constructor_exists():
    assert callable(Simple_Specification.__init__)


def test_simple_specification_constructor_args():
    sig = inspect.signature(Simple_Specification.__init__)
    params = list(sig.parameters.keys())



def test_pous_structure_elements_is_not_abstract():
    assert not inspect.isabstract(pous_Structure_Elements)


def test_pous_structure_elements_constructor_exists():
    assert callable(pous_Structure_Elements.__init__)


def test_pous_structure_elements_constructor_args():
    sig = inspect.signature(pous_Structure_Elements.__init__)
    params = list(sig.parameters.keys())



def test_interfaces_located_var_spec_init_is_not_abstract():
    assert not inspect.isabstract(interfaces_Located_Var_Spec_Init)


def test_interfaces_located_var_spec_init_constructor_exists():
    assert callable(interfaces_Located_Var_Spec_Init.__init__)


def test_interfaces_located_var_spec_init_constructor_args():
    sig = inspect.signature(interfaces_Located_Var_Spec_Init.__init__)
    params = list(sig.parameters.keys())



def test_interfaces_var1_specification_is_not_abstract():
    assert not inspect.isabstract(interfaces_Var1_Specification)


def test_interfaces_var1_specification_constructor_exists():
    assert callable(interfaces_Var1_Specification.__init__)


def test_interfaces_var1_specification_constructor_args():
    sig = inspect.signature(interfaces_Var1_Specification.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_subrange_spec_init_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Subrange_Spec_Init)


def test_iec61131_interfaces_subrange_spec_init_constructor_exists():
    assert callable(iec61131_interfaces_Subrange_Spec_Init.__init__)


def test_iec61131_interfaces_subrange_spec_init_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Subrange_Spec_Init.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_enumerated_spec_init_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Enumerated_Spec_Init)


def test_iec61131_interfaces_enumerated_spec_init_constructor_exists():
    assert callable(iec61131_interfaces_Enumerated_Spec_Init.__init__)


def test_iec61131_interfaces_enumerated_spec_init_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Enumerated_Spec_Init.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_simple_spec_init_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Simple_Spec_Init)


def test_iec61131_interfaces_simple_spec_init_constructor_exists():
    assert callable(iec61131_interfaces_Simple_Spec_Init.__init__)


def test_iec61131_interfaces_simple_spec_init_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Simple_Spec_Init.__init__)
    params = list(sig.parameters.keys())



def test_assignment_symbol_is_not_abstract():
    assert not inspect.isabstract(Assignment_Symbol)


def test_assignment_symbol_constructor_exists():
    assert callable(Assignment_Symbol.__init__)


def test_assignment_symbol_constructor_args():
    sig = inspect.signature(Assignment_Symbol.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_var1_specification_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Var1_Specification)


def test_iec61131_interfaces_var1_specification_constructor_exists():
    assert callable(iec61131_interfaces_Var1_Specification.__init__)


def test_iec61131_interfaces_var1_specification_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Var1_Specification.__init__)
    params = list(sig.parameters.keys())



def test_bool_type_name_is_not_abstract():
    assert not inspect.isabstract(Bool_Type_Name)


def test_bool_type_name_constructor_exists():
    assert callable(Bool_Type_Name.__init__)


def test_bool_type_name_constructor_args():
    sig = inspect.signature(Bool_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_operators_divide_operator_is_not_abstract():
    assert not inspect.isabstract(operators_Divide_Operator)


def test_operators_divide_operator_constructor_exists():
    assert callable(operators_Divide_Operator.__init__)


def test_operators_divide_operator_constructor_args():
    sig = inspect.signature(operators_Divide_Operator.__init__)
    params = list(sig.parameters.keys())



def test_multiply_operator_is_not_abstract():
    assert not inspect.isabstract(Multiply_Operator)


def test_multiply_operator_constructor_exists():
    assert callable(Multiply_Operator.__init__)


def test_multiply_operator_constructor_args():
    sig = inspect.signature(Multiply_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_multiply_symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Multiply_Symbol)


def test_iec61131_operators_multiply_symbol_constructor_exists():
    assert callable(iec61131_operators_Multiply_Symbol.__init__)


def test_iec61131_operators_multiply_symbol_constructor_args():
    sig = inspect.signature(iec61131_operators_Multiply_Symbol.__init__)
    params = list(sig.parameters.keys())



def test_operators_multiply_operator_is_not_abstract():
    assert not inspect.isabstract(operators_Multiply_Operator)


def test_operators_multiply_operator_constructor_exists():
    assert callable(operators_Multiply_Operator.__init__)


def test_operators_multiply_operator_constructor_args():
    sig = inspect.signature(operators_Multiply_Operator.__init__)
    params = list(sig.parameters.keys())



def test_operators_add_operator_is_not_abstract():
    assert not inspect.isabstract(operators_Add_Operator)


def test_operators_add_operator_constructor_exists():
    assert callable(operators_Add_Operator.__init__)


def test_operators_add_operator_constructor_args():
    sig = inspect.signature(operators_Add_Operator.__init__)
    params = list(sig.parameters.keys())



def test_operators_arithmetic_name_is_not_abstract():
    assert not inspect.isabstract(operators_Arithmetic_Name)


def test_operators_arithmetic_name_constructor_exists():
    assert callable(operators_Arithmetic_Name.__init__)


def test_operators_arithmetic_name_constructor_args():
    sig = inspect.signature(operators_Arithmetic_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_divide_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Divide_Name)


def test_iec61131_operators_divide_name_constructor_exists():
    assert callable(iec61131_operators_Divide_Name.__init__)


def test_iec61131_operators_divide_name_constructor_args():
    sig = inspect.signature(iec61131_operators_Divide_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_multiply_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Multiply_Name)


def test_iec61131_operators_multiply_name_constructor_exists():
    assert callable(iec61131_operators_Multiply_Name.__init__)


def test_iec61131_operators_multiply_name_constructor_args():
    sig = inspect.signature(iec61131_operators_Multiply_Name.__init__)
    params = list(sig.parameters.keys())



def test_operators_addition_operator_is_not_abstract():
    assert not inspect.isabstract(operators_Addition_Operator)


def test_operators_addition_operator_constructor_exists():
    assert callable(operators_Addition_Operator.__init__)


def test_operators_addition_operator_constructor_args():
    sig = inspect.signature(operators_Addition_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_addition_symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Addition_Symbol)


def test_iec61131_operators_addition_symbol_constructor_exists():
    assert callable(iec61131_operators_Addition_Symbol.__init__)


def test_iec61131_operators_addition_symbol_constructor_args():
    sig = inspect.signature(iec61131_operators_Addition_Symbol.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_addition_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Addition_Name)


def test_iec61131_operators_addition_name_constructor_exists():
    assert callable(iec61131_operators_Addition_Name.__init__)


def test_iec61131_operators_addition_name_constructor_args():
    sig = inspect.signature(iec61131_operators_Addition_Name.__init__)
    params = list(sig.parameters.keys())



def test_comparison_operator_is_not_abstract():
    assert not inspect.isabstract(Comparison_Operator)


def test_comparison_operator_constructor_exists():
    assert callable(Comparison_Operator.__init__)


def test_comparison_operator_constructor_args():
    sig = inspect.signature(Comparison_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_lessequal_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_LessEqual_Operator)


def test_iec61131_operators_lessequal_operator_constructor_exists():
    assert callable(iec61131_operators_LessEqual_Operator.__init__)


def test_iec61131_operators_lessequal_operator_constructor_args():
    sig = inspect.signature(iec61131_operators_LessEqual_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_greaterequal_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_GreaterEqual_Operator)


def test_iec61131_operators_greaterequal_operator_constructor_exists():
    assert callable(iec61131_operators_GreaterEqual_Operator.__init__)


def test_iec61131_operators_greaterequal_operator_constructor_args():
    sig = inspect.signature(iec61131_operators_GreaterEqual_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_greater_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Greater_Operator)


def test_iec61131_operators_greater_operator_constructor_exists():
    assert callable(iec61131_operators_Greater_Operator.__init__)


def test_iec61131_operators_greater_operator_constructor_args():
    sig = inspect.signature(iec61131_operators_Greater_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_less_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Less_Operator)


def test_iec61131_operators_less_operator_constructor_exists():
    assert callable(iec61131_operators_Less_Operator.__init__)


def test_iec61131_operators_less_operator_constructor_args():
    sig = inspect.signature(iec61131_operators_Less_Operator.__init__)
    params = list(sig.parameters.keys())



def test_il_expr_operator_is_not_abstract():
    assert not inspect.isabstract(Il_Expr_Operator)


def test_il_expr_operator_constructor_exists():
    assert callable(Il_Expr_Operator.__init__)


def test_il_expr_operator_constructor_args():
    sig = inspect.signature(Il_Expr_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_arithmetic_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Arithmetic_Name)


def test_iec61131_operators_arithmetic_name_constructor_exists():
    assert callable(iec61131_operators_Arithmetic_Name.__init__)


def test_iec61131_operators_arithmetic_name_constructor_args():
    sig = inspect.signature(iec61131_operators_Arithmetic_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_comparison_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Comparison_Name)


def test_iec61131_operators_comparison_name_constructor_exists():
    assert callable(iec61131_operators_Comparison_Name.__init__)


def test_iec61131_operators_comparison_name_constructor_args():
    sig = inspect.signature(iec61131_operators_Comparison_Name.__init__)
    params = list(sig.parameters.keys())



def test_operators_substraction_operator_is_not_abstract():
    assert not inspect.isabstract(operators_Substraction_Operator)


def test_operators_substraction_operator_constructor_exists():
    assert callable(operators_Substraction_Operator.__init__)


def test_operators_substraction_operator_constructor_args():
    sig = inspect.signature(operators_Substraction_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_substraction_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Substraction_Name)


def test_iec61131_operators_substraction_name_constructor_exists():
    assert callable(iec61131_operators_Substraction_Name.__init__)


def test_iec61131_operators_substraction_name_constructor_args():
    sig = inspect.signature(iec61131_operators_Substraction_Name.__init__)
    params = list(sig.parameters.keys())



def test_greaterequal_operator_is_not_abstract():
    assert not inspect.isabstract(GreaterEqual_Operator)


def test_greaterequal_operator_constructor_exists():
    assert callable(GreaterEqual_Operator.__init__)


def test_greaterequal_operator_constructor_args():
    sig = inspect.signature(GreaterEqual_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_greaterequal_symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_GreaterEqual_Symbol)


def test_iec61131_operators_greaterequal_symbol_constructor_exists():
    assert callable(iec61131_operators_GreaterEqual_Symbol.__init__)


def test_iec61131_operators_greaterequal_symbol_constructor_args():
    sig = inspect.signature(iec61131_operators_GreaterEqual_Symbol.__init__)
    params = list(sig.parameters.keys())



def test_operators_greaterequal_operator_is_not_abstract():
    assert not inspect.isabstract(operators_GreaterEqual_Operator)


def test_operators_greaterequal_operator_constructor_exists():
    assert callable(operators_GreaterEqual_Operator.__init__)


def test_operators_greaterequal_operator_constructor_args():
    sig = inspect.signature(operators_GreaterEqual_Operator.__init__)
    params = list(sig.parameters.keys())



def test_greater_operator_is_not_abstract():
    assert not inspect.isabstract(Greater_Operator)


def test_greater_operator_constructor_exists():
    assert callable(Greater_Operator.__init__)


def test_greater_operator_constructor_args():
    sig = inspect.signature(Greater_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_greater_symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Greater_Symbol)


def test_iec61131_operators_greater_symbol_constructor_exists():
    assert callable(iec61131_operators_Greater_Symbol.__init__)


def test_iec61131_operators_greater_symbol_constructor_args():
    sig = inspect.signature(iec61131_operators_Greater_Symbol.__init__)
    params = list(sig.parameters.keys())



def test_operators_greater_operator_is_not_abstract():
    assert not inspect.isabstract(operators_Greater_Operator)


def test_operators_greater_operator_constructor_exists():
    assert callable(operators_Greater_Operator.__init__)


def test_operators_greater_operator_constructor_args():
    sig = inspect.signature(operators_Greater_Operator.__init__)
    params = list(sig.parameters.keys())



def test_lessequal_operator_is_not_abstract():
    assert not inspect.isabstract(LessEqual_Operator)


def test_lessequal_operator_constructor_exists():
    assert callable(LessEqual_Operator.__init__)


def test_lessequal_operator_constructor_args():
    sig = inspect.signature(LessEqual_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_lessequal_symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_LessEqual_Symbol)


def test_iec61131_operators_lessequal_symbol_constructor_exists():
    assert callable(iec61131_operators_LessEqual_Symbol.__init__)


def test_iec61131_operators_lessequal_symbol_constructor_args():
    sig = inspect.signature(iec61131_operators_LessEqual_Symbol.__init__)
    params = list(sig.parameters.keys())



def test_operators_lessequal_operator_is_not_abstract():
    assert not inspect.isabstract(operators_LessEqual_Operator)


def test_operators_lessequal_operator_constructor_exists():
    assert callable(operators_LessEqual_Operator.__init__)


def test_operators_lessequal_operator_constructor_args():
    sig = inspect.signature(operators_LessEqual_Operator.__init__)
    params = list(sig.parameters.keys())



def test_less_operator_is_not_abstract():
    assert not inspect.isabstract(Less_Operator)


def test_less_operator_constructor_exists():
    assert callable(Less_Operator.__init__)


def test_less_operator_constructor_args():
    sig = inspect.signature(Less_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_less_symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Less_Symbol)


def test_iec61131_operators_less_symbol_constructor_exists():
    assert callable(iec61131_operators_Less_Symbol.__init__)


def test_iec61131_operators_less_symbol_constructor_args():
    sig = inspect.signature(iec61131_operators_Less_Symbol.__init__)
    params = list(sig.parameters.keys())



def test_operators_less_operator_is_not_abstract():
    assert not inspect.isabstract(operators_Less_Operator)


def test_operators_less_operator_constructor_exists():
    assert callable(operators_Less_Operator.__init__)


def test_operators_less_operator_constructor_args():
    sig = inspect.signature(operators_Less_Operator.__init__)
    params = list(sig.parameters.keys())



def test_unequal_operator_is_not_abstract():
    assert not inspect.isabstract(Unequal_Operator)


def test_unequal_operator_constructor_exists():
    assert callable(Unequal_Operator.__init__)


def test_unequal_operator_constructor_args():
    sig = inspect.signature(Unequal_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_unequal_symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Unequal_Symbol)


def test_iec61131_operators_unequal_symbol_constructor_exists():
    assert callable(iec61131_operators_Unequal_Symbol.__init__)


def test_iec61131_operators_unequal_symbol_constructor_args():
    sig = inspect.signature(iec61131_operators_Unequal_Symbol.__init__)
    params = list(sig.parameters.keys())



def test_operators_unequal_operator_is_not_abstract():
    assert not inspect.isabstract(operators_Unequal_Operator)


def test_operators_unequal_operator_constructor_exists():
    assert callable(operators_Unequal_Operator.__init__)


def test_operators_unequal_operator_constructor_args():
    sig = inspect.signature(operators_Unequal_Operator.__init__)
    params = list(sig.parameters.keys())



def test_equal_operator_is_not_abstract():
    assert not inspect.isabstract(Equal_Operator)


def test_equal_operator_constructor_exists():
    assert callable(Equal_Operator.__init__)


def test_equal_operator_constructor_args():
    sig = inspect.signature(Equal_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_equal_symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Equal_Symbol)


def test_iec61131_operators_equal_symbol_constructor_exists():
    assert callable(iec61131_operators_Equal_Symbol.__init__)


def test_iec61131_operators_equal_symbol_constructor_args():
    sig = inspect.signature(iec61131_operators_Equal_Symbol.__init__)
    params = list(sig.parameters.keys())



def test_operators_comparison_name_is_not_abstract():
    assert not inspect.isabstract(operators_Comparison_Name)


def test_operators_comparison_name_constructor_exists():
    assert callable(operators_Comparison_Name.__init__)


def test_operators_comparison_name_constructor_args():
    sig = inspect.signature(operators_Comparison_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_less_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Less_Name)


def test_iec61131_operators_less_name_constructor_exists():
    assert callable(iec61131_operators_Less_Name.__init__)


def test_iec61131_operators_less_name_constructor_args():
    sig = inspect.signature(iec61131_operators_Less_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_greaterequal_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_GreaterEqual_Name)


def test_iec61131_operators_greaterequal_name_constructor_exists():
    assert callable(iec61131_operators_GreaterEqual_Name.__init__)


def test_iec61131_operators_greaterequal_name_constructor_args():
    sig = inspect.signature(iec61131_operators_GreaterEqual_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_greater_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Greater_Name)


def test_iec61131_operators_greater_name_constructor_exists():
    assert callable(iec61131_operators_Greater_Name.__init__)


def test_iec61131_operators_greater_name_constructor_args():
    sig = inspect.signature(iec61131_operators_Greater_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_unequal_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Unequal_Name)


def test_iec61131_operators_unequal_name_constructor_exists():
    assert callable(iec61131_operators_Unequal_Name.__init__)


def test_iec61131_operators_unequal_name_constructor_args():
    sig = inspect.signature(iec61131_operators_Unequal_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_lessequal_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_LessEqual_Name)


def test_iec61131_operators_lessequal_name_constructor_exists():
    assert callable(iec61131_operators_LessEqual_Name.__init__)


def test_iec61131_operators_lessequal_name_constructor_args():
    sig = inspect.signature(iec61131_operators_LessEqual_Name.__init__)
    params = list(sig.parameters.keys())



def test_operators_equal_operator_is_not_abstract():
    assert not inspect.isabstract(operators_Equal_Operator)


def test_operators_equal_operator_constructor_exists():
    assert callable(operators_Equal_Operator.__init__)


def test_operators_equal_operator_constructor_args():
    sig = inspect.signature(operators_Equal_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_equal_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Equal_Name)


def test_iec61131_operators_equal_name_constructor_exists():
    assert callable(iec61131_operators_Equal_Name.__init__)


def test_iec61131_operators_equal_name_constructor_args():
    sig = inspect.signature(iec61131_operators_Equal_Name.__init__)
    params = list(sig.parameters.keys())



def test_and_operator_is_not_abstract():
    assert not inspect.isabstract(And_Operator)


def test_and_operator_constructor_exists():
    assert callable(And_Operator.__init__)


def test_and_operator_constructor_args():
    sig = inspect.signature(And_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_and_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_And_Name)


def test_iec61131_operators_and_name_constructor_exists():
    assert callable(iec61131_operators_And_Name.__init__)


def test_iec61131_operators_and_name_constructor_args():
    sig = inspect.signature(iec61131_operators_And_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_and_symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_And_Symbol)


def test_iec61131_operators_and_symbol_constructor_exists():
    assert callable(iec61131_operators_And_Symbol.__init__)


def test_iec61131_operators_and_symbol_constructor_args():
    sig = inspect.signature(iec61131_operators_And_Symbol.__init__)
    params = list(sig.parameters.keys())



def test_assignment_operator_is_not_abstract():
    assert not inspect.isabstract(Assignment_Operator)


def test_assignment_operator_constructor_exists():
    assert callable(Assignment_Operator.__init__)


def test_assignment_operator_constructor_args():
    sig = inspect.signature(Assignment_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_assignment_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Assignment_Name)


def test_iec61131_operators_assignment_name_constructor_exists():
    assert callable(iec61131_operators_Assignment_Name.__init__)


def test_iec61131_operators_assignment_name_constructor_args():
    sig = inspect.signature(iec61131_operators_Assignment_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_assignment_symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Assignment_Symbol)


def test_iec61131_operators_assignment_symbol_constructor_exists():
    assert callable(iec61131_operators_Assignment_Symbol.__init__)


def test_iec61131_operators_assignment_symbol_constructor_args():
    sig = inspect.signature(iec61131_operators_Assignment_Symbol.__init__)
    params = list(sig.parameters.keys())



def test_power_operator_is_not_abstract():
    assert not inspect.isabstract(Power_Operator)


def test_power_operator_constructor_exists():
    assert callable(Power_Operator.__init__)


def test_power_operator_constructor_args():
    sig = inspect.signature(Power_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_power_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Power_Name)


def test_iec61131_operators_power_name_constructor_exists():
    assert callable(iec61131_operators_Power_Name.__init__)


def test_iec61131_operators_power_name_constructor_args():
    sig = inspect.signature(iec61131_operators_Power_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_power_symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Power_Symbol)


def test_iec61131_operators_power_symbol_constructor_exists():
    assert callable(iec61131_operators_Power_Symbol.__init__)


def test_iec61131_operators_power_symbol_constructor_args():
    sig = inspect.signature(iec61131_operators_Power_Symbol.__init__)
    params = list(sig.parameters.keys())



def test_divide_operator_is_not_abstract():
    assert not inspect.isabstract(Divide_Operator)


def test_divide_operator_constructor_exists():
    assert callable(Divide_Operator.__init__)


def test_divide_operator_constructor_args():
    sig = inspect.signature(Divide_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_divide_symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Divide_Symbol)


def test_iec61131_operators_divide_symbol_constructor_exists():
    assert callable(iec61131_operators_Divide_Symbol.__init__)


def test_iec61131_operators_divide_symbol_constructor_args():
    sig = inspect.signature(iec61131_operators_Divide_Symbol.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_integer_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Integer)


def test_iec61131_literals_integer_constructor_exists():
    assert callable(iec61131_literals_Integer.__init__)


def test_iec61131_literals_integer_constructor_args():
    sig = inspect.signature(iec61131_literals_Integer.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iec61131_literals_integer_has_value():
    assert hasattr(iec61131_literals_Integer, "value")
    descriptor = None
    for klass in iec61131_literals_Integer.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iec61131_literals_bsinteger_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_BSInteger)


def test_iec61131_literals_bsinteger_constructor_exists():
    assert callable(iec61131_literals_BSInteger.__init__)


def test_iec61131_literals_bsinteger_constructor_args():
    sig = inspect.signature(iec61131_literals_BSInteger.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_date_literal_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Date_Literal)


def test_iec61131_literals_date_literal_constructor_exists():
    assert callable(iec61131_literals_Date_Literal.__init__)


def test_iec61131_literals_date_literal_constructor_args():
    sig = inspect.signature(iec61131_literals_Date_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "day" in params, "Missing parameter 'day'"
    assert "month" in params, "Missing parameter 'month'"

def test_iec61131_literals_date_literal_has_year():
    assert hasattr(iec61131_literals_Date_Literal, "year")
    descriptor = None
    for klass in iec61131_literals_Date_Literal.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_iec61131_literals_date_literal_has_day():
    assert hasattr(iec61131_literals_Date_Literal, "day")
    descriptor = None
    for klass in iec61131_literals_Date_Literal.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_iec61131_literals_date_literal_has_month():
    assert hasattr(iec61131_literals_Date_Literal, "month")
    descriptor = None
    for klass in iec61131_literals_Date_Literal.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)



def test_iec61131_literals_daytime_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Daytime)


def test_iec61131_literals_daytime_constructor_exists():
    assert callable(iec61131_literals_Daytime.__init__)


def test_iec61131_literals_daytime_constructor_args():
    sig = inspect.signature(iec61131_literals_Daytime.__init__)
    params = list(sig.parameters.keys())
    assert "minute" in params, "Missing parameter 'minute'"
    assert "hour" in params, "Missing parameter 'hour'"

def test_iec61131_literals_daytime_has_minute():
    assert hasattr(iec61131_literals_Daytime, "minute")
    descriptor = None
    for klass in iec61131_literals_Daytime.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)

def test_iec61131_literals_daytime_has_hour():
    assert hasattr(iec61131_literals_Daytime, "hour")
    descriptor = None
    for klass in iec61131_literals_Daytime.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)



def test_iec61131_literals_fixed_point_literal_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Fixed_Point_Literal)


def test_iec61131_literals_fixed_point_literal_constructor_exists():
    assert callable(iec61131_literals_Fixed_Point_Literal.__init__)


def test_iec61131_literals_fixed_point_literal_constructor_args():
    sig = inspect.signature(iec61131_literals_Fixed_Point_Literal.__init__)
    params = list(sig.parameters.keys())



def test_double_byte_character_representation_is_not_abstract():
    assert not inspect.isabstract(Double_Byte_Character_Representation)


def test_double_byte_character_representation_constructor_exists():
    assert callable(Double_Byte_Character_Representation.__init__)


def test_double_byte_character_representation_constructor_args():
    sig = inspect.signature(Double_Byte_Character_Representation.__init__)
    params = list(sig.parameters.keys())



def test_operators_dot_operator_is_not_abstract():
    assert not inspect.isabstract(operators_Dot_Operator)


def test_operators_dot_operator_constructor_exists():
    assert callable(operators_Dot_Operator.__init__)


def test_operators_dot_operator_constructor_args():
    sig = inspect.signature(operators_Dot_Operator.__init__)
    params = list(sig.parameters.keys())



def test_il_il_simple_operator_is_not_abstract():
    assert not inspect.isabstract(il_Il_Simple_Operator)


def test_il_il_simple_operator_constructor_exists():
    assert callable(il_Il_Simple_Operator.__init__)


def test_il_il_simple_operator_constructor_args():
    sig = inspect.signature(il_Il_Simple_Operator.__init__)
    params = list(sig.parameters.keys())



def test_operators_unary_operator_is_not_abstract():
    assert not inspect.isabstract(operators_Unary_Operator)


def test_operators_unary_operator_constructor_exists():
    assert callable(operators_Unary_Operator.__init__)


def test_operators_unary_operator_constructor_args():
    sig = inspect.signature(operators_Unary_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_substraction_symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Substraction_Symbol)


def test_iec61131_operators_substraction_symbol_constructor_exists():
    assert callable(iec61131_operators_Substraction_Symbol.__init__)


def test_iec61131_operators_substraction_symbol_constructor_args():
    sig = inspect.signature(iec61131_operators_Substraction_Symbol.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_not_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Not_Operator)


def test_iec61131_operators_not_operator_constructor_exists():
    assert callable(iec61131_operators_Not_Operator.__init__)


def test_iec61131_operators_not_operator_constructor_args():
    sig = inspect.signature(iec61131_operators_Not_Operator.__init__)
    params = list(sig.parameters.keys())



def test_il_il_expr_operator_is_not_abstract():
    assert not inspect.isabstract(il_Il_Expr_Operator)


def test_il_il_expr_operator_constructor_exists():
    assert callable(il_Il_Expr_Operator.__init__)


def test_il_il_expr_operator_constructor_args():
    sig = inspect.signature(il_Il_Expr_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_modulo_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Modulo_Operator)


def test_iec61131_operators_modulo_operator_constructor_exists():
    assert callable(iec61131_operators_Modulo_Operator.__init__)


def test_iec61131_operators_modulo_operator_constructor_args():
    sig = inspect.signature(iec61131_operators_Modulo_Operator.__init__)
    params = list(sig.parameters.keys())



def test_operators_operator_is_not_abstract():
    assert not inspect.isabstract(operators_Operator)


def test_operators_operator_constructor_exists():
    assert callable(operators_Operator.__init__)


def test_operators_operator_constructor_args():
    sig = inspect.signature(operators_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_xor_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Xor_Operator)


def test_iec61131_operators_xor_operator_constructor_exists():
    assert callable(iec61131_operators_Xor_Operator.__init__)


def test_iec61131_operators_xor_operator_constructor_args():
    sig = inspect.signature(iec61131_operators_Xor_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_or_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Or_Operator)


def test_iec61131_operators_or_operator_constructor_exists():
    assert callable(iec61131_operators_Or_Operator.__init__)


def test_iec61131_operators_or_operator_constructor_args():
    sig = inspect.signature(iec61131_operators_Or_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_and_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_And_Operator)


def test_iec61131_operators_and_operator_constructor_exists():
    assert callable(iec61131_operators_And_Operator.__init__)


def test_iec61131_operators_and_operator_constructor_args():
    sig = inspect.signature(iec61131_operators_And_Operator.__init__)
    params = list(sig.parameters.keys())



def test_equuequ_operator_is_not_abstract():
    assert not inspect.isabstract(EquUequ_Operator)


def test_equuequ_operator_constructor_exists():
    assert callable(EquUequ_Operator.__init__)


def test_equuequ_operator_constructor_args():
    sig = inspect.signature(EquUequ_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_unequal_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Unequal_Operator)


def test_iec61131_operators_unequal_operator_constructor_exists():
    assert callable(iec61131_operators_Unequal_Operator.__init__)


def test_iec61131_operators_unequal_operator_constructor_args():
    sig = inspect.signature(iec61131_operators_Unequal_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_equal_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Equal_Operator)


def test_iec61131_operators_equal_operator_constructor_exists():
    assert callable(iec61131_operators_Equal_Operator.__init__)


def test_iec61131_operators_equal_operator_constructor_args():
    sig = inspect.signature(iec61131_operators_Equal_Operator.__init__)
    params = list(sig.parameters.keys())



def test_dot_operator_is_not_abstract():
    assert not inspect.isabstract(Dot_Operator)


def test_dot_operator_constructor_exists():
    assert callable(Dot_Operator.__init__)


def test_dot_operator_constructor_args():
    sig = inspect.signature(Dot_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_divide_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Divide_Operator)


def test_iec61131_operators_divide_operator_constructor_exists():
    assert callable(iec61131_operators_Divide_Operator.__init__)


def test_iec61131_operators_divide_operator_constructor_args():
    sig = inspect.signature(iec61131_operators_Divide_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_multiply_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Multiply_Operator)


def test_iec61131_operators_multiply_operator_constructor_exists():
    assert callable(iec61131_operators_Multiply_Operator.__init__)


def test_iec61131_operators_multiply_operator_constructor_args():
    sig = inspect.signature(iec61131_operators_Multiply_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_substraction_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Substraction_Operator)


def test_iec61131_operators_substraction_operator_constructor_exists():
    assert callable(iec61131_operators_Substraction_Operator.__init__)


def test_iec61131_operators_substraction_operator_constructor_args():
    sig = inspect.signature(iec61131_operators_Substraction_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_addition_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Addition_Operator)


def test_iec61131_operators_addition_operator_constructor_exists():
    assert callable(iec61131_operators_Addition_Operator.__init__)


def test_iec61131_operators_addition_operator_constructor_args():
    sig = inspect.signature(iec61131_operators_Addition_Operator.__init__)
    params = list(sig.parameters.keys())



def test_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_equuequ_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_EquUequ_Operator)


def test_iec61131_operators_equuequ_operator_constructor_exists():
    assert callable(iec61131_operators_EquUequ_Operator.__init__)


def test_iec61131_operators_equuequ_operator_constructor_args():
    sig = inspect.signature(iec61131_operators_EquUequ_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_assignment_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Assignment_Operator)


def test_iec61131_operators_assignment_operator_constructor_exists():
    assert callable(iec61131_operators_Assignment_Operator.__init__)


def test_iec61131_operators_assignment_operator_constructor_args():
    sig = inspect.signature(iec61131_operators_Assignment_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_dot_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Dot_Operator)


def test_iec61131_operators_dot_operator_constructor_exists():
    assert callable(iec61131_operators_Dot_Operator.__init__)


def test_iec61131_operators_dot_operator_constructor_args():
    sig = inspect.signature(iec61131_operators_Dot_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_comparison_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Comparison_Operator)


def test_iec61131_operators_comparison_operator_constructor_exists():
    assert callable(iec61131_operators_Comparison_Operator.__init__)


def test_iec61131_operators_comparison_operator_constructor_args():
    sig = inspect.signature(iec61131_operators_Comparison_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_power_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Power_Operator)


def test_iec61131_operators_power_operator_constructor_exists():
    assert callable(iec61131_operators_Power_Operator.__init__)


def test_iec61131_operators_power_operator_constructor_args():
    sig = inspect.signature(iec61131_operators_Power_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_unary_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Unary_Operator)


def test_iec61131_operators_unary_operator_constructor_exists():
    assert callable(iec61131_operators_Unary_Operator.__init__)


def test_iec61131_operators_unary_operator_constructor_args():
    sig = inspect.signature(iec61131_operators_Unary_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_add_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Add_Operator)


def test_iec61131_operators_add_operator_constructor_exists():
    assert callable(iec61131_operators_Add_Operator.__init__)


def test_iec61131_operators_add_operator_constructor_args():
    sig = inspect.signature(iec61131_operators_Add_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_operators_operator_is_not_abstract():
    assert not inspect.isabstract(iec61131_operators_Operator)


def test_iec61131_operators_operator_constructor_exists():
    assert callable(iec61131_operators_Operator.__init__)


def test_iec61131_operators_operator_constructor_args():
    sig = inspect.signature(iec61131_operators_Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_double_byte_character_representation_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Double_Byte_Character_Representation)


def test_iec61131_literals_double_byte_character_representation_constructor_exists():
    assert callable(iec61131_literals_Double_Byte_Character_Representation.__init__)


def test_iec61131_literals_double_byte_character_representation_constructor_args():
    sig = inspect.signature(iec61131_literals_Double_Byte_Character_Representation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iec61131_literals_double_byte_character_representation_has_value():
    assert hasattr(iec61131_literals_Double_Byte_Character_Representation, "value")
    descriptor = None
    for klass in iec61131_literals_Double_Byte_Character_Representation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_common_character_representation_is_not_abstract():
    assert not inspect.isabstract(Common_Character_Representation)


def test_common_character_representation_constructor_exists():
    assert callable(Common_Character_Representation.__init__)


def test_common_character_representation_constructor_args():
    sig = inspect.signature(Common_Character_Representation.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_single_byte_character_representation_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Single_Byte_Character_Representation)


def test_iec61131_literals_single_byte_character_representation_constructor_exists():
    assert callable(iec61131_literals_Single_Byte_Character_Representation.__init__)


def test_iec61131_literals_single_byte_character_representation_constructor_args():
    sig = inspect.signature(iec61131_literals_Single_Byte_Character_Representation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iec61131_literals_single_byte_character_representation_has_value():
    assert hasattr(iec61131_literals_Single_Byte_Character_Representation, "value")
    descriptor = None
    for klass in iec61131_literals_Single_Byte_Character_Representation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iec61131_literals_common_character_representation_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Common_Character_Representation)


def test_iec61131_literals_common_character_representation_constructor_exists():
    assert callable(iec61131_literals_Common_Character_Representation.__init__)


def test_iec61131_literals_common_character_representation_constructor_args():
    sig = inspect.signature(iec61131_literals_Common_Character_Representation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iec61131_literals_common_character_representation_has_value():
    assert hasattr(iec61131_literals_Common_Character_Representation, "value")
    descriptor = None
    for klass in iec61131_literals_Common_Character_Representation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dt_type_name_is_not_abstract():
    assert not inspect.isabstract(DT_Type_Name)


def test_dt_type_name_constructor_exists():
    assert callable(DT_Type_Name.__init__)


def test_dt_type_name_constructor_args():
    sig = inspect.signature(DT_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_date_literal_is_not_abstract():
    assert not inspect.isabstract(Date_Literal)


def test_date_literal_constructor_exists():
    assert callable(Date_Literal.__init__)


def test_date_literal_constructor_args():
    sig = inspect.signature(Date_Literal.__init__)
    params = list(sig.parameters.keys())



def test_date_type_name_is_not_abstract():
    assert not inspect.isabstract(Date_Type_Name)


def test_date_type_name_constructor_exists():
    assert callable(Date_Type_Name.__init__)


def test_date_type_name_constructor_args():
    sig = inspect.signature(Date_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_tod_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_TOD_Type_Name)


def test_iec61131_types_tod_type_name_constructor_exists():
    assert callable(iec61131_types_TOD_Type_Name.__init__)


def test_iec61131_types_tod_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_TOD_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_dt_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_DT_Type_Name)


def test_iec61131_types_dt_type_name_constructor_exists():
    assert callable(iec61131_types_DT_Type_Name.__init__)


def test_iec61131_types_dt_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_DT_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_single_byte_character_representation_is_not_abstract():
    assert not inspect.isabstract(Single_Byte_Character_Representation)


def test_single_byte_character_representation_constructor_exists():
    assert callable(Single_Byte_Character_Representation.__init__)


def test_single_byte_character_representation_constructor_args():
    sig = inspect.signature(Single_Byte_Character_Representation.__init__)
    params = list(sig.parameters.keys())



def test_character_string_is_not_abstract():
    assert not inspect.isabstract(Character_String)


def test_character_string_constructor_exists():
    assert callable(Character_String.__init__)


def test_character_string_constructor_args():
    sig = inspect.signature(Character_String.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_double_byte_character_string_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Double_Byte_Character_String)


def test_iec61131_literals_double_byte_character_string_constructor_exists():
    assert callable(iec61131_literals_Double_Byte_Character_String.__init__)


def test_iec61131_literals_double_byte_character_string_constructor_args():
    sig = inspect.signature(iec61131_literals_Double_Byte_Character_String.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_single_byte_character_string_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Single_Byte_Character_String)


def test_iec61131_literals_single_byte_character_string_constructor_exists():
    assert callable(iec61131_literals_Single_Byte_Character_String.__init__)


def test_iec61131_literals_single_byte_character_string_constructor_args():
    sig = inspect.signature(iec61131_literals_Single_Byte_Character_String.__init__)
    params = list(sig.parameters.keys())



def test_milliseconds_is_not_abstract():
    assert not inspect.isabstract(Milliseconds)


def test_milliseconds_constructor_exists():
    assert callable(Milliseconds.__init__)


def test_milliseconds_constructor_args():
    sig = inspect.signature(Milliseconds.__init__)
    params = list(sig.parameters.keys())



def test_seconds_is_not_abstract():
    assert not inspect.isabstract(Seconds)


def test_seconds_constructor_exists():
    assert callable(Seconds.__init__)


def test_seconds_constructor_args():
    sig = inspect.signature(Seconds.__init__)
    params = list(sig.parameters.keys())



def test_minutes_is_not_abstract():
    assert not inspect.isabstract(Minutes)


def test_minutes_constructor_exists():
    assert callable(Minutes.__init__)


def test_minutes_constructor_args():
    sig = inspect.signature(Minutes.__init__)
    params = list(sig.parameters.keys())



def test_hours_is_not_abstract():
    assert not inspect.isabstract(Hours)


def test_hours_constructor_exists():
    assert callable(Hours.__init__)


def test_hours_constructor_args():
    sig = inspect.signature(Hours.__init__)
    params = list(sig.parameters.keys())



def test_unsigned_integer_is_not_abstract():
    assert not inspect.isabstract(Unsigned_Integer)


def test_unsigned_integer_constructor_exists():
    assert callable(Unsigned_Integer.__init__)


def test_unsigned_integer_constructor_args():
    sig = inspect.signature(Unsigned_Integer.__init__)
    params = list(sig.parameters.keys())



def test_fixed_point_literal_is_not_abstract():
    assert not inspect.isabstract(Fixed_Point_Literal)


def test_fixed_point_literal_constructor_exists():
    assert callable(Fixed_Point_Literal.__init__)


def test_fixed_point_literal_constructor_args():
    sig = inspect.signature(Fixed_Point_Literal.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_fixed_point_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Fixed_Point)


def test_iec61131_literals_fixed_point_constructor_exists():
    assert callable(iec61131_literals_Fixed_Point.__init__)


def test_iec61131_literals_fixed_point_constructor_args():
    sig = inspect.signature(iec61131_literals_Fixed_Point.__init__)
    params = list(sig.parameters.keys())
    assert "valuePre" in params, "Missing parameter 'valuePre'"
    assert "valuePost" in params, "Missing parameter 'valuePost'"

def test_iec61131_literals_fixed_point_has_valuePre():
    assert hasattr(iec61131_literals_Fixed_Point, "valuePre")
    descriptor = None
    for klass in iec61131_literals_Fixed_Point.__mro__:
        if "valuePre" in klass.__dict__:
            descriptor = klass.__dict__["valuePre"]
            break
    assert isinstance(descriptor, property)

def test_iec61131_literals_fixed_point_has_valuePost():
    assert hasattr(iec61131_literals_Fixed_Point, "valuePost")
    descriptor = None
    for klass in iec61131_literals_Fixed_Point.__mro__:
        if "valuePost" in klass.__dict__:
            descriptor = klass.__dict__["valuePost"]
            break
    assert isinstance(descriptor, property)



def test_iec61131_literals_interval_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Interval)


def test_iec61131_literals_interval_constructor_exists():
    assert callable(iec61131_literals_Interval.__init__)


def test_iec61131_literals_interval_constructor_args():
    sig = inspect.signature(iec61131_literals_Interval.__init__)
    params = list(sig.parameters.keys())



def test_literals_fixed_point_literal_is_not_abstract():
    assert not inspect.isabstract(literals_Fixed_Point_Literal)


def test_literals_fixed_point_literal_constructor_exists():
    assert callable(literals_Fixed_Point_Literal.__init__)


def test_literals_fixed_point_literal_constructor_args():
    sig = inspect.signature(literals_Fixed_Point_Literal.__init__)
    params = list(sig.parameters.keys())



def test_integer_is_not_abstract():
    assert not inspect.isabstract(Integer)


def test_integer_constructor_exists():
    assert callable(Integer.__init__)


def test_integer_constructor_args():
    sig = inspect.signature(Integer.__init__)
    params = list(sig.parameters.keys())



def test_numeric_literal_is_not_abstract():
    assert not inspect.isabstract(Numeric_Literal)


def test_numeric_literal_constructor_exists():
    assert callable(Numeric_Literal.__init__)


def test_numeric_literal_constructor_args():
    sig = inspect.signature(Numeric_Literal.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_integer_literal_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Integer_Literal)


def test_iec61131_literals_integer_literal_constructor_exists():
    assert callable(iec61131_literals_Integer_Literal.__init__)


def test_iec61131_literals_integer_literal_constructor_args():
    sig = inspect.signature(iec61131_literals_Integer_Literal.__init__)
    params = list(sig.parameters.keys())



def test_bit_string_type_name_is_not_abstract():
    assert not inspect.isabstract(Bit_String_Type_Name)


def test_bit_string_type_name_constructor_exists():
    assert callable(Bit_String_Type_Name.__init__)


def test_bit_string_type_name_constructor_args():
    sig = inspect.signature(Bit_String_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_bool_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_Bool_Type_Name)


def test_iec61131_types_bool_type_name_constructor_exists():
    assert callable(iec61131_types_Bool_Type_Name.__init__)


def test_iec61131_types_bool_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_Bool_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_bsinteger_is_not_abstract():
    assert not inspect.isabstract(BSInteger)


def test_bsinteger_constructor_exists():
    assert callable(BSInteger.__init__)


def test_bsinteger_constructor_args():
    sig = inspect.signature(BSInteger.__init__)
    params = list(sig.parameters.keys())



def test_constant_is_not_abstract():
    assert not inspect.isabstract(Constant)


def test_constant_constructor_exists():
    assert callable(Constant.__init__)


def test_constant_constructor_args():
    sig = inspect.signature(Constant.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_bit_string_literal_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Bit_String_Literal)


def test_iec61131_literals_bit_string_literal_constructor_exists():
    assert callable(iec61131_literals_Bit_String_Literal.__init__)


def test_iec61131_literals_bit_string_literal_constructor_args():
    sig = inspect.signature(iec61131_literals_Bit_String_Literal.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_time_literal_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Time_Literal)


def test_iec61131_literals_time_literal_constructor_exists():
    assert callable(iec61131_literals_Time_Literal.__init__)


def test_iec61131_literals_time_literal_constructor_args():
    sig = inspect.signature(iec61131_literals_Time_Literal.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_character_string_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Character_String)


def test_iec61131_literals_character_string_constructor_exists():
    assert callable(iec61131_literals_Character_String.__init__)


def test_iec61131_literals_character_string_constructor_args():
    sig = inspect.signature(iec61131_literals_Character_String.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_numeric_literal_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Numeric_Literal)


def test_iec61131_literals_numeric_literal_constructor_exists():
    assert callable(iec61131_literals_Numeric_Literal.__init__)


def test_iec61131_literals_numeric_literal_constructor_args():
    sig = inspect.signature(iec61131_literals_Numeric_Literal.__init__)
    params = list(sig.parameters.keys())



def test_tod_type_name_is_not_abstract():
    assert not inspect.isabstract(TOD_Type_Name)


def test_tod_type_name_constructor_exists():
    assert callable(TOD_Type_Name.__init__)


def test_tod_type_name_constructor_args():
    sig = inspect.signature(TOD_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_daytime_is_not_abstract():
    assert not inspect.isabstract(Daytime)


def test_daytime_constructor_exists():
    assert callable(Daytime.__init__)


def test_daytime_constructor_args():
    sig = inspect.signature(Daytime.__init__)
    params = list(sig.parameters.keys())



def test_time_literal_is_not_abstract():
    assert not inspect.isabstract(Time_Literal)


def test_time_literal_constructor_exists():
    assert callable(Time_Literal.__init__)


def test_time_literal_constructor_args():
    sig = inspect.signature(Time_Literal.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_date_and_time_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Date_And_Time)


def test_iec61131_literals_date_and_time_constructor_exists():
    assert callable(iec61131_literals_Date_And_Time.__init__)


def test_iec61131_literals_date_and_time_constructor_args():
    sig = inspect.signature(iec61131_literals_Date_And_Time.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_date_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Date)


def test_iec61131_literals_date_constructor_exists():
    assert callable(iec61131_literals_Date.__init__)


def test_iec61131_literals_date_constructor_args():
    sig = inspect.signature(iec61131_literals_Date.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_time_of_day_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Time_Of_Day)


def test_iec61131_literals_time_of_day_constructor_exists():
    assert callable(iec61131_literals_Time_Of_Day.__init__)


def test_iec61131_literals_time_of_day_constructor_args():
    sig = inspect.signature(iec61131_literals_Time_Of_Day.__init__)
    params = list(sig.parameters.keys())



def test_substraction_operator_is_not_abstract():
    assert not inspect.isabstract(Substraction_Operator)


def test_substraction_operator_constructor_exists():
    assert callable(Substraction_Operator.__init__)


def test_substraction_operator_constructor_args():
    sig = inspect.signature(Substraction_Operator.__init__)
    params = list(sig.parameters.keys())



def test_duration_type_name_is_not_abstract():
    assert not inspect.isabstract(Duration_Type_Name)


def test_duration_type_name_constructor_exists():
    assert callable(Duration_Type_Name.__init__)


def test_duration_type_name_constructor_args():
    sig = inspect.signature(Duration_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_interval_is_not_abstract():
    assert not inspect.isabstract(Interval)


def test_interval_constructor_exists():
    assert callable(Interval.__init__)


def test_interval_constructor_args():
    sig = inspect.signature(Interval.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_days_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Days)


def test_iec61131_literals_days_constructor_exists():
    assert callable(iec61131_literals_Days.__init__)


def test_iec61131_literals_days_constructor_args():
    sig = inspect.signature(iec61131_literals_Days.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_minutes_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Minutes)


def test_iec61131_literals_minutes_constructor_exists():
    assert callable(iec61131_literals_Minutes.__init__)


def test_iec61131_literals_minutes_constructor_args():
    sig = inspect.signature(iec61131_literals_Minutes.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_hours_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Hours)


def test_iec61131_literals_hours_constructor_exists():
    assert callable(iec61131_literals_Hours.__init__)


def test_iec61131_literals_hours_constructor_args():
    sig = inspect.signature(iec61131_literals_Hours.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_milliseconds_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Milliseconds)


def test_iec61131_literals_milliseconds_constructor_exists():
    assert callable(iec61131_literals_Milliseconds.__init__)


def test_iec61131_literals_milliseconds_constructor_args():
    sig = inspect.signature(iec61131_literals_Milliseconds.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_seconds_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Seconds)


def test_iec61131_literals_seconds_constructor_exists():
    assert callable(iec61131_literals_Seconds.__init__)


def test_iec61131_literals_seconds_constructor_args():
    sig = inspect.signature(iec61131_literals_Seconds.__init__)
    params = list(sig.parameters.keys())



def test_sfc_action_time_is_not_abstract():
    assert not inspect.isabstract(sfc_Action_Time)


def test_sfc_action_time_constructor_exists():
    assert callable(sfc_Action_Time.__init__)


def test_sfc_action_time_constructor_args():
    sig = inspect.signature(sfc_Action_Time.__init__)
    params = list(sig.parameters.keys())



def test_literals_time_literal_is_not_abstract():
    assert not inspect.isabstract(literals_Time_Literal)


def test_literals_time_literal_constructor_exists():
    assert callable(literals_Time_Literal.__init__)


def test_literals_time_literal_constructor_args():
    sig = inspect.signature(literals_Time_Literal.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_duration_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Duration)


def test_iec61131_literals_duration_constructor_exists():
    assert callable(iec61131_literals_Duration.__init__)


def test_iec61131_literals_duration_constructor_args():
    sig = inspect.signature(iec61131_literals_Duration.__init__)
    params = list(sig.parameters.keys())



def test_literals_bsinteger_is_not_abstract():
    assert not inspect.isabstract(literals_BSInteger)


def test_literals_bsinteger_constructor_exists():
    assert callable(literals_BSInteger.__init__)


def test_literals_bsinteger_constructor_args():
    sig = inspect.signature(literals_BSInteger.__init__)
    params = list(sig.parameters.keys())



def test_interfaces_range_is_not_abstract():
    assert not inspect.isabstract(interfaces_Range)


def test_interfaces_range_constructor_exists():
    assert callable(interfaces_Range.__init__)


def test_interfaces_range_constructor_args():
    sig = inspect.signature(interfaces_Range.__init__)
    params = list(sig.parameters.keys())



def test_st_case_list_element_is_not_abstract():
    assert not inspect.isabstract(st_Case_List_Element)


def test_st_case_list_element_constructor_exists():
    assert callable(st_Case_List_Element.__init__)


def test_st_case_list_element_constructor_args():
    sig = inspect.signature(st_Case_List_Element.__init__)
    params = list(sig.parameters.keys())



def test_literals_integer_is_not_abstract():
    assert not inspect.isabstract(literals_Integer)


def test_literals_integer_constructor_exists():
    assert callable(literals_Integer.__init__)


def test_literals_integer_constructor_args():
    sig = inspect.signature(literals_Integer.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_unsigned_integer_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Unsigned_Integer)


def test_iec61131_literals_unsigned_integer_constructor_exists():
    assert callable(iec61131_literals_Unsigned_Integer.__init__)


def test_iec61131_literals_unsigned_integer_constructor_args():
    sig = inspect.signature(iec61131_literals_Unsigned_Integer.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_hex_integer_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Hex_Integer)


def test_iec61131_literals_hex_integer_constructor_exists():
    assert callable(iec61131_literals_Hex_Integer.__init__)


def test_iec61131_literals_hex_integer_constructor_args():
    sig = inspect.signature(iec61131_literals_Hex_Integer.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_octal_integer_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Octal_Integer)


def test_iec61131_literals_octal_integer_constructor_exists():
    assert callable(iec61131_literals_Octal_Integer.__init__)


def test_iec61131_literals_octal_integer_constructor_args():
    sig = inspect.signature(iec61131_literals_Octal_Integer.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_binary_integer_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Binary_Integer)


def test_iec61131_literals_binary_integer_constructor_exists():
    assert callable(iec61131_literals_Binary_Integer.__init__)


def test_iec61131_literals_binary_integer_constructor_args():
    sig = inspect.signature(iec61131_literals_Binary_Integer.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_signed_integer_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Signed_Integer)


def test_iec61131_literals_signed_integer_constructor_exists():
    assert callable(iec61131_literals_Signed_Integer.__init__)


def test_iec61131_literals_signed_integer_constructor_args():
    sig = inspect.signature(iec61131_literals_Signed_Integer.__init__)
    params = list(sig.parameters.keys())
    assert "negative" in params, "Missing parameter 'negative'"

def test_iec61131_literals_signed_integer_has_negative():
    assert hasattr(iec61131_literals_Signed_Integer, "negative")
    descriptor = None
    for klass in iec61131_literals_Signed_Integer.__mro__:
        if "negative" in klass.__dict__:
            descriptor = klass.__dict__["negative"]
            break
    assert isinstance(descriptor, property)



def test_il_il_operand_is_not_abstract():
    assert not inspect.isabstract(il_Il_Operand)


def test_il_il_operand_constructor_exists():
    assert callable(il_Il_Operand.__init__)


def test_il_il_operand_constructor_args():
    sig = inspect.signature(il_Il_Operand.__init__)
    params = list(sig.parameters.keys())



def test_configurations_prog_data_source_is_not_abstract():
    assert not inspect.isabstract(configurations_Prog_Data_Source)


def test_configurations_prog_data_source_constructor_exists():
    assert callable(configurations_Prog_Data_Source.__init__)


def test_configurations_prog_data_source_constructor_args():
    sig = inspect.signature(configurations_Prog_Data_Source.__init__)
    params = list(sig.parameters.keys())



def test_configurations_data_source_is_not_abstract():
    assert not inspect.isabstract(configurations_Data_Source)


def test_configurations_data_source_constructor_exists():
    assert callable(configurations_Data_Source.__init__)


def test_configurations_data_source_constructor_args():
    sig = inspect.signature(configurations_Data_Source.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_global_var_reference_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Global_Var_Reference)


def test_iec61131_configurations_global_var_reference_constructor_exists():
    assert callable(iec61131_configurations_Global_Var_Reference.__init__)


def test_iec61131_configurations_global_var_reference_constructor_args():
    sig = inspect.signature(iec61131_configurations_Global_Var_Reference.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_variables_direct_variable_is_not_abstract():
    assert not inspect.isabstract(iec61131_variables_Direct_Variable)


def test_iec61131_variables_direct_variable_constructor_exists():
    assert callable(iec61131_variables_Direct_Variable.__init__)


def test_iec61131_variables_direct_variable_constructor_args():
    sig = inspect.signature(iec61131_variables_Direct_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iec61131_variables_direct_variable_has_value():
    assert hasattr(iec61131_variables_Direct_Variable, "value")
    descriptor = None
    for klass in iec61131_variables_Direct_Variable.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iec61131_literals_constant_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Constant)


def test_iec61131_literals_constant_constructor_exists():
    assert callable(iec61131_literals_Constant.__init__)


def test_iec61131_literals_constant_constructor_args():
    sig = inspect.signature(iec61131_literals_Constant.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_boolean_literal_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Boolean_Literal)


def test_iec61131_literals_boolean_literal_constructor_exists():
    assert callable(iec61131_literals_Boolean_Literal.__init__)


def test_iec61131_literals_boolean_literal_constructor_args():
    sig = inspect.signature(iec61131_literals_Boolean_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iec61131_literals_boolean_literal_has_value():
    assert hasattr(iec61131_literals_Boolean_Literal, "value")
    descriptor = None
    for klass in iec61131_literals_Boolean_Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fixed_point_is_not_abstract():
    assert not inspect.isabstract(Fixed_Point)


def test_fixed_point_constructor_exists():
    assert callable(Fixed_Point.__init__)


def test_fixed_point_constructor_args():
    sig = inspect.signature(Fixed_Point.__init__)
    params = list(sig.parameters.keys())



def test_real_type_name_is_not_abstract():
    assert not inspect.isabstract(Real_Type_Name)


def test_real_type_name_constructor_exists():
    assert callable(Real_Type_Name.__init__)


def test_real_type_name_constructor_args():
    sig = inspect.signature(Real_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_literals_real_literal_is_not_abstract():
    assert not inspect.isabstract(iec61131_literals_Real_Literal)


def test_iec61131_literals_real_literal_constructor_exists():
    assert callable(iec61131_literals_Real_Literal.__init__)


def test_iec61131_literals_real_literal_constructor_args():
    sig = inspect.signature(iec61131_literals_Real_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "exponent" in params, "Missing parameter 'exponent'"
    assert "negative" in params, "Missing parameter 'negative'"

def test_iec61131_literals_real_literal_has_exponent():
    assert hasattr(iec61131_literals_Real_Literal, "exponent")
    descriptor = None
    for klass in iec61131_literals_Real_Literal.__mro__:
        if "exponent" in klass.__dict__:
            descriptor = klass.__dict__["exponent"]
            break
    assert isinstance(descriptor, property)

def test_iec61131_literals_real_literal_has_negative():
    assert hasattr(iec61131_literals_Real_Literal, "negative")
    descriptor = None
    for klass in iec61131_literals_Real_Literal.__mro__:
        if "negative" in klass.__dict__:
            descriptor = klass.__dict__["negative"]
            break
    assert isinstance(descriptor, property)



def test_integer_type_name_is_not_abstract():
    assert not inspect.isabstract(Integer_Type_Name)


def test_integer_type_name_constructor_exists():
    assert callable(Integer_Type_Name.__init__)


def test_integer_type_name_constructor_args():
    sig = inspect.signature(Integer_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_unsigned_integer_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_Unsigned_Integer_Type_Name)


def test_iec61131_types_unsigned_integer_type_name_constructor_exists():
    assert callable(iec61131_types_Unsigned_Integer_Type_Name.__init__)


def test_iec61131_types_unsigned_integer_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_Unsigned_Integer_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_signed_integer_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_Signed_Integer_Type_Name)


def test_iec61131_types_signed_integer_type_name_constructor_exists():
    assert callable(iec61131_types_Signed_Integer_Type_Name.__init__)


def test_iec61131_types_signed_integer_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_Signed_Integer_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_namedelement_is_not_abstract():
    assert not inspect.isabstract(iec61131_NamedElement)


def test_iec61131_namedelement_constructor_exists():
    assert callable(iec61131_NamedElement.__init__)


def test_iec61131_namedelement_constructor_args():
    sig = inspect.signature(iec61131_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iec61131_namedelement_has_name():
    assert hasattr(iec61131_NamedElement, "name")
    descriptor = None
    for klass in iec61131_NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iec61131_commentable_is_not_abstract():
    assert not inspect.isabstract(iec61131_Commentable)


def test_iec61131_commentable_constructor_exists():
    assert callable(iec61131_Commentable.__init__)


def test_iec61131_commentable_constructor_args():
    sig = inspect.signature(iec61131_Commentable.__init__)
    params = list(sig.parameters.keys())
    assert "comments" in params, "Missing parameter 'comments'"

def test_iec61131_commentable_has_comments():
    assert hasattr(iec61131_Commentable, "comments")
    descriptor = None
    for klass in iec61131_Commentable.__mro__:
        if "comments" in klass.__dict__:
            descriptor = klass.__dict__["comments"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_sfc_step_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_sfc_Step_Name)


def test_iec61131_sfc_step_name_constructor_exists():
    assert callable(iec61131_sfc_Step_Name.__init__)


def test_iec61131_sfc_step_name_constructor_args():
    sig = inspect.signature(iec61131_sfc_Step_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_variables_variable_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_variables_Variable_Name)


def test_iec61131_variables_variable_name_constructor_exists():
    assert callable(iec61131_variables_Variable_Name.__init__)


def test_iec61131_variables_variable_name_constructor_args():
    sig = inspect.signature(iec61131_variables_Variable_Name.__init__)
    params = list(sig.parameters.keys())



def test_commentable_is_not_abstract():
    assert not inspect.isabstract(Commentable)


def test_commentable_constructor_exists():
    assert callable(Commentable.__init__)


def test_commentable_constructor_args():
    sig = inspect.signature(Commentable.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_program_configuration_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Program_Configuration)


def test_iec61131_configurations_program_configuration_constructor_exists():
    assert callable(iec61131_configurations_Program_Configuration.__init__)


def test_iec61131_configurations_program_configuration_constructor_args():
    sig = inspect.signature(iec61131_configurations_Program_Configuration.__init__)
    params = list(sig.parameters.keys())
    assert "retain" in params, "Missing parameter 'retain'"

def test_iec61131_configurations_program_configuration_has_retain():
    assert hasattr(iec61131_configurations_Program_Configuration, "retain")
    descriptor = None
    for klass in iec61131_configurations_Program_Configuration.__mro__:
        if "retain" in klass.__dict__:
            descriptor = klass.__dict__["retain"]
            break
    assert isinstance(descriptor, property)



def test_iec61131_variables_variable_is_not_abstract():
    assert not inspect.isabstract(iec61131_variables_Variable)


def test_iec61131_variables_variable_constructor_exists():
    assert callable(iec61131_variables_Variable.__init__)


def test_iec61131_variables_variable_constructor_args():
    sig = inspect.signature(iec61131_variables_Variable.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_statement_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Statement)


def test_iec61131_st_statement_constructor_exists():
    assert callable(iec61131_st_Statement.__init__)


def test_iec61131_st_statement_constructor_args():
    sig = inspect.signature(iec61131_st_Statement.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_expression_variable_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Expression_Variable)


def test_iec61131_st_expression_variable_constructor_exists():
    assert callable(iec61131_st_Expression_Variable.__init__)


def test_iec61131_st_expression_variable_constructor_args():
    sig = inspect.signature(iec61131_st_Expression_Variable.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_param_assignment_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Param_Assignment)


def test_iec61131_st_param_assignment_constructor_exists():
    assert callable(iec61131_st_Param_Assignment.__init__)


def test_iec61131_st_param_assignment_constructor_args():
    sig = inspect.signature(iec61131_st_Param_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_st_expression_types_is_not_abstract():
    assert not inspect.isabstract(iec61131_st_Expression_Types)


def test_iec61131_st_expression_types_constructor_exists():
    assert callable(iec61131_st_Expression_Types.__init__)


def test_iec61131_st_expression_types_constructor_args():
    sig = inspect.signature(iec61131_st_Expression_Types.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_library_element_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_Library_Element_Name)


def test_iec61131_library_element_name_constructor_exists():
    assert callable(iec61131_Library_Element_Name.__init__)


def test_iec61131_library_element_name_constructor_args():
    sig = inspect.signature(iec61131_Library_Element_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_library_element_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_Library_Element_Declaration)


def test_iec61131_library_element_declaration_constructor_exists():
    assert callable(iec61131_Library_Element_Declaration.__init__)


def test_iec61131_library_element_declaration_constructor_args():
    sig = inspect.signature(iec61131_Library_Element_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_iec61131_is_not_abstract():
    assert not inspect.isabstract(iec61131_IEC61131)


def test_iec61131_iec61131_constructor_exists():
    assert callable(iec61131_IEC61131.__init__)


def test_iec61131_iec61131_constructor_args():
    sig = inspect.signature(iec61131_IEC61131.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_input_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Input_Declaration)


def test_iec61131_interfaces_input_declaration_constructor_exists():
    assert callable(iec61131_interfaces_Input_Declaration.__init__)


def test_iec61131_interfaces_input_declaration_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Input_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_global_var_spec_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Global_Var_Spec)


def test_iec61131_interfaces_global_var_spec_constructor_exists():
    assert callable(iec61131_interfaces_Global_Var_Spec.__init__)


def test_iec61131_interfaces_global_var_spec_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Global_Var_Spec.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_global_var_decl_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Global_Var_Decl)


def test_iec61131_interfaces_global_var_decl_constructor_exists():
    assert callable(iec61131_interfaces_Global_Var_Decl.__init__)


def test_iec61131_interfaces_global_var_decl_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Global_Var_Decl.__init__)
    params = list(sig.parameters.keys())



def test_external_specification_is_not_abstract():
    assert not inspect.isabstract(External_Specification)


def test_external_specification_constructor_exists():
    assert callable(External_Specification.__init__)


def test_external_specification_constructor_args():
    sig = inspect.signature(External_Specification.__init__)
    params = list(sig.parameters.keys())



def test_global_var_name_is_not_abstract():
    assert not inspect.isabstract(Global_Var_Name)


def test_global_var_name_constructor_exists():
    assert callable(Global_Var_Name.__init__)


def test_global_var_name_constructor_args():
    sig = inspect.signature(Global_Var_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_external_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_External_Declaration)


def test_iec61131_interfaces_external_declaration_constructor_exists():
    assert callable(iec61131_interfaces_External_Declaration.__init__)


def test_iec61131_interfaces_external_declaration_constructor_args():
    sig = inspect.signature(iec61131_interfaces_External_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_interface_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Interface)


def test_iec61131_interfaces_interface_constructor_exists():
    assert callable(iec61131_interfaces_Interface.__init__)


def test_iec61131_interfaces_interface_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Interface.__init__)
    params = list(sig.parameters.keys())



def test_rnv_declarations_is_not_abstract():
    assert not inspect.isabstract(RNV_Declarations)


def test_rnv_declarations_constructor_exists():
    assert callable(RNV_Declarations.__init__)


def test_rnv_declarations_constructor_args():
    sig = inspect.signature(RNV_Declarations.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_non_retentive_var_declarations_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Non_Retentive_Var_Declarations)


def test_iec61131_interfaces_non_retentive_var_declarations_constructor_exists():
    assert callable(iec61131_interfaces_Non_Retentive_Var_Declarations.__init__)


def test_iec61131_interfaces_non_retentive_var_declarations_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Non_Retentive_Var_Declarations.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_retentive_var_declarations_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Retentive_Var_Declarations)


def test_iec61131_interfaces_retentive_var_declarations_constructor_exists():
    assert callable(iec61131_interfaces_Retentive_Var_Declarations.__init__)


def test_iec61131_interfaces_retentive_var_declarations_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Retentive_Var_Declarations.__init__)
    params = list(sig.parameters.keys())



def test_external_declaration_is_not_abstract():
    assert not inspect.isabstract(External_Declaration)


def test_external_declaration_constructor_exists():
    assert callable(External_Declaration.__init__)


def test_external_declaration_constructor_args():
    sig = inspect.signature(External_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_other_var_declaration_is_not_abstract():
    assert not inspect.isabstract(Other_Var_Declaration)


def test_other_var_declaration_constructor_exists():
    assert callable(Other_Var_Declaration.__init__)


def test_other_var_declaration_constructor_args():
    sig = inspect.signature(Other_Var_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_external_var_declarations_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_External_Var_Declarations)


def test_iec61131_interfaces_external_var_declarations_constructor_exists():
    assert callable(iec61131_interfaces_External_Var_Declarations.__init__)


def test_iec61131_interfaces_external_var_declarations_constructor_args():
    sig = inspect.signature(iec61131_interfaces_External_Var_Declarations.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"

def test_iec61131_interfaces_external_var_declarations_has_constant():
    assert hasattr(iec61131_interfaces_External_Var_Declarations, "constant")
    descriptor = None
    for klass in iec61131_interfaces_External_Var_Declarations.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_variable_name_is_not_abstract():
    assert not inspect.isabstract(Variable_Name)


def test_variable_name_constructor_exists():
    assert callable(Variable_Name.__init__)


def test_variable_name_constructor_args():
    sig = inspect.signature(Variable_Name.__init__)
    params = list(sig.parameters.keys())



def test_location_is_not_abstract():
    assert not inspect.isabstract(Location)


def test_location_constructor_exists():
    assert callable(Location.__init__)


def test_location_constructor_args():
    sig = inspect.signature(Location.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_located_var_decl_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Located_Var_Decl)


def test_iec61131_interfaces_located_var_decl_constructor_exists():
    assert callable(iec61131_interfaces_Located_Var_Decl.__init__)


def test_iec61131_interfaces_located_var_decl_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Located_Var_Decl.__init__)
    params = list(sig.parameters.keys())



def test_direct_variable_is_not_abstract():
    assert not inspect.isabstract(Direct_Variable)


def test_direct_variable_constructor_exists():
    assert callable(Direct_Variable.__init__)


def test_direct_variable_constructor_args():
    sig = inspect.signature(Direct_Variable.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_location_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Location)


def test_iec61131_interfaces_location_constructor_exists():
    assert callable(iec61131_interfaces_Location.__init__)


def test_iec61131_interfaces_location_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Location.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_located_var_spec_init_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Located_Var_Spec_Init)


def test_iec61131_interfaces_located_var_spec_init_constructor_exists():
    assert callable(iec61131_interfaces_Located_Var_Spec_Init.__init__)


def test_iec61131_interfaces_located_var_spec_init_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Located_Var_Spec_Init.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_external_specification_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_External_Specification)


def test_iec61131_interfaces_external_specification_constructor_exists():
    assert callable(iec61131_interfaces_External_Specification.__init__)


def test_iec61131_interfaces_external_specification_constructor_args():
    sig = inspect.signature(iec61131_interfaces_External_Specification.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_var_spec_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Var_Spec)


def test_iec61131_interfaces_var_spec_constructor_exists():
    assert callable(iec61131_interfaces_Var_Spec.__init__)


def test_iec61131_interfaces_var_spec_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Var_Spec.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_incompl_location_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Incompl_Location)


def test_iec61131_interfaces_incompl_location_constructor_exists():
    assert callable(iec61131_interfaces_Incompl_Location.__init__)


def test_iec61131_interfaces_incompl_location_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Incompl_Location.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_iec61131_interfaces_incompl_location_has_location():
    assert hasattr(iec61131_interfaces_Incompl_Location, "location")
    descriptor = None
    for klass in iec61131_interfaces_Incompl_Location.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_var_spec_is_not_abstract():
    assert not inspect.isabstract(Var_Spec)


def test_var_spec_constructor_exists():
    assert callable(Var_Spec.__init__)


def test_var_spec_constructor_args():
    sig = inspect.signature(Var_Spec.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_byte_string_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Byte_String)


def test_iec61131_interfaces_byte_string_constructor_exists():
    assert callable(iec61131_interfaces_Byte_String.__init__)


def test_iec61131_interfaces_byte_string_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Byte_String.__init__)
    params = list(sig.parameters.keys())



def test_incompl_location_is_not_abstract():
    assert not inspect.isabstract(Incompl_Location)


def test_incompl_location_constructor_exists():
    assert callable(Incompl_Location.__init__)


def test_incompl_location_constructor_args():
    sig = inspect.signature(Incompl_Location.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_incompl_located_var_decl_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Incompl_Located_Var_Decl)


def test_iec61131_interfaces_incompl_located_var_decl_constructor_exists():
    assert callable(iec61131_interfaces_Incompl_Located_Var_Decl.__init__)


def test_iec61131_interfaces_incompl_located_var_decl_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Incompl_Located_Var_Decl.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_rnv_declarations_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_RNV_Declarations)


def test_iec61131_interfaces_rnv_declarations_constructor_exists():
    assert callable(iec61131_interfaces_RNV_Declarations.__init__)


def test_iec61131_interfaces_rnv_declarations_constructor_args():
    sig = inspect.signature(iec61131_interfaces_RNV_Declarations.__init__)
    params = list(sig.parameters.keys())



def test_incompl_located_var_decl_is_not_abstract():
    assert not inspect.isabstract(Incompl_Located_Var_Decl)


def test_incompl_located_var_decl_constructor_exists():
    assert callable(Incompl_Located_Var_Decl.__init__)


def test_incompl_located_var_decl_constructor_args():
    sig = inspect.signature(Incompl_Located_Var_Decl.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_incompl_located_var_declarations_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Incompl_Located_Var_Declarations)


def test_iec61131_interfaces_incompl_located_var_declarations_constructor_exists():
    assert callable(iec61131_interfaces_Incompl_Located_Var_Declarations.__init__)


def test_iec61131_interfaces_incompl_located_var_declarations_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Incompl_Located_Var_Declarations.__init__)
    params = list(sig.parameters.keys())
    assert "retain" in params, "Missing parameter 'retain'"

def test_iec61131_interfaces_incompl_located_var_declarations_has_retain():
    assert hasattr(iec61131_interfaces_Incompl_Located_Var_Declarations, "retain")
    descriptor = None
    for klass in iec61131_interfaces_Incompl_Located_Var_Declarations.__mro__:
        if "retain" in klass.__dict__:
            descriptor = klass.__dict__["retain"]
            break
    assert isinstance(descriptor, property)



def test_iec61131_interfaces_var_declarations_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Var_Declarations)


def test_iec61131_interfaces_var_declarations_constructor_exists():
    assert callable(iec61131_interfaces_Var_Declarations.__init__)


def test_iec61131_interfaces_var_declarations_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Var_Declarations.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"

def test_iec61131_interfaces_var_declarations_has_constant():
    assert hasattr(iec61131_interfaces_Var_Declarations, "constant")
    descriptor = None
    for klass in iec61131_interfaces_Var_Declarations.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_temp_var_decl_is_not_abstract():
    assert not inspect.isabstract(Temp_Var_Decl)


def test_temp_var_decl_constructor_exists():
    assert callable(Temp_Var_Decl.__init__)


def test_temp_var_decl_constructor_args():
    sig = inspect.signature(Temp_Var_Decl.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_temp_var_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Temp_Var_Declaration)


def test_iec61131_interfaces_temp_var_declaration_constructor_exists():
    assert callable(iec61131_interfaces_Temp_Var_Declaration.__init__)


def test_iec61131_interfaces_temp_var_declaration_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Temp_Var_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_temp_var_decls_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Temp_Var_Decls)


def test_iec61131_interfaces_temp_var_decls_constructor_exists():
    assert callable(iec61131_interfaces_Temp_Var_Decls.__init__)


def test_iec61131_interfaces_temp_var_decls_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Temp_Var_Decls.__init__)
    params = list(sig.parameters.keys())



def test_global_var_spec_is_not_abstract():
    assert not inspect.isabstract(Global_Var_Spec)


def test_global_var_spec_constructor_exists():
    assert callable(Global_Var_Spec.__init__)


def test_global_var_spec_constructor_args():
    sig = inspect.signature(Global_Var_Spec.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_global_var_location_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Global_Var_Location)


def test_iec61131_interfaces_global_var_location_constructor_exists():
    assert callable(iec61131_interfaces_Global_Var_Location.__init__)


def test_iec61131_interfaces_global_var_location_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Global_Var_Location.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_global_var_list_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Global_Var_List)


def test_iec61131_interfaces_global_var_list_constructor_exists():
    assert callable(iec61131_interfaces_Global_Var_List.__init__)


def test_iec61131_interfaces_global_var_list_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Global_Var_List.__init__)
    params = list(sig.parameters.keys())



def test_library_element_name_is_not_abstract():
    assert not inspect.isabstract(Library_Element_Name)


def test_library_element_name_constructor_exists():
    assert callable(Library_Element_Name.__init__)


def test_library_element_name_constructor_args():
    sig = inspect.signature(Library_Element_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_program_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Program_Type_Name)


def test_iec61131_pous_program_type_name_constructor_exists():
    assert callable(iec61131_pous_Program_Type_Name.__init__)


def test_iec61131_pous_program_type_name_constructor_args():
    sig = inspect.signature(iec61131_pous_Program_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_data_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_Data_Type_Name)


def test_iec61131_types_data_type_name_constructor_exists():
    assert callable(iec61131_types_Data_Type_Name.__init__)


def test_iec61131_types_data_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_Data_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_configuration_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Configuration_Name)


def test_iec61131_configurations_configuration_name_constructor_exists():
    assert callable(iec61131_configurations_Configuration_Name.__init__)


def test_iec61131_configurations_configuration_name_constructor_args():
    sig = inspect.signature(iec61131_configurations_Configuration_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_function_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Function_Name)


def test_iec61131_pous_function_name_constructor_exists():
    assert callable(iec61131_pous_Function_Name.__init__)


def test_iec61131_pous_function_name_constructor_args():
    sig = inspect.signature(iec61131_pous_Function_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_configurations_resource_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_configurations_Resource_Type_Name)


def test_iec61131_configurations_resource_type_name_constructor_exists():
    assert callable(iec61131_configurations_Resource_Type_Name.__init__)


def test_iec61131_configurations_resource_type_name_constructor_args():
    sig = inspect.signature(iec61131_configurations_Resource_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_global_var_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Global_Var_Name)


def test_iec61131_interfaces_global_var_name_constructor_exists():
    assert callable(iec61131_interfaces_Global_Var_Name.__init__)


def test_iec61131_interfaces_global_var_name_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Global_Var_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_specification_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Specification)


def test_iec61131_interfaces_specification_constructor_exists():
    assert callable(iec61131_interfaces_Specification.__init__)


def test_iec61131_interfaces_specification_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Specification.__init__)
    params = list(sig.parameters.keys())



def test_specification_is_not_abstract():
    assert not inspect.isabstract(Specification)


def test_specification_constructor_exists():
    assert callable(Specification.__init__)


def test_specification_constructor_args():
    sig = inspect.signature(Specification.__init__)
    params = list(sig.parameters.keys())



def test_array_initial_elements_is_not_abstract():
    assert not inspect.isabstract(Array_Initial_Elements)


def test_array_initial_elements_constructor_exists():
    assert callable(Array_Initial_Elements.__init__)


def test_array_initial_elements_constructor_args():
    sig = inspect.signature(Array_Initial_Elements.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_array_initial_elements1_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Array_Initial_Elements1)


def test_iec61131_interfaces_array_initial_elements1_constructor_exists():
    assert callable(iec61131_interfaces_Array_Initial_Elements1.__init__)


def test_iec61131_interfaces_array_initial_elements1_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Array_Initial_Elements1.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_array_initial_elements2_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Array_Initial_Elements2)


def test_iec61131_interfaces_array_initial_elements2_constructor_exists():
    assert callable(iec61131_interfaces_Array_Initial_Elements2.__init__)


def test_iec61131_interfaces_array_initial_elements2_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Array_Initial_Elements2.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_array_initialization_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Array_Initialization)


def test_iec61131_interfaces_array_initialization_constructor_exists():
    assert callable(iec61131_interfaces_Array_Initialization.__init__)


def test_iec61131_interfaces_array_initialization_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Array_Initialization.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_var1_list_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Var1_List)


def test_iec61131_interfaces_var1_list_constructor_exists():
    assert callable(iec61131_interfaces_Var1_List.__init__)


def test_iec61131_interfaces_var1_list_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Var1_List.__init__)
    params = list(sig.parameters.keys())



def test_double_bstring_is_not_abstract():
    assert not inspect.isabstract(Double_BString)


def test_double_bstring_constructor_exists():
    assert callable(Double_BString.__init__)


def test_double_bstring_constructor_args():
    sig = inspect.signature(Double_BString.__init__)
    params = list(sig.parameters.keys())



def test_double_byte_character_string_is_not_abstract():
    assert not inspect.isabstract(Double_Byte_Character_String)


def test_double_byte_character_string_constructor_exists():
    assert callable(Double_Byte_Character_String.__init__)


def test_double_byte_character_string_constructor_args():
    sig = inspect.signature(Double_Byte_Character_String.__init__)
    params = list(sig.parameters.keys())



def test_single_bstring_is_not_abstract():
    assert not inspect.isabstract(Single_BString)


def test_single_bstring_constructor_exists():
    assert callable(Single_BString.__init__)


def test_single_bstring_constructor_args():
    sig = inspect.signature(Single_BString.__init__)
    params = list(sig.parameters.keys())



def test_single_byte_character_string_is_not_abstract():
    assert not inspect.isabstract(Single_Byte_Character_String)


def test_single_byte_character_string_constructor_exists():
    assert callable(Single_Byte_Character_String.__init__)


def test_single_byte_character_string_constructor_args():
    sig = inspect.signature(Single_Byte_Character_String.__init__)
    params = list(sig.parameters.keys())



def test_located_var_spec_init_is_not_abstract():
    assert not inspect.isabstract(Located_Var_Spec_Init)


def test_located_var_spec_init_constructor_exists():
    assert callable(Located_Var_Spec_Init.__init__)


def test_located_var_spec_init_constructor_args():
    sig = inspect.signature(Located_Var_Spec_Init.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_double_byte_string_spec_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Double_Byte_String_Spec)


def test_iec61131_interfaces_double_byte_string_spec_constructor_exists():
    assert callable(iec61131_interfaces_Double_Byte_String_Spec.__init__)


def test_iec61131_interfaces_double_byte_string_spec_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Double_Byte_String_Spec.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_single_byte_string_spec_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Single_Byte_String_Spec)


def test_iec61131_interfaces_single_byte_string_spec_constructor_exists():
    assert callable(iec61131_interfaces_Single_Byte_String_Spec.__init__)


def test_iec61131_interfaces_single_byte_string_spec_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Single_Byte_String_Spec.__init__)
    params = list(sig.parameters.keys())



def test_double_byte_string_spec_is_not_abstract():
    assert not inspect.isabstract(Double_Byte_String_Spec)


def test_double_byte_string_spec_constructor_exists():
    assert callable(Double_Byte_String_Spec.__init__)


def test_double_byte_string_spec_constructor_args():
    sig = inspect.signature(Double_Byte_String_Spec.__init__)
    params = list(sig.parameters.keys())



def test_single_byte_string_spec_is_not_abstract():
    assert not inspect.isabstract(Single_Byte_String_Spec)


def test_single_byte_string_spec_constructor_exists():
    assert callable(Single_Byte_String_Spec.__init__)


def test_single_byte_string_spec_constructor_args():
    sig = inspect.signature(Single_Byte_String_Spec.__init__)
    params = list(sig.parameters.keys())



def test_string_var_declaration_is_not_abstract():
    assert not inspect.isabstract(String_Var_Declaration)


def test_string_var_declaration_constructor_exists():
    assert callable(String_Var_Declaration.__init__)


def test_string_var_declaration_constructor_args():
    sig = inspect.signature(String_Var_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_double_byte_string_var_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Double_Byte_String_Var_Declaration)


def test_iec61131_interfaces_double_byte_string_var_declaration_constructor_exists():
    assert callable(iec61131_interfaces_Double_Byte_String_Var_Declaration.__init__)


def test_iec61131_interfaces_double_byte_string_var_declaration_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Double_Byte_String_Var_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_single_byte_string_var_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Single_Byte_String_Var_Declaration)


def test_iec61131_interfaces_single_byte_string_var_declaration_constructor_exists():
    assert callable(iec61131_interfaces_Single_Byte_String_Var_Declaration.__init__)


def test_iec61131_interfaces_single_byte_string_var_declaration_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Single_Byte_String_Var_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_range_is_not_abstract():
    assert not inspect.isabstract(Range)


def test_range_constructor_exists():
    assert callable(Range.__init__)


def test_range_constructor_args():
    sig = inspect.signature(Range.__init__)
    params = list(sig.parameters.keys())



def test_case_list_element_is_not_abstract():
    assert not inspect.isabstract(Case_List_Element)


def test_case_list_element_constructor_exists():
    assert callable(Case_List_Element.__init__)


def test_case_list_element_constructor_args():
    sig = inspect.signature(Case_List_Element.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_subrange_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Subrange)


def test_iec61131_interfaces_subrange_constructor_exists():
    assert callable(iec61131_interfaces_Subrange.__init__)


def test_iec61131_interfaces_subrange_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Subrange.__init__)
    params = list(sig.parameters.keys())
    assert "delimiter" in params, "Missing parameter 'delimiter'"

def test_iec61131_interfaces_subrange_has_delimiter():
    assert hasattr(iec61131_interfaces_Subrange, "delimiter")
    descriptor = None
    for klass in iec61131_interfaces_Subrange.__mro__:
        if "delimiter" in klass.__dict__:
            descriptor = klass.__dict__["delimiter"]
            break
    assert isinstance(descriptor, property)



def test_iec61131_interfaces_array_initial_elements_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Array_Initial_Elements)


def test_iec61131_interfaces_array_initial_elements_constructor_exists():
    assert callable(iec61131_interfaces_Array_Initial_Elements.__init__)


def test_iec61131_interfaces_array_initial_elements_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Array_Initial_Elements.__init__)
    params = list(sig.parameters.keys())



def test_interfaces_var_spec_is_not_abstract():
    assert not inspect.isabstract(interfaces_Var_Spec)


def test_interfaces_var_spec_constructor_exists():
    assert callable(interfaces_Var_Spec.__init__)


def test_interfaces_var_spec_constructor_args():
    sig = inspect.signature(interfaces_Var_Spec.__init__)
    params = list(sig.parameters.keys())



def test_interfaces_external_specification_is_not_abstract():
    assert not inspect.isabstract(interfaces_External_Specification)


def test_interfaces_external_specification_constructor_exists():
    assert callable(interfaces_External_Specification.__init__)


def test_interfaces_external_specification_constructor_args():
    sig = inspect.signature(interfaces_External_Specification.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_pous_function_block_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_pous_Function_Block_Type_Name)


def test_iec61131_pous_function_block_type_name_constructor_exists():
    assert callable(iec61131_pous_Function_Block_Type_Name.__init__)


def test_iec61131_pous_function_block_type_name_constructor_args():
    sig = inspect.signature(iec61131_pous_Function_Block_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_array_specification_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Array_Specification)


def test_iec61131_interfaces_array_specification_constructor_exists():
    assert callable(iec61131_interfaces_Array_Specification.__init__)


def test_iec61131_interfaces_array_specification_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Array_Specification.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_types_structure_type_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_types_Structure_Type_Name)


def test_iec61131_types_structure_type_name_constructor_exists():
    assert callable(iec61131_types_Structure_Type_Name.__init__)


def test_iec61131_types_structure_type_name_constructor_args():
    sig = inspect.signature(iec61131_types_Structure_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_interfaces_specification_is_not_abstract():
    assert not inspect.isabstract(interfaces_Specification)


def test_interfaces_specification_constructor_exists():
    assert callable(interfaces_Specification.__init__)


def test_interfaces_specification_constructor_args():
    sig = inspect.signature(interfaces_Specification.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_enumerated_specification_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Enumerated_Specification)


def test_iec61131_interfaces_enumerated_specification_constructor_exists():
    assert callable(iec61131_interfaces_Enumerated_Specification.__init__)


def test_iec61131_interfaces_enumerated_specification_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Enumerated_Specification.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_subrange_specification_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Subrange_Specification)


def test_iec61131_interfaces_subrange_specification_constructor_exists():
    assert callable(iec61131_interfaces_Subrange_Specification.__init__)


def test_iec61131_interfaces_subrange_specification_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Subrange_Specification.__init__)
    params = list(sig.parameters.keys())



def test_interfaces_var2_init_decl_is_not_abstract():
    assert not inspect.isabstract(interfaces_Var2_Init_Decl)


def test_interfaces_var2_init_decl_constructor_exists():
    assert callable(interfaces_Var2_Init_Decl.__init__)


def test_interfaces_var2_init_decl_constructor_args():
    sig = inspect.signature(interfaces_Var2_Init_Decl.__init__)
    params = list(sig.parameters.keys())



def test_interfaces_temp_var_decl_is_not_abstract():
    assert not inspect.isabstract(interfaces_Temp_Var_Decl)


def test_interfaces_temp_var_decl_constructor_exists():
    assert callable(interfaces_Temp_Var_Decl.__init__)


def test_interfaces_temp_var_decl_constructor_args():
    sig = inspect.signature(interfaces_Temp_Var_Decl.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_string_var_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_String_Var_Declaration)


def test_iec61131_interfaces_string_var_declaration_constructor_exists():
    assert callable(iec61131_interfaces_String_Var_Declaration.__init__)


def test_iec61131_interfaces_string_var_declaration_constructor_args():
    sig = inspect.signature(iec61131_interfaces_String_Var_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_function_block_type_name_is_not_abstract():
    assert not inspect.isabstract(Function_Block_Type_Name)


def test_function_block_type_name_constructor_exists():
    assert callable(Function_Block_Type_Name.__init__)


def test_function_block_type_name_constructor_args():
    sig = inspect.signature(Function_Block_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_structure_initialization_is_not_abstract():
    assert not inspect.isabstract(Structure_Initialization)


def test_structure_initialization_constructor_exists():
    assert callable(Structure_Initialization.__init__)


def test_structure_initialization_constructor_args():
    sig = inspect.signature(Structure_Initialization.__init__)
    params = list(sig.parameters.keys())



def test_temp_var_declaration_is_not_abstract():
    assert not inspect.isabstract(Temp_Var_Declaration)


def test_temp_var_declaration_constructor_exists():
    assert callable(Temp_Var_Declaration.__init__)


def test_temp_var_declaration_constructor_args():
    sig = inspect.signature(Temp_Var_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_var1_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Var1_Declaration)


def test_iec61131_interfaces_var1_declaration_constructor_exists():
    assert callable(iec61131_interfaces_Var1_Declaration.__init__)


def test_iec61131_interfaces_var1_declaration_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Var1_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_structured_var_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Structured_Var_Declaration)


def test_iec61131_interfaces_structured_var_declaration_constructor_exists():
    assert callable(iec61131_interfaces_Structured_Var_Declaration.__init__)


def test_iec61131_interfaces_structured_var_declaration_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Structured_Var_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_array_var_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Array_Var_Declaration)


def test_iec61131_interfaces_array_var_declaration_constructor_exists():
    assert callable(iec61131_interfaces_Array_Var_Declaration.__init__)


def test_iec61131_interfaces_array_var_declaration_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Array_Var_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_fb_name_decl_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Fb_Name_Decl)


def test_iec61131_interfaces_fb_name_decl_constructor_exists():
    assert callable(iec61131_interfaces_Fb_Name_Decl.__init__)


def test_iec61131_interfaces_fb_name_decl_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Fb_Name_Decl.__init__)
    params = list(sig.parameters.keys())



def test_enumerated_type_name_is_not_abstract():
    assert not inspect.isabstract(Enumerated_Type_Name)


def test_enumerated_type_name_constructor_exists():
    assert callable(Enumerated_Type_Name.__init__)


def test_enumerated_type_name_constructor_args():
    sig = inspect.signature(Enumerated_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_enumerated_value_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Enumerated_Value)


def test_iec61131_interfaces_enumerated_value_constructor_exists():
    assert callable(iec61131_interfaces_Enumerated_Value.__init__)


def test_iec61131_interfaces_enumerated_value_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Enumerated_Value.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iec61131_interfaces_enumerated_value_has_name():
    assert hasattr(iec61131_interfaces_Enumerated_Value, "name")
    descriptor = None
    for klass in iec61131_interfaces_Enumerated_Value.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iec61131_interfaces_structure_element_name_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Structure_Element_Name)


def test_iec61131_interfaces_structure_element_name_constructor_exists():
    assert callable(iec61131_interfaces_Structure_Element_Name.__init__)


def test_iec61131_interfaces_structure_element_name_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Structure_Element_Name.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iec61131_interfaces_structure_element_name_has_name():
    assert hasattr(iec61131_interfaces_Structure_Element_Name, "name")
    descriptor = None
    for klass in iec61131_interfaces_Structure_Element_Name.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_initial_element_is_not_abstract():
    assert not inspect.isabstract(Initial_Element)


def test_initial_element_constructor_exists():
    assert callable(Initial_Element.__init__)


def test_initial_element_constructor_args():
    sig = inspect.signature(Initial_Element.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_initelement_constant_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_InitElement_Constant)


def test_iec61131_interfaces_initelement_constant_constructor_exists():
    assert callable(iec61131_interfaces_InitElement_Constant.__init__)


def test_iec61131_interfaces_initelement_constant_constructor_args():
    sig = inspect.signature(iec61131_interfaces_InitElement_Constant.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_initelement_array_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_InitElement_Array)


def test_iec61131_interfaces_initelement_array_constructor_exists():
    assert callable(iec61131_interfaces_InitElement_Array.__init__)


def test_iec61131_interfaces_initelement_array_constructor_args():
    sig = inspect.signature(iec61131_interfaces_InitElement_Array.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_initelement_enumvalue_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_InitElement_EnumValue)


def test_iec61131_interfaces_initelement_enumvalue_constructor_exists():
    assert callable(iec61131_interfaces_InitElement_EnumValue.__init__)


def test_iec61131_interfaces_initelement_enumvalue_constructor_args():
    sig = inspect.signature(iec61131_interfaces_InitElement_EnumValue.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_initelement_structure_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_InitElement_Structure)


def test_iec61131_interfaces_initelement_structure_constructor_exists():
    assert callable(iec61131_interfaces_InitElement_Structure.__init__)


def test_iec61131_interfaces_initelement_structure_constructor_args():
    sig = inspect.signature(iec61131_interfaces_InitElement_Structure.__init__)
    params = list(sig.parameters.keys())



def test_structure_element_name_is_not_abstract():
    assert not inspect.isabstract(Structure_Element_Name)


def test_structure_element_name_constructor_exists():
    assert callable(Structure_Element_Name.__init__)


def test_structure_element_name_constructor_args():
    sig = inspect.signature(Structure_Element_Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_structure_element_initialization_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Structure_Element_Initialization)


def test_iec61131_interfaces_structure_element_initialization_constructor_exists():
    assert callable(iec61131_interfaces_Structure_Element_Initialization.__init__)


def test_iec61131_interfaces_structure_element_initialization_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Structure_Element_Initialization.__init__)
    params = list(sig.parameters.keys())



def test_structure_element_initialization_is_not_abstract():
    assert not inspect.isabstract(Structure_Element_Initialization)


def test_structure_element_initialization_constructor_exists():
    assert callable(Structure_Element_Initialization.__init__)


def test_structure_element_initialization_constructor_args():
    sig = inspect.signature(Structure_Element_Initialization.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_structure_initialization_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Structure_Initialization)


def test_iec61131_interfaces_structure_initialization_constructor_exists():
    assert callable(iec61131_interfaces_Structure_Initialization.__init__)


def test_iec61131_interfaces_structure_initialization_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Structure_Initialization.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_var_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Var_Declaration)


def test_iec61131_interfaces_var_declaration_constructor_exists():
    assert callable(iec61131_interfaces_Var_Declaration.__init__)


def test_iec61131_interfaces_var_declaration_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Var_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_structure_type_name_is_not_abstract():
    assert not inspect.isabstract(Structure_Type_Name)


def test_structure_type_name_constructor_exists():
    assert callable(Structure_Type_Name.__init__)


def test_structure_type_name_constructor_args():
    sig = inspect.signature(Structure_Type_Name.__init__)
    params = list(sig.parameters.keys())



def test_pous_structure_specification_is_not_abstract():
    assert not inspect.isabstract(pous_Structure_Specification)


def test_pous_structure_specification_constructor_exists():
    assert callable(pous_Structure_Specification.__init__)


def test_pous_structure_specification_constructor_args():
    sig = inspect.signature(pous_Structure_Specification.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_initialized_structure_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Initialized_Structure)


def test_iec61131_interfaces_initialized_structure_constructor_exists():
    assert callable(iec61131_interfaces_Initialized_Structure.__init__)


def test_iec61131_interfaces_initialized_structure_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Initialized_Structure.__init__)
    params = list(sig.parameters.keys())



def test_array_specification_is_not_abstract():
    assert not inspect.isabstract(Array_Specification)


def test_array_specification_constructor_exists():
    assert callable(Array_Specification.__init__)


def test_array_specification_constructor_args():
    sig = inspect.signature(Array_Specification.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_array_specification1_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Array_Specification1)


def test_iec61131_interfaces_array_specification1_constructor_exists():
    assert callable(iec61131_interfaces_Array_Specification1.__init__)


def test_iec61131_interfaces_array_specification1_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Array_Specification1.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_array_specification2_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Array_Specification2)


def test_iec61131_interfaces_array_specification2_constructor_exists():
    assert callable(iec61131_interfaces_Array_Specification2.__init__)


def test_iec61131_interfaces_array_specification2_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Array_Specification2.__init__)
    params = list(sig.parameters.keys())



def test_array_initialization_is_not_abstract():
    assert not inspect.isabstract(Array_Initialization)


def test_array_initialization_constructor_exists():
    assert callable(Array_Initialization.__init__)


def test_array_initialization_constructor_args():
    sig = inspect.signature(Array_Initialization.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_array_spec_init_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Array_Spec_Init)


def test_iec61131_interfaces_array_spec_init_constructor_exists():
    assert callable(iec61131_interfaces_Array_Spec_Init.__init__)


def test_iec61131_interfaces_array_spec_init_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Array_Spec_Init.__init__)
    params = list(sig.parameters.keys())



def test_var_declaration_is_not_abstract():
    assert not inspect.isabstract(Var_Declaration)


def test_var_declaration_constructor_exists():
    assert callable(Var_Declaration.__init__)


def test_var_declaration_constructor_args():
    sig = inspect.signature(Var_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_temp_var_decl_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Temp_Var_Decl)


def test_iec61131_interfaces_temp_var_decl_constructor_exists():
    assert callable(iec61131_interfaces_Temp_Var_Decl.__init__)


def test_iec61131_interfaces_temp_var_decl_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Temp_Var_Decl.__init__)
    params = list(sig.parameters.keys())



def test_var1_specification_is_not_abstract():
    assert not inspect.isabstract(Var1_Specification)


def test_var1_specification_constructor_exists():
    assert callable(Var1_Specification.__init__)


def test_var1_specification_constructor_args():
    sig = inspect.signature(Var1_Specification.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_var1_specification_func_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Var1_Specification_Func)


def test_iec61131_interfaces_var1_specification_func_constructor_exists():
    assert callable(iec61131_interfaces_Var1_Specification_Func.__init__)


def test_iec61131_interfaces_var1_specification_func_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Var1_Specification_Func.__init__)
    params = list(sig.parameters.keys())



def test_var_init_decl_is_not_abstract():
    assert not inspect.isabstract(Var_Init_Decl)


def test_var_init_decl_constructor_exists():
    assert callable(Var_Init_Decl.__init__)


def test_var_init_decl_constructor_args():
    sig = inspect.signature(Var_Init_Decl.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_var2_init_decl_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Var2_Init_Decl)


def test_iec61131_interfaces_var2_init_decl_constructor_exists():
    assert callable(iec61131_interfaces_Var2_Init_Decl.__init__)


def test_iec61131_interfaces_var2_init_decl_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Var2_Init_Decl.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_var1_init_decl_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Var1_Init_Decl)


def test_iec61131_interfaces_var1_init_decl_constructor_exists():
    assert callable(iec61131_interfaces_Var1_Init_Decl.__init__)


def test_iec61131_interfaces_var1_init_decl_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Var1_Init_Decl.__init__)
    params = list(sig.parameters.keys())



def test_var1_list_is_not_abstract():
    assert not inspect.isabstract(Var1_List)


def test_var1_list_constructor_exists():
    assert callable(Var1_List.__init__)


def test_var1_list_constructor_args():
    sig = inspect.signature(Var1_List.__init__)
    params = list(sig.parameters.keys())



def test_input_declaration_is_not_abstract():
    assert not inspect.isabstract(Input_Declaration)


def test_input_declaration_constructor_exists():
    assert callable(Input_Declaration.__init__)


def test_input_declaration_constructor_args():
    sig = inspect.signature(Input_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_var_init_decl_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Var_Init_Decl)


def test_iec61131_interfaces_var_init_decl_constructor_exists():
    assert callable(iec61131_interfaces_Var_Init_Decl.__init__)


def test_iec61131_interfaces_var_init_decl_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Var_Init_Decl.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_edge_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Edge_Declaration)


def test_iec61131_interfaces_edge_declaration_constructor_exists():
    assert callable(iec61131_interfaces_Edge_Declaration.__init__)


def test_iec61131_interfaces_edge_declaration_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Edge_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "edge" in params, "Missing parameter 'edge'"

def test_iec61131_interfaces_edge_declaration_has_edge():
    assert hasattr(iec61131_interfaces_Edge_Declaration, "edge")
    descriptor = None
    for klass in iec61131_interfaces_Edge_Declaration.__mro__:
        if "edge" in klass.__dict__:
            descriptor = klass.__dict__["edge"]
            break
    assert isinstance(descriptor, property)



def test_io_var_declaration_is_not_abstract():
    assert not inspect.isabstract(Io_Var_Declaration)


def test_io_var_declaration_constructor_exists():
    assert callable(Io_Var_Declaration.__init__)


def test_io_var_declaration_constructor_args():
    sig = inspect.signature(Io_Var_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_input_output_declarations_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Input_Output_Declarations)


def test_iec61131_interfaces_input_output_declarations_constructor_exists():
    assert callable(iec61131_interfaces_Input_Output_Declarations.__init__)


def test_iec61131_interfaces_input_output_declarations_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Input_Output_Declarations.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_output_declarations_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Output_Declarations)


def test_iec61131_interfaces_output_declarations_constructor_exists():
    assert callable(iec61131_interfaces_Output_Declarations.__init__)


def test_iec61131_interfaces_output_declarations_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Output_Declarations.__init__)
    params = list(sig.parameters.keys())
    assert "retain" in params, "Missing parameter 'retain'"

def test_iec61131_interfaces_output_declarations_has_retain():
    assert hasattr(iec61131_interfaces_Output_Declarations, "retain")
    descriptor = None
    for klass in iec61131_interfaces_Output_Declarations.__mro__:
        if "retain" in klass.__dict__:
            descriptor = klass.__dict__["retain"]
            break
    assert isinstance(descriptor, property)



def test_iec61131_interfaces_input_declarations_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Input_Declarations)


def test_iec61131_interfaces_input_declarations_constructor_exists():
    assert callable(iec61131_interfaces_Input_Declarations.__init__)


def test_iec61131_interfaces_input_declarations_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Input_Declarations.__init__)
    params = list(sig.parameters.keys())
    assert "retain" in params, "Missing parameter 'retain'"

def test_iec61131_interfaces_input_declarations_has_retain():
    assert hasattr(iec61131_interfaces_Input_Declarations, "retain")
    descriptor = None
    for klass in iec61131_interfaces_Input_Declarations.__mro__:
        if "retain" in klass.__dict__:
            descriptor = klass.__dict__["retain"]
            break
    assert isinstance(descriptor, property)



def test_pous_function_vars_is_not_abstract():
    assert not inspect.isabstract(pous_Function_Vars)


def test_pous_function_vars_constructor_exists():
    assert callable(pous_Function_Vars.__init__)


def test_pous_function_vars_constructor_args():
    sig = inspect.signature(pous_Function_Vars.__init__)
    params = list(sig.parameters.keys())



def test_pous_program_vars_is_not_abstract():
    assert not inspect.isabstract(pous_Program_Vars)


def test_pous_program_vars_constructor_exists():
    assert callable(pous_Program_Vars.__init__)


def test_pous_program_vars_constructor_args():
    sig = inspect.signature(pous_Program_Vars.__init__)
    params = list(sig.parameters.keys())



def test_pous_function_block_vars_is_not_abstract():
    assert not inspect.isabstract(pous_Function_Block_Vars)


def test_pous_function_block_vars_constructor_exists():
    assert callable(pous_Function_Block_Vars.__init__)


def test_pous_function_block_vars_constructor_args():
    sig = inspect.signature(pous_Function_Block_Vars.__init__)
    params = list(sig.parameters.keys())



def test_interfaces_interface_is_not_abstract():
    assert not inspect.isabstract(interfaces_Interface)


def test_interfaces_interface_constructor_exists():
    assert callable(interfaces_Interface.__init__)


def test_interfaces_interface_constructor_args():
    sig = inspect.signature(interfaces_Interface.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_function_var_decl_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Function_Var_Decl)


def test_iec61131_interfaces_function_var_decl_constructor_exists():
    assert callable(iec61131_interfaces_Function_Var_Decl.__init__)


def test_iec61131_interfaces_function_var_decl_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Function_Var_Decl.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"

def test_iec61131_interfaces_function_var_decl_has_constant():
    assert hasattr(iec61131_interfaces_Function_Var_Decl, "constant")
    descriptor = None
    for klass in iec61131_interfaces_Function_Var_Decl.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_iec61131_interfaces_io_var_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Io_Var_Declaration)


def test_iec61131_interfaces_io_var_declaration_constructor_exists():
    assert callable(iec61131_interfaces_Io_Var_Declaration.__init__)


def test_iec61131_interfaces_io_var_declaration_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Io_Var_Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131_interfaces_other_var_declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131_interfaces_Other_Var_Declaration)


def test_iec61131_interfaces_other_var_declaration_constructor_exists():
    assert callable(iec61131_interfaces_Other_Var_Declaration.__init__)


def test_iec61131_interfaces_other_var_declaration_constructor_args():
    sig = inspect.signature(iec61131_interfaces_Other_Var_Declaration.__init__)
    params = list(sig.parameters.keys())

def test_edge_exists():
    # Check that the Enumeration exists
    assert Edge is not None

def test_edge_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Edge]
    expected_literals = [
        "R_EDGE",
        "F_EDGE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Edge"

def test_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "READ_WRITE",
        "READ_ONLY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Output_Reference_strategy = st.builds(
    Output_Reference,
)
variables_Symbolic_Variable_strategy = st.builds(
    variables_Symbolic_Variable,
)
pous_Function_Return_Value_strategy = st.builds(
    pous_Function_Return_Value,
)
types_Data_Type_Name_strategy = st.builds(
    types_Data_Type_Name,
)
iec61131_types_Non_Generic_Type_Name_strategy = st.builds(
    iec61131_types_Non_Generic_Type_Name,
)
interfaces_Simple_Specification_Func_strategy = st.builds(
    interfaces_Simple_Specification_Func,
)
types_Non_Generic_Type_Name_strategy = st.builds(
    types_Non_Generic_Type_Name,
)
Numeric_Type_Name_strategy = st.builds(
    Numeric_Type_Name,
)
iec61131_types_Real_Type_Name_strategy = st.builds(
    iec61131_types_Real_Type_Name,
)
iec61131_types_Integer_Type_Name_strategy = st.builds(
    iec61131_types_Integer_Type_Name,
)
Elementary_Type_Name_strategy = st.builds(
    Elementary_Type_Name,
)
iec61131_types_Bit_String_Type_Name_strategy = st.builds(
    iec61131_types_Bit_String_Type_Name,
)
iec61131_types_Date_Type_Name_strategy = st.builds(
    iec61131_types_Date_Type_Name,
)
iec61131_types_Numeric_Type_Name_strategy = st.builds(
    iec61131_types_Numeric_Type_Name,
)
Data_Type_Name_strategy = st.builds(
    Data_Type_Name,
)
iec61131_types_TypeLib_strategy = st.builds(
    iec61131_types_TypeLib,
)
Fbd_Network_strategy = st.builds(
    Fbd_Network,
)
iec61131_sfc_Transition_Condition_strategy = st.builds(
    iec61131_sfc_Transition_Condition,
)
iec61131_sfc_Steps_strategy = st.builds(
    iec61131_sfc_Steps,
)
iec61131_sfc_Transition_Name_strategy = st.builds(
    iec61131_sfc_Transition_Name,
    name=
        safe_text
)
iec61131_sfc_Action_Time_strategy = st.builds(
    iec61131_sfc_Action_Time,
)
variables_Variable_strategy = st.builds(
    variables_Variable,
)
Subscript_List_strategy = st.builds(
    Subscript_List,
)
Multi_Element_Variable_strategy = st.builds(
    Multi_Element_Variable,
)
iec61131_variables_Structured_Variable_strategy = st.builds(
    iec61131_variables_Structured_Variable,
)
iec61131_variables_Array_Variable_strategy = st.builds(
    iec61131_variables_Array_Variable,
)
iec61131_sfc_Cond2_Condition_strategy = st.builds(
    iec61131_sfc_Cond2_Condition,
)
Cond2_Condition_strategy = st.builds(
    Cond2_Condition,
)
iec61131_fbd_Fbd_Network_strategy = st.builds(
    iec61131_fbd_Fbd_Network,
)
Steps_strategy = st.builds(
    Steps,
)
iec61131_sfc_Steps2_strategy = st.builds(
    iec61131_sfc_Steps2,
)
iec61131_sfc_Steps1_strategy = st.builds(
    iec61131_sfc_Steps1,
)
Transition_Name_strategy = st.builds(
    Transition_Name,
)
sfc_Step_Types_strategy = st.builds(
    sfc_Step_Types,
)
sfc_Sfc_Elements_strategy = st.builds(
    sfc_Sfc_Elements,
)
iec61131_sfc_Step_strategy = st.builds(
    iec61131_sfc_Step,
)
Step_Types_strategy = st.builds(
    Step_Types,
)
iec61131_sfc_Initial_Step_strategy = st.builds(
    iec61131_sfc_Initial_Step,
)
Sfc_Elements_strategy = st.builds(
    Sfc_Elements,
)
iec61131_sfc_Transition_strategy = st.builds(
    iec61131_sfc_Transition,
)
Initial_Step_strategy = st.builds(
    Initial_Step,
)
iec61131_sfc_Timed_Qualifier_strategy = st.builds(
    iec61131_sfc_Timed_Qualifier,
    qualifier=
        safe_text
)
Action_Time_strategy = st.builds(
    Action_Time,
)
iec61131_sfc_ActionTime2_strategy = st.builds(
    iec61131_sfc_ActionTime2,
)
Timed_Qualifier_strategy = st.builds(
    Timed_Qualifier,
)
iec61131_sfc_Action_Qualifier_strategy = st.builds(
    iec61131_sfc_Action_Qualifier,
    qualifier=
        safe_text
)
iec61131_sfc_Action_Name_strategy = st.builds(
    iec61131_sfc_Action_Name,
    name=
        safe_text
)
Step_Name_strategy = st.builds(
    Step_Name,
)
Action_Association_strategy = st.builds(
    Action_Association,
)
iec61131_sfc_Step_Types_strategy = st.builds(
    iec61131_sfc_Step_Types,
)
Action_Qualifier_strategy = st.builds(
    Action_Qualifier,
)
iec61131_sfc_Action_Association_strategy = st.builds(
    iec61131_sfc_Action_Association,
)
iec61131_sfc_Sfc_Elements_strategy = st.builds(
    iec61131_sfc_Sfc_Elements,
)
Action_Name_strategy = st.builds(
    Action_Name,
)
iec61131_sfc_Action_strategy = st.builds(
    iec61131_sfc_Action,
)
Transition_Condition_strategy = st.builds(
    Transition_Condition,
)
iec61131_sfc_Transition_Cond2_strategy = st.builds(
    iec61131_sfc_Transition_Cond2,
)
iec61131_sfc_Transition_Cond3_strategy = st.builds(
    iec61131_sfc_Transition_Cond3,
)
iec61131_sfc_Transition_Cond1_strategy = st.builds(
    iec61131_sfc_Transition_Cond1,
)
iec61131_sfc_Sfc_Network_strategy = st.builds(
    iec61131_sfc_Sfc_Network,
)
Sfc_Network_strategy = st.builds(
    Sfc_Network,
)
iec61131_il_Il_Assign_Out_Operator_strategy = st.builds(
    iec61131_il_Il_Assign_Out_Operator,
)
iec61131_il_Param_Assignment_strategy = st.builds(
    iec61131_il_Param_Assignment,
)
Assignment_Name_strategy = st.builds(
    Assignment_Name,
)
iec61131_il_Il_Assign_Operator_strategy = st.builds(
    iec61131_il_Il_Assign_Operator,
)
iec61131_il_Param_Instruction_strategy = st.builds(
    iec61131_il_Param_Instruction,
)
iec61131_il_Param_Assignments_strategy = st.builds(
    iec61131_il_Param_Assignments,
)
Il_Assign_Out_Operator_strategy = st.builds(
    Il_Assign_Out_Operator,
)
iec61131_il_Il_Operand_List_strategy = st.builds(
    iec61131_il_Il_Operand_List,
)
iec61131_il_Il_Simple_Operator_strategy = st.builds(
    iec61131_il_Il_Simple_Operator,
)
iec61131_il_Il_Operations_strategy = st.builds(
    iec61131_il_Il_Operations,
)
Il_Param_List_strategy = st.builds(
    Il_Param_List,
)
Il_Assign_Operator_strategy = st.builds(
    Il_Assign_Operator,
)
Param_Assignments_strategy = st.builds(
    Param_Assignments,
)
iec61131_il_Il_Param_Out_Assignment_strategy = st.builds(
    iec61131_il_Il_Param_Out_Assignment,
)
iec61131_il_Il_Param_Assignment_strategy = st.builds(
    iec61131_il_Il_Param_Assignment,
)
Param_Instruction_strategy = st.builds(
    Param_Instruction,
)
iec61131_il_Il_Param_Last_Instruction_strategy = st.builds(
    iec61131_il_Il_Param_Last_Instruction,
)
iec61131_il_Il_Param_Instruction_strategy = st.builds(
    iec61131_il_Il_Param_Instruction,
)
iec61131_il_Simple_Instr_strategy = st.builds(
    iec61131_il_Simple_Instr,
)
Simple_Instr_strategy = st.builds(
    Simple_Instr,
)
iec61131_il_Il_Simple_Instruction_strategy = st.builds(
    iec61131_il_Il_Simple_Instruction,
)
iec61131_il_Operands_strategy = st.builds(
    iec61131_il_Operands,
)
Il_Param_Last_Instruction_strategy = st.builds(
    Il_Param_Last_Instruction,
)
Il_Param_Instruction_strategy = st.builds(
    Il_Param_Instruction,
)
iec61131_il_Il_Param_List_strategy = st.builds(
    iec61131_il_Il_Param_List,
)
iec61131_il_Il_Call_Operator_strategy = st.builds(
    iec61131_il_Il_Call_Operator,
)
iec61131_il_Il_Jump_Operator_strategy = st.builds(
    iec61131_il_Il_Jump_Operator,
)
Il_Operand_List_strategy = st.builds(
    Il_Operand_List,
)
Il_Simple_Operator_strategy = st.builds(
    Il_Simple_Operator,
)
iec61131_il_Il_Expr_Operator_strategy = st.builds(
    iec61131_il_Il_Expr_Operator,
)
Il_Simple_Operation_strategy = st.builds(
    Il_Simple_Operation,
)
iec61131_il_Simple_Operation2_strategy = st.builds(
    iec61131_il_Simple_Operation2,
)
iec61131_il_Simple_Operation1_strategy = st.builds(
    iec61131_il_Simple_Operation1,
)
Il_Instruction_strategy = st.builds(
    Il_Instruction,
)
Operands_strategy = st.builds(
    Operands,
)
iec61131_il_Operand1_strategy = st.builds(
    iec61131_il_Operand1,
)
iec61131_il_Operand2_strategy = st.builds(
    iec61131_il_Operand2,
)
Il_Call_Operator_strategy = st.builds(
    Il_Call_Operator,
)
Il_Jump_Operator_strategy = st.builds(
    Il_Jump_Operator,
)
Simple_Instr_List_strategy = st.builds(
    Simple_Instr_List,
)
Il_Operand_strategy = st.builds(
    Il_Operand,
)
il_Simple_Instr_strategy = st.builds(
    il_Simple_Instr,
)
il_Il_Operations_strategy = st.builds(
    il_Il_Operations,
)
iec61131_il_Il_Formal_Funct_Call_strategy = st.builds(
    iec61131_il_Il_Formal_Funct_Call,
)
iec61131_il_Il_Expression_strategy = st.builds(
    iec61131_il_Il_Expression,
)
iec61131_il_Il_Simple_Operation_strategy = st.builds(
    iec61131_il_Il_Simple_Operation,
)
iec61131_il_Label_strategy = st.builds(
    iec61131_il_Label,
    label=
        safe_text
)
Il_Operations_strategy = st.builds(
    Il_Operations,
)
iec61131_il_Il_Return_Operator_strategy = st.builds(
    iec61131_il_Il_Return_Operator,
)
iec61131_il_Il_Fb_Call_strategy = st.builds(
    iec61131_il_Il_Fb_Call,
)
iec61131_il_Il_Jump_Operation_strategy = st.builds(
    iec61131_il_Il_Jump_Operation,
)
Label_strategy = st.builds(
    Label,
)
iec61131_il_Il_Instruction_strategy = st.builds(
    iec61131_il_Il_Instruction,
)
Il_Simple_Instruction_strategy = st.builds(
    Il_Simple_Instruction,
)
iec61131_il_Simple_Instr_List_strategy = st.builds(
    iec61131_il_Simple_Instr_List,
)
Unary_Operator_strategy = st.builds(
    Unary_Operator,
)
Power_Symbol_strategy = st.builds(
    Power_Symbol,
)
Structured_Variable_strategy = st.builds(
    Structured_Variable,
)
Array_Variable_strategy = st.builds(
    Array_Variable,
)
Function_Name_strategy = st.builds(
    Function_Name,
)
Primary_Expression_strategy = st.builds(
    Primary_Expression,
)
iec61131_st_Expression_Constant_strategy = st.builds(
    iec61131_st_Expression_Constant,
)
iec61131_st_Expression_Variable_Type_strategy = st.builds(
    iec61131_st_Expression_Variable_Type,
)
iec61131_st_Call_Expression_strategy = st.builds(
    iec61131_st_Call_Expression,
)
iec61131_st_Expression_EnumValue_strategy = st.builds(
    iec61131_st_Expression_EnumValue,
)
iec61131_st_Bracket_Expression_strategy = st.builds(
    iec61131_st_Bracket_Expression,
)
Add_Operator_strategy = st.builds(
    Add_Operator,
)
Xor_Operator_strategy = st.builds(
    Xor_Operator,
)
iec61131_st_For_List_strategy = st.builds(
    iec61131_st_For_List,
)
iec61131_st_Control_Variable_strategy = st.builds(
    iec61131_st_Control_Variable,
    name=
        safe_text
)
Statement_List_strategy = st.builds(
    Statement_List,
)
Selection_Statement_strategy = st.builds(
    Selection_Statement,
)
iec61131_st_If_Statement_strategy = st.builds(
    iec61131_st_If_Statement,
)
Not_Operator_strategy = st.builds(
    Not_Operator,
)
Variable_strategy = st.builds(
    Variable,
)
iec61131_variables_Symbolic_Variable_strategy = st.builds(
    iec61131_variables_Symbolic_Variable,
)
For_List_strategy = st.builds(
    For_List,
)
Control_Variable_strategy = st.builds(
    Control_Variable,
)
Iteration_Statement_strategy = st.builds(
    Iteration_Statement,
)
iec61131_st_Exit_Statement_strategy = st.builds(
    iec61131_st_Exit_Statement,
)
iec61131_st_While_Statement_strategy = st.builds(
    iec61131_st_While_Statement,
)
iec61131_st_Repeat_Statement_strategy = st.builds(
    iec61131_st_Repeat_Statement,
)
iec61131_st_For_Statement_strategy = st.builds(
    iec61131_st_For_Statement,
)
iec61131_st_Case_List_Element_strategy = st.builds(
    iec61131_st_Case_List_Element,
)
iec61131_st_Case_List_strategy = st.builds(
    iec61131_st_Case_List,
)
Case_List_strategy = st.builds(
    Case_List,
)
iec61131_st_Case_Element_strategy = st.builds(
    iec61131_st_Case_Element,
)
iec61131_st_Else_Statement_strategy = st.builds(
    iec61131_st_Else_Statement,
)
iec61131_st_Else_If_Statement_strategy = st.builds(
    iec61131_st_Else_If_Statement,
)
Case_Element_strategy = st.builds(
    Case_Element,
)
iec61131_st_Case_Statement_strategy = st.builds(
    iec61131_st_Case_Statement,
)
Else_Statement_strategy = st.builds(
    Else_Statement,
)
Else_If_Statement_strategy = st.builds(
    Else_If_Statement,
)
Statement_strategy = st.builds(
    Statement,
)
Param_Assignment_strategy = st.builds(
    Param_Assignment,
)
iec61131_st_Param_Type1_strategy = st.builds(
    iec61131_st_Param_Type1,
)
iec61131_st_Param_Type2_strategy = st.builds(
    iec61131_st_Param_Type2,
)
iec61131_il_Param_Assignment2_strategy = st.builds(
    iec61131_il_Param_Assignment2,
)
iec61131_il_Il_Operand_strategy = st.builds(
    iec61131_il_Il_Operand,
)
Subprogram_Control_Statement_strategy = st.builds(
    Subprogram_Control_Statement,
)
iec61131_st_Fb_Invocation_strategy = st.builds(
    iec61131_st_Fb_Invocation,
)
iec61131_st_Return_Statement_strategy = st.builds(
    iec61131_st_Return_Statement,
)
iec61131_st_Iteration_Statement_strategy = st.builds(
    iec61131_st_Iteration_Statement,
)
iec61131_st_Selection_Statement_strategy = st.builds(
    iec61131_st_Selection_Statement,
)
iec61131_st_Subprogram_Control_Statement_strategy = st.builds(
    iec61131_st_Subprogram_Control_Statement,
)
Expression_Variable_strategy = st.builds(
    Expression_Variable,
)
iec61131_st_Assignment_Statement_strategy = st.builds(
    iec61131_st_Assignment_Statement,
)
Or_Operator_strategy = st.builds(
    Or_Operator,
)
Expression_Types_strategy = st.builds(
    Expression_Types,
)
iec61131_st_Xor_Expression_strategy = st.builds(
    iec61131_st_Xor_Expression,
)
iec61131_st_Power_Expression_strategy = st.builds(
    iec61131_st_Power_Expression,
)
iec61131_st_Unary_Expression_strategy = st.builds(
    iec61131_st_Unary_Expression,
)
iec61131_st_Equ_Expression_strategy = st.builds(
    iec61131_st_Equ_Expression,
)
iec61131_st_And_Expression_strategy = st.builds(
    iec61131_st_And_Expression,
)
iec61131_st_Add_Expression_strategy = st.builds(
    iec61131_st_Add_Expression,
)
iec61131_st_Term_Expression_strategy = st.builds(
    iec61131_st_Term_Expression,
)
iec61131_st_Comparison_strategy = st.builds(
    iec61131_st_Comparison,
)
iec61131_st_Primary_Expression_strategy = st.builds(
    iec61131_st_Primary_Expression,
)
iec61131_st_Expression_strategy = st.builds(
    iec61131_st_Expression,
)
iec61131_configurations_Prog_Data_Source_strategy = st.builds(
    iec61131_configurations_Prog_Data_Source,
)
iec61131_configurations_Prog_Conf_Element_strategy = st.builds(
    iec61131_configurations_Prog_Conf_Element,
)
Prog_Conf_Element_strategy = st.builds(
    Prog_Conf_Element,
)
iec61131_configurations_Fb_Task_strategy = st.builds(
    iec61131_configurations_Fb_Task,
)
iec61131_configurations_Prog_Cnxn_strategy = st.builds(
    iec61131_configurations_Prog_Cnxn,
)
iec61131_configurations_Prog_Conf_Elements_strategy = st.builds(
    iec61131_configurations_Prog_Conf_Elements,
)
Task_Initialization_strategy = st.builds(
    Task_Initialization,
)
iec61131_configurations_Priority_strategy = st.builds(
    iec61131_configurations_Priority,
)
iec61131_configurations_Interval_strategy = st.builds(
    iec61131_configurations_Interval,
)
iec61131_configurations_Single_strategy = st.builds(
    iec61131_configurations_Single,
)
iec61131_configurations_Instance_Specific_Init_strategy = st.builds(
    iec61131_configurations_Instance_Specific_Init,
)
iec61131_configurations_Data_Sink_strategy = st.builds(
    iec61131_configurations_Data_Sink,
)
Prog_Data_Source_strategy = st.builds(
    Prog_Data_Source,
)
Data_Sink_strategy = st.builds(
    Data_Sink,
)
Prog_Cnxn_strategy = st.builds(
    Prog_Cnxn,
)
iec61131_configurations_Prog_Source_strategy = st.builds(
    iec61131_configurations_Prog_Source,
)
iec61131_configurations_Prog_Sink_strategy = st.builds(
    iec61131_configurations_Prog_Sink,
)
Data_Source_strategy = st.builds(
    Data_Source,
)
iec61131_configurations_Program_Output_Reference_strategy = st.builds(
    iec61131_configurations_Program_Output_Reference,
)
configurations_Data_Sink_strategy = st.builds(
    configurations_Data_Sink,
)
iec61131_configurations_Data_Source_strategy = st.builds(
    iec61131_configurations_Data_Source,
)
Instance_Specific_Init_strategy = st.builds(
    Instance_Specific_Init,
)
iec61131_configurations_Instance_Spec2_strategy = st.builds(
    iec61131_configurations_Instance_Spec2,
)
iec61131_configurations_Instance_Spec1_strategy = st.builds(
    iec61131_configurations_Instance_Spec1,
)
iec61131_configurations_Instance_Specific_Initializations_strategy = st.builds(
    iec61131_configurations_Instance_Specific_Initializations,
)
iec61131_types_Byte_String_Type_Name_strategy = st.builds(
    iec61131_types_Byte_String_Type_Name,
)
Single_Element_Type_Name_strategy = st.builds(
    Single_Element_Type_Name,
)
iec61131_types_Enumerated_Type_Name_strategy = st.builds(
    iec61131_types_Enumerated_Type_Name,
)
iec61131_types_Subrange_Type_Name_strategy = st.builds(
    iec61131_types_Subrange_Type_Name,
)
types_Single_Element_Type_Name_strategy = st.builds(
    types_Single_Element_Type_Name,
)
types_Derived_Type_Name_strategy = st.builds(
    types_Derived_Type_Name,
)
Derived_Type_Name_strategy = st.builds(
    Derived_Type_Name,
)
iec61131_types_Array_Type_Name_strategy = st.builds(
    iec61131_types_Array_Type_Name,
)
iec61131_types_String_Type_Name_strategy = st.builds(
    iec61131_types_String_Type_Name,
)
iec61131_types_Single_Element_Type_Name_strategy = st.builds(
    iec61131_types_Single_Element_Type_Name,
)
iec61131_types_Duration_Type_Name_strategy = st.builds(
    iec61131_types_Duration_Type_Name,
)
iec61131_ld_Rung_strategy = st.builds(
    iec61131_ld_Rung,
)
iec61131_types_Simple_Specification_strategy = st.builds(
    iec61131_types_Simple_Specification,
)
iec61131_variables_Subscript_List_strategy = st.builds(
    iec61131_variables_Subscript_List,
)
Input_Reference_strategy = st.builds(
    Input_Reference,
)
iec61131_configurations_Task_Initialization_strategy = st.builds(
    iec61131_configurations_Task_Initialization,
)
iec61131_configurations_Task_Name_strategy = st.builds(
    iec61131_configurations_Task_Name,
    name=
        safe_text
)
iec61131_configurations_Program_Name_strategy = st.builds(
    iec61131_configurations_Program_Name,
    name=
        safe_text
)
iec61131_configurations_Access_Path_strategy = st.builds(
    iec61131_configurations_Access_Path,
)
iec61131_configurations_Access_Name_strategy = st.builds(
    iec61131_configurations_Access_Name,
    name=
        safe_text
)
Access_Path_strategy = st.builds(
    Access_Path,
)
iec61131_configurations_Symbolic_Path_strategy = st.builds(
    iec61131_configurations_Symbolic_Path,
)
iec61131_configurations_Direct_Path_strategy = st.builds(
    iec61131_configurations_Direct_Path,
)
iec61131_configurations_Access_Declaration_strategy = st.builds(
    iec61131_configurations_Access_Declaration,
    direction=
        safe_text
)
Access_Declaration_strategy = st.builds(
    Access_Declaration,
)
iec61131_configurations_Access_Declarations_strategy = st.builds(
    iec61131_configurations_Access_Declarations,
)
Resource_Declaration_strategy = st.builds(
    Resource_Declaration,
)
Access_Declarations_strategy = st.builds(
    Access_Declarations,
)
Instance_Specific_Initializations_strategy = st.builds(
    Instance_Specific_Initializations,
)
Global_Var_Declarations_strategy = st.builds(
    Global_Var_Declarations,
)
Single_Resource_Declaration_strategy = st.builds(
    Single_Resource_Declaration,
)
Configuration_Name_strategy = st.builds(
    Configuration_Name,
)
Prog_Conf_Elements_strategy = st.builds(
    Prog_Conf_Elements,
)
Program_Name_strategy = st.builds(
    Program_Name,
)
Single_strategy = st.builds(
    Single,
)
Priority_strategy = st.builds(
    Priority,
)
Task_Name_strategy = st.builds(
    Task_Name,
)
iec61131_configurations_Task_Configuration_strategy = st.builds(
    iec61131_configurations_Task_Configuration,
)
Program_Configuration_strategy = st.builds(
    Program_Configuration,
)
Task_Configuration_strategy = st.builds(
    Task_Configuration,
)
iec61131_configurations_Single_Resource_Declaration_strategy = st.builds(
    iec61131_configurations_Single_Resource_Declaration,
)
Resource_Type_Name_strategy = st.builds(
    Resource_Type_Name,
)
Resource_Name_strategy = st.builds(
    Resource_Name,
)
iec61131_configurations_Resource_Name_strategy = st.builds(
    iec61131_configurations_Resource_Name,
    name=
        safe_text
)
Simple_Type_Name_strategy = st.builds(
    Simple_Type_Name,
)
Single_Element_Type_Declaration_strategy = st.builds(
    Single_Element_Type_Declaration,
)
iec61131_pous_Subrange_Type_Declaration_strategy = st.builds(
    iec61131_pous_Subrange_Type_Declaration,
)
iec61131_pous_Simple_Type_Declaration_strategy = st.builds(
    iec61131_pous_Simple_Type_Declaration,
)
Function_Block_Declaration_strategy = st.builds(
    Function_Block_Declaration,
)
Function_Declaration_strategy = st.builds(
    Function_Declaration,
)
Program_Declaration_strategy = st.builds(
    Program_Declaration,
)
iec61131_pous_Library_strategy = st.builds(
    iec61131_pous_Library,
)
Program_Access_Decl_strategy = st.builds(
    Program_Access_Decl,
)
iec61131_pous_Function_Block_Vars_strategy = st.builds(
    iec61131_pous_Function_Block_Vars,
)
iec61131_pous_Function_Vars_strategy = st.builds(
    iec61131_pous_Function_Vars,
)
iec61131_pous_Program_Vars_strategy = st.builds(
    iec61131_pous_Program_Vars,
)
iec61131_pous_Structure_Elements_strategy = st.builds(
    iec61131_pous_Structure_Elements,
)
Structure_Elements_strategy = st.builds(
    Structure_Elements,
)
iec61131_pous_Structure_Element_Declaration_strategy = st.builds(
    iec61131_pous_Structure_Element_Declaration,
)
Structure_Element_Declaration_strategy = st.builds(
    Structure_Element_Declaration,
)
iec61131_pous_Structure_Specification_strategy = st.builds(
    iec61131_pous_Structure_Specification,
)
Enumerated_Spec_Init_strategy = st.builds(
    Enumerated_Spec_Init,
)
iec61131_pous_Enumerated_Type_Declaration_strategy = st.builds(
    iec61131_pous_Enumerated_Type_Declaration,
)
Subrange_Spec_Init_strategy = st.builds(
    Subrange_Spec_Init,
)
pous_Function_Block_Body_strategy = st.builds(
    pous_Function_Block_Body,
)
pous_Function_Body_strategy = st.builds(
    pous_Function_Body,
)
iec61131_ld_Ladder_Diagram_strategy = st.builds(
    iec61131_ld_Ladder_Diagram,
)
iec61131_fbd_Function_Block_Diagram_strategy = st.builds(
    iec61131_fbd_Function_Block_Diagram,
)
iec61131_st_Statement_List_strategy = st.builds(
    iec61131_st_Statement_List,
)
iec61131_il_Instruction_List_strategy = st.builds(
    iec61131_il_Instruction_List,
)
iec61131_pous_Other_Language_strategy = st.builds(
    iec61131_pous_Other_Language,
    text=
        safe_text
)
iec61131_pous_Function_Body_strategy = st.builds(
    iec61131_pous_Function_Body,
)
iec61131_pous_Function_Return_Value_strategy = st.builds(
    iec61131_pous_Function_Return_Value,
)
pous_Function_Name_strategy = st.builds(
    pous_Function_Name,
)
Function_Body_strategy = st.builds(
    Function_Body,
)
Function_Vars_strategy = st.builds(
    Function_Vars,
)
Byte_String_Type_Name_strategy = st.builds(
    Byte_String_Type_Name,
)
iec61131_types_Double_Byte_String_Type_Name_strategy = st.builds(
    iec61131_types_Double_Byte_String_Type_Name,
)
iec61131_types_Single_Byte_String_Type_Name_strategy = st.builds(
    iec61131_types_Single_Byte_String_Type_Name,
)
String_Type_Name_strategy = st.builds(
    String_Type_Name,
)
Structure_Specification_strategy = st.builds(
    Structure_Specification,
)
iec61131_pous_Structure_Declaration_strategy = st.builds(
    iec61131_pous_Structure_Declaration,
)
iec61131_pous_Type_Declaration_strategy = st.builds(
    iec61131_pous_Type_Declaration,
)
Type_Declaration_strategy = st.builds(
    Type_Declaration,
)
iec61131_pous_Structure_Type_Declaration_strategy = st.builds(
    iec61131_pous_Structure_Type_Declaration,
)
iec61131_pous_Array_Type_Declaration_strategy = st.builds(
    iec61131_pous_Array_Type_Declaration,
)
iec61131_pous_String_Type_Declaration_strategy = st.builds(
    iec61131_pous_String_Type_Declaration,
)
iec61131_pous_Single_Element_Type_Declaration_strategy = st.builds(
    iec61131_pous_Single_Element_Type_Declaration,
)
iec61131_pous_Access_Name_strategy = st.builds(
    iec61131_pous_Access_Name,
    name=
        safe_text
)
Symbolic_Variable_strategy = st.builds(
    Symbolic_Variable,
)
iec61131_variables_Multi_Element_Variable_strategy = st.builds(
    iec61131_variables_Multi_Element_Variable,
)
Access_Name_strategy = st.builds(
    Access_Name,
)
iec61131_pous_Program_Access_Decl_strategy = st.builds(
    iec61131_pous_Program_Access_Decl,
    direction=
        safe_text
)
iec61131_pous_Function_Block_Body_strategy = st.builds(
    iec61131_pous_Function_Block_Body,
)
Program_Type_Name_strategy = st.builds(
    Program_Type_Name,
)
Function_Return_Value_strategy = st.builds(
    Function_Return_Value,
)
Derived_Function_Name_strategy = st.builds(
    Derived_Function_Name,
)
Function_Block_Vars_strategy = st.builds(
    Function_Block_Vars,
)
Derived_Function_Block_Name_strategy = st.builds(
    Derived_Function_Block_Name,
)
pous_Function_Block_Type_Name_strategy = st.builds(
    pous_Function_Block_Type_Name,
)
types_Simple_Specification_strategy = st.builds(
    types_Simple_Specification,
)
iec61131_types_Generic_Type_Name_strategy = st.builds(
    iec61131_types_Generic_Type_Name,
)
iec61131_types_Elementary_Type_Name_strategy = st.builds(
    iec61131_types_Elementary_Type_Name,
)
iec61131_types_Simple_Type_Name_strategy = st.builds(
    iec61131_types_Simple_Type_Name,
)
Blocks_strategy = st.builds(
    Blocks,
)
iec61131_pous_Derived_Function_Name_strategy = st.builds(
    iec61131_pous_Derived_Function_Name,
)
iec61131_pous_Derived_Function_Block_Name_strategy = st.builds(
    iec61131_pous_Derived_Function_Block_Name,
)
Function_Block_Body_strategy = st.builds(
    Function_Block_Body,
)
iec61131_sfc_Sequential_Function_Chart_strategy = st.builds(
    iec61131_sfc_Sequential_Function_Chart,
)
iec61131_interfaces_Simple_Specification_Func_strategy = st.builds(
    iec61131_interfaces_Simple_Specification_Func,
)
Simple_Specification_Func_strategy = st.builds(
    Simple_Specification_Func,
)
Var1_Specification_Func_strategy = st.builds(
    Var1_Specification_Func,
)
iec61131_interfaces_Simple_Spec_Init_Func_strategy = st.builds(
    iec61131_interfaces_Simple_Spec_Init_Func,
)
Simple_Spec_Init_strategy = st.builds(
    Simple_Spec_Init,
)
iec61131_interfaces_Var_Name_Decl_strategy = st.builds(
    iec61131_interfaces_Var_Name_Decl,
)
Array_Type_Name_strategy = st.builds(
    Array_Type_Name,
)
iec61131_interfaces_Initial_Element_strategy = st.builds(
    iec61131_interfaces_Initial_Element,
)
Non_Generic_Type_Name_strategy = st.builds(
    Non_Generic_Type_Name,
)
iec61131_types_Derived_Type_Name_strategy = st.builds(
    iec61131_types_Derived_Type_Name,
)
Global_Var_Decl_strategy = st.builds(
    Global_Var_Decl,
)
Library_Element_Declaration_strategy = st.builds(
    Library_Element_Declaration,
)
iec61131_configurations_Configuration_Declaration_strategy = st.builds(
    iec61131_configurations_Configuration_Declaration,
)
iec61131_pous_Data_Type_Declaration_strategy = st.builds(
    iec61131_pous_Data_Type_Declaration,
)
iec61131_pous_Program_Declaration_strategy = st.builds(
    iec61131_pous_Program_Declaration,
)
iec61131_pous_Function_Declaration_strategy = st.builds(
    iec61131_pous_Function_Declaration,
)
iec61131_pous_Function_Block_Declaration_strategy = st.builds(
    iec61131_pous_Function_Block_Declaration,
)
iec61131_configurations_Resource_Declaration_strategy = st.builds(
    iec61131_configurations_Resource_Declaration,
)
iec61131_interfaces_Global_Var_Declarations_strategy = st.builds(
    iec61131_interfaces_Global_Var_Declarations,
    retain=
        st.booleans(),
    constant=
        st.booleans()
)
Located_Var_Decl_strategy = st.builds(
    Located_Var_Decl,
)
Program_Vars_strategy = st.builds(
    Program_Vars,
)
iec61131_pous_Program_Access_Decls_strategy = st.builds(
    iec61131_pous_Program_Access_Decls,
)
iec61131_interfaces_Located_Var_Declarations_strategy = st.builds(
    iec61131_interfaces_Located_Var_Declarations,
    constant=
        st.booleans(),
    retain=
        st.booleans()
)
Subrange_Type_Name_strategy = st.builds(
    Subrange_Type_Name,
)
Subrange_strategy = st.builds(
    Subrange,
)
Double_Byte_String_Type_Name_strategy = st.builds(
    Double_Byte_String_Type_Name,
)
Single_Byte_String_Type_Name_strategy = st.builds(
    Single_Byte_String_Type_Name,
)
Byte_String_strategy = st.builds(
    Byte_String,
)
iec61131_interfaces_Double_BString_strategy = st.builds(
    iec61131_interfaces_Double_BString,
)
iec61131_interfaces_Single_BString_strategy = st.builds(
    iec61131_interfaces_Single_BString,
)
iec61131_interfaces_Range_strategy = st.builds(
    iec61131_interfaces_Range,
)
Initialized_Structure_strategy = st.builds(
    Initialized_Structure,
)
Array_Spec_Init_strategy = st.builds(
    Array_Spec_Init,
)
Var2_Init_Decl_strategy = st.builds(
    Var2_Init_Decl,
)
iec61131_interfaces_Var_Init_Decl_Func_strategy = st.builds(
    iec61131_interfaces_Var_Init_Decl_Func,
)
iec61131_interfaces_Structured_Var_Init_Decl_strategy = st.builds(
    iec61131_interfaces_Structured_Var_Init_Decl,
)
iec61131_interfaces_Array_Var_Init_Decl_strategy = st.builds(
    iec61131_interfaces_Array_Var_Init_Decl,
)
Enumerated_Value_strategy = st.builds(
    Enumerated_Value,
)
Enumerated_Specification_strategy = st.builds(
    Enumerated_Specification,
)
iec61131_interfaces_Enumerated_Specification1_strategy = st.builds(
    iec61131_interfaces_Enumerated_Specification1,
)
iec61131_interfaces_Enumerated_Specification2_strategy = st.builds(
    iec61131_interfaces_Enumerated_Specification2,
)
Signed_Integer_strategy = st.builds(
    Signed_Integer,
)
Subrange_Specification_strategy = st.builds(
    Subrange_Specification,
)
iec61131_interfaces_Subrange_Specification2_strategy = st.builds(
    iec61131_interfaces_Subrange_Specification2,
)
iec61131_interfaces_Subrange_Specification1_strategy = st.builds(
    iec61131_interfaces_Subrange_Specification1,
)
interfaces_Var1_Specification_Func_strategy = st.builds(
    interfaces_Var1_Specification_Func,
)
Simple_Specification_strategy = st.builds(
    Simple_Specification,
)
pous_Structure_Elements_strategy = st.builds(
    pous_Structure_Elements,
)
interfaces_Located_Var_Spec_Init_strategy = st.builds(
    interfaces_Located_Var_Spec_Init,
)
interfaces_Var1_Specification_strategy = st.builds(
    interfaces_Var1_Specification,
)
iec61131_interfaces_Subrange_Spec_Init_strategy = st.builds(
    iec61131_interfaces_Subrange_Spec_Init,
)
iec61131_interfaces_Enumerated_Spec_Init_strategy = st.builds(
    iec61131_interfaces_Enumerated_Spec_Init,
)
iec61131_interfaces_Simple_Spec_Init_strategy = st.builds(
    iec61131_interfaces_Simple_Spec_Init,
)
Assignment_Symbol_strategy = st.builds(
    Assignment_Symbol,
)
iec61131_interfaces_Var1_Specification_strategy = st.builds(
    iec61131_interfaces_Var1_Specification,
)
Bool_Type_Name_strategy = st.builds(
    Bool_Type_Name,
)
operators_Divide_Operator_strategy = st.builds(
    operators_Divide_Operator,
)
Multiply_Operator_strategy = st.builds(
    Multiply_Operator,
)
iec61131_operators_Multiply_Symbol_strategy = st.builds(
    iec61131_operators_Multiply_Symbol,
)
operators_Multiply_Operator_strategy = st.builds(
    operators_Multiply_Operator,
)
operators_Add_Operator_strategy = st.builds(
    operators_Add_Operator,
)
operators_Arithmetic_Name_strategy = st.builds(
    operators_Arithmetic_Name,
)
iec61131_operators_Divide_Name_strategy = st.builds(
    iec61131_operators_Divide_Name,
)
iec61131_operators_Multiply_Name_strategy = st.builds(
    iec61131_operators_Multiply_Name,
)
operators_Addition_Operator_strategy = st.builds(
    operators_Addition_Operator,
)
iec61131_operators_Addition_Symbol_strategy = st.builds(
    iec61131_operators_Addition_Symbol,
)
iec61131_operators_Addition_Name_strategy = st.builds(
    iec61131_operators_Addition_Name,
)
Comparison_Operator_strategy = st.builds(
    Comparison_Operator,
)
iec61131_operators_LessEqual_Operator_strategy = st.builds(
    iec61131_operators_LessEqual_Operator,
)
iec61131_operators_GreaterEqual_Operator_strategy = st.builds(
    iec61131_operators_GreaterEqual_Operator,
)
iec61131_operators_Greater_Operator_strategy = st.builds(
    iec61131_operators_Greater_Operator,
)
iec61131_operators_Less_Operator_strategy = st.builds(
    iec61131_operators_Less_Operator,
)
Il_Expr_Operator_strategy = st.builds(
    Il_Expr_Operator,
)
iec61131_operators_Arithmetic_Name_strategy = st.builds(
    iec61131_operators_Arithmetic_Name,
)
iec61131_operators_Comparison_Name_strategy = st.builds(
    iec61131_operators_Comparison_Name,
)
operators_Substraction_Operator_strategy = st.builds(
    operators_Substraction_Operator,
)
iec61131_operators_Substraction_Name_strategy = st.builds(
    iec61131_operators_Substraction_Name,
)
GreaterEqual_Operator_strategy = st.builds(
    GreaterEqual_Operator,
)
iec61131_operators_GreaterEqual_Symbol_strategy = st.builds(
    iec61131_operators_GreaterEqual_Symbol,
)
operators_GreaterEqual_Operator_strategy = st.builds(
    operators_GreaterEqual_Operator,
)
Greater_Operator_strategy = st.builds(
    Greater_Operator,
)
iec61131_operators_Greater_Symbol_strategy = st.builds(
    iec61131_operators_Greater_Symbol,
)
operators_Greater_Operator_strategy = st.builds(
    operators_Greater_Operator,
)
LessEqual_Operator_strategy = st.builds(
    LessEqual_Operator,
)
iec61131_operators_LessEqual_Symbol_strategy = st.builds(
    iec61131_operators_LessEqual_Symbol,
)
operators_LessEqual_Operator_strategy = st.builds(
    operators_LessEqual_Operator,
)
Less_Operator_strategy = st.builds(
    Less_Operator,
)
iec61131_operators_Less_Symbol_strategy = st.builds(
    iec61131_operators_Less_Symbol,
)
operators_Less_Operator_strategy = st.builds(
    operators_Less_Operator,
)
Unequal_Operator_strategy = st.builds(
    Unequal_Operator,
)
iec61131_operators_Unequal_Symbol_strategy = st.builds(
    iec61131_operators_Unequal_Symbol,
)
operators_Unequal_Operator_strategy = st.builds(
    operators_Unequal_Operator,
)
Equal_Operator_strategy = st.builds(
    Equal_Operator,
)
iec61131_operators_Equal_Symbol_strategy = st.builds(
    iec61131_operators_Equal_Symbol,
)
operators_Comparison_Name_strategy = st.builds(
    operators_Comparison_Name,
)
iec61131_operators_Less_Name_strategy = st.builds(
    iec61131_operators_Less_Name,
)
iec61131_operators_GreaterEqual_Name_strategy = st.builds(
    iec61131_operators_GreaterEqual_Name,
)
iec61131_operators_Greater_Name_strategy = st.builds(
    iec61131_operators_Greater_Name,
)
iec61131_operators_Unequal_Name_strategy = st.builds(
    iec61131_operators_Unequal_Name,
)
iec61131_operators_LessEqual_Name_strategy = st.builds(
    iec61131_operators_LessEqual_Name,
)
operators_Equal_Operator_strategy = st.builds(
    operators_Equal_Operator,
)
iec61131_operators_Equal_Name_strategy = st.builds(
    iec61131_operators_Equal_Name,
)
And_Operator_strategy = st.builds(
    And_Operator,
)
iec61131_operators_And_Name_strategy = st.builds(
    iec61131_operators_And_Name,
)
iec61131_operators_And_Symbol_strategy = st.builds(
    iec61131_operators_And_Symbol,
)
Assignment_Operator_strategy = st.builds(
    Assignment_Operator,
)
iec61131_operators_Assignment_Name_strategy = st.builds(
    iec61131_operators_Assignment_Name,
)
iec61131_operators_Assignment_Symbol_strategy = st.builds(
    iec61131_operators_Assignment_Symbol,
)
Power_Operator_strategy = st.builds(
    Power_Operator,
)
iec61131_operators_Power_Name_strategy = st.builds(
    iec61131_operators_Power_Name,
)
iec61131_operators_Power_Symbol_strategy = st.builds(
    iec61131_operators_Power_Symbol,
)
Divide_Operator_strategy = st.builds(
    Divide_Operator,
)
iec61131_operators_Divide_Symbol_strategy = st.builds(
    iec61131_operators_Divide_Symbol,
)
iec61131_literals_Integer_strategy = st.builds(
    iec61131_literals_Integer,
    value=
        safe_text
)
iec61131_literals_BSInteger_strategy = st.builds(
    iec61131_literals_BSInteger,
)
iec61131_literals_Date_Literal_strategy = st.builds(
    iec61131_literals_Date_Literal,
    year=
        safe_text,
    day=
        safe_text,
    month=
        safe_text
)
iec61131_literals_Daytime_strategy = st.builds(
    iec61131_literals_Daytime,
    minute=
        safe_text,
    hour=
        safe_text
)
iec61131_literals_Fixed_Point_Literal_strategy = st.builds(
    iec61131_literals_Fixed_Point_Literal,
)
Double_Byte_Character_Representation_strategy = st.builds(
    Double_Byte_Character_Representation,
)
operators_Dot_Operator_strategy = st.builds(
    operators_Dot_Operator,
)
il_Il_Simple_Operator_strategy = st.builds(
    il_Il_Simple_Operator,
)
operators_Unary_Operator_strategy = st.builds(
    operators_Unary_Operator,
)
iec61131_operators_Substraction_Symbol_strategy = st.builds(
    iec61131_operators_Substraction_Symbol,
)
iec61131_operators_Not_Operator_strategy = st.builds(
    iec61131_operators_Not_Operator,
)
il_Il_Expr_Operator_strategy = st.builds(
    il_Il_Expr_Operator,
)
iec61131_operators_Modulo_Operator_strategy = st.builds(
    iec61131_operators_Modulo_Operator,
)
operators_Operator_strategy = st.builds(
    operators_Operator,
)
iec61131_operators_Xor_Operator_strategy = st.builds(
    iec61131_operators_Xor_Operator,
)
iec61131_operators_Or_Operator_strategy = st.builds(
    iec61131_operators_Or_Operator,
)
iec61131_operators_And_Operator_strategy = st.builds(
    iec61131_operators_And_Operator,
)
EquUequ_Operator_strategy = st.builds(
    EquUequ_Operator,
)
iec61131_operators_Unequal_Operator_strategy = st.builds(
    iec61131_operators_Unequal_Operator,
)
iec61131_operators_Equal_Operator_strategy = st.builds(
    iec61131_operators_Equal_Operator,
)
Dot_Operator_strategy = st.builds(
    Dot_Operator,
)
iec61131_operators_Divide_Operator_strategy = st.builds(
    iec61131_operators_Divide_Operator,
)
iec61131_operators_Multiply_Operator_strategy = st.builds(
    iec61131_operators_Multiply_Operator,
)
iec61131_operators_Substraction_Operator_strategy = st.builds(
    iec61131_operators_Substraction_Operator,
)
iec61131_operators_Addition_Operator_strategy = st.builds(
    iec61131_operators_Addition_Operator,
)
Operator_strategy = st.builds(
    Operator,
)
iec61131_operators_EquUequ_Operator_strategy = st.builds(
    iec61131_operators_EquUequ_Operator,
)
iec61131_operators_Assignment_Operator_strategy = st.builds(
    iec61131_operators_Assignment_Operator,
)
iec61131_operators_Dot_Operator_strategy = st.builds(
    iec61131_operators_Dot_Operator,
)
iec61131_operators_Comparison_Operator_strategy = st.builds(
    iec61131_operators_Comparison_Operator,
)
iec61131_operators_Power_Operator_strategy = st.builds(
    iec61131_operators_Power_Operator,
)
iec61131_operators_Unary_Operator_strategy = st.builds(
    iec61131_operators_Unary_Operator,
)
iec61131_operators_Add_Operator_strategy = st.builds(
    iec61131_operators_Add_Operator,
)
iec61131_operators_Operator_strategy = st.builds(
    iec61131_operators_Operator,
)
iec61131_literals_Double_Byte_Character_Representation_strategy = st.builds(
    iec61131_literals_Double_Byte_Character_Representation,
    value=
        safe_text
)
Common_Character_Representation_strategy = st.builds(
    Common_Character_Representation,
)
iec61131_literals_Single_Byte_Character_Representation_strategy = st.builds(
    iec61131_literals_Single_Byte_Character_Representation,
    value=
        safe_text
)
iec61131_literals_Common_Character_Representation_strategy = st.builds(
    iec61131_literals_Common_Character_Representation,
    value=
        safe_text
)
DT_Type_Name_strategy = st.builds(
    DT_Type_Name,
)
Date_Literal_strategy = st.builds(
    Date_Literal,
)
Date_Type_Name_strategy = st.builds(
    Date_Type_Name,
)
iec61131_types_TOD_Type_Name_strategy = st.builds(
    iec61131_types_TOD_Type_Name,
)
iec61131_types_DT_Type_Name_strategy = st.builds(
    iec61131_types_DT_Type_Name,
)
Single_Byte_Character_Representation_strategy = st.builds(
    Single_Byte_Character_Representation,
)
Character_String_strategy = st.builds(
    Character_String,
)
iec61131_literals_Double_Byte_Character_String_strategy = st.builds(
    iec61131_literals_Double_Byte_Character_String,
)
iec61131_literals_Single_Byte_Character_String_strategy = st.builds(
    iec61131_literals_Single_Byte_Character_String,
)
Milliseconds_strategy = st.builds(
    Milliseconds,
)
Seconds_strategy = st.builds(
    Seconds,
)
Minutes_strategy = st.builds(
    Minutes,
)
Hours_strategy = st.builds(
    Hours,
)
Unsigned_Integer_strategy = st.builds(
    Unsigned_Integer,
)
Fixed_Point_Literal_strategy = st.builds(
    Fixed_Point_Literal,
)
iec61131_literals_Fixed_Point_strategy = st.builds(
    iec61131_literals_Fixed_Point,
    valuePre=
        safe_text,
    valuePost=
        safe_text
)
iec61131_literals_Interval_strategy = st.builds(
    iec61131_literals_Interval,
)
literals_Fixed_Point_Literal_strategy = st.builds(
    literals_Fixed_Point_Literal,
)
Integer_strategy = st.builds(
    Integer,
)
Numeric_Literal_strategy = st.builds(
    Numeric_Literal,
)
iec61131_literals_Integer_Literal_strategy = st.builds(
    iec61131_literals_Integer_Literal,
)
Bit_String_Type_Name_strategy = st.builds(
    Bit_String_Type_Name,
)
iec61131_types_Bool_Type_Name_strategy = st.builds(
    iec61131_types_Bool_Type_Name,
)
BSInteger_strategy = st.builds(
    BSInteger,
)
Constant_strategy = st.builds(
    Constant,
)
iec61131_literals_Bit_String_Literal_strategy = st.builds(
    iec61131_literals_Bit_String_Literal,
)
iec61131_literals_Time_Literal_strategy = st.builds(
    iec61131_literals_Time_Literal,
)
iec61131_literals_Character_String_strategy = st.builds(
    iec61131_literals_Character_String,
)
iec61131_literals_Numeric_Literal_strategy = st.builds(
    iec61131_literals_Numeric_Literal,
)
TOD_Type_Name_strategy = st.builds(
    TOD_Type_Name,
)
Daytime_strategy = st.builds(
    Daytime,
)
Time_Literal_strategy = st.builds(
    Time_Literal,
)
iec61131_literals_Date_And_Time_strategy = st.builds(
    iec61131_literals_Date_And_Time,
)
iec61131_literals_Date_strategy = st.builds(
    iec61131_literals_Date,
)
iec61131_literals_Time_Of_Day_strategy = st.builds(
    iec61131_literals_Time_Of_Day,
)
Substraction_Operator_strategy = st.builds(
    Substraction_Operator,
)
Duration_Type_Name_strategy = st.builds(
    Duration_Type_Name,
)
Interval_strategy = st.builds(
    Interval,
)
iec61131_literals_Days_strategy = st.builds(
    iec61131_literals_Days,
)
iec61131_literals_Minutes_strategy = st.builds(
    iec61131_literals_Minutes,
)
iec61131_literals_Hours_strategy = st.builds(
    iec61131_literals_Hours,
)
iec61131_literals_Milliseconds_strategy = st.builds(
    iec61131_literals_Milliseconds,
)
iec61131_literals_Seconds_strategy = st.builds(
    iec61131_literals_Seconds,
)
sfc_Action_Time_strategy = st.builds(
    sfc_Action_Time,
)
literals_Time_Literal_strategy = st.builds(
    literals_Time_Literal,
)
iec61131_literals_Duration_strategy = st.builds(
    iec61131_literals_Duration,
)
literals_BSInteger_strategy = st.builds(
    literals_BSInteger,
)
interfaces_Range_strategy = st.builds(
    interfaces_Range,
)
st_Case_List_Element_strategy = st.builds(
    st_Case_List_Element,
)
literals_Integer_strategy = st.builds(
    literals_Integer,
)
iec61131_literals_Unsigned_Integer_strategy = st.builds(
    iec61131_literals_Unsigned_Integer,
)
iec61131_literals_Hex_Integer_strategy = st.builds(
    iec61131_literals_Hex_Integer,
)
iec61131_literals_Octal_Integer_strategy = st.builds(
    iec61131_literals_Octal_Integer,
)
iec61131_literals_Binary_Integer_strategy = st.builds(
    iec61131_literals_Binary_Integer,
)
iec61131_literals_Signed_Integer_strategy = st.builds(
    iec61131_literals_Signed_Integer,
    negative=
        st.booleans()
)
il_Il_Operand_strategy = st.builds(
    il_Il_Operand,
)
configurations_Prog_Data_Source_strategy = st.builds(
    configurations_Prog_Data_Source,
)
configurations_Data_Source_strategy = st.builds(
    configurations_Data_Source,
)
iec61131_configurations_Global_Var_Reference_strategy = st.builds(
    iec61131_configurations_Global_Var_Reference,
)
iec61131_variables_Direct_Variable_strategy = st.builds(
    iec61131_variables_Direct_Variable,
    value=
        safe_text
)
iec61131_literals_Constant_strategy = st.builds(
    iec61131_literals_Constant,
)
iec61131_literals_Boolean_Literal_strategy = st.builds(
    iec61131_literals_Boolean_Literal,
    value=
        safe_text
)
Fixed_Point_strategy = st.builds(
    Fixed_Point,
)
Real_Type_Name_strategy = st.builds(
    Real_Type_Name,
)
iec61131_literals_Real_Literal_strategy = st.builds(
    iec61131_literals_Real_Literal,
    exponent=
        safe_text,
    negative=
        st.booleans()
)
Integer_Type_Name_strategy = st.builds(
    Integer_Type_Name,
)
iec61131_types_Unsigned_Integer_Type_Name_strategy = st.builds(
    iec61131_types_Unsigned_Integer_Type_Name,
)
iec61131_types_Signed_Integer_Type_Name_strategy = st.builds(
    iec61131_types_Signed_Integer_Type_Name,
)
iec61131_NamedElement_strategy = st.builds(
    iec61131_NamedElement,
    name=
        safe_text
)
iec61131_Commentable_strategy = st.builds(
    iec61131_Commentable,
    comments=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
iec61131_sfc_Step_Name_strategy = st.builds(
    iec61131_sfc_Step_Name,
)
iec61131_variables_Variable_Name_strategy = st.builds(
    iec61131_variables_Variable_Name,
)
Commentable_strategy = st.builds(
    Commentable,
)
iec61131_configurations_Program_Configuration_strategy = st.builds(
    iec61131_configurations_Program_Configuration,
    retain=
        st.booleans()
)
iec61131_variables_Variable_strategy = st.builds(
    iec61131_variables_Variable,
)
iec61131_st_Statement_strategy = st.builds(
    iec61131_st_Statement,
)
iec61131_st_Expression_Variable_strategy = st.builds(
    iec61131_st_Expression_Variable,
)
iec61131_st_Param_Assignment_strategy = st.builds(
    iec61131_st_Param_Assignment,
)
iec61131_st_Expression_Types_strategy = st.builds(
    iec61131_st_Expression_Types,
)
iec61131_Library_Element_Name_strategy = st.builds(
    iec61131_Library_Element_Name,
)
iec61131_Library_Element_Declaration_strategy = st.builds(
    iec61131_Library_Element_Declaration,
)
iec61131_IEC61131_strategy = st.builds(
    iec61131_IEC61131,
)
iec61131_interfaces_Input_Declaration_strategy = st.builds(
    iec61131_interfaces_Input_Declaration,
)
iec61131_interfaces_Global_Var_Spec_strategy = st.builds(
    iec61131_interfaces_Global_Var_Spec,
)
iec61131_interfaces_Global_Var_Decl_strategy = st.builds(
    iec61131_interfaces_Global_Var_Decl,
)
External_Specification_strategy = st.builds(
    External_Specification,
)
Global_Var_Name_strategy = st.builds(
    Global_Var_Name,
)
iec61131_interfaces_External_Declaration_strategy = st.builds(
    iec61131_interfaces_External_Declaration,
)
iec61131_interfaces_Interface_strategy = st.builds(
    iec61131_interfaces_Interface,
)
RNV_Declarations_strategy = st.builds(
    RNV_Declarations,
)
iec61131_interfaces_Non_Retentive_Var_Declarations_strategy = st.builds(
    iec61131_interfaces_Non_Retentive_Var_Declarations,
)
iec61131_interfaces_Retentive_Var_Declarations_strategy = st.builds(
    iec61131_interfaces_Retentive_Var_Declarations,
)
External_Declaration_strategy = st.builds(
    External_Declaration,
)
Other_Var_Declaration_strategy = st.builds(
    Other_Var_Declaration,
)
iec61131_interfaces_External_Var_Declarations_strategy = st.builds(
    iec61131_interfaces_External_Var_Declarations,
    constant=
        st.booleans()
)
Variable_Name_strategy = st.builds(
    Variable_Name,
)
Location_strategy = st.builds(
    Location,
)
iec61131_interfaces_Located_Var_Decl_strategy = st.builds(
    iec61131_interfaces_Located_Var_Decl,
)
Direct_Variable_strategy = st.builds(
    Direct_Variable,
)
iec61131_interfaces_Location_strategy = st.builds(
    iec61131_interfaces_Location,
)
iec61131_interfaces_Located_Var_Spec_Init_strategy = st.builds(
    iec61131_interfaces_Located_Var_Spec_Init,
)
iec61131_interfaces_External_Specification_strategy = st.builds(
    iec61131_interfaces_External_Specification,
)
iec61131_interfaces_Var_Spec_strategy = st.builds(
    iec61131_interfaces_Var_Spec,
)
iec61131_interfaces_Incompl_Location_strategy = st.builds(
    iec61131_interfaces_Incompl_Location,
    location=
        safe_text
)
Var_Spec_strategy = st.builds(
    Var_Spec,
)
iec61131_interfaces_Byte_String_strategy = st.builds(
    iec61131_interfaces_Byte_String,
)
Incompl_Location_strategy = st.builds(
    Incompl_Location,
)
iec61131_interfaces_Incompl_Located_Var_Decl_strategy = st.builds(
    iec61131_interfaces_Incompl_Located_Var_Decl,
)
iec61131_interfaces_RNV_Declarations_strategy = st.builds(
    iec61131_interfaces_RNV_Declarations,
)
Incompl_Located_Var_Decl_strategy = st.builds(
    Incompl_Located_Var_Decl,
)
iec61131_interfaces_Incompl_Located_Var_Declarations_strategy = st.builds(
    iec61131_interfaces_Incompl_Located_Var_Declarations,
    retain=
        st.booleans()
)
iec61131_interfaces_Var_Declarations_strategy = st.builds(
    iec61131_interfaces_Var_Declarations,
    constant=
        st.booleans()
)
Temp_Var_Decl_strategy = st.builds(
    Temp_Var_Decl,
)
iec61131_interfaces_Temp_Var_Declaration_strategy = st.builds(
    iec61131_interfaces_Temp_Var_Declaration,
)
iec61131_interfaces_Temp_Var_Decls_strategy = st.builds(
    iec61131_interfaces_Temp_Var_Decls,
)
Global_Var_Spec_strategy = st.builds(
    Global_Var_Spec,
)
iec61131_interfaces_Global_Var_Location_strategy = st.builds(
    iec61131_interfaces_Global_Var_Location,
)
iec61131_interfaces_Global_Var_List_strategy = st.builds(
    iec61131_interfaces_Global_Var_List,
)
Library_Element_Name_strategy = st.builds(
    Library_Element_Name,
)
iec61131_pous_Program_Type_Name_strategy = st.builds(
    iec61131_pous_Program_Type_Name,
)
iec61131_types_Data_Type_Name_strategy = st.builds(
    iec61131_types_Data_Type_Name,
)
iec61131_configurations_Configuration_Name_strategy = st.builds(
    iec61131_configurations_Configuration_Name,
)
iec61131_pous_Function_Name_strategy = st.builds(
    iec61131_pous_Function_Name,
)
iec61131_configurations_Resource_Type_Name_strategy = st.builds(
    iec61131_configurations_Resource_Type_Name,
)
iec61131_interfaces_Global_Var_Name_strategy = st.builds(
    iec61131_interfaces_Global_Var_Name,
)
iec61131_interfaces_Specification_strategy = st.builds(
    iec61131_interfaces_Specification,
)
Specification_strategy = st.builds(
    Specification,
)
Array_Initial_Elements_strategy = st.builds(
    Array_Initial_Elements,
)
iec61131_interfaces_Array_Initial_Elements1_strategy = st.builds(
    iec61131_interfaces_Array_Initial_Elements1,
)
iec61131_interfaces_Array_Initial_Elements2_strategy = st.builds(
    iec61131_interfaces_Array_Initial_Elements2,
)
iec61131_interfaces_Array_Initialization_strategy = st.builds(
    iec61131_interfaces_Array_Initialization,
)
iec61131_interfaces_Var1_List_strategy = st.builds(
    iec61131_interfaces_Var1_List,
)
Double_BString_strategy = st.builds(
    Double_BString,
)
Double_Byte_Character_String_strategy = st.builds(
    Double_Byte_Character_String,
)
Single_BString_strategy = st.builds(
    Single_BString,
)
Single_Byte_Character_String_strategy = st.builds(
    Single_Byte_Character_String,
)
Located_Var_Spec_Init_strategy = st.builds(
    Located_Var_Spec_Init,
)
iec61131_interfaces_Double_Byte_String_Spec_strategy = st.builds(
    iec61131_interfaces_Double_Byte_String_Spec,
)
iec61131_interfaces_Single_Byte_String_Spec_strategy = st.builds(
    iec61131_interfaces_Single_Byte_String_Spec,
)
Double_Byte_String_Spec_strategy = st.builds(
    Double_Byte_String_Spec,
)
Single_Byte_String_Spec_strategy = st.builds(
    Single_Byte_String_Spec,
)
String_Var_Declaration_strategy = st.builds(
    String_Var_Declaration,
)
iec61131_interfaces_Double_Byte_String_Var_Declaration_strategy = st.builds(
    iec61131_interfaces_Double_Byte_String_Var_Declaration,
)
iec61131_interfaces_Single_Byte_String_Var_Declaration_strategy = st.builds(
    iec61131_interfaces_Single_Byte_String_Var_Declaration,
)
Range_strategy = st.builds(
    Range,
)
Case_List_Element_strategy = st.builds(
    Case_List_Element,
)
iec61131_interfaces_Subrange_strategy = st.builds(
    iec61131_interfaces_Subrange,
    delimiter=
        safe_text
)
iec61131_interfaces_Array_Initial_Elements_strategy = st.builds(
    iec61131_interfaces_Array_Initial_Elements,
)
interfaces_Var_Spec_strategy = st.builds(
    interfaces_Var_Spec,
)
interfaces_External_Specification_strategy = st.builds(
    interfaces_External_Specification,
)
iec61131_pous_Function_Block_Type_Name_strategy = st.builds(
    iec61131_pous_Function_Block_Type_Name,
)
iec61131_interfaces_Array_Specification_strategy = st.builds(
    iec61131_interfaces_Array_Specification,
)
iec61131_types_Structure_Type_Name_strategy = st.builds(
    iec61131_types_Structure_Type_Name,
)
interfaces_Specification_strategy = st.builds(
    interfaces_Specification,
)
iec61131_interfaces_Enumerated_Specification_strategy = st.builds(
    iec61131_interfaces_Enumerated_Specification,
)
iec61131_interfaces_Subrange_Specification_strategy = st.builds(
    iec61131_interfaces_Subrange_Specification,
)
interfaces_Var2_Init_Decl_strategy = st.builds(
    interfaces_Var2_Init_Decl,
)
interfaces_Temp_Var_Decl_strategy = st.builds(
    interfaces_Temp_Var_Decl,
)
iec61131_interfaces_String_Var_Declaration_strategy = st.builds(
    iec61131_interfaces_String_Var_Declaration,
)
Function_Block_Type_Name_strategy = st.builds(
    Function_Block_Type_Name,
)
Structure_Initialization_strategy = st.builds(
    Structure_Initialization,
)
Temp_Var_Declaration_strategy = st.builds(
    Temp_Var_Declaration,
)
iec61131_interfaces_Var1_Declaration_strategy = st.builds(
    iec61131_interfaces_Var1_Declaration,
)
iec61131_interfaces_Structured_Var_Declaration_strategy = st.builds(
    iec61131_interfaces_Structured_Var_Declaration,
)
iec61131_interfaces_Array_Var_Declaration_strategy = st.builds(
    iec61131_interfaces_Array_Var_Declaration,
)
iec61131_interfaces_Fb_Name_Decl_strategy = st.builds(
    iec61131_interfaces_Fb_Name_Decl,
)
Enumerated_Type_Name_strategy = st.builds(
    Enumerated_Type_Name,
)
iec61131_interfaces_Enumerated_Value_strategy = st.builds(
    iec61131_interfaces_Enumerated_Value,
    name=
        safe_text
)
iec61131_interfaces_Structure_Element_Name_strategy = st.builds(
    iec61131_interfaces_Structure_Element_Name,
    name=
        safe_text
)
Initial_Element_strategy = st.builds(
    Initial_Element,
)
iec61131_interfaces_InitElement_Constant_strategy = st.builds(
    iec61131_interfaces_InitElement_Constant,
)
iec61131_interfaces_InitElement_Array_strategy = st.builds(
    iec61131_interfaces_InitElement_Array,
)
iec61131_interfaces_InitElement_EnumValue_strategy = st.builds(
    iec61131_interfaces_InitElement_EnumValue,
)
iec61131_interfaces_InitElement_Structure_strategy = st.builds(
    iec61131_interfaces_InitElement_Structure,
)
Structure_Element_Name_strategy = st.builds(
    Structure_Element_Name,
)
iec61131_interfaces_Structure_Element_Initialization_strategy = st.builds(
    iec61131_interfaces_Structure_Element_Initialization,
)
Structure_Element_Initialization_strategy = st.builds(
    Structure_Element_Initialization,
)
iec61131_interfaces_Structure_Initialization_strategy = st.builds(
    iec61131_interfaces_Structure_Initialization,
)
iec61131_interfaces_Var_Declaration_strategy = st.builds(
    iec61131_interfaces_Var_Declaration,
)
Structure_Type_Name_strategy = st.builds(
    Structure_Type_Name,
)
pous_Structure_Specification_strategy = st.builds(
    pous_Structure_Specification,
)
iec61131_interfaces_Initialized_Structure_strategy = st.builds(
    iec61131_interfaces_Initialized_Structure,
)
Array_Specification_strategy = st.builds(
    Array_Specification,
)
iec61131_interfaces_Array_Specification1_strategy = st.builds(
    iec61131_interfaces_Array_Specification1,
)
iec61131_interfaces_Array_Specification2_strategy = st.builds(
    iec61131_interfaces_Array_Specification2,
)
Array_Initialization_strategy = st.builds(
    Array_Initialization,
)
iec61131_interfaces_Array_Spec_Init_strategy = st.builds(
    iec61131_interfaces_Array_Spec_Init,
)
Var_Declaration_strategy = st.builds(
    Var_Declaration,
)
iec61131_interfaces_Temp_Var_Decl_strategy = st.builds(
    iec61131_interfaces_Temp_Var_Decl,
)
Var1_Specification_strategy = st.builds(
    Var1_Specification,
)
iec61131_interfaces_Var1_Specification_Func_strategy = st.builds(
    iec61131_interfaces_Var1_Specification_Func,
)
Var_Init_Decl_strategy = st.builds(
    Var_Init_Decl,
)
iec61131_interfaces_Var2_Init_Decl_strategy = st.builds(
    iec61131_interfaces_Var2_Init_Decl,
)
iec61131_interfaces_Var1_Init_Decl_strategy = st.builds(
    iec61131_interfaces_Var1_Init_Decl,
)
Var1_List_strategy = st.builds(
    Var1_List,
)
Input_Declaration_strategy = st.builds(
    Input_Declaration,
)
iec61131_interfaces_Var_Init_Decl_strategy = st.builds(
    iec61131_interfaces_Var_Init_Decl,
)
iec61131_interfaces_Edge_Declaration_strategy = st.builds(
    iec61131_interfaces_Edge_Declaration,
    edge=
        safe_text
)
Io_Var_Declaration_strategy = st.builds(
    Io_Var_Declaration,
)
iec61131_interfaces_Input_Output_Declarations_strategy = st.builds(
    iec61131_interfaces_Input_Output_Declarations,
)
iec61131_interfaces_Output_Declarations_strategy = st.builds(
    iec61131_interfaces_Output_Declarations,
    retain=
        st.booleans()
)
iec61131_interfaces_Input_Declarations_strategy = st.builds(
    iec61131_interfaces_Input_Declarations,
    retain=
        st.booleans()
)
pous_Function_Vars_strategy = st.builds(
    pous_Function_Vars,
)
pous_Program_Vars_strategy = st.builds(
    pous_Program_Vars,
)
pous_Function_Block_Vars_strategy = st.builds(
    pous_Function_Block_Vars,
)
interfaces_Interface_strategy = st.builds(
    interfaces_Interface,
)
iec61131_interfaces_Function_Var_Decl_strategy = st.builds(
    iec61131_interfaces_Function_Var_Decl,
    constant=
        st.booleans()
)
iec61131_interfaces_Io_Var_Declaration_strategy = st.builds(
    iec61131_interfaces_Io_Var_Declaration,
)
iec61131_interfaces_Other_Var_Declaration_strategy = st.builds(
    iec61131_interfaces_Other_Var_Declaration,
)

@given(instance=Output_Reference_strategy)
@settings(max_examples=50)
def test_output_reference_instantiation(instance):
    assert isinstance(instance, Output_Reference)

@given(instance=variables_Symbolic_Variable_strategy)
@settings(max_examples=50)
def test_variables_symbolic_variable_instantiation(instance):
    assert isinstance(instance, variables_Symbolic_Variable)

@given(instance=pous_Function_Return_Value_strategy)
@settings(max_examples=50)
def test_pous_function_return_value_instantiation(instance):
    assert isinstance(instance, pous_Function_Return_Value)

@given(instance=types_Data_Type_Name_strategy)
@settings(max_examples=50)
def test_types_data_type_name_instantiation(instance):
    assert isinstance(instance, types_Data_Type_Name)

@given(instance=iec61131_types_Non_Generic_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_non_generic_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Non_Generic_Type_Name)

@given(instance=interfaces_Simple_Specification_Func_strategy)
@settings(max_examples=50)
def test_interfaces_simple_specification_func_instantiation(instance):
    assert isinstance(instance, interfaces_Simple_Specification_Func)

@given(instance=types_Non_Generic_Type_Name_strategy)
@settings(max_examples=50)
def test_types_non_generic_type_name_instantiation(instance):
    assert isinstance(instance, types_Non_Generic_Type_Name)

@given(instance=Numeric_Type_Name_strategy)
@settings(max_examples=50)
def test_numeric_type_name_instantiation(instance):
    assert isinstance(instance, Numeric_Type_Name)

@given(instance=iec61131_types_Real_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_real_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Real_Type_Name)

@given(instance=iec61131_types_Integer_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_integer_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Integer_Type_Name)

@given(instance=Elementary_Type_Name_strategy)
@settings(max_examples=50)
def test_elementary_type_name_instantiation(instance):
    assert isinstance(instance, Elementary_Type_Name)

@given(instance=iec61131_types_Bit_String_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_bit_string_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Bit_String_Type_Name)

@given(instance=iec61131_types_Date_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_date_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Date_Type_Name)

@given(instance=iec61131_types_Numeric_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_numeric_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Numeric_Type_Name)

@given(instance=Data_Type_Name_strategy)
@settings(max_examples=50)
def test_data_type_name_instantiation(instance):
    assert isinstance(instance, Data_Type_Name)

@given(instance=iec61131_types_TypeLib_strategy)
@settings(max_examples=50)
def test_iec61131_types_typelib_instantiation(instance):
    assert isinstance(instance, iec61131_types_TypeLib)

@given(instance=Fbd_Network_strategy)
@settings(max_examples=50)
def test_fbd_network_instantiation(instance):
    assert isinstance(instance, Fbd_Network)

@given(instance=iec61131_sfc_Transition_Condition_strategy)
@settings(max_examples=50)
def test_iec61131_sfc_transition_condition_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Transition_Condition)

@given(instance=iec61131_sfc_Steps_strategy)
@settings(max_examples=50)
def test_iec61131_sfc_steps_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Steps)

@given(instance=iec61131_sfc_Transition_Name_strategy)
@settings(max_examples=50)
def test_iec61131_sfc_transition_name_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Transition_Name)



@given(instance=iec61131_sfc_Transition_Name_strategy)
def test_iec61131_sfc_transition_name_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iec61131_sfc_Action_Time_strategy)
@settings(max_examples=50)
def test_iec61131_sfc_action_time_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Action_Time)

@given(instance=variables_Variable_strategy)
@settings(max_examples=50)
def test_variables_variable_instantiation(instance):
    assert isinstance(instance, variables_Variable)

@given(instance=Subscript_List_strategy)
@settings(max_examples=50)
def test_subscript_list_instantiation(instance):
    assert isinstance(instance, Subscript_List)

@given(instance=Multi_Element_Variable_strategy)
@settings(max_examples=50)
def test_multi_element_variable_instantiation(instance):
    assert isinstance(instance, Multi_Element_Variable)

@given(instance=iec61131_variables_Structured_Variable_strategy)
@settings(max_examples=50)
def test_iec61131_variables_structured_variable_instantiation(instance):
    assert isinstance(instance, iec61131_variables_Structured_Variable)

@given(instance=iec61131_variables_Array_Variable_strategy)
@settings(max_examples=50)
def test_iec61131_variables_array_variable_instantiation(instance):
    assert isinstance(instance, iec61131_variables_Array_Variable)

@given(instance=iec61131_sfc_Cond2_Condition_strategy)
@settings(max_examples=50)
def test_iec61131_sfc_cond2_condition_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Cond2_Condition)

@given(instance=Cond2_Condition_strategy)
@settings(max_examples=50)
def test_cond2_condition_instantiation(instance):
    assert isinstance(instance, Cond2_Condition)

@given(instance=iec61131_fbd_Fbd_Network_strategy)
@settings(max_examples=50)
def test_iec61131_fbd_fbd_network_instantiation(instance):
    assert isinstance(instance, iec61131_fbd_Fbd_Network)

@given(instance=Steps_strategy)
@settings(max_examples=50)
def test_steps_instantiation(instance):
    assert isinstance(instance, Steps)

@given(instance=iec61131_sfc_Steps2_strategy)
@settings(max_examples=50)
def test_iec61131_sfc_steps2_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Steps2)

@given(instance=iec61131_sfc_Steps1_strategy)
@settings(max_examples=50)
def test_iec61131_sfc_steps1_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Steps1)

@given(instance=Transition_Name_strategy)
@settings(max_examples=50)
def test_transition_name_instantiation(instance):
    assert isinstance(instance, Transition_Name)

@given(instance=sfc_Step_Types_strategy)
@settings(max_examples=50)
def test_sfc_step_types_instantiation(instance):
    assert isinstance(instance, sfc_Step_Types)

@given(instance=sfc_Sfc_Elements_strategy)
@settings(max_examples=50)
def test_sfc_sfc_elements_instantiation(instance):
    assert isinstance(instance, sfc_Sfc_Elements)

@given(instance=iec61131_sfc_Step_strategy)
@settings(max_examples=50)
def test_iec61131_sfc_step_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Step)

@given(instance=Step_Types_strategy)
@settings(max_examples=50)
def test_step_types_instantiation(instance):
    assert isinstance(instance, Step_Types)

@given(instance=iec61131_sfc_Initial_Step_strategy)
@settings(max_examples=50)
def test_iec61131_sfc_initial_step_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Initial_Step)

@given(instance=Sfc_Elements_strategy)
@settings(max_examples=50)
def test_sfc_elements_instantiation(instance):
    assert isinstance(instance, Sfc_Elements)

@given(instance=iec61131_sfc_Transition_strategy)
@settings(max_examples=50)
def test_iec61131_sfc_transition_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Transition)

@given(instance=Initial_Step_strategy)
@settings(max_examples=50)
def test_initial_step_instantiation(instance):
    assert isinstance(instance, Initial_Step)

@given(instance=iec61131_sfc_Timed_Qualifier_strategy)
@settings(max_examples=50)
def test_iec61131_sfc_timed_qualifier_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Timed_Qualifier)



@given(instance=iec61131_sfc_Timed_Qualifier_strategy)
def test_iec61131_sfc_timed_qualifier_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original

@given(instance=Action_Time_strategy)
@settings(max_examples=50)
def test_action_time_instantiation(instance):
    assert isinstance(instance, Action_Time)

@given(instance=iec61131_sfc_ActionTime2_strategy)
@settings(max_examples=50)
def test_iec61131_sfc_actiontime2_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_ActionTime2)

@given(instance=Timed_Qualifier_strategy)
@settings(max_examples=50)
def test_timed_qualifier_instantiation(instance):
    assert isinstance(instance, Timed_Qualifier)

@given(instance=iec61131_sfc_Action_Qualifier_strategy)
@settings(max_examples=50)
def test_iec61131_sfc_action_qualifier_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Action_Qualifier)



@given(instance=iec61131_sfc_Action_Qualifier_strategy)
def test_iec61131_sfc_action_qualifier_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original

@given(instance=iec61131_sfc_Action_Name_strategy)
@settings(max_examples=50)
def test_iec61131_sfc_action_name_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Action_Name)



@given(instance=iec61131_sfc_Action_Name_strategy)
def test_iec61131_sfc_action_name_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Step_Name_strategy)
@settings(max_examples=50)
def test_step_name_instantiation(instance):
    assert isinstance(instance, Step_Name)

@given(instance=Action_Association_strategy)
@settings(max_examples=50)
def test_action_association_instantiation(instance):
    assert isinstance(instance, Action_Association)

@given(instance=iec61131_sfc_Step_Types_strategy)
@settings(max_examples=50)
def test_iec61131_sfc_step_types_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Step_Types)

@given(instance=Action_Qualifier_strategy)
@settings(max_examples=50)
def test_action_qualifier_instantiation(instance):
    assert isinstance(instance, Action_Qualifier)

@given(instance=iec61131_sfc_Action_Association_strategy)
@settings(max_examples=50)
def test_iec61131_sfc_action_association_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Action_Association)

@given(instance=iec61131_sfc_Sfc_Elements_strategy)
@settings(max_examples=50)
def test_iec61131_sfc_sfc_elements_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Sfc_Elements)

@given(instance=Action_Name_strategy)
@settings(max_examples=50)
def test_action_name_instantiation(instance):
    assert isinstance(instance, Action_Name)

@given(instance=iec61131_sfc_Action_strategy)
@settings(max_examples=50)
def test_iec61131_sfc_action_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Action)

@given(instance=Transition_Condition_strategy)
@settings(max_examples=50)
def test_transition_condition_instantiation(instance):
    assert isinstance(instance, Transition_Condition)

@given(instance=iec61131_sfc_Transition_Cond2_strategy)
@settings(max_examples=50)
def test_iec61131_sfc_transition_cond2_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Transition_Cond2)

@given(instance=iec61131_sfc_Transition_Cond3_strategy)
@settings(max_examples=50)
def test_iec61131_sfc_transition_cond3_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Transition_Cond3)

@given(instance=iec61131_sfc_Transition_Cond1_strategy)
@settings(max_examples=50)
def test_iec61131_sfc_transition_cond1_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Transition_Cond1)

@given(instance=iec61131_sfc_Sfc_Network_strategy)
@settings(max_examples=50)
def test_iec61131_sfc_sfc_network_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Sfc_Network)

@given(instance=Sfc_Network_strategy)
@settings(max_examples=50)
def test_sfc_network_instantiation(instance):
    assert isinstance(instance, Sfc_Network)

@given(instance=iec61131_il_Il_Assign_Out_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_il_il_assign_out_operator_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Assign_Out_Operator)

@given(instance=iec61131_il_Param_Assignment_strategy)
@settings(max_examples=50)
def test_iec61131_il_param_assignment_instantiation(instance):
    assert isinstance(instance, iec61131_il_Param_Assignment)

@given(instance=Assignment_Name_strategy)
@settings(max_examples=50)
def test_assignment_name_instantiation(instance):
    assert isinstance(instance, Assignment_Name)

@given(instance=iec61131_il_Il_Assign_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_il_il_assign_operator_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Assign_Operator)

@given(instance=iec61131_il_Param_Instruction_strategy)
@settings(max_examples=50)
def test_iec61131_il_param_instruction_instantiation(instance):
    assert isinstance(instance, iec61131_il_Param_Instruction)

@given(instance=iec61131_il_Param_Assignments_strategy)
@settings(max_examples=50)
def test_iec61131_il_param_assignments_instantiation(instance):
    assert isinstance(instance, iec61131_il_Param_Assignments)

@given(instance=Il_Assign_Out_Operator_strategy)
@settings(max_examples=50)
def test_il_assign_out_operator_instantiation(instance):
    assert isinstance(instance, Il_Assign_Out_Operator)

@given(instance=iec61131_il_Il_Operand_List_strategy)
@settings(max_examples=50)
def test_iec61131_il_il_operand_list_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Operand_List)

@given(instance=iec61131_il_Il_Simple_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_il_il_simple_operator_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Simple_Operator)

@given(instance=iec61131_il_Il_Operations_strategy)
@settings(max_examples=50)
def test_iec61131_il_il_operations_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Operations)

@given(instance=Il_Param_List_strategy)
@settings(max_examples=50)
def test_il_param_list_instantiation(instance):
    assert isinstance(instance, Il_Param_List)

@given(instance=Il_Assign_Operator_strategy)
@settings(max_examples=50)
def test_il_assign_operator_instantiation(instance):
    assert isinstance(instance, Il_Assign_Operator)

@given(instance=Param_Assignments_strategy)
@settings(max_examples=50)
def test_param_assignments_instantiation(instance):
    assert isinstance(instance, Param_Assignments)

@given(instance=iec61131_il_Il_Param_Out_Assignment_strategy)
@settings(max_examples=50)
def test_iec61131_il_il_param_out_assignment_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Param_Out_Assignment)

@given(instance=iec61131_il_Il_Param_Assignment_strategy)
@settings(max_examples=50)
def test_iec61131_il_il_param_assignment_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Param_Assignment)

@given(instance=Param_Instruction_strategy)
@settings(max_examples=50)
def test_param_instruction_instantiation(instance):
    assert isinstance(instance, Param_Instruction)

@given(instance=iec61131_il_Il_Param_Last_Instruction_strategy)
@settings(max_examples=50)
def test_iec61131_il_il_param_last_instruction_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Param_Last_Instruction)

@given(instance=iec61131_il_Il_Param_Instruction_strategy)
@settings(max_examples=50)
def test_iec61131_il_il_param_instruction_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Param_Instruction)

@given(instance=iec61131_il_Simple_Instr_strategy)
@settings(max_examples=50)
def test_iec61131_il_simple_instr_instantiation(instance):
    assert isinstance(instance, iec61131_il_Simple_Instr)

@given(instance=Simple_Instr_strategy)
@settings(max_examples=50)
def test_simple_instr_instantiation(instance):
    assert isinstance(instance, Simple_Instr)

@given(instance=iec61131_il_Il_Simple_Instruction_strategy)
@settings(max_examples=50)
def test_iec61131_il_il_simple_instruction_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Simple_Instruction)

@given(instance=iec61131_il_Operands_strategy)
@settings(max_examples=50)
def test_iec61131_il_operands_instantiation(instance):
    assert isinstance(instance, iec61131_il_Operands)

@given(instance=Il_Param_Last_Instruction_strategy)
@settings(max_examples=50)
def test_il_param_last_instruction_instantiation(instance):
    assert isinstance(instance, Il_Param_Last_Instruction)

@given(instance=Il_Param_Instruction_strategy)
@settings(max_examples=50)
def test_il_param_instruction_instantiation(instance):
    assert isinstance(instance, Il_Param_Instruction)

@given(instance=iec61131_il_Il_Param_List_strategy)
@settings(max_examples=50)
def test_iec61131_il_il_param_list_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Param_List)

@given(instance=iec61131_il_Il_Call_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_il_il_call_operator_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Call_Operator)

@given(instance=iec61131_il_Il_Jump_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_il_il_jump_operator_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Jump_Operator)

@given(instance=Il_Operand_List_strategy)
@settings(max_examples=50)
def test_il_operand_list_instantiation(instance):
    assert isinstance(instance, Il_Operand_List)

@given(instance=Il_Simple_Operator_strategy)
@settings(max_examples=50)
def test_il_simple_operator_instantiation(instance):
    assert isinstance(instance, Il_Simple_Operator)

@given(instance=iec61131_il_Il_Expr_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_il_il_expr_operator_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Expr_Operator)

@given(instance=Il_Simple_Operation_strategy)
@settings(max_examples=50)
def test_il_simple_operation_instantiation(instance):
    assert isinstance(instance, Il_Simple_Operation)

@given(instance=iec61131_il_Simple_Operation2_strategy)
@settings(max_examples=50)
def test_iec61131_il_simple_operation2_instantiation(instance):
    assert isinstance(instance, iec61131_il_Simple_Operation2)

@given(instance=iec61131_il_Simple_Operation1_strategy)
@settings(max_examples=50)
def test_iec61131_il_simple_operation1_instantiation(instance):
    assert isinstance(instance, iec61131_il_Simple_Operation1)

@given(instance=Il_Instruction_strategy)
@settings(max_examples=50)
def test_il_instruction_instantiation(instance):
    assert isinstance(instance, Il_Instruction)

@given(instance=Operands_strategy)
@settings(max_examples=50)
def test_operands_instantiation(instance):
    assert isinstance(instance, Operands)

@given(instance=iec61131_il_Operand1_strategy)
@settings(max_examples=50)
def test_iec61131_il_operand1_instantiation(instance):
    assert isinstance(instance, iec61131_il_Operand1)

@given(instance=iec61131_il_Operand2_strategy)
@settings(max_examples=50)
def test_iec61131_il_operand2_instantiation(instance):
    assert isinstance(instance, iec61131_il_Operand2)

@given(instance=Il_Call_Operator_strategy)
@settings(max_examples=50)
def test_il_call_operator_instantiation(instance):
    assert isinstance(instance, Il_Call_Operator)

@given(instance=Il_Jump_Operator_strategy)
@settings(max_examples=50)
def test_il_jump_operator_instantiation(instance):
    assert isinstance(instance, Il_Jump_Operator)

@given(instance=Simple_Instr_List_strategy)
@settings(max_examples=50)
def test_simple_instr_list_instantiation(instance):
    assert isinstance(instance, Simple_Instr_List)

@given(instance=Il_Operand_strategy)
@settings(max_examples=50)
def test_il_operand_instantiation(instance):
    assert isinstance(instance, Il_Operand)

@given(instance=il_Simple_Instr_strategy)
@settings(max_examples=50)
def test_il_simple_instr_instantiation(instance):
    assert isinstance(instance, il_Simple_Instr)

@given(instance=il_Il_Operations_strategy)
@settings(max_examples=50)
def test_il_il_operations_instantiation(instance):
    assert isinstance(instance, il_Il_Operations)

@given(instance=iec61131_il_Il_Formal_Funct_Call_strategy)
@settings(max_examples=50)
def test_iec61131_il_il_formal_funct_call_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Formal_Funct_Call)

@given(instance=iec61131_il_Il_Expression_strategy)
@settings(max_examples=50)
def test_iec61131_il_il_expression_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Expression)

@given(instance=iec61131_il_Il_Simple_Operation_strategy)
@settings(max_examples=50)
def test_iec61131_il_il_simple_operation_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Simple_Operation)

@given(instance=iec61131_il_Label_strategy)
@settings(max_examples=50)
def test_iec61131_il_label_instantiation(instance):
    assert isinstance(instance, iec61131_il_Label)



@given(instance=iec61131_il_Label_strategy)
def test_iec61131_il_label_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=Il_Operations_strategy)
@settings(max_examples=50)
def test_il_operations_instantiation(instance):
    assert isinstance(instance, Il_Operations)

@given(instance=iec61131_il_Il_Return_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_il_il_return_operator_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Return_Operator)

@given(instance=iec61131_il_Il_Fb_Call_strategy)
@settings(max_examples=50)
def test_iec61131_il_il_fb_call_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Fb_Call)

@given(instance=iec61131_il_Il_Jump_Operation_strategy)
@settings(max_examples=50)
def test_iec61131_il_il_jump_operation_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Jump_Operation)

@given(instance=Label_strategy)
@settings(max_examples=50)
def test_label_instantiation(instance):
    assert isinstance(instance, Label)

@given(instance=iec61131_il_Il_Instruction_strategy)
@settings(max_examples=50)
def test_iec61131_il_il_instruction_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Instruction)

@given(instance=Il_Simple_Instruction_strategy)
@settings(max_examples=50)
def test_il_simple_instruction_instantiation(instance):
    assert isinstance(instance, Il_Simple_Instruction)

@given(instance=iec61131_il_Simple_Instr_List_strategy)
@settings(max_examples=50)
def test_iec61131_il_simple_instr_list_instantiation(instance):
    assert isinstance(instance, iec61131_il_Simple_Instr_List)

@given(instance=Unary_Operator_strategy)
@settings(max_examples=50)
def test_unary_operator_instantiation(instance):
    assert isinstance(instance, Unary_Operator)

@given(instance=Power_Symbol_strategy)
@settings(max_examples=50)
def test_power_symbol_instantiation(instance):
    assert isinstance(instance, Power_Symbol)

@given(instance=Structured_Variable_strategy)
@settings(max_examples=50)
def test_structured_variable_instantiation(instance):
    assert isinstance(instance, Structured_Variable)

@given(instance=Array_Variable_strategy)
@settings(max_examples=50)
def test_array_variable_instantiation(instance):
    assert isinstance(instance, Array_Variable)

@given(instance=Function_Name_strategy)
@settings(max_examples=50)
def test_function_name_instantiation(instance):
    assert isinstance(instance, Function_Name)

@given(instance=Primary_Expression_strategy)
@settings(max_examples=50)
def test_primary_expression_instantiation(instance):
    assert isinstance(instance, Primary_Expression)

@given(instance=iec61131_st_Expression_Constant_strategy)
@settings(max_examples=50)
def test_iec61131_st_expression_constant_instantiation(instance):
    assert isinstance(instance, iec61131_st_Expression_Constant)

@given(instance=iec61131_st_Expression_Variable_Type_strategy)
@settings(max_examples=50)
def test_iec61131_st_expression_variable_type_instantiation(instance):
    assert isinstance(instance, iec61131_st_Expression_Variable_Type)

@given(instance=iec61131_st_Call_Expression_strategy)
@settings(max_examples=50)
def test_iec61131_st_call_expression_instantiation(instance):
    assert isinstance(instance, iec61131_st_Call_Expression)

@given(instance=iec61131_st_Expression_EnumValue_strategy)
@settings(max_examples=50)
def test_iec61131_st_expression_enumvalue_instantiation(instance):
    assert isinstance(instance, iec61131_st_Expression_EnumValue)

@given(instance=iec61131_st_Bracket_Expression_strategy)
@settings(max_examples=50)
def test_iec61131_st_bracket_expression_instantiation(instance):
    assert isinstance(instance, iec61131_st_Bracket_Expression)

@given(instance=Add_Operator_strategy)
@settings(max_examples=50)
def test_add_operator_instantiation(instance):
    assert isinstance(instance, Add_Operator)

@given(instance=Xor_Operator_strategy)
@settings(max_examples=50)
def test_xor_operator_instantiation(instance):
    assert isinstance(instance, Xor_Operator)

@given(instance=iec61131_st_For_List_strategy)
@settings(max_examples=50)
def test_iec61131_st_for_list_instantiation(instance):
    assert isinstance(instance, iec61131_st_For_List)

@given(instance=iec61131_st_Control_Variable_strategy)
@settings(max_examples=50)
def test_iec61131_st_control_variable_instantiation(instance):
    assert isinstance(instance, iec61131_st_Control_Variable)



@given(instance=iec61131_st_Control_Variable_strategy)
def test_iec61131_st_control_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Statement_List_strategy)
@settings(max_examples=50)
def test_statement_list_instantiation(instance):
    assert isinstance(instance, Statement_List)

@given(instance=Selection_Statement_strategy)
@settings(max_examples=50)
def test_selection_statement_instantiation(instance):
    assert isinstance(instance, Selection_Statement)

@given(instance=iec61131_st_If_Statement_strategy)
@settings(max_examples=50)
def test_iec61131_st_if_statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_If_Statement)

@given(instance=Not_Operator_strategy)
@settings(max_examples=50)
def test_not_operator_instantiation(instance):
    assert isinstance(instance, Not_Operator)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=iec61131_variables_Symbolic_Variable_strategy)
@settings(max_examples=50)
def test_iec61131_variables_symbolic_variable_instantiation(instance):
    assert isinstance(instance, iec61131_variables_Symbolic_Variable)

@given(instance=For_List_strategy)
@settings(max_examples=50)
def test_for_list_instantiation(instance):
    assert isinstance(instance, For_List)

@given(instance=Control_Variable_strategy)
@settings(max_examples=50)
def test_control_variable_instantiation(instance):
    assert isinstance(instance, Control_Variable)

@given(instance=Iteration_Statement_strategy)
@settings(max_examples=50)
def test_iteration_statement_instantiation(instance):
    assert isinstance(instance, Iteration_Statement)

@given(instance=iec61131_st_Exit_Statement_strategy)
@settings(max_examples=50)
def test_iec61131_st_exit_statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_Exit_Statement)

@given(instance=iec61131_st_While_Statement_strategy)
@settings(max_examples=50)
def test_iec61131_st_while_statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_While_Statement)

@given(instance=iec61131_st_Repeat_Statement_strategy)
@settings(max_examples=50)
def test_iec61131_st_repeat_statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_Repeat_Statement)

@given(instance=iec61131_st_For_Statement_strategy)
@settings(max_examples=50)
def test_iec61131_st_for_statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_For_Statement)

@given(instance=iec61131_st_Case_List_Element_strategy)
@settings(max_examples=50)
def test_iec61131_st_case_list_element_instantiation(instance):
    assert isinstance(instance, iec61131_st_Case_List_Element)

@given(instance=iec61131_st_Case_List_strategy)
@settings(max_examples=50)
def test_iec61131_st_case_list_instantiation(instance):
    assert isinstance(instance, iec61131_st_Case_List)

@given(instance=Case_List_strategy)
@settings(max_examples=50)
def test_case_list_instantiation(instance):
    assert isinstance(instance, Case_List)

@given(instance=iec61131_st_Case_Element_strategy)
@settings(max_examples=50)
def test_iec61131_st_case_element_instantiation(instance):
    assert isinstance(instance, iec61131_st_Case_Element)

@given(instance=iec61131_st_Else_Statement_strategy)
@settings(max_examples=50)
def test_iec61131_st_else_statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_Else_Statement)

@given(instance=iec61131_st_Else_If_Statement_strategy)
@settings(max_examples=50)
def test_iec61131_st_else_if_statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_Else_If_Statement)

@given(instance=Case_Element_strategy)
@settings(max_examples=50)
def test_case_element_instantiation(instance):
    assert isinstance(instance, Case_Element)

@given(instance=iec61131_st_Case_Statement_strategy)
@settings(max_examples=50)
def test_iec61131_st_case_statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_Case_Statement)

@given(instance=Else_Statement_strategy)
@settings(max_examples=50)
def test_else_statement_instantiation(instance):
    assert isinstance(instance, Else_Statement)

@given(instance=Else_If_Statement_strategy)
@settings(max_examples=50)
def test_else_if_statement_instantiation(instance):
    assert isinstance(instance, Else_If_Statement)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=Param_Assignment_strategy)
@settings(max_examples=50)
def test_param_assignment_instantiation(instance):
    assert isinstance(instance, Param_Assignment)

@given(instance=iec61131_st_Param_Type1_strategy)
@settings(max_examples=50)
def test_iec61131_st_param_type1_instantiation(instance):
    assert isinstance(instance, iec61131_st_Param_Type1)

@given(instance=iec61131_st_Param_Type2_strategy)
@settings(max_examples=50)
def test_iec61131_st_param_type2_instantiation(instance):
    assert isinstance(instance, iec61131_st_Param_Type2)

@given(instance=iec61131_il_Param_Assignment2_strategy)
@settings(max_examples=50)
def test_iec61131_il_param_assignment2_instantiation(instance):
    assert isinstance(instance, iec61131_il_Param_Assignment2)

@given(instance=iec61131_il_Il_Operand_strategy)
@settings(max_examples=50)
def test_iec61131_il_il_operand_instantiation(instance):
    assert isinstance(instance, iec61131_il_Il_Operand)

@given(instance=Subprogram_Control_Statement_strategy)
@settings(max_examples=50)
def test_subprogram_control_statement_instantiation(instance):
    assert isinstance(instance, Subprogram_Control_Statement)

@given(instance=iec61131_st_Fb_Invocation_strategy)
@settings(max_examples=50)
def test_iec61131_st_fb_invocation_instantiation(instance):
    assert isinstance(instance, iec61131_st_Fb_Invocation)

@given(instance=iec61131_st_Return_Statement_strategy)
@settings(max_examples=50)
def test_iec61131_st_return_statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_Return_Statement)

@given(instance=iec61131_st_Iteration_Statement_strategy)
@settings(max_examples=50)
def test_iec61131_st_iteration_statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_Iteration_Statement)

@given(instance=iec61131_st_Selection_Statement_strategy)
@settings(max_examples=50)
def test_iec61131_st_selection_statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_Selection_Statement)

@given(instance=iec61131_st_Subprogram_Control_Statement_strategy)
@settings(max_examples=50)
def test_iec61131_st_subprogram_control_statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_Subprogram_Control_Statement)

@given(instance=Expression_Variable_strategy)
@settings(max_examples=50)
def test_expression_variable_instantiation(instance):
    assert isinstance(instance, Expression_Variable)

@given(instance=iec61131_st_Assignment_Statement_strategy)
@settings(max_examples=50)
def test_iec61131_st_assignment_statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_Assignment_Statement)

@given(instance=Or_Operator_strategy)
@settings(max_examples=50)
def test_or_operator_instantiation(instance):
    assert isinstance(instance, Or_Operator)

@given(instance=Expression_Types_strategy)
@settings(max_examples=50)
def test_expression_types_instantiation(instance):
    assert isinstance(instance, Expression_Types)

@given(instance=iec61131_st_Xor_Expression_strategy)
@settings(max_examples=50)
def test_iec61131_st_xor_expression_instantiation(instance):
    assert isinstance(instance, iec61131_st_Xor_Expression)

@given(instance=iec61131_st_Power_Expression_strategy)
@settings(max_examples=50)
def test_iec61131_st_power_expression_instantiation(instance):
    assert isinstance(instance, iec61131_st_Power_Expression)

@given(instance=iec61131_st_Unary_Expression_strategy)
@settings(max_examples=50)
def test_iec61131_st_unary_expression_instantiation(instance):
    assert isinstance(instance, iec61131_st_Unary_Expression)

@given(instance=iec61131_st_Equ_Expression_strategy)
@settings(max_examples=50)
def test_iec61131_st_equ_expression_instantiation(instance):
    assert isinstance(instance, iec61131_st_Equ_Expression)

@given(instance=iec61131_st_And_Expression_strategy)
@settings(max_examples=50)
def test_iec61131_st_and_expression_instantiation(instance):
    assert isinstance(instance, iec61131_st_And_Expression)

@given(instance=iec61131_st_Add_Expression_strategy)
@settings(max_examples=50)
def test_iec61131_st_add_expression_instantiation(instance):
    assert isinstance(instance, iec61131_st_Add_Expression)

@given(instance=iec61131_st_Term_Expression_strategy)
@settings(max_examples=50)
def test_iec61131_st_term_expression_instantiation(instance):
    assert isinstance(instance, iec61131_st_Term_Expression)

@given(instance=iec61131_st_Comparison_strategy)
@settings(max_examples=50)
def test_iec61131_st_comparison_instantiation(instance):
    assert isinstance(instance, iec61131_st_Comparison)

@given(instance=iec61131_st_Primary_Expression_strategy)
@settings(max_examples=50)
def test_iec61131_st_primary_expression_instantiation(instance):
    assert isinstance(instance, iec61131_st_Primary_Expression)

@given(instance=iec61131_st_Expression_strategy)
@settings(max_examples=50)
def test_iec61131_st_expression_instantiation(instance):
    assert isinstance(instance, iec61131_st_Expression)

@given(instance=iec61131_configurations_Prog_Data_Source_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_prog_data_source_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Prog_Data_Source)

@given(instance=iec61131_configurations_Prog_Conf_Element_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_prog_conf_element_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Prog_Conf_Element)

@given(instance=Prog_Conf_Element_strategy)
@settings(max_examples=50)
def test_prog_conf_element_instantiation(instance):
    assert isinstance(instance, Prog_Conf_Element)

@given(instance=iec61131_configurations_Fb_Task_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_fb_task_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Fb_Task)

@given(instance=iec61131_configurations_Prog_Cnxn_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_prog_cnxn_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Prog_Cnxn)

@given(instance=iec61131_configurations_Prog_Conf_Elements_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_prog_conf_elements_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Prog_Conf_Elements)

@given(instance=Task_Initialization_strategy)
@settings(max_examples=50)
def test_task_initialization_instantiation(instance):
    assert isinstance(instance, Task_Initialization)

@given(instance=iec61131_configurations_Priority_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_priority_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Priority)

@given(instance=iec61131_configurations_Interval_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_interval_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Interval)

@given(instance=iec61131_configurations_Single_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_single_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Single)

@given(instance=iec61131_configurations_Instance_Specific_Init_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_instance_specific_init_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Instance_Specific_Init)

@given(instance=iec61131_configurations_Data_Sink_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_data_sink_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Data_Sink)

@given(instance=Prog_Data_Source_strategy)
@settings(max_examples=50)
def test_prog_data_source_instantiation(instance):
    assert isinstance(instance, Prog_Data_Source)

@given(instance=Data_Sink_strategy)
@settings(max_examples=50)
def test_data_sink_instantiation(instance):
    assert isinstance(instance, Data_Sink)

@given(instance=Prog_Cnxn_strategy)
@settings(max_examples=50)
def test_prog_cnxn_instantiation(instance):
    assert isinstance(instance, Prog_Cnxn)

@given(instance=iec61131_configurations_Prog_Source_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_prog_source_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Prog_Source)

@given(instance=iec61131_configurations_Prog_Sink_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_prog_sink_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Prog_Sink)

@given(instance=Data_Source_strategy)
@settings(max_examples=50)
def test_data_source_instantiation(instance):
    assert isinstance(instance, Data_Source)

@given(instance=iec61131_configurations_Program_Output_Reference_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_program_output_reference_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Program_Output_Reference)

@given(instance=configurations_Data_Sink_strategy)
@settings(max_examples=50)
def test_configurations_data_sink_instantiation(instance):
    assert isinstance(instance, configurations_Data_Sink)

@given(instance=iec61131_configurations_Data_Source_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_data_source_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Data_Source)

@given(instance=Instance_Specific_Init_strategy)
@settings(max_examples=50)
def test_instance_specific_init_instantiation(instance):
    assert isinstance(instance, Instance_Specific_Init)

@given(instance=iec61131_configurations_Instance_Spec2_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_instance_spec2_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Instance_Spec2)

@given(instance=iec61131_configurations_Instance_Spec1_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_instance_spec1_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Instance_Spec1)

@given(instance=iec61131_configurations_Instance_Specific_Initializations_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_instance_specific_initializations_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Instance_Specific_Initializations)

@given(instance=iec61131_types_Byte_String_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_byte_string_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Byte_String_Type_Name)

@given(instance=Single_Element_Type_Name_strategy)
@settings(max_examples=50)
def test_single_element_type_name_instantiation(instance):
    assert isinstance(instance, Single_Element_Type_Name)

@given(instance=iec61131_types_Enumerated_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_enumerated_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Enumerated_Type_Name)

@given(instance=iec61131_types_Subrange_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_subrange_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Subrange_Type_Name)

@given(instance=types_Single_Element_Type_Name_strategy)
@settings(max_examples=50)
def test_types_single_element_type_name_instantiation(instance):
    assert isinstance(instance, types_Single_Element_Type_Name)

@given(instance=types_Derived_Type_Name_strategy)
@settings(max_examples=50)
def test_types_derived_type_name_instantiation(instance):
    assert isinstance(instance, types_Derived_Type_Name)

@given(instance=Derived_Type_Name_strategy)
@settings(max_examples=50)
def test_derived_type_name_instantiation(instance):
    assert isinstance(instance, Derived_Type_Name)

@given(instance=iec61131_types_Array_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_array_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Array_Type_Name)

@given(instance=iec61131_types_String_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_string_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_String_Type_Name)

@given(instance=iec61131_types_Single_Element_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_single_element_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Single_Element_Type_Name)

@given(instance=iec61131_types_Duration_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_duration_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Duration_Type_Name)

@given(instance=iec61131_ld_Rung_strategy)
@settings(max_examples=50)
def test_iec61131_ld_rung_instantiation(instance):
    assert isinstance(instance, iec61131_ld_Rung)

@given(instance=iec61131_types_Simple_Specification_strategy)
@settings(max_examples=50)
def test_iec61131_types_simple_specification_instantiation(instance):
    assert isinstance(instance, iec61131_types_Simple_Specification)

@given(instance=iec61131_variables_Subscript_List_strategy)
@settings(max_examples=50)
def test_iec61131_variables_subscript_list_instantiation(instance):
    assert isinstance(instance, iec61131_variables_Subscript_List)

@given(instance=Input_Reference_strategy)
@settings(max_examples=50)
def test_input_reference_instantiation(instance):
    assert isinstance(instance, Input_Reference)

@given(instance=iec61131_configurations_Task_Initialization_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_task_initialization_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Task_Initialization)

@given(instance=iec61131_configurations_Task_Name_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_task_name_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Task_Name)



@given(instance=iec61131_configurations_Task_Name_strategy)
def test_iec61131_configurations_task_name_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iec61131_configurations_Program_Name_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_program_name_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Program_Name)



@given(instance=iec61131_configurations_Program_Name_strategy)
def test_iec61131_configurations_program_name_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iec61131_configurations_Access_Path_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_access_path_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Access_Path)

@given(instance=iec61131_configurations_Access_Name_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_access_name_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Access_Name)



@given(instance=iec61131_configurations_Access_Name_strategy)
def test_iec61131_configurations_access_name_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Access_Path_strategy)
@settings(max_examples=50)
def test_access_path_instantiation(instance):
    assert isinstance(instance, Access_Path)

@given(instance=iec61131_configurations_Symbolic_Path_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_symbolic_path_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Symbolic_Path)

@given(instance=iec61131_configurations_Direct_Path_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_direct_path_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Direct_Path)

@given(instance=iec61131_configurations_Access_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_access_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Access_Declaration)



@given(instance=iec61131_configurations_Access_Declaration_strategy)
def test_iec61131_configurations_access_declaration_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=Access_Declaration_strategy)
@settings(max_examples=50)
def test_access_declaration_instantiation(instance):
    assert isinstance(instance, Access_Declaration)

@given(instance=iec61131_configurations_Access_Declarations_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_access_declarations_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Access_Declarations)

@given(instance=Resource_Declaration_strategy)
@settings(max_examples=50)
def test_resource_declaration_instantiation(instance):
    assert isinstance(instance, Resource_Declaration)

@given(instance=Access_Declarations_strategy)
@settings(max_examples=50)
def test_access_declarations_instantiation(instance):
    assert isinstance(instance, Access_Declarations)

@given(instance=Instance_Specific_Initializations_strategy)
@settings(max_examples=50)
def test_instance_specific_initializations_instantiation(instance):
    assert isinstance(instance, Instance_Specific_Initializations)

@given(instance=Global_Var_Declarations_strategy)
@settings(max_examples=50)
def test_global_var_declarations_instantiation(instance):
    assert isinstance(instance, Global_Var_Declarations)

@given(instance=Single_Resource_Declaration_strategy)
@settings(max_examples=50)
def test_single_resource_declaration_instantiation(instance):
    assert isinstance(instance, Single_Resource_Declaration)

@given(instance=Configuration_Name_strategy)
@settings(max_examples=50)
def test_configuration_name_instantiation(instance):
    assert isinstance(instance, Configuration_Name)

@given(instance=Prog_Conf_Elements_strategy)
@settings(max_examples=50)
def test_prog_conf_elements_instantiation(instance):
    assert isinstance(instance, Prog_Conf_Elements)

@given(instance=Program_Name_strategy)
@settings(max_examples=50)
def test_program_name_instantiation(instance):
    assert isinstance(instance, Program_Name)

@given(instance=Single_strategy)
@settings(max_examples=50)
def test_single_instantiation(instance):
    assert isinstance(instance, Single)

@given(instance=Priority_strategy)
@settings(max_examples=50)
def test_priority_instantiation(instance):
    assert isinstance(instance, Priority)

@given(instance=Task_Name_strategy)
@settings(max_examples=50)
def test_task_name_instantiation(instance):
    assert isinstance(instance, Task_Name)

@given(instance=iec61131_configurations_Task_Configuration_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_task_configuration_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Task_Configuration)

@given(instance=Program_Configuration_strategy)
@settings(max_examples=50)
def test_program_configuration_instantiation(instance):
    assert isinstance(instance, Program_Configuration)

@given(instance=Task_Configuration_strategy)
@settings(max_examples=50)
def test_task_configuration_instantiation(instance):
    assert isinstance(instance, Task_Configuration)

@given(instance=iec61131_configurations_Single_Resource_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_single_resource_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Single_Resource_Declaration)

@given(instance=Resource_Type_Name_strategy)
@settings(max_examples=50)
def test_resource_type_name_instantiation(instance):
    assert isinstance(instance, Resource_Type_Name)

@given(instance=Resource_Name_strategy)
@settings(max_examples=50)
def test_resource_name_instantiation(instance):
    assert isinstance(instance, Resource_Name)

@given(instance=iec61131_configurations_Resource_Name_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_resource_name_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Resource_Name)



@given(instance=iec61131_configurations_Resource_Name_strategy)
def test_iec61131_configurations_resource_name_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Simple_Type_Name_strategy)
@settings(max_examples=50)
def test_simple_type_name_instantiation(instance):
    assert isinstance(instance, Simple_Type_Name)

@given(instance=Single_Element_Type_Declaration_strategy)
@settings(max_examples=50)
def test_single_element_type_declaration_instantiation(instance):
    assert isinstance(instance, Single_Element_Type_Declaration)

@given(instance=iec61131_pous_Subrange_Type_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_pous_subrange_type_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Subrange_Type_Declaration)

@given(instance=iec61131_pous_Simple_Type_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_pous_simple_type_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Simple_Type_Declaration)

@given(instance=Function_Block_Declaration_strategy)
@settings(max_examples=50)
def test_function_block_declaration_instantiation(instance):
    assert isinstance(instance, Function_Block_Declaration)

@given(instance=Function_Declaration_strategy)
@settings(max_examples=50)
def test_function_declaration_instantiation(instance):
    assert isinstance(instance, Function_Declaration)

@given(instance=Program_Declaration_strategy)
@settings(max_examples=50)
def test_program_declaration_instantiation(instance):
    assert isinstance(instance, Program_Declaration)

@given(instance=iec61131_pous_Library_strategy)
@settings(max_examples=50)
def test_iec61131_pous_library_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Library)

@given(instance=Program_Access_Decl_strategy)
@settings(max_examples=50)
def test_program_access_decl_instantiation(instance):
    assert isinstance(instance, Program_Access_Decl)

@given(instance=iec61131_pous_Function_Block_Vars_strategy)
@settings(max_examples=50)
def test_iec61131_pous_function_block_vars_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Function_Block_Vars)

@given(instance=iec61131_pous_Function_Vars_strategy)
@settings(max_examples=50)
def test_iec61131_pous_function_vars_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Function_Vars)

@given(instance=iec61131_pous_Program_Vars_strategy)
@settings(max_examples=50)
def test_iec61131_pous_program_vars_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Program_Vars)

@given(instance=iec61131_pous_Structure_Elements_strategy)
@settings(max_examples=50)
def test_iec61131_pous_structure_elements_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Structure_Elements)

@given(instance=Structure_Elements_strategy)
@settings(max_examples=50)
def test_structure_elements_instantiation(instance):
    assert isinstance(instance, Structure_Elements)

@given(instance=iec61131_pous_Structure_Element_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_pous_structure_element_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Structure_Element_Declaration)

@given(instance=Structure_Element_Declaration_strategy)
@settings(max_examples=50)
def test_structure_element_declaration_instantiation(instance):
    assert isinstance(instance, Structure_Element_Declaration)

@given(instance=iec61131_pous_Structure_Specification_strategy)
@settings(max_examples=50)
def test_iec61131_pous_structure_specification_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Structure_Specification)

@given(instance=Enumerated_Spec_Init_strategy)
@settings(max_examples=50)
def test_enumerated_spec_init_instantiation(instance):
    assert isinstance(instance, Enumerated_Spec_Init)

@given(instance=iec61131_pous_Enumerated_Type_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_pous_enumerated_type_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Enumerated_Type_Declaration)

@given(instance=Subrange_Spec_Init_strategy)
@settings(max_examples=50)
def test_subrange_spec_init_instantiation(instance):
    assert isinstance(instance, Subrange_Spec_Init)

@given(instance=pous_Function_Block_Body_strategy)
@settings(max_examples=50)
def test_pous_function_block_body_instantiation(instance):
    assert isinstance(instance, pous_Function_Block_Body)

@given(instance=pous_Function_Body_strategy)
@settings(max_examples=50)
def test_pous_function_body_instantiation(instance):
    assert isinstance(instance, pous_Function_Body)

@given(instance=iec61131_ld_Ladder_Diagram_strategy)
@settings(max_examples=50)
def test_iec61131_ld_ladder_diagram_instantiation(instance):
    assert isinstance(instance, iec61131_ld_Ladder_Diagram)

@given(instance=iec61131_fbd_Function_Block_Diagram_strategy)
@settings(max_examples=50)
def test_iec61131_fbd_function_block_diagram_instantiation(instance):
    assert isinstance(instance, iec61131_fbd_Function_Block_Diagram)

@given(instance=iec61131_st_Statement_List_strategy)
@settings(max_examples=50)
def test_iec61131_st_statement_list_instantiation(instance):
    assert isinstance(instance, iec61131_st_Statement_List)

@given(instance=iec61131_il_Instruction_List_strategy)
@settings(max_examples=50)
def test_iec61131_il_instruction_list_instantiation(instance):
    assert isinstance(instance, iec61131_il_Instruction_List)

@given(instance=iec61131_pous_Other_Language_strategy)
@settings(max_examples=50)
def test_iec61131_pous_other_language_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Other_Language)



@given(instance=iec61131_pous_Other_Language_strategy)
def test_iec61131_pous_other_language_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=iec61131_pous_Function_Body_strategy)
@settings(max_examples=50)
def test_iec61131_pous_function_body_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Function_Body)

@given(instance=iec61131_pous_Function_Return_Value_strategy)
@settings(max_examples=50)
def test_iec61131_pous_function_return_value_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Function_Return_Value)

@given(instance=pous_Function_Name_strategy)
@settings(max_examples=50)
def test_pous_function_name_instantiation(instance):
    assert isinstance(instance, pous_Function_Name)

@given(instance=Function_Body_strategy)
@settings(max_examples=50)
def test_function_body_instantiation(instance):
    assert isinstance(instance, Function_Body)

@given(instance=Function_Vars_strategy)
@settings(max_examples=50)
def test_function_vars_instantiation(instance):
    assert isinstance(instance, Function_Vars)

@given(instance=Byte_String_Type_Name_strategy)
@settings(max_examples=50)
def test_byte_string_type_name_instantiation(instance):
    assert isinstance(instance, Byte_String_Type_Name)

@given(instance=iec61131_types_Double_Byte_String_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_double_byte_string_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Double_Byte_String_Type_Name)

@given(instance=iec61131_types_Single_Byte_String_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_single_byte_string_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Single_Byte_String_Type_Name)

@given(instance=String_Type_Name_strategy)
@settings(max_examples=50)
def test_string_type_name_instantiation(instance):
    assert isinstance(instance, String_Type_Name)

@given(instance=Structure_Specification_strategy)
@settings(max_examples=50)
def test_structure_specification_instantiation(instance):
    assert isinstance(instance, Structure_Specification)

@given(instance=iec61131_pous_Structure_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_pous_structure_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Structure_Declaration)

@given(instance=iec61131_pous_Type_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_pous_type_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Type_Declaration)

@given(instance=Type_Declaration_strategy)
@settings(max_examples=50)
def test_type_declaration_instantiation(instance):
    assert isinstance(instance, Type_Declaration)

@given(instance=iec61131_pous_Structure_Type_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_pous_structure_type_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Structure_Type_Declaration)

@given(instance=iec61131_pous_Array_Type_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_pous_array_type_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Array_Type_Declaration)

@given(instance=iec61131_pous_String_Type_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_pous_string_type_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_String_Type_Declaration)

@given(instance=iec61131_pous_Single_Element_Type_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_pous_single_element_type_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Single_Element_Type_Declaration)

@given(instance=iec61131_pous_Access_Name_strategy)
@settings(max_examples=50)
def test_iec61131_pous_access_name_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Access_Name)



@given(instance=iec61131_pous_Access_Name_strategy)
def test_iec61131_pous_access_name_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Symbolic_Variable_strategy)
@settings(max_examples=50)
def test_symbolic_variable_instantiation(instance):
    assert isinstance(instance, Symbolic_Variable)

@given(instance=iec61131_variables_Multi_Element_Variable_strategy)
@settings(max_examples=50)
def test_iec61131_variables_multi_element_variable_instantiation(instance):
    assert isinstance(instance, iec61131_variables_Multi_Element_Variable)

@given(instance=Access_Name_strategy)
@settings(max_examples=50)
def test_access_name_instantiation(instance):
    assert isinstance(instance, Access_Name)

@given(instance=iec61131_pous_Program_Access_Decl_strategy)
@settings(max_examples=50)
def test_iec61131_pous_program_access_decl_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Program_Access_Decl)



@given(instance=iec61131_pous_Program_Access_Decl_strategy)
def test_iec61131_pous_program_access_decl_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=iec61131_pous_Function_Block_Body_strategy)
@settings(max_examples=50)
def test_iec61131_pous_function_block_body_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Function_Block_Body)

@given(instance=Program_Type_Name_strategy)
@settings(max_examples=50)
def test_program_type_name_instantiation(instance):
    assert isinstance(instance, Program_Type_Name)

@given(instance=Function_Return_Value_strategy)
@settings(max_examples=50)
def test_function_return_value_instantiation(instance):
    assert isinstance(instance, Function_Return_Value)

@given(instance=Derived_Function_Name_strategy)
@settings(max_examples=50)
def test_derived_function_name_instantiation(instance):
    assert isinstance(instance, Derived_Function_Name)

@given(instance=Function_Block_Vars_strategy)
@settings(max_examples=50)
def test_function_block_vars_instantiation(instance):
    assert isinstance(instance, Function_Block_Vars)

@given(instance=Derived_Function_Block_Name_strategy)
@settings(max_examples=50)
def test_derived_function_block_name_instantiation(instance):
    assert isinstance(instance, Derived_Function_Block_Name)

@given(instance=pous_Function_Block_Type_Name_strategy)
@settings(max_examples=50)
def test_pous_function_block_type_name_instantiation(instance):
    assert isinstance(instance, pous_Function_Block_Type_Name)

@given(instance=types_Simple_Specification_strategy)
@settings(max_examples=50)
def test_types_simple_specification_instantiation(instance):
    assert isinstance(instance, types_Simple_Specification)

@given(instance=iec61131_types_Generic_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_generic_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Generic_Type_Name)

@given(instance=iec61131_types_Elementary_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_elementary_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Elementary_Type_Name)

@given(instance=iec61131_types_Simple_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_simple_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Simple_Type_Name)

@given(instance=Blocks_strategy)
@settings(max_examples=50)
def test_blocks_instantiation(instance):
    assert isinstance(instance, Blocks)

@given(instance=iec61131_pous_Derived_Function_Name_strategy)
@settings(max_examples=50)
def test_iec61131_pous_derived_function_name_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Derived_Function_Name)

@given(instance=iec61131_pous_Derived_Function_Block_Name_strategy)
@settings(max_examples=50)
def test_iec61131_pous_derived_function_block_name_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Derived_Function_Block_Name)

@given(instance=Function_Block_Body_strategy)
@settings(max_examples=50)
def test_function_block_body_instantiation(instance):
    assert isinstance(instance, Function_Block_Body)

@given(instance=iec61131_sfc_Sequential_Function_Chart_strategy)
@settings(max_examples=50)
def test_iec61131_sfc_sequential_function_chart_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Sequential_Function_Chart)

@given(instance=iec61131_interfaces_Simple_Specification_Func_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_simple_specification_func_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Simple_Specification_Func)

@given(instance=Simple_Specification_Func_strategy)
@settings(max_examples=50)
def test_simple_specification_func_instantiation(instance):
    assert isinstance(instance, Simple_Specification_Func)

@given(instance=Var1_Specification_Func_strategy)
@settings(max_examples=50)
def test_var1_specification_func_instantiation(instance):
    assert isinstance(instance, Var1_Specification_Func)

@given(instance=iec61131_interfaces_Simple_Spec_Init_Func_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_simple_spec_init_func_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Simple_Spec_Init_Func)

@given(instance=Simple_Spec_Init_strategy)
@settings(max_examples=50)
def test_simple_spec_init_instantiation(instance):
    assert isinstance(instance, Simple_Spec_Init)

@given(instance=iec61131_interfaces_Var_Name_Decl_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_var_name_decl_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Var_Name_Decl)

@given(instance=Array_Type_Name_strategy)
@settings(max_examples=50)
def test_array_type_name_instantiation(instance):
    assert isinstance(instance, Array_Type_Name)

@given(instance=iec61131_interfaces_Initial_Element_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_initial_element_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Initial_Element)

@given(instance=Non_Generic_Type_Name_strategy)
@settings(max_examples=50)
def test_non_generic_type_name_instantiation(instance):
    assert isinstance(instance, Non_Generic_Type_Name)

@given(instance=iec61131_types_Derived_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_derived_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Derived_Type_Name)

@given(instance=Global_Var_Decl_strategy)
@settings(max_examples=50)
def test_global_var_decl_instantiation(instance):
    assert isinstance(instance, Global_Var_Decl)

@given(instance=Library_Element_Declaration_strategy)
@settings(max_examples=50)
def test_library_element_declaration_instantiation(instance):
    assert isinstance(instance, Library_Element_Declaration)

@given(instance=iec61131_configurations_Configuration_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_configuration_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Configuration_Declaration)

@given(instance=iec61131_pous_Data_Type_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_pous_data_type_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Data_Type_Declaration)

@given(instance=iec61131_pous_Program_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_pous_program_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Program_Declaration)

@given(instance=iec61131_pous_Function_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_pous_function_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Function_Declaration)

@given(instance=iec61131_pous_Function_Block_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_pous_function_block_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Function_Block_Declaration)

@given(instance=iec61131_configurations_Resource_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_resource_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Resource_Declaration)

@given(instance=iec61131_interfaces_Global_Var_Declarations_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_global_var_declarations_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Global_Var_Declarations)



@given(instance=iec61131_interfaces_Global_Var_Declarations_strategy)
def test_iec61131_interfaces_global_var_declarations_retain_setter(instance):
    original = instance.retain
    instance.retain = original
    assert instance.retain == original



@given(instance=iec61131_interfaces_Global_Var_Declarations_strategy)
def test_iec61131_interfaces_global_var_declarations_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=Located_Var_Decl_strategy)
@settings(max_examples=50)
def test_located_var_decl_instantiation(instance):
    assert isinstance(instance, Located_Var_Decl)

@given(instance=Program_Vars_strategy)
@settings(max_examples=50)
def test_program_vars_instantiation(instance):
    assert isinstance(instance, Program_Vars)

@given(instance=iec61131_pous_Program_Access_Decls_strategy)
@settings(max_examples=50)
def test_iec61131_pous_program_access_decls_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Program_Access_Decls)

@given(instance=iec61131_interfaces_Located_Var_Declarations_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_located_var_declarations_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Located_Var_Declarations)



@given(instance=iec61131_interfaces_Located_Var_Declarations_strategy)
def test_iec61131_interfaces_located_var_declarations_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original



@given(instance=iec61131_interfaces_Located_Var_Declarations_strategy)
def test_iec61131_interfaces_located_var_declarations_retain_setter(instance):
    original = instance.retain
    instance.retain = original
    assert instance.retain == original

@given(instance=Subrange_Type_Name_strategy)
@settings(max_examples=50)
def test_subrange_type_name_instantiation(instance):
    assert isinstance(instance, Subrange_Type_Name)

@given(instance=Subrange_strategy)
@settings(max_examples=50)
def test_subrange_instantiation(instance):
    assert isinstance(instance, Subrange)

@given(instance=Double_Byte_String_Type_Name_strategy)
@settings(max_examples=50)
def test_double_byte_string_type_name_instantiation(instance):
    assert isinstance(instance, Double_Byte_String_Type_Name)

@given(instance=Single_Byte_String_Type_Name_strategy)
@settings(max_examples=50)
def test_single_byte_string_type_name_instantiation(instance):
    assert isinstance(instance, Single_Byte_String_Type_Name)

@given(instance=Byte_String_strategy)
@settings(max_examples=50)
def test_byte_string_instantiation(instance):
    assert isinstance(instance, Byte_String)

@given(instance=iec61131_interfaces_Double_BString_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_double_bstring_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Double_BString)

@given(instance=iec61131_interfaces_Single_BString_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_single_bstring_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Single_BString)

@given(instance=iec61131_interfaces_Range_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_range_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Range)

@given(instance=Initialized_Structure_strategy)
@settings(max_examples=50)
def test_initialized_structure_instantiation(instance):
    assert isinstance(instance, Initialized_Structure)

@given(instance=Array_Spec_Init_strategy)
@settings(max_examples=50)
def test_array_spec_init_instantiation(instance):
    assert isinstance(instance, Array_Spec_Init)

@given(instance=Var2_Init_Decl_strategy)
@settings(max_examples=50)
def test_var2_init_decl_instantiation(instance):
    assert isinstance(instance, Var2_Init_Decl)

@given(instance=iec61131_interfaces_Var_Init_Decl_Func_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_var_init_decl_func_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Var_Init_Decl_Func)

@given(instance=iec61131_interfaces_Structured_Var_Init_Decl_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_structured_var_init_decl_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Structured_Var_Init_Decl)

@given(instance=iec61131_interfaces_Array_Var_Init_Decl_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_array_var_init_decl_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Array_Var_Init_Decl)

@given(instance=Enumerated_Value_strategy)
@settings(max_examples=50)
def test_enumerated_value_instantiation(instance):
    assert isinstance(instance, Enumerated_Value)

@given(instance=Enumerated_Specification_strategy)
@settings(max_examples=50)
def test_enumerated_specification_instantiation(instance):
    assert isinstance(instance, Enumerated_Specification)

@given(instance=iec61131_interfaces_Enumerated_Specification1_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_enumerated_specification1_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Enumerated_Specification1)

@given(instance=iec61131_interfaces_Enumerated_Specification2_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_enumerated_specification2_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Enumerated_Specification2)

@given(instance=Signed_Integer_strategy)
@settings(max_examples=50)
def test_signed_integer_instantiation(instance):
    assert isinstance(instance, Signed_Integer)

@given(instance=Subrange_Specification_strategy)
@settings(max_examples=50)
def test_subrange_specification_instantiation(instance):
    assert isinstance(instance, Subrange_Specification)

@given(instance=iec61131_interfaces_Subrange_Specification2_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_subrange_specification2_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Subrange_Specification2)

@given(instance=iec61131_interfaces_Subrange_Specification1_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_subrange_specification1_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Subrange_Specification1)

@given(instance=interfaces_Var1_Specification_Func_strategy)
@settings(max_examples=50)
def test_interfaces_var1_specification_func_instantiation(instance):
    assert isinstance(instance, interfaces_Var1_Specification_Func)

@given(instance=Simple_Specification_strategy)
@settings(max_examples=50)
def test_simple_specification_instantiation(instance):
    assert isinstance(instance, Simple_Specification)

@given(instance=pous_Structure_Elements_strategy)
@settings(max_examples=50)
def test_pous_structure_elements_instantiation(instance):
    assert isinstance(instance, pous_Structure_Elements)

@given(instance=interfaces_Located_Var_Spec_Init_strategy)
@settings(max_examples=50)
def test_interfaces_located_var_spec_init_instantiation(instance):
    assert isinstance(instance, interfaces_Located_Var_Spec_Init)

@given(instance=interfaces_Var1_Specification_strategy)
@settings(max_examples=50)
def test_interfaces_var1_specification_instantiation(instance):
    assert isinstance(instance, interfaces_Var1_Specification)

@given(instance=iec61131_interfaces_Subrange_Spec_Init_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_subrange_spec_init_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Subrange_Spec_Init)

@given(instance=iec61131_interfaces_Enumerated_Spec_Init_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_enumerated_spec_init_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Enumerated_Spec_Init)

@given(instance=iec61131_interfaces_Simple_Spec_Init_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_simple_spec_init_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Simple_Spec_Init)

@given(instance=Assignment_Symbol_strategy)
@settings(max_examples=50)
def test_assignment_symbol_instantiation(instance):
    assert isinstance(instance, Assignment_Symbol)

@given(instance=iec61131_interfaces_Var1_Specification_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_var1_specification_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Var1_Specification)

@given(instance=Bool_Type_Name_strategy)
@settings(max_examples=50)
def test_bool_type_name_instantiation(instance):
    assert isinstance(instance, Bool_Type_Name)

@given(instance=operators_Divide_Operator_strategy)
@settings(max_examples=50)
def test_operators_divide_operator_instantiation(instance):
    assert isinstance(instance, operators_Divide_Operator)

@given(instance=Multiply_Operator_strategy)
@settings(max_examples=50)
def test_multiply_operator_instantiation(instance):
    assert isinstance(instance, Multiply_Operator)

@given(instance=iec61131_operators_Multiply_Symbol_strategy)
@settings(max_examples=50)
def test_iec61131_operators_multiply_symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Multiply_Symbol)

@given(instance=operators_Multiply_Operator_strategy)
@settings(max_examples=50)
def test_operators_multiply_operator_instantiation(instance):
    assert isinstance(instance, operators_Multiply_Operator)

@given(instance=operators_Add_Operator_strategy)
@settings(max_examples=50)
def test_operators_add_operator_instantiation(instance):
    assert isinstance(instance, operators_Add_Operator)

@given(instance=operators_Arithmetic_Name_strategy)
@settings(max_examples=50)
def test_operators_arithmetic_name_instantiation(instance):
    assert isinstance(instance, operators_Arithmetic_Name)

@given(instance=iec61131_operators_Divide_Name_strategy)
@settings(max_examples=50)
def test_iec61131_operators_divide_name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Divide_Name)

@given(instance=iec61131_operators_Multiply_Name_strategy)
@settings(max_examples=50)
def test_iec61131_operators_multiply_name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Multiply_Name)

@given(instance=operators_Addition_Operator_strategy)
@settings(max_examples=50)
def test_operators_addition_operator_instantiation(instance):
    assert isinstance(instance, operators_Addition_Operator)

@given(instance=iec61131_operators_Addition_Symbol_strategy)
@settings(max_examples=50)
def test_iec61131_operators_addition_symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Addition_Symbol)

@given(instance=iec61131_operators_Addition_Name_strategy)
@settings(max_examples=50)
def test_iec61131_operators_addition_name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Addition_Name)

@given(instance=Comparison_Operator_strategy)
@settings(max_examples=50)
def test_comparison_operator_instantiation(instance):
    assert isinstance(instance, Comparison_Operator)

@given(instance=iec61131_operators_LessEqual_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_operators_lessequal_operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_LessEqual_Operator)

@given(instance=iec61131_operators_GreaterEqual_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_operators_greaterequal_operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_GreaterEqual_Operator)

@given(instance=iec61131_operators_Greater_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_operators_greater_operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Greater_Operator)

@given(instance=iec61131_operators_Less_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_operators_less_operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Less_Operator)

@given(instance=Il_Expr_Operator_strategy)
@settings(max_examples=50)
def test_il_expr_operator_instantiation(instance):
    assert isinstance(instance, Il_Expr_Operator)

@given(instance=iec61131_operators_Arithmetic_Name_strategy)
@settings(max_examples=50)
def test_iec61131_operators_arithmetic_name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Arithmetic_Name)

@given(instance=iec61131_operators_Comparison_Name_strategy)
@settings(max_examples=50)
def test_iec61131_operators_comparison_name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Comparison_Name)

@given(instance=operators_Substraction_Operator_strategy)
@settings(max_examples=50)
def test_operators_substraction_operator_instantiation(instance):
    assert isinstance(instance, operators_Substraction_Operator)

@given(instance=iec61131_operators_Substraction_Name_strategy)
@settings(max_examples=50)
def test_iec61131_operators_substraction_name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Substraction_Name)

@given(instance=GreaterEqual_Operator_strategy)
@settings(max_examples=50)
def test_greaterequal_operator_instantiation(instance):
    assert isinstance(instance, GreaterEqual_Operator)

@given(instance=iec61131_operators_GreaterEqual_Symbol_strategy)
@settings(max_examples=50)
def test_iec61131_operators_greaterequal_symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_GreaterEqual_Symbol)

@given(instance=operators_GreaterEqual_Operator_strategy)
@settings(max_examples=50)
def test_operators_greaterequal_operator_instantiation(instance):
    assert isinstance(instance, operators_GreaterEqual_Operator)

@given(instance=Greater_Operator_strategy)
@settings(max_examples=50)
def test_greater_operator_instantiation(instance):
    assert isinstance(instance, Greater_Operator)

@given(instance=iec61131_operators_Greater_Symbol_strategy)
@settings(max_examples=50)
def test_iec61131_operators_greater_symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Greater_Symbol)

@given(instance=operators_Greater_Operator_strategy)
@settings(max_examples=50)
def test_operators_greater_operator_instantiation(instance):
    assert isinstance(instance, operators_Greater_Operator)

@given(instance=LessEqual_Operator_strategy)
@settings(max_examples=50)
def test_lessequal_operator_instantiation(instance):
    assert isinstance(instance, LessEqual_Operator)

@given(instance=iec61131_operators_LessEqual_Symbol_strategy)
@settings(max_examples=50)
def test_iec61131_operators_lessequal_symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_LessEqual_Symbol)

@given(instance=operators_LessEqual_Operator_strategy)
@settings(max_examples=50)
def test_operators_lessequal_operator_instantiation(instance):
    assert isinstance(instance, operators_LessEqual_Operator)

@given(instance=Less_Operator_strategy)
@settings(max_examples=50)
def test_less_operator_instantiation(instance):
    assert isinstance(instance, Less_Operator)

@given(instance=iec61131_operators_Less_Symbol_strategy)
@settings(max_examples=50)
def test_iec61131_operators_less_symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Less_Symbol)

@given(instance=operators_Less_Operator_strategy)
@settings(max_examples=50)
def test_operators_less_operator_instantiation(instance):
    assert isinstance(instance, operators_Less_Operator)

@given(instance=Unequal_Operator_strategy)
@settings(max_examples=50)
def test_unequal_operator_instantiation(instance):
    assert isinstance(instance, Unequal_Operator)

@given(instance=iec61131_operators_Unequal_Symbol_strategy)
@settings(max_examples=50)
def test_iec61131_operators_unequal_symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Unequal_Symbol)

@given(instance=operators_Unequal_Operator_strategy)
@settings(max_examples=50)
def test_operators_unequal_operator_instantiation(instance):
    assert isinstance(instance, operators_Unequal_Operator)

@given(instance=Equal_Operator_strategy)
@settings(max_examples=50)
def test_equal_operator_instantiation(instance):
    assert isinstance(instance, Equal_Operator)

@given(instance=iec61131_operators_Equal_Symbol_strategy)
@settings(max_examples=50)
def test_iec61131_operators_equal_symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Equal_Symbol)

@given(instance=operators_Comparison_Name_strategy)
@settings(max_examples=50)
def test_operators_comparison_name_instantiation(instance):
    assert isinstance(instance, operators_Comparison_Name)

@given(instance=iec61131_operators_Less_Name_strategy)
@settings(max_examples=50)
def test_iec61131_operators_less_name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Less_Name)

@given(instance=iec61131_operators_GreaterEqual_Name_strategy)
@settings(max_examples=50)
def test_iec61131_operators_greaterequal_name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_GreaterEqual_Name)

@given(instance=iec61131_operators_Greater_Name_strategy)
@settings(max_examples=50)
def test_iec61131_operators_greater_name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Greater_Name)

@given(instance=iec61131_operators_Unequal_Name_strategy)
@settings(max_examples=50)
def test_iec61131_operators_unequal_name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Unequal_Name)

@given(instance=iec61131_operators_LessEqual_Name_strategy)
@settings(max_examples=50)
def test_iec61131_operators_lessequal_name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_LessEqual_Name)

@given(instance=operators_Equal_Operator_strategy)
@settings(max_examples=50)
def test_operators_equal_operator_instantiation(instance):
    assert isinstance(instance, operators_Equal_Operator)

@given(instance=iec61131_operators_Equal_Name_strategy)
@settings(max_examples=50)
def test_iec61131_operators_equal_name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Equal_Name)

@given(instance=And_Operator_strategy)
@settings(max_examples=50)
def test_and_operator_instantiation(instance):
    assert isinstance(instance, And_Operator)

@given(instance=iec61131_operators_And_Name_strategy)
@settings(max_examples=50)
def test_iec61131_operators_and_name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_And_Name)

@given(instance=iec61131_operators_And_Symbol_strategy)
@settings(max_examples=50)
def test_iec61131_operators_and_symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_And_Symbol)

@given(instance=Assignment_Operator_strategy)
@settings(max_examples=50)
def test_assignment_operator_instantiation(instance):
    assert isinstance(instance, Assignment_Operator)

@given(instance=iec61131_operators_Assignment_Name_strategy)
@settings(max_examples=50)
def test_iec61131_operators_assignment_name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Assignment_Name)

@given(instance=iec61131_operators_Assignment_Symbol_strategy)
@settings(max_examples=50)
def test_iec61131_operators_assignment_symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Assignment_Symbol)

@given(instance=Power_Operator_strategy)
@settings(max_examples=50)
def test_power_operator_instantiation(instance):
    assert isinstance(instance, Power_Operator)

@given(instance=iec61131_operators_Power_Name_strategy)
@settings(max_examples=50)
def test_iec61131_operators_power_name_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Power_Name)

@given(instance=iec61131_operators_Power_Symbol_strategy)
@settings(max_examples=50)
def test_iec61131_operators_power_symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Power_Symbol)

@given(instance=Divide_Operator_strategy)
@settings(max_examples=50)
def test_divide_operator_instantiation(instance):
    assert isinstance(instance, Divide_Operator)

@given(instance=iec61131_operators_Divide_Symbol_strategy)
@settings(max_examples=50)
def test_iec61131_operators_divide_symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Divide_Symbol)

@given(instance=iec61131_literals_Integer_strategy)
@settings(max_examples=50)
def test_iec61131_literals_integer_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Integer)



@given(instance=iec61131_literals_Integer_strategy)
def test_iec61131_literals_integer_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=iec61131_literals_BSInteger_strategy)
@settings(max_examples=50)
def test_iec61131_literals_bsinteger_instantiation(instance):
    assert isinstance(instance, iec61131_literals_BSInteger)

@given(instance=iec61131_literals_Date_Literal_strategy)
@settings(max_examples=50)
def test_iec61131_literals_date_literal_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Date_Literal)



@given(instance=iec61131_literals_Date_Literal_strategy)
def test_iec61131_literals_date_literal_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=iec61131_literals_Date_Literal_strategy)
def test_iec61131_literals_date_literal_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original



@given(instance=iec61131_literals_Date_Literal_strategy)
def test_iec61131_literals_date_literal_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=iec61131_literals_Daytime_strategy)
@settings(max_examples=50)
def test_iec61131_literals_daytime_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Daytime)



@given(instance=iec61131_literals_Daytime_strategy)
def test_iec61131_literals_daytime_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original



@given(instance=iec61131_literals_Daytime_strategy)
def test_iec61131_literals_daytime_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original

@given(instance=iec61131_literals_Fixed_Point_Literal_strategy)
@settings(max_examples=50)
def test_iec61131_literals_fixed_point_literal_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Fixed_Point_Literal)

@given(instance=Double_Byte_Character_Representation_strategy)
@settings(max_examples=50)
def test_double_byte_character_representation_instantiation(instance):
    assert isinstance(instance, Double_Byte_Character_Representation)

@given(instance=operators_Dot_Operator_strategy)
@settings(max_examples=50)
def test_operators_dot_operator_instantiation(instance):
    assert isinstance(instance, operators_Dot_Operator)

@given(instance=il_Il_Simple_Operator_strategy)
@settings(max_examples=50)
def test_il_il_simple_operator_instantiation(instance):
    assert isinstance(instance, il_Il_Simple_Operator)

@given(instance=operators_Unary_Operator_strategy)
@settings(max_examples=50)
def test_operators_unary_operator_instantiation(instance):
    assert isinstance(instance, operators_Unary_Operator)

@given(instance=iec61131_operators_Substraction_Symbol_strategy)
@settings(max_examples=50)
def test_iec61131_operators_substraction_symbol_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Substraction_Symbol)

@given(instance=iec61131_operators_Not_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_operators_not_operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Not_Operator)

@given(instance=il_Il_Expr_Operator_strategy)
@settings(max_examples=50)
def test_il_il_expr_operator_instantiation(instance):
    assert isinstance(instance, il_Il_Expr_Operator)

@given(instance=iec61131_operators_Modulo_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_operators_modulo_operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Modulo_Operator)

@given(instance=operators_Operator_strategy)
@settings(max_examples=50)
def test_operators_operator_instantiation(instance):
    assert isinstance(instance, operators_Operator)

@given(instance=iec61131_operators_Xor_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_operators_xor_operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Xor_Operator)

@given(instance=iec61131_operators_Or_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_operators_or_operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Or_Operator)

@given(instance=iec61131_operators_And_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_operators_and_operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_And_Operator)

@given(instance=EquUequ_Operator_strategy)
@settings(max_examples=50)
def test_equuequ_operator_instantiation(instance):
    assert isinstance(instance, EquUequ_Operator)

@given(instance=iec61131_operators_Unequal_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_operators_unequal_operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Unequal_Operator)

@given(instance=iec61131_operators_Equal_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_operators_equal_operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Equal_Operator)

@given(instance=Dot_Operator_strategy)
@settings(max_examples=50)
def test_dot_operator_instantiation(instance):
    assert isinstance(instance, Dot_Operator)

@given(instance=iec61131_operators_Divide_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_operators_divide_operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Divide_Operator)

@given(instance=iec61131_operators_Multiply_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_operators_multiply_operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Multiply_Operator)

@given(instance=iec61131_operators_Substraction_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_operators_substraction_operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Substraction_Operator)

@given(instance=iec61131_operators_Addition_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_operators_addition_operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Addition_Operator)

@given(instance=Operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, Operator)

@given(instance=iec61131_operators_EquUequ_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_operators_equuequ_operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_EquUequ_Operator)

@given(instance=iec61131_operators_Assignment_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_operators_assignment_operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Assignment_Operator)

@given(instance=iec61131_operators_Dot_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_operators_dot_operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Dot_Operator)

@given(instance=iec61131_operators_Comparison_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_operators_comparison_operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Comparison_Operator)

@given(instance=iec61131_operators_Power_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_operators_power_operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Power_Operator)

@given(instance=iec61131_operators_Unary_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_operators_unary_operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Unary_Operator)

@given(instance=iec61131_operators_Add_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_operators_add_operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Add_Operator)

@given(instance=iec61131_operators_Operator_strategy)
@settings(max_examples=50)
def test_iec61131_operators_operator_instantiation(instance):
    assert isinstance(instance, iec61131_operators_Operator)

@given(instance=iec61131_literals_Double_Byte_Character_Representation_strategy)
@settings(max_examples=50)
def test_iec61131_literals_double_byte_character_representation_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Double_Byte_Character_Representation)



@given(instance=iec61131_literals_Double_Byte_Character_Representation_strategy)
def test_iec61131_literals_double_byte_character_representation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Common_Character_Representation_strategy)
@settings(max_examples=50)
def test_common_character_representation_instantiation(instance):
    assert isinstance(instance, Common_Character_Representation)

@given(instance=iec61131_literals_Single_Byte_Character_Representation_strategy)
@settings(max_examples=50)
def test_iec61131_literals_single_byte_character_representation_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Single_Byte_Character_Representation)



@given(instance=iec61131_literals_Single_Byte_Character_Representation_strategy)
def test_iec61131_literals_single_byte_character_representation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=iec61131_literals_Common_Character_Representation_strategy)
@settings(max_examples=50)
def test_iec61131_literals_common_character_representation_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Common_Character_Representation)



@given(instance=iec61131_literals_Common_Character_Representation_strategy)
def test_iec61131_literals_common_character_representation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DT_Type_Name_strategy)
@settings(max_examples=50)
def test_dt_type_name_instantiation(instance):
    assert isinstance(instance, DT_Type_Name)

@given(instance=Date_Literal_strategy)
@settings(max_examples=50)
def test_date_literal_instantiation(instance):
    assert isinstance(instance, Date_Literal)

@given(instance=Date_Type_Name_strategy)
@settings(max_examples=50)
def test_date_type_name_instantiation(instance):
    assert isinstance(instance, Date_Type_Name)

@given(instance=iec61131_types_TOD_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_tod_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_TOD_Type_Name)

@given(instance=iec61131_types_DT_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_dt_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_DT_Type_Name)

@given(instance=Single_Byte_Character_Representation_strategy)
@settings(max_examples=50)
def test_single_byte_character_representation_instantiation(instance):
    assert isinstance(instance, Single_Byte_Character_Representation)

@given(instance=Character_String_strategy)
@settings(max_examples=50)
def test_character_string_instantiation(instance):
    assert isinstance(instance, Character_String)

@given(instance=iec61131_literals_Double_Byte_Character_String_strategy)
@settings(max_examples=50)
def test_iec61131_literals_double_byte_character_string_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Double_Byte_Character_String)

@given(instance=iec61131_literals_Single_Byte_Character_String_strategy)
@settings(max_examples=50)
def test_iec61131_literals_single_byte_character_string_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Single_Byte_Character_String)

@given(instance=Milliseconds_strategy)
@settings(max_examples=50)
def test_milliseconds_instantiation(instance):
    assert isinstance(instance, Milliseconds)

@given(instance=Seconds_strategy)
@settings(max_examples=50)
def test_seconds_instantiation(instance):
    assert isinstance(instance, Seconds)

@given(instance=Minutes_strategy)
@settings(max_examples=50)
def test_minutes_instantiation(instance):
    assert isinstance(instance, Minutes)

@given(instance=Hours_strategy)
@settings(max_examples=50)
def test_hours_instantiation(instance):
    assert isinstance(instance, Hours)

@given(instance=Unsigned_Integer_strategy)
@settings(max_examples=50)
def test_unsigned_integer_instantiation(instance):
    assert isinstance(instance, Unsigned_Integer)

@given(instance=Fixed_Point_Literal_strategy)
@settings(max_examples=50)
def test_fixed_point_literal_instantiation(instance):
    assert isinstance(instance, Fixed_Point_Literal)

@given(instance=iec61131_literals_Fixed_Point_strategy)
@settings(max_examples=50)
def test_iec61131_literals_fixed_point_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Fixed_Point)



@given(instance=iec61131_literals_Fixed_Point_strategy)
def test_iec61131_literals_fixed_point_valuePre_setter(instance):
    original = instance.valuePre
    instance.valuePre = original
    assert instance.valuePre == original



@given(instance=iec61131_literals_Fixed_Point_strategy)
def test_iec61131_literals_fixed_point_valuePost_setter(instance):
    original = instance.valuePost
    instance.valuePost = original
    assert instance.valuePost == original

@given(instance=iec61131_literals_Interval_strategy)
@settings(max_examples=50)
def test_iec61131_literals_interval_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Interval)

@given(instance=literals_Fixed_Point_Literal_strategy)
@settings(max_examples=50)
def test_literals_fixed_point_literal_instantiation(instance):
    assert isinstance(instance, literals_Fixed_Point_Literal)

@given(instance=Integer_strategy)
@settings(max_examples=50)
def test_integer_instantiation(instance):
    assert isinstance(instance, Integer)

@given(instance=Numeric_Literal_strategy)
@settings(max_examples=50)
def test_numeric_literal_instantiation(instance):
    assert isinstance(instance, Numeric_Literal)

@given(instance=iec61131_literals_Integer_Literal_strategy)
@settings(max_examples=50)
def test_iec61131_literals_integer_literal_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Integer_Literal)

@given(instance=Bit_String_Type_Name_strategy)
@settings(max_examples=50)
def test_bit_string_type_name_instantiation(instance):
    assert isinstance(instance, Bit_String_Type_Name)

@given(instance=iec61131_types_Bool_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_bool_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Bool_Type_Name)

@given(instance=BSInteger_strategy)
@settings(max_examples=50)
def test_bsinteger_instantiation(instance):
    assert isinstance(instance, BSInteger)

@given(instance=Constant_strategy)
@settings(max_examples=50)
def test_constant_instantiation(instance):
    assert isinstance(instance, Constant)

@given(instance=iec61131_literals_Bit_String_Literal_strategy)
@settings(max_examples=50)
def test_iec61131_literals_bit_string_literal_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Bit_String_Literal)

@given(instance=iec61131_literals_Time_Literal_strategy)
@settings(max_examples=50)
def test_iec61131_literals_time_literal_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Time_Literal)

@given(instance=iec61131_literals_Character_String_strategy)
@settings(max_examples=50)
def test_iec61131_literals_character_string_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Character_String)

@given(instance=iec61131_literals_Numeric_Literal_strategy)
@settings(max_examples=50)
def test_iec61131_literals_numeric_literal_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Numeric_Literal)

@given(instance=TOD_Type_Name_strategy)
@settings(max_examples=50)
def test_tod_type_name_instantiation(instance):
    assert isinstance(instance, TOD_Type_Name)

@given(instance=Daytime_strategy)
@settings(max_examples=50)
def test_daytime_instantiation(instance):
    assert isinstance(instance, Daytime)

@given(instance=Time_Literal_strategy)
@settings(max_examples=50)
def test_time_literal_instantiation(instance):
    assert isinstance(instance, Time_Literal)

@given(instance=iec61131_literals_Date_And_Time_strategy)
@settings(max_examples=50)
def test_iec61131_literals_date_and_time_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Date_And_Time)

@given(instance=iec61131_literals_Date_strategy)
@settings(max_examples=50)
def test_iec61131_literals_date_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Date)

@given(instance=iec61131_literals_Time_Of_Day_strategy)
@settings(max_examples=50)
def test_iec61131_literals_time_of_day_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Time_Of_Day)

@given(instance=Substraction_Operator_strategy)
@settings(max_examples=50)
def test_substraction_operator_instantiation(instance):
    assert isinstance(instance, Substraction_Operator)

@given(instance=Duration_Type_Name_strategy)
@settings(max_examples=50)
def test_duration_type_name_instantiation(instance):
    assert isinstance(instance, Duration_Type_Name)

@given(instance=Interval_strategy)
@settings(max_examples=50)
def test_interval_instantiation(instance):
    assert isinstance(instance, Interval)

@given(instance=iec61131_literals_Days_strategy)
@settings(max_examples=50)
def test_iec61131_literals_days_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Days)

@given(instance=iec61131_literals_Minutes_strategy)
@settings(max_examples=50)
def test_iec61131_literals_minutes_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Minutes)

@given(instance=iec61131_literals_Hours_strategy)
@settings(max_examples=50)
def test_iec61131_literals_hours_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Hours)

@given(instance=iec61131_literals_Milliseconds_strategy)
@settings(max_examples=50)
def test_iec61131_literals_milliseconds_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Milliseconds)

@given(instance=iec61131_literals_Seconds_strategy)
@settings(max_examples=50)
def test_iec61131_literals_seconds_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Seconds)

@given(instance=sfc_Action_Time_strategy)
@settings(max_examples=50)
def test_sfc_action_time_instantiation(instance):
    assert isinstance(instance, sfc_Action_Time)

@given(instance=literals_Time_Literal_strategy)
@settings(max_examples=50)
def test_literals_time_literal_instantiation(instance):
    assert isinstance(instance, literals_Time_Literal)

@given(instance=iec61131_literals_Duration_strategy)
@settings(max_examples=50)
def test_iec61131_literals_duration_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Duration)

@given(instance=literals_BSInteger_strategy)
@settings(max_examples=50)
def test_literals_bsinteger_instantiation(instance):
    assert isinstance(instance, literals_BSInteger)

@given(instance=interfaces_Range_strategy)
@settings(max_examples=50)
def test_interfaces_range_instantiation(instance):
    assert isinstance(instance, interfaces_Range)

@given(instance=st_Case_List_Element_strategy)
@settings(max_examples=50)
def test_st_case_list_element_instantiation(instance):
    assert isinstance(instance, st_Case_List_Element)

@given(instance=literals_Integer_strategy)
@settings(max_examples=50)
def test_literals_integer_instantiation(instance):
    assert isinstance(instance, literals_Integer)

@given(instance=iec61131_literals_Unsigned_Integer_strategy)
@settings(max_examples=50)
def test_iec61131_literals_unsigned_integer_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Unsigned_Integer)

@given(instance=iec61131_literals_Hex_Integer_strategy)
@settings(max_examples=50)
def test_iec61131_literals_hex_integer_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Hex_Integer)

@given(instance=iec61131_literals_Octal_Integer_strategy)
@settings(max_examples=50)
def test_iec61131_literals_octal_integer_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Octal_Integer)

@given(instance=iec61131_literals_Binary_Integer_strategy)
@settings(max_examples=50)
def test_iec61131_literals_binary_integer_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Binary_Integer)

@given(instance=iec61131_literals_Signed_Integer_strategy)
@settings(max_examples=50)
def test_iec61131_literals_signed_integer_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Signed_Integer)



@given(instance=iec61131_literals_Signed_Integer_strategy)
def test_iec61131_literals_signed_integer_negative_setter(instance):
    original = instance.negative
    instance.negative = original
    assert instance.negative == original

@given(instance=il_Il_Operand_strategy)
@settings(max_examples=50)
def test_il_il_operand_instantiation(instance):
    assert isinstance(instance, il_Il_Operand)

@given(instance=configurations_Prog_Data_Source_strategy)
@settings(max_examples=50)
def test_configurations_prog_data_source_instantiation(instance):
    assert isinstance(instance, configurations_Prog_Data_Source)

@given(instance=configurations_Data_Source_strategy)
@settings(max_examples=50)
def test_configurations_data_source_instantiation(instance):
    assert isinstance(instance, configurations_Data_Source)

@given(instance=iec61131_configurations_Global_Var_Reference_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_global_var_reference_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Global_Var_Reference)

@given(instance=iec61131_variables_Direct_Variable_strategy)
@settings(max_examples=50)
def test_iec61131_variables_direct_variable_instantiation(instance):
    assert isinstance(instance, iec61131_variables_Direct_Variable)



@given(instance=iec61131_variables_Direct_Variable_strategy)
def test_iec61131_variables_direct_variable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=iec61131_literals_Constant_strategy)
@settings(max_examples=50)
def test_iec61131_literals_constant_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Constant)

@given(instance=iec61131_literals_Boolean_Literal_strategy)
@settings(max_examples=50)
def test_iec61131_literals_boolean_literal_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Boolean_Literal)



@given(instance=iec61131_literals_Boolean_Literal_strategy)
def test_iec61131_literals_boolean_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Fixed_Point_strategy)
@settings(max_examples=50)
def test_fixed_point_instantiation(instance):
    assert isinstance(instance, Fixed_Point)

@given(instance=Real_Type_Name_strategy)
@settings(max_examples=50)
def test_real_type_name_instantiation(instance):
    assert isinstance(instance, Real_Type_Name)

@given(instance=iec61131_literals_Real_Literal_strategy)
@settings(max_examples=50)
def test_iec61131_literals_real_literal_instantiation(instance):
    assert isinstance(instance, iec61131_literals_Real_Literal)



@given(instance=iec61131_literals_Real_Literal_strategy)
def test_iec61131_literals_real_literal_exponent_setter(instance):
    original = instance.exponent
    instance.exponent = original
    assert instance.exponent == original



@given(instance=iec61131_literals_Real_Literal_strategy)
def test_iec61131_literals_real_literal_negative_setter(instance):
    original = instance.negative
    instance.negative = original
    assert instance.negative == original

@given(instance=Integer_Type_Name_strategy)
@settings(max_examples=50)
def test_integer_type_name_instantiation(instance):
    assert isinstance(instance, Integer_Type_Name)

@given(instance=iec61131_types_Unsigned_Integer_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_unsigned_integer_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Unsigned_Integer_Type_Name)

@given(instance=iec61131_types_Signed_Integer_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_signed_integer_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Signed_Integer_Type_Name)

@given(instance=iec61131_NamedElement_strategy)
@settings(max_examples=50)
def test_iec61131_namedelement_instantiation(instance):
    assert isinstance(instance, iec61131_NamedElement)



@given(instance=iec61131_NamedElement_strategy)
def test_iec61131_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iec61131_Commentable_strategy)
@settings(max_examples=50)
def test_iec61131_commentable_instantiation(instance):
    assert isinstance(instance, iec61131_Commentable)



@given(instance=iec61131_Commentable_strategy)
def test_iec61131_commentable_comments_setter(instance):
    original = instance.comments
    instance.comments = original
    assert instance.comments == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=iec61131_sfc_Step_Name_strategy)
@settings(max_examples=50)
def test_iec61131_sfc_step_name_instantiation(instance):
    assert isinstance(instance, iec61131_sfc_Step_Name)

@given(instance=iec61131_variables_Variable_Name_strategy)
@settings(max_examples=50)
def test_iec61131_variables_variable_name_instantiation(instance):
    assert isinstance(instance, iec61131_variables_Variable_Name)

@given(instance=Commentable_strategy)
@settings(max_examples=50)
def test_commentable_instantiation(instance):
    assert isinstance(instance, Commentable)

@given(instance=iec61131_configurations_Program_Configuration_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_program_configuration_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Program_Configuration)



@given(instance=iec61131_configurations_Program_Configuration_strategy)
def test_iec61131_configurations_program_configuration_retain_setter(instance):
    original = instance.retain
    instance.retain = original
    assert instance.retain == original

@given(instance=iec61131_variables_Variable_strategy)
@settings(max_examples=50)
def test_iec61131_variables_variable_instantiation(instance):
    assert isinstance(instance, iec61131_variables_Variable)

@given(instance=iec61131_st_Statement_strategy)
@settings(max_examples=50)
def test_iec61131_st_statement_instantiation(instance):
    assert isinstance(instance, iec61131_st_Statement)

@given(instance=iec61131_st_Expression_Variable_strategy)
@settings(max_examples=50)
def test_iec61131_st_expression_variable_instantiation(instance):
    assert isinstance(instance, iec61131_st_Expression_Variable)

@given(instance=iec61131_st_Param_Assignment_strategy)
@settings(max_examples=50)
def test_iec61131_st_param_assignment_instantiation(instance):
    assert isinstance(instance, iec61131_st_Param_Assignment)

@given(instance=iec61131_st_Expression_Types_strategy)
@settings(max_examples=50)
def test_iec61131_st_expression_types_instantiation(instance):
    assert isinstance(instance, iec61131_st_Expression_Types)

@given(instance=iec61131_Library_Element_Name_strategy)
@settings(max_examples=50)
def test_iec61131_library_element_name_instantiation(instance):
    assert isinstance(instance, iec61131_Library_Element_Name)

@given(instance=iec61131_Library_Element_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_library_element_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_Library_Element_Declaration)

@given(instance=iec61131_IEC61131_strategy)
@settings(max_examples=50)
def test_iec61131_iec61131_instantiation(instance):
    assert isinstance(instance, iec61131_IEC61131)

@given(instance=iec61131_interfaces_Input_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_input_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Input_Declaration)

@given(instance=iec61131_interfaces_Global_Var_Spec_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_global_var_spec_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Global_Var_Spec)

@given(instance=iec61131_interfaces_Global_Var_Decl_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_global_var_decl_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Global_Var_Decl)

@given(instance=External_Specification_strategy)
@settings(max_examples=50)
def test_external_specification_instantiation(instance):
    assert isinstance(instance, External_Specification)

@given(instance=Global_Var_Name_strategy)
@settings(max_examples=50)
def test_global_var_name_instantiation(instance):
    assert isinstance(instance, Global_Var_Name)

@given(instance=iec61131_interfaces_External_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_external_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_External_Declaration)

@given(instance=iec61131_interfaces_Interface_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_interface_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Interface)

@given(instance=RNV_Declarations_strategy)
@settings(max_examples=50)
def test_rnv_declarations_instantiation(instance):
    assert isinstance(instance, RNV_Declarations)

@given(instance=iec61131_interfaces_Non_Retentive_Var_Declarations_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_non_retentive_var_declarations_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Non_Retentive_Var_Declarations)

@given(instance=iec61131_interfaces_Retentive_Var_Declarations_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_retentive_var_declarations_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Retentive_Var_Declarations)

@given(instance=External_Declaration_strategy)
@settings(max_examples=50)
def test_external_declaration_instantiation(instance):
    assert isinstance(instance, External_Declaration)

@given(instance=Other_Var_Declaration_strategy)
@settings(max_examples=50)
def test_other_var_declaration_instantiation(instance):
    assert isinstance(instance, Other_Var_Declaration)

@given(instance=iec61131_interfaces_External_Var_Declarations_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_external_var_declarations_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_External_Var_Declarations)



@given(instance=iec61131_interfaces_External_Var_Declarations_strategy)
def test_iec61131_interfaces_external_var_declarations_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=Variable_Name_strategy)
@settings(max_examples=50)
def test_variable_name_instantiation(instance):
    assert isinstance(instance, Variable_Name)

@given(instance=Location_strategy)
@settings(max_examples=50)
def test_location_instantiation(instance):
    assert isinstance(instance, Location)

@given(instance=iec61131_interfaces_Located_Var_Decl_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_located_var_decl_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Located_Var_Decl)

@given(instance=Direct_Variable_strategy)
@settings(max_examples=50)
def test_direct_variable_instantiation(instance):
    assert isinstance(instance, Direct_Variable)

@given(instance=iec61131_interfaces_Location_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_location_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Location)

@given(instance=iec61131_interfaces_Located_Var_Spec_Init_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_located_var_spec_init_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Located_Var_Spec_Init)

@given(instance=iec61131_interfaces_External_Specification_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_external_specification_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_External_Specification)

@given(instance=iec61131_interfaces_Var_Spec_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_var_spec_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Var_Spec)

@given(instance=iec61131_interfaces_Incompl_Location_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_incompl_location_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Incompl_Location)



@given(instance=iec61131_interfaces_Incompl_Location_strategy)
def test_iec61131_interfaces_incompl_location_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=Var_Spec_strategy)
@settings(max_examples=50)
def test_var_spec_instantiation(instance):
    assert isinstance(instance, Var_Spec)

@given(instance=iec61131_interfaces_Byte_String_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_byte_string_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Byte_String)

@given(instance=Incompl_Location_strategy)
@settings(max_examples=50)
def test_incompl_location_instantiation(instance):
    assert isinstance(instance, Incompl_Location)

@given(instance=iec61131_interfaces_Incompl_Located_Var_Decl_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_incompl_located_var_decl_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Incompl_Located_Var_Decl)

@given(instance=iec61131_interfaces_RNV_Declarations_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_rnv_declarations_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_RNV_Declarations)

@given(instance=Incompl_Located_Var_Decl_strategy)
@settings(max_examples=50)
def test_incompl_located_var_decl_instantiation(instance):
    assert isinstance(instance, Incompl_Located_Var_Decl)

@given(instance=iec61131_interfaces_Incompl_Located_Var_Declarations_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_incompl_located_var_declarations_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Incompl_Located_Var_Declarations)



@given(instance=iec61131_interfaces_Incompl_Located_Var_Declarations_strategy)
def test_iec61131_interfaces_incompl_located_var_declarations_retain_setter(instance):
    original = instance.retain
    instance.retain = original
    assert instance.retain == original

@given(instance=iec61131_interfaces_Var_Declarations_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_var_declarations_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Var_Declarations)



@given(instance=iec61131_interfaces_Var_Declarations_strategy)
def test_iec61131_interfaces_var_declarations_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=Temp_Var_Decl_strategy)
@settings(max_examples=50)
def test_temp_var_decl_instantiation(instance):
    assert isinstance(instance, Temp_Var_Decl)

@given(instance=iec61131_interfaces_Temp_Var_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_temp_var_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Temp_Var_Declaration)

@given(instance=iec61131_interfaces_Temp_Var_Decls_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_temp_var_decls_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Temp_Var_Decls)

@given(instance=Global_Var_Spec_strategy)
@settings(max_examples=50)
def test_global_var_spec_instantiation(instance):
    assert isinstance(instance, Global_Var_Spec)

@given(instance=iec61131_interfaces_Global_Var_Location_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_global_var_location_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Global_Var_Location)

@given(instance=iec61131_interfaces_Global_Var_List_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_global_var_list_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Global_Var_List)

@given(instance=Library_Element_Name_strategy)
@settings(max_examples=50)
def test_library_element_name_instantiation(instance):
    assert isinstance(instance, Library_Element_Name)

@given(instance=iec61131_pous_Program_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_pous_program_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Program_Type_Name)

@given(instance=iec61131_types_Data_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_data_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Data_Type_Name)

@given(instance=iec61131_configurations_Configuration_Name_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_configuration_name_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Configuration_Name)

@given(instance=iec61131_pous_Function_Name_strategy)
@settings(max_examples=50)
def test_iec61131_pous_function_name_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Function_Name)

@given(instance=iec61131_configurations_Resource_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_configurations_resource_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_configurations_Resource_Type_Name)

@given(instance=iec61131_interfaces_Global_Var_Name_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_global_var_name_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Global_Var_Name)

@given(instance=iec61131_interfaces_Specification_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_specification_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Specification)

@given(instance=Specification_strategy)
@settings(max_examples=50)
def test_specification_instantiation(instance):
    assert isinstance(instance, Specification)

@given(instance=Array_Initial_Elements_strategy)
@settings(max_examples=50)
def test_array_initial_elements_instantiation(instance):
    assert isinstance(instance, Array_Initial_Elements)

@given(instance=iec61131_interfaces_Array_Initial_Elements1_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_array_initial_elements1_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Array_Initial_Elements1)

@given(instance=iec61131_interfaces_Array_Initial_Elements2_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_array_initial_elements2_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Array_Initial_Elements2)

@given(instance=iec61131_interfaces_Array_Initialization_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_array_initialization_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Array_Initialization)

@given(instance=iec61131_interfaces_Var1_List_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_var1_list_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Var1_List)

@given(instance=Double_BString_strategy)
@settings(max_examples=50)
def test_double_bstring_instantiation(instance):
    assert isinstance(instance, Double_BString)

@given(instance=Double_Byte_Character_String_strategy)
@settings(max_examples=50)
def test_double_byte_character_string_instantiation(instance):
    assert isinstance(instance, Double_Byte_Character_String)

@given(instance=Single_BString_strategy)
@settings(max_examples=50)
def test_single_bstring_instantiation(instance):
    assert isinstance(instance, Single_BString)

@given(instance=Single_Byte_Character_String_strategy)
@settings(max_examples=50)
def test_single_byte_character_string_instantiation(instance):
    assert isinstance(instance, Single_Byte_Character_String)

@given(instance=Located_Var_Spec_Init_strategy)
@settings(max_examples=50)
def test_located_var_spec_init_instantiation(instance):
    assert isinstance(instance, Located_Var_Spec_Init)

@given(instance=iec61131_interfaces_Double_Byte_String_Spec_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_double_byte_string_spec_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Double_Byte_String_Spec)

@given(instance=iec61131_interfaces_Single_Byte_String_Spec_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_single_byte_string_spec_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Single_Byte_String_Spec)

@given(instance=Double_Byte_String_Spec_strategy)
@settings(max_examples=50)
def test_double_byte_string_spec_instantiation(instance):
    assert isinstance(instance, Double_Byte_String_Spec)

@given(instance=Single_Byte_String_Spec_strategy)
@settings(max_examples=50)
def test_single_byte_string_spec_instantiation(instance):
    assert isinstance(instance, Single_Byte_String_Spec)

@given(instance=String_Var_Declaration_strategy)
@settings(max_examples=50)
def test_string_var_declaration_instantiation(instance):
    assert isinstance(instance, String_Var_Declaration)

@given(instance=iec61131_interfaces_Double_Byte_String_Var_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_double_byte_string_var_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Double_Byte_String_Var_Declaration)

@given(instance=iec61131_interfaces_Single_Byte_String_Var_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_single_byte_string_var_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Single_Byte_String_Var_Declaration)

@given(instance=Range_strategy)
@settings(max_examples=50)
def test_range_instantiation(instance):
    assert isinstance(instance, Range)

@given(instance=Case_List_Element_strategy)
@settings(max_examples=50)
def test_case_list_element_instantiation(instance):
    assert isinstance(instance, Case_List_Element)

@given(instance=iec61131_interfaces_Subrange_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_subrange_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Subrange)



@given(instance=iec61131_interfaces_Subrange_strategy)
def test_iec61131_interfaces_subrange_delimiter_setter(instance):
    original = instance.delimiter
    instance.delimiter = original
    assert instance.delimiter == original

@given(instance=iec61131_interfaces_Array_Initial_Elements_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_array_initial_elements_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Array_Initial_Elements)

@given(instance=interfaces_Var_Spec_strategy)
@settings(max_examples=50)
def test_interfaces_var_spec_instantiation(instance):
    assert isinstance(instance, interfaces_Var_Spec)

@given(instance=interfaces_External_Specification_strategy)
@settings(max_examples=50)
def test_interfaces_external_specification_instantiation(instance):
    assert isinstance(instance, interfaces_External_Specification)

@given(instance=iec61131_pous_Function_Block_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_pous_function_block_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_pous_Function_Block_Type_Name)

@given(instance=iec61131_interfaces_Array_Specification_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_array_specification_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Array_Specification)

@given(instance=iec61131_types_Structure_Type_Name_strategy)
@settings(max_examples=50)
def test_iec61131_types_structure_type_name_instantiation(instance):
    assert isinstance(instance, iec61131_types_Structure_Type_Name)

@given(instance=interfaces_Specification_strategy)
@settings(max_examples=50)
def test_interfaces_specification_instantiation(instance):
    assert isinstance(instance, interfaces_Specification)

@given(instance=iec61131_interfaces_Enumerated_Specification_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_enumerated_specification_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Enumerated_Specification)

@given(instance=iec61131_interfaces_Subrange_Specification_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_subrange_specification_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Subrange_Specification)

@given(instance=interfaces_Var2_Init_Decl_strategy)
@settings(max_examples=50)
def test_interfaces_var2_init_decl_instantiation(instance):
    assert isinstance(instance, interfaces_Var2_Init_Decl)

@given(instance=interfaces_Temp_Var_Decl_strategy)
@settings(max_examples=50)
def test_interfaces_temp_var_decl_instantiation(instance):
    assert isinstance(instance, interfaces_Temp_Var_Decl)

@given(instance=iec61131_interfaces_String_Var_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_string_var_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_String_Var_Declaration)

@given(instance=Function_Block_Type_Name_strategy)
@settings(max_examples=50)
def test_function_block_type_name_instantiation(instance):
    assert isinstance(instance, Function_Block_Type_Name)

@given(instance=Structure_Initialization_strategy)
@settings(max_examples=50)
def test_structure_initialization_instantiation(instance):
    assert isinstance(instance, Structure_Initialization)

@given(instance=Temp_Var_Declaration_strategy)
@settings(max_examples=50)
def test_temp_var_declaration_instantiation(instance):
    assert isinstance(instance, Temp_Var_Declaration)

@given(instance=iec61131_interfaces_Var1_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_var1_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Var1_Declaration)

@given(instance=iec61131_interfaces_Structured_Var_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_structured_var_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Structured_Var_Declaration)

@given(instance=iec61131_interfaces_Array_Var_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_array_var_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Array_Var_Declaration)

@given(instance=iec61131_interfaces_Fb_Name_Decl_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_fb_name_decl_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Fb_Name_Decl)

@given(instance=Enumerated_Type_Name_strategy)
@settings(max_examples=50)
def test_enumerated_type_name_instantiation(instance):
    assert isinstance(instance, Enumerated_Type_Name)

@given(instance=iec61131_interfaces_Enumerated_Value_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_enumerated_value_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Enumerated_Value)



@given(instance=iec61131_interfaces_Enumerated_Value_strategy)
def test_iec61131_interfaces_enumerated_value_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iec61131_interfaces_Structure_Element_Name_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_structure_element_name_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Structure_Element_Name)



@given(instance=iec61131_interfaces_Structure_Element_Name_strategy)
def test_iec61131_interfaces_structure_element_name_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Initial_Element_strategy)
@settings(max_examples=50)
def test_initial_element_instantiation(instance):
    assert isinstance(instance, Initial_Element)

@given(instance=iec61131_interfaces_InitElement_Constant_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_initelement_constant_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_InitElement_Constant)

@given(instance=iec61131_interfaces_InitElement_Array_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_initelement_array_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_InitElement_Array)

@given(instance=iec61131_interfaces_InitElement_EnumValue_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_initelement_enumvalue_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_InitElement_EnumValue)

@given(instance=iec61131_interfaces_InitElement_Structure_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_initelement_structure_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_InitElement_Structure)

@given(instance=Structure_Element_Name_strategy)
@settings(max_examples=50)
def test_structure_element_name_instantiation(instance):
    assert isinstance(instance, Structure_Element_Name)

@given(instance=iec61131_interfaces_Structure_Element_Initialization_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_structure_element_initialization_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Structure_Element_Initialization)

@given(instance=Structure_Element_Initialization_strategy)
@settings(max_examples=50)
def test_structure_element_initialization_instantiation(instance):
    assert isinstance(instance, Structure_Element_Initialization)

@given(instance=iec61131_interfaces_Structure_Initialization_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_structure_initialization_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Structure_Initialization)

@given(instance=iec61131_interfaces_Var_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_var_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Var_Declaration)

@given(instance=Structure_Type_Name_strategy)
@settings(max_examples=50)
def test_structure_type_name_instantiation(instance):
    assert isinstance(instance, Structure_Type_Name)

@given(instance=pous_Structure_Specification_strategy)
@settings(max_examples=50)
def test_pous_structure_specification_instantiation(instance):
    assert isinstance(instance, pous_Structure_Specification)

@given(instance=iec61131_interfaces_Initialized_Structure_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_initialized_structure_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Initialized_Structure)

@given(instance=Array_Specification_strategy)
@settings(max_examples=50)
def test_array_specification_instantiation(instance):
    assert isinstance(instance, Array_Specification)

@given(instance=iec61131_interfaces_Array_Specification1_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_array_specification1_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Array_Specification1)

@given(instance=iec61131_interfaces_Array_Specification2_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_array_specification2_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Array_Specification2)

@given(instance=Array_Initialization_strategy)
@settings(max_examples=50)
def test_array_initialization_instantiation(instance):
    assert isinstance(instance, Array_Initialization)

@given(instance=iec61131_interfaces_Array_Spec_Init_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_array_spec_init_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Array_Spec_Init)

@given(instance=Var_Declaration_strategy)
@settings(max_examples=50)
def test_var_declaration_instantiation(instance):
    assert isinstance(instance, Var_Declaration)

@given(instance=iec61131_interfaces_Temp_Var_Decl_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_temp_var_decl_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Temp_Var_Decl)

@given(instance=Var1_Specification_strategy)
@settings(max_examples=50)
def test_var1_specification_instantiation(instance):
    assert isinstance(instance, Var1_Specification)

@given(instance=iec61131_interfaces_Var1_Specification_Func_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_var1_specification_func_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Var1_Specification_Func)

@given(instance=Var_Init_Decl_strategy)
@settings(max_examples=50)
def test_var_init_decl_instantiation(instance):
    assert isinstance(instance, Var_Init_Decl)

@given(instance=iec61131_interfaces_Var2_Init_Decl_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_var2_init_decl_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Var2_Init_Decl)

@given(instance=iec61131_interfaces_Var1_Init_Decl_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_var1_init_decl_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Var1_Init_Decl)

@given(instance=Var1_List_strategy)
@settings(max_examples=50)
def test_var1_list_instantiation(instance):
    assert isinstance(instance, Var1_List)

@given(instance=Input_Declaration_strategy)
@settings(max_examples=50)
def test_input_declaration_instantiation(instance):
    assert isinstance(instance, Input_Declaration)

@given(instance=iec61131_interfaces_Var_Init_Decl_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_var_init_decl_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Var_Init_Decl)

@given(instance=iec61131_interfaces_Edge_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_edge_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Edge_Declaration)



@given(instance=iec61131_interfaces_Edge_Declaration_strategy)
def test_iec61131_interfaces_edge_declaration_edge_setter(instance):
    original = instance.edge
    instance.edge = original
    assert instance.edge == original

@given(instance=Io_Var_Declaration_strategy)
@settings(max_examples=50)
def test_io_var_declaration_instantiation(instance):
    assert isinstance(instance, Io_Var_Declaration)

@given(instance=iec61131_interfaces_Input_Output_Declarations_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_input_output_declarations_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Input_Output_Declarations)

@given(instance=iec61131_interfaces_Output_Declarations_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_output_declarations_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Output_Declarations)



@given(instance=iec61131_interfaces_Output_Declarations_strategy)
def test_iec61131_interfaces_output_declarations_retain_setter(instance):
    original = instance.retain
    instance.retain = original
    assert instance.retain == original

@given(instance=iec61131_interfaces_Input_Declarations_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_input_declarations_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Input_Declarations)



@given(instance=iec61131_interfaces_Input_Declarations_strategy)
def test_iec61131_interfaces_input_declarations_retain_setter(instance):
    original = instance.retain
    instance.retain = original
    assert instance.retain == original

@given(instance=pous_Function_Vars_strategy)
@settings(max_examples=50)
def test_pous_function_vars_instantiation(instance):
    assert isinstance(instance, pous_Function_Vars)

@given(instance=pous_Program_Vars_strategy)
@settings(max_examples=50)
def test_pous_program_vars_instantiation(instance):
    assert isinstance(instance, pous_Program_Vars)

@given(instance=pous_Function_Block_Vars_strategy)
@settings(max_examples=50)
def test_pous_function_block_vars_instantiation(instance):
    assert isinstance(instance, pous_Function_Block_Vars)

@given(instance=interfaces_Interface_strategy)
@settings(max_examples=50)
def test_interfaces_interface_instantiation(instance):
    assert isinstance(instance, interfaces_Interface)

@given(instance=iec61131_interfaces_Function_Var_Decl_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_function_var_decl_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Function_Var_Decl)



@given(instance=iec61131_interfaces_Function_Var_Decl_strategy)
def test_iec61131_interfaces_function_var_decl_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=iec61131_interfaces_Io_Var_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_io_var_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Io_Var_Declaration)

@given(instance=iec61131_interfaces_Other_Var_Declaration_strategy)
@settings(max_examples=50)
def test_iec61131_interfaces_other_var_declaration_instantiation(instance):
    assert isinstance(instance, iec61131_interfaces_Other_Var_Declaration)
