from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Edge(Enum):
    R_EDGE = "R_EDGE"
    F_EDGE = "F_EDGE"
class Direction(Enum):
    READ_WRITE = "READ_WRITE"
    READ_ONLY = "READ_ONLY"


############################################
# Definition of Classes
############################################

class Single_Element_Type_Name:

    pass
class iec61131_types_Enumerated_Type_Name(Single_Element_Type_Name):

    pass
class iec61131_types_Subrange_Type_Name(Single_Element_Type_Name):

    pass
class types_Single_Element_Type_Name:

    pass
class types_Derived_Type_Name:

    pass
class Derived_Type_Name:

    pass
class iec61131_types_Array_Type_Name(Derived_Type_Name):

    pass
class iec61131_types_String_Type_Name(Derived_Type_Name):

    pass
class iec61131_types_Single_Element_Type_Name(Derived_Type_Name):

    pass
class pous_Function_Return_Value:

    pass
class types_Data_Type_Name:

    pass
class iec61131_types_Non_Generic_Type_Name(types_Data_Type_Name, pous_Function_Return_Value):

    pass
class interfaces_Simple_Specification_Func:

    pass
class types_Non_Generic_Type_Name:

    pass
class Numeric_Type_Name:

    pass
class iec61131_types_Real_Type_Name(Numeric_Type_Name):

    pass
class iec61131_types_Integer_Type_Name(Numeric_Type_Name):

    pass
class Elementary_Type_Name:

    pass
class iec61131_types_Byte_String_Type_Name(Elementary_Type_Name):

    pass
class iec61131_types_Duration_Type_Name(Elementary_Type_Name):

    pass
class iec61131_types_Numeric_Type_Name(Elementary_Type_Name):

    pass
class Data_Type_Name:

    pass
class iec61131_types_Simple_Specification(Data_Type_Name):

    pass
class iec61131_types_TypeLib:

    pass
class Fbd_Network:

    pass
class iec61131_variables_Subscript_List:

    pass
class Input_Reference:

    pass
class Output_Reference:

    pass
class variables_Symbolic_Variable:

    pass
class variables_Variable:

    pass
class iec61131_types_Bit_String_Type_Name(Elementary_Type_Name):

    pass
class iec61131_types_Date_Type_Name(Elementary_Type_Name):

    pass
class Subscript_List:

    pass
class Multi_Element_Variable:

    pass
class iec61131_variables_Structured_Variable(Multi_Element_Variable):

    pass
class iec61131_variables_Array_Variable(Multi_Element_Variable):

    pass
class iec61131_sfc_Cond2_Condition(ABC):

    pass
class iec61131_sfc_Transition_Condition(ABC):

    pass
class iec61131_sfc_Steps(ABC):

    pass
class iec61131_sfc_Transition_Name:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class iec61131_sfc_Action_Time(ABC):

    pass
class iec61131_sfc_Timed_Qualifier:

    def __init__(self, qualifier: str):
        self.qualifier = qualifier
        
    @property
    def qualifier(self) -> str:
        return self.__qualifier

    @qualifier.setter
    def qualifier(self, qualifier: str):
        self.__qualifier = qualifier

class Action_Time:

    pass
class iec61131_sfc_ActionTime2(Action_Time):

    pass
class Timed_Qualifier:

    pass
class iec61131_sfc_Action_Qualifier:

    def __init__(self, qualifier: str, iec61131_sfc_Action_Qualifier: "Timed_Qualifier" = None, iec61131_sfc_Action_Qualifier653: "Action_Time" = None):
        self.qualifier = qualifier
        self.iec61131_sfc_Action_Qualifier = iec61131_sfc_Action_Qualifier
        self.iec61131_sfc_Action_Qualifier653 = iec61131_sfc_Action_Qualifier653
        
    @property
    def qualifier(self) -> str:
        return self.__qualifier

    @qualifier.setter
    def qualifier(self, qualifier: str):
        self.__qualifier = qualifier

    @property
    def iec61131_sfc_Action_Qualifier(self):
        return self.__iec61131_sfc_Action_Qualifier

    @iec61131_sfc_Action_Qualifier.setter
    def iec61131_sfc_Action_Qualifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_sfc_Action_Qualifier__iec61131_sfc_Action_Qualifier", None)
        self.__iec61131_sfc_Action_Qualifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Timed_Qualifier"):
                opp_val = getattr(old_value, "Timed_Qualifier", None)
                if opp_val == self:
                    setattr(old_value, "Timed_Qualifier", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Timed_Qualifier"):
                opp_val = getattr(value, "Timed_Qualifier", None)
                setattr(value, "Timed_Qualifier", self)

    @property
    def iec61131_sfc_Action_Qualifier653(self):
        return self.__iec61131_sfc_Action_Qualifier653

    @iec61131_sfc_Action_Qualifier653.setter
    def iec61131_sfc_Action_Qualifier653(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_sfc_Action_Qualifier__iec61131_sfc_Action_Qualifier653", None)
        self.__iec61131_sfc_Action_Qualifier653 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Action_Time"):
                opp_val = getattr(old_value, "Action_Time", None)
                if opp_val == self:
                    setattr(old_value, "Action_Time", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Action_Time"):
                opp_val = getattr(value, "Action_Time", None)
                setattr(value, "Action_Time", self)

class iec61131_sfc_Action_Name:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Cond2_Condition:

    pass
class iec61131_fbd_Fbd_Network(Cond2_Condition):

    pass
class iec61131_ld_Rung(Cond2_Condition):

    pass
class Action_Qualifier:

    pass
class iec61131_sfc_Action_Association:

    pass
class iec61131_sfc_Sfc_Elements(ABC):

    pass
class Action_Name:

    pass
class Transition_Condition:

    pass
class iec61131_sfc_Transition_Cond3(Transition_Condition):

    pass
class iec61131_sfc_Transition_Cond2(Transition_Condition):

    pass
class iec61131_sfc_Transition_Cond1(Transition_Condition):

    pass
class Steps:

    pass
class iec61131_sfc_Steps1(Steps):

    pass
class iec61131_sfc_Steps2(Steps):

    pass
class Transition_Name:

    pass
class sfc_Step_Types:

    pass
class sfc_Sfc_Elements:

    pass
class iec61131_sfc_Step(sfc_Sfc_Elements, sfc_Step_Types):

    pass
class Step_Types:

    pass
class iec61131_sfc_Initial_Step(Step_Types):

    pass
class Sfc_Elements:

    pass
class iec61131_sfc_Action(Sfc_Elements):

    pass
class iec61131_sfc_Transition(Sfc_Elements):

    pass
class Step_Name:

    pass
class Action_Association:

    pass
class iec61131_sfc_Step_Types(ABC):

    pass
class iec61131_il_Il_Assign_Out_Operator:

    pass
class iec61131_il_Param_Assignment(ABC):

    pass
class Assignment_Name:

    pass
class iec61131_il_Il_Assign_Operator:

    pass
class iec61131_il_Param_Instruction(ABC):

    pass
class iec61131_il_Param_Assignments(ABC):

    pass
class Il_Assign_Out_Operator:

    pass
class Initial_Step:

    pass
class iec61131_sfc_Sfc_Network:

    pass
class Sfc_Network:

    pass
class Il_Assign_Operator:

    pass
class Param_Assignments:

    pass
class iec61131_il_Il_Param_Out_Assignment(Param_Assignments):

    pass
class iec61131_il_Il_Param_Assignment(Param_Assignments):

    pass
class Param_Instruction:

    pass
class iec61131_il_Il_Param_Last_Instruction(Param_Instruction):

    pass
class iec61131_il_Il_Param_Instruction(Param_Instruction):

    pass
class iec61131_il_Simple_Instr(ABC):

    pass
class Simple_Instr:

    pass
class iec61131_il_Il_Simple_Instruction:

    pass
class iec61131_il_Operands(ABC):

    pass
class Il_Param_Last_Instruction:

    pass
class Il_Param_Instruction:

    pass
class iec61131_il_Il_Param_List:

    pass
class iec61131_il_Il_Call_Operator:

    pass
class iec61131_il_Il_Jump_Operator:

    pass
class Il_Operand_List:

    pass
class Il_Simple_Operator:

    pass
class iec61131_il_Il_Expr_Operator(Il_Simple_Operator):

    pass
class Il_Simple_Operation:

    pass
class iec61131_il_Simple_Operation2(Il_Simple_Operation):

    pass
class iec61131_il_Simple_Operation1(Il_Simple_Operation):

    pass
class iec61131_il_Il_Operand_List:

    pass
class iec61131_il_Il_Simple_Operator:

    pass
class iec61131_il_Il_Operations(ABC):

    pass
class Il_Param_List:

    pass
class Operands:

    pass
class iec61131_il_Operand2(Operands):

    pass
class iec61131_il_Operand1(Operands):

    pass
class Il_Call_Operator:

    pass
class Il_Jump_Operator:

    pass
class Simple_Instr_List:

    pass
class Il_Operand:

    pass
class il_Simple_Instr:

    pass
class il_Il_Operations:

    pass
class iec61131_il_Il_Expression(il_Simple_Instr, il_Il_Operations):

    pass
class iec61131_il_Il_Simple_Operation(il_Simple_Instr, il_Il_Operations):

    pass
class iec61131_il_Label:

    def __init__(self, label: str):
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

class Il_Operations:

    pass
class iec61131_il_Il_Jump_Operation(Il_Operations):

    pass
class iec61131_il_Il_Fb_Call(Il_Operations):

    pass
class iec61131_il_Il_Return_Operator(Il_Operations):

    pass
class Label:

    pass
class iec61131_il_Il_Instruction:

    pass
class Il_Simple_Instruction:

    pass
class iec61131_il_Simple_Instr_List:

    pass
class iec61131_il_Il_Formal_Funct_Call(il_Simple_Instr, il_Il_Operations):

    pass
class Structured_Variable:

    pass
class Array_Variable:

    pass
class Function_Name:

    pass
class Primary_Expression:

    pass
class iec61131_st_Expression_Constant(Primary_Expression):

    pass
class iec61131_st_Expression_Variable_Type(Primary_Expression):

    pass
class iec61131_st_Call_Expression(Primary_Expression):

    pass
class iec61131_st_Expression_EnumValue(Primary_Expression):

    pass
class iec61131_st_Bracket_Expression(Primary_Expression):

    pass
class Il_Instruction:

    pass
class Unary_Operator:

    pass
class Power_Symbol:

    pass
class Add_Operator:

    pass
class Xor_Operator:

    pass
class iec61131_st_For_List:

    pass
class iec61131_st_Control_Variable:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class For_List:

    pass
class Control_Variable:

    pass
class Iteration_Statement:

    pass
class iec61131_st_Exit_Statement(Iteration_Statement):

    pass
class iec61131_st_Repeat_Statement(Iteration_Statement):

    pass
class iec61131_st_For_Statement(Iteration_Statement):

    pass
class iec61131_st_Case_List_Element(ABC):

    pass
class iec61131_st_Case_List:

    pass
class Case_List:

    pass
class iec61131_st_Case_Element:

    pass
class iec61131_st_Else_Statement:

    pass
class iec61131_st_Else_If_Statement:

    pass
class Case_Element:

    pass
class iec61131_st_While_Statement(Iteration_Statement):

    pass
class Else_If_Statement:

    pass
class Statement_List:

    pass
class Selection_Statement:

    pass
class iec61131_st_If_Statement(Selection_Statement):

    pass
class Not_Operator:

    pass
class Variable:

    pass
class iec61131_variables_Symbolic_Variable(Variable):

    pass
class Param_Assignment:

    pass
class iec61131_il_Il_Operand(Param_Assignment):

    pass
class iec61131_il_Param_Assignment2(Param_Assignment):

    pass
class iec61131_st_Param_Type2(Param_Assignment):

    pass
class iec61131_st_Param_Type1(Param_Assignment):

    pass
class Subprogram_Control_Statement:

    pass
class iec61131_st_Fb_Invocation(Subprogram_Control_Statement):

    pass
class iec61131_st_Return_Statement(Subprogram_Control_Statement):

    pass
class iec61131_st_Case_Statement(Selection_Statement):

    pass
class Else_Statement:

    pass
class Expression_Variable:

    pass
class Or_Operator:

    pass
class Expression_Types:

    pass
class iec61131_st_Unary_Expression(Expression_Types):

    pass
class iec61131_st_Power_Expression(Expression_Types):

    pass
class iec61131_st_And_Expression(Expression_Types):

    pass
class iec61131_st_Term_Expression(Expression_Types):

    pass
class iec61131_st_Comparison(Expression_Types):

    pass
class iec61131_st_Primary_Expression(Expression_Types):

    pass
class iec61131_st_Xor_Expression(Expression_Types):

    pass
class iec61131_st_Equ_Expression(Expression_Types):

    pass
class iec61131_st_Add_Expression(Expression_Types):

    pass
class iec61131_st_Expression(Expression_Types):

    pass
class Statement:

    pass
class iec61131_st_Assignment_Statement(Statement):

    pass
class iec61131_st_Iteration_Statement(Statement):

    pass
class Task_Initialization:

    pass
class iec61131_configurations_Priority(Task_Initialization):

    pass
class iec61131_configurations_Interval(Task_Initialization):

    pass
class iec61131_configurations_Single(Task_Initialization):

    pass
class iec61131_st_Selection_Statement(Statement):

    pass
class iec61131_st_Subprogram_Control_Statement(Statement):

    pass
class iec61131_configurations_Instance_Specific_Init(ABC):

    pass
class iec61131_configurations_Data_Sink(ABC):

    pass
class Prog_Data_Source:

    pass
class Data_Sink:

    pass
class Prog_Cnxn:

    pass
class iec61131_configurations_Prog_Source(Prog_Cnxn):

    pass
class iec61131_configurations_Prog_Sink(Prog_Cnxn):

    pass
class iec61131_configurations_Prog_Data_Source(ABC):

    pass
class iec61131_configurations_Prog_Conf_Element(ABC):

    pass
class Prog_Conf_Element:

    pass
class iec61131_configurations_Fb_Task(Prog_Conf_Element):

    pass
class iec61131_configurations_Prog_Conf_Elements:

    pass
class iec61131_configurations_Task_Initialization(ABC):

    pass
class iec61131_configurations_Task_Name:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class iec61131_configurations_Program_Name:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class iec61131_configurations_Access_Path(ABC):

    pass
class iec61131_configurations_Prog_Cnxn(Prog_Conf_Element):

    pass
class Access_Path:

    pass
class iec61131_configurations_Symbolic_Path(Access_Path):

    pass
class iec61131_configurations_Direct_Path(Access_Path):

    pass
class iec61131_configurations_Access_Declaration:

    def __init__(self, direction: str, iec61131_configurations_Access_Declaration: "Access_Name" = None, iec61131_configurations_Access_Declaration337: "Access_Path" = None, iec61131_configurations_Access_Declaration339: "Non_Generic_Type_Name" = None):
        self.direction = direction
        self.iec61131_configurations_Access_Declaration = iec61131_configurations_Access_Declaration
        self.iec61131_configurations_Access_Declaration337 = iec61131_configurations_Access_Declaration337
        self.iec61131_configurations_Access_Declaration339 = iec61131_configurations_Access_Declaration339
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def iec61131_configurations_Access_Declaration339(self):
        return self.__iec61131_configurations_Access_Declaration339

    @iec61131_configurations_Access_Declaration339.setter
    def iec61131_configurations_Access_Declaration339(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_configurations_Access_Declaration__iec61131_configurations_Access_Declaration339", None)
        self.__iec61131_configurations_Access_Declaration339 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Non_Generic_Type_Name340"):
                opp_val = getattr(old_value, "Non_Generic_Type_Name340", None)
                if opp_val == self:
                    setattr(old_value, "Non_Generic_Type_Name340", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Non_Generic_Type_Name340"):
                opp_val = getattr(value, "Non_Generic_Type_Name340", None)
                setattr(value, "Non_Generic_Type_Name340", self)

    @property
    def iec61131_configurations_Access_Declaration(self):
        return self.__iec61131_configurations_Access_Declaration

    @iec61131_configurations_Access_Declaration.setter
    def iec61131_configurations_Access_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_configurations_Access_Declaration__iec61131_configurations_Access_Declaration", None)
        self.__iec61131_configurations_Access_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Access_Name335"):
                opp_val = getattr(old_value, "Access_Name335", None)
                if opp_val == self:
                    setattr(old_value, "Access_Name335", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Access_Name335"):
                opp_val = getattr(value, "Access_Name335", None)
                setattr(value, "Access_Name335", self)

    @property
    def iec61131_configurations_Access_Declaration337(self):
        return self.__iec61131_configurations_Access_Declaration337

    @iec61131_configurations_Access_Declaration337.setter
    def iec61131_configurations_Access_Declaration337(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_configurations_Access_Declaration__iec61131_configurations_Access_Declaration337", None)
        self.__iec61131_configurations_Access_Declaration337 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Access_Path"):
                opp_val = getattr(old_value, "Access_Path", None)
                if opp_val == self:
                    setattr(old_value, "Access_Path", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Access_Path"):
                opp_val = getattr(value, "Access_Path", None)
                setattr(value, "Access_Path", self)

class Access_Declaration:

    pass
class iec61131_configurations_Access_Declarations:

    pass
class Data_Source:

    pass
class iec61131_configurations_Program_Output_Reference(Data_Source):

    pass
class configurations_Data_Sink:

    pass
class iec61131_configurations_Data_Source(ABC):

    pass
class Instance_Specific_Init:

    pass
class iec61131_configurations_Instance_Spec2(Instance_Specific_Init):

    pass
class iec61131_configurations_Instance_Spec1(Instance_Specific_Init):

    pass
class iec61131_configurations_Instance_Specific_Initializations:

    pass
class Prog_Conf_Elements:

    pass
class iec61131_configurations_Access_Name:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Program_Name:

    pass
class Single:

    pass
class Priority:

    pass
class Task_Name:

    pass
class iec61131_configurations_Task_Configuration:

    pass
class Program_Configuration:

    pass
class Task_Configuration:

    pass
class iec61131_configurations_Single_Resource_Declaration:

    pass
class Resource_Type_Name:

    pass
class iec61131_configurations_Resource_Name:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Resource_Declaration:

    pass
class Access_Declarations:

    pass
class Instance_Specific_Initializations:

    pass
class Global_Var_Declarations:

    pass
class Single_Resource_Declaration:

    pass
class Configuration_Name:

    pass
class Function_Block_Declaration:

    pass
class Resource_Name:

    pass
class iec61131_pous_Function_Block_Vars(ABC):

    pass
class iec61131_pous_Function_Vars(ABC):

    pass
class iec61131_pous_Program_Vars(ABC):

    pass
class iec61131_pous_Structure_Elements(ABC):

    pass
class Structure_Elements:

    pass
class iec61131_pous_Structure_Element_Declaration:

    pass
class Structure_Element_Declaration:

    pass
class iec61131_pous_Structure_Specification(ABC):

    pass
class Enumerated_Spec_Init:

    pass
class Subrange_Spec_Init:

    pass
class Simple_Type_Name:

    pass
class Single_Element_Type_Declaration:

    pass
class iec61131_pous_Subrange_Type_Declaration(Single_Element_Type_Declaration):

    pass
class iec61131_pous_Enumerated_Type_Declaration(Single_Element_Type_Declaration):

    pass
class iec61131_pous_Simple_Type_Declaration(Single_Element_Type_Declaration):

    pass
class Function_Declaration:

    pass
class Program_Declaration:

    pass
class iec61131_pous_Library:

    pass
class Program_Access_Decl:

    pass
class Byte_String_Type_Name:

    pass
class iec61131_types_Double_Byte_String_Type_Name(Byte_String_Type_Name):

    pass
class iec61131_types_Single_Byte_String_Type_Name(Byte_String_Type_Name):

    pass
class String_Type_Name:

    pass
class Structure_Specification:

    pass
class iec61131_pous_Structure_Declaration(Structure_Specification):

    pass
class iec61131_pous_Type_Declaration(ABC):

    pass
class Type_Declaration:

    pass
class iec61131_pous_Structure_Type_Declaration(Type_Declaration):

    pass
class iec61131_pous_String_Type_Declaration(Type_Declaration):

    pass
class iec61131_pous_Array_Type_Declaration(Type_Declaration):

    pass
class iec61131_pous_Single_Element_Type_Declaration(Type_Declaration):

    pass
class Symbolic_Variable:

    pass
class iec61131_variables_Multi_Element_Variable(Symbolic_Variable):

    pass
class Access_Name:

    pass
class iec61131_pous_Program_Access_Decl:

    def __init__(self, direction: str, iec61131_pous_Program_Access_Decl: "Access_Name" = None, iec61131_pous_Program_Access_Decl232: "Non_Generic_Type_Name" = None, iec61131_pous_Program_Access_Decl235: "Symbolic_Variable" = None):
        self.direction = direction
        self.iec61131_pous_Program_Access_Decl = iec61131_pous_Program_Access_Decl
        self.iec61131_pous_Program_Access_Decl232 = iec61131_pous_Program_Access_Decl232
        self.iec61131_pous_Program_Access_Decl235 = iec61131_pous_Program_Access_Decl235
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def iec61131_pous_Program_Access_Decl232(self):
        return self.__iec61131_pous_Program_Access_Decl232

    @iec61131_pous_Program_Access_Decl232.setter
    def iec61131_pous_Program_Access_Decl232(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_pous_Program_Access_Decl__iec61131_pous_Program_Access_Decl232", None)
        self.__iec61131_pous_Program_Access_Decl232 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Non_Generic_Type_Name233"):
                opp_val = getattr(old_value, "Non_Generic_Type_Name233", None)
                if opp_val == self:
                    setattr(old_value, "Non_Generic_Type_Name233", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Non_Generic_Type_Name233"):
                opp_val = getattr(value, "Non_Generic_Type_Name233", None)
                setattr(value, "Non_Generic_Type_Name233", self)

    @property
    def iec61131_pous_Program_Access_Decl235(self):
        return self.__iec61131_pous_Program_Access_Decl235

    @iec61131_pous_Program_Access_Decl235.setter
    def iec61131_pous_Program_Access_Decl235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_pous_Program_Access_Decl__iec61131_pous_Program_Access_Decl235", None)
        self.__iec61131_pous_Program_Access_Decl235 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Symbolic_Variable"):
                opp_val = getattr(old_value, "Symbolic_Variable", None)
                if opp_val == self:
                    setattr(old_value, "Symbolic_Variable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Symbolic_Variable"):
                opp_val = getattr(value, "Symbolic_Variable", None)
                setattr(value, "Symbolic_Variable", self)

    @property
    def iec61131_pous_Program_Access_Decl(self):
        return self.__iec61131_pous_Program_Access_Decl

    @iec61131_pous_Program_Access_Decl.setter
    def iec61131_pous_Program_Access_Decl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_pous_Program_Access_Decl__iec61131_pous_Program_Access_Decl", None)
        self.__iec61131_pous_Program_Access_Decl = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Access_Name"):
                opp_val = getattr(old_value, "Access_Name", None)
                if opp_val == self:
                    setattr(old_value, "Access_Name", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Access_Name"):
                opp_val = getattr(value, "Access_Name", None)
                setattr(value, "Access_Name", self)

class iec61131_pous_Function_Block_Body(ABC):

    pass
class pous_Function_Block_Body:

    pass
class pous_Function_Body:

    pass
class iec61131_il_Instruction_List(pous_Function_Body, pous_Function_Block_Body):

    pass
class iec61131_fbd_Function_Block_Diagram(pous_Function_Body, pous_Function_Block_Body):

    pass
class iec61131_ld_Ladder_Diagram(pous_Function_Body, pous_Function_Block_Body):

    pass
class iec61131_st_Statement_List(pous_Function_Body, pous_Function_Block_Body):

    pass
class iec61131_pous_Other_Language(pous_Function_Body, pous_Function_Block_Body):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class iec61131_pous_Function_Body(ABC):

    pass
class iec61131_pous_Function_Return_Value(ABC):

    pass
class pous_Function_Name:

    pass
class iec61131_pous_Access_Name:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Function_Body:

    pass
class Function_Vars:

    pass
class Function_Return_Value:

    pass
class Derived_Function_Name:

    pass
class Function_Block_Vars:

    pass
class Derived_Function_Block_Name:

    pass
class types_Simple_Specification:

    pass
class iec61131_types_Simple_Type_Name(types_Simple_Specification, types_Single_Element_Type_Name, interfaces_Simple_Specification_Func):

    pass
class iec61131_types_Generic_Type_Name(types_Data_Type_Name, types_Simple_Specification, pous_Function_Return_Value):

    pass
class iec61131_types_Elementary_Type_Name(interfaces_Simple_Specification_Func, types_Simple_Specification, types_Non_Generic_Type_Name):

    pass
class Blocks:

    pass
class iec61131_pous_Derived_Function_Name(Blocks, pous_Function_Name):

    pass
class Function_Block_Body:

    pass
class iec61131_sfc_Sequential_Function_Chart(Function_Block_Body):

    pass
class Program_Type_Name:

    pass
class pous_Function_Block_Type_Name:

    pass
class iec61131_pous_Derived_Function_Block_Name(Blocks, pous_Function_Block_Type_Name):

    pass
class Simple_Specification_Func:

    pass
class Var1_Specification_Func:

    pass
class iec61131_interfaces_Simple_Spec_Init_Func(Var1_Specification_Func):

    pass
class Simple_Spec_Init:

    pass
class iec61131_interfaces_Var_Name_Decl(Simple_Spec_Init):

    pass
class iec61131_interfaces_Simple_Specification_Func(ABC):

    pass
class iec61131_interfaces_Initial_Element(ABC):

    pass
class Non_Generic_Type_Name:

    pass
class iec61131_types_Derived_Type_Name(Non_Generic_Type_Name):

    pass
class Array_Type_Name:

    pass
class Subrange_Type_Name:

    pass
class Subrange:

    pass
class Double_Byte_String_Type_Name:

    pass
class Single_Byte_String_Type_Name:

    pass
class Byte_String:

    pass
class iec61131_interfaces_Double_BString(Byte_String):

    pass
class iec61131_interfaces_Single_BString(Byte_String):

    pass
class iec61131_interfaces_Range(ABC):

    pass
class iec61131_interfaces_Input_Declaration(ABC):

    pass
class iec61131_interfaces_Global_Var_Spec(ABC):

    pass
class Global_Var_Decl:

    pass
class Library_Element_Declaration:

    pass
class iec61131_pous_Function_Block_Declaration(Library_Element_Declaration):

    pass
class iec61131_pous_Function_Declaration(Library_Element_Declaration):

    pass
class iec61131_pous_Program_Declaration(Library_Element_Declaration):

    pass
class iec61131_pous_Data_Type_Declaration(Library_Element_Declaration):

    pass
class iec61131_configurations_Resource_Declaration(Library_Element_Declaration):

    pass
class iec61131_configurations_Configuration_Declaration(Library_Element_Declaration):

    pass
class iec61131_interfaces_Global_Var_Declarations(Library_Element_Declaration):

    def __init__(self, constant: bool, retain: bool, iec61131_interfaces_Global_Var_Declarations: set["Global_Var_Decl"] = None):
        self.constant = constant
        self.retain = retain
        self.iec61131_interfaces_Global_Var_Declarations = iec61131_interfaces_Global_Var_Declarations if iec61131_interfaces_Global_Var_Declarations is not None else set()
        
    @property
    def retain(self) -> bool:
        return self.__retain

    @retain.setter
    def retain(self, retain: bool):
        self.__retain = retain

    @property
    def constant(self) -> bool:
        return self.__constant

    @constant.setter
    def constant(self, constant: bool):
        self.__constant = constant

    @property
    def iec61131_interfaces_Global_Var_Declarations(self):
        return self.__iec61131_interfaces_Global_Var_Declarations

    @iec61131_interfaces_Global_Var_Declarations.setter
    def iec61131_interfaces_Global_Var_Declarations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_interfaces_Global_Var_Declarations__iec61131_interfaces_Global_Var_Declarations", None)
        self.__iec61131_interfaces_Global_Var_Declarations = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Global_Var_Decl"):
                    opp_val = getattr(item, "Global_Var_Decl", None)
                    
                    if opp_val == self:
                        setattr(item, "Global_Var_Decl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Global_Var_Decl"):
                    opp_val = getattr(item, "Global_Var_Decl", None)
                    
                    setattr(item, "Global_Var_Decl", self)
                    

class Program_Vars:

    pass
class iec61131_pous_Program_Access_Decls(Program_Vars):

    pass
class iec61131_interfaces_Located_Var_Declarations(Program_Vars):

    def __init__(self, constant: bool, retain: bool, iec61131_interfaces_Located_Var_Declarations: set["Located_Var_Decl"] = None, Program_Vars: "iec61131_pous_Program_Declaration"):
        self.constant = constant
        self.retain = retain
        self.iec61131_interfaces_Located_Var_Declarations = iec61131_interfaces_Located_Var_Declarations if iec61131_interfaces_Located_Var_Declarations is not None else set()
        
    @property
    def constant(self) -> bool:
        return self.__constant

    @constant.setter
    def constant(self, constant: bool):
        self.__constant = constant

    @property
    def retain(self) -> bool:
        return self.__retain

    @retain.setter
    def retain(self, retain: bool):
        self.__retain = retain

    @property
    def iec61131_interfaces_Located_Var_Declarations(self):
        return self.__iec61131_interfaces_Located_Var_Declarations

    @iec61131_interfaces_Located_Var_Declarations.setter
    def iec61131_interfaces_Located_Var_Declarations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_interfaces_Located_Var_Declarations__iec61131_interfaces_Located_Var_Declarations", None)
        self.__iec61131_interfaces_Located_Var_Declarations = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Located_Var_Decl"):
                    opp_val = getattr(item, "Located_Var_Decl", None)
                    
                    if opp_val == self:
                        setattr(item, "Located_Var_Decl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Located_Var_Decl"):
                    opp_val = getattr(item, "Located_Var_Decl", None)
                    
                    setattr(item, "Located_Var_Decl", self)
                    

class Location:

    pass
class iec61131_interfaces_Located_Var_Decl:

    pass
class Direct_Variable:

    pass
class iec61131_interfaces_Location:

    pass
class iec61131_interfaces_Located_Var_Spec_Init(ABC):

    pass
class iec61131_interfaces_External_Specification(ABC):

    pass
class iec61131_interfaces_Var_Spec(ABC):

    pass
class Located_Var_Decl:

    pass
class Var_Spec:

    pass
class iec61131_interfaces_Byte_String(Var_Spec):

    pass
class Incompl_Location:

    pass
class iec61131_interfaces_Incompl_Located_Var_Decl:

    pass
class Incompl_Located_Var_Decl:

    pass
class iec61131_interfaces_Incompl_Location:

    def __init__(self, location: str):
        self.location = location
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

class Temp_Var_Decl:

    pass
class iec61131_interfaces_Temp_Var_Declaration(Temp_Var_Decl):

    pass
class Global_Var_Spec:

    pass
class iec61131_interfaces_Global_Var_Location(Global_Var_Spec):

    pass
class iec61131_interfaces_Global_Var_List(Global_Var_Spec):

    pass
class Library_Element_Name:

    pass
class iec61131_configurations_Configuration_Name(Library_Element_Name):

    pass
class iec61131_configurations_Resource_Type_Name(Library_Element_Name):

    pass
class iec61131_pous_Program_Type_Name(Blocks, Library_Element_Name):

    pass
class iec61131_pous_Function_Name(Library_Element_Name):

    pass
class iec61131_types_Data_Type_Name(Library_Element_Name):

    pass
class External_Specification:

    pass
class Global_Var_Name:

    pass
class iec61131_interfaces_External_Declaration:

    pass
class RNV_Declarations:

    pass
class iec61131_interfaces_Non_Retentive_Var_Declarations(RNV_Declarations):

    pass
class iec61131_interfaces_Var_Declarations(RNV_Declarations):

    def __init__(self, constant: bool):
        self.constant = constant
        
    @property
    def constant(self) -> bool:
        return self.__constant

    @constant.setter
    def constant(self, constant: bool):
        self.__constant = constant

class iec61131_interfaces_Retentive_Var_Declarations(RNV_Declarations):

    pass
class External_Declaration:

    pass
class Other_Var_Declaration:

    pass
class iec61131_interfaces_RNV_Declarations(Other_Var_Declaration):

    pass
class iec61131_interfaces_Incompl_Located_Var_Declarations(Other_Var_Declaration):

    def __init__(self, retain: bool, iec61131_interfaces_Incompl_Located_Var_Declarations: set["Incompl_Located_Var_Decl"] = None):
        self.retain = retain
        self.iec61131_interfaces_Incompl_Located_Var_Declarations = iec61131_interfaces_Incompl_Located_Var_Declarations if iec61131_interfaces_Incompl_Located_Var_Declarations is not None else set()
        
    @property
    def retain(self) -> bool:
        return self.__retain

    @retain.setter
    def retain(self, retain: bool):
        self.__retain = retain

    @property
    def iec61131_interfaces_Incompl_Located_Var_Declarations(self):
        return self.__iec61131_interfaces_Incompl_Located_Var_Declarations

    @iec61131_interfaces_Incompl_Located_Var_Declarations.setter
    def iec61131_interfaces_Incompl_Located_Var_Declarations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_interfaces_Incompl_Located_Var_Declarations__iec61131_interfaces_Incompl_Located_Var_Declarations", None)
        self.__iec61131_interfaces_Incompl_Located_Var_Declarations = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Incompl_Located_Var_Decl"):
                    opp_val = getattr(item, "Incompl_Located_Var_Decl", None)
                    
                    if opp_val == self:
                        setattr(item, "Incompl_Located_Var_Decl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Incompl_Located_Var_Decl"):
                    opp_val = getattr(item, "Incompl_Located_Var_Decl", None)
                    
                    setattr(item, "Incompl_Located_Var_Decl", self)
                    

class iec61131_interfaces_Temp_Var_Decls(Other_Var_Declaration):

    pass
class iec61131_interfaces_External_Var_Declarations(Other_Var_Declaration):

    def __init__(self, constant: bool, iec61131_interfaces_External_Var_Declarations: set["External_Declaration"] = None):
        self.constant = constant
        self.iec61131_interfaces_External_Var_Declarations = iec61131_interfaces_External_Var_Declarations if iec61131_interfaces_External_Var_Declarations is not None else set()
        
    @property
    def constant(self) -> bool:
        return self.__constant

    @constant.setter
    def constant(self, constant: bool):
        self.__constant = constant

    @property
    def iec61131_interfaces_External_Var_Declarations(self):
        return self.__iec61131_interfaces_External_Var_Declarations

    @iec61131_interfaces_External_Var_Declarations.setter
    def iec61131_interfaces_External_Var_Declarations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_interfaces_External_Var_Declarations__iec61131_interfaces_External_Var_Declarations", None)
        self.__iec61131_interfaces_External_Var_Declarations = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "External_Declaration"):
                    opp_val = getattr(item, "External_Declaration", None)
                    
                    if opp_val == self:
                        setattr(item, "External_Declaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "External_Declaration"):
                    opp_val = getattr(item, "External_Declaration", None)
                    
                    setattr(item, "External_Declaration", self)
                    

class Variable_Name:

    pass
class iec61131_interfaces_Var1_List:

    pass
class Double_BString:

    pass
class Single_BString:

    pass
class Single_Byte_Character_String:

    pass
class Located_Var_Spec_Init:

    pass
class iec61131_interfaces_Single_Byte_String_Spec(Located_Var_Spec_Init):

    pass
class Double_Byte_String_Spec:

    pass
class Case_List_Element:

    pass
class iec61131_interfaces_Subrange(Case_List_Element):

    def __init__(self, delimiter: str, iec61131_interfaces_Subrange: set["Range"] = None, Case_List_Element: "iec61131_st_Case_List"):
        self.delimiter = delimiter
        self.iec61131_interfaces_Subrange = iec61131_interfaces_Subrange if iec61131_interfaces_Subrange is not None else set()
        
    @property
    def delimiter(self) -> str:
        return self.__delimiter

    @delimiter.setter
    def delimiter(self, delimiter: str):
        self.__delimiter = delimiter

    @property
    def iec61131_interfaces_Subrange(self):
        return self.__iec61131_interfaces_Subrange

    @iec61131_interfaces_Subrange.setter
    def iec61131_interfaces_Subrange(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_interfaces_Subrange__iec61131_interfaces_Subrange", None)
        self.__iec61131_interfaces_Subrange = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Range"):
                    opp_val = getattr(item, "Range", None)
                    
                    if opp_val == self:
                        setattr(item, "Range", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Range"):
                    opp_val = getattr(item, "Range", None)
                    
                    setattr(item, "Range", self)
                    

class iec61131_interfaces_Array_Initial_Elements(ABC):

    pass
class Single_Byte_String_Spec:

    pass
class String_Var_Declaration:

    pass
class iec61131_interfaces_Double_Byte_String_Var_Declaration(String_Var_Declaration):

    pass
class iec61131_interfaces_Single_Byte_String_Var_Declaration(String_Var_Declaration):

    pass
class Double_Byte_Character_String:

    pass
class interfaces_Var_Spec:

    pass
class iec61131_interfaces_Double_Byte_String_Spec(Located_Var_Spec_Init):

    pass
class Range:

    pass
class Specification:

    pass
class interfaces_External_Specification:

    pass
class iec61131_types_Structure_Type_Name(types_Derived_Type_Name, interfaces_Var_Spec, interfaces_External_Specification):

    pass
class iec61131_interfaces_Array_Specification(interfaces_Var_Spec, interfaces_External_Specification):

    pass
class interfaces_Specification:

    pass
class iec61131_interfaces_Enumerated_Specification(interfaces_Var_Spec, interfaces_Specification, interfaces_External_Specification):

    pass
class iec61131_interfaces_Subrange_Specification(interfaces_Var_Spec, interfaces_Specification, interfaces_External_Specification):

    pass
class iec61131_interfaces_Specification(ABC):

    pass
class Structure_Element_Name:

    pass
class iec61131_interfaces_Structure_Element_Initialization:

    pass
class Structure_Element_Initialization:

    pass
class iec61131_interfaces_Structure_Initialization:

    pass
class iec61131_interfaces_Var_Declaration(ABC):

    pass
class Array_Initial_Elements:

    pass
class iec61131_interfaces_Array_Initial_Elements2(Array_Initial_Elements):

    pass
class iec61131_interfaces_Array_Initial_Elements1(Array_Initial_Elements):

    pass
class iec61131_interfaces_Array_Initialization:

    pass
class Enumerated_Type_Name:

    pass
class iec61131_interfaces_Structure_Element_Name:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Initial_Element:

    pass
class iec61131_interfaces_InitElement_Array(Initial_Element):

    pass
class iec61131_interfaces_InitElement_EnumValue(Initial_Element):

    pass
class iec61131_interfaces_InitElement_Structure(Initial_Element):

    pass
class iec61131_interfaces_InitElement_Constant(Initial_Element):

    pass
class Var_Declaration:

    pass
class iec61131_interfaces_Temp_Var_Decl(Var_Declaration):

    pass
class Structure_Type_Name:

    pass
class pous_Structure_Specification:

    pass
class Array_Specification:

    pass
class iec61131_interfaces_Array_Specification1(Array_Specification):

    pass
class iec61131_interfaces_Array_Specification2(Array_Specification):

    pass
class Array_Initialization:

    pass
class Initialized_Structure:

    pass
class Array_Spec_Init:

    pass
class Var2_Init_Decl:

    pass
class iec61131_interfaces_Structured_Var_Init_Decl(Var2_Init_Decl):

    pass
class iec61131_interfaces_Var_Init_Decl_Func(Var2_Init_Decl):

    pass
class iec61131_interfaces_Array_Var_Init_Decl(Var2_Init_Decl):

    pass
class Enumerated_Value:

    pass
class interfaces_Var2_Init_Decl:

    pass
class interfaces_Temp_Var_Decl:

    pass
class iec61131_interfaces_String_Var_Declaration(interfaces_Var2_Init_Decl, interfaces_Temp_Var_Decl):

    pass
class Function_Block_Type_Name:

    pass
class Structure_Initialization:

    pass
class Temp_Var_Declaration:

    pass
class iec61131_interfaces_Var1_Declaration(Temp_Var_Declaration):

    pass
class iec61131_interfaces_Array_Var_Declaration(Temp_Var_Declaration):

    pass
class iec61131_interfaces_Structured_Var_Declaration(Temp_Var_Declaration):

    pass
class iec61131_interfaces_Fb_Name_Decl(Temp_Var_Declaration):

    pass
class Simple_Specification:

    pass
class pous_Structure_Elements:

    pass
class interfaces_Located_Var_Spec_Init:

    pass
class iec61131_interfaces_Array_Spec_Init(pous_Structure_Elements, interfaces_Located_Var_Spec_Init):

    pass
class iec61131_interfaces_Initialized_Structure(pous_Structure_Elements, pous_Structure_Specification, interfaces_Located_Var_Spec_Init):

    pass
class interfaces_Var1_Specification:

    pass
class iec61131_interfaces_Simple_Spec_Init(pous_Structure_Elements, interfaces_Var1_Specification, interfaces_Located_Var_Spec_Init):

    pass
class Assignment_Symbol:

    pass
class iec61131_interfaces_Var1_Specification(ABC):

    pass
class Bool_Type_Name:

    pass
class Enumerated_Specification:

    pass
class iec61131_interfaces_Enumerated_Specification1(Enumerated_Specification):

    pass
class iec61131_interfaces_Enumerated_Specification2(Enumerated_Specification):

    pass
class Signed_Integer:

    pass
class Subrange_Specification:

    pass
class iec61131_interfaces_Subrange_Specification2(Subrange_Specification):

    pass
class iec61131_interfaces_Subrange_Specification1(Subrange_Specification):

    pass
class interfaces_Var1_Specification_Func:

    pass
class iec61131_interfaces_Enumerated_Spec_Init(pous_Structure_Elements, interfaces_Var1_Specification, interfaces_Var1_Specification_Func, interfaces_Located_Var_Spec_Init):

    pass
class iec61131_interfaces_Subrange_Spec_Init(pous_Structure_Elements, interfaces_Var1_Specification, interfaces_Var1_Specification_Func, interfaces_Located_Var_Spec_Init):

    pass
class Input_Declaration:

    pass
class Io_Var_Declaration:

    pass
class iec61131_interfaces_Input_Output_Declarations(Io_Var_Declaration):

    pass
class iec61131_interfaces_Output_Declarations(Io_Var_Declaration):

    def __init__(self, retain: bool, iec61131_interfaces_Output_Declarations: set["Var_Init_Decl"] = None):
        self.retain = retain
        self.iec61131_interfaces_Output_Declarations = iec61131_interfaces_Output_Declarations if iec61131_interfaces_Output_Declarations is not None else set()
        
    @property
    def retain(self) -> bool:
        return self.__retain

    @retain.setter
    def retain(self, retain: bool):
        self.__retain = retain

    @property
    def iec61131_interfaces_Output_Declarations(self):
        return self.__iec61131_interfaces_Output_Declarations

    @iec61131_interfaces_Output_Declarations.setter
    def iec61131_interfaces_Output_Declarations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_interfaces_Output_Declarations__iec61131_interfaces_Output_Declarations", None)
        self.__iec61131_interfaces_Output_Declarations = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Var_Init_Decl"):
                    opp_val = getattr(item, "Var_Init_Decl", None)
                    
                    if opp_val == self:
                        setattr(item, "Var_Init_Decl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Var_Init_Decl"):
                    opp_val = getattr(item, "Var_Init_Decl", None)
                    
                    setattr(item, "Var_Init_Decl", self)
                    

class iec61131_interfaces_Input_Declarations(Io_Var_Declaration):

    def __init__(self, retain: bool, iec61131_interfaces_Input_Declarations: set["Input_Declaration"] = None):
        self.retain = retain
        self.iec61131_interfaces_Input_Declarations = iec61131_interfaces_Input_Declarations if iec61131_interfaces_Input_Declarations is not None else set()
        
    @property
    def retain(self) -> bool:
        return self.__retain

    @retain.setter
    def retain(self, retain: bool):
        self.__retain = retain

    @property
    def iec61131_interfaces_Input_Declarations(self):
        return self.__iec61131_interfaces_Input_Declarations

    @iec61131_interfaces_Input_Declarations.setter
    def iec61131_interfaces_Input_Declarations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_interfaces_Input_Declarations__iec61131_interfaces_Input_Declarations", None)
        self.__iec61131_interfaces_Input_Declarations = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Input_Declaration"):
                    opp_val = getattr(item, "Input_Declaration", None)
                    
                    if opp_val == self:
                        setattr(item, "Input_Declaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Input_Declaration"):
                    opp_val = getattr(item, "Input_Declaration", None)
                    
                    setattr(item, "Input_Declaration", self)
                    

class pous_Function_Vars:

    pass
class pous_Program_Vars:

    pass
class pous_Function_Block_Vars:

    pass
class interfaces_Interface:

    pass
class iec61131_interfaces_Function_Var_Decl(interfaces_Interface, pous_Function_Vars):

    def __init__(self, constant: bool, iec61131_interfaces_Function_Var_Decl: set["Var2_Init_Decl"] = None):
        self.constant = constant
        self.iec61131_interfaces_Function_Var_Decl = iec61131_interfaces_Function_Var_Decl if iec61131_interfaces_Function_Var_Decl is not None else set()
        
    @property
    def constant(self) -> bool:
        return self.__constant

    @constant.setter
    def constant(self, constant: bool):
        self.__constant = constant

    @property
    def iec61131_interfaces_Function_Var_Decl(self):
        return self.__iec61131_interfaces_Function_Var_Decl

    @iec61131_interfaces_Function_Var_Decl.setter
    def iec61131_interfaces_Function_Var_Decl(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_interfaces_Function_Var_Decl__iec61131_interfaces_Function_Var_Decl", None)
        self.__iec61131_interfaces_Function_Var_Decl = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Var2_Init_Decl"):
                    opp_val = getattr(item, "Var2_Init_Decl", None)
                    
                    if opp_val == self:
                        setattr(item, "Var2_Init_Decl", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Var2_Init_Decl"):
                    opp_val = getattr(item, "Var2_Init_Decl", None)
                    
                    setattr(item, "Var2_Init_Decl", self)
                    

class iec61131_interfaces_Other_Var_Declaration(pous_Function_Block_Vars, pous_Program_Vars, interfaces_Interface):

    pass
class iec61131_interfaces_Io_Var_Declaration(pous_Program_Vars, pous_Function_Block_Vars, interfaces_Interface, pous_Function_Vars):

    pass
class iec61131_interfaces_Edge_Declaration(Input_Declaration):

    def __init__(self, edge: str, iec61131_interfaces_Edge_Declaration: "Var1_List" = None, iec61131_interfaces_Edge_Declaration59: "Bool_Type_Name" = None, Input_Declaration: "iec61131_interfaces_Input_Declarations"):
        self.edge = edge
        self.iec61131_interfaces_Edge_Declaration = iec61131_interfaces_Edge_Declaration
        self.iec61131_interfaces_Edge_Declaration59 = iec61131_interfaces_Edge_Declaration59
        
    @property
    def edge(self) -> str:
        return self.__edge

    @edge.setter
    def edge(self, edge: str):
        self.__edge = edge

    @property
    def iec61131_interfaces_Edge_Declaration(self):
        return self.__iec61131_interfaces_Edge_Declaration

    @iec61131_interfaces_Edge_Declaration.setter
    def iec61131_interfaces_Edge_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_interfaces_Edge_Declaration__iec61131_interfaces_Edge_Declaration", None)
        self.__iec61131_interfaces_Edge_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Var1_List57"):
                opp_val = getattr(old_value, "Var1_List57", None)
                if opp_val == self:
                    setattr(old_value, "Var1_List57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Var1_List57"):
                opp_val = getattr(value, "Var1_List57", None)
                setattr(value, "Var1_List57", self)

    @property
    def iec61131_interfaces_Edge_Declaration59(self):
        return self.__iec61131_interfaces_Edge_Declaration59

    @iec61131_interfaces_Edge_Declaration59.setter
    def iec61131_interfaces_Edge_Declaration59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_interfaces_Edge_Declaration__iec61131_interfaces_Edge_Declaration59", None)
        self.__iec61131_interfaces_Edge_Declaration59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Bool_Type_Name"):
                opp_val = getattr(old_value, "Bool_Type_Name", None)
                if opp_val == self:
                    setattr(old_value, "Bool_Type_Name", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Bool_Type_Name"):
                opp_val = getattr(value, "Bool_Type_Name", None)
                setattr(value, "Bool_Type_Name", self)

class Var1_Specification:

    pass
class iec61131_interfaces_Var1_Specification_Func(Var1_Specification):

    pass
class Var_Init_Decl:

    pass
class iec61131_interfaces_Var2_Init_Decl(Var_Init_Decl):

    pass
class iec61131_interfaces_Var1_Init_Decl(Var_Init_Decl):

    pass
class Var1_List:

    pass
class iec61131_interfaces_Var_Init_Decl(Input_Declaration):

    pass
class LessEqual_Operator:

    pass
class iec61131_operators_LessEqual_Symbol(LessEqual_Operator):

    pass
class operators_LessEqual_Operator:

    pass
class Less_Operator:

    pass
class iec61131_operators_Less_Symbol(Less_Operator):

    pass
class operators_Less_Operator:

    pass
class Unequal_Operator:

    pass
class iec61131_operators_Unequal_Symbol(Unequal_Operator):

    pass
class operators_Unequal_Operator:

    pass
class Il_Expr_Operator:

    pass
class iec61131_operators_Arithmetic_Name(Il_Expr_Operator):

    pass
class iec61131_operators_Comparison_Name(Il_Expr_Operator):

    pass
class operators_Substraction_Operator:

    pass
class GreaterEqual_Operator:

    pass
class iec61131_operators_GreaterEqual_Symbol(GreaterEqual_Operator):

    pass
class operators_GreaterEqual_Operator:

    pass
class Greater_Operator:

    pass
class iec61131_operators_Greater_Symbol(Greater_Operator):

    pass
class operators_Greater_Operator:

    pass
class operators_Divide_Operator:

    pass
class Multiply_Operator:

    pass
class iec61131_operators_Multiply_Symbol(Multiply_Operator):

    pass
class operators_Multiply_Operator:

    pass
class operators_Add_Operator:

    pass
class operators_Arithmetic_Name:

    pass
class iec61131_operators_Multiply_Name(operators_Arithmetic_Name, operators_Multiply_Operator):

    pass
class iec61131_operators_Substraction_Name(operators_Arithmetic_Name, operators_Substraction_Operator):

    pass
class iec61131_operators_Divide_Name(operators_Divide_Operator, operators_Arithmetic_Name):

    pass
class operators_Addition_Operator:

    pass
class iec61131_operators_Addition_Symbol(operators_Add_Operator, operators_Addition_Operator):

    pass
class Equal_Operator:

    pass
class iec61131_operators_Equal_Symbol(Equal_Operator):

    pass
class operators_Comparison_Name:

    pass
class iec61131_operators_LessEqual_Name(operators_LessEqual_Operator, operators_Comparison_Name):

    pass
class iec61131_operators_GreaterEqual_Name(operators_Comparison_Name, operators_GreaterEqual_Operator):

    pass
class iec61131_operators_Less_Name(operators_Comparison_Name, operators_Less_Operator):

    pass
class iec61131_operators_Greater_Name(operators_Comparison_Name, operators_Greater_Operator):

    pass
class iec61131_operators_Unequal_Name(operators_Comparison_Name, operators_Unequal_Operator):

    pass
class operators_Equal_Operator:

    pass
class iec61131_operators_Equal_Name(operators_Comparison_Name, operators_Equal_Operator):

    pass
class And_Operator:

    pass
class iec61131_operators_And_Name(And_Operator):

    pass
class iec61131_operators_And_Symbol(And_Operator):

    pass
class Assignment_Operator:

    pass
class iec61131_operators_Assignment_Name(Assignment_Operator):

    pass
class iec61131_operators_Assignment_Symbol(Assignment_Operator):

    pass
class Power_Operator:

    pass
class iec61131_operators_Power_Name(Power_Operator):

    pass
class iec61131_operators_Power_Symbol(Power_Operator):

    pass
class Divide_Operator:

    pass
class iec61131_operators_Divide_Symbol(Divide_Operator):

    pass
class operators_Unary_Operator:

    pass
class iec61131_operators_Substraction_Symbol(operators_Unary_Operator, operators_Add_Operator, operators_Substraction_Operator):

    pass
class il_Il_Expr_Operator:

    pass
class operators_Operator:

    pass
class iec61131_operators_Or_Operator(il_Il_Expr_Operator, operators_Operator):

    pass
class iec61131_operators_Xor_Operator(il_Il_Expr_Operator, operators_Operator):

    pass
class iec61131_operators_And_Operator(il_Il_Expr_Operator, operators_Operator):

    pass
class EquUequ_Operator:

    pass
class iec61131_operators_Equal_Operator(EquUequ_Operator):

    pass
class Dot_Operator:

    pass
class iec61131_operators_Multiply_Operator(Dot_Operator):

    pass
class iec61131_operators_Addition_Name(operators_Arithmetic_Name, operators_Addition_Operator):

    pass
class iec61131_operators_Unequal_Operator(EquUequ_Operator):

    pass
class Comparison_Operator:

    pass
class iec61131_operators_GreaterEqual_Operator(Comparison_Operator):

    pass
class iec61131_operators_LessEqual_Operator(Comparison_Operator):

    pass
class iec61131_operators_Greater_Operator(Comparison_Operator):

    pass
class iec61131_operators_Less_Operator(Comparison_Operator):

    pass
class iec61131_operators_Divide_Operator(Dot_Operator):

    pass
class operators_Dot_Operator:

    pass
class iec61131_operators_Modulo_Operator(operators_Dot_Operator, il_Il_Expr_Operator):

    pass
class il_Il_Simple_Operator:

    pass
class iec61131_operators_Not_Operator(operators_Unary_Operator, il_Il_Simple_Operator):

    pass
class iec61131_literals_Double_Byte_Character_Representation:

    def __init__(self, value: str, iec61131_literals_Double_Byte_Character_Representation: "Common_Character_Representation" = None):
        self.value = value
        self.iec61131_literals_Double_Byte_Character_Representation = iec61131_literals_Double_Byte_Character_Representation
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def iec61131_literals_Double_Byte_Character_Representation(self):
        return self.__iec61131_literals_Double_Byte_Character_Representation

    @iec61131_literals_Double_Byte_Character_Representation.setter
    def iec61131_literals_Double_Byte_Character_Representation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_literals_Double_Byte_Character_Representation__iec61131_literals_Double_Byte_Character_Representation", None)
        self.__iec61131_literals_Double_Byte_Character_Representation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Common_Character_Representation52"):
                opp_val = getattr(old_value, "Common_Character_Representation52", None)
                if opp_val == self:
                    setattr(old_value, "Common_Character_Representation52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Common_Character_Representation52"):
                opp_val = getattr(value, "Common_Character_Representation52", None)
                setattr(value, "Common_Character_Representation52", self)

class Common_Character_Representation:

    pass
class iec61131_literals_Single_Byte_Character_Representation:

    def __init__(self, value: str, iec61131_literals_Single_Byte_Character_Representation: "Common_Character_Representation" = None):
        self.value = value
        self.iec61131_literals_Single_Byte_Character_Representation = iec61131_literals_Single_Byte_Character_Representation
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def iec61131_literals_Single_Byte_Character_Representation(self):
        return self.__iec61131_literals_Single_Byte_Character_Representation

    @iec61131_literals_Single_Byte_Character_Representation.setter
    def iec61131_literals_Single_Byte_Character_Representation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_literals_Single_Byte_Character_Representation__iec61131_literals_Single_Byte_Character_Representation", None)
        self.__iec61131_literals_Single_Byte_Character_Representation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Common_Character_Representation"):
                opp_val = getattr(old_value, "Common_Character_Representation", None)
                if opp_val == self:
                    setattr(old_value, "Common_Character_Representation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Common_Character_Representation"):
                opp_val = getattr(value, "Common_Character_Representation", None)
                setattr(value, "Common_Character_Representation", self)

class iec61131_literals_Common_Character_Representation:

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class iec61131_literals_Integer(ABC):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class iec61131_operators_Substraction_Operator(ABC):

    pass
class iec61131_operators_Addition_Operator(ABC):

    pass
class Operator:

    pass
class iec61131_operators_Unary_Operator(Operator):

    pass
class iec61131_operators_Comparison_Operator(Operator):

    pass
class iec61131_operators_Power_Operator(Operator):

    pass
class iec61131_operators_Dot_Operator(Operator):

    pass
class iec61131_operators_Assignment_Operator(Operator):

    pass
class iec61131_operators_EquUequ_Operator(Operator):

    pass
class iec61131_operators_Add_Operator(Operator):

    pass
class iec61131_operators_Operator(ABC):

    pass
class Single_Byte_Character_Representation:

    pass
class Character_String:

    pass
class iec61131_literals_Double_Byte_Character_String(Character_String):

    pass
class iec61131_literals_Single_Byte_Character_String(Character_String):

    pass
class iec61131_literals_BSInteger(ABC):

    pass
class iec61131_literals_Date_Literal:

    def __init__(self, year: str, month: str, day: str):
        self.year = year
        self.month = month
        self.day = day
        
    @property
    def day(self) -> str:
        return self.__day

    @day.setter
    def day(self, day: str):
        self.__day = day

    @property
    def month(self) -> str:
        return self.__month

    @month.setter
    def month(self, month: str):
        self.__month = month

    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

class iec61131_literals_Daytime:

    def __init__(self, hour: str, minute: str, iec61131_literals_Daytime: "Fixed_Point" = None):
        self.hour = hour
        self.minute = minute
        self.iec61131_literals_Daytime = iec61131_literals_Daytime
        
    @property
    def minute(self) -> str:
        return self.__minute

    @minute.setter
    def minute(self, minute: str):
        self.__minute = minute

    @property
    def hour(self) -> str:
        return self.__hour

    @hour.setter
    def hour(self, hour: str):
        self.__hour = hour

    @property
    def iec61131_literals_Daytime(self):
        return self.__iec61131_literals_Daytime

    @iec61131_literals_Daytime.setter
    def iec61131_literals_Daytime(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_literals_Daytime__iec61131_literals_Daytime", None)
        self.__iec61131_literals_Daytime = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fixed_Point49"):
                opp_val = getattr(old_value, "Fixed_Point49", None)
                if opp_val == self:
                    setattr(old_value, "Fixed_Point49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fixed_Point49"):
                opp_val = getattr(value, "Fixed_Point49", None)
                setattr(value, "Fixed_Point49", self)

class iec61131_literals_Fixed_Point_Literal(ABC):

    pass
class Double_Byte_Character_Representation:

    pass
class Hours:

    pass
class Unsigned_Integer:

    pass
class Milliseconds:

    pass
class Seconds:

    pass
class Minutes:

    pass
class Date_Literal:

    pass
class Date_Type_Name:

    pass
class iec61131_types_DT_Type_Name(Date_Type_Name):

    pass
class iec61131_types_TOD_Type_Name(Date_Type_Name):

    pass
class TOD_Type_Name:

    pass
class Fixed_Point_Literal:

    pass
class iec61131_literals_Fixed_Point(Fixed_Point_Literal):

    def __init__(self, valuePre: str, valuePost: str, Fixed_Point_Literal: "iec61131_literals_Interval"):
        self.valuePre = valuePre
        self.valuePost = valuePost
        
    @property
    def valuePost(self) -> str:
        return self.__valuePost

    @valuePost.setter
    def valuePost(self, valuePost: str):
        self.__valuePost = valuePost

    @property
    def valuePre(self) -> str:
        return self.__valuePre

    @valuePre.setter
    def valuePre(self, valuePre: str):
        self.__valuePre = valuePre

class iec61131_literals_Interval(ABC):

    pass
class literals_Fixed_Point_Literal:

    pass
class DT_Type_Name:

    pass
class literals_BSInteger:

    pass
class interfaces_Range:

    pass
class st_Case_List_Element:

    pass
class literals_Integer:

    pass
class iec61131_literals_Octal_Integer(literals_Integer, literals_BSInteger):

    pass
class iec61131_literals_Binary_Integer(literals_Integer, literals_BSInteger):

    pass
class iec61131_literals_Unsigned_Integer(literals_Integer, interfaces_Range, st_Case_List_Element, literals_BSInteger, literals_Fixed_Point_Literal):

    pass
class iec61131_literals_Signed_Integer(st_Case_List_Element, literals_Integer, interfaces_Range):

    def __init__(self, negative: bool):
        self.negative = negative
        
    @property
    def negative(self) -> bool:
        return self.__negative

    @negative.setter
    def negative(self, negative: bool):
        self.__negative = negative

class Daytime:

    pass
class Time_Literal:

    pass
class iec61131_literals_Date(Time_Literal):

    pass
class iec61131_literals_Date_And_Time(Time_Literal):

    pass
class iec61131_literals_Time_Of_Day(Time_Literal):

    pass
class Substraction_Operator:

    pass
class Duration_Type_Name:

    pass
class Interval:

    pass
class iec61131_literals_Seconds(Interval):

    pass
class iec61131_literals_Hours(Interval):

    pass
class iec61131_literals_Days(Interval):

    pass
class iec61131_literals_Milliseconds(Interval):

    pass
class iec61131_literals_Minutes(Interval):

    pass
class sfc_Action_Time:

    pass
class literals_Time_Literal:

    pass
class iec61131_literals_Duration(sfc_Action_Time, literals_Time_Literal):

    pass
class iec61131_literals_Hex_Integer(literals_BSInteger, literals_Integer):

    pass
class Integer:

    pass
class Numeric_Literal:

    pass
class iec61131_literals_Integer_Literal(Numeric_Literal):

    pass
class Bit_String_Type_Name:

    pass
class iec61131_types_Bool_Type_Name(Bit_String_Type_Name):

    pass
class BSInteger:

    pass
class il_Il_Operand:

    pass
class configurations_Prog_Data_Source:

    pass
class iec61131_interfaces_Enumerated_Value(st_Case_List_Element, configurations_Prog_Data_Source, il_Il_Operand):

    def __init__(self, name: str, iec61131_interfaces_Enumerated_Value: "Enumerated_Type_Name" = None):
        self.name = name
        self.iec61131_interfaces_Enumerated_Value = iec61131_interfaces_Enumerated_Value
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def iec61131_interfaces_Enumerated_Value(self):
        return self.__iec61131_interfaces_Enumerated_Value

    @iec61131_interfaces_Enumerated_Value.setter
    def iec61131_interfaces_Enumerated_Value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_interfaces_Enumerated_Value__iec61131_interfaces_Enumerated_Value", None)
        self.__iec61131_interfaces_Enumerated_Value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Enumerated_Type_Name"):
                opp_val = getattr(old_value, "Enumerated_Type_Name", None)
                if opp_val == self:
                    setattr(old_value, "Enumerated_Type_Name", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Enumerated_Type_Name"):
                opp_val = getattr(value, "Enumerated_Type_Name", None)
                setattr(value, "Enumerated_Type_Name", self)

class configurations_Data_Source:

    pass
class iec61131_configurations_Global_Var_Reference(configurations_Prog_Data_Source, configurations_Data_Sink, configurations_Data_Source):

    pass
class iec61131_variables_Direct_Variable(variables_Variable, configurations_Prog_Data_Source, configurations_Data_Sink, configurations_Data_Source):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class iec61131_literals_Constant(il_Il_Operand, configurations_Prog_Data_Source, configurations_Data_Source):

    pass
class Fixed_Point:

    pass
class Real_Type_Name:

    pass
class iec61131_literals_Real_Literal(Numeric_Literal):

    def __init__(self, exponent: str, negative: bool, iec61131_literals_Real_Literal: "Real_Type_Name" = None, iec61131_literals_Real_Literal11: "Fixed_Point" = None):
        self.exponent = exponent
        self.negative = negative
        self.iec61131_literals_Real_Literal = iec61131_literals_Real_Literal
        self.iec61131_literals_Real_Literal11 = iec61131_literals_Real_Literal11
        
    @property
    def negative(self) -> bool:
        return self.__negative

    @negative.setter
    def negative(self, negative: bool):
        self.__negative = negative

    @property
    def exponent(self) -> str:
        return self.__exponent

    @exponent.setter
    def exponent(self, exponent: str):
        self.__exponent = exponent

    @property
    def iec61131_literals_Real_Literal11(self):
        return self.__iec61131_literals_Real_Literal11

    @iec61131_literals_Real_Literal11.setter
    def iec61131_literals_Real_Literal11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_literals_Real_Literal__iec61131_literals_Real_Literal11", None)
        self.__iec61131_literals_Real_Literal11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Fixed_Point"):
                opp_val = getattr(old_value, "Fixed_Point", None)
                if opp_val == self:
                    setattr(old_value, "Fixed_Point", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Fixed_Point"):
                opp_val = getattr(value, "Fixed_Point", None)
                setattr(value, "Fixed_Point", self)

    @property
    def iec61131_literals_Real_Literal(self):
        return self.__iec61131_literals_Real_Literal

    @iec61131_literals_Real_Literal.setter
    def iec61131_literals_Real_Literal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_literals_Real_Literal__iec61131_literals_Real_Literal", None)
        self.__iec61131_literals_Real_Literal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Real_Type_Name"):
                opp_val = getattr(old_value, "Real_Type_Name", None)
                if opp_val == self:
                    setattr(old_value, "Real_Type_Name", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Real_Type_Name"):
                opp_val = getattr(value, "Real_Type_Name", None)
                setattr(value, "Real_Type_Name", self)

class Integer_Type_Name:

    pass
class iec61131_types_Signed_Integer_Type_Name(Integer_Type_Name):

    pass
class iec61131_types_Unsigned_Integer_Type_Name(Integer_Type_Name):

    pass
class iec61131_IEC61131:

    pass
class Constant:

    pass
class iec61131_literals_Time_Literal(Constant):

    pass
class iec61131_literals_Character_String(Constant):

    pass
class iec61131_literals_Bit_String_Literal(Constant):

    pass
class iec61131_literals_Boolean_Literal(Constant):

    def __init__(self, value: str, Constant201: "iec61131_interfaces_Var_Name_Decl", Constant555: "iec61131_st_Expression_Constant", Constant209: "iec61131_interfaces_Simple_Spec_Init_Func", Constant: "iec61131_interfaces_InitElement_Constant"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class iec61131_literals_Numeric_Literal(Constant):

    pass
class iec61131_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class iec61131_Commentable(ABC):

    def __init__(self, comments: str):
        self.comments = comments
        
    @property
    def comments(self) -> str:
        return self.__comments

    @comments.setter
    def comments(self, comments: str):
        self.__comments = comments

class NamedElement:

    pass
class iec61131_variables_Variable_Name(Input_Reference, Output_Reference, variables_Symbolic_Variable, NamedElement):

    pass
class iec61131_sfc_Step_Name(NamedElement):

    pass
class iec61131_Library_Element_Name(NamedElement):

    pass
class Commentable:

    pass
class iec61131_Library_Element_Declaration(Commentable):

    pass
class iec61131_interfaces_Global_Var_Name(Commentable, Library_Element_Name):

    pass
class iec61131_st_Param_Assignment(Commentable):

    pass
class iec61131_interfaces_Interface(Commentable):

    pass
class iec61131_st_Statement(Commentable):

    pass
class iec61131_interfaces_Global_Var_Decl(Commentable):

    pass
class iec61131_st_Expression_Variable(Commentable):

    pass
class iec61131_configurations_Program_Configuration(Commentable):

    def __init__(self, retain: bool, iec61131_configurations_Program_Configuration312: "Task_Name" = None, iec61131_configurations_Program_Configuration: "Program_Name" = None, iec61131_configurations_Program_Configuration315: "Program_Type_Name" = None, iec61131_configurations_Program_Configuration318: "Prog_Conf_Elements" = None):
        self.retain = retain
        self.iec61131_configurations_Program_Configuration312 = iec61131_configurations_Program_Configuration312
        self.iec61131_configurations_Program_Configuration = iec61131_configurations_Program_Configuration
        self.iec61131_configurations_Program_Configuration315 = iec61131_configurations_Program_Configuration315
        self.iec61131_configurations_Program_Configuration318 = iec61131_configurations_Program_Configuration318
        
    @property
    def retain(self) -> bool:
        return self.__retain

    @retain.setter
    def retain(self, retain: bool):
        self.__retain = retain

    @property
    def iec61131_configurations_Program_Configuration312(self):
        return self.__iec61131_configurations_Program_Configuration312

    @iec61131_configurations_Program_Configuration312.setter
    def iec61131_configurations_Program_Configuration312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_configurations_Program_Configuration__iec61131_configurations_Program_Configuration312", None)
        self.__iec61131_configurations_Program_Configuration312 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Task_Name313"):
                opp_val = getattr(old_value, "Task_Name313", None)
                if opp_val == self:
                    setattr(old_value, "Task_Name313", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Task_Name313"):
                opp_val = getattr(value, "Task_Name313", None)
                setattr(value, "Task_Name313", self)

    @property
    def iec61131_configurations_Program_Configuration318(self):
        return self.__iec61131_configurations_Program_Configuration318

    @iec61131_configurations_Program_Configuration318.setter
    def iec61131_configurations_Program_Configuration318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_configurations_Program_Configuration__iec61131_configurations_Program_Configuration318", None)
        self.__iec61131_configurations_Program_Configuration318 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Prog_Conf_Elements"):
                opp_val = getattr(old_value, "Prog_Conf_Elements", None)
                if opp_val == self:
                    setattr(old_value, "Prog_Conf_Elements", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Prog_Conf_Elements"):
                opp_val = getattr(value, "Prog_Conf_Elements", None)
                setattr(value, "Prog_Conf_Elements", self)

    @property
    def iec61131_configurations_Program_Configuration(self):
        return self.__iec61131_configurations_Program_Configuration

    @iec61131_configurations_Program_Configuration.setter
    def iec61131_configurations_Program_Configuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_configurations_Program_Configuration__iec61131_configurations_Program_Configuration", None)
        self.__iec61131_configurations_Program_Configuration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Program_Name"):
                opp_val = getattr(old_value, "Program_Name", None)
                if opp_val == self:
                    setattr(old_value, "Program_Name", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Program_Name"):
                opp_val = getattr(value, "Program_Name", None)
                setattr(value, "Program_Name", self)

    @property
    def iec61131_configurations_Program_Configuration315(self):
        return self.__iec61131_configurations_Program_Configuration315

    @iec61131_configurations_Program_Configuration315.setter
    def iec61131_configurations_Program_Configuration315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_iec61131_configurations_Program_Configuration__iec61131_configurations_Program_Configuration315", None)
        self.__iec61131_configurations_Program_Configuration315 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Program_Type_Name316"):
                opp_val = getattr(old_value, "Program_Type_Name316", None)
                if opp_val == self:
                    setattr(old_value, "Program_Type_Name316", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Program_Type_Name316"):
                opp_val = getattr(value, "Program_Type_Name316", None)
                setattr(value, "Program_Type_Name316", self)

class iec61131_variables_Variable(il_Il_Operand, Commentable):

    pass
class iec61131_pous_Function_Block_Type_Name(types_Simple_Specification, Commentable, Library_Element_Name, interfaces_External_Specification):

    pass
class iec61131_st_Expression_Types(Commentable):

    pass