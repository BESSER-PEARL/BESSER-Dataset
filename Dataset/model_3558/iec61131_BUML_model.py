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
Edge: Enumeration = Enumeration(
    name="Edge",
    literals={
            EnumerationLiteral(name="R_EDGE"),
			EnumerationLiteral(name="F_EDGE")
    }
)

Direction: Enumeration = Enumeration(
    name="Direction",
    literals={
            EnumerationLiteral(name="READ_WRITE"),
			EnumerationLiteral(name="READ_ONLY")
    }
)

# Classes
Commentable = Class(name="Commentable")
NamedElement = Class(name="NamedElement")
iec61131_Commentable = Class(name="iec61131::Commentable", is_abstract=True)
iec61131_NamedElement = Class(name="iec61131::NamedElement", is_abstract=True)
iec61131_literals_Numeric_Literal = Class(name="iec61131::literals::Numeric::Literal", is_abstract=True)
Constant = Class(name="Constant")
iec61131_literals_Character_String = Class(name="iec61131::literals::Character::String", is_abstract=True)
iec61131_IEC61131 = Class(name="iec61131::IEC61131")
iec61131_Library_Element_Declaration = Class(name="iec61131::Library::Element::Declaration", is_abstract=True)
iec61131_Library_Element_Name = Class(name="iec61131::Library::Element::Name", is_abstract=True)
Integer_Type_Name = Class(name="Integer::Type::Name")
iec61131_literals_Real_Literal = Class(name="iec61131::literals::Real::Literal")
Real_Type_Name = Class(name="Real::Type::Name")
Fixed_Point = Class(name="Fixed::Point")
iec61131_literals_Boolean_Literal = Class(name="iec61131::literals::Boolean::Literal")
iec61131_literals_Time_Literal = Class(name="iec61131::literals::Time::Literal", is_abstract=True)
iec61131_literals_Constant = Class(name="iec61131::literals::Constant", is_abstract=True)
configurations_Data_Source = Class(name="configurations::Data::Source")
iec61131_literals_Bit_String_Literal = Class(name="iec61131::literals::Bit::String::Literal")
configurations_Prog_Data_Source = Class(name="configurations::Prog::Data::Source")
il_Il_Operand = Class(name="il::Il::Operand")
BSInteger = Class(name="BSInteger")
Bit_String_Type_Name = Class(name="Bit::String::Type::Name")
iec61131_literals_Integer_Literal = Class(name="iec61131::literals::Integer::Literal")
Numeric_Literal = Class(name="Numeric::Literal")
Integer = Class(name="Integer")
iec61131_literals_Hex_Integer = Class(name="iec61131::literals::Hex::Integer")
iec61131_literals_Duration = Class(name="iec61131::literals::Duration")
literals_Time_Literal = Class(name="literals::Time::Literal")
sfc_Action_Time = Class(name="sfc::Action::Time")
Interval = Class(name="Interval")
Duration_Type_Name = Class(name="Duration::Type::Name")
Substraction_Operator = Class(name="Substraction::Operator")
iec61131_literals_Time_Of_Day = Class(name="iec61131::literals::Time::Of::Day")
Time_Literal = Class(name="Time::Literal")
Daytime = Class(name="Daytime")
iec61131_literals_Signed_Integer = Class(name="iec61131::literals::Signed::Integer")
literals_Integer = Class(name="literals::Integer")
st_Case_List_Element = Class(name="st::Case::List::Element")
interfaces_Range = Class(name="interfaces::Range")
iec61131_literals_Binary_Integer = Class(name="iec61131::literals::Binary::Integer")
literals_BSInteger = Class(name="literals::BSInteger")
iec61131_literals_Octal_Integer = Class(name="iec61131::literals::Octal::Integer")
iec61131_literals_Date_And_Time = Class(name="iec61131::literals::Date::And::Time")
DT_Type_Name = Class(name="DT::Type::Name")
iec61131_literals_Unsigned_Integer = Class(name="iec61131::literals::Unsigned::Integer")
literals_Fixed_Point_Literal = Class(name="literals::Fixed::Point::Literal")
iec61131_literals_Interval = Class(name="iec61131::literals::Interval", is_abstract=True)
Fixed_Point_Literal = Class(name="Fixed::Point::Literal")
TOD_Type_Name = Class(name="TOD::Type::Name")
iec61131_literals_Date = Class(name="iec61131::literals::Date")
Date_Type_Name = Class(name="Date::Type::Name")
Date_Literal = Class(name="Date::Literal")
Minutes = Class(name="Minutes")
iec61131_literals_Minutes = Class(name="iec61131::literals::Minutes")
Seconds = Class(name="Seconds")
iec61131_literals_Seconds = Class(name="iec61131::literals::Seconds")
Milliseconds = Class(name="Milliseconds")
iec61131_literals_Days = Class(name="iec61131::literals::Days")
Unsigned_Integer = Class(name="Unsigned::Integer")
Hours = Class(name="Hours")
Double_Byte_Character_Representation = Class(name="Double::Byte::Character::Representation")
iec61131_literals_Hours = Class(name="iec61131::literals::Hours")
iec61131_literals_Fixed_Point_Literal = Class(name="iec61131::literals::Fixed::Point::Literal", is_abstract=True)
iec61131_literals_Daytime = Class(name="iec61131::literals::Daytime")
iec61131_literals_Date_Literal = Class(name="iec61131::literals::Date::Literal")
iec61131_literals_BSInteger = Class(name="iec61131::literals::BSInteger", is_abstract=True)
iec61131_literals_Milliseconds = Class(name="iec61131::literals::Milliseconds")
iec61131_literals_Single_Byte_Character_String = Class(name="iec61131::literals::Single::Byte::Character::String")
Character_String = Class(name="Character::String")
Single_Byte_Character_Representation = Class(name="Single::Byte::Character::Representation")
iec61131_literals_Double_Byte_Character_String = Class(name="iec61131::literals::Double::Byte::Character::String")
iec61131_literals_Fixed_Point = Class(name="iec61131::literals::Fixed::Point")
iec61131_operators_Operator = Class(name="iec61131::operators::Operator", is_abstract=True)
iec61131_operators_Add_Operator = Class(name="iec61131::operators::Add::Operator", is_abstract=True)
Operator = Class(name="Operator")
iec61131_operators_Unary_Operator = Class(name="iec61131::operators::Unary::Operator", is_abstract=True)
iec61131_operators_Addition_Operator = Class(name="iec61131::operators::Addition::Operator", is_abstract=True)
iec61131_operators_Substraction_Operator = Class(name="iec61131::operators::Substraction::Operator", is_abstract=True)
iec61131_operators_Assignment_Operator = Class(name="iec61131::operators::Assignment::Operator", is_abstract=True)
iec61131_operators_Comparison_Operator = Class(name="iec61131::operators::Comparison::Operator", is_abstract=True)
iec61131_literals_Integer = Class(name="iec61131::literals::Integer", is_abstract=True)
iec61131_literals_Common_Character_Representation = Class(name="iec61131::literals::Common::Character::Representation")
iec61131_literals_Single_Byte_Character_Representation = Class(name="iec61131::literals::Single::Byte::Character::Representation")
Common_Character_Representation = Class(name="Common::Character::Representation")
iec61131_literals_Double_Byte_Character_Representation = Class(name="iec61131::literals::Double::Byte::Character::Representation")
il_Il_Simple_Operator = Class(name="il::Il::Simple::Operator")
iec61131_operators_Power_Operator = Class(name="iec61131::operators::Power::Operator", is_abstract=True)
iec61131_operators_Modulo_Operator = Class(name="iec61131::operators::Modulo::Operator")
operators_Dot_Operator = Class(name="operators::Dot::Operator")
iec61131_operators_Divide_Operator = Class(name="iec61131::operators::Divide::Operator", is_abstract=True)
iec61131_operators_Less_Operator = Class(name="iec61131::operators::Less::Operator", is_abstract=True)
Comparison_Operator = Class(name="Comparison::Operator")
iec61131_operators_Greater_Operator = Class(name="iec61131::operators::Greater::Operator", is_abstract=True)
iec61131_operators_GreaterEqual_Operator = Class(name="iec61131::operators::GreaterEqual::Operator", is_abstract=True)
iec61131_operators_LessEqual_Operator = Class(name="iec61131::operators::LessEqual::Operator", is_abstract=True)
iec61131_operators_Unequal_Operator = Class(name="iec61131::operators::Unequal::Operator", is_abstract=True)
iec61131_operators_Addition_Name = Class(name="iec61131::operators::Addition::Name")
iec61131_operators_Multiply_Operator = Class(name="iec61131::operators::Multiply::Operator", is_abstract=True)
Dot_Operator = Class(name="Dot::Operator")
iec61131_operators_Equal_Operator = Class(name="iec61131::operators::Equal::Operator", is_abstract=True)
EquUequ_Operator = Class(name="EquUequ::Operator")
iec61131_operators_And_Operator = Class(name="iec61131::operators::And::Operator", is_abstract=True)
operators_Operator = Class(name="operators::Operator")
il_Il_Expr_Operator = Class(name="il::Il::Expr::Operator")
iec61131_operators_Or_Operator = Class(name="iec61131::operators::Or::Operator")
iec61131_operators_Xor_Operator = Class(name="iec61131::operators::Xor::Operator")
iec61131_operators_Not_Operator = Class(name="iec61131::operators::Not::Operator")
operators_Unary_Operator = Class(name="operators::Unary::Operator")
iec61131_operators_Divide_Symbol = Class(name="iec61131::operators::Divide::Symbol")
Divide_Operator = Class(name="Divide::Operator")
iec61131_operators_Power_Symbol = Class(name="iec61131::operators::Power::Symbol")
Power_Operator = Class(name="Power::Operator")
iec61131_operators_Power_Name = Class(name="iec61131::operators::Power::Name")
iec61131_operators_Assignment_Symbol = Class(name="iec61131::operators::Assignment::Symbol")
Assignment_Operator = Class(name="Assignment::Operator")
iec61131_operators_Assignment_Name = Class(name="iec61131::operators::Assignment::Name")
iec61131_operators_And_Symbol = Class(name="iec61131::operators::And::Symbol")
And_Operator = Class(name="And::Operator")
iec61131_operators_And_Name = Class(name="iec61131::operators::And::Name")
iec61131_operators_Equal_Name = Class(name="iec61131::operators::Equal::Name")
operators_Equal_Operator = Class(name="operators::Equal::Operator")
operators_Comparison_Name = Class(name="operators::Comparison::Name")
iec61131_operators_Equal_Symbol = Class(name="iec61131::operators::Equal::Symbol")
Equal_Operator = Class(name="Equal::Operator")
operators_Addition_Operator = Class(name="operators::Addition::Operator")
operators_Arithmetic_Name = Class(name="operators::Arithmetic::Name")
iec61131_operators_Addition_Symbol = Class(name="iec61131::operators::Addition::Symbol")
operators_Add_Operator = Class(name="operators::Add::Operator")
iec61131_operators_Dot_Operator = Class(name="iec61131::operators::Dot::Operator", is_abstract=True)
iec61131_operators_Multiply_Name = Class(name="iec61131::operators::Multiply::Name")
operators_Multiply_Operator = Class(name="operators::Multiply::Operator")
iec61131_operators_Multiply_Symbol = Class(name="iec61131::operators::Multiply::Symbol")
Multiply_Operator = Class(name="Multiply::Operator")
iec61131_operators_Divide_Name = Class(name="iec61131::operators::Divide::Name")
operators_Divide_Operator = Class(name="operators::Divide::Operator")
iec61131_operators_Greater_Name = Class(name="iec61131::operators::Greater::Name")
operators_Greater_Operator = Class(name="operators::Greater::Operator")
iec61131_operators_Greater_Symbol = Class(name="iec61131::operators::Greater::Symbol")
Greater_Operator = Class(name="Greater::Operator")
iec61131_operators_GreaterEqual_Name = Class(name="iec61131::operators::GreaterEqual::Name")
operators_GreaterEqual_Operator = Class(name="operators::GreaterEqual::Operator")
iec61131_operators_GreaterEqual_Symbol = Class(name="iec61131::operators::GreaterEqual::Symbol")
GreaterEqual_Operator = Class(name="GreaterEqual::Operator")
iec61131_operators_Substraction_Name = Class(name="iec61131::operators::Substraction::Name")
operators_Substraction_Operator = Class(name="operators::Substraction::Operator")
iec61131_operators_Substraction_Symbol = Class(name="iec61131::operators::Substraction::Symbol")
iec61131_operators_EquUequ_Operator = Class(name="iec61131::operators::EquUequ::Operator", is_abstract=True)
iec61131_operators_Comparison_Name = Class(name="iec61131::operators::Comparison::Name", is_abstract=True)
Il_Expr_Operator = Class(name="Il::Expr::Operator")
iec61131_operators_Unequal_Name = Class(name="iec61131::operators::Unequal::Name")
operators_Unequal_Operator = Class(name="operators::Unequal::Operator")
iec61131_operators_Unequal_Symbol = Class(name="iec61131::operators::Unequal::Symbol")
Unequal_Operator = Class(name="Unequal::Operator")
iec61131_operators_Less_Name = Class(name="iec61131::operators::Less::Name")
operators_Less_Operator = Class(name="operators::Less::Operator")
iec61131_operators_Less_Symbol = Class(name="iec61131::operators::Less::Symbol")
Less_Operator = Class(name="Less::Operator")
iec61131_operators_LessEqual_Name = Class(name="iec61131::operators::LessEqual::Name")
operators_LessEqual_Operator = Class(name="operators::LessEqual::Operator")
iec61131_operators_LessEqual_Symbol = Class(name="iec61131::operators::LessEqual::Symbol")
LessEqual_Operator = Class(name="LessEqual::Operator")
iec61131_interfaces_Var_Init_Decl = Class(name="iec61131::interfaces::Var::Init::Decl", is_abstract=True)
Var1_List = Class(name="Var1::List")
iec61131_interfaces_Var1_Init_Decl = Class(name="iec61131::interfaces::Var1::Init::Decl")
Var_Init_Decl = Class(name="Var::Init::Decl")
Var1_Specification = Class(name="Var1::Specification")
iec61131_interfaces_Edge_Declaration = Class(name="iec61131::interfaces::Edge::Declaration")
iec61131_operators_Arithmetic_Name = Class(name="iec61131::operators::Arithmetic::Name", is_abstract=True)
iec61131_interfaces_Io_Var_Declaration = Class(name="iec61131::interfaces::Io::Var::Declaration", is_abstract=True)
interfaces_Interface = Class(name="interfaces::Interface")
pous_Function_Block_Vars = Class(name="pous::Function::Block::Vars")
pous_Program_Vars = Class(name="pous::Program::Vars")
pous_Function_Vars = Class(name="pous::Function::Vars")
iec61131_interfaces_Input_Declarations = Class(name="iec61131::interfaces::Input::Declarations")
Io_Var_Declaration = Class(name="Io::Var::Declaration")
Input_Declaration = Class(name="Input::Declaration")
iec61131_interfaces_Subrange_Spec_Init = Class(name="iec61131::interfaces::Subrange::Spec::Init")
interfaces_Var1_Specification_Func = Class(name="interfaces::Var1::Specification::Func")
Subrange_Specification = Class(name="Subrange::Specification")
Signed_Integer = Class(name="Signed::Integer")
iec61131_interfaces_Enumerated_Spec_Init = Class(name="iec61131::interfaces::Enumerated::Spec::Init")
Enumerated_Specification = Class(name="Enumerated::Specification")
Bool_Type_Name = Class(name="Bool::Type::Name")
iec61131_interfaces_Var1_Specification = Class(name="iec61131::interfaces::Var1::Specification", is_abstract=True)
Assignment_Symbol = Class(name="Assignment::Symbol")
iec61131_interfaces_Simple_Spec_Init = Class(name="iec61131::interfaces::Simple::Spec::Init", is_abstract=True)
interfaces_Var1_Specification = Class(name="interfaces::Var1::Specification")
interfaces_Located_Var_Spec_Init = Class(name="interfaces::Located::Var::Spec::Init")
pous_Structure_Elements = Class(name="pous::Structure::Elements")
Simple_Specification = Class(name="Simple::Specification")
iec61131_interfaces_Fb_Name_Decl = Class(name="iec61131::interfaces::Fb::Name::Decl")
Temp_Var_Declaration = Class(name="Temp::Var::Declaration")
Structure_Initialization = Class(name="Structure::Initialization")
Function_Block_Type_Name = Class(name="Function::Block::Type::Name")
iec61131_interfaces_String_Var_Declaration = Class(name="iec61131::interfaces::String::Var::Declaration", is_abstract=True)
interfaces_Temp_Var_Decl = Class(name="interfaces::Temp::Var::Decl")
interfaces_Var2_Init_Decl = Class(name="interfaces::Var2::Init::Decl")
iec61131_interfaces_Output_Declarations = Class(name="iec61131::interfaces::Output::Declarations")
Enumerated_Value = Class(name="Enumerated::Value")
iec61131_interfaces_Array_Var_Init_Decl = Class(name="iec61131::interfaces::Array::Var::Init::Decl")
Var2_Init_Decl = Class(name="Var2::Init::Decl")
Array_Spec_Init = Class(name="Array::Spec::Init")
iec61131_interfaces_Structured_Var_Init_Decl = Class(name="iec61131::interfaces::Structured::Var::Init::Decl")
Initialized_Structure = Class(name="Initialized::Structure")
Array_Initialization = Class(name="Array::Initialization")
Array_Specification = Class(name="Array::Specification")
iec61131_interfaces_Initialized_Structure = Class(name="iec61131::interfaces::Initialized::Structure")
pous_Structure_Specification = Class(name="pous::Structure::Specification")
Structure_Type_Name = Class(name="Structure::Type::Name")
iec61131_interfaces_Input_Output_Declarations = Class(name="iec61131::interfaces::Input::Output::Declarations")
Var_Declaration = Class(name="Var::Declaration")
iec61131_interfaces_Array_Spec_Init = Class(name="iec61131::interfaces::Array::Spec::Init")
Initial_Element = Class(name="Initial::Element")
iec61131_interfaces_Structure_Element_Name = Class(name="iec61131::interfaces::Structure::Element::Name")
iec61131_interfaces_Enumerated_Value = Class(name="iec61131::interfaces::Enumerated::Value")
Enumerated_Type_Name = Class(name="Enumerated::Type::Name")
iec61131_interfaces_Array_Initialization = Class(name="iec61131::interfaces::Array::Initialization")
Array_Initial_Elements = Class(name="Array::Initial::Elements")
iec61131_interfaces_Var_Declaration = Class(name="iec61131::interfaces::Var::Declaration", is_abstract=True)
iec61131_interfaces_Temp_Var_Decl = Class(name="iec61131::interfaces::Temp::Var::Decl", is_abstract=True)
iec61131_interfaces_Structure_Initialization = Class(name="iec61131::interfaces::Structure::Initialization")
Structure_Element_Initialization = Class(name="Structure::Element::Initialization")
iec61131_interfaces_Structure_Element_Initialization = Class(name="iec61131::interfaces::Structure::Element::Initialization")
Structure_Element_Name = Class(name="Structure::Element::Name")
iec61131_interfaces_Array_Var_Declaration = Class(name="iec61131::interfaces::Array::Var::Declaration")
iec61131_interfaces_Structured_Var_Declaration = Class(name="iec61131::interfaces::Structured::Var::Declaration")
iec61131_interfaces_Specification = Class(name="iec61131::interfaces::Specification", is_abstract=True)
iec61131_interfaces_Subrange_Specification = Class(name="iec61131::interfaces::Subrange::Specification", is_abstract=True)
interfaces_Specification = Class(name="interfaces::Specification")
interfaces_External_Specification = Class(name="interfaces::External::Specification")
iec61131_interfaces_Var1_Declaration = Class(name="iec61131::interfaces::Var1::Declaration")
Specification = Class(name="Specification")
Range = Class(name="Range")
iec61131_interfaces_Double_Byte_String_Spec = Class(name="iec61131::interfaces::Double::Byte::String::Spec")
interfaces_Var_Spec = Class(name="interfaces::Var::Spec")
Double_Byte_Character_String = Class(name="Double::Byte::Character::String")
iec61131_interfaces_Enumerated_Specification = Class(name="iec61131::interfaces::Enumerated::Specification", is_abstract=True)
iec61131_interfaces_Single_Byte_String_Var_Declaration = Class(name="iec61131::interfaces::Single::Byte::String::Var::Declaration")
String_Var_Declaration = Class(name="String::Var::Declaration")
iec61131_interfaces_Array_Specification = Class(name="iec61131::interfaces::Array::Specification", is_abstract=True)
Single_Byte_String_Spec = Class(name="Single::Byte::String::Spec")
iec61131_interfaces_Array_Initial_Elements = Class(name="iec61131::interfaces::Array::Initial::Elements", is_abstract=True)
iec61131_interfaces_Double_Byte_String_Var_Declaration = Class(name="iec61131::interfaces::Double::Byte::String::Var::Declaration")
iec61131_interfaces_Subrange = Class(name="iec61131::interfaces::Subrange")
Case_List_Element = Class(name="Case::List::Element")
Double_Byte_String_Spec = Class(name="Double::Byte::String::Spec")
iec61131_interfaces_Single_Byte_String_Spec = Class(name="iec61131::interfaces::Single::Byte::String::Spec")
Located_Var_Spec_Init = Class(name="Located::Var::Spec::Init")
Single_Byte_Character_String = Class(name="Single::Byte::Character::String")
Single_BString = Class(name="Single::BString")
iec61131_interfaces_Interface = Class(name="iec61131::interfaces::Interface", is_abstract=True)
Double_BString = Class(name="Double::BString")
iec61131_interfaces_Var1_List = Class(name="iec61131::interfaces::Var1::List")
Variable_Name = Class(name="Variable::Name")
iec61131_interfaces_Other_Var_Declaration = Class(name="iec61131::interfaces::Other::Var::Declaration", is_abstract=True)
iec61131_interfaces_External_Var_Declarations = Class(name="iec61131::interfaces::External::Var::Declarations")
Other_Var_Declaration = Class(name="Other::Var::Declaration")
External_Declaration = Class(name="External::Declaration")
iec61131_interfaces_Retentive_Var_Declarations = Class(name="iec61131::interfaces::Retentive::Var::Declarations")
RNV_Declarations = Class(name="RNV::Declarations")
iec61131_interfaces_Non_Retentive_Var_Declarations = Class(name="iec61131::interfaces::Non::Retentive::Var::Declarations")
iec61131_interfaces_External_Declaration = Class(name="iec61131::interfaces::External::Declaration")
Global_Var_Name = Class(name="Global::Var::Name")
External_Specification = Class(name="External::Specification")
iec61131_interfaces_Global_Var_Name = Class(name="iec61131::interfaces::Global::Var::Name")
Library_Element_Name = Class(name="Library::Element::Name")
iec61131_interfaces_Global_Var_List = Class(name="iec61131::interfaces::Global::Var::List")
Global_Var_Spec = Class(name="Global::Var::Spec")
iec61131_interfaces_Temp_Var_Decls = Class(name="iec61131::interfaces::Temp::Var::Decls")
Temp_Var_Decl = Class(name="Temp::Var::Decl")
iec61131_interfaces_Var_Declarations = Class(name="iec61131::interfaces::Var::Declarations")
iec61131_interfaces_Incompl_Location = Class(name="iec61131::interfaces::Incompl::Location")
iec61131_interfaces_Incompl_Located_Var_Declarations = Class(name="iec61131::interfaces::Incompl::Located::Var::Declarations")
Incompl_Located_Var_Decl = Class(name="Incompl::Located::Var::Decl")
iec61131_interfaces_RNV_Declarations = Class(name="iec61131::interfaces::RNV::Declarations", is_abstract=True)
iec61131_interfaces_Incompl_Located_Var_Decl = Class(name="iec61131::interfaces::Incompl::Located::Var::Decl")
Incompl_Location = Class(name="Incompl::Location")
Var_Spec = Class(name="Var::Spec")
Located_Var_Decl = Class(name="Located::Var::Decl")
iec61131_interfaces_Var_Spec = Class(name="iec61131::interfaces::Var::Spec", is_abstract=True)
iec61131_interfaces_External_Specification = Class(name="iec61131::interfaces::External::Specification", is_abstract=True)
iec61131_interfaces_Located_Var_Spec_Init = Class(name="iec61131::interfaces::Located::Var::Spec::Init", is_abstract=True)
iec61131_interfaces_Location = Class(name="iec61131::interfaces::Location")
Direct_Variable = Class(name="Direct::Variable")
iec61131_interfaces_Located_Var_Decl = Class(name="iec61131::interfaces::Located::Var::Decl")
Location = Class(name="Location")
iec61131_interfaces_Located_Var_Declarations = Class(name="iec61131::interfaces::Located::Var::Declarations")
Program_Vars = Class(name="Program::Vars")
iec61131_interfaces_Global_Var_Declarations = Class(name="iec61131::interfaces::Global::Var::Declarations")
Library_Element_Declaration = Class(name="Library::Element::Declaration")
Global_Var_Decl = Class(name="Global::Var::Decl")
iec61131_interfaces_Global_Var_Decl = Class(name="iec61131::interfaces::Global::Var::Decl")
iec61131_interfaces_Global_Var_Spec = Class(name="iec61131::interfaces::Global::Var::Spec", is_abstract=True)
iec61131_interfaces_Global_Var_Location = Class(name="iec61131::interfaces::Global::Var::Location")
iec61131_interfaces_Subrange_Specification2 = Class(name="iec61131::interfaces::Subrange::Specification2")
iec61131_interfaces_Input_Declaration = Class(name="iec61131::interfaces::Input::Declaration", is_abstract=True)
iec61131_interfaces_Range = Class(name="iec61131::interfaces::Range", is_abstract=True)
iec61131_interfaces_Byte_String = Class(name="iec61131::interfaces::Byte::String", is_abstract=True)
iec61131_interfaces_Single_BString = Class(name="iec61131::interfaces::Single::BString")
Byte_String = Class(name="Byte::String")
Single_Byte_String_Type_Name = Class(name="Single::Byte::String::Type::Name")
iec61131_interfaces_Double_BString = Class(name="iec61131::interfaces::Double::BString")
Double_Byte_String_Type_Name = Class(name="Double::Byte::String::Type::Name")
iec61131_interfaces_Subrange_Specification1 = Class(name="iec61131::interfaces::Subrange::Specification1")
Subrange = Class(name="Subrange")
iec61131_interfaces_Array_Initial_Elements1 = Class(name="iec61131::interfaces::Array::Initial::Elements1")
Subrange_Type_Name = Class(name="Subrange::Type::Name")
iec61131_interfaces_Enumerated_Specification1 = Class(name="iec61131::interfaces::Enumerated::Specification1")
iec61131_interfaces_Enumerated_Specification2 = Class(name="iec61131::interfaces::Enumerated::Specification2")
iec61131_interfaces_Array_Specification1 = Class(name="iec61131::interfaces::Array::Specification1")
Array_Type_Name = Class(name="Array::Type::Name")
iec61131_interfaces_Array_Specification2 = Class(name="iec61131::interfaces::Array::Specification2")
Non_Generic_Type_Name = Class(name="Non::Generic::Type::Name")
iec61131_interfaces_Array_Initial_Elements2 = Class(name="iec61131::interfaces::Array::Initial::Elements2")
iec61131_interfaces_Initial_Element = Class(name="iec61131::interfaces::Initial::Element", is_abstract=True)
iec61131_interfaces_InitElement_Constant = Class(name="iec61131::interfaces::InitElement::Constant")
iec61131_interfaces_InitElement_EnumValue = Class(name="iec61131::interfaces::InitElement::EnumValue")
iec61131_interfaces_InitElement_Structure = Class(name="iec61131::interfaces::InitElement::Structure")
iec61131_interfaces_InitElement_Array = Class(name="iec61131::interfaces::InitElement::Array")
iec61131_interfaces_Var2_Init_Decl = Class(name="iec61131::interfaces::Var2::Init::Decl", is_abstract=True)
iec61131_interfaces_Function_Var_Decl = Class(name="iec61131::interfaces::Function::Var::Decl")
iec61131_interfaces_Simple_Specification_Func = Class(name="iec61131::interfaces::Simple::Specification::Func", is_abstract=True)
iec61131_interfaces_Var1_Specification_Func = Class(name="iec61131::interfaces::Var1::Specification::Func", is_abstract=True)
iec61131_interfaces_Var_Name_Decl = Class(name="iec61131::interfaces::Var::Name::Decl")
Simple_Spec_Init = Class(name="Simple::Spec::Init")
iec61131_interfaces_Var_Init_Decl_Func = Class(name="iec61131::interfaces::Var::Init::Decl::Func")
Var1_Specification_Func = Class(name="Var1::Specification::Func")
iec61131_interfaces_Simple_Spec_Init_Func = Class(name="iec61131::interfaces::Simple::Spec::Init::Func")
Simple_Specification_Func = Class(name="Simple::Specification::Func")
pous_Function_Block_Type_Name = Class(name="pous::Function::Block::Type::Name")
iec61131_pous_Function_Block_Declaration = Class(name="iec61131::pous::Function::Block::Declaration")
iec61131_interfaces_Temp_Var_Declaration = Class(name="iec61131::interfaces::Temp::Var::Declaration", is_abstract=True)
iec61131_pous_Program_Declaration = Class(name="iec61131::pous::Program::Declaration")
Program_Type_Name = Class(name="Program::Type::Name")
Function_Block_Body = Class(name="Function::Block::Body")
iec61131_pous_Program_Type_Name = Class(name="iec61131::pous::Program::Type::Name")
Blocks = Class(name="Blocks")
iec61131_pous_Function_Block_Type_Name = Class(name="iec61131::pous::Function::Block::Type::Name", is_abstract=True)
types_Simple_Specification = Class(name="types::Simple::Specification")
iec61131_pous_Derived_Function_Block_Name = Class(name="iec61131::pous::Derived::Function::Block::Name")
Derived_Function_Block_Name = Class(name="Derived::Function::Block::Name")
Function_Block_Vars = Class(name="Function::Block::Vars")
iec61131_pous_Function_Declaration = Class(name="iec61131::pous::Function::Declaration")
Derived_Function_Name = Class(name="Derived::Function::Name")
Function_Return_Value = Class(name="Function::Return::Value")
Function_Vars = Class(name="Function::Vars")
Function_Body = Class(name="Function::Body")
iec61131_pous_Access_Name = Class(name="iec61131::pous::Access::Name")
iec61131_pous_Derived_Function_Name = Class(name="iec61131::pous::Derived::Function::Name")
pous_Function_Name = Class(name="pous::Function::Name")
iec61131_pous_Function_Return_Value = Class(name="iec61131::pous::Function::Return::Value", is_abstract=True)
iec61131_pous_Function_Body = Class(name="iec61131::pous::Function::Body", is_abstract=True)
iec61131_pous_Other_Language = Class(name="iec61131::pous::Other::Language")
pous_Function_Body = Class(name="pous::Function::Body")
pous_Function_Block_Body = Class(name="pous::Function::Block::Body")
iec61131_pous_Function_Block_Body = Class(name="iec61131::pous::Function::Block::Body", is_abstract=True)
iec61131_pous_Program_Access_Decl = Class(name="iec61131::pous::Program::Access::Decl")
Access_Name = Class(name="Access::Name")
Symbolic_Variable = Class(name="Symbolic::Variable")
iec61131_pous_Function_Name = Class(name="iec61131::pous::Function::Name", is_abstract=True)
iec61131_pous_Data_Type_Declaration = Class(name="iec61131::pous::Data::Type::Declaration")
Type_Declaration = Class(name="Type::Declaration")
iec61131_pous_Type_Declaration = Class(name="iec61131::pous::Type::Declaration", is_abstract=True)
iec61131_pous_Single_Element_Type_Declaration = Class(name="iec61131::pous::Single::Element::Type::Declaration", is_abstract=True)
iec61131_pous_Array_Type_Declaration = Class(name="iec61131::pous::Array::Type::Declaration")
iec61131_pous_Structure_Type_Declaration = Class(name="iec61131::pous::Structure::Type::Declaration")
Structure_Specification = Class(name="Structure::Specification")
iec61131_pous_String_Type_Declaration = Class(name="iec61131::pous::String::Type::Declaration")
String_Type_Name = Class(name="String::Type::Name")
Byte_String_Type_Name = Class(name="Byte::String::Type::Name")
Program_Access_Decl = Class(name="Program::Access::Decl")
iec61131_pous_Library = Class(name="iec61131::pous::Library")
Program_Declaration = Class(name="Program::Declaration")
Function_Declaration = Class(name="Function::Declaration")
iec61131_pous_Simple_Type_Declaration = Class(name="iec61131::pous::Simple::Type::Declaration")
Single_Element_Type_Declaration = Class(name="Single::Element::Type::Declaration")
Simple_Type_Name = Class(name="Simple::Type::Name")
iec61131_pous_Subrange_Type_Declaration = Class(name="iec61131::pous::Subrange::Type::Declaration")
Subrange_Spec_Init = Class(name="Subrange::Spec::Init")
iec61131_pous_Enumerated_Type_Declaration = Class(name="iec61131::pous::Enumerated::Type::Declaration")
Enumerated_Spec_Init = Class(name="Enumerated::Spec::Init")
iec61131_pous_Structure_Specification = Class(name="iec61131::pous::Structure::Specification", is_abstract=True)
iec61131_pous_Structure_Declaration = Class(name="iec61131::pous::Structure::Declaration")
Structure_Element_Declaration = Class(name="Structure::Element::Declaration")
iec61131_pous_Structure_Element_Declaration = Class(name="iec61131::pous::Structure::Element::Declaration")
Structure_Elements = Class(name="Structure::Elements")
iec61131_pous_Structure_Elements = Class(name="iec61131::pous::Structure::Elements", is_abstract=True)
iec61131_pous_Program_Vars = Class(name="iec61131::pous::Program::Vars", is_abstract=True)
iec61131_pous_Function_Vars = Class(name="iec61131::pous::Function::Vars", is_abstract=True)
iec61131_pous_Function_Block_Vars = Class(name="iec61131::pous::Function::Block::Vars", is_abstract=True)
iec61131_pous_Program_Access_Decls = Class(name="iec61131::pous::Program::Access::Decls")
Resource_Name = Class(name="Resource::Name")
Function_Block_Declaration = Class(name="Function::Block::Declaration")
iec61131_configurations_Configuration_Name = Class(name="iec61131::configurations::Configuration::Name")
iec61131_configurations_Resource_Type_Name = Class(name="iec61131::configurations::Resource::Type::Name")
iec61131_configurations_Configuration_Declaration = Class(name="iec61131::configurations::Configuration::Declaration")
Configuration_Name = Class(name="Configuration::Name")
Single_Resource_Declaration = Class(name="Single::Resource::Declaration")
Global_Var_Declarations = Class(name="Global::Var::Declarations")
Instance_Specific_Initializations = Class(name="Instance::Specific::Initializations")
Access_Declarations = Class(name="Access::Declarations")
Resource_Declaration = Class(name="Resource::Declaration")
iec61131_configurations_Resource_Name = Class(name="iec61131::configurations::Resource::Name")
iec61131_configurations_Resource_Declaration = Class(name="iec61131::configurations::Resource::Declaration")
Resource_Type_Name = Class(name="Resource::Type::Name")
iec61131_configurations_Single_Resource_Declaration = Class(name="iec61131::configurations::Single::Resource::Declaration")
Task_Configuration = Class(name="Task::Configuration")
Program_Configuration = Class(name="Program::Configuration")
iec61131_configurations_Task_Configuration = Class(name="iec61131::configurations::Task::Configuration")
Task_Name = Class(name="Task::Name")
Priority = Class(name="Priority")
Single = Class(name="Single")
iec61131_configurations_Program_Configuration = Class(name="iec61131::configurations::Program::Configuration")
Program_Name = Class(name="Program::Name")
iec61131_configurations_Access_Name = Class(name="iec61131::configurations::Access::Name")
Prog_Conf_Elements = Class(name="Prog::Conf::Elements")
iec61131_configurations_Instance_Specific_Initializations = Class(name="iec61131::configurations::Instance::Specific::Initializations")
Instance_Specific_Init = Class(name="Instance::Specific::Init")
iec61131_configurations_Data_Source = Class(name="iec61131::configurations::Data::Source", is_abstract=True)
iec61131_configurations_Global_Var_Reference = Class(name="iec61131::configurations::Global::Var::Reference")
configurations_Data_Sink = Class(name="configurations::Data::Sink")
iec61131_configurations_Program_Output_Reference = Class(name="iec61131::configurations::Program::Output::Reference")
Data_Source = Class(name="Data::Source")
iec61131_configurations_Access_Declarations = Class(name="iec61131::configurations::Access::Declarations")
Access_Declaration = Class(name="Access::Declaration")
iec61131_configurations_Access_Declaration = Class(name="iec61131::configurations::Access::Declaration")
Access_Path = Class(name="Access::Path")
iec61131_configurations_Prog_Cnxn = Class(name="iec61131::configurations::Prog::Cnxn", is_abstract=True)
iec61131_configurations_Access_Path = Class(name="iec61131::configurations::Access::Path", is_abstract=True)
iec61131_configurations_Direct_Path = Class(name="iec61131::configurations::Direct::Path")
iec61131_configurations_Symbolic_Path = Class(name="iec61131::configurations::Symbolic::Path")
iec61131_configurations_Program_Name = Class(name="iec61131::configurations::Program::Name")
iec61131_configurations_Task_Name = Class(name="iec61131::configurations::Task::Name")
iec61131_configurations_Task_Initialization = Class(name="iec61131::configurations::Task::Initialization", is_abstract=True)
iec61131_configurations_Prog_Conf_Elements = Class(name="iec61131::configurations::Prog::Conf::Elements")
Prog_Conf_Element = Class(name="Prog::Conf::Element")
iec61131_configurations_Prog_Conf_Element = Class(name="iec61131::configurations::Prog::Conf::Element", is_abstract=True)
iec61131_configurations_Fb_Task = Class(name="iec61131::configurations::Fb::Task")
iec61131_configurations_Prog_Data_Source = Class(name="iec61131::configurations::Prog::Data::Source", is_abstract=True)
iec61131_configurations_Prog_Sink = Class(name="iec61131::configurations::Prog::Sink")
Prog_Cnxn = Class(name="Prog::Cnxn")
Data_Sink = Class(name="Data::Sink")
iec61131_configurations_Prog_Source = Class(name="iec61131::configurations::Prog::Source")
Prog_Data_Source = Class(name="Prog::Data::Source")
iec61131_configurations_Data_Sink = Class(name="iec61131::configurations::Data::Sink", is_abstract=True)
iec61131_configurations_Instance_Specific_Init = Class(name="iec61131::configurations::Instance::Specific::Init", is_abstract=True)
iec61131_configurations_Instance_Spec1 = Class(name="iec61131::configurations::Instance::Spec1")
iec61131_configurations_Instance_Spec2 = Class(name="iec61131::configurations::Instance::Spec2")
iec61131_st_Subprogram_Control_Statement = Class(name="iec61131::st::Subprogram::Control::Statement", is_abstract=True)
iec61131_st_Selection_Statement = Class(name="iec61131::st::Selection::Statement", is_abstract=True)
iec61131_configurations_Single = Class(name="iec61131::configurations::Single")
Task_Initialization = Class(name="Task::Initialization")
iec61131_configurations_Interval = Class(name="iec61131::configurations::Interval")
iec61131_configurations_Priority = Class(name="iec61131::configurations::Priority")
iec61131_st_Statement_List = Class(name="iec61131::st::Statement::List")
Statement = Class(name="Statement")
iec61131_st_Expression = Class(name="iec61131::st::Expression")
Expression_Types = Class(name="Expression::Types")
Or_Operator = Class(name="Or::Operator")
iec61131_st_Statement = Class(name="iec61131::st::Statement", is_abstract=True)
iec61131_st_Assignment_Statement = Class(name="iec61131::st::Assignment::Statement")
Expression_Variable = Class(name="Expression::Variable")
Else_Statement = Class(name="Else::Statement")
iec61131_st_Case_Statement = Class(name="iec61131::st::Case::Statement")
iec61131_st_Iteration_Statement = Class(name="iec61131::st::Iteration::Statement", is_abstract=True)
iec61131_st_Return_Statement = Class(name="iec61131::st::Return::Statement")
Subprogram_Control_Statement = Class(name="Subprogram::Control::Statement")
iec61131_st_Fb_Invocation = Class(name="iec61131::st::Fb::Invocation")
Param_Assignment = Class(name="Param::Assignment")
iec61131_st_Param_Assignment = Class(name="iec61131::st::Param::Assignment", is_abstract=True)
iec61131_st_Param_Type1 = Class(name="iec61131::st::Param::Type1")
iec61131_st_Param_Type2 = Class(name="iec61131::st::Param::Type2")
Variable = Class(name="Variable")
Not_Operator = Class(name="Not::Operator")
iec61131_st_If_Statement = Class(name="iec61131::st::If::Statement")
Selection_Statement = Class(name="Selection::Statement")
Statement_List = Class(name="Statement::List")
Else_If_Statement = Class(name="Else::If::Statement")
iec61131_st_While_Statement = Class(name="iec61131::st::While::Statement")
Case_Element = Class(name="Case::Element")
iec61131_st_Else_If_Statement = Class(name="iec61131::st::Else::If::Statement")
iec61131_st_Else_Statement = Class(name="iec61131::st::Else::Statement")
iec61131_st_Case_Element = Class(name="iec61131::st::Case::Element")
Case_List = Class(name="Case::List")
iec61131_st_Case_List = Class(name="iec61131::st::Case::List")
iec61131_st_Case_List_Element = Class(name="iec61131::st::Case::List::Element", is_abstract=True)
iec61131_st_For_Statement = Class(name="iec61131::st::For::Statement")
Iteration_Statement = Class(name="Iteration::Statement")
Control_Variable = Class(name="Control::Variable")
For_List = Class(name="For::List")
iec61131_st_Repeat_Statement = Class(name="iec61131::st::Repeat::Statement")
iec61131_st_Exit_Statement = Class(name="iec61131::st::Exit::Statement")
iec61131_st_Control_Variable = Class(name="iec61131::st::Control::Variable")
iec61131_st_For_List = Class(name="iec61131::st::For::List")
iec61131_st_Xor_Expression = Class(name="iec61131::st::Xor::Expression")
Xor_Operator = Class(name="Xor::Operator")
iec61131_st_And_Expression = Class(name="iec61131::st::And::Expression")
iec61131_st_Comparison = Class(name="iec61131::st::Comparison")
iec61131_st_Equ_Expression = Class(name="iec61131::st::Equ::Expression")
iec61131_st_Add_Expression = Class(name="iec61131::st::Add::Expression")
iec61131_st_Primary_Expression = Class(name="iec61131::st::Primary::Expression", is_abstract=True)
Add_Operator = Class(name="Add::Operator")
iec61131_st_Term_Expression = Class(name="iec61131::st::Term::Expression")
iec61131_st_Power_Expression = Class(name="iec61131::st::Power::Expression")
Power_Symbol = Class(name="Power::Symbol")
iec61131_st_Unary_Expression = Class(name="iec61131::st::Unary::Expression")
Unary_Operator = Class(name="Unary::Operator")
iec61131_il_Instruction_List = Class(name="iec61131::il::Instruction::List")
Il_Instruction = Class(name="Il::Instruction")
iec61131_st_Bracket_Expression = Class(name="iec61131::st::Bracket::Expression")
Primary_Expression = Class(name="Primary::Expression")
iec61131_st_Call_Expression = Class(name="iec61131::st::Call::Expression")
Function_Name = Class(name="Function::Name")
iec61131_st_Expression_Types = Class(name="iec61131::st::Expression::Types", is_abstract=True)
iec61131_st_Expression_Variable = Class(name="iec61131::st::Expression::Variable")
Array_Variable = Class(name="Array::Variable")
Structured_Variable = Class(name="Structured::Variable")
iec61131_st_Expression_Constant = Class(name="iec61131::st::Expression::Constant")
iec61131_st_Expression_EnumValue = Class(name="iec61131::st::Expression::EnumValue")
iec61131_st_Expression_Variable_Type = Class(name="iec61131::st::Expression::Variable::Type")
iec61131_il_Il_Formal_Funct_Call = Class(name="iec61131::il::Il::Formal::Funct::Call")
iec61131_il_Simple_Instr_List = Class(name="iec61131::il::Simple::Instr::List")
Il_Simple_Instruction = Class(name="Il::Simple::Instruction")
iec61131_il_Il_Instruction = Class(name="iec61131::il::Il::Instruction")
Label = Class(name="Label")
Il_Operations = Class(name="Il::Operations")
iec61131_il_Label = Class(name="iec61131::il::Label")
iec61131_il_Il_Simple_Operation = Class(name="iec61131::il::Il::Simple::Operation", is_abstract=True)
il_Il_Operations = Class(name="il::Il::Operations")
il_Simple_Instr = Class(name="il::Simple::Instr")
iec61131_il_Il_Expression = Class(name="iec61131::il::Il::Expression")
Il_Operand = Class(name="Il::Operand")
Simple_Instr_List = Class(name="Simple::Instr::List")
iec61131_il_Il_Jump_Operation = Class(name="iec61131::il::Il::Jump::Operation")
Il_Jump_Operator = Class(name="Il::Jump::Operator")
iec61131_il_Il_Fb_Call = Class(name="iec61131::il::Il::Fb::Call")
Il_Call_Operator = Class(name="Il::Call::Operator")
Operands = Class(name="Operands")
iec61131_il_Operand2 = Class(name="iec61131::il::Operand2")
Il_Param_List = Class(name="Il::Param::List")
iec61131_il_Il_Return_Operator = Class(name="iec61131::il::Il::Return::Operator")
iec61131_il_Il_Operations = Class(name="iec61131::il::Il::Operations", is_abstract=True)
iec61131_il_Il_Simple_Operator = Class(name="iec61131::il::Il::Simple::Operator")
iec61131_il_Il_Operand = Class(name="iec61131::il::Il::Operand", is_abstract=True)
iec61131_il_Il_Operand_List = Class(name="iec61131::il::Il::Operand::List")
iec61131_il_Simple_Operation1 = Class(name="iec61131::il::Simple::Operation1")
Il_Simple_Operation = Class(name="Il::Simple::Operation")
Il_Simple_Operator = Class(name="Il::Simple::Operator")
iec61131_il_Simple_Operation2 = Class(name="iec61131::il::Simple::Operation2")
Il_Operand_List = Class(name="Il::Operand::List")
iec61131_il_Il_Expr_Operator = Class(name="iec61131::il::Il::Expr::Operator")
iec61131_il_Il_Jump_Operator = Class(name="iec61131::il::Il::Jump::Operator")
iec61131_il_Il_Call_Operator = Class(name="iec61131::il::Il::Call::Operator")
iec61131_il_Il_Param_List = Class(name="iec61131::il::Il::Param::List")
Il_Param_Instruction = Class(name="Il::Param::Instruction")
Il_Param_Last_Instruction = Class(name="Il::Param::Last::Instruction")
iec61131_il_Operand1 = Class(name="iec61131::il::Operand1")
iec61131_il_Operands = Class(name="iec61131::il::Operands", is_abstract=True)
iec61131_il_Il_Simple_Instruction = Class(name="iec61131::il::Il::Simple::Instruction")
Simple_Instr = Class(name="Simple::Instr")
iec61131_il_Simple_Instr = Class(name="iec61131::il::Simple::Instr", is_abstract=True)
iec61131_il_Il_Param_Instruction = Class(name="iec61131::il::Il::Param::Instruction")
Param_Instruction = Class(name="Param::Instruction")
iec61131_il_Il_Param_Last_Instruction = Class(name="iec61131::il::Il::Param::Last::Instruction")
iec61131_il_Il_Param_Assignment = Class(name="iec61131::il::Il::Param::Assignment")
Param_Assignments = Class(name="Param::Assignments")
Il_Assign_Operator = Class(name="Il::Assign::Operator")
Sfc_Network = Class(name="Sfc::Network")
iec61131_sfc_Sfc_Network = Class(name="iec61131::sfc::Sfc::Network")
Initial_Step = Class(name="Initial::Step")
iec61131_il_Il_Param_Out_Assignment = Class(name="iec61131::il::Il::Param::Out::Assignment")
Il_Assign_Out_Operator = Class(name="Il::Assign::Out::Operator")
iec61131_il_Param_Assignments = Class(name="iec61131::il::Param::Assignments", is_abstract=True)
iec61131_il_Param_Instruction = Class(name="iec61131::il::Param::Instruction", is_abstract=True)
iec61131_il_Il_Assign_Operator = Class(name="iec61131::il::Il::Assign::Operator")
Assignment_Name = Class(name="Assignment::Name")
iec61131_il_Param_Assignment2 = Class(name="iec61131::il::Param::Assignment2")
iec61131_il_Param_Assignment = Class(name="iec61131::il::Param::Assignment", is_abstract=True)
iec61131_il_Il_Assign_Out_Operator = Class(name="iec61131::il::Il::Assign::Out::Operator")
iec61131_sfc_Sequential_Function_Chart = Class(name="iec61131::sfc::Sequential::Function::Chart")
iec61131_sfc_Step_Types = Class(name="iec61131::sfc::Step::Types", is_abstract=True)
Action_Association = Class(name="Action::Association")
Step_Name = Class(name="Step::Name")
Sfc_Elements = Class(name="Sfc::Elements")
iec61131_sfc_Initial_Step = Class(name="iec61131::sfc::Initial::Step")
Step_Types = Class(name="Step::Types")
iec61131_sfc_Step = Class(name="iec61131::sfc::Step")
sfc_Sfc_Elements = Class(name="sfc::Sfc::Elements")
sfc_Step_Types = Class(name="sfc::Step::Types")
iec61131_sfc_Transition = Class(name="iec61131::sfc::Transition")
Transition_Name = Class(name="Transition::Name")
Steps = Class(name="Steps")
Transition_Condition = Class(name="Transition::Condition")
iec61131_sfc_Action = Class(name="iec61131::sfc::Action")
Action_Name = Class(name="Action::Name")
iec61131_sfc_Sfc_Elements = Class(name="iec61131::sfc::Sfc::Elements", is_abstract=True)
iec61131_sfc_Step_Name = Class(name="iec61131::sfc::Step::Name")
iec61131_sfc_Action_Association = Class(name="iec61131::sfc::Action::Association")
Action_Qualifier = Class(name="Action::Qualifier")
Cond2_Condition = Class(name="Cond2::Condition")
iec61131_sfc_Action_Name = Class(name="iec61131::sfc::Action::Name")
iec61131_sfc_Action_Qualifier = Class(name="iec61131::sfc::Action::Qualifier")
Timed_Qualifier = Class(name="Timed::Qualifier")
Action_Time = Class(name="Action::Time")
iec61131_sfc_Timed_Qualifier = Class(name="iec61131::sfc::Timed::Qualifier")
iec61131_sfc_Action_Time = Class(name="iec61131::sfc::Action::Time", is_abstract=True)
iec61131_sfc_Transition_Name = Class(name="iec61131::sfc::Transition::Name")
iec61131_sfc_Steps = Class(name="iec61131::sfc::Steps", is_abstract=True)
iec61131_sfc_Transition_Condition = Class(name="iec61131::sfc::Transition::Condition", is_abstract=True)
iec61131_sfc_Steps1 = Class(name="iec61131::sfc::Steps1")
iec61131_sfc_Steps2 = Class(name="iec61131::sfc::Steps2")
iec61131_sfc_Transition_Cond1 = Class(name="iec61131::sfc::Transition::Cond1")
iec61131_sfc_Transition_Cond2 = Class(name="iec61131::sfc::Transition::Cond2")
iec61131_sfc_Transition_Cond3 = Class(name="iec61131::sfc::Transition::Cond3")
iec61131_sfc_Cond2_Condition = Class(name="iec61131::sfc::Cond2::Condition", is_abstract=True)
iec61131_sfc_ActionTime2 = Class(name="iec61131::sfc::ActionTime2")
iec61131_variables_Symbolic_Variable = Class(name="iec61131::variables::Symbolic::Variable", is_abstract=True)
iec61131_variables_Multi_Element_Variable = Class(name="iec61131::variables::Multi::Element::Variable", is_abstract=True)
iec61131_variables_Array_Variable = Class(name="iec61131::variables::Array::Variable")
Multi_Element_Variable = Class(name="Multi::Element::Variable")
Subscript_List = Class(name="Subscript::List")
iec61131_variables_Structured_Variable = Class(name="iec61131::variables::Structured::Variable")
iec61131_types_Date_Type_Name = Class(name="iec61131::types::Date::Type::Name")
iec61131_types_Bit_String_Type_Name = Class(name="iec61131::types::Bit::String::Type::Name")
iec61131_variables_Direct_Variable = Class(name="iec61131::variables::Direct::Variable")
variables_Variable = Class(name="variables::Variable")
iec61131_variables_Variable = Class(name="iec61131::variables::Variable", is_abstract=True)
iec61131_variables_Variable_Name = Class(name="iec61131::variables::Variable::Name")
variables_Symbolic_Variable = Class(name="variables::Symbolic::Variable")
Output_Reference = Class(name="Output::Reference")
Input_Reference = Class(name="Input::Reference")
iec61131_variables_Subscript_List = Class(name="iec61131::variables::Subscript::List")
iec61131_ld_Ladder_Diagram = Class(name="iec61131::ld::Ladder::Diagram")
iec61131_ld_Rung = Class(name="iec61131::ld::Rung")
iec61131_fbd_Function_Block_Diagram = Class(name="iec61131::fbd::Function::Block::Diagram")
Fbd_Network = Class(name="Fbd::Network")
iec61131_fbd_Fbd_Network = Class(name="iec61131::fbd::Fbd::Network")
iec61131_types_TypeLib = Class(name="iec61131::types::TypeLib")
Data_Type_Name = Class(name="Data::Type::Name")
iec61131_types_Numeric_Type_Name = Class(name="iec61131::types::Numeric::Type::Name", is_abstract=True)
Elementary_Type_Name = Class(name="Elementary::Type::Name")
iec61131_types_Integer_Type_Name = Class(name="iec61131::types::Integer::Type::Name", is_abstract=True)
Numeric_Type_Name = Class(name="Numeric::Type::Name")
iec61131_types_Real_Type_Name = Class(name="iec61131::types::Real::Type::Name")
iec61131_types_Signed_Integer_Type_Name = Class(name="iec61131::types::Signed::Integer::Type::Name")
iec61131_types_Unsigned_Integer_Type_Name = Class(name="iec61131::types::Unsigned::Integer::Type::Name")
iec61131_types_Elementary_Type_Name = Class(name="iec61131::types::Elementary::Type::Name", is_abstract=True)
types_Non_Generic_Type_Name = Class(name="types::Non::Generic::Type::Name")
interfaces_Simple_Specification_Func = Class(name="interfaces::Simple::Specification::Func")
iec61131_types_Non_Generic_Type_Name = Class(name="iec61131::types::Non::Generic::Type::Name", is_abstract=True)
types_Data_Type_Name = Class(name="types::Data::Type::Name")
pous_Function_Return_Value = Class(name="pous::Function::Return::Value")
iec61131_types_Derived_Type_Name = Class(name="iec61131::types::Derived::Type::Name", is_abstract=True)
iec61131_types_Generic_Type_Name = Class(name="iec61131::types::Generic::Type::Name")
iec61131_types_Data_Type_Name = Class(name="iec61131::types::Data::Type::Name", is_abstract=True)
iec61131_types_Bool_Type_Name = Class(name="iec61131::types::Bool::Type::Name")
iec61131_types_DT_Type_Name = Class(name="iec61131::types::DT::Type::Name")
iec61131_types_TOD_Type_Name = Class(name="iec61131::types::TOD::Type::Name")
iec61131_types_Duration_Type_Name = Class(name="iec61131::types::Duration::Type::Name")
iec61131_types_Single_Element_Type_Name = Class(name="iec61131::types::Single::Element::Type::Name", is_abstract=True)
Derived_Type_Name = Class(name="Derived::Type::Name")
iec61131_types_Array_Type_Name = Class(name="iec61131::types::Array::Type::Name")
iec61131_types_Structure_Type_Name = Class(name="iec61131::types::Structure::Type::Name")
types_Derived_Type_Name = Class(name="types::Derived::Type::Name")
iec61131_types_String_Type_Name = Class(name="iec61131::types::String::Type::Name")
iec61131_types_Simple_Type_Name = Class(name="iec61131::types::Simple::Type::Name")
types_Single_Element_Type_Name = Class(name="types::Single::Element::Type::Name")
iec61131_types_Subrange_Type_Name = Class(name="iec61131::types::Subrange::Type::Name")
Single_Element_Type_Name = Class(name="Single::Element::Type::Name")
iec61131_types_Enumerated_Type_Name = Class(name="iec61131::types::Enumerated::Type::Name")
iec61131_types_Single_Byte_String_Type_Name = Class(name="iec61131::types::Single::Byte::String::Type::Name")
iec61131_types_Double_Byte_String_Type_Name = Class(name="iec61131::types::Double::Byte::String::Type::Name")
iec61131_types_Byte_String_Type_Name = Class(name="iec61131::types::Byte::String::Type::Name", is_abstract=True)
iec61131_types_Simple_Specification = Class(name="iec61131::types::Simple::Specification", is_abstract=True)

# Commentable class attributes and methods

# NamedElement class attributes and methods

# iec61131_Commentable class attributes and methods
iec61131_Commentable_comments: Property = Property(name="comments", type=StringType)
iec61131_Commentable.attributes={iec61131_Commentable_comments}

# iec61131_NamedElement class attributes and methods
iec61131_NamedElement_name: Property = Property(name="name", type=StringType)
iec61131_NamedElement.attributes={iec61131_NamedElement_name}

# iec61131_literals_Numeric_Literal class attributes and methods

# Constant class attributes and methods

# iec61131_literals_Character_String class attributes and methods

# iec61131_IEC61131 class attributes and methods

# iec61131_Library_Element_Declaration class attributes and methods

# iec61131_Library_Element_Name class attributes and methods

# Integer_Type_Name class attributes and methods

# iec61131_literals_Real_Literal class attributes and methods
iec61131_literals_Real_Literal_exponent: Property = Property(name="exponent", type=StringType)
iec61131_literals_Real_Literal_negative: Property = Property(name="negative", type=BooleanType)
iec61131_literals_Real_Literal.attributes={iec61131_literals_Real_Literal_negative, iec61131_literals_Real_Literal_exponent}

# Real_Type_Name class attributes and methods

# Fixed_Point class attributes and methods

# iec61131_literals_Boolean_Literal class attributes and methods
iec61131_literals_Boolean_Literal_value: Property = Property(name="value", type=StringType)
iec61131_literals_Boolean_Literal.attributes={iec61131_literals_Boolean_Literal_value}

# iec61131_literals_Time_Literal class attributes and methods

# iec61131_literals_Constant class attributes and methods

# configurations_Data_Source class attributes and methods

# iec61131_literals_Bit_String_Literal class attributes and methods

# configurations_Prog_Data_Source class attributes and methods

# il_Il_Operand class attributes and methods

# BSInteger class attributes and methods

# Bit_String_Type_Name class attributes and methods

# iec61131_literals_Integer_Literal class attributes and methods

# Numeric_Literal class attributes and methods

# Integer class attributes and methods

# iec61131_literals_Hex_Integer class attributes and methods

# iec61131_literals_Duration class attributes and methods

# literals_Time_Literal class attributes and methods

# sfc_Action_Time class attributes and methods

# Interval class attributes and methods

# Duration_Type_Name class attributes and methods

# Substraction_Operator class attributes and methods

# iec61131_literals_Time_Of_Day class attributes and methods

# Time_Literal class attributes and methods

# Daytime class attributes and methods

# iec61131_literals_Signed_Integer class attributes and methods
iec61131_literals_Signed_Integer_negative: Property = Property(name="negative", type=BooleanType)
iec61131_literals_Signed_Integer.attributes={iec61131_literals_Signed_Integer_negative}

# literals_Integer class attributes and methods

# st_Case_List_Element class attributes and methods

# interfaces_Range class attributes and methods

# iec61131_literals_Binary_Integer class attributes and methods

# literals_BSInteger class attributes and methods

# iec61131_literals_Octal_Integer class attributes and methods

# iec61131_literals_Date_And_Time class attributes and methods

# DT_Type_Name class attributes and methods

# iec61131_literals_Unsigned_Integer class attributes and methods

# literals_Fixed_Point_Literal class attributes and methods

# iec61131_literals_Interval class attributes and methods

# Fixed_Point_Literal class attributes and methods

# TOD_Type_Name class attributes and methods

# iec61131_literals_Date class attributes and methods

# Date_Type_Name class attributes and methods

# Date_Literal class attributes and methods

# Minutes class attributes and methods

# iec61131_literals_Minutes class attributes and methods

# Seconds class attributes and methods

# iec61131_literals_Seconds class attributes and methods

# Milliseconds class attributes and methods

# iec61131_literals_Days class attributes and methods

# Unsigned_Integer class attributes and methods

# Hours class attributes and methods

# Double_Byte_Character_Representation class attributes and methods

# iec61131_literals_Hours class attributes and methods

# iec61131_literals_Fixed_Point_Literal class attributes and methods

# iec61131_literals_Daytime class attributes and methods
iec61131_literals_Daytime_hour: Property = Property(name="hour", type=StringType)
iec61131_literals_Daytime_minute: Property = Property(name="minute", type=StringType)
iec61131_literals_Daytime.attributes={iec61131_literals_Daytime_minute, iec61131_literals_Daytime_hour}

# iec61131_literals_Date_Literal class attributes and methods
iec61131_literals_Date_Literal_year: Property = Property(name="year", type=StringType)
iec61131_literals_Date_Literal_month: Property = Property(name="month", type=StringType)
iec61131_literals_Date_Literal_day: Property = Property(name="day", type=StringType)
iec61131_literals_Date_Literal.attributes={iec61131_literals_Date_Literal_day, iec61131_literals_Date_Literal_month, iec61131_literals_Date_Literal_year}

# iec61131_literals_BSInteger class attributes and methods

# iec61131_literals_Milliseconds class attributes and methods

# iec61131_literals_Single_Byte_Character_String class attributes and methods

# Character_String class attributes and methods

# Single_Byte_Character_Representation class attributes and methods

# iec61131_literals_Double_Byte_Character_String class attributes and methods

# iec61131_literals_Fixed_Point class attributes and methods
iec61131_literals_Fixed_Point_valuePre: Property = Property(name="valuePre", type=StringType)
iec61131_literals_Fixed_Point_valuePost: Property = Property(name="valuePost", type=StringType)
iec61131_literals_Fixed_Point.attributes={iec61131_literals_Fixed_Point_valuePost, iec61131_literals_Fixed_Point_valuePre}

# iec61131_operators_Operator class attributes and methods

# iec61131_operators_Add_Operator class attributes and methods

# Operator class attributes and methods

# iec61131_operators_Unary_Operator class attributes and methods

# iec61131_operators_Addition_Operator class attributes and methods

# iec61131_operators_Substraction_Operator class attributes and methods

# iec61131_operators_Assignment_Operator class attributes and methods

# iec61131_operators_Comparison_Operator class attributes and methods

# iec61131_literals_Integer class attributes and methods
iec61131_literals_Integer_value: Property = Property(name="value", type=StringType)
iec61131_literals_Integer.attributes={iec61131_literals_Integer_value}

# iec61131_literals_Common_Character_Representation class attributes and methods
iec61131_literals_Common_Character_Representation_value: Property = Property(name="value", type=StringType)
iec61131_literals_Common_Character_Representation.attributes={iec61131_literals_Common_Character_Representation_value}

# iec61131_literals_Single_Byte_Character_Representation class attributes and methods
iec61131_literals_Single_Byte_Character_Representation_value: Property = Property(name="value", type=StringType)
iec61131_literals_Single_Byte_Character_Representation.attributes={iec61131_literals_Single_Byte_Character_Representation_value}

# Common_Character_Representation class attributes and methods

# iec61131_literals_Double_Byte_Character_Representation class attributes and methods
iec61131_literals_Double_Byte_Character_Representation_value: Property = Property(name="value", type=StringType)
iec61131_literals_Double_Byte_Character_Representation.attributes={iec61131_literals_Double_Byte_Character_Representation_value}

# il_Il_Simple_Operator class attributes and methods

# iec61131_operators_Power_Operator class attributes and methods

# iec61131_operators_Modulo_Operator class attributes and methods

# operators_Dot_Operator class attributes and methods

# iec61131_operators_Divide_Operator class attributes and methods

# iec61131_operators_Less_Operator class attributes and methods

# Comparison_Operator class attributes and methods

# iec61131_operators_Greater_Operator class attributes and methods

# iec61131_operators_GreaterEqual_Operator class attributes and methods

# iec61131_operators_LessEqual_Operator class attributes and methods

# iec61131_operators_Unequal_Operator class attributes and methods

# iec61131_operators_Addition_Name class attributes and methods

# iec61131_operators_Multiply_Operator class attributes and methods

# Dot_Operator class attributes and methods

# iec61131_operators_Equal_Operator class attributes and methods

# EquUequ_Operator class attributes and methods

# iec61131_operators_And_Operator class attributes and methods

# operators_Operator class attributes and methods

# il_Il_Expr_Operator class attributes and methods

# iec61131_operators_Or_Operator class attributes and methods

# iec61131_operators_Xor_Operator class attributes and methods

# iec61131_operators_Not_Operator class attributes and methods

# operators_Unary_Operator class attributes and methods

# iec61131_operators_Divide_Symbol class attributes and methods

# Divide_Operator class attributes and methods

# iec61131_operators_Power_Symbol class attributes and methods

# Power_Operator class attributes and methods

# iec61131_operators_Power_Name class attributes and methods

# iec61131_operators_Assignment_Symbol class attributes and methods

# Assignment_Operator class attributes and methods

# iec61131_operators_Assignment_Name class attributes and methods

# iec61131_operators_And_Symbol class attributes and methods

# And_Operator class attributes and methods

# iec61131_operators_And_Name class attributes and methods

# iec61131_operators_Equal_Name class attributes and methods

# operators_Equal_Operator class attributes and methods

# operators_Comparison_Name class attributes and methods

# iec61131_operators_Equal_Symbol class attributes and methods

# Equal_Operator class attributes and methods

# operators_Addition_Operator class attributes and methods

# operators_Arithmetic_Name class attributes and methods

# iec61131_operators_Addition_Symbol class attributes and methods

# operators_Add_Operator class attributes and methods

# iec61131_operators_Dot_Operator class attributes and methods

# iec61131_operators_Multiply_Name class attributes and methods

# operators_Multiply_Operator class attributes and methods

# iec61131_operators_Multiply_Symbol class attributes and methods

# Multiply_Operator class attributes and methods

# iec61131_operators_Divide_Name class attributes and methods

# operators_Divide_Operator class attributes and methods

# iec61131_operators_Greater_Name class attributes and methods

# operators_Greater_Operator class attributes and methods

# iec61131_operators_Greater_Symbol class attributes and methods

# Greater_Operator class attributes and methods

# iec61131_operators_GreaterEqual_Name class attributes and methods

# operators_GreaterEqual_Operator class attributes and methods

# iec61131_operators_GreaterEqual_Symbol class attributes and methods

# GreaterEqual_Operator class attributes and methods

# iec61131_operators_Substraction_Name class attributes and methods

# operators_Substraction_Operator class attributes and methods

# iec61131_operators_Substraction_Symbol class attributes and methods

# iec61131_operators_EquUequ_Operator class attributes and methods

# iec61131_operators_Comparison_Name class attributes and methods

# Il_Expr_Operator class attributes and methods

# iec61131_operators_Unequal_Name class attributes and methods

# operators_Unequal_Operator class attributes and methods

# iec61131_operators_Unequal_Symbol class attributes and methods

# Unequal_Operator class attributes and methods

# iec61131_operators_Less_Name class attributes and methods

# operators_Less_Operator class attributes and methods

# iec61131_operators_Less_Symbol class attributes and methods

# Less_Operator class attributes and methods

# iec61131_operators_LessEqual_Name class attributes and methods

# operators_LessEqual_Operator class attributes and methods

# iec61131_operators_LessEqual_Symbol class attributes and methods

# LessEqual_Operator class attributes and methods

# iec61131_interfaces_Var_Init_Decl class attributes and methods

# Var1_List class attributes and methods

# iec61131_interfaces_Var1_Init_Decl class attributes and methods

# Var_Init_Decl class attributes and methods

# Var1_Specification class attributes and methods

# iec61131_interfaces_Edge_Declaration class attributes and methods
iec61131_interfaces_Edge_Declaration_edge: Property = Property(name="edge", type=StringType)
iec61131_interfaces_Edge_Declaration.attributes={iec61131_interfaces_Edge_Declaration_edge}

# iec61131_operators_Arithmetic_Name class attributes and methods

# iec61131_interfaces_Io_Var_Declaration class attributes and methods

# interfaces_Interface class attributes and methods

# pous_Function_Block_Vars class attributes and methods

# pous_Program_Vars class attributes and methods

# pous_Function_Vars class attributes and methods

# iec61131_interfaces_Input_Declarations class attributes and methods
iec61131_interfaces_Input_Declarations_retain: Property = Property(name="retain", type=BooleanType)
iec61131_interfaces_Input_Declarations.attributes={iec61131_interfaces_Input_Declarations_retain}

# Io_Var_Declaration class attributes and methods

# Input_Declaration class attributes and methods

# iec61131_interfaces_Subrange_Spec_Init class attributes and methods

# interfaces_Var1_Specification_Func class attributes and methods

# Subrange_Specification class attributes and methods

# Signed_Integer class attributes and methods

# iec61131_interfaces_Enumerated_Spec_Init class attributes and methods

# Enumerated_Specification class attributes and methods

# Bool_Type_Name class attributes and methods

# iec61131_interfaces_Var1_Specification class attributes and methods

# Assignment_Symbol class attributes and methods

# iec61131_interfaces_Simple_Spec_Init class attributes and methods

# interfaces_Var1_Specification class attributes and methods

# interfaces_Located_Var_Spec_Init class attributes and methods

# pous_Structure_Elements class attributes and methods

# Simple_Specification class attributes and methods

# iec61131_interfaces_Fb_Name_Decl class attributes and methods

# Temp_Var_Declaration class attributes and methods

# Structure_Initialization class attributes and methods

# Function_Block_Type_Name class attributes and methods

# iec61131_interfaces_String_Var_Declaration class attributes and methods

# interfaces_Temp_Var_Decl class attributes and methods

# interfaces_Var2_Init_Decl class attributes and methods

# iec61131_interfaces_Output_Declarations class attributes and methods
iec61131_interfaces_Output_Declarations_retain: Property = Property(name="retain", type=BooleanType)
iec61131_interfaces_Output_Declarations.attributes={iec61131_interfaces_Output_Declarations_retain}

# Enumerated_Value class attributes and methods

# iec61131_interfaces_Array_Var_Init_Decl class attributes and methods

# Var2_Init_Decl class attributes and methods

# Array_Spec_Init class attributes and methods

# iec61131_interfaces_Structured_Var_Init_Decl class attributes and methods

# Initialized_Structure class attributes and methods

# Array_Initialization class attributes and methods

# Array_Specification class attributes and methods

# iec61131_interfaces_Initialized_Structure class attributes and methods

# pous_Structure_Specification class attributes and methods

# Structure_Type_Name class attributes and methods

# iec61131_interfaces_Input_Output_Declarations class attributes and methods

# Var_Declaration class attributes and methods

# iec61131_interfaces_Array_Spec_Init class attributes and methods

# Initial_Element class attributes and methods

# iec61131_interfaces_Structure_Element_Name class attributes and methods
iec61131_interfaces_Structure_Element_Name_name: Property = Property(name="name", type=StringType)
iec61131_interfaces_Structure_Element_Name.attributes={iec61131_interfaces_Structure_Element_Name_name}

# iec61131_interfaces_Enumerated_Value class attributes and methods
iec61131_interfaces_Enumerated_Value_name: Property = Property(name="name", type=StringType)
iec61131_interfaces_Enumerated_Value.attributes={iec61131_interfaces_Enumerated_Value_name}

# Enumerated_Type_Name class attributes and methods

# iec61131_interfaces_Array_Initialization class attributes and methods

# Array_Initial_Elements class attributes and methods

# iec61131_interfaces_Var_Declaration class attributes and methods

# iec61131_interfaces_Temp_Var_Decl class attributes and methods

# iec61131_interfaces_Structure_Initialization class attributes and methods

# Structure_Element_Initialization class attributes and methods

# iec61131_interfaces_Structure_Element_Initialization class attributes and methods

# Structure_Element_Name class attributes and methods

# iec61131_interfaces_Array_Var_Declaration class attributes and methods

# iec61131_interfaces_Structured_Var_Declaration class attributes and methods

# iec61131_interfaces_Specification class attributes and methods

# iec61131_interfaces_Subrange_Specification class attributes and methods

# interfaces_Specification class attributes and methods

# interfaces_External_Specification class attributes and methods

# iec61131_interfaces_Var1_Declaration class attributes and methods

# Specification class attributes and methods

# Range class attributes and methods

# iec61131_interfaces_Double_Byte_String_Spec class attributes and methods

# interfaces_Var_Spec class attributes and methods

# Double_Byte_Character_String class attributes and methods

# iec61131_interfaces_Enumerated_Specification class attributes and methods

# iec61131_interfaces_Single_Byte_String_Var_Declaration class attributes and methods

# String_Var_Declaration class attributes and methods

# iec61131_interfaces_Array_Specification class attributes and methods

# Single_Byte_String_Spec class attributes and methods

# iec61131_interfaces_Array_Initial_Elements class attributes and methods

# iec61131_interfaces_Double_Byte_String_Var_Declaration class attributes and methods

# iec61131_interfaces_Subrange class attributes and methods
iec61131_interfaces_Subrange_delimiter: Property = Property(name="delimiter", type=StringType)
iec61131_interfaces_Subrange.attributes={iec61131_interfaces_Subrange_delimiter}

# Case_List_Element class attributes and methods

# Double_Byte_String_Spec class attributes and methods

# iec61131_interfaces_Single_Byte_String_Spec class attributes and methods

# Located_Var_Spec_Init class attributes and methods

# Single_Byte_Character_String class attributes and methods

# Single_BString class attributes and methods

# iec61131_interfaces_Interface class attributes and methods

# Double_BString class attributes and methods

# iec61131_interfaces_Var1_List class attributes and methods

# Variable_Name class attributes and methods

# iec61131_interfaces_Other_Var_Declaration class attributes and methods

# iec61131_interfaces_External_Var_Declarations class attributes and methods
iec61131_interfaces_External_Var_Declarations_constant: Property = Property(name="constant", type=BooleanType)
iec61131_interfaces_External_Var_Declarations.attributes={iec61131_interfaces_External_Var_Declarations_constant}

# Other_Var_Declaration class attributes and methods

# External_Declaration class attributes and methods

# iec61131_interfaces_Retentive_Var_Declarations class attributes and methods

# RNV_Declarations class attributes and methods

# iec61131_interfaces_Non_Retentive_Var_Declarations class attributes and methods

# iec61131_interfaces_External_Declaration class attributes and methods

# Global_Var_Name class attributes and methods

# External_Specification class attributes and methods

# iec61131_interfaces_Global_Var_Name class attributes and methods

# Library_Element_Name class attributes and methods

# iec61131_interfaces_Global_Var_List class attributes and methods

# Global_Var_Spec class attributes and methods

# iec61131_interfaces_Temp_Var_Decls class attributes and methods

# Temp_Var_Decl class attributes and methods

# iec61131_interfaces_Var_Declarations class attributes and methods
iec61131_interfaces_Var_Declarations_constant: Property = Property(name="constant", type=BooleanType)
iec61131_interfaces_Var_Declarations.attributes={iec61131_interfaces_Var_Declarations_constant}

# iec61131_interfaces_Incompl_Location class attributes and methods
iec61131_interfaces_Incompl_Location_location: Property = Property(name="location", type=StringType)
iec61131_interfaces_Incompl_Location.attributes={iec61131_interfaces_Incompl_Location_location}

# iec61131_interfaces_Incompl_Located_Var_Declarations class attributes and methods
iec61131_interfaces_Incompl_Located_Var_Declarations_retain: Property = Property(name="retain", type=BooleanType)
iec61131_interfaces_Incompl_Located_Var_Declarations.attributes={iec61131_interfaces_Incompl_Located_Var_Declarations_retain}

# Incompl_Located_Var_Decl class attributes and methods

# iec61131_interfaces_RNV_Declarations class attributes and methods

# iec61131_interfaces_Incompl_Located_Var_Decl class attributes and methods

# Incompl_Location class attributes and methods

# Var_Spec class attributes and methods

# Located_Var_Decl class attributes and methods

# iec61131_interfaces_Var_Spec class attributes and methods

# iec61131_interfaces_External_Specification class attributes and methods

# iec61131_interfaces_Located_Var_Spec_Init class attributes and methods

# iec61131_interfaces_Location class attributes and methods

# Direct_Variable class attributes and methods

# iec61131_interfaces_Located_Var_Decl class attributes and methods

# Location class attributes and methods

# iec61131_interfaces_Located_Var_Declarations class attributes and methods
iec61131_interfaces_Located_Var_Declarations_constant: Property = Property(name="constant", type=BooleanType)
iec61131_interfaces_Located_Var_Declarations_retain: Property = Property(name="retain", type=BooleanType)
iec61131_interfaces_Located_Var_Declarations.attributes={iec61131_interfaces_Located_Var_Declarations_constant, iec61131_interfaces_Located_Var_Declarations_retain}

# Program_Vars class attributes and methods

# iec61131_interfaces_Global_Var_Declarations class attributes and methods
iec61131_interfaces_Global_Var_Declarations_constant: Property = Property(name="constant", type=BooleanType)
iec61131_interfaces_Global_Var_Declarations_retain: Property = Property(name="retain", type=BooleanType)
iec61131_interfaces_Global_Var_Declarations.attributes={iec61131_interfaces_Global_Var_Declarations_retain, iec61131_interfaces_Global_Var_Declarations_constant}

# Library_Element_Declaration class attributes and methods

# Global_Var_Decl class attributes and methods

# iec61131_interfaces_Global_Var_Decl class attributes and methods

# iec61131_interfaces_Global_Var_Spec class attributes and methods

# iec61131_interfaces_Global_Var_Location class attributes and methods

# iec61131_interfaces_Subrange_Specification2 class attributes and methods

# iec61131_interfaces_Input_Declaration class attributes and methods

# iec61131_interfaces_Range class attributes and methods

# iec61131_interfaces_Byte_String class attributes and methods

# iec61131_interfaces_Single_BString class attributes and methods

# Byte_String class attributes and methods

# Single_Byte_String_Type_Name class attributes and methods

# iec61131_interfaces_Double_BString class attributes and methods

# Double_Byte_String_Type_Name class attributes and methods

# iec61131_interfaces_Subrange_Specification1 class attributes and methods

# Subrange class attributes and methods

# iec61131_interfaces_Array_Initial_Elements1 class attributes and methods

# Subrange_Type_Name class attributes and methods

# iec61131_interfaces_Enumerated_Specification1 class attributes and methods

# iec61131_interfaces_Enumerated_Specification2 class attributes and methods

# iec61131_interfaces_Array_Specification1 class attributes and methods

# Array_Type_Name class attributes and methods

# iec61131_interfaces_Array_Specification2 class attributes and methods

# Non_Generic_Type_Name class attributes and methods

# iec61131_interfaces_Array_Initial_Elements2 class attributes and methods

# iec61131_interfaces_Initial_Element class attributes and methods

# iec61131_interfaces_InitElement_Constant class attributes and methods

# iec61131_interfaces_InitElement_EnumValue class attributes and methods

# iec61131_interfaces_InitElement_Structure class attributes and methods

# iec61131_interfaces_InitElement_Array class attributes and methods

# iec61131_interfaces_Var2_Init_Decl class attributes and methods

# iec61131_interfaces_Function_Var_Decl class attributes and methods
iec61131_interfaces_Function_Var_Decl_constant: Property = Property(name="constant", type=BooleanType)
iec61131_interfaces_Function_Var_Decl.attributes={iec61131_interfaces_Function_Var_Decl_constant}

# iec61131_interfaces_Simple_Specification_Func class attributes and methods

# iec61131_interfaces_Var1_Specification_Func class attributes and methods

# iec61131_interfaces_Var_Name_Decl class attributes and methods

# Simple_Spec_Init class attributes and methods

# iec61131_interfaces_Var_Init_Decl_Func class attributes and methods

# Var1_Specification_Func class attributes and methods

# iec61131_interfaces_Simple_Spec_Init_Func class attributes and methods

# Simple_Specification_Func class attributes and methods

# pous_Function_Block_Type_Name class attributes and methods

# iec61131_pous_Function_Block_Declaration class attributes and methods

# iec61131_interfaces_Temp_Var_Declaration class attributes and methods

# iec61131_pous_Program_Declaration class attributes and methods

# Program_Type_Name class attributes and methods

# Function_Block_Body class attributes and methods

# iec61131_pous_Program_Type_Name class attributes and methods

# Blocks class attributes and methods

# iec61131_pous_Function_Block_Type_Name class attributes and methods

# types_Simple_Specification class attributes and methods

# iec61131_pous_Derived_Function_Block_Name class attributes and methods

# Derived_Function_Block_Name class attributes and methods

# Function_Block_Vars class attributes and methods

# iec61131_pous_Function_Declaration class attributes and methods

# Derived_Function_Name class attributes and methods

# Function_Return_Value class attributes and methods

# Function_Vars class attributes and methods

# Function_Body class attributes and methods

# iec61131_pous_Access_Name class attributes and methods
iec61131_pous_Access_Name_name: Property = Property(name="name", type=StringType)
iec61131_pous_Access_Name.attributes={iec61131_pous_Access_Name_name}

# iec61131_pous_Derived_Function_Name class attributes and methods

# pous_Function_Name class attributes and methods

# iec61131_pous_Function_Return_Value class attributes and methods

# iec61131_pous_Function_Body class attributes and methods

# iec61131_pous_Other_Language class attributes and methods
iec61131_pous_Other_Language_text: Property = Property(name="text", type=StringType)
iec61131_pous_Other_Language.attributes={iec61131_pous_Other_Language_text}

# pous_Function_Body class attributes and methods

# pous_Function_Block_Body class attributes and methods

# iec61131_pous_Function_Block_Body class attributes and methods

# iec61131_pous_Program_Access_Decl class attributes and methods
iec61131_pous_Program_Access_Decl_direction: Property = Property(name="direction", type=StringType)
iec61131_pous_Program_Access_Decl.attributes={iec61131_pous_Program_Access_Decl_direction}

# Access_Name class attributes and methods

# Symbolic_Variable class attributes and methods

# iec61131_pous_Function_Name class attributes and methods

# iec61131_pous_Data_Type_Declaration class attributes and methods

# Type_Declaration class attributes and methods

# iec61131_pous_Type_Declaration class attributes and methods

# iec61131_pous_Single_Element_Type_Declaration class attributes and methods

# iec61131_pous_Array_Type_Declaration class attributes and methods

# iec61131_pous_Structure_Type_Declaration class attributes and methods

# Structure_Specification class attributes and methods

# iec61131_pous_String_Type_Declaration class attributes and methods

# String_Type_Name class attributes and methods

# Byte_String_Type_Name class attributes and methods

# Program_Access_Decl class attributes and methods

# iec61131_pous_Library class attributes and methods

# Program_Declaration class attributes and methods

# Function_Declaration class attributes and methods

# iec61131_pous_Simple_Type_Declaration class attributes and methods

# Single_Element_Type_Declaration class attributes and methods

# Simple_Type_Name class attributes and methods

# iec61131_pous_Subrange_Type_Declaration class attributes and methods

# Subrange_Spec_Init class attributes and methods

# iec61131_pous_Enumerated_Type_Declaration class attributes and methods

# Enumerated_Spec_Init class attributes and methods

# iec61131_pous_Structure_Specification class attributes and methods

# iec61131_pous_Structure_Declaration class attributes and methods

# Structure_Element_Declaration class attributes and methods

# iec61131_pous_Structure_Element_Declaration class attributes and methods

# Structure_Elements class attributes and methods

# iec61131_pous_Structure_Elements class attributes and methods

# iec61131_pous_Program_Vars class attributes and methods

# iec61131_pous_Function_Vars class attributes and methods

# iec61131_pous_Function_Block_Vars class attributes and methods

# iec61131_pous_Program_Access_Decls class attributes and methods

# Resource_Name class attributes and methods

# Function_Block_Declaration class attributes and methods

# iec61131_configurations_Configuration_Name class attributes and methods

# iec61131_configurations_Resource_Type_Name class attributes and methods

# iec61131_configurations_Configuration_Declaration class attributes and methods

# Configuration_Name class attributes and methods

# Single_Resource_Declaration class attributes and methods

# Global_Var_Declarations class attributes and methods

# Instance_Specific_Initializations class attributes and methods

# Access_Declarations class attributes and methods

# Resource_Declaration class attributes and methods

# iec61131_configurations_Resource_Name class attributes and methods
iec61131_configurations_Resource_Name_name: Property = Property(name="name", type=StringType)
iec61131_configurations_Resource_Name.attributes={iec61131_configurations_Resource_Name_name}

# iec61131_configurations_Resource_Declaration class attributes and methods

# Resource_Type_Name class attributes and methods

# iec61131_configurations_Single_Resource_Declaration class attributes and methods

# Task_Configuration class attributes and methods

# Program_Configuration class attributes and methods

# iec61131_configurations_Task_Configuration class attributes and methods

# Task_Name class attributes and methods

# Priority class attributes and methods

# Single class attributes and methods

# iec61131_configurations_Program_Configuration class attributes and methods
iec61131_configurations_Program_Configuration_retain: Property = Property(name="retain", type=BooleanType)
iec61131_configurations_Program_Configuration.attributes={iec61131_configurations_Program_Configuration_retain}

# Program_Name class attributes and methods

# iec61131_configurations_Access_Name class attributes and methods
iec61131_configurations_Access_Name_name: Property = Property(name="name", type=StringType)
iec61131_configurations_Access_Name.attributes={iec61131_configurations_Access_Name_name}

# Prog_Conf_Elements class attributes and methods

# iec61131_configurations_Instance_Specific_Initializations class attributes and methods

# Instance_Specific_Init class attributes and methods

# iec61131_configurations_Data_Source class attributes and methods

# iec61131_configurations_Global_Var_Reference class attributes and methods

# configurations_Data_Sink class attributes and methods

# iec61131_configurations_Program_Output_Reference class attributes and methods

# Data_Source class attributes and methods

# iec61131_configurations_Access_Declarations class attributes and methods

# Access_Declaration class attributes and methods

# iec61131_configurations_Access_Declaration class attributes and methods
iec61131_configurations_Access_Declaration_direction: Property = Property(name="direction", type=StringType)
iec61131_configurations_Access_Declaration.attributes={iec61131_configurations_Access_Declaration_direction}

# Access_Path class attributes and methods

# iec61131_configurations_Prog_Cnxn class attributes and methods

# iec61131_configurations_Access_Path class attributes and methods

# iec61131_configurations_Direct_Path class attributes and methods

# iec61131_configurations_Symbolic_Path class attributes and methods

# iec61131_configurations_Program_Name class attributes and methods
iec61131_configurations_Program_Name_name: Property = Property(name="name", type=StringType)
iec61131_configurations_Program_Name.attributes={iec61131_configurations_Program_Name_name}

# iec61131_configurations_Task_Name class attributes and methods
iec61131_configurations_Task_Name_name: Property = Property(name="name", type=StringType)
iec61131_configurations_Task_Name.attributes={iec61131_configurations_Task_Name_name}

# iec61131_configurations_Task_Initialization class attributes and methods

# iec61131_configurations_Prog_Conf_Elements class attributes and methods

# Prog_Conf_Element class attributes and methods

# iec61131_configurations_Prog_Conf_Element class attributes and methods

# iec61131_configurations_Fb_Task class attributes and methods

# iec61131_configurations_Prog_Data_Source class attributes and methods

# iec61131_configurations_Prog_Sink class attributes and methods

# Prog_Cnxn class attributes and methods

# Data_Sink class attributes and methods

# iec61131_configurations_Prog_Source class attributes and methods

# Prog_Data_Source class attributes and methods

# iec61131_configurations_Data_Sink class attributes and methods

# iec61131_configurations_Instance_Specific_Init class attributes and methods

# iec61131_configurations_Instance_Spec1 class attributes and methods

# iec61131_configurations_Instance_Spec2 class attributes and methods

# iec61131_st_Subprogram_Control_Statement class attributes and methods

# iec61131_st_Selection_Statement class attributes and methods

# iec61131_configurations_Single class attributes and methods

# Task_Initialization class attributes and methods

# iec61131_configurations_Interval class attributes and methods

# iec61131_configurations_Priority class attributes and methods

# iec61131_st_Statement_List class attributes and methods

# Statement class attributes and methods

# iec61131_st_Expression class attributes and methods

# Expression_Types class attributes and methods

# Or_Operator class attributes and methods

# iec61131_st_Statement class attributes and methods

# iec61131_st_Assignment_Statement class attributes and methods

# Expression_Variable class attributes and methods

# Else_Statement class attributes and methods

# iec61131_st_Case_Statement class attributes and methods

# iec61131_st_Iteration_Statement class attributes and methods

# iec61131_st_Return_Statement class attributes and methods

# Subprogram_Control_Statement class attributes and methods

# iec61131_st_Fb_Invocation class attributes and methods

# Param_Assignment class attributes and methods

# iec61131_st_Param_Assignment class attributes and methods

# iec61131_st_Param_Type1 class attributes and methods

# iec61131_st_Param_Type2 class attributes and methods

# Variable class attributes and methods

# Not_Operator class attributes and methods

# iec61131_st_If_Statement class attributes and methods

# Selection_Statement class attributes and methods

# Statement_List class attributes and methods

# Else_If_Statement class attributes and methods

# iec61131_st_While_Statement class attributes and methods

# Case_Element class attributes and methods

# iec61131_st_Else_If_Statement class attributes and methods

# iec61131_st_Else_Statement class attributes and methods

# iec61131_st_Case_Element class attributes and methods

# Case_List class attributes and methods

# iec61131_st_Case_List class attributes and methods

# iec61131_st_Case_List_Element class attributes and methods

# iec61131_st_For_Statement class attributes and methods

# Iteration_Statement class attributes and methods

# Control_Variable class attributes and methods

# For_List class attributes and methods

# iec61131_st_Repeat_Statement class attributes and methods

# iec61131_st_Exit_Statement class attributes and methods

# iec61131_st_Control_Variable class attributes and methods
iec61131_st_Control_Variable_name: Property = Property(name="name", type=StringType)
iec61131_st_Control_Variable.attributes={iec61131_st_Control_Variable_name}

# iec61131_st_For_List class attributes and methods

# iec61131_st_Xor_Expression class attributes and methods

# Xor_Operator class attributes and methods

# iec61131_st_And_Expression class attributes and methods

# iec61131_st_Comparison class attributes and methods

# iec61131_st_Equ_Expression class attributes and methods

# iec61131_st_Add_Expression class attributes and methods

# iec61131_st_Primary_Expression class attributes and methods

# Add_Operator class attributes and methods

# iec61131_st_Term_Expression class attributes and methods

# iec61131_st_Power_Expression class attributes and methods

# Power_Symbol class attributes and methods

# iec61131_st_Unary_Expression class attributes and methods

# Unary_Operator class attributes and methods

# iec61131_il_Instruction_List class attributes and methods

# Il_Instruction class attributes and methods

# iec61131_st_Bracket_Expression class attributes and methods

# Primary_Expression class attributes and methods

# iec61131_st_Call_Expression class attributes and methods

# Function_Name class attributes and methods

# iec61131_st_Expression_Types class attributes and methods

# iec61131_st_Expression_Variable class attributes and methods

# Array_Variable class attributes and methods

# Structured_Variable class attributes and methods

# iec61131_st_Expression_Constant class attributes and methods

# iec61131_st_Expression_EnumValue class attributes and methods

# iec61131_st_Expression_Variable_Type class attributes and methods

# iec61131_il_Il_Formal_Funct_Call class attributes and methods

# iec61131_il_Simple_Instr_List class attributes and methods

# Il_Simple_Instruction class attributes and methods

# iec61131_il_Il_Instruction class attributes and methods

# Label class attributes and methods

# Il_Operations class attributes and methods

# iec61131_il_Label class attributes and methods
iec61131_il_Label_label: Property = Property(name="label", type=StringType)
iec61131_il_Label.attributes={iec61131_il_Label_label}

# iec61131_il_Il_Simple_Operation class attributes and methods

# il_Il_Operations class attributes and methods

# il_Simple_Instr class attributes and methods

# iec61131_il_Il_Expression class attributes and methods

# Il_Operand class attributes and methods

# Simple_Instr_List class attributes and methods

# iec61131_il_Il_Jump_Operation class attributes and methods

# Il_Jump_Operator class attributes and methods

# iec61131_il_Il_Fb_Call class attributes and methods

# Il_Call_Operator class attributes and methods

# Operands class attributes and methods

# iec61131_il_Operand2 class attributes and methods

# Il_Param_List class attributes and methods

# iec61131_il_Il_Return_Operator class attributes and methods

# iec61131_il_Il_Operations class attributes and methods

# iec61131_il_Il_Simple_Operator class attributes and methods

# iec61131_il_Il_Operand class attributes and methods

# iec61131_il_Il_Operand_List class attributes and methods

# iec61131_il_Simple_Operation1 class attributes and methods

# Il_Simple_Operation class attributes and methods

# Il_Simple_Operator class attributes and methods

# iec61131_il_Simple_Operation2 class attributes and methods

# Il_Operand_List class attributes and methods

# iec61131_il_Il_Expr_Operator class attributes and methods

# iec61131_il_Il_Jump_Operator class attributes and methods

# iec61131_il_Il_Call_Operator class attributes and methods

# iec61131_il_Il_Param_List class attributes and methods

# Il_Param_Instruction class attributes and methods

# Il_Param_Last_Instruction class attributes and methods

# iec61131_il_Operand1 class attributes and methods

# iec61131_il_Operands class attributes and methods

# iec61131_il_Il_Simple_Instruction class attributes and methods

# Simple_Instr class attributes and methods

# iec61131_il_Simple_Instr class attributes and methods

# iec61131_il_Il_Param_Instruction class attributes and methods

# Param_Instruction class attributes and methods

# iec61131_il_Il_Param_Last_Instruction class attributes and methods

# iec61131_il_Il_Param_Assignment class attributes and methods

# Param_Assignments class attributes and methods

# Il_Assign_Operator class attributes and methods

# Sfc_Network class attributes and methods

# iec61131_sfc_Sfc_Network class attributes and methods

# Initial_Step class attributes and methods

# iec61131_il_Il_Param_Out_Assignment class attributes and methods

# Il_Assign_Out_Operator class attributes and methods

# iec61131_il_Param_Assignments class attributes and methods

# iec61131_il_Param_Instruction class attributes and methods

# iec61131_il_Il_Assign_Operator class attributes and methods

# Assignment_Name class attributes and methods

# iec61131_il_Param_Assignment2 class attributes and methods

# iec61131_il_Param_Assignment class attributes and methods

# iec61131_il_Il_Assign_Out_Operator class attributes and methods

# iec61131_sfc_Sequential_Function_Chart class attributes and methods

# iec61131_sfc_Step_Types class attributes and methods

# Action_Association class attributes and methods

# Step_Name class attributes and methods

# Sfc_Elements class attributes and methods

# iec61131_sfc_Initial_Step class attributes and methods

# Step_Types class attributes and methods

# iec61131_sfc_Step class attributes and methods

# sfc_Sfc_Elements class attributes and methods

# sfc_Step_Types class attributes and methods

# iec61131_sfc_Transition class attributes and methods

# Transition_Name class attributes and methods

# Steps class attributes and methods

# Transition_Condition class attributes and methods

# iec61131_sfc_Action class attributes and methods

# Action_Name class attributes and methods

# iec61131_sfc_Sfc_Elements class attributes and methods

# iec61131_sfc_Step_Name class attributes and methods

# iec61131_sfc_Action_Association class attributes and methods

# Action_Qualifier class attributes and methods

# Cond2_Condition class attributes and methods

# iec61131_sfc_Action_Name class attributes and methods
iec61131_sfc_Action_Name_name: Property = Property(name="name", type=StringType)
iec61131_sfc_Action_Name.attributes={iec61131_sfc_Action_Name_name}

# iec61131_sfc_Action_Qualifier class attributes and methods
iec61131_sfc_Action_Qualifier_qualifier: Property = Property(name="qualifier", type=StringType)
iec61131_sfc_Action_Qualifier.attributes={iec61131_sfc_Action_Qualifier_qualifier}

# Timed_Qualifier class attributes and methods

# Action_Time class attributes and methods

# iec61131_sfc_Timed_Qualifier class attributes and methods
iec61131_sfc_Timed_Qualifier_qualifier: Property = Property(name="qualifier", type=StringType)
iec61131_sfc_Timed_Qualifier.attributes={iec61131_sfc_Timed_Qualifier_qualifier}

# iec61131_sfc_Action_Time class attributes and methods

# iec61131_sfc_Transition_Name class attributes and methods
iec61131_sfc_Transition_Name_name: Property = Property(name="name", type=StringType)
iec61131_sfc_Transition_Name.attributes={iec61131_sfc_Transition_Name_name}

# iec61131_sfc_Steps class attributes and methods

# iec61131_sfc_Transition_Condition class attributes and methods

# iec61131_sfc_Steps1 class attributes and methods

# iec61131_sfc_Steps2 class attributes and methods

# iec61131_sfc_Transition_Cond1 class attributes and methods

# iec61131_sfc_Transition_Cond2 class attributes and methods

# iec61131_sfc_Transition_Cond3 class attributes and methods

# iec61131_sfc_Cond2_Condition class attributes and methods

# iec61131_sfc_ActionTime2 class attributes and methods

# iec61131_variables_Symbolic_Variable class attributes and methods

# iec61131_variables_Multi_Element_Variable class attributes and methods

# iec61131_variables_Array_Variable class attributes and methods

# Multi_Element_Variable class attributes and methods

# Subscript_List class attributes and methods

# iec61131_variables_Structured_Variable class attributes and methods

# iec61131_types_Date_Type_Name class attributes and methods

# iec61131_types_Bit_String_Type_Name class attributes and methods

# iec61131_variables_Direct_Variable class attributes and methods
iec61131_variables_Direct_Variable_value: Property = Property(name="value", type=StringType)
iec61131_variables_Direct_Variable.attributes={iec61131_variables_Direct_Variable_value}

# variables_Variable class attributes and methods

# iec61131_variables_Variable class attributes and methods

# iec61131_variables_Variable_Name class attributes and methods

# variables_Symbolic_Variable class attributes and methods

# Output_Reference class attributes and methods

# Input_Reference class attributes and methods

# iec61131_variables_Subscript_List class attributes and methods

# iec61131_ld_Ladder_Diagram class attributes and methods

# iec61131_ld_Rung class attributes and methods

# iec61131_fbd_Function_Block_Diagram class attributes and methods

# Fbd_Network class attributes and methods

# iec61131_fbd_Fbd_Network class attributes and methods

# iec61131_types_TypeLib class attributes and methods

# Data_Type_Name class attributes and methods

# iec61131_types_Numeric_Type_Name class attributes and methods

# Elementary_Type_Name class attributes and methods

# iec61131_types_Integer_Type_Name class attributes and methods

# Numeric_Type_Name class attributes and methods

# iec61131_types_Real_Type_Name class attributes and methods

# iec61131_types_Signed_Integer_Type_Name class attributes and methods

# iec61131_types_Unsigned_Integer_Type_Name class attributes and methods

# iec61131_types_Elementary_Type_Name class attributes and methods

# types_Non_Generic_Type_Name class attributes and methods

# interfaces_Simple_Specification_Func class attributes and methods

# iec61131_types_Non_Generic_Type_Name class attributes and methods

# types_Data_Type_Name class attributes and methods

# pous_Function_Return_Value class attributes and methods

# iec61131_types_Derived_Type_Name class attributes and methods

# iec61131_types_Generic_Type_Name class attributes and methods

# iec61131_types_Data_Type_Name class attributes and methods

# iec61131_types_Bool_Type_Name class attributes and methods

# iec61131_types_DT_Type_Name class attributes and methods

# iec61131_types_TOD_Type_Name class attributes and methods

# iec61131_types_Duration_Type_Name class attributes and methods

# iec61131_types_Single_Element_Type_Name class attributes and methods

# Derived_Type_Name class attributes and methods

# iec61131_types_Array_Type_Name class attributes and methods

# iec61131_types_Structure_Type_Name class attributes and methods

# types_Derived_Type_Name class attributes and methods

# iec61131_types_String_Type_Name class attributes and methods

# iec61131_types_Simple_Type_Name class attributes and methods

# types_Single_Element_Type_Name class attributes and methods

# iec61131_types_Subrange_Type_Name class attributes and methods

# Single_Element_Type_Name class attributes and methods

# iec61131_types_Enumerated_Type_Name class attributes and methods

# iec61131_types_Single_Byte_String_Type_Name class attributes and methods

# iec61131_types_Double_Byte_String_Type_Name class attributes and methods

# iec61131_types_Byte_String_Type_Name class attributes and methods

# iec61131_types_Simple_Specification class attributes and methods

# Relationships
library_element_declaration0: BinaryAssociation = BinaryAssociation(
    name="library_element_declaration0",
    ends={
        Property(name="iec61131_Library_Element_Declaration", type=iec61131_IEC61131, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_IEC61131", type=iec61131_Library_Element_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
library_element_name1: BinaryAssociation = BinaryAssociation(
    name="library_element_name1",
    ends={
        Property(name="iec61131_Library_Element_Name", type=iec61131_IEC61131, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_IEC611312", type=iec61131_Library_Element_Name, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
integer_type_name7: BinaryAssociation = BinaryAssociation(
    name="integer_type_name7",
    ends={
        Property(name="Integer_Type_Name", type=iec61131_literals_Integer_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Integer_Literal8", type=Integer_Type_Name, multiplicity=Multiplicity(0, 1))
    }
)
real_type_name9: BinaryAssociation = BinaryAssociation(
    name="real_type_name9",
    ends={
        Property(name="Real_Type_Name", type=iec61131_literals_Real_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Real_Literal", type=Real_Type_Name, multiplicity=Multiplicity(0, 1))
    }
)
fixed_point10: BinaryAssociation = BinaryAssociation(
    name="fixed_point10",
    ends={
        Property(name="Fixed_Point", type=iec61131_literals_Real_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Real_Literal11", type=Fixed_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
integer3: BinaryAssociation = BinaryAssociation(
    name="integer3",
    ends={
        Property(name="BSInteger", type=iec61131_literals_Bit_String_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Bit_String_Literal", type=BSInteger, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bit_string_type4: BinaryAssociation = BinaryAssociation(
    name="bit_string_type4",
    ends={
        Property(name="Bit_String_Type_Name", type=iec61131_literals_Bit_String_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Bit_String_Literal5", type=Bit_String_Type_Name, multiplicity=Multiplicity(0, 1))
    }
)
integer6: BinaryAssociation = BinaryAssociation(
    name="integer6",
    ends={
        Property(name="Integer", type=iec61131_literals_Integer_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Integer_Literal", type=Integer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
interval12: BinaryAssociation = BinaryAssociation(
    name="interval12",
    ends={
        Property(name="Interval", type=iec61131_literals_Duration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Duration", type=Interval, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
duration_type_name13: BinaryAssociation = BinaryAssociation(
    name="duration_type_name13",
    ends={
        Property(name="Duration_Type_Name", type=iec61131_literals_Duration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Duration14", type=Duration_Type_Name, multiplicity=Multiplicity(1, 1))
    }
)
substraction15: BinaryAssociation = BinaryAssociation(
    name="substraction15",
    ends={
        Property(name="Substraction_Operator", type=iec61131_literals_Duration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Duration16", type=Substraction_Operator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
date_literal21: BinaryAssociation = BinaryAssociation(
    name="date_literal21",
    ends={
        Property(name="iec61131_literals_Date22", type=Date_Literal, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Date_Literal", type=iec61131_literals_Date, multiplicity=Multiplicity(1, 1))
    }
)
dt_type_name23: BinaryAssociation = BinaryAssociation(
    name="dt_type_name23",
    ends={
        Property(name="DT_Type_Name", type=iec61131_literals_Date_And_Time, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Date_And_Time", type=DT_Type_Name, multiplicity=Multiplicity(1, 1))
    }
)
date_literal24: BinaryAssociation = BinaryAssociation(
    name="date_literal24",
    ends={
        Property(name="Date_Literal26", type=iec61131_literals_Date_And_Time, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Date_And_Time25", type=Date_Literal, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
daytime27: BinaryAssociation = BinaryAssociation(
    name="daytime27",
    ends={
        Property(name="Daytime29", type=iec61131_literals_Date_And_Time, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Date_And_Time28", type=Daytime, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fixed_point30: BinaryAssociation = BinaryAssociation(
    name="fixed_point30",
    ends={
        Property(name="Fixed_Point_Literal", type=iec61131_literals_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Interval", type=Fixed_Point_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
daytime17: BinaryAssociation = BinaryAssociation(
    name="daytime17",
    ends={
        Property(name="Daytime", type=iec61131_literals_Time_Of_Day, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Time_Of_Day", type=Daytime, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tod_type_name18: BinaryAssociation = BinaryAssociation(
    name="tod_type_name18",
    ends={
        Property(name="TOD_Type_Name", type=iec61131_literals_Time_Of_Day, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Time_Of_Day19", type=TOD_Type_Name, multiplicity=Multiplicity(1, 1))
    }
)
date_type_name20: BinaryAssociation = BinaryAssociation(
    name="date_type_name20",
    ends={
        Property(name="Date_Type_Name", type=iec61131_literals_Date, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Date", type=Date_Type_Name, multiplicity=Multiplicity(1, 1))
    }
)
minutes34: BinaryAssociation = BinaryAssociation(
    name="minutes34",
    ends={
        Property(name="Minutes", type=iec61131_literals_Hours, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Hours", type=Minutes, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
integer35: BinaryAssociation = BinaryAssociation(
    name="integer35",
    ends={
        Property(name="Unsigned_Integer37", type=iec61131_literals_Hours, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Hours36", type=Unsigned_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
seconds38: BinaryAssociation = BinaryAssociation(
    name="seconds38",
    ends={
        Property(name="Seconds", type=iec61131_literals_Minutes, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Minutes", type=Seconds, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
integer39: BinaryAssociation = BinaryAssociation(
    name="integer39",
    ends={
        Property(name="Unsigned_Integer41", type=iec61131_literals_Minutes, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Minutes40", type=Unsigned_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
integer31: BinaryAssociation = BinaryAssociation(
    name="integer31",
    ends={
        Property(name="Unsigned_Integer", type=iec61131_literals_Days, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Days", type=Unsigned_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
hours32: BinaryAssociation = BinaryAssociation(
    name="hours32",
    ends={
        Property(name="Hours", type=iec61131_literals_Days, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Days33", type=Hours, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
double_byte_character_representation47: BinaryAssociation = BinaryAssociation(
    name="double_byte_character_representation47",
    ends={
        Property(name="Double_Byte_Character_Representation", type=iec61131_literals_Double_Byte_Character_String, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Double_Byte_Character_String", type=Double_Byte_Character_Representation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
second48: BinaryAssociation = BinaryAssociation(
    name="second48",
    ends={
        Property(name="Fixed_Point49", type=iec61131_literals_Daytime, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Daytime", type=Fixed_Point, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
milliseconds42: BinaryAssociation = BinaryAssociation(
    name="milliseconds42",
    ends={
        Property(name="Milliseconds", type=iec61131_literals_Seconds, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Seconds", type=Milliseconds, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
integer43: BinaryAssociation = BinaryAssociation(
    name="integer43",
    ends={
        Property(name="Unsigned_Integer45", type=iec61131_literals_Seconds, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Seconds44", type=Unsigned_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
single_byte_character_representation46: BinaryAssociation = BinaryAssociation(
    name="single_byte_character_representation46",
    ends={
        Property(name="Single_Byte_Character_Representation", type=iec61131_literals_Single_Byte_Character_String, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Single_Byte_Character_String", type=Single_Byte_Character_Representation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
common_character_representation51: BinaryAssociation = BinaryAssociation(
    name="common_character_representation51",
    ends={
        Property(name="Common_Character_Representation52", type=iec61131_literals_Double_Byte_Character_Representation, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Double_Byte_Character_Representation", type=Common_Character_Representation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
common_character_representation50: BinaryAssociation = BinaryAssociation(
    name="common_character_representation50",
    ends={
        Property(name="Common_Character_Representation", type=iec61131_literals_Single_Byte_Character_Representation, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_literals_Single_Byte_Character_Representation", type=Common_Character_Representation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var_list54: BinaryAssociation = BinaryAssociation(
    name="var_list54",
    ends={
        Property(name="Var1_List", type=iec61131_interfaces_Var_Init_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Var_Init_Decl", type=Var1_List, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
specification55: BinaryAssociation = BinaryAssociation(
    name="specification55",
    ends={
        Property(name="Var1_Specification", type=iec61131_interfaces_Var1_Init_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Var1_Init_Decl", type=Var1_Specification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
var_list56: BinaryAssociation = BinaryAssociation(
    name="var_list56",
    ends={
        Property(name="Var1_List57", type=iec61131_interfaces_Edge_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Edge_Declaration", type=Var1_List, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
input_declaration53: BinaryAssociation = BinaryAssociation(
    name="input_declaration53",
    ends={
        Property(name="Input_Declaration", type=iec61131_interfaces_Input_Declarations, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Input_Declarations", type=Input_Declaration, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
simple_specification61: BinaryAssociation = BinaryAssociation(
    name="simple_specification61",
    ends={
        Property(name="Simple_Specification", type=iec61131_interfaces_Simple_Spec_Init, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Simple_Spec_Init", type=Simple_Specification, multiplicity=Multiplicity(1, 1))
    }
)
subrange_specification62: BinaryAssociation = BinaryAssociation(
    name="subrange_specification62",
    ends={
        Property(name="Subrange_Specification", type=iec61131_interfaces_Subrange_Spec_Init, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Subrange_Spec_Init", type=Subrange_Specification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
signed_integer63: BinaryAssociation = BinaryAssociation(
    name="signed_integer63",
    ends={
        Property(name="Signed_Integer", type=iec61131_interfaces_Subrange_Spec_Init, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Subrange_Spec_Init64", type=Signed_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bool_type_name58: BinaryAssociation = BinaryAssociation(
    name="bool_type_name58",
    ends={
        Property(name="Bool_Type_Name", type=iec61131_interfaces_Edge_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Edge_Declaration59", type=Bool_Type_Name, multiplicity=Multiplicity(1, 1))
    }
)
assignment60: BinaryAssociation = BinaryAssociation(
    name="assignment60",
    ends={
        Property(name="Assignment_Symbol", type=iec61131_interfaces_Var1_Specification, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Var1_Specification", type=Assignment_Symbol, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structure_initialization70: BinaryAssociation = BinaryAssociation(
    name="structure_initialization70",
    ends={
        Property(name="Structure_Initialization", type=iec61131_interfaces_Fb_Name_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Fb_Name_Decl", type=Structure_Initialization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function_block_type_name71: BinaryAssociation = BinaryAssociation(
    name="function_block_type_name71",
    ends={
        Property(name="Function_Block_Type_Name", type=iec61131_interfaces_Fb_Name_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Fb_Name_Decl72", type=Function_Block_Type_Name, multiplicity=Multiplicity(1, 1))
    }
)
assignment73: BinaryAssociation = BinaryAssociation(
    name="assignment73",
    ends={
        Property(name="Assignment_Symbol75", type=iec61131_interfaces_Fb_Name_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Fb_Name_Decl74", type=Assignment_Symbol, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumerated_specification65: BinaryAssociation = BinaryAssociation(
    name="enumerated_specification65",
    ends={
        Property(name="Enumerated_Specification", type=iec61131_interfaces_Enumerated_Spec_Init, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Enumerated_Spec_Init", type=Enumerated_Specification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
enumerated_value66: BinaryAssociation = BinaryAssociation(
    name="enumerated_value66",
    ends={
        Property(name="Enumerated_Value", type=iec61131_interfaces_Enumerated_Spec_Init, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Enumerated_Spec_Init67", type=Enumerated_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array_spec_init68: BinaryAssociation = BinaryAssociation(
    name="array_spec_init68",
    ends={
        Property(name="Array_Spec_Init", type=iec61131_interfaces_Array_Var_Init_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Array_Var_Init_Decl", type=Array_Spec_Init, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initialized_structure69: BinaryAssociation = BinaryAssociation(
    name="initialized_structure69",
    ends={
        Property(name="Initialized_Structure", type=iec61131_interfaces_Structured_Var_Init_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Structured_Var_Init_Decl", type=Initialized_Structure, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
array_initialization80: BinaryAssociation = BinaryAssociation(
    name="array_initialization80",
    ends={
        Property(name="Array_Initialization", type=iec61131_interfaces_Array_Spec_Init, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Array_Spec_Init81", type=Array_Initialization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array_specification82: BinaryAssociation = BinaryAssociation(
    name="array_specification82",
    ends={
        Property(name="Array_Specification", type=iec61131_interfaces_Array_Spec_Init, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Array_Spec_Init83", type=Array_Specification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assignment84: BinaryAssociation = BinaryAssociation(
    name="assignment84",
    ends={
        Property(name="Assignment_Symbol85", type=iec61131_interfaces_Initialized_Structure, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Initialized_Structure", type=Assignment_Symbol, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structure_initialization86: BinaryAssociation = BinaryAssociation(
    name="structure_initialization86",
    ends={
        Property(name="Structure_Initialization88", type=iec61131_interfaces_Initialized_Structure, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Initialized_Structure87", type=Structure_Initialization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structure_type_name89: BinaryAssociation = BinaryAssociation(
    name="structure_type_name89",
    ends={
        Property(name="Structure_Type_Name", type=iec61131_interfaces_Initialized_Structure, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Initialized_Structure90", type=Structure_Type_Name, multiplicity=Multiplicity(1, 1))
    }
)
var_init_decl76: BinaryAssociation = BinaryAssociation(
    name="var_init_decl76",
    ends={
        Property(name="Var_Init_Decl", type=iec61131_interfaces_Output_Declarations, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Output_Declarations", type=Var_Init_Decl, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
var_declaration77: BinaryAssociation = BinaryAssociation(
    name="var_declaration77",
    ends={
        Property(name="Var_Declaration", type=iec61131_interfaces_Input_Output_Declarations, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Input_Output_Declarations", type=Var_Declaration, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
assignment78: BinaryAssociation = BinaryAssociation(
    name="assignment78",
    ends={
        Property(name="Assignment_Symbol79", type=iec61131_interfaces_Array_Spec_Init, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Array_Spec_Init", type=Assignment_Symbol, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structure_element_init96: BinaryAssociation = BinaryAssociation(
    name="structure_element_init96",
    ends={
        Property(name="Initial_Element", type=iec61131_interfaces_Structure_Element_Initialization, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Structure_Element_Initialization97", type=Initial_Element, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
enumerated_type_name98: BinaryAssociation = BinaryAssociation(
    name="enumerated_type_name98",
    ends={
        Property(name="Enumerated_Type_Name", type=iec61131_interfaces_Enumerated_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Enumerated_Value", type=Enumerated_Type_Name, multiplicity=Multiplicity(0, 1))
    }
)
array_initial_elements99: BinaryAssociation = BinaryAssociation(
    name="array_initial_elements99",
    ends={
        Property(name="Array_Initial_Elements", type=iec61131_interfaces_Array_Initialization, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Array_Initialization", type=Array_Initial_Elements, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
structure_element_initialization91: BinaryAssociation = BinaryAssociation(
    name="structure_element_initialization91",
    ends={
        Property(name="Structure_Element_Initialization", type=iec61131_interfaces_Structure_Initialization, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Structure_Initialization", type=Structure_Element_Initialization, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
structure_element_name92: BinaryAssociation = BinaryAssociation(
    name="structure_element_name92",
    ends={
        Property(name="Structure_Element_Name", type=iec61131_interfaces_Structure_Element_Initialization, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Structure_Element_Initialization", type=Structure_Element_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assignment93: BinaryAssociation = BinaryAssociation(
    name="assignment93",
    ends={
        Property(name="Assignment_Symbol95", type=iec61131_interfaces_Structure_Element_Initialization, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Structure_Element_Initialization94", type=Assignment_Symbol, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
array_specification101: BinaryAssociation = BinaryAssociation(
    name="array_specification101",
    ends={
        Property(name="Array_Specification102", type=iec61131_interfaces_Array_Var_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Array_Var_Declaration", type=Array_Specification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
structure_type_name103: BinaryAssociation = BinaryAssociation(
    name="structure_type_name103",
    ends={
        Property(name="Structure_Type_Name104", type=iec61131_interfaces_Structured_Var_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Structured_Var_Declaration", type=Structure_Type_Name, multiplicity=Multiplicity(1, 1))
    }
)
specification100: BinaryAssociation = BinaryAssociation(
    name="specification100",
    ends={
        Property(name="Specification", type=iec61131_interfaces_Var1_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Var1_Declaration", type=Specification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
integer105: BinaryAssociation = BinaryAssociation(
    name="integer105",
    ends={
        Property(name="Range", type=iec61131_interfaces_Subrange, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Subrange", type=Range, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
single_byte_string_spec106: BinaryAssociation = BinaryAssociation(
    name="single_byte_string_spec106",
    ends={
        Property(name="Single_Byte_String_Spec", type=iec61131_interfaces_Single_Byte_String_Var_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Single_Byte_String_Var_Declaration", type=Single_Byte_String_Spec, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
double_byte_string_spec107: BinaryAssociation = BinaryAssociation(
    name="double_byte_string_spec107",
    ends={
        Property(name="Double_Byte_String_Spec", type=iec61131_interfaces_Double_Byte_String_Var_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Double_Byte_String_Var_Declaration", type=Double_Byte_String_Spec, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
single_byte_character_string108: BinaryAssociation = BinaryAssociation(
    name="single_byte_character_string108",
    ends={
        Property(name="Single_Byte_Character_String", type=iec61131_interfaces_Single_Byte_String_Spec, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Single_Byte_String_Spec", type=Single_Byte_Character_String, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment109: BinaryAssociation = BinaryAssociation(
    name="assignment109",
    ends={
        Property(name="Assignment_Symbol111", type=iec61131_interfaces_Single_Byte_String_Spec, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Single_Byte_String_Spec110", type=Assignment_Symbol, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
single_string112: BinaryAssociation = BinaryAssociation(
    name="single_string112",
    ends={
        Property(name="Single_BString", type=iec61131_interfaces_Single_Byte_String_Spec, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Single_Byte_String_Spec113", type=Single_BString, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
double_byte_character_string114: BinaryAssociation = BinaryAssociation(
    name="double_byte_character_string114",
    ends={
        Property(name="Double_Byte_Character_String", type=iec61131_interfaces_Double_Byte_String_Spec, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Double_Byte_String_Spec", type=Double_Byte_Character_String, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment115: BinaryAssociation = BinaryAssociation(
    name="assignment115",
    ends={
        Property(name="Assignment_Symbol117", type=iec61131_interfaces_Double_Byte_String_Spec, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Double_Byte_String_Spec116", type=Assignment_Symbol, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
double_string118: BinaryAssociation = BinaryAssociation(
    name="double_string118",
    ends={
        Property(name="Double_BString", type=iec61131_interfaces_Double_Byte_String_Spec, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Double_Byte_String_Spec119", type=Double_BString, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable_name120: BinaryAssociation = BinaryAssociation(
    name="variable_name120",
    ends={
        Property(name="Variable_Name", type=iec61131_interfaces_Var1_List, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Var1_List", type=Variable_Name, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
external_declaration121: BinaryAssociation = BinaryAssociation(
    name="external_declaration121",
    ends={
        Property(name="External_Declaration", type=iec61131_interfaces_External_Var_Declarations, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_External_Var_Declarations", type=External_Declaration, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
global_var_name122: BinaryAssociation = BinaryAssociation(
    name="global_var_name122",
    ends={
        Property(name="Global_Var_Name", type=iec61131_interfaces_External_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_External_Declaration", type=Global_Var_Name, multiplicity=Multiplicity(1, 1))
    }
)
specification123: BinaryAssociation = BinaryAssociation(
    name="specification123",
    ends={
        Property(name="External_Specification", type=iec61131_interfaces_External_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_External_Declaration124", type=External_Specification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
global_var_name125: BinaryAssociation = BinaryAssociation(
    name="global_var_name125",
    ends={
        Property(name="Global_Var_Name126", type=iec61131_interfaces_Global_Var_List, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Global_Var_List", type=Global_Var_Name, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
temp_var_decl127: BinaryAssociation = BinaryAssociation(
    name="temp_var_decl127",
    ends={
        Property(name="Temp_Var_Decl", type=iec61131_interfaces_Temp_Var_Decls, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Temp_Var_Decls", type=Temp_Var_Decl, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
incompl_located_var_decl128: BinaryAssociation = BinaryAssociation(
    name="incompl_located_var_decl128",
    ends={
        Property(name="Incompl_Located_Var_Decl", type=iec61131_interfaces_Incompl_Located_Var_Declarations, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Incompl_Located_Var_Declarations", type=Incompl_Located_Var_Decl, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
var_init_decl129: BinaryAssociation = BinaryAssociation(
    name="var_init_decl129",
    ends={
        Property(name="Var_Init_Decl130", type=iec61131_interfaces_RNV_Declarations, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_RNV_Declarations", type=Var_Init_Decl, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variable_name131: BinaryAssociation = BinaryAssociation(
    name="variable_name131",
    ends={
        Property(name="Variable_Name132", type=iec61131_interfaces_Incompl_Located_Var_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Incompl_Located_Var_Decl", type=Variable_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
incompl_location133: BinaryAssociation = BinaryAssociation(
    name="incompl_location133",
    ends={
        Property(name="Incompl_Location", type=iec61131_interfaces_Incompl_Located_Var_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Incompl_Located_Var_Decl134", type=Incompl_Location, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
var_spec135: BinaryAssociation = BinaryAssociation(
    name="var_spec135",
    ends={
        Property(name="Var_Spec", type=iec61131_interfaces_Incompl_Located_Var_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Incompl_Located_Var_Decl136", type=Var_Spec, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
direct_variable137: BinaryAssociation = BinaryAssociation(
    name="direct_variable137",
    ends={
        Property(name="Direct_Variable", type=iec61131_interfaces_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Location", type=Direct_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
location138: BinaryAssociation = BinaryAssociation(
    name="location138",
    ends={
        Property(name="Location", type=iec61131_interfaces_Located_Var_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Located_Var_Decl", type=Location, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable_name139: BinaryAssociation = BinaryAssociation(
    name="variable_name139",
    ends={
        Property(name="Variable_Name141", type=iec61131_interfaces_Located_Var_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Located_Var_Decl140", type=Variable_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
located_var_spec_init142: BinaryAssociation = BinaryAssociation(
    name="located_var_spec_init142",
    ends={
        Property(name="Located_Var_Spec_Init", type=iec61131_interfaces_Located_Var_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Located_Var_Decl143", type=Located_Var_Spec_Init, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
global_var_name152: BinaryAssociation = BinaryAssociation(
    name="global_var_name152",
    ends={
        Property(name="iec61131_interfaces_Global_Var_Location153", type=Global_Var_Name, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="Global_Var_Name154", type=iec61131_interfaces_Global_Var_Location, multiplicity=Multiplicity(1, 1))
    }
)
located_var_decl144: BinaryAssociation = BinaryAssociation(
    name="located_var_decl144",
    ends={
        Property(name="Located_Var_Decl", type=iec61131_interfaces_Located_Var_Declarations, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Located_Var_Declarations", type=Located_Var_Decl, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
global_var_decl145: BinaryAssociation = BinaryAssociation(
    name="global_var_decl145",
    ends={
        Property(name="Global_Var_Decl", type=iec61131_interfaces_Global_Var_Declarations, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Global_Var_Declarations", type=Global_Var_Decl, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
global_var_spec146: BinaryAssociation = BinaryAssociation(
    name="global_var_spec146",
    ends={
        Property(name="Global_Var_Spec", type=iec61131_interfaces_Global_Var_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Global_Var_Decl", type=Global_Var_Spec, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
located_var_spec_init147: BinaryAssociation = BinaryAssociation(
    name="located_var_spec_init147",
    ends={
        Property(name="Located_Var_Spec_Init149", type=iec61131_interfaces_Global_Var_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Global_Var_Decl148", type=Located_Var_Spec_Init, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
location150: BinaryAssociation = BinaryAssociation(
    name="location150",
    ends={
        Property(name="Location151", type=iec61131_interfaces_Global_Var_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Global_Var_Location", type=Location, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
integer155: BinaryAssociation = BinaryAssociation(
    name="integer155",
    ends={
        Property(name="Unsigned_Integer156", type=iec61131_interfaces_Byte_String, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Byte_String", type=Unsigned_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
single_byte_string_type_name157: BinaryAssociation = BinaryAssociation(
    name="single_byte_string_type_name157",
    ends={
        Property(name="Single_Byte_String_Type_Name", type=iec61131_interfaces_Single_BString, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Single_BString", type=Single_Byte_String_Type_Name, multiplicity=Multiplicity(1, 1))
    }
)
double_byte_string_type_name158: BinaryAssociation = BinaryAssociation(
    name="double_byte_string_type_name158",
    ends={
        Property(name="Double_Byte_String_Type_Name", type=iec61131_interfaces_Double_BString, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Double_BString", type=Double_Byte_String_Type_Name, multiplicity=Multiplicity(1, 1))
    }
)
integer_type_name159: BinaryAssociation = BinaryAssociation(
    name="integer_type_name159",
    ends={
        Property(name="Integer_Type_Name160", type=iec61131_interfaces_Subrange_Specification1, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Subrange_Specification1", type=Integer_Type_Name, multiplicity=Multiplicity(1, 1))
    }
)
subrange161: BinaryAssociation = BinaryAssociation(
    name="subrange161",
    ends={
        Property(name="Subrange", type=iec61131_interfaces_Subrange_Specification1, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Subrange_Specification1162", type=Subrange, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subrange_type_name163: BinaryAssociation = BinaryAssociation(
    name="subrange_type_name163",
    ends={
        Property(name="Subrange_Type_Name", type=iec61131_interfaces_Subrange_Specification2, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Subrange_Specification2", type=Subrange_Type_Name, multiplicity=Multiplicity(1, 1))
    }
)
enumerated_value164: BinaryAssociation = BinaryAssociation(
    name="enumerated_value164",
    ends={
        Property(name="Enumerated_Value165", type=iec61131_interfaces_Enumerated_Specification1, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Enumerated_Specification1", type=Enumerated_Value, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
enumerated_type_name166: BinaryAssociation = BinaryAssociation(
    name="enumerated_type_name166",
    ends={
        Property(name="Enumerated_Type_Name167", type=iec61131_interfaces_Enumerated_Specification2, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Enumerated_Specification2", type=Enumerated_Type_Name, multiplicity=Multiplicity(1, 1))
    }
)
array_type_name168: BinaryAssociation = BinaryAssociation(
    name="array_type_name168",
    ends={
        Property(name="Array_Type_Name", type=iec61131_interfaces_Array_Specification1, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Array_Specification1", type=Array_Type_Name, multiplicity=Multiplicity(1, 1))
    }
)
non_generic_type_name169: BinaryAssociation = BinaryAssociation(
    name="non_generic_type_name169",
    ends={
        Property(name="Non_Generic_Type_Name", type=iec61131_interfaces_Array_Specification2, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Array_Specification2", type=Non_Generic_Type_Name, multiplicity=Multiplicity(1, 1))
    }
)
subrange170: BinaryAssociation = BinaryAssociation(
    name="subrange170",
    ends={
        Property(name="Subrange172", type=iec61131_interfaces_Array_Specification2, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Array_Specification2171", type=Subrange, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
structure183: BinaryAssociation = BinaryAssociation(
    name="structure183",
    ends={
        Property(name="Structure_Initialization184", type=iec61131_interfaces_InitElement_Structure, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_InitElement_Structure", type=Structure_Initialization, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
array_initial_element173: BinaryAssociation = BinaryAssociation(
    name="array_initial_element173",
    ends={
        Property(name="Initial_Element174", type=iec61131_interfaces_Array_Initial_Elements1, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Array_Initial_Elements1", type=Initial_Element, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
integer175: BinaryAssociation = BinaryAssociation(
    name="integer175",
    ends={
        Property(name="Unsigned_Integer176", type=iec61131_interfaces_Array_Initial_Elements2, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Array_Initial_Elements2", type=Unsigned_Integer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
array_initial_element177: BinaryAssociation = BinaryAssociation(
    name="array_initial_element177",
    ends={
        Property(name="Initial_Element179", type=iec61131_interfaces_Array_Initial_Elements2, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Array_Initial_Elements2178", type=Initial_Element, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant180: BinaryAssociation = BinaryAssociation(
    name="constant180",
    ends={
        Property(name="Constant", type=iec61131_interfaces_InitElement_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_InitElement_Constant", type=Constant, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
enum_value181: BinaryAssociation = BinaryAssociation(
    name="enum_value181",
    ends={
        Property(name="Enumerated_Value182", type=iec61131_interfaces_InitElement_EnumValue, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_InitElement_EnumValue", type=Enumerated_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
structure_left185: BinaryAssociation = BinaryAssociation(
    name="structure_left185",
    ends={
        Property(name="Initial_Element187", type=iec61131_interfaces_InitElement_Structure, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_InitElement_Structure186", type=Initial_Element, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
structure_right188: BinaryAssociation = BinaryAssociation(
    name="structure_right188",
    ends={
        Property(name="Initial_Element190", type=iec61131_interfaces_InitElement_Structure, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_InitElement_Structure189", type=Initial_Element, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
array191: BinaryAssociation = BinaryAssociation(
    name="array191",
    ends={
        Property(name="Array_Initialization192", type=iec61131_interfaces_InitElement_Array, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_InitElement_Array", type=Array_Initialization, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
array_left193: BinaryAssociation = BinaryAssociation(
    name="array_left193",
    ends={
        Property(name="Initial_Element195", type=iec61131_interfaces_InitElement_Array, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_InitElement_Array194", type=Initial_Element, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
array_right196: BinaryAssociation = BinaryAssociation(
    name="array_right196",
    ends={
        Property(name="Initial_Element198", type=iec61131_interfaces_InitElement_Array, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_InitElement_Array197", type=Initial_Element, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
var2_init_decl199: BinaryAssociation = BinaryAssociation(
    name="var2_init_decl199",
    ends={
        Property(name="Var2_Init_Decl", type=iec61131_interfaces_Function_Var_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Function_Var_Decl", type=Var2_Init_Decl, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
constant200: BinaryAssociation = BinaryAssociation(
    name="constant200",
    ends={
        Property(name="Constant201", type=iec61131_interfaces_Var_Name_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Var_Name_Decl", type=Constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structure_initialization202: BinaryAssociation = BinaryAssociation(
    name="structure_initialization202",
    ends={
        Property(name="Structure_Initialization204", type=iec61131_interfaces_Var_Name_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Var_Name_Decl203", type=Structure_Initialization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specification205: BinaryAssociation = BinaryAssociation(
    name="specification205",
    ends={
        Property(name="Var1_Specification_Func", type=iec61131_interfaces_Var_Init_Decl_Func, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Var_Init_Decl_Func", type=Var1_Specification_Func, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
simple_specification206: BinaryAssociation = BinaryAssociation(
    name="simple_specification206",
    ends={
        Property(name="Simple_Specification_Func", type=iec61131_interfaces_Simple_Spec_Init_Func, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Simple_Spec_Init_Func", type=Simple_Specification_Func, multiplicity=Multiplicity(1, 1))
    }
)
constant207: BinaryAssociation = BinaryAssociation(
    name="constant207",
    ends={
        Property(name="Constant209", type=iec61131_interfaces_Simple_Spec_Init_Func, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Simple_Spec_Init_Func208", type=Constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var_list210: BinaryAssociation = BinaryAssociation(
    name="var_list210",
    ends={
        Property(name="Var1_List211", type=iec61131_interfaces_Temp_Var_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_interfaces_Temp_Var_Declaration", type=Var1_List, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
program_type_name212: BinaryAssociation = BinaryAssociation(
    name="program_type_name212",
    ends={
        Property(name="Program_Type_Name", type=iec61131_pous_Program_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Program_Declaration", type=Program_Type_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
program_var_declarations213: BinaryAssociation = BinaryAssociation(
    name="program_var_declarations213",
    ends={
        Property(name="Program_Vars", type=iec61131_pous_Program_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Program_Declaration214", type=Program_Vars, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function_block_body215: BinaryAssociation = BinaryAssociation(
    name="function_block_body215",
    ends={
        Property(name="Function_Block_Body", type=iec61131_pous_Program_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Program_Declaration216", type=Function_Block_Body, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
function_body228: BinaryAssociation = BinaryAssociation(
    name="function_body228",
    ends={
        Property(name="iec61131_pous_Function_Declaration229", type=Function_Body, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="Function_Body", type=iec61131_pous_Function_Declaration, multiplicity=Multiplicity(1, 1))
    }
)
derived_function_block_name217: BinaryAssociation = BinaryAssociation(
    name="derived_function_block_name217",
    ends={
        Property(name="Derived_Function_Block_Name", type=iec61131_pous_Function_Block_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Function_Block_Declaration", type=Derived_Function_Block_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
function_block_body218: BinaryAssociation = BinaryAssociation(
    name="function_block_body218",
    ends={
        Property(name="Function_Block_Body220", type=iec61131_pous_Function_Block_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Function_Block_Declaration219", type=Function_Block_Body, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
function_block_var_declarations221: BinaryAssociation = BinaryAssociation(
    name="function_block_var_declarations221",
    ends={
        Property(name="Function_Block_Vars", type=iec61131_pous_Function_Block_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Function_Block_Declaration222", type=Function_Block_Vars, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
derived_function_name223: BinaryAssociation = BinaryAssociation(
    name="derived_function_name223",
    ends={
        Property(name="Derived_Function_Name", type=iec61131_pous_Function_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Function_Declaration", type=Derived_Function_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
function_return_value224: BinaryAssociation = BinaryAssociation(
    name="function_return_value224",
    ends={
        Property(name="Function_Return_Value", type=iec61131_pous_Function_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Function_Declaration225", type=Function_Return_Value, multiplicity=Multiplicity(1, 1))
    }
)
function_var_declarations226: BinaryAssociation = BinaryAssociation(
    name="function_var_declarations226",
    ends={
        Property(name="Function_Vars", type=iec61131_pous_Function_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Function_Declaration227", type=Function_Vars, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
access_name230: BinaryAssociation = BinaryAssociation(
    name="access_name230",
    ends={
        Property(name="Access_Name", type=iec61131_pous_Program_Access_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Program_Access_Decl", type=Access_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
non_generic_type_name231: BinaryAssociation = BinaryAssociation(
    name="non_generic_type_name231",
    ends={
        Property(name="Non_Generic_Type_Name233", type=iec61131_pous_Program_Access_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Program_Access_Decl232", type=Non_Generic_Type_Name, multiplicity=Multiplicity(1, 1))
    }
)
symbolic_variable234: BinaryAssociation = BinaryAssociation(
    name="symbolic_variable234",
    ends={
        Property(name="Symbolic_Variable", type=iec61131_pous_Program_Access_Decl, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Program_Access_Decl235", type=Symbolic_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assignment249: BinaryAssociation = BinaryAssociation(
    name="assignment249",
    ends={
        Property(name="Assignment_Symbol251", type=iec61131_pous_String_Type_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_String_Type_Declaration250", type=Assignment_Symbol, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
character_string252: BinaryAssociation = BinaryAssociation(
    name="character_string252",
    ends={
        Property(name="Character_String", type=iec61131_pous_String_Type_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_String_Type_Declaration253", type=Character_String, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type_declaration236: BinaryAssociation = BinaryAssociation(
    name="type_declaration236",
    ends={
        Property(name="Type_Declaration", type=iec61131_pous_Data_Type_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Data_Type_Declaration", type=Type_Declaration, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
array_type_name237: BinaryAssociation = BinaryAssociation(
    name="array_type_name237",
    ends={
        Property(name="Array_Type_Name238", type=iec61131_pous_Array_Type_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Array_Type_Declaration", type=Array_Type_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
array_spec_init239: BinaryAssociation = BinaryAssociation(
    name="array_spec_init239",
    ends={
        Property(name="Array_Spec_Init241", type=iec61131_pous_Array_Type_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Array_Type_Declaration240", type=Array_Spec_Init, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
structure_type_name242: BinaryAssociation = BinaryAssociation(
    name="structure_type_name242",
    ends={
        Property(name="Structure_Type_Name243", type=iec61131_pous_Structure_Type_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Structure_Type_Declaration", type=Structure_Type_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
structure_specification244: BinaryAssociation = BinaryAssociation(
    name="structure_specification244",
    ends={
        Property(name="Structure_Specification", type=iec61131_pous_Structure_Type_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Structure_Type_Declaration245", type=Structure_Specification, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
string_type_name246: BinaryAssociation = BinaryAssociation(
    name="string_type_name246",
    ends={
        Property(name="String_Type_Name", type=iec61131_pous_String_Type_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_String_Type_Declaration", type=String_Type_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
byte_string_type_name247: BinaryAssociation = BinaryAssociation(
    name="byte_string_type_name247",
    ends={
        Property(name="Byte_String_Type_Name", type=iec61131_pous_String_Type_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_String_Type_Declaration248", type=Byte_String_Type_Name, multiplicity=Multiplicity(1, 1))
    }
)
program_access_decl273: BinaryAssociation = BinaryAssociation(
    name="program_access_decl273",
    ends={
        Property(name="Program_Access_Decl", type=iec61131_pous_Program_Access_Decls, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Program_Access_Decls", type=Program_Access_Decl, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
programs274: BinaryAssociation = BinaryAssociation(
    name="programs274",
    ends={
        Property(name="Program_Declaration", type=iec61131_pous_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Library", type=Program_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
integer254: BinaryAssociation = BinaryAssociation(
    name="integer254",
    ends={
        Property(name="Unsigned_Integer256", type=iec61131_pous_String_Type_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_String_Type_Declaration255", type=Unsigned_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
functions275: BinaryAssociation = BinaryAssociation(
    name="functions275",
    ends={
        Property(name="Function_Declaration", type=iec61131_pous_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Library276", type=Function_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
simple_type_name257: BinaryAssociation = BinaryAssociation(
    name="simple_type_name257",
    ends={
        Property(name="Simple_Type_Name", type=iec61131_pous_Simple_Type_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Simple_Type_Declaration", type=Simple_Type_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
simple_spec_init258: BinaryAssociation = BinaryAssociation(
    name="simple_spec_init258",
    ends={
        Property(name="Simple_Spec_Init", type=iec61131_pous_Simple_Type_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Simple_Type_Declaration259", type=Simple_Spec_Init, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subrange_type_name260: BinaryAssociation = BinaryAssociation(
    name="subrange_type_name260",
    ends={
        Property(name="Subrange_Type_Name261", type=iec61131_pous_Subrange_Type_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Subrange_Type_Declaration", type=Subrange_Type_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subrange_spec_init262: BinaryAssociation = BinaryAssociation(
    name="subrange_spec_init262",
    ends={
        Property(name="Subrange_Spec_Init", type=iec61131_pous_Subrange_Type_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Subrange_Type_Declaration263", type=Subrange_Spec_Init, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
enumerated_type_name264: BinaryAssociation = BinaryAssociation(
    name="enumerated_type_name264",
    ends={
        Property(name="Enumerated_Type_Name265", type=iec61131_pous_Enumerated_Type_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Enumerated_Type_Declaration", type=Enumerated_Type_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
enumerated_spec_init266: BinaryAssociation = BinaryAssociation(
    name="enumerated_spec_init266",
    ends={
        Property(name="Enumerated_Spec_Init", type=iec61131_pous_Enumerated_Type_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Enumerated_Type_Declaration267", type=Enumerated_Spec_Init, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
structure_element_declaration268: BinaryAssociation = BinaryAssociation(
    name="structure_element_declaration268",
    ends={
        Property(name="Structure_Element_Declaration", type=iec61131_pous_Structure_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Structure_Declaration", type=Structure_Element_Declaration, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
structure_element_name269: BinaryAssociation = BinaryAssociation(
    name="structure_element_name269",
    ends={
        Property(name="Structure_Element_Name270", type=iec61131_pous_Structure_Element_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Structure_Element_Declaration", type=Structure_Element_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
structure_element271: BinaryAssociation = BinaryAssociation(
    name="structure_element271",
    ends={
        Property(name="Structure_Elements", type=iec61131_pous_Structure_Element_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Structure_Element_Declaration272", type=Structure_Elements, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resource_name290: BinaryAssociation = BinaryAssociation(
    name="resource_name290",
    ends={
        Property(name="Resource_Name", type=iec61131_configurations_Resource_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Resource_Declaration", type=Resource_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function_blocks277: BinaryAssociation = BinaryAssociation(
    name="function_blocks277",
    ends={
        Property(name="Function_Block_Declaration", type=iec61131_pous_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_pous_Library278", type=Function_Block_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configuration_name279: BinaryAssociation = BinaryAssociation(
    name="configuration_name279",
    ends={
        Property(name="Configuration_Name", type=iec61131_configurations_Configuration_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Configuration_Declaration", type=Configuration_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
single_resource_declaration280: BinaryAssociation = BinaryAssociation(
    name="single_resource_declaration280",
    ends={
        Property(name="Single_Resource_Declaration", type=iec61131_configurations_Configuration_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Configuration_Declaration281", type=Single_Resource_Declaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
global_var_declarations282: BinaryAssociation = BinaryAssociation(
    name="global_var_declarations282",
    ends={
        Property(name="Global_Var_Declarations", type=iec61131_configurations_Configuration_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Configuration_Declaration283", type=Global_Var_Declarations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instance_specific_initializations284: BinaryAssociation = BinaryAssociation(
    name="instance_specific_initializations284",
    ends={
        Property(name="Instance_Specific_Initializations", type=iec61131_configurations_Configuration_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Configuration_Declaration285", type=Instance_Specific_Initializations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
access_declarations286: BinaryAssociation = BinaryAssociation(
    name="access_declarations286",
    ends={
        Property(name="Access_Declarations", type=iec61131_configurations_Configuration_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Configuration_Declaration287", type=Access_Declarations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resource_declaration288: BinaryAssociation = BinaryAssociation(
    name="resource_declaration288",
    ends={
        Property(name="Resource_Declaration", type=iec61131_configurations_Configuration_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Configuration_Declaration289", type=Resource_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
task_name311: BinaryAssociation = BinaryAssociation(
    name="task_name311",
    ends={
        Property(name="Task_Name313", type=iec61131_configurations_Program_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Program_Configuration312", type=Task_Name, multiplicity=Multiplicity(0, 1))
    }
)
resource_type_name291: BinaryAssociation = BinaryAssociation(
    name="resource_type_name291",
    ends={
        Property(name="Resource_Type_Name", type=iec61131_configurations_Resource_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Resource_Declaration292", type=Resource_Type_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
single_resource_declaration293: BinaryAssociation = BinaryAssociation(
    name="single_resource_declaration293",
    ends={
        Property(name="Single_Resource_Declaration295", type=iec61131_configurations_Resource_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Resource_Declaration294", type=Single_Resource_Declaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
global_var_declarations296: BinaryAssociation = BinaryAssociation(
    name="global_var_declarations296",
    ends={
        Property(name="Global_Var_Declarations298", type=iec61131_configurations_Resource_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Resource_Declaration297", type=Global_Var_Declarations, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
task_configuration299: BinaryAssociation = BinaryAssociation(
    name="task_configuration299",
    ends={
        Property(name="Task_Configuration", type=iec61131_configurations_Single_Resource_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Single_Resource_Declaration", type=Task_Configuration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
program_configuration300: BinaryAssociation = BinaryAssociation(
    name="program_configuration300",
    ends={
        Property(name="Program_Configuration", type=iec61131_configurations_Single_Resource_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Single_Resource_Declaration301", type=Program_Configuration, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
task_name302: BinaryAssociation = BinaryAssociation(
    name="task_name302",
    ends={
        Property(name="Task_Name", type=iec61131_configurations_Task_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Task_Configuration", type=Task_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
task_initialization_priority303: BinaryAssociation = BinaryAssociation(
    name="task_initialization_priority303",
    ends={
        Property(name="Priority", type=iec61131_configurations_Task_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Task_Configuration304", type=Priority, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
task_initialization_single305: BinaryAssociation = BinaryAssociation(
    name="task_initialization_single305",
    ends={
        Property(name="Single", type=iec61131_configurations_Task_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Task_Configuration306", type=Single, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
task_initialization_interval307: BinaryAssociation = BinaryAssociation(
    name="task_initialization_interval307",
    ends={
        Property(name="Interval309", type=iec61131_configurations_Task_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Task_Configuration308", type=Interval, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
program_name310: BinaryAssociation = BinaryAssociation(
    name="program_name310",
    ends={
        Property(name="Program_Name", type=iec61131_configurations_Program_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Program_Configuration", type=Program_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
program_type_name314: BinaryAssociation = BinaryAssociation(
    name="program_type_name314",
    ends={
        Property(name="Program_Type_Name316", type=iec61131_configurations_Program_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Program_Configuration315", type=Program_Type_Name, multiplicity=Multiplicity(1, 1))
    }
)
prog_conf_elements317: BinaryAssociation = BinaryAssociation(
    name="prog_conf_elements317",
    ends={
        Property(name="Prog_Conf_Elements", type=iec61131_configurations_Program_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Program_Configuration318", type=Prog_Conf_Elements, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instance_specific_init319: BinaryAssociation = BinaryAssociation(
    name="instance_specific_init319",
    ends={
        Property(name="Instance_Specific_Init", type=iec61131_configurations_Instance_Specific_Initializations, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Instance_Specific_Initializations", type=Instance_Specific_Init, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
structure_element_name320: BinaryAssociation = BinaryAssociation(
    name="structure_element_name320",
    ends={
        Property(name="Structure_Element_Name321", type=iec61131_configurations_Global_Var_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Global_Var_Reference", type=Structure_Element_Name, multiplicity=Multiplicity(0, 1))
    }
)
global_var_name322: BinaryAssociation = BinaryAssociation(
    name="global_var_name322",
    ends={
        Property(name="Global_Var_Name324", type=iec61131_configurations_Global_Var_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Global_Var_Reference323", type=Global_Var_Name, multiplicity=Multiplicity(1, 1))
    }
)
resource_name325: BinaryAssociation = BinaryAssociation(
    name="resource_name325",
    ends={
        Property(name="Resource_Name327", type=iec61131_configurations_Global_Var_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Global_Var_Reference326", type=Resource_Name, multiplicity=Multiplicity(0, 1))
    }
)
symbolic_variable328: BinaryAssociation = BinaryAssociation(
    name="symbolic_variable328",
    ends={
        Property(name="Symbolic_Variable329", type=iec61131_configurations_Program_Output_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Program_Output_Reference", type=Symbolic_Variable, multiplicity=Multiplicity(1, 1))
    }
)
program_name330: BinaryAssociation = BinaryAssociation(
    name="program_name330",
    ends={
        Property(name="Program_Name332", type=iec61131_configurations_Program_Output_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Program_Output_Reference331", type=Program_Name, multiplicity=Multiplicity(1, 1))
    }
)
access_declaration333: BinaryAssociation = BinaryAssociation(
    name="access_declaration333",
    ends={
        Property(name="Access_Declaration", type=iec61131_configurations_Access_Declarations, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Access_Declarations", type=Access_Declaration, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
access_name334: BinaryAssociation = BinaryAssociation(
    name="access_name334",
    ends={
        Property(name="Access_Name335", type=iec61131_configurations_Access_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Access_Declaration", type=Access_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
access_path336: BinaryAssociation = BinaryAssociation(
    name="access_path336",
    ends={
        Property(name="Access_Path", type=iec61131_configurations_Access_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Access_Declaration337", type=Access_Path, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
non_generic_type_name338: BinaryAssociation = BinaryAssociation(
    name="non_generic_type_name338",
    ends={
        Property(name="Non_Generic_Type_Name340", type=iec61131_configurations_Access_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Access_Declaration339", type=Non_Generic_Type_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resource_name341: BinaryAssociation = BinaryAssociation(
    name="resource_name341",
    ends={
        Property(name="Resource_Name342", type=iec61131_configurations_Access_Path, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Access_Path", type=Resource_Name, multiplicity=Multiplicity(0, 1))
    }
)
direct_variable343: BinaryAssociation = BinaryAssociation(
    name="direct_variable343",
    ends={
        Property(name="Direct_Variable344", type=iec61131_configurations_Direct_Path, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Direct_Path", type=Direct_Variable, multiplicity=Multiplicity(1, 1))
    }
)
program_name345: BinaryAssociation = BinaryAssociation(
    name="program_name345",
    ends={
        Property(name="Program_Name346", type=iec61131_configurations_Symbolic_Path, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Symbolic_Path", type=Program_Name, multiplicity=Multiplicity(0, 1))
    }
)
fb_name347: BinaryAssociation = BinaryAssociation(
    name="fb_name347",
    ends={
        Property(name="Variable_Name349", type=iec61131_configurations_Symbolic_Path, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Symbolic_Path348", type=Variable_Name, multiplicity=Multiplicity(0, 9999))
    }
)
symbolic_variable350: BinaryAssociation = BinaryAssociation(
    name="symbolic_variable350",
    ends={
        Property(name="Symbolic_Variable352", type=iec61131_configurations_Symbolic_Path, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Symbolic_Path351", type=Symbolic_Variable, multiplicity=Multiplicity(1, 1))
    }
)
assignment353: BinaryAssociation = BinaryAssociation(
    name="assignment353",
    ends={
        Property(name="Assignment_Symbol354", type=iec61131_configurations_Task_Initialization, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Task_Initialization", type=Assignment_Symbol, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
prog_conf_element355: BinaryAssociation = BinaryAssociation(
    name="prog_conf_element355",
    ends={
        Property(name="Prog_Conf_Element", type=iec61131_configurations_Prog_Conf_Elements, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Prog_Conf_Elements", type=Prog_Conf_Element, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
task_name356: BinaryAssociation = BinaryAssociation(
    name="task_name356",
    ends={
        Property(name="Task_Name357", type=iec61131_configurations_Fb_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Fb_Task", type=Task_Name, multiplicity=Multiplicity(1, 1))
    }
)
fb_name358: BinaryAssociation = BinaryAssociation(
    name="fb_name358",
    ends={
        Property(name="Variable_Name360", type=iec61131_configurations_Fb_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Fb_Task359", type=Variable_Name, multiplicity=Multiplicity(1, 1))
    }
)
fb_name_spec389: BinaryAssociation = BinaryAssociation(
    name="fb_name_spec389",
    ends={
        Property(name="Variable_Name391", type=iec61131_configurations_Instance_Spec2, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Instance_Spec2390", type=Variable_Name, multiplicity=Multiplicity(1, 1))
    }
)
assignment392: BinaryAssociation = BinaryAssociation(
    name="assignment392",
    ends={
        Property(name="Assignment_Symbol394", type=iec61131_configurations_Instance_Spec2, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Instance_Spec2393", type=Assignment_Symbol, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
symbolic_variable361: BinaryAssociation = BinaryAssociation(
    name="symbolic_variable361",
    ends={
        Property(name="Symbolic_Variable362", type=iec61131_configurations_Prog_Cnxn, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Prog_Cnxn", type=Symbolic_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
data_sink363: BinaryAssociation = BinaryAssociation(
    name="data_sink363",
    ends={
        Property(name="Data_Sink", type=iec61131_configurations_Prog_Sink, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Prog_Sink", type=Data_Sink, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
prog_data_source364: BinaryAssociation = BinaryAssociation(
    name="prog_data_source364",
    ends={
        Property(name="Prog_Data_Source", type=iec61131_configurations_Prog_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Prog_Source", type=Prog_Data_Source, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assignment365: BinaryAssociation = BinaryAssociation(
    name="assignment365",
    ends={
        Property(name="Assignment_Symbol367", type=iec61131_configurations_Prog_Source, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Prog_Source366", type=Assignment_Symbol, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
resource_name368: BinaryAssociation = BinaryAssociation(
    name="resource_name368",
    ends={
        Property(name="Resource_Name369", type=iec61131_configurations_Instance_Specific_Init, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Instance_Specific_Init", type=Resource_Name, multiplicity=Multiplicity(1, 1))
    }
)
program_name370: BinaryAssociation = BinaryAssociation(
    name="program_name370",
    ends={
        Property(name="Program_Name372", type=iec61131_configurations_Instance_Specific_Init, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Instance_Specific_Init371", type=Program_Name, multiplicity=Multiplicity(1, 1))
    }
)
fb_name373: BinaryAssociation = BinaryAssociation(
    name="fb_name373",
    ends={
        Property(name="Variable_Name375", type=iec61131_configurations_Instance_Specific_Init, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Instance_Specific_Init374", type=Variable_Name, multiplicity=Multiplicity(0, 9999))
    }
)
location376: BinaryAssociation = BinaryAssociation(
    name="location376",
    ends={
        Property(name="Location377", type=iec61131_configurations_Instance_Spec1, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Instance_Spec1", type=Location, multiplicity=Multiplicity(0, 1))
    }
)
variable_name378: BinaryAssociation = BinaryAssociation(
    name="variable_name378",
    ends={
        Property(name="Variable_Name380", type=iec61131_configurations_Instance_Spec1, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Instance_Spec1379", type=Variable_Name, multiplicity=Multiplicity(1, 1))
    }
)
located_var_spec_init381: BinaryAssociation = BinaryAssociation(
    name="located_var_spec_init381",
    ends={
        Property(name="Located_Var_Spec_Init383", type=iec61131_configurations_Instance_Spec1, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Instance_Spec1382", type=Located_Var_Spec_Init, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
function_block_type_name384: BinaryAssociation = BinaryAssociation(
    name="function_block_type_name384",
    ends={
        Property(name="Function_Block_Type_Name385", type=iec61131_configurations_Instance_Spec2, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Instance_Spec2", type=Function_Block_Type_Name, multiplicity=Multiplicity(1, 1))
    }
)
structure_initialization386: BinaryAssociation = BinaryAssociation(
    name="structure_initialization386",
    ends={
        Property(name="Structure_Initialization388", type=iec61131_configurations_Instance_Spec2, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Instance_Spec2387", type=Structure_Initialization, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
data_source395: BinaryAssociation = BinaryAssociation(
    name="data_source395",
    ends={
        Property(name="Data_Source", type=iec61131_configurations_Single, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Single", type=Data_Source, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
data_source396: BinaryAssociation = BinaryAssociation(
    name="data_source396",
    ends={
        Property(name="Data_Source397", type=iec61131_configurations_Interval, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Interval", type=Data_Source, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
integer398: BinaryAssociation = BinaryAssociation(
    name="integer398",
    ends={
        Property(name="Unsigned_Integer399", type=iec61131_configurations_Priority, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_configurations_Priority", type=Unsigned_Integer, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement400: BinaryAssociation = BinaryAssociation(
    name="statement400",
    ends={
        Property(name="Statement", type=iec61131_st_Statement_List, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Statement_List", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression_left401: BinaryAssociation = BinaryAssociation(
    name="expression_left401",
    ends={
        Property(name="Expression_Types", type=iec61131_st_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Expression", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
or402: BinaryAssociation = BinaryAssociation(
    name="or402",
    ends={
        Property(name="Or_Operator", type=iec61131_st_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Expression403", type=Or_Operator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression_right404: BinaryAssociation = BinaryAssociation(
    name="expression_right404",
    ends={
        Property(name="Expression_Types406", type=iec61131_st_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Expression405", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assignment407: BinaryAssociation = BinaryAssociation(
    name="assignment407",
    ends={
        Property(name="Assignment_Symbol408", type=iec61131_st_Assignment_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Assignment_Statement", type=Assignment_Symbol, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression409: BinaryAssociation = BinaryAssociation(
    name="expression409",
    ends={
        Property(name="Expression_Types411", type=iec61131_st_Assignment_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Assignment_Statement410", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable412: BinaryAssociation = BinaryAssociation(
    name="variable412",
    ends={
        Property(name="Expression_Variable", type=iec61131_st_Assignment_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Assignment_Statement413", type=Expression_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
else438: BinaryAssociation = BinaryAssociation(
    name="else438",
    ends={
        Property(name="Else_Statement", type=iec61131_st_If_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_If_Statement439", type=Else_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fb_name414: BinaryAssociation = BinaryAssociation(
    name="fb_name414",
    ends={
        Property(name="Variable_Name415", type=iec61131_st_Fb_Invocation, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Fb_Invocation", type=Variable_Name, multiplicity=Multiplicity(1, 1))
    }
)
param_assignment416: BinaryAssociation = BinaryAssociation(
    name="param_assignment416",
    ends={
        Property(name="Param_Assignment", type=iec61131_st_Fb_Invocation, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Fb_Invocation417", type=Param_Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression418: BinaryAssociation = BinaryAssociation(
    name="expression418",
    ends={
        Property(name="Expression_Types419", type=iec61131_st_Param_Type1, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Param_Type1", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assignment420: BinaryAssociation = BinaryAssociation(
    name="assignment420",
    ends={
        Property(name="Assignment_Symbol422", type=iec61131_st_Param_Type1, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Param_Type1421", type=Assignment_Symbol, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable_name423: BinaryAssociation = BinaryAssociation(
    name="variable_name423",
    ends={
        Property(name="Variable_Name425", type=iec61131_st_Param_Type1, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Param_Type1424", type=Variable_Name, multiplicity=Multiplicity(0, 1))
    }
)
variable_name426: BinaryAssociation = BinaryAssociation(
    name="variable_name426",
    ends={
        Property(name="Variable_Name427", type=iec61131_st_Param_Type2, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Param_Type2", type=Variable_Name, multiplicity=Multiplicity(1, 1))
    }
)
variable428: BinaryAssociation = BinaryAssociation(
    name="variable428",
    ends={
        Property(name="Variable", type=iec61131_st_Param_Type2, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Param_Type2429", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
not430: BinaryAssociation = BinaryAssociation(
    name="not430",
    ends={
        Property(name="Not_Operator", type=iec61131_st_Param_Type2, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Param_Type2431", type=Not_Operator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression432: BinaryAssociation = BinaryAssociation(
    name="expression432",
    ends={
        Property(name="Expression_Types433", type=iec61131_st_If_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_If_Statement", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement_list434: BinaryAssociation = BinaryAssociation(
    name="statement_list434",
    ends={
        Property(name="Statement_List", type=iec61131_st_If_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_If_Statement435", type=Statement_List, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
else_if436: BinaryAssociation = BinaryAssociation(
    name="else_if436",
    ends={
        Property(name="Else_If_Statement", type=iec61131_st_If_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_If_Statement437", type=Else_If_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assignment465: BinaryAssociation = BinaryAssociation(
    name="assignment465",
    ends={
        Property(name="Assignment_Symbol467", type=iec61131_st_For_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_For_Statement466", type=Assignment_Symbol, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
else440: BinaryAssociation = BinaryAssociation(
    name="else440",
    ends={
        Property(name="Else_Statement441", type=iec61131_st_Case_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Case_Statement", type=Else_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression442: BinaryAssociation = BinaryAssociation(
    name="expression442",
    ends={
        Property(name="Expression_Types444", type=iec61131_st_Case_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Case_Statement443", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
case_element445: BinaryAssociation = BinaryAssociation(
    name="case_element445",
    ends={
        Property(name="Case_Element", type=iec61131_st_Case_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Case_Statement446", type=Case_Element, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expression447: BinaryAssociation = BinaryAssociation(
    name="expression447",
    ends={
        Property(name="Expression_Types448", type=iec61131_st_Else_If_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Else_If_Statement", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement_list449: BinaryAssociation = BinaryAssociation(
    name="statement_list449",
    ends={
        Property(name="Statement_List451", type=iec61131_st_Else_If_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Else_If_Statement450", type=Statement_List, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement_list452: BinaryAssociation = BinaryAssociation(
    name="statement_list452",
    ends={
        Property(name="Statement_List453", type=iec61131_st_Else_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Else_Statement", type=Statement_List, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
case_list454: BinaryAssociation = BinaryAssociation(
    name="case_list454",
    ends={
        Property(name="Case_List", type=iec61131_st_Case_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Case_Element", type=Case_List, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement_list455: BinaryAssociation = BinaryAssociation(
    name="statement_list455",
    ends={
        Property(name="Statement_List457", type=iec61131_st_Case_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Case_Element456", type=Statement_List, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
case_list_element458: BinaryAssociation = BinaryAssociation(
    name="case_list_element458",
    ends={
        Property(name="Case_List_Element", type=iec61131_st_Case_List, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Case_List", type=Case_List_Element, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
control_variable459: BinaryAssociation = BinaryAssociation(
    name="control_variable459",
    ends={
        Property(name="Control_Variable", type=iec61131_st_For_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_For_Statement", type=Control_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
for_list460: BinaryAssociation = BinaryAssociation(
    name="for_list460",
    ends={
        Property(name="For_List", type=iec61131_st_For_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_For_Statement461", type=For_List, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement_list462: BinaryAssociation = BinaryAssociation(
    name="statement_list462",
    ends={
        Property(name="Statement_List464", type=iec61131_st_For_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_For_Statement463", type=Statement_List, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression468: BinaryAssociation = BinaryAssociation(
    name="expression468",
    ends={
        Property(name="Expression_Types469", type=iec61131_st_While_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_While_Statement", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement_list470: BinaryAssociation = BinaryAssociation(
    name="statement_list470",
    ends={
        Property(name="Statement_List472", type=iec61131_st_While_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_While_Statement471", type=Statement_List, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression473: BinaryAssociation = BinaryAssociation(
    name="expression473",
    ends={
        Property(name="Expression_Types474", type=iec61131_st_Repeat_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Repeat_Statement", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statement_list475: BinaryAssociation = BinaryAssociation(
    name="statement_list475",
    ends={
        Property(name="Statement_List477", type=iec61131_st_Repeat_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Repeat_Statement476", type=Statement_List, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression478: BinaryAssociation = BinaryAssociation(
    name="expression478",
    ends={
        Property(name="Expression_Types479", type=iec61131_st_For_List, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_For_List", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
to_expression480: BinaryAssociation = BinaryAssociation(
    name="to_expression480",
    ends={
        Property(name="Expression_Types482", type=iec61131_st_For_List, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_For_List481", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
by_expression483: BinaryAssociation = BinaryAssociation(
    name="by_expression483",
    ends={
        Property(name="Expression_Types485", type=iec61131_st_For_List, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_For_List484", type=Expression_Types, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
xor_expression_left486: BinaryAssociation = BinaryAssociation(
    name="xor_expression_left486",
    ends={
        Property(name="Expression_Types487", type=iec61131_st_Xor_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Xor_Expression", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
xor488: BinaryAssociation = BinaryAssociation(
    name="xor488",
    ends={
        Property(name="Xor_Operator", type=iec61131_st_Xor_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Xor_Expression489", type=Xor_Operator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
xor_expression_right490: BinaryAssociation = BinaryAssociation(
    name="xor_expression_right490",
    ends={
        Property(name="Expression_Types492", type=iec61131_st_Xor_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Xor_Expression491", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
and_expression_left493: BinaryAssociation = BinaryAssociation(
    name="and_expression_left493",
    ends={
        Property(name="Expression_Types494", type=iec61131_st_And_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_And_Expression", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
add_expression_right516: BinaryAssociation = BinaryAssociation(
    name="add_expression_right516",
    ends={
        Property(name="Expression_Types518", type=iec61131_st_Add_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Add_Expression517", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
and495: BinaryAssociation = BinaryAssociation(
    name="and495",
    ends={
        Property(name="And_Operator", type=iec61131_st_And_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_And_Expression496", type=And_Operator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
and_expression_right497: BinaryAssociation = BinaryAssociation(
    name="and_expression_right497",
    ends={
        Property(name="Expression_Types499", type=iec61131_st_And_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_And_Expression498", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
comparison_expression_left500: BinaryAssociation = BinaryAssociation(
    name="comparison_expression_left500",
    ends={
        Property(name="Expression_Types501", type=iec61131_st_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Comparison", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
comparison_expression_right502: BinaryAssociation = BinaryAssociation(
    name="comparison_expression_right502",
    ends={
        Property(name="Expression_Types504", type=iec61131_st_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Comparison503", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
equ_operator505: BinaryAssociation = BinaryAssociation(
    name="equ_operator505",
    ends={
        Property(name="EquUequ_Operator", type=iec61131_st_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Comparison506", type=EquUequ_Operator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
equ_expression_left507: BinaryAssociation = BinaryAssociation(
    name="equ_expression_left507",
    ends={
        Property(name="Expression_Types508", type=iec61131_st_Equ_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Equ_Expression", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
equ_expression_right509: BinaryAssociation = BinaryAssociation(
    name="equ_expression_right509",
    ends={
        Property(name="Expression_Types511", type=iec61131_st_Equ_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Equ_Expression510", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
comparison_operator512: BinaryAssociation = BinaryAssociation(
    name="comparison_operator512",
    ends={
        Property(name="Comparison_Operator", type=iec61131_st_Equ_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Equ_Expression513", type=Comparison_Operator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
add_expression_left514: BinaryAssociation = BinaryAssociation(
    name="add_expression_left514",
    ends={
        Property(name="Expression_Types515", type=iec61131_st_Add_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Add_Expression", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
add_operator519: BinaryAssociation = BinaryAssociation(
    name="add_operator519",
    ends={
        Property(name="Add_Operator", type=iec61131_st_Add_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Add_Expression520", type=Add_Operator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
term_expression_left521: BinaryAssociation = BinaryAssociation(
    name="term_expression_left521",
    ends={
        Property(name="Expression_Types522", type=iec61131_st_Term_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Term_Expression", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
term_expression_right523: BinaryAssociation = BinaryAssociation(
    name="term_expression_right523",
    ends={
        Property(name="Expression_Types525", type=iec61131_st_Term_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Term_Expression524", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
multiply_operator526: BinaryAssociation = BinaryAssociation(
    name="multiply_operator526",
    ends={
        Property(name="Dot_Operator", type=iec61131_st_Term_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Term_Expression527", type=Dot_Operator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
power528: BinaryAssociation = BinaryAssociation(
    name="power528",
    ends={
        Property(name="Power_Symbol", type=iec61131_st_Power_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Power_Expression", type=Power_Symbol, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
power_expression_left529: BinaryAssociation = BinaryAssociation(
    name="power_expression_left529",
    ends={
        Property(name="Expression_Types531", type=iec61131_st_Power_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Power_Expression530", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
power_expression_right532: BinaryAssociation = BinaryAssociation(
    name="power_expression_right532",
    ends={
        Property(name="Expression_Types534", type=iec61131_st_Power_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Power_Expression533", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
unary_operator535: BinaryAssociation = BinaryAssociation(
    name="unary_operator535",
    ends={
        Property(name="Unary_Operator", type=iec61131_st_Unary_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Unary_Expression", type=Unary_Operator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
unary_expression536: BinaryAssociation = BinaryAssociation(
    name="unary_expression536",
    ends={
        Property(name="Expression_Types538", type=iec61131_st_Unary_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Unary_Expression537", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression539: BinaryAssociation = BinaryAssociation(
    name="expression539",
    ends={
        Property(name="Expression_Types540", type=iec61131_st_Bracket_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Bracket_Expression", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
param_assignment541: BinaryAssociation = BinaryAssociation(
    name="param_assignment541",
    ends={
        Property(name="Param_Assignment542", type=iec61131_st_Call_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Call_Expression", type=Param_Assignment, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
function_name543: BinaryAssociation = BinaryAssociation(
    name="function_name543",
    ends={
        Property(name="Function_Name", type=iec61131_st_Call_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Call_Expression544", type=Function_Name, multiplicity=Multiplicity(1, 1))
    }
)
variable545: BinaryAssociation = BinaryAssociation(
    name="variable545",
    ends={
        Property(name="Variable_Name546", type=iec61131_st_Expression_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Expression_Variable", type=Variable_Name, multiplicity=Multiplicity(0, 1))
    }
)
direct_variable547: BinaryAssociation = BinaryAssociation(
    name="direct_variable547",
    ends={
        Property(name="Direct_Variable549", type=iec61131_st_Expression_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Expression_Variable548", type=Direct_Variable, multiplicity=Multiplicity(0, 1))
    }
)
array_variable550: BinaryAssociation = BinaryAssociation(
    name="array_variable550",
    ends={
        Property(name="Array_Variable", type=iec61131_st_Expression_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Expression_Variable551", type=Array_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structured_variable552: BinaryAssociation = BinaryAssociation(
    name="structured_variable552",
    ends={
        Property(name="Structured_Variable", type=iec61131_st_Expression_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Expression_Variable553", type=Structured_Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constant554: BinaryAssociation = BinaryAssociation(
    name="constant554",
    ends={
        Property(name="Constant555", type=iec61131_st_Expression_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Expression_Constant", type=Constant, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
enum_value556: BinaryAssociation = BinaryAssociation(
    name="enum_value556",
    ends={
        Property(name="Enumerated_Value557", type=iec61131_st_Expression_EnumValue, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Expression_EnumValue", type=Enumerated_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression_variable558: BinaryAssociation = BinaryAssociation(
    name="expression_variable558",
    ends={
        Property(name="Expression_Variable559", type=iec61131_st_Expression_Variable_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_st_Expression_Variable_Type", type=Expression_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operands578: BinaryAssociation = BinaryAssociation(
    name="operands578",
    ends={
        Property(name="Operands", type=iec61131_il_Il_Fb_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Il_Fb_Call579", type=Operands, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
il_instruction560: BinaryAssociation = BinaryAssociation(
    name="il_instruction560",
    ends={
        Property(name="Il_Instruction", type=iec61131_il_Instruction_List, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Instruction_List", type=Il_Instruction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
il_simple_instruction561: BinaryAssociation = BinaryAssociation(
    name="il_simple_instruction561",
    ends={
        Property(name="Il_Simple_Instruction", type=iec61131_il_Simple_Instr_List, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Simple_Instr_List", type=Il_Simple_Instruction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
label562: BinaryAssociation = BinaryAssociation(
    name="label562",
    ends={
        Property(name="Label", type=iec61131_il_Il_Instruction, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Il_Instruction", type=Label, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
il_operation563: BinaryAssociation = BinaryAssociation(
    name="il_operation563",
    ends={
        Property(name="Il_Operations", type=iec61131_il_Il_Instruction, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Il_Instruction564", type=Il_Operations, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
il_expr_operator565: BinaryAssociation = BinaryAssociation(
    name="il_expr_operator565",
    ends={
        Property(name="Il_Expr_Operator", type=iec61131_il_Il_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Il_Expression", type=Il_Expr_Operator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
il_operand566: BinaryAssociation = BinaryAssociation(
    name="il_operand566",
    ends={
        Property(name="Il_Operand", type=iec61131_il_Il_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Il_Expression567", type=Il_Operand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simple_instr_list568: BinaryAssociation = BinaryAssociation(
    name="simple_instr_list568",
    ends={
        Property(name="Simple_Instr_List", type=iec61131_il_Il_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Il_Expression569", type=Simple_Instr_List, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
label570: BinaryAssociation = BinaryAssociation(
    name="label570",
    ends={
        Property(name="Label571", type=iec61131_il_Il_Jump_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Il_Jump_Operation", type=Label, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
il_jump_operator572: BinaryAssociation = BinaryAssociation(
    name="il_jump_operator572",
    ends={
        Property(name="Il_Jump_Operator", type=iec61131_il_Il_Jump_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Il_Jump_Operation573", type=Il_Jump_Operator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
il_call_operator574: BinaryAssociation = BinaryAssociation(
    name="il_call_operator574",
    ends={
        Property(name="Il_Call_Operator", type=iec61131_il_Il_Fb_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Il_Fb_Call", type=Il_Call_Operator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fb_name575: BinaryAssociation = BinaryAssociation(
    name="fb_name575",
    ends={
        Property(name="Variable_Name577", type=iec61131_il_Il_Fb_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Il_Fb_Call576", type=Variable_Name, multiplicity=Multiplicity(1, 1))
    }
)
il_param_list597: BinaryAssociation = BinaryAssociation(
    name="il_param_list597",
    ends={
        Property(name="Il_Param_List598", type=iec61131_il_Operand1, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Operand1", type=Il_Param_List, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function_name580: BinaryAssociation = BinaryAssociation(
    name="function_name580",
    ends={
        Property(name="Function_Name581", type=iec61131_il_Il_Formal_Funct_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Il_Formal_Funct_Call", type=Function_Name, multiplicity=Multiplicity(1, 1))
    }
)
il_param_list582: BinaryAssociation = BinaryAssociation(
    name="il_param_list582",
    ends={
        Property(name="Il_Param_List", type=iec61131_il_Il_Formal_Funct_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Il_Formal_Funct_Call583", type=Il_Param_List, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
il_operand584: BinaryAssociation = BinaryAssociation(
    name="il_operand584",
    ends={
        Property(name="Il_Operand585", type=iec61131_il_Il_Operand_List, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Il_Operand_List", type=Il_Operand, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
il_simple_operator586: BinaryAssociation = BinaryAssociation(
    name="il_simple_operator586",
    ends={
        Property(name="Il_Simple_Operator", type=iec61131_il_Simple_Operation1, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Simple_Operation1", type=Il_Simple_Operator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
il_operand587: BinaryAssociation = BinaryAssociation(
    name="il_operand587",
    ends={
        Property(name="Il_Operand589", type=iec61131_il_Simple_Operation1, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Simple_Operation1588", type=Il_Operand, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function_name590: BinaryAssociation = BinaryAssociation(
    name="function_name590",
    ends={
        Property(name="Function_Name591", type=iec61131_il_Simple_Operation2, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Simple_Operation2", type=Function_Name, multiplicity=Multiplicity(1, 1))
    }
)
il_operand_list592: BinaryAssociation = BinaryAssociation(
    name="il_operand_list592",
    ends={
        Property(name="Il_Operand_List", type=iec61131_il_Simple_Operation2, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Simple_Operation2593", type=Il_Operand_List, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
il_param_instruction594: BinaryAssociation = BinaryAssociation(
    name="il_param_instruction594",
    ends={
        Property(name="Il_Param_Instruction", type=iec61131_il_Il_Param_List, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Il_Param_List", type=Il_Param_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
il_param_last_instruction595: BinaryAssociation = BinaryAssociation(
    name="il_param_last_instruction595",
    ends={
        Property(name="Il_Param_Last_Instruction", type=iec61131_il_Il_Param_List, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Il_Param_List596", type=Il_Param_Last_Instruction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
il_operand_list599: BinaryAssociation = BinaryAssociation(
    name="il_operand_list599",
    ends={
        Property(name="Il_Operand_List600", type=iec61131_il_Operand2, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Operand2", type=Il_Operand_List, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
simple_inst601: BinaryAssociation = BinaryAssociation(
    name="simple_inst601",
    ends={
        Property(name="Simple_Instr", type=iec61131_il_Il_Simple_Instruction, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Il_Simple_Instruction", type=Simple_Instr, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
il_assign_operator602: BinaryAssociation = BinaryAssociation(
    name="il_assign_operator602",
    ends={
        Property(name="Il_Assign_Operator", type=iec61131_il_Il_Param_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Il_Param_Assignment", type=Il_Assign_Operator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sfc_network622: BinaryAssociation = BinaryAssociation(
    name="sfc_network622",
    ends={
        Property(name="Sfc_Network", type=iec61131_sfc_Sequential_Function_Chart, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_sfc_Sequential_Function_Chart", type=Sfc_Network, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
initial_step623: BinaryAssociation = BinaryAssociation(
    name="initial_step623",
    ends={
        Property(name="Initial_Step", type=iec61131_sfc_Sfc_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_sfc_Sfc_Network", type=Initial_Step, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
param_assignment603: BinaryAssociation = BinaryAssociation(
    name="param_assignment603",
    ends={
        Property(name="Param_Assignment605", type=iec61131_il_Il_Param_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Il_Param_Assignment604", type=Param_Assignment, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable606: BinaryAssociation = BinaryAssociation(
    name="variable606",
    ends={
        Property(name="Variable607", type=iec61131_il_Il_Param_Out_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Il_Param_Out_Assignment", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
il_assign_out_operator608: BinaryAssociation = BinaryAssociation(
    name="il_assign_out_operator608",
    ends={
        Property(name="Il_Assign_Out_Operator", type=iec61131_il_Il_Param_Out_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Il_Param_Out_Assignment609", type=Il_Assign_Out_Operator, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
param_assignment610: BinaryAssociation = BinaryAssociation(
    name="param_assignment610",
    ends={
        Property(name="Param_Assignments", type=iec61131_il_Param_Instruction, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Param_Instruction", type=Param_Assignments, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable_name611: BinaryAssociation = BinaryAssociation(
    name="variable_name611",
    ends={
        Property(name="Variable_Name612", type=iec61131_il_Il_Assign_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Il_Assign_Operator", type=Variable_Name, multiplicity=Multiplicity(1, 1))
    }
)
assignment613: BinaryAssociation = BinaryAssociation(
    name="assignment613",
    ends={
        Property(name="Assignment_Name", type=iec61131_il_Il_Assign_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Il_Assign_Operator614", type=Assignment_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
simple_instr_list615: BinaryAssociation = BinaryAssociation(
    name="simple_instr_list615",
    ends={
        Property(name="Simple_Instr_List616", type=iec61131_il_Param_Assignment2, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Param_Assignment2", type=Simple_Instr_List, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
not617: BinaryAssociation = BinaryAssociation(
    name="not617",
    ends={
        Property(name="Not_Operator618", type=iec61131_il_Il_Assign_Out_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Il_Assign_Out_Operator", type=Not_Operator, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable_name619: BinaryAssociation = BinaryAssociation(
    name="variable_name619",
    ends={
        Property(name="Variable_Name621", type=iec61131_il_Il_Assign_Out_Operator, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_il_Il_Assign_Out_Operator620", type=Variable_Name, multiplicity=Multiplicity(1, 1))
    }
)
indicator_name645: BinaryAssociation = BinaryAssociation(
    name="indicator_name645",
    ends={
        Property(name="Variable_Name647", type=iec61131_sfc_Action_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_sfc_Action_Association646", type=Variable_Name, multiplicity=Multiplicity(0, 9999))
    }
)
action_association648: BinaryAssociation = BinaryAssociation(
    name="action_association648",
    ends={
        Property(name="Action_Association", type=iec61131_sfc_Step_Types, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_sfc_Step_Types", type=Action_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sfc_elements624: BinaryAssociation = BinaryAssociation(
    name="sfc_elements624",
    ends={
        Property(name="Sfc_Elements", type=iec61131_sfc_Sfc_Network, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_sfc_Sfc_Network625", type=Sfc_Elements, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition_name626: BinaryAssociation = BinaryAssociation(
    name="transition_name626",
    ends={
        Property(name="Transition_Name", type=iec61131_sfc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_sfc_Transition", type=Transition_Name, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment627: BinaryAssociation = BinaryAssociation(
    name="assignment627",
    ends={
        Property(name="Assignment_Symbol629", type=iec61131_sfc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_sfc_Transition628", type=Assignment_Symbol, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
steps630: BinaryAssociation = BinaryAssociation(
    name="steps630",
    ends={
        Property(name="Steps", type=iec61131_sfc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_sfc_Transition631", type=Steps, multiplicity=Multiplicity(2, 2), is_composite=True)
    }
)
transition_condition632: BinaryAssociation = BinaryAssociation(
    name="transition_condition632",
    ends={
        Property(name="Transition_Condition", type=iec61131_sfc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_sfc_Transition633", type=Transition_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
integer634: BinaryAssociation = BinaryAssociation(
    name="integer634",
    ends={
        Property(name="Unsigned_Integer636", type=iec61131_sfc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_sfc_Transition635", type=Unsigned_Integer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action_name637: BinaryAssociation = BinaryAssociation(
    name="action_name637",
    ends={
        Property(name="Action_Name", type=iec61131_sfc_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_sfc_Action", type=Action_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
function_block_body638: BinaryAssociation = BinaryAssociation(
    name="function_block_body638",
    ends={
        Property(name="Function_Block_Body640", type=iec61131_sfc_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_sfc_Action639", type=Function_Block_Body, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
action_name641: BinaryAssociation = BinaryAssociation(
    name="action_name641",
    ends={
        Property(name="Action_Name642", type=iec61131_sfc_Action_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_sfc_Action_Association", type=Action_Name, multiplicity=Multiplicity(1, 1))
    }
)
action_qualifier643: BinaryAssociation = BinaryAssociation(
    name="action_qualifier643",
    ends={
        Property(name="Action_Qualifier", type=iec61131_sfc_Action_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_sfc_Action_Association644", type=Action_Qualifier, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition658: BinaryAssociation = BinaryAssociation(
    name="condition658",
    ends={
        Property(name="Cond2_Condition", type=iec61131_sfc_Transition_Cond2, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_sfc_Transition_Cond2", type=Cond2_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
step_name649: BinaryAssociation = BinaryAssociation(
    name="step_name649",
    ends={
        Property(name="Step_Name", type=iec61131_sfc_Step_Types, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_sfc_Step_Types650", type=Step_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
timed_qualifier651: BinaryAssociation = BinaryAssociation(
    name="timed_qualifier651",
    ends={
        Property(name="Timed_Qualifier", type=iec61131_sfc_Action_Qualifier, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_sfc_Action_Qualifier", type=Timed_Qualifier, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
action_time652: BinaryAssociation = BinaryAssociation(
    name="action_time652",
    ends={
        Property(name="Action_Time", type=iec61131_sfc_Action_Qualifier, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_sfc_Action_Qualifier653", type=Action_Time, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
step_name654: BinaryAssociation = BinaryAssociation(
    name="step_name654",
    ends={
        Property(name="Step_Name655", type=iec61131_sfc_Steps1, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_sfc_Steps1", type=Step_Name, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
field_selector674: BinaryAssociation = BinaryAssociation(
    name="field_selector674",
    ends={
        Property(name="Variable_Name676", type=iec61131_variables_Structured_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_variables_Structured_Variable675", type=Variable_Name, multiplicity=Multiplicity(1, 1))
    }
)
step_name656: BinaryAssociation = BinaryAssociation(
    name="step_name656",
    ends={
        Property(name="Step_Name657", type=iec61131_sfc_Steps2, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_sfc_Steps2", type=Step_Name, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
simple_instr_list659: BinaryAssociation = BinaryAssociation(
    name="simple_instr_list659",
    ends={
        Property(name="Il_Simple_Instruction660", type=iec61131_sfc_Transition_Cond1, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_sfc_Transition_Cond1", type=Il_Simple_Instruction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression661: BinaryAssociation = BinaryAssociation(
    name="expression661",
    ends={
        Property(name="Expression_Types662", type=iec61131_sfc_Transition_Cond3, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_sfc_Transition_Cond3", type=Expression_Types, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assignment663: BinaryAssociation = BinaryAssociation(
    name="assignment663",
    ends={
        Property(name="Assignment_Symbol665", type=iec61131_sfc_Transition_Cond3, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_sfc_Transition_Cond3664", type=Assignment_Symbol, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
time_variable666: BinaryAssociation = BinaryAssociation(
    name="time_variable666",
    ends={
        Property(name="Variable_Name667", type=iec61131_sfc_ActionTime2, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_sfc_ActionTime2", type=Variable_Name, multiplicity=Multiplicity(1, 1))
    }
)
subscripted_variable668: BinaryAssociation = BinaryAssociation(
    name="subscripted_variable668",
    ends={
        Property(name="Symbolic_Variable669", type=iec61131_variables_Array_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_variables_Array_Variable", type=Symbolic_Variable, multiplicity=Multiplicity(1, 1))
    }
)
subscript_list670: BinaryAssociation = BinaryAssociation(
    name="subscript_list670",
    ends={
        Property(name="Subscript_List", type=iec61131_variables_Array_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_variables_Array_Variable671", type=Subscript_List, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
record_variable672: BinaryAssociation = BinaryAssociation(
    name="record_variable672",
    ends={
        Property(name="Symbolic_Variable673", type=iec61131_variables_Structured_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_variables_Structured_Variable", type=Symbolic_Variable, multiplicity=Multiplicity(1, 1))
    }
)
subscript677: BinaryAssociation = BinaryAssociation(
    name="subscript677",
    ends={
        Property(name="Expression_Types678", type=iec61131_variables_Subscript_List, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_variables_Subscript_List", type=Expression_Types, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
fbd_network679: BinaryAssociation = BinaryAssociation(
    name="fbd_network679",
    ends={
        Property(name="Fbd_Network", type=iec61131_fbd_Function_Block_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_fbd_Function_Block_Diagram", type=Fbd_Network, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
types680: BinaryAssociation = BinaryAssociation(
    name="types680",
    ends={
        Property(name="Data_Type_Name", type=iec61131_types_TypeLib, multiplicity=Multiplicity(1, 1)),
        Property(name="iec61131_types_TypeLib", type=Data_Type_Name, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_iec61131_Library_Element_Declaration_Commentable = Generalization(general=Commentable, specific=iec61131_Library_Element_Declaration)
gen_iec61131_Library_Element_Name_NamedElement = Generalization(general=NamedElement, specific=iec61131_Library_Element_Name)
gen_iec61131_literals_Numeric_Literal_Constant = Generalization(general=Constant, specific=iec61131_literals_Numeric_Literal)
gen_iec61131_literals_Character_String_Constant = Generalization(general=Constant, specific=iec61131_literals_Character_String)
gen_iec61131_literals_Real_Literal_Numeric_Literal = Generalization(general=Numeric_Literal, specific=iec61131_literals_Real_Literal)
gen_iec61131_literals_Boolean_Literal_Constant = Generalization(general=Constant, specific=iec61131_literals_Boolean_Literal)
gen_iec61131_literals_Time_Literal_Constant = Generalization(general=Constant, specific=iec61131_literals_Time_Literal)
gen_iec61131_literals_Constant_configurations_Data_Source = Generalization(general=configurations_Data_Source, specific=iec61131_literals_Constant)
gen_iec61131_literals_Bit_String_Literal_Constant = Generalization(general=Constant, specific=iec61131_literals_Bit_String_Literal)
gen_iec61131_literals_Constant_configurations_Prog_Data_Source = Generalization(general=configurations_Prog_Data_Source, specific=iec61131_literals_Constant)
gen_iec61131_literals_Constant_il_Il_Operand = Generalization(general=il_Il_Operand, specific=iec61131_literals_Constant)
gen_iec61131_literals_Integer_Literal_Numeric_Literal = Generalization(general=Numeric_Literal, specific=iec61131_literals_Integer_Literal)
gen_iec61131_literals_Octal_Integer_literals_BSInteger = Generalization(general=literals_BSInteger, specific=iec61131_literals_Octal_Integer)
gen_iec61131_literals_Hex_Integer_literals_Integer = Generalization(general=literals_Integer, specific=iec61131_literals_Hex_Integer)
gen_iec61131_literals_Hex_Integer_literals_BSInteger = Generalization(general=literals_BSInteger, specific=iec61131_literals_Hex_Integer)
gen_iec61131_literals_Duration_literals_Time_Literal = Generalization(general=literals_Time_Literal, specific=iec61131_literals_Duration)
gen_iec61131_literals_Duration_sfc_Action_Time = Generalization(general=sfc_Action_Time, specific=iec61131_literals_Duration)
gen_iec61131_literals_Time_Of_Day_Time_Literal = Generalization(general=Time_Literal, specific=iec61131_literals_Time_Of_Day)
gen_iec61131_literals_Signed_Integer_literals_Integer = Generalization(general=literals_Integer, specific=iec61131_literals_Signed_Integer)
gen_iec61131_literals_Signed_Integer_st_Case_List_Element = Generalization(general=st_Case_List_Element, specific=iec61131_literals_Signed_Integer)
gen_iec61131_literals_Signed_Integer_interfaces_Range = Generalization(general=interfaces_Range, specific=iec61131_literals_Signed_Integer)
gen_iec61131_literals_Binary_Integer_literals_Integer = Generalization(general=literals_Integer, specific=iec61131_literals_Binary_Integer)
gen_iec61131_literals_Binary_Integer_literals_BSInteger = Generalization(general=literals_BSInteger, specific=iec61131_literals_Binary_Integer)
gen_iec61131_literals_Octal_Integer_literals_Integer = Generalization(general=literals_Integer, specific=iec61131_literals_Octal_Integer)
gen_iec61131_literals_Date_And_Time_Time_Literal = Generalization(general=Time_Literal, specific=iec61131_literals_Date_And_Time)
gen_iec61131_literals_Unsigned_Integer_st_Case_List_Element = Generalization(general=st_Case_List_Element, specific=iec61131_literals_Unsigned_Integer)
gen_iec61131_literals_Unsigned_Integer_interfaces_Range = Generalization(general=interfaces_Range, specific=iec61131_literals_Unsigned_Integer)
gen_iec61131_literals_Unsigned_Integer_literals_Integer = Generalization(general=literals_Integer, specific=iec61131_literals_Unsigned_Integer)
gen_iec61131_literals_Unsigned_Integer_literals_BSInteger = Generalization(general=literals_BSInteger, specific=iec61131_literals_Unsigned_Integer)
gen_iec61131_literals_Unsigned_Integer_literals_Fixed_Point_Literal = Generalization(general=literals_Fixed_Point_Literal, specific=iec61131_literals_Unsigned_Integer)
gen_iec61131_literals_Date_Time_Literal = Generalization(general=Time_Literal, specific=iec61131_literals_Date)
gen_iec61131_literals_Minutes_Interval = Generalization(general=Interval, specific=iec61131_literals_Minutes)
gen_iec61131_literals_Seconds_Interval = Generalization(general=Interval, specific=iec61131_literals_Seconds)
gen_iec61131_literals_Days_Interval = Generalization(general=Interval, specific=iec61131_literals_Days)
gen_iec61131_literals_Hours_Interval = Generalization(general=Interval, specific=iec61131_literals_Hours)
gen_iec61131_literals_Milliseconds_Interval = Generalization(general=Interval, specific=iec61131_literals_Milliseconds)
gen_iec61131_literals_Single_Byte_Character_String_Character_String = Generalization(general=Character_String, specific=iec61131_literals_Single_Byte_Character_String)
gen_iec61131_literals_Double_Byte_Character_String_Character_String = Generalization(general=Character_String, specific=iec61131_literals_Double_Byte_Character_String)
gen_iec61131_literals_Fixed_Point_Fixed_Point_Literal = Generalization(general=Fixed_Point_Literal, specific=iec61131_literals_Fixed_Point)
gen_iec61131_operators_Add_Operator_Operator = Generalization(general=Operator, specific=iec61131_operators_Add_Operator)
gen_iec61131_operators_Unary_Operator_Operator = Generalization(general=Operator, specific=iec61131_operators_Unary_Operator)
gen_iec61131_operators_Assignment_Operator_Operator = Generalization(general=Operator, specific=iec61131_operators_Assignment_Operator)
gen_iec61131_operators_Not_Operator_il_Il_Simple_Operator = Generalization(general=il_Il_Simple_Operator, specific=iec61131_operators_Not_Operator)
gen_iec61131_operators_Power_Operator_Operator = Generalization(general=Operator, specific=iec61131_operators_Power_Operator)
gen_iec61131_operators_Modulo_Operator_il_Il_Expr_Operator = Generalization(general=il_Il_Expr_Operator, specific=iec61131_operators_Modulo_Operator)
gen_iec61131_operators_Modulo_Operator_operators_Dot_Operator = Generalization(general=operators_Dot_Operator, specific=iec61131_operators_Modulo_Operator)
gen_iec61131_operators_Divide_Operator_Dot_Operator = Generalization(general=Dot_Operator, specific=iec61131_operators_Divide_Operator)
gen_iec61131_operators_Less_Operator_Comparison_Operator = Generalization(general=Comparison_Operator, specific=iec61131_operators_Less_Operator)
gen_iec61131_operators_Greater_Operator_Comparison_Operator = Generalization(general=Comparison_Operator, specific=iec61131_operators_Greater_Operator)
gen_iec61131_operators_GreaterEqual_Operator_Comparison_Operator = Generalization(general=Comparison_Operator, specific=iec61131_operators_GreaterEqual_Operator)
gen_iec61131_operators_LessEqual_Operator_Comparison_Operator = Generalization(general=Comparison_Operator, specific=iec61131_operators_LessEqual_Operator)
gen_iec61131_operators_Unequal_Operator_EquUequ_Operator = Generalization(general=EquUequ_Operator, specific=iec61131_operators_Unequal_Operator)
gen_iec61131_operators_Comparison_Operator_Operator = Generalization(general=Operator, specific=iec61131_operators_Comparison_Operator)
gen_iec61131_operators_Multiply_Operator_Dot_Operator = Generalization(general=Dot_Operator, specific=iec61131_operators_Multiply_Operator)
gen_iec61131_operators_Equal_Operator_EquUequ_Operator = Generalization(general=EquUequ_Operator, specific=iec61131_operators_Equal_Operator)
gen_iec61131_operators_And_Operator_operators_Operator = Generalization(general=operators_Operator, specific=iec61131_operators_And_Operator)
gen_iec61131_operators_And_Operator_il_Il_Expr_Operator = Generalization(general=il_Il_Expr_Operator, specific=iec61131_operators_And_Operator)
gen_iec61131_operators_Or_Operator_operators_Operator = Generalization(general=operators_Operator, specific=iec61131_operators_Or_Operator)
gen_iec61131_operators_Or_Operator_il_Il_Expr_Operator = Generalization(general=il_Il_Expr_Operator, specific=iec61131_operators_Or_Operator)
gen_iec61131_operators_Xor_Operator_operators_Operator = Generalization(general=operators_Operator, specific=iec61131_operators_Xor_Operator)
gen_iec61131_operators_Xor_Operator_il_Il_Expr_Operator = Generalization(general=il_Il_Expr_Operator, specific=iec61131_operators_Xor_Operator)
gen_iec61131_operators_Not_Operator_operators_Unary_Operator = Generalization(general=operators_Unary_Operator, specific=iec61131_operators_Not_Operator)
gen_iec61131_operators_Divide_Name_operators_Arithmetic_Name = Generalization(general=operators_Arithmetic_Name, specific=iec61131_operators_Divide_Name)
gen_iec61131_operators_Divide_Symbol_Divide_Operator = Generalization(general=Divide_Operator, specific=iec61131_operators_Divide_Symbol)
gen_iec61131_operators_Power_Symbol_Power_Operator = Generalization(general=Power_Operator, specific=iec61131_operators_Power_Symbol)
gen_iec61131_operators_Power_Name_Power_Operator = Generalization(general=Power_Operator, specific=iec61131_operators_Power_Name)
gen_iec61131_operators_Assignment_Symbol_Assignment_Operator = Generalization(general=Assignment_Operator, specific=iec61131_operators_Assignment_Symbol)
gen_iec61131_operators_Assignment_Name_Assignment_Operator = Generalization(general=Assignment_Operator, specific=iec61131_operators_Assignment_Name)
gen_iec61131_operators_And_Symbol_And_Operator = Generalization(general=And_Operator, specific=iec61131_operators_And_Symbol)
gen_iec61131_operators_And_Name_And_Operator = Generalization(general=And_Operator, specific=iec61131_operators_And_Name)
gen_iec61131_operators_Equal_Name_operators_Equal_Operator = Generalization(general=operators_Equal_Operator, specific=iec61131_operators_Equal_Name)
gen_iec61131_operators_Equal_Name_operators_Comparison_Name = Generalization(general=operators_Comparison_Name, specific=iec61131_operators_Equal_Name)
gen_iec61131_operators_Addition_Name_operators_Addition_Operator = Generalization(general=operators_Addition_Operator, specific=iec61131_operators_Addition_Name)
gen_iec61131_operators_Addition_Name_operators_Arithmetic_Name = Generalization(general=operators_Arithmetic_Name, specific=iec61131_operators_Addition_Name)
gen_iec61131_operators_Addition_Symbol_operators_Addition_Operator = Generalization(general=operators_Addition_Operator, specific=iec61131_operators_Addition_Symbol)
gen_iec61131_operators_Addition_Symbol_operators_Add_Operator = Generalization(general=operators_Add_Operator, specific=iec61131_operators_Addition_Symbol)
gen_iec61131_operators_Dot_Operator_Operator = Generalization(general=Operator, specific=iec61131_operators_Dot_Operator)
gen_iec61131_operators_Multiply_Name_operators_Multiply_Operator = Generalization(general=operators_Multiply_Operator, specific=iec61131_operators_Multiply_Name)
gen_iec61131_operators_Multiply_Name_operators_Arithmetic_Name = Generalization(general=operators_Arithmetic_Name, specific=iec61131_operators_Multiply_Name)
gen_iec61131_operators_Multiply_Symbol_Multiply_Operator = Generalization(general=Multiply_Operator, specific=iec61131_operators_Multiply_Symbol)
gen_iec61131_operators_Divide_Name_operators_Divide_Operator = Generalization(general=operators_Divide_Operator, specific=iec61131_operators_Divide_Name)
gen_iec61131_operators_Greater_Name_operators_Greater_Operator = Generalization(general=operators_Greater_Operator, specific=iec61131_operators_Greater_Name)
gen_iec61131_operators_Greater_Name_operators_Comparison_Name = Generalization(general=operators_Comparison_Name, specific=iec61131_operators_Greater_Name)
gen_iec61131_operators_Greater_Symbol_Greater_Operator = Generalization(general=Greater_Operator, specific=iec61131_operators_Greater_Symbol)
gen_iec61131_operators_GreaterEqual_Name_operators_GreaterEqual_Operator = Generalization(general=operators_GreaterEqual_Operator, specific=iec61131_operators_GreaterEqual_Name)
gen_iec61131_operators_GreaterEqual_Name_operators_Comparison_Name = Generalization(general=operators_Comparison_Name, specific=iec61131_operators_GreaterEqual_Name)
gen_iec61131_operators_GreaterEqual_Symbol_GreaterEqual_Operator = Generalization(general=GreaterEqual_Operator, specific=iec61131_operators_GreaterEqual_Symbol)
gen_iec61131_operators_Substraction_Name_operators_Substraction_Operator = Generalization(general=operators_Substraction_Operator, specific=iec61131_operators_Substraction_Name)
gen_iec61131_operators_Substraction_Name_operators_Arithmetic_Name = Generalization(general=operators_Arithmetic_Name, specific=iec61131_operators_Substraction_Name)
gen_iec61131_operators_Substraction_Symbol_operators_Substraction_Operator = Generalization(general=operators_Substraction_Operator, specific=iec61131_operators_Substraction_Symbol)
gen_iec61131_operators_Substraction_Symbol_operators_Unary_Operator = Generalization(general=operators_Unary_Operator, specific=iec61131_operators_Substraction_Symbol)
gen_iec61131_operators_Substraction_Symbol_operators_Add_Operator = Generalization(general=operators_Add_Operator, specific=iec61131_operators_Substraction_Symbol)
gen_iec61131_operators_EquUequ_Operator_Operator = Generalization(general=Operator, specific=iec61131_operators_EquUequ_Operator)
gen_iec61131_operators_Comparison_Name_Il_Expr_Operator = Generalization(general=Il_Expr_Operator, specific=iec61131_operators_Comparison_Name)
gen_iec61131_operators_Equal_Symbol_Equal_Operator = Generalization(general=Equal_Operator, specific=iec61131_operators_Equal_Symbol)
gen_iec61131_operators_Unequal_Name_operators_Unequal_Operator = Generalization(general=operators_Unequal_Operator, specific=iec61131_operators_Unequal_Name)
gen_iec61131_operators_Unequal_Name_operators_Comparison_Name = Generalization(general=operators_Comparison_Name, specific=iec61131_operators_Unequal_Name)
gen_iec61131_operators_Unequal_Symbol_Unequal_Operator = Generalization(general=Unequal_Operator, specific=iec61131_operators_Unequal_Symbol)
gen_iec61131_operators_Less_Name_operators_Less_Operator = Generalization(general=operators_Less_Operator, specific=iec61131_operators_Less_Name)
gen_iec61131_operators_Less_Name_operators_Comparison_Name = Generalization(general=operators_Comparison_Name, specific=iec61131_operators_Less_Name)
gen_iec61131_operators_Less_Symbol_Less_Operator = Generalization(general=Less_Operator, specific=iec61131_operators_Less_Symbol)
gen_iec61131_operators_LessEqual_Name_operators_LessEqual_Operator = Generalization(general=operators_LessEqual_Operator, specific=iec61131_operators_LessEqual_Name)
gen_iec61131_operators_LessEqual_Name_operators_Comparison_Name = Generalization(general=operators_Comparison_Name, specific=iec61131_operators_LessEqual_Name)
gen_iec61131_operators_LessEqual_Symbol_LessEqual_Operator = Generalization(general=LessEqual_Operator, specific=iec61131_operators_LessEqual_Symbol)
gen_iec61131_interfaces_Var_Init_Decl_Input_Declaration = Generalization(general=Input_Declaration, specific=iec61131_interfaces_Var_Init_Decl)
gen_iec61131_interfaces_Var1_Init_Decl_Var_Init_Decl = Generalization(general=Var_Init_Decl, specific=iec61131_interfaces_Var1_Init_Decl)
gen_iec61131_interfaces_Edge_Declaration_Input_Declaration = Generalization(general=Input_Declaration, specific=iec61131_interfaces_Edge_Declaration)
gen_iec61131_operators_Arithmetic_Name_Il_Expr_Operator = Generalization(general=Il_Expr_Operator, specific=iec61131_operators_Arithmetic_Name)
gen_iec61131_interfaces_Io_Var_Declaration_interfaces_Interface = Generalization(general=interfaces_Interface, specific=iec61131_interfaces_Io_Var_Declaration)
gen_iec61131_interfaces_Io_Var_Declaration_pous_Function_Block_Vars = Generalization(general=pous_Function_Block_Vars, specific=iec61131_interfaces_Io_Var_Declaration)
gen_iec61131_interfaces_Io_Var_Declaration_pous_Program_Vars = Generalization(general=pous_Program_Vars, specific=iec61131_interfaces_Io_Var_Declaration)
gen_iec61131_interfaces_Io_Var_Declaration_pous_Function_Vars = Generalization(general=pous_Function_Vars, specific=iec61131_interfaces_Io_Var_Declaration)
gen_iec61131_interfaces_Input_Declarations_Io_Var_Declaration = Generalization(general=Io_Var_Declaration, specific=iec61131_interfaces_Input_Declarations)
gen_iec61131_interfaces_Subrange_Spec_Init_interfaces_Var1_Specification = Generalization(general=interfaces_Var1_Specification, specific=iec61131_interfaces_Subrange_Spec_Init)
gen_iec61131_interfaces_Subrange_Spec_Init_interfaces_Located_Var_Spec_Init = Generalization(general=interfaces_Located_Var_Spec_Init, specific=iec61131_interfaces_Subrange_Spec_Init)
gen_iec61131_interfaces_Subrange_Spec_Init_pous_Structure_Elements = Generalization(general=pous_Structure_Elements, specific=iec61131_interfaces_Subrange_Spec_Init)
gen_iec61131_interfaces_Subrange_Spec_Init_interfaces_Var1_Specification_Func = Generalization(general=interfaces_Var1_Specification_Func, specific=iec61131_interfaces_Subrange_Spec_Init)
gen_iec61131_interfaces_Enumerated_Spec_Init_interfaces_Var1_Specification = Generalization(general=interfaces_Var1_Specification, specific=iec61131_interfaces_Enumerated_Spec_Init)
gen_iec61131_interfaces_Enumerated_Spec_Init_interfaces_Located_Var_Spec_Init = Generalization(general=interfaces_Located_Var_Spec_Init, specific=iec61131_interfaces_Enumerated_Spec_Init)
gen_iec61131_interfaces_Enumerated_Spec_Init_pous_Structure_Elements = Generalization(general=pous_Structure_Elements, specific=iec61131_interfaces_Enumerated_Spec_Init)
gen_iec61131_interfaces_Enumerated_Spec_Init_interfaces_Var1_Specification_Func = Generalization(general=interfaces_Var1_Specification_Func, specific=iec61131_interfaces_Enumerated_Spec_Init)
gen_iec61131_interfaces_Simple_Spec_Init_interfaces_Var1_Specification = Generalization(general=interfaces_Var1_Specification, specific=iec61131_interfaces_Simple_Spec_Init)
gen_iec61131_interfaces_Simple_Spec_Init_interfaces_Located_Var_Spec_Init = Generalization(general=interfaces_Located_Var_Spec_Init, specific=iec61131_interfaces_Simple_Spec_Init)
gen_iec61131_interfaces_Simple_Spec_Init_pous_Structure_Elements = Generalization(general=pous_Structure_Elements, specific=iec61131_interfaces_Simple_Spec_Init)
gen_iec61131_interfaces_Fb_Name_Decl_Temp_Var_Declaration = Generalization(general=Temp_Var_Declaration, specific=iec61131_interfaces_Fb_Name_Decl)
gen_iec61131_interfaces_String_Var_Declaration_interfaces_Temp_Var_Decl = Generalization(general=interfaces_Temp_Var_Decl, specific=iec61131_interfaces_String_Var_Declaration)
gen_iec61131_interfaces_String_Var_Declaration_interfaces_Var2_Init_Decl = Generalization(general=interfaces_Var2_Init_Decl, specific=iec61131_interfaces_String_Var_Declaration)
gen_iec61131_interfaces_Output_Declarations_Io_Var_Declaration = Generalization(general=Io_Var_Declaration, specific=iec61131_interfaces_Output_Declarations)
gen_iec61131_interfaces_Array_Var_Init_Decl_Var2_Init_Decl = Generalization(general=Var2_Init_Decl, specific=iec61131_interfaces_Array_Var_Init_Decl)
gen_iec61131_interfaces_Structured_Var_Init_Decl_Var2_Init_Decl = Generalization(general=Var2_Init_Decl, specific=iec61131_interfaces_Structured_Var_Init_Decl)
gen_iec61131_interfaces_Initialized_Structure_interfaces_Located_Var_Spec_Init = Generalization(general=interfaces_Located_Var_Spec_Init, specific=iec61131_interfaces_Initialized_Structure)
gen_iec61131_interfaces_Initialized_Structure_pous_Structure_Specification = Generalization(general=pous_Structure_Specification, specific=iec61131_interfaces_Initialized_Structure)
gen_iec61131_interfaces_Initialized_Structure_pous_Structure_Elements = Generalization(general=pous_Structure_Elements, specific=iec61131_interfaces_Initialized_Structure)
gen_iec61131_interfaces_Input_Output_Declarations_Io_Var_Declaration = Generalization(general=Io_Var_Declaration, specific=iec61131_interfaces_Input_Output_Declarations)
gen_iec61131_interfaces_Array_Spec_Init_interfaces_Located_Var_Spec_Init = Generalization(general=interfaces_Located_Var_Spec_Init, specific=iec61131_interfaces_Array_Spec_Init)
gen_iec61131_interfaces_Array_Spec_Init_pous_Structure_Elements = Generalization(general=pous_Structure_Elements, specific=iec61131_interfaces_Array_Spec_Init)
gen_iec61131_interfaces_Enumerated_Value_st_Case_List_Element = Generalization(general=st_Case_List_Element, specific=iec61131_interfaces_Enumerated_Value)
gen_iec61131_interfaces_Enumerated_Value_configurations_Prog_Data_Source = Generalization(general=configurations_Prog_Data_Source, specific=iec61131_interfaces_Enumerated_Value)
gen_iec61131_interfaces_Enumerated_Value_il_Il_Operand = Generalization(general=il_Il_Operand, specific=iec61131_interfaces_Enumerated_Value)
gen_iec61131_interfaces_Temp_Var_Decl_Var_Declaration = Generalization(general=Var_Declaration, specific=iec61131_interfaces_Temp_Var_Decl)
gen_iec61131_interfaces_Array_Var_Declaration_Temp_Var_Declaration = Generalization(general=Temp_Var_Declaration, specific=iec61131_interfaces_Array_Var_Declaration)
gen_iec61131_interfaces_Structured_Var_Declaration_Temp_Var_Declaration = Generalization(general=Temp_Var_Declaration, specific=iec61131_interfaces_Structured_Var_Declaration)
gen_iec61131_interfaces_Subrange_Specification_interfaces_Specification = Generalization(general=interfaces_Specification, specific=iec61131_interfaces_Subrange_Specification)
gen_iec61131_interfaces_Subrange_Specification_interfaces_External_Specification = Generalization(general=interfaces_External_Specification, specific=iec61131_interfaces_Subrange_Specification)
gen_iec61131_interfaces_Var1_Declaration_Temp_Var_Declaration = Generalization(general=Temp_Var_Declaration, specific=iec61131_interfaces_Var1_Declaration)
gen_iec61131_interfaces_Double_Byte_String_Spec_Located_Var_Spec_Init = Generalization(general=Located_Var_Spec_Init, specific=iec61131_interfaces_Double_Byte_String_Spec)
gen_iec61131_interfaces_Subrange_Specification_interfaces_Var_Spec = Generalization(general=interfaces_Var_Spec, specific=iec61131_interfaces_Subrange_Specification)
gen_iec61131_interfaces_Enumerated_Specification_interfaces_Specification = Generalization(general=interfaces_Specification, specific=iec61131_interfaces_Enumerated_Specification)
gen_iec61131_interfaces_Enumerated_Specification_interfaces_External_Specification = Generalization(general=interfaces_External_Specification, specific=iec61131_interfaces_Enumerated_Specification)
gen_iec61131_interfaces_Enumerated_Specification_interfaces_Var_Spec = Generalization(general=interfaces_Var_Spec, specific=iec61131_interfaces_Enumerated_Specification)
gen_iec61131_interfaces_Single_Byte_String_Var_Declaration_String_Var_Declaration = Generalization(general=String_Var_Declaration, specific=iec61131_interfaces_Single_Byte_String_Var_Declaration)
gen_iec61131_interfaces_Array_Specification_interfaces_External_Specification = Generalization(general=interfaces_External_Specification, specific=iec61131_interfaces_Array_Specification)
gen_iec61131_interfaces_Array_Specification_interfaces_Var_Spec = Generalization(general=interfaces_Var_Spec, specific=iec61131_interfaces_Array_Specification)
gen_iec61131_interfaces_Double_Byte_String_Var_Declaration_String_Var_Declaration = Generalization(general=String_Var_Declaration, specific=iec61131_interfaces_Double_Byte_String_Var_Declaration)
gen_iec61131_interfaces_Subrange_Case_List_Element = Generalization(general=Case_List_Element, specific=iec61131_interfaces_Subrange)
gen_iec61131_interfaces_Single_Byte_String_Spec_Located_Var_Spec_Init = Generalization(general=Located_Var_Spec_Init, specific=iec61131_interfaces_Single_Byte_String_Spec)
gen_iec61131_interfaces_Interface_Commentable = Generalization(general=Commentable, specific=iec61131_interfaces_Interface)
gen_iec61131_interfaces_Other_Var_Declaration_interfaces_Interface = Generalization(general=interfaces_Interface, specific=iec61131_interfaces_Other_Var_Declaration)
gen_iec61131_interfaces_Other_Var_Declaration_pous_Function_Block_Vars = Generalization(general=pous_Function_Block_Vars, specific=iec61131_interfaces_Other_Var_Declaration)
gen_iec61131_interfaces_Other_Var_Declaration_pous_Program_Vars = Generalization(general=pous_Program_Vars, specific=iec61131_interfaces_Other_Var_Declaration)
gen_iec61131_interfaces_External_Var_Declarations_Other_Var_Declaration = Generalization(general=Other_Var_Declaration, specific=iec61131_interfaces_External_Var_Declarations)
gen_iec61131_interfaces_Retentive_Var_Declarations_RNV_Declarations = Generalization(general=RNV_Declarations, specific=iec61131_interfaces_Retentive_Var_Declarations)
gen_iec61131_interfaces_Non_Retentive_Var_Declarations_RNV_Declarations = Generalization(general=RNV_Declarations, specific=iec61131_interfaces_Non_Retentive_Var_Declarations)
gen_iec61131_interfaces_Global_Var_Name_Library_Element_Name = Generalization(general=Library_Element_Name, specific=iec61131_interfaces_Global_Var_Name)
gen_iec61131_interfaces_Global_Var_Name_Commentable = Generalization(general=Commentable, specific=iec61131_interfaces_Global_Var_Name)
gen_iec61131_interfaces_Global_Var_List_Global_Var_Spec = Generalization(general=Global_Var_Spec, specific=iec61131_interfaces_Global_Var_List)
gen_iec61131_interfaces_Temp_Var_Decls_Other_Var_Declaration = Generalization(general=Other_Var_Declaration, specific=iec61131_interfaces_Temp_Var_Decls)
gen_iec61131_interfaces_Var_Declarations_RNV_Declarations = Generalization(general=RNV_Declarations, specific=iec61131_interfaces_Var_Declarations)
gen_iec61131_interfaces_Incompl_Located_Var_Declarations_Other_Var_Declaration = Generalization(general=Other_Var_Declaration, specific=iec61131_interfaces_Incompl_Located_Var_Declarations)
gen_iec61131_interfaces_RNV_Declarations_Other_Var_Declaration = Generalization(general=Other_Var_Declaration, specific=iec61131_interfaces_RNV_Declarations)
gen_iec61131_interfaces_Located_Var_Declarations_Program_Vars = Generalization(general=Program_Vars, specific=iec61131_interfaces_Located_Var_Declarations)
gen_iec61131_interfaces_Global_Var_Declarations_Library_Element_Declaration = Generalization(general=Library_Element_Declaration, specific=iec61131_interfaces_Global_Var_Declarations)
gen_iec61131_interfaces_Global_Var_Decl_Commentable = Generalization(general=Commentable, specific=iec61131_interfaces_Global_Var_Decl)
gen_iec61131_interfaces_Global_Var_Location_Global_Var_Spec = Generalization(general=Global_Var_Spec, specific=iec61131_interfaces_Global_Var_Location)
gen_iec61131_interfaces_Subrange_Specification2_Subrange_Specification = Generalization(general=Subrange_Specification, specific=iec61131_interfaces_Subrange_Specification2)
gen_iec61131_interfaces_Byte_String_Var_Spec = Generalization(general=Var_Spec, specific=iec61131_interfaces_Byte_String)
gen_iec61131_interfaces_Single_BString_Byte_String = Generalization(general=Byte_String, specific=iec61131_interfaces_Single_BString)
gen_iec61131_interfaces_Double_BString_Byte_String = Generalization(general=Byte_String, specific=iec61131_interfaces_Double_BString)
gen_iec61131_interfaces_Subrange_Specification1_Subrange_Specification = Generalization(general=Subrange_Specification, specific=iec61131_interfaces_Subrange_Specification1)
gen_iec61131_interfaces_Array_Initial_Elements1_Array_Initial_Elements = Generalization(general=Array_Initial_Elements, specific=iec61131_interfaces_Array_Initial_Elements1)
gen_iec61131_interfaces_Enumerated_Specification1_Enumerated_Specification = Generalization(general=Enumerated_Specification, specific=iec61131_interfaces_Enumerated_Specification1)
gen_iec61131_interfaces_Enumerated_Specification2_Enumerated_Specification = Generalization(general=Enumerated_Specification, specific=iec61131_interfaces_Enumerated_Specification2)
gen_iec61131_interfaces_Array_Specification1_Array_Specification = Generalization(general=Array_Specification, specific=iec61131_interfaces_Array_Specification1)
gen_iec61131_interfaces_Array_Specification2_Array_Specification = Generalization(general=Array_Specification, specific=iec61131_interfaces_Array_Specification2)
gen_iec61131_interfaces_Array_Initial_Elements2_Array_Initial_Elements = Generalization(general=Array_Initial_Elements, specific=iec61131_interfaces_Array_Initial_Elements2)
gen_iec61131_interfaces_InitElement_Constant_Initial_Element = Generalization(general=Initial_Element, specific=iec61131_interfaces_InitElement_Constant)
gen_iec61131_interfaces_InitElement_EnumValue_Initial_Element = Generalization(general=Initial_Element, specific=iec61131_interfaces_InitElement_EnumValue)
gen_iec61131_interfaces_InitElement_Structure_Initial_Element = Generalization(general=Initial_Element, specific=iec61131_interfaces_InitElement_Structure)
gen_iec61131_interfaces_InitElement_Array_Initial_Element = Generalization(general=Initial_Element, specific=iec61131_interfaces_InitElement_Array)
gen_iec61131_interfaces_Var2_Init_Decl_Var_Init_Decl = Generalization(general=Var_Init_Decl, specific=iec61131_interfaces_Var2_Init_Decl)
gen_iec61131_interfaces_Function_Var_Decl_pous_Function_Vars = Generalization(general=pous_Function_Vars, specific=iec61131_interfaces_Function_Var_Decl)
gen_iec61131_interfaces_Function_Var_Decl_interfaces_Interface = Generalization(general=interfaces_Interface, specific=iec61131_interfaces_Function_Var_Decl)
gen_iec61131_interfaces_Var1_Specification_Func_Var1_Specification = Generalization(general=Var1_Specification, specific=iec61131_interfaces_Var1_Specification_Func)
gen_iec61131_interfaces_Var_Name_Decl_Simple_Spec_Init = Generalization(general=Simple_Spec_Init, specific=iec61131_interfaces_Var_Name_Decl)
gen_iec61131_interfaces_Var_Init_Decl_Func_Var2_Init_Decl = Generalization(general=Var2_Init_Decl, specific=iec61131_interfaces_Var_Init_Decl_Func)
gen_iec61131_interfaces_Simple_Spec_Init_Func_Var1_Specification_Func = Generalization(general=Var1_Specification_Func, specific=iec61131_interfaces_Simple_Spec_Init_Func)
gen_iec61131_pous_Derived_Function_Block_Name_pous_Function_Block_Type_Name = Generalization(general=pous_Function_Block_Type_Name, specific=iec61131_pous_Derived_Function_Block_Name)
gen_iec61131_pous_Derived_Function_Block_Name_Blocks = Generalization(general=Blocks, specific=iec61131_pous_Derived_Function_Block_Name)
gen_iec61131_pous_Function_Block_Declaration_Library_Element_Declaration = Generalization(general=Library_Element_Declaration, specific=iec61131_pous_Function_Block_Declaration)
gen_iec61131_interfaces_Temp_Var_Declaration_Temp_Var_Decl = Generalization(general=Temp_Var_Decl, specific=iec61131_interfaces_Temp_Var_Declaration)
gen_iec61131_pous_Program_Declaration_Library_Element_Declaration = Generalization(general=Library_Element_Declaration, specific=iec61131_pous_Program_Declaration)
gen_iec61131_pous_Program_Type_Name_Library_Element_Name = Generalization(general=Library_Element_Name, specific=iec61131_pous_Program_Type_Name)
gen_iec61131_pous_Program_Type_Name_Blocks = Generalization(general=Blocks, specific=iec61131_pous_Program_Type_Name)
gen_iec61131_pous_Function_Block_Type_Name_Library_Element_Name = Generalization(general=Library_Element_Name, specific=iec61131_pous_Function_Block_Type_Name)
gen_iec61131_pous_Function_Block_Type_Name_interfaces_External_Specification = Generalization(general=interfaces_External_Specification, specific=iec61131_pous_Function_Block_Type_Name)
gen_iec61131_pous_Function_Block_Type_Name_Commentable = Generalization(general=Commentable, specific=iec61131_pous_Function_Block_Type_Name)
gen_iec61131_pous_Function_Block_Type_Name_types_Simple_Specification = Generalization(general=types_Simple_Specification, specific=iec61131_pous_Function_Block_Type_Name)
gen_iec61131_pous_Function_Declaration_Library_Element_Declaration = Generalization(general=Library_Element_Declaration, specific=iec61131_pous_Function_Declaration)
gen_iec61131_pous_Derived_Function_Name_pous_Function_Name = Generalization(general=pous_Function_Name, specific=iec61131_pous_Derived_Function_Name)
gen_iec61131_pous_Derived_Function_Name_Blocks = Generalization(general=Blocks, specific=iec61131_pous_Derived_Function_Name)
gen_iec61131_pous_Other_Language_pous_Function_Body = Generalization(general=pous_Function_Body, specific=iec61131_pous_Other_Language)
gen_iec61131_pous_Other_Language_pous_Function_Block_Body = Generalization(general=pous_Function_Block_Body, specific=iec61131_pous_Other_Language)
gen_iec61131_pous_Function_Name_Library_Element_Name = Generalization(general=Library_Element_Name, specific=iec61131_pous_Function_Name)
gen_iec61131_pous_Data_Type_Declaration_Library_Element_Declaration = Generalization(general=Library_Element_Declaration, specific=iec61131_pous_Data_Type_Declaration)
gen_iec61131_pous_Single_Element_Type_Declaration_Type_Declaration = Generalization(general=Type_Declaration, specific=iec61131_pous_Single_Element_Type_Declaration)
gen_iec61131_pous_Array_Type_Declaration_Type_Declaration = Generalization(general=Type_Declaration, specific=iec61131_pous_Array_Type_Declaration)
gen_iec61131_pous_Structure_Type_Declaration_Type_Declaration = Generalization(general=Type_Declaration, specific=iec61131_pous_Structure_Type_Declaration)
gen_iec61131_pous_String_Type_Declaration_Type_Declaration = Generalization(general=Type_Declaration, specific=iec61131_pous_String_Type_Declaration)
gen_iec61131_pous_Simple_Type_Declaration_Single_Element_Type_Declaration = Generalization(general=Single_Element_Type_Declaration, specific=iec61131_pous_Simple_Type_Declaration)
gen_iec61131_pous_Subrange_Type_Declaration_Single_Element_Type_Declaration = Generalization(general=Single_Element_Type_Declaration, specific=iec61131_pous_Subrange_Type_Declaration)
gen_iec61131_pous_Enumerated_Type_Declaration_Single_Element_Type_Declaration = Generalization(general=Single_Element_Type_Declaration, specific=iec61131_pous_Enumerated_Type_Declaration)
gen_iec61131_pous_Structure_Declaration_Structure_Specification = Generalization(general=Structure_Specification, specific=iec61131_pous_Structure_Declaration)
gen_iec61131_pous_Program_Access_Decls_Program_Vars = Generalization(general=Program_Vars, specific=iec61131_pous_Program_Access_Decls)
gen_iec61131_configurations_Configuration_Name_Library_Element_Name = Generalization(general=Library_Element_Name, specific=iec61131_configurations_Configuration_Name)
gen_iec61131_configurations_Resource_Type_Name_Library_Element_Name = Generalization(general=Library_Element_Name, specific=iec61131_configurations_Resource_Type_Name)
gen_iec61131_configurations_Configuration_Declaration_Library_Element_Declaration = Generalization(general=Library_Element_Declaration, specific=iec61131_configurations_Configuration_Declaration)
gen_iec61131_configurations_Resource_Declaration_Library_Element_Declaration = Generalization(general=Library_Element_Declaration, specific=iec61131_configurations_Resource_Declaration)
gen_iec61131_configurations_Program_Configuration_Commentable = Generalization(general=Commentable, specific=iec61131_configurations_Program_Configuration)
gen_iec61131_configurations_Global_Var_Reference_configurations_Data_Source = Generalization(general=configurations_Data_Source, specific=iec61131_configurations_Global_Var_Reference)
gen_iec61131_configurations_Global_Var_Reference_configurations_Data_Sink = Generalization(general=configurations_Data_Sink, specific=iec61131_configurations_Global_Var_Reference)
gen_iec61131_configurations_Global_Var_Reference_configurations_Prog_Data_Source = Generalization(general=configurations_Prog_Data_Source, specific=iec61131_configurations_Global_Var_Reference)
gen_iec61131_configurations_Program_Output_Reference_Data_Source = Generalization(general=Data_Source, specific=iec61131_configurations_Program_Output_Reference)
gen_iec61131_configurations_Prog_Cnxn_Prog_Conf_Element = Generalization(general=Prog_Conf_Element, specific=iec61131_configurations_Prog_Cnxn)
gen_iec61131_configurations_Direct_Path_Access_Path = Generalization(general=Access_Path, specific=iec61131_configurations_Direct_Path)
gen_iec61131_configurations_Symbolic_Path_Access_Path = Generalization(general=Access_Path, specific=iec61131_configurations_Symbolic_Path)
gen_iec61131_configurations_Fb_Task_Prog_Conf_Element = Generalization(general=Prog_Conf_Element, specific=iec61131_configurations_Fb_Task)
gen_iec61131_configurations_Prog_Sink_Prog_Cnxn = Generalization(general=Prog_Cnxn, specific=iec61131_configurations_Prog_Sink)
gen_iec61131_configurations_Prog_Source_Prog_Cnxn = Generalization(general=Prog_Cnxn, specific=iec61131_configurations_Prog_Source)
gen_iec61131_configurations_Instance_Spec1_Instance_Specific_Init = Generalization(general=Instance_Specific_Init, specific=iec61131_configurations_Instance_Spec1)
gen_iec61131_configurations_Instance_Spec2_Instance_Specific_Init = Generalization(general=Instance_Specific_Init, specific=iec61131_configurations_Instance_Spec2)
gen_iec61131_st_Subprogram_Control_Statement_Statement = Generalization(general=Statement, specific=iec61131_st_Subprogram_Control_Statement)
gen_iec61131_st_Selection_Statement_Statement = Generalization(general=Statement, specific=iec61131_st_Selection_Statement)
gen_iec61131_configurations_Single_Task_Initialization = Generalization(general=Task_Initialization, specific=iec61131_configurations_Single)
gen_iec61131_configurations_Interval_Task_Initialization = Generalization(general=Task_Initialization, specific=iec61131_configurations_Interval)
gen_iec61131_configurations_Priority_Task_Initialization = Generalization(general=Task_Initialization, specific=iec61131_configurations_Priority)
gen_iec61131_st_Statement_List_pous_Function_Body = Generalization(general=pous_Function_Body, specific=iec61131_st_Statement_List)
gen_iec61131_st_Statement_List_pous_Function_Block_Body = Generalization(general=pous_Function_Block_Body, specific=iec61131_st_Statement_List)
gen_iec61131_st_Expression_Expression_Types = Generalization(general=Expression_Types, specific=iec61131_st_Expression)
gen_iec61131_st_Statement_Commentable = Generalization(general=Commentable, specific=iec61131_st_Statement)
gen_iec61131_st_Assignment_Statement_Statement = Generalization(general=Statement, specific=iec61131_st_Assignment_Statement)
gen_iec61131_st_Case_Statement_Selection_Statement = Generalization(general=Selection_Statement, specific=iec61131_st_Case_Statement)
gen_iec61131_st_Iteration_Statement_Statement = Generalization(general=Statement, specific=iec61131_st_Iteration_Statement)
gen_iec61131_st_Return_Statement_Subprogram_Control_Statement = Generalization(general=Subprogram_Control_Statement, specific=iec61131_st_Return_Statement)
gen_iec61131_st_Fb_Invocation_Subprogram_Control_Statement = Generalization(general=Subprogram_Control_Statement, specific=iec61131_st_Fb_Invocation)
gen_iec61131_st_Param_Assignment_Commentable = Generalization(general=Commentable, specific=iec61131_st_Param_Assignment)
gen_iec61131_st_Param_Type1_Param_Assignment = Generalization(general=Param_Assignment, specific=iec61131_st_Param_Type1)
gen_iec61131_st_Param_Type2_Param_Assignment = Generalization(general=Param_Assignment, specific=iec61131_st_Param_Type2)
gen_iec61131_st_If_Statement_Selection_Statement = Generalization(general=Selection_Statement, specific=iec61131_st_If_Statement)
gen_iec61131_st_For_Statement_Iteration_Statement = Generalization(general=Iteration_Statement, specific=iec61131_st_For_Statement)
gen_iec61131_st_While_Statement_Iteration_Statement = Generalization(general=Iteration_Statement, specific=iec61131_st_While_Statement)
gen_iec61131_st_Repeat_Statement_Iteration_Statement = Generalization(general=Iteration_Statement, specific=iec61131_st_Repeat_Statement)
gen_iec61131_st_Exit_Statement_Iteration_Statement = Generalization(general=Iteration_Statement, specific=iec61131_st_Exit_Statement)
gen_iec61131_st_Xor_Expression_Expression_Types = Generalization(general=Expression_Types, specific=iec61131_st_Xor_Expression)
gen_iec61131_st_And_Expression_Expression_Types = Generalization(general=Expression_Types, specific=iec61131_st_And_Expression)
gen_iec61131_st_Comparison_Expression_Types = Generalization(general=Expression_Types, specific=iec61131_st_Comparison)
gen_iec61131_st_Equ_Expression_Expression_Types = Generalization(general=Expression_Types, specific=iec61131_st_Equ_Expression)
gen_iec61131_st_Add_Expression_Expression_Types = Generalization(general=Expression_Types, specific=iec61131_st_Add_Expression)
gen_iec61131_st_Term_Expression_Expression_Types = Generalization(general=Expression_Types, specific=iec61131_st_Term_Expression)
gen_iec61131_st_Power_Expression_Expression_Types = Generalization(general=Expression_Types, specific=iec61131_st_Power_Expression)
gen_iec61131_st_Unary_Expression_Expression_Types = Generalization(general=Expression_Types, specific=iec61131_st_Unary_Expression)
gen_iec61131_il_Instruction_List_pous_Function_Body = Generalization(general=pous_Function_Body, specific=iec61131_il_Instruction_List)
gen_iec61131_il_Instruction_List_pous_Function_Block_Body = Generalization(general=pous_Function_Block_Body, specific=iec61131_il_Instruction_List)
gen_iec61131_st_Primary_Expression_Expression_Types = Generalization(general=Expression_Types, specific=iec61131_st_Primary_Expression)
gen_iec61131_st_Bracket_Expression_Primary_Expression = Generalization(general=Primary_Expression, specific=iec61131_st_Bracket_Expression)
gen_iec61131_st_Call_Expression_Primary_Expression = Generalization(general=Primary_Expression, specific=iec61131_st_Call_Expression)
gen_iec61131_st_Expression_Types_Commentable = Generalization(general=Commentable, specific=iec61131_st_Expression_Types)
gen_iec61131_st_Expression_Variable_Commentable = Generalization(general=Commentable, specific=iec61131_st_Expression_Variable)
gen_iec61131_st_Expression_Constant_Primary_Expression = Generalization(general=Primary_Expression, specific=iec61131_st_Expression_Constant)
gen_iec61131_st_Expression_EnumValue_Primary_Expression = Generalization(general=Primary_Expression, specific=iec61131_st_Expression_EnumValue)
gen_iec61131_st_Expression_Variable_Type_Primary_Expression = Generalization(general=Primary_Expression, specific=iec61131_st_Expression_Variable_Type)
gen_iec61131_il_Il_Formal_Funct_Call_il_Il_Operations = Generalization(general=il_Il_Operations, specific=iec61131_il_Il_Formal_Funct_Call)
gen_iec61131_il_Il_Formal_Funct_Call_il_Simple_Instr = Generalization(general=il_Simple_Instr, specific=iec61131_il_Il_Formal_Funct_Call)
gen_iec61131_il_Il_Simple_Operation_il_Il_Operations = Generalization(general=il_Il_Operations, specific=iec61131_il_Il_Simple_Operation)
gen_iec61131_il_Il_Simple_Operation_il_Simple_Instr = Generalization(general=il_Simple_Instr, specific=iec61131_il_Il_Simple_Operation)
gen_iec61131_il_Il_Expression_il_Il_Operations = Generalization(general=il_Il_Operations, specific=iec61131_il_Il_Expression)
gen_iec61131_il_Il_Expression_il_Simple_Instr = Generalization(general=il_Simple_Instr, specific=iec61131_il_Il_Expression)
gen_iec61131_il_Il_Jump_Operation_Il_Operations = Generalization(general=Il_Operations, specific=iec61131_il_Il_Jump_Operation)
gen_iec61131_il_Il_Fb_Call_Il_Operations = Generalization(general=Il_Operations, specific=iec61131_il_Il_Fb_Call)
gen_iec61131_il_Operand2_Operands = Generalization(general=Operands, specific=iec61131_il_Operand2)
gen_iec61131_il_Il_Return_Operator_Il_Operations = Generalization(general=Il_Operations, specific=iec61131_il_Il_Return_Operator)
gen_iec61131_il_Il_Operand_Param_Assignment = Generalization(general=Param_Assignment, specific=iec61131_il_Il_Operand)
gen_iec61131_il_Simple_Operation1_Il_Simple_Operation = Generalization(general=Il_Simple_Operation, specific=iec61131_il_Simple_Operation1)
gen_iec61131_il_Simple_Operation2_Il_Simple_Operation = Generalization(general=Il_Simple_Operation, specific=iec61131_il_Simple_Operation2)
gen_iec61131_il_Il_Expr_Operator_Il_Simple_Operator = Generalization(general=Il_Simple_Operator, specific=iec61131_il_Il_Expr_Operator)
gen_iec61131_il_Operand1_Operands = Generalization(general=Operands, specific=iec61131_il_Operand1)
gen_iec61131_il_Il_Param_Instruction_Param_Instruction = Generalization(general=Param_Instruction, specific=iec61131_il_Il_Param_Instruction)
gen_iec61131_il_Il_Param_Last_Instruction_Param_Instruction = Generalization(general=Param_Instruction, specific=iec61131_il_Il_Param_Last_Instruction)
gen_iec61131_il_Il_Param_Assignment_Param_Assignments = Generalization(general=Param_Assignments, specific=iec61131_il_Il_Param_Assignment)
gen_iec61131_il_Il_Param_Out_Assignment_Param_Assignments = Generalization(general=Param_Assignments, specific=iec61131_il_Il_Param_Out_Assignment)
gen_iec61131_il_Param_Assignment2_Param_Assignment = Generalization(general=Param_Assignment, specific=iec61131_il_Param_Assignment2)
gen_iec61131_sfc_Sequential_Function_Chart_Function_Block_Body = Generalization(general=Function_Block_Body, specific=iec61131_sfc_Sequential_Function_Chart)
gen_iec61131_sfc_Initial_Step_Step_Types = Generalization(general=Step_Types, specific=iec61131_sfc_Initial_Step)
gen_iec61131_sfc_Step_sfc_Sfc_Elements = Generalization(general=sfc_Sfc_Elements, specific=iec61131_sfc_Step)
gen_iec61131_sfc_Step_sfc_Step_Types = Generalization(general=sfc_Step_Types, specific=iec61131_sfc_Step)
gen_iec61131_sfc_Transition_Sfc_Elements = Generalization(general=Sfc_Elements, specific=iec61131_sfc_Transition)
gen_iec61131_sfc_Action_Sfc_Elements = Generalization(general=Sfc_Elements, specific=iec61131_sfc_Action)
gen_iec61131_sfc_Step_Name_NamedElement = Generalization(general=NamedElement, specific=iec61131_sfc_Step_Name)
gen_iec61131_sfc_Transition_Cond2_Transition_Condition = Generalization(general=Transition_Condition, specific=iec61131_sfc_Transition_Cond2)
gen_iec61131_sfc_Steps1_Steps = Generalization(general=Steps, specific=iec61131_sfc_Steps1)
gen_iec61131_sfc_Steps2_Steps = Generalization(general=Steps, specific=iec61131_sfc_Steps2)
gen_iec61131_sfc_Transition_Cond1_Transition_Condition = Generalization(general=Transition_Condition, specific=iec61131_sfc_Transition_Cond1)
gen_iec61131_sfc_Transition_Cond3_Transition_Condition = Generalization(general=Transition_Condition, specific=iec61131_sfc_Transition_Cond3)
gen_iec61131_sfc_ActionTime2_Action_Time = Generalization(general=Action_Time, specific=iec61131_sfc_ActionTime2)
gen_iec61131_variables_Symbolic_Variable_Variable = Generalization(general=Variable, specific=iec61131_variables_Symbolic_Variable)
gen_iec61131_variables_Multi_Element_Variable_Symbolic_Variable = Generalization(general=Symbolic_Variable, specific=iec61131_variables_Multi_Element_Variable)
gen_iec61131_variables_Array_Variable_Multi_Element_Variable = Generalization(general=Multi_Element_Variable, specific=iec61131_variables_Array_Variable)
gen_iec61131_variables_Structured_Variable_Multi_Element_Variable = Generalization(general=Multi_Element_Variable, specific=iec61131_variables_Structured_Variable)
gen_iec61131_types_Date_Type_Name_Elementary_Type_Name = Generalization(general=Elementary_Type_Name, specific=iec61131_types_Date_Type_Name)
gen_iec61131_types_Bit_String_Type_Name_Elementary_Type_Name = Generalization(general=Elementary_Type_Name, specific=iec61131_types_Bit_String_Type_Name)
gen_iec61131_variables_Direct_Variable_variables_Variable = Generalization(general=variables_Variable, specific=iec61131_variables_Direct_Variable)
gen_iec61131_variables_Direct_Variable_configurations_Data_Source = Generalization(general=configurations_Data_Source, specific=iec61131_variables_Direct_Variable)
gen_iec61131_variables_Direct_Variable_configurations_Data_Sink = Generalization(general=configurations_Data_Sink, specific=iec61131_variables_Direct_Variable)
gen_iec61131_variables_Direct_Variable_configurations_Prog_Data_Source = Generalization(general=configurations_Prog_Data_Source, specific=iec61131_variables_Direct_Variable)
gen_iec61131_variables_Variable_il_Il_Operand = Generalization(general=il_Il_Operand, specific=iec61131_variables_Variable)
gen_iec61131_variables_Variable_Commentable = Generalization(general=Commentable, specific=iec61131_variables_Variable)
gen_iec61131_variables_Variable_Name_variables_Symbolic_Variable = Generalization(general=variables_Symbolic_Variable, specific=iec61131_variables_Variable_Name)
gen_iec61131_variables_Variable_Name_NamedElement = Generalization(general=NamedElement, specific=iec61131_variables_Variable_Name)
gen_iec61131_variables_Variable_Name_Output_Reference = Generalization(general=Output_Reference, specific=iec61131_variables_Variable_Name)
gen_iec61131_variables_Variable_Name_Input_Reference = Generalization(general=Input_Reference, specific=iec61131_variables_Variable_Name)
gen_iec61131_ld_Ladder_Diagram_pous_Function_Body = Generalization(general=pous_Function_Body, specific=iec61131_ld_Ladder_Diagram)
gen_iec61131_ld_Ladder_Diagram_pous_Function_Block_Body = Generalization(general=pous_Function_Block_Body, specific=iec61131_ld_Ladder_Diagram)
gen_iec61131_ld_Rung_Cond2_Condition = Generalization(general=Cond2_Condition, specific=iec61131_ld_Rung)
gen_iec61131_fbd_Function_Block_Diagram_pous_Function_Body = Generalization(general=pous_Function_Body, specific=iec61131_fbd_Function_Block_Diagram)
gen_iec61131_fbd_Function_Block_Diagram_pous_Function_Block_Body = Generalization(general=pous_Function_Block_Body, specific=iec61131_fbd_Function_Block_Diagram)
gen_iec61131_fbd_Fbd_Network_Cond2_Condition = Generalization(general=Cond2_Condition, specific=iec61131_fbd_Fbd_Network)
gen_iec61131_types_Numeric_Type_Name_Elementary_Type_Name = Generalization(general=Elementary_Type_Name, specific=iec61131_types_Numeric_Type_Name)
gen_iec61131_types_Integer_Type_Name_Numeric_Type_Name = Generalization(general=Numeric_Type_Name, specific=iec61131_types_Integer_Type_Name)
gen_iec61131_types_Real_Type_Name_Numeric_Type_Name = Generalization(general=Numeric_Type_Name, specific=iec61131_types_Real_Type_Name)
gen_iec61131_types_Signed_Integer_Type_Name_Integer_Type_Name = Generalization(general=Integer_Type_Name, specific=iec61131_types_Signed_Integer_Type_Name)
gen_iec61131_types_Unsigned_Integer_Type_Name_Integer_Type_Name = Generalization(general=Integer_Type_Name, specific=iec61131_types_Unsigned_Integer_Type_Name)
gen_iec61131_types_Elementary_Type_Name_types_Non_Generic_Type_Name = Generalization(general=types_Non_Generic_Type_Name, specific=iec61131_types_Elementary_Type_Name)
gen_iec61131_types_Elementary_Type_Name_types_Simple_Specification = Generalization(general=types_Simple_Specification, specific=iec61131_types_Elementary_Type_Name)
gen_iec61131_types_Elementary_Type_Name_interfaces_Simple_Specification_Func = Generalization(general=interfaces_Simple_Specification_Func, specific=iec61131_types_Elementary_Type_Name)
gen_iec61131_types_Non_Generic_Type_Name_types_Data_Type_Name = Generalization(general=types_Data_Type_Name, specific=iec61131_types_Non_Generic_Type_Name)
gen_iec61131_types_Non_Generic_Type_Name_pous_Function_Return_Value = Generalization(general=pous_Function_Return_Value, specific=iec61131_types_Non_Generic_Type_Name)
gen_iec61131_types_Derived_Type_Name_Non_Generic_Type_Name = Generalization(general=Non_Generic_Type_Name, specific=iec61131_types_Derived_Type_Name)
gen_iec61131_types_Generic_Type_Name_types_Data_Type_Name = Generalization(general=types_Data_Type_Name, specific=iec61131_types_Generic_Type_Name)
gen_iec61131_types_Generic_Type_Name_pous_Function_Return_Value = Generalization(general=pous_Function_Return_Value, specific=iec61131_types_Generic_Type_Name)
gen_iec61131_types_Generic_Type_Name_types_Simple_Specification = Generalization(general=types_Simple_Specification, specific=iec61131_types_Generic_Type_Name)
gen_iec61131_types_Data_Type_Name_Library_Element_Name = Generalization(general=Library_Element_Name, specific=iec61131_types_Data_Type_Name)
gen_iec61131_types_Bool_Type_Name_Bit_String_Type_Name = Generalization(general=Bit_String_Type_Name, specific=iec61131_types_Bool_Type_Name)
gen_iec61131_types_DT_Type_Name_Date_Type_Name = Generalization(general=Date_Type_Name, specific=iec61131_types_DT_Type_Name)
gen_iec61131_types_TOD_Type_Name_Date_Type_Name = Generalization(general=Date_Type_Name, specific=iec61131_types_TOD_Type_Name)
gen_iec61131_types_Duration_Type_Name_Elementary_Type_Name = Generalization(general=Elementary_Type_Name, specific=iec61131_types_Duration_Type_Name)
gen_iec61131_types_Single_Element_Type_Name_Derived_Type_Name = Generalization(general=Derived_Type_Name, specific=iec61131_types_Single_Element_Type_Name)
gen_iec61131_types_Array_Type_Name_Derived_Type_Name = Generalization(general=Derived_Type_Name, specific=iec61131_types_Array_Type_Name)
gen_iec61131_types_Structure_Type_Name_types_Derived_Type_Name = Generalization(general=types_Derived_Type_Name, specific=iec61131_types_Structure_Type_Name)
gen_iec61131_types_Structure_Type_Name_interfaces_External_Specification = Generalization(general=interfaces_External_Specification, specific=iec61131_types_Structure_Type_Name)
gen_iec61131_types_Structure_Type_Name_interfaces_Var_Spec = Generalization(general=interfaces_Var_Spec, specific=iec61131_types_Structure_Type_Name)
gen_iec61131_types_String_Type_Name_Derived_Type_Name = Generalization(general=Derived_Type_Name, specific=iec61131_types_String_Type_Name)
gen_iec61131_types_Simple_Type_Name_types_Single_Element_Type_Name = Generalization(general=types_Single_Element_Type_Name, specific=iec61131_types_Simple_Type_Name)
gen_iec61131_types_Simple_Type_Name_types_Simple_Specification = Generalization(general=types_Simple_Specification, specific=iec61131_types_Simple_Type_Name)
gen_iec61131_types_Simple_Type_Name_interfaces_Simple_Specification_Func = Generalization(general=interfaces_Simple_Specification_Func, specific=iec61131_types_Simple_Type_Name)
gen_iec61131_types_Subrange_Type_Name_Single_Element_Type_Name = Generalization(general=Single_Element_Type_Name, specific=iec61131_types_Subrange_Type_Name)
gen_iec61131_types_Enumerated_Type_Name_Single_Element_Type_Name = Generalization(general=Single_Element_Type_Name, specific=iec61131_types_Enumerated_Type_Name)
gen_iec61131_types_Single_Byte_String_Type_Name_Byte_String_Type_Name = Generalization(general=Byte_String_Type_Name, specific=iec61131_types_Single_Byte_String_Type_Name)
gen_iec61131_types_Double_Byte_String_Type_Name_Byte_String_Type_Name = Generalization(general=Byte_String_Type_Name, specific=iec61131_types_Double_Byte_String_Type_Name)
gen_iec61131_types_Byte_String_Type_Name_Elementary_Type_Name = Generalization(general=Elementary_Type_Name, specific=iec61131_types_Byte_String_Type_Name)
gen_iec61131_types_Simple_Specification_Data_Type_Name = Generalization(general=Data_Type_Name, specific=iec61131_types_Simple_Specification)

# Domain Model
domain_model = DomainModel(
    name="iec61131",
    types={Commentable, NamedElement, iec61131_Commentable, iec61131_NamedElement, iec61131_literals_Numeric_Literal, Constant, iec61131_literals_Character_String, iec61131_IEC61131, iec61131_Library_Element_Declaration, iec61131_Library_Element_Name, Integer_Type_Name, iec61131_literals_Real_Literal, Real_Type_Name, Fixed_Point, iec61131_literals_Boolean_Literal, iec61131_literals_Time_Literal, iec61131_literals_Constant, configurations_Data_Source, iec61131_literals_Bit_String_Literal, configurations_Prog_Data_Source, il_Il_Operand, BSInteger, Bit_String_Type_Name, iec61131_literals_Integer_Literal, Numeric_Literal, Integer, iec61131_literals_Hex_Integer, iec61131_literals_Duration, literals_Time_Literal, sfc_Action_Time, Interval, Duration_Type_Name, Substraction_Operator, iec61131_literals_Time_Of_Day, Time_Literal, Daytime, iec61131_literals_Signed_Integer, literals_Integer, st_Case_List_Element, interfaces_Range, iec61131_literals_Binary_Integer, literals_BSInteger, iec61131_literals_Octal_Integer, iec61131_literals_Date_And_Time, DT_Type_Name, iec61131_literals_Unsigned_Integer, literals_Fixed_Point_Literal, iec61131_literals_Interval, Fixed_Point_Literal, TOD_Type_Name, iec61131_literals_Date, Date_Type_Name, Date_Literal, Minutes, iec61131_literals_Minutes, Seconds, iec61131_literals_Seconds, Milliseconds, iec61131_literals_Days, Unsigned_Integer, Hours, Double_Byte_Character_Representation, iec61131_literals_Hours, iec61131_literals_Fixed_Point_Literal, iec61131_literals_Daytime, iec61131_literals_Date_Literal, iec61131_literals_BSInteger, iec61131_literals_Milliseconds, iec61131_literals_Single_Byte_Character_String, Character_String, Single_Byte_Character_Representation, iec61131_literals_Double_Byte_Character_String, iec61131_literals_Fixed_Point, iec61131_operators_Operator, iec61131_operators_Add_Operator, Operator, iec61131_operators_Unary_Operator, iec61131_operators_Addition_Operator, iec61131_operators_Substraction_Operator, iec61131_operators_Assignment_Operator, iec61131_operators_Comparison_Operator, iec61131_literals_Integer, iec61131_literals_Common_Character_Representation, iec61131_literals_Single_Byte_Character_Representation, Common_Character_Representation, iec61131_literals_Double_Byte_Character_Representation, il_Il_Simple_Operator, iec61131_operators_Power_Operator, iec61131_operators_Modulo_Operator, operators_Dot_Operator, iec61131_operators_Divide_Operator, iec61131_operators_Less_Operator, Comparison_Operator, iec61131_operators_Greater_Operator, iec61131_operators_GreaterEqual_Operator, iec61131_operators_LessEqual_Operator, iec61131_operators_Unequal_Operator, iec61131_operators_Addition_Name, iec61131_operators_Multiply_Operator, Dot_Operator, iec61131_operators_Equal_Operator, EquUequ_Operator, iec61131_operators_And_Operator, operators_Operator, il_Il_Expr_Operator, iec61131_operators_Or_Operator, iec61131_operators_Xor_Operator, iec61131_operators_Not_Operator, operators_Unary_Operator, iec61131_operators_Divide_Symbol, Divide_Operator, iec61131_operators_Power_Symbol, Power_Operator, iec61131_operators_Power_Name, iec61131_operators_Assignment_Symbol, Assignment_Operator, iec61131_operators_Assignment_Name, iec61131_operators_And_Symbol, And_Operator, iec61131_operators_And_Name, iec61131_operators_Equal_Name, operators_Equal_Operator, operators_Comparison_Name, iec61131_operators_Equal_Symbol, Equal_Operator, operators_Addition_Operator, operators_Arithmetic_Name, iec61131_operators_Addition_Symbol, operators_Add_Operator, iec61131_operators_Dot_Operator, iec61131_operators_Multiply_Name, operators_Multiply_Operator, iec61131_operators_Multiply_Symbol, Multiply_Operator, iec61131_operators_Divide_Name, operators_Divide_Operator, iec61131_operators_Greater_Name, operators_Greater_Operator, iec61131_operators_Greater_Symbol, Greater_Operator, iec61131_operators_GreaterEqual_Name, operators_GreaterEqual_Operator, iec61131_operators_GreaterEqual_Symbol, GreaterEqual_Operator, iec61131_operators_Substraction_Name, operators_Substraction_Operator, iec61131_operators_Substraction_Symbol, iec61131_operators_EquUequ_Operator, iec61131_operators_Comparison_Name, Il_Expr_Operator, iec61131_operators_Unequal_Name, operators_Unequal_Operator, iec61131_operators_Unequal_Symbol, Unequal_Operator, iec61131_operators_Less_Name, operators_Less_Operator, iec61131_operators_Less_Symbol, Less_Operator, iec61131_operators_LessEqual_Name, operators_LessEqual_Operator, iec61131_operators_LessEqual_Symbol, LessEqual_Operator, iec61131_interfaces_Var_Init_Decl, Var1_List, iec61131_interfaces_Var1_Init_Decl, Var_Init_Decl, Var1_Specification, iec61131_interfaces_Edge_Declaration, iec61131_operators_Arithmetic_Name, iec61131_interfaces_Io_Var_Declaration, interfaces_Interface, pous_Function_Block_Vars, pous_Program_Vars, pous_Function_Vars, iec61131_interfaces_Input_Declarations, Io_Var_Declaration, Input_Declaration, iec61131_interfaces_Subrange_Spec_Init, interfaces_Var1_Specification_Func, Subrange_Specification, Signed_Integer, iec61131_interfaces_Enumerated_Spec_Init, Enumerated_Specification, Bool_Type_Name, iec61131_interfaces_Var1_Specification, Assignment_Symbol, iec61131_interfaces_Simple_Spec_Init, interfaces_Var1_Specification, interfaces_Located_Var_Spec_Init, pous_Structure_Elements, Simple_Specification, iec61131_interfaces_Fb_Name_Decl, Temp_Var_Declaration, Structure_Initialization, Function_Block_Type_Name, iec61131_interfaces_String_Var_Declaration, interfaces_Temp_Var_Decl, interfaces_Var2_Init_Decl, iec61131_interfaces_Output_Declarations, Enumerated_Value, iec61131_interfaces_Array_Var_Init_Decl, Var2_Init_Decl, Array_Spec_Init, iec61131_interfaces_Structured_Var_Init_Decl, Initialized_Structure, Array_Initialization, Array_Specification, iec61131_interfaces_Initialized_Structure, pous_Structure_Specification, Structure_Type_Name, iec61131_interfaces_Input_Output_Declarations, Var_Declaration, iec61131_interfaces_Array_Spec_Init, Initial_Element, iec61131_interfaces_Structure_Element_Name, iec61131_interfaces_Enumerated_Value, Enumerated_Type_Name, iec61131_interfaces_Array_Initialization, Array_Initial_Elements, iec61131_interfaces_Var_Declaration, iec61131_interfaces_Temp_Var_Decl, iec61131_interfaces_Structure_Initialization, Structure_Element_Initialization, iec61131_interfaces_Structure_Element_Initialization, Structure_Element_Name, iec61131_interfaces_Array_Var_Declaration, iec61131_interfaces_Structured_Var_Declaration, iec61131_interfaces_Specification, iec61131_interfaces_Subrange_Specification, interfaces_Specification, interfaces_External_Specification, iec61131_interfaces_Var1_Declaration, Specification, Range, iec61131_interfaces_Double_Byte_String_Spec, interfaces_Var_Spec, Double_Byte_Character_String, iec61131_interfaces_Enumerated_Specification, iec61131_interfaces_Single_Byte_String_Var_Declaration, String_Var_Declaration, iec61131_interfaces_Array_Specification, Single_Byte_String_Spec, iec61131_interfaces_Array_Initial_Elements, iec61131_interfaces_Double_Byte_String_Var_Declaration, iec61131_interfaces_Subrange, Case_List_Element, Double_Byte_String_Spec, iec61131_interfaces_Single_Byte_String_Spec, Located_Var_Spec_Init, Single_Byte_Character_String, Single_BString, iec61131_interfaces_Interface, Double_BString, iec61131_interfaces_Var1_List, Variable_Name, iec61131_interfaces_Other_Var_Declaration, iec61131_interfaces_External_Var_Declarations, Other_Var_Declaration, External_Declaration, iec61131_interfaces_Retentive_Var_Declarations, RNV_Declarations, iec61131_interfaces_Non_Retentive_Var_Declarations, iec61131_interfaces_External_Declaration, Global_Var_Name, External_Specification, iec61131_interfaces_Global_Var_Name, Library_Element_Name, iec61131_interfaces_Global_Var_List, Global_Var_Spec, iec61131_interfaces_Temp_Var_Decls, Temp_Var_Decl, iec61131_interfaces_Var_Declarations, iec61131_interfaces_Incompl_Location, iec61131_interfaces_Incompl_Located_Var_Declarations, Incompl_Located_Var_Decl, iec61131_interfaces_RNV_Declarations, iec61131_interfaces_Incompl_Located_Var_Decl, Incompl_Location, Var_Spec, Located_Var_Decl, iec61131_interfaces_Var_Spec, iec61131_interfaces_External_Specification, iec61131_interfaces_Located_Var_Spec_Init, iec61131_interfaces_Location, Direct_Variable, iec61131_interfaces_Located_Var_Decl, Location, iec61131_interfaces_Located_Var_Declarations, Program_Vars, iec61131_interfaces_Global_Var_Declarations, Library_Element_Declaration, Global_Var_Decl, iec61131_interfaces_Global_Var_Decl, iec61131_interfaces_Global_Var_Spec, iec61131_interfaces_Global_Var_Location, iec61131_interfaces_Subrange_Specification2, iec61131_interfaces_Input_Declaration, iec61131_interfaces_Range, iec61131_interfaces_Byte_String, iec61131_interfaces_Single_BString, Byte_String, Single_Byte_String_Type_Name, iec61131_interfaces_Double_BString, Double_Byte_String_Type_Name, iec61131_interfaces_Subrange_Specification1, Subrange, iec61131_interfaces_Array_Initial_Elements1, Subrange_Type_Name, iec61131_interfaces_Enumerated_Specification1, iec61131_interfaces_Enumerated_Specification2, iec61131_interfaces_Array_Specification1, Array_Type_Name, iec61131_interfaces_Array_Specification2, Non_Generic_Type_Name, iec61131_interfaces_Array_Initial_Elements2, iec61131_interfaces_Initial_Element, iec61131_interfaces_InitElement_Constant, iec61131_interfaces_InitElement_EnumValue, iec61131_interfaces_InitElement_Structure, iec61131_interfaces_InitElement_Array, iec61131_interfaces_Var2_Init_Decl, iec61131_interfaces_Function_Var_Decl, iec61131_interfaces_Simple_Specification_Func, iec61131_interfaces_Var1_Specification_Func, iec61131_interfaces_Var_Name_Decl, Simple_Spec_Init, iec61131_interfaces_Var_Init_Decl_Func, Var1_Specification_Func, iec61131_interfaces_Simple_Spec_Init_Func, Simple_Specification_Func, pous_Function_Block_Type_Name, iec61131_pous_Function_Block_Declaration, iec61131_interfaces_Temp_Var_Declaration, iec61131_pous_Program_Declaration, Program_Type_Name, Function_Block_Body, iec61131_pous_Program_Type_Name, Blocks, iec61131_pous_Function_Block_Type_Name, types_Simple_Specification, iec61131_pous_Derived_Function_Block_Name, Derived_Function_Block_Name, Function_Block_Vars, iec61131_pous_Function_Declaration, Derived_Function_Name, Function_Return_Value, Function_Vars, Function_Body, iec61131_pous_Access_Name, iec61131_pous_Derived_Function_Name, pous_Function_Name, iec61131_pous_Function_Return_Value, iec61131_pous_Function_Body, iec61131_pous_Other_Language, pous_Function_Body, pous_Function_Block_Body, iec61131_pous_Function_Block_Body, iec61131_pous_Program_Access_Decl, Access_Name, Symbolic_Variable, iec61131_pous_Function_Name, iec61131_pous_Data_Type_Declaration, Type_Declaration, iec61131_pous_Type_Declaration, iec61131_pous_Single_Element_Type_Declaration, iec61131_pous_Array_Type_Declaration, iec61131_pous_Structure_Type_Declaration, Structure_Specification, iec61131_pous_String_Type_Declaration, String_Type_Name, Byte_String_Type_Name, Program_Access_Decl, iec61131_pous_Library, Program_Declaration, Function_Declaration, iec61131_pous_Simple_Type_Declaration, Single_Element_Type_Declaration, Simple_Type_Name, iec61131_pous_Subrange_Type_Declaration, Subrange_Spec_Init, iec61131_pous_Enumerated_Type_Declaration, Enumerated_Spec_Init, iec61131_pous_Structure_Specification, iec61131_pous_Structure_Declaration, Structure_Element_Declaration, iec61131_pous_Structure_Element_Declaration, Structure_Elements, iec61131_pous_Structure_Elements, iec61131_pous_Program_Vars, iec61131_pous_Function_Vars, iec61131_pous_Function_Block_Vars, iec61131_pous_Program_Access_Decls, Resource_Name, Function_Block_Declaration, iec61131_configurations_Configuration_Name, iec61131_configurations_Resource_Type_Name, iec61131_configurations_Configuration_Declaration, Configuration_Name, Single_Resource_Declaration, Global_Var_Declarations, Instance_Specific_Initializations, Access_Declarations, Resource_Declaration, iec61131_configurations_Resource_Name, iec61131_configurations_Resource_Declaration, Resource_Type_Name, iec61131_configurations_Single_Resource_Declaration, Task_Configuration, Program_Configuration, iec61131_configurations_Task_Configuration, Task_Name, Priority, Single, iec61131_configurations_Program_Configuration, Program_Name, iec61131_configurations_Access_Name, Prog_Conf_Elements, iec61131_configurations_Instance_Specific_Initializations, Instance_Specific_Init, iec61131_configurations_Data_Source, iec61131_configurations_Global_Var_Reference, configurations_Data_Sink, iec61131_configurations_Program_Output_Reference, Data_Source, iec61131_configurations_Access_Declarations, Access_Declaration, iec61131_configurations_Access_Declaration, Access_Path, iec61131_configurations_Prog_Cnxn, iec61131_configurations_Access_Path, iec61131_configurations_Direct_Path, iec61131_configurations_Symbolic_Path, iec61131_configurations_Program_Name, iec61131_configurations_Task_Name, iec61131_configurations_Task_Initialization, iec61131_configurations_Prog_Conf_Elements, Prog_Conf_Element, iec61131_configurations_Prog_Conf_Element, iec61131_configurations_Fb_Task, iec61131_configurations_Prog_Data_Source, iec61131_configurations_Prog_Sink, Prog_Cnxn, Data_Sink, iec61131_configurations_Prog_Source, Prog_Data_Source, iec61131_configurations_Data_Sink, iec61131_configurations_Instance_Specific_Init, iec61131_configurations_Instance_Spec1, iec61131_configurations_Instance_Spec2, iec61131_st_Subprogram_Control_Statement, iec61131_st_Selection_Statement, iec61131_configurations_Single, Task_Initialization, iec61131_configurations_Interval, iec61131_configurations_Priority, iec61131_st_Statement_List, Statement, iec61131_st_Expression, Expression_Types, Or_Operator, iec61131_st_Statement, iec61131_st_Assignment_Statement, Expression_Variable, Else_Statement, iec61131_st_Case_Statement, iec61131_st_Iteration_Statement, iec61131_st_Return_Statement, Subprogram_Control_Statement, iec61131_st_Fb_Invocation, Param_Assignment, iec61131_st_Param_Assignment, iec61131_st_Param_Type1, iec61131_st_Param_Type2, Variable, Not_Operator, iec61131_st_If_Statement, Selection_Statement, Statement_List, Else_If_Statement, iec61131_st_While_Statement, Case_Element, iec61131_st_Else_If_Statement, iec61131_st_Else_Statement, iec61131_st_Case_Element, Case_List, iec61131_st_Case_List, iec61131_st_Case_List_Element, iec61131_st_For_Statement, Iteration_Statement, Control_Variable, For_List, iec61131_st_Repeat_Statement, iec61131_st_Exit_Statement, iec61131_st_Control_Variable, iec61131_st_For_List, iec61131_st_Xor_Expression, Xor_Operator, iec61131_st_And_Expression, iec61131_st_Comparison, iec61131_st_Equ_Expression, iec61131_st_Add_Expression, iec61131_st_Primary_Expression, Add_Operator, iec61131_st_Term_Expression, iec61131_st_Power_Expression, Power_Symbol, iec61131_st_Unary_Expression, Unary_Operator, iec61131_il_Instruction_List, Il_Instruction, iec61131_st_Bracket_Expression, Primary_Expression, iec61131_st_Call_Expression, Function_Name, iec61131_st_Expression_Types, iec61131_st_Expression_Variable, Array_Variable, Structured_Variable, iec61131_st_Expression_Constant, iec61131_st_Expression_EnumValue, iec61131_st_Expression_Variable_Type, iec61131_il_Il_Formal_Funct_Call, iec61131_il_Simple_Instr_List, Il_Simple_Instruction, iec61131_il_Il_Instruction, Label, Il_Operations, iec61131_il_Label, iec61131_il_Il_Simple_Operation, il_Il_Operations, il_Simple_Instr, iec61131_il_Il_Expression, Il_Operand, Simple_Instr_List, iec61131_il_Il_Jump_Operation, Il_Jump_Operator, iec61131_il_Il_Fb_Call, Il_Call_Operator, Operands, iec61131_il_Operand2, Il_Param_List, iec61131_il_Il_Return_Operator, iec61131_il_Il_Operations, iec61131_il_Il_Simple_Operator, iec61131_il_Il_Operand, iec61131_il_Il_Operand_List, iec61131_il_Simple_Operation1, Il_Simple_Operation, Il_Simple_Operator, iec61131_il_Simple_Operation2, Il_Operand_List, iec61131_il_Il_Expr_Operator, iec61131_il_Il_Jump_Operator, iec61131_il_Il_Call_Operator, iec61131_il_Il_Param_List, Il_Param_Instruction, Il_Param_Last_Instruction, iec61131_il_Operand1, iec61131_il_Operands, iec61131_il_Il_Simple_Instruction, Simple_Instr, iec61131_il_Simple_Instr, iec61131_il_Il_Param_Instruction, Param_Instruction, iec61131_il_Il_Param_Last_Instruction, iec61131_il_Il_Param_Assignment, Param_Assignments, Il_Assign_Operator, Sfc_Network, iec61131_sfc_Sfc_Network, Initial_Step, iec61131_il_Il_Param_Out_Assignment, Il_Assign_Out_Operator, iec61131_il_Param_Assignments, iec61131_il_Param_Instruction, iec61131_il_Il_Assign_Operator, Assignment_Name, iec61131_il_Param_Assignment2, iec61131_il_Param_Assignment, iec61131_il_Il_Assign_Out_Operator, iec61131_sfc_Sequential_Function_Chart, iec61131_sfc_Step_Types, Action_Association, Step_Name, Sfc_Elements, iec61131_sfc_Initial_Step, Step_Types, iec61131_sfc_Step, sfc_Sfc_Elements, sfc_Step_Types, iec61131_sfc_Transition, Transition_Name, Steps, Transition_Condition, iec61131_sfc_Action, Action_Name, iec61131_sfc_Sfc_Elements, iec61131_sfc_Step_Name, iec61131_sfc_Action_Association, Action_Qualifier, Cond2_Condition, iec61131_sfc_Action_Name, iec61131_sfc_Action_Qualifier, Timed_Qualifier, Action_Time, iec61131_sfc_Timed_Qualifier, iec61131_sfc_Action_Time, iec61131_sfc_Transition_Name, iec61131_sfc_Steps, iec61131_sfc_Transition_Condition, iec61131_sfc_Steps1, iec61131_sfc_Steps2, iec61131_sfc_Transition_Cond1, iec61131_sfc_Transition_Cond2, iec61131_sfc_Transition_Cond3, iec61131_sfc_Cond2_Condition, iec61131_sfc_ActionTime2, iec61131_variables_Symbolic_Variable, iec61131_variables_Multi_Element_Variable, iec61131_variables_Array_Variable, Multi_Element_Variable, Subscript_List, iec61131_variables_Structured_Variable, iec61131_types_Date_Type_Name, iec61131_types_Bit_String_Type_Name, iec61131_variables_Direct_Variable, variables_Variable, iec61131_variables_Variable, iec61131_variables_Variable_Name, variables_Symbolic_Variable, Output_Reference, Input_Reference, iec61131_variables_Subscript_List, iec61131_ld_Ladder_Diagram, iec61131_ld_Rung, iec61131_fbd_Function_Block_Diagram, Fbd_Network, iec61131_fbd_Fbd_Network, iec61131_types_TypeLib, Data_Type_Name, iec61131_types_Numeric_Type_Name, Elementary_Type_Name, iec61131_types_Integer_Type_Name, Numeric_Type_Name, iec61131_types_Real_Type_Name, iec61131_types_Signed_Integer_Type_Name, iec61131_types_Unsigned_Integer_Type_Name, iec61131_types_Elementary_Type_Name, types_Non_Generic_Type_Name, interfaces_Simple_Specification_Func, iec61131_types_Non_Generic_Type_Name, types_Data_Type_Name, pous_Function_Return_Value, iec61131_types_Derived_Type_Name, iec61131_types_Generic_Type_Name, iec61131_types_Data_Type_Name, iec61131_types_Bool_Type_Name, iec61131_types_DT_Type_Name, iec61131_types_TOD_Type_Name, iec61131_types_Duration_Type_Name, iec61131_types_Single_Element_Type_Name, Derived_Type_Name, iec61131_types_Array_Type_Name, iec61131_types_Structure_Type_Name, types_Derived_Type_Name, iec61131_types_String_Type_Name, iec61131_types_Simple_Type_Name, types_Single_Element_Type_Name, iec61131_types_Subrange_Type_Name, Single_Element_Type_Name, iec61131_types_Enumerated_Type_Name, iec61131_types_Single_Byte_String_Type_Name, iec61131_types_Double_Byte_String_Type_Name, iec61131_types_Byte_String_Type_Name, iec61131_types_Simple_Specification, Edge, Direction},
    associations={library_element_declaration0, library_element_name1, integer_type_name7, real_type_name9, fixed_point10, integer3, bit_string_type4, integer6, interval12, duration_type_name13, substraction15, date_literal21, dt_type_name23, date_literal24, daytime27, fixed_point30, daytime17, tod_type_name18, date_type_name20, minutes34, integer35, seconds38, integer39, integer31, hours32, double_byte_character_representation47, second48, milliseconds42, integer43, single_byte_character_representation46, common_character_representation51, common_character_representation50, var_list54, specification55, var_list56, input_declaration53, simple_specification61, subrange_specification62, signed_integer63, bool_type_name58, assignment60, structure_initialization70, function_block_type_name71, assignment73, enumerated_specification65, enumerated_value66, array_spec_init68, initialized_structure69, array_initialization80, array_specification82, assignment84, structure_initialization86, structure_type_name89, var_init_decl76, var_declaration77, assignment78, structure_element_init96, enumerated_type_name98, array_initial_elements99, structure_element_initialization91, structure_element_name92, assignment93, array_specification101, structure_type_name103, specification100, integer105, single_byte_string_spec106, double_byte_string_spec107, single_byte_character_string108, assignment109, single_string112, double_byte_character_string114, assignment115, double_string118, variable_name120, external_declaration121, global_var_name122, specification123, global_var_name125, temp_var_decl127, incompl_located_var_decl128, var_init_decl129, variable_name131, incompl_location133, var_spec135, direct_variable137, location138, variable_name139, located_var_spec_init142, global_var_name152, located_var_decl144, global_var_decl145, global_var_spec146, located_var_spec_init147, location150, integer155, single_byte_string_type_name157, double_byte_string_type_name158, integer_type_name159, subrange161, subrange_type_name163, enumerated_value164, enumerated_type_name166, array_type_name168, non_generic_type_name169, subrange170, structure183, array_initial_element173, integer175, array_initial_element177, constant180, enum_value181, structure_left185, structure_right188, array191, array_left193, array_right196, var2_init_decl199, constant200, structure_initialization202, specification205, simple_specification206, constant207, var_list210, program_type_name212, program_var_declarations213, function_block_body215, function_body228, derived_function_block_name217, function_block_body218, function_block_var_declarations221, derived_function_name223, function_return_value224, function_var_declarations226, access_name230, non_generic_type_name231, symbolic_variable234, assignment249, character_string252, type_declaration236, array_type_name237, array_spec_init239, structure_type_name242, structure_specification244, string_type_name246, byte_string_type_name247, program_access_decl273, programs274, integer254, functions275, simple_type_name257, simple_spec_init258, subrange_type_name260, subrange_spec_init262, enumerated_type_name264, enumerated_spec_init266, structure_element_declaration268, structure_element_name269, structure_element271, resource_name290, function_blocks277, configuration_name279, single_resource_declaration280, global_var_declarations282, instance_specific_initializations284, access_declarations286, resource_declaration288, task_name311, resource_type_name291, single_resource_declaration293, global_var_declarations296, task_configuration299, program_configuration300, task_name302, task_initialization_priority303, task_initialization_single305, task_initialization_interval307, program_name310, program_type_name314, prog_conf_elements317, instance_specific_init319, structure_element_name320, global_var_name322, resource_name325, symbolic_variable328, program_name330, access_declaration333, access_name334, access_path336, non_generic_type_name338, resource_name341, direct_variable343, program_name345, fb_name347, symbolic_variable350, assignment353, prog_conf_element355, task_name356, fb_name358, fb_name_spec389, assignment392, symbolic_variable361, data_sink363, prog_data_source364, assignment365, resource_name368, program_name370, fb_name373, location376, variable_name378, located_var_spec_init381, function_block_type_name384, structure_initialization386, data_source395, data_source396, integer398, statement400, expression_left401, or402, expression_right404, assignment407, expression409, variable412, else438, fb_name414, param_assignment416, expression418, assignment420, variable_name423, variable_name426, variable428, not430, expression432, statement_list434, else_if436, assignment465, else440, expression442, case_element445, expression447, statement_list449, statement_list452, case_list454, statement_list455, case_list_element458, control_variable459, for_list460, statement_list462, expression468, statement_list470, expression473, statement_list475, expression478, to_expression480, by_expression483, xor_expression_left486, xor488, xor_expression_right490, and_expression_left493, add_expression_right516, and495, and_expression_right497, comparison_expression_left500, comparison_expression_right502, equ_operator505, equ_expression_left507, equ_expression_right509, comparison_operator512, add_expression_left514, add_operator519, term_expression_left521, term_expression_right523, multiply_operator526, power528, power_expression_left529, power_expression_right532, unary_operator535, unary_expression536, expression539, param_assignment541, function_name543, variable545, direct_variable547, array_variable550, structured_variable552, constant554, enum_value556, expression_variable558, operands578, il_instruction560, il_simple_instruction561, label562, il_operation563, il_expr_operator565, il_operand566, simple_instr_list568, label570, il_jump_operator572, il_call_operator574, fb_name575, il_param_list597, function_name580, il_param_list582, il_operand584, il_simple_operator586, il_operand587, function_name590, il_operand_list592, il_param_instruction594, il_param_last_instruction595, il_operand_list599, simple_inst601, il_assign_operator602, sfc_network622, initial_step623, param_assignment603, variable606, il_assign_out_operator608, param_assignment610, variable_name611, assignment613, simple_instr_list615, not617, variable_name619, indicator_name645, action_association648, sfc_elements624, transition_name626, assignment627, steps630, transition_condition632, integer634, action_name637, function_block_body638, action_name641, action_qualifier643, condition658, step_name649, timed_qualifier651, action_time652, step_name654, field_selector674, step_name656, simple_instr_list659, expression661, assignment663, time_variable666, subscripted_variable668, subscript_list670, record_variable672, subscript677, fbd_network679, types680},
    generalizations={gen_iec61131_Library_Element_Declaration_Commentable, gen_iec61131_Library_Element_Name_NamedElement, gen_iec61131_literals_Numeric_Literal_Constant, gen_iec61131_literals_Character_String_Constant, gen_iec61131_literals_Real_Literal_Numeric_Literal, gen_iec61131_literals_Boolean_Literal_Constant, gen_iec61131_literals_Time_Literal_Constant, gen_iec61131_literals_Constant_configurations_Data_Source, gen_iec61131_literals_Bit_String_Literal_Constant, gen_iec61131_literals_Constant_configurations_Prog_Data_Source, gen_iec61131_literals_Constant_il_Il_Operand, gen_iec61131_literals_Integer_Literal_Numeric_Literal, gen_iec61131_literals_Octal_Integer_literals_BSInteger, gen_iec61131_literals_Hex_Integer_literals_Integer, gen_iec61131_literals_Hex_Integer_literals_BSInteger, gen_iec61131_literals_Duration_literals_Time_Literal, gen_iec61131_literals_Duration_sfc_Action_Time, gen_iec61131_literals_Time_Of_Day_Time_Literal, gen_iec61131_literals_Signed_Integer_literals_Integer, gen_iec61131_literals_Signed_Integer_st_Case_List_Element, gen_iec61131_literals_Signed_Integer_interfaces_Range, gen_iec61131_literals_Binary_Integer_literals_Integer, gen_iec61131_literals_Binary_Integer_literals_BSInteger, gen_iec61131_literals_Octal_Integer_literals_Integer, gen_iec61131_literals_Date_And_Time_Time_Literal, gen_iec61131_literals_Unsigned_Integer_st_Case_List_Element, gen_iec61131_literals_Unsigned_Integer_interfaces_Range, gen_iec61131_literals_Unsigned_Integer_literals_Integer, gen_iec61131_literals_Unsigned_Integer_literals_BSInteger, gen_iec61131_literals_Unsigned_Integer_literals_Fixed_Point_Literal, gen_iec61131_literals_Date_Time_Literal, gen_iec61131_literals_Minutes_Interval, gen_iec61131_literals_Seconds_Interval, gen_iec61131_literals_Days_Interval, gen_iec61131_literals_Hours_Interval, gen_iec61131_literals_Milliseconds_Interval, gen_iec61131_literals_Single_Byte_Character_String_Character_String, gen_iec61131_literals_Double_Byte_Character_String_Character_String, gen_iec61131_literals_Fixed_Point_Fixed_Point_Literal, gen_iec61131_operators_Add_Operator_Operator, gen_iec61131_operators_Unary_Operator_Operator, gen_iec61131_operators_Assignment_Operator_Operator, gen_iec61131_operators_Not_Operator_il_Il_Simple_Operator, gen_iec61131_operators_Power_Operator_Operator, gen_iec61131_operators_Modulo_Operator_il_Il_Expr_Operator, gen_iec61131_operators_Modulo_Operator_operators_Dot_Operator, gen_iec61131_operators_Divide_Operator_Dot_Operator, gen_iec61131_operators_Less_Operator_Comparison_Operator, gen_iec61131_operators_Greater_Operator_Comparison_Operator, gen_iec61131_operators_GreaterEqual_Operator_Comparison_Operator, gen_iec61131_operators_LessEqual_Operator_Comparison_Operator, gen_iec61131_operators_Unequal_Operator_EquUequ_Operator, gen_iec61131_operators_Comparison_Operator_Operator, gen_iec61131_operators_Multiply_Operator_Dot_Operator, gen_iec61131_operators_Equal_Operator_EquUequ_Operator, gen_iec61131_operators_And_Operator_operators_Operator, gen_iec61131_operators_And_Operator_il_Il_Expr_Operator, gen_iec61131_operators_Or_Operator_operators_Operator, gen_iec61131_operators_Or_Operator_il_Il_Expr_Operator, gen_iec61131_operators_Xor_Operator_operators_Operator, gen_iec61131_operators_Xor_Operator_il_Il_Expr_Operator, gen_iec61131_operators_Not_Operator_operators_Unary_Operator, gen_iec61131_operators_Divide_Name_operators_Arithmetic_Name, gen_iec61131_operators_Divide_Symbol_Divide_Operator, gen_iec61131_operators_Power_Symbol_Power_Operator, gen_iec61131_operators_Power_Name_Power_Operator, gen_iec61131_operators_Assignment_Symbol_Assignment_Operator, gen_iec61131_operators_Assignment_Name_Assignment_Operator, gen_iec61131_operators_And_Symbol_And_Operator, gen_iec61131_operators_And_Name_And_Operator, gen_iec61131_operators_Equal_Name_operators_Equal_Operator, gen_iec61131_operators_Equal_Name_operators_Comparison_Name, gen_iec61131_operators_Addition_Name_operators_Addition_Operator, gen_iec61131_operators_Addition_Name_operators_Arithmetic_Name, gen_iec61131_operators_Addition_Symbol_operators_Addition_Operator, gen_iec61131_operators_Addition_Symbol_operators_Add_Operator, gen_iec61131_operators_Dot_Operator_Operator, gen_iec61131_operators_Multiply_Name_operators_Multiply_Operator, gen_iec61131_operators_Multiply_Name_operators_Arithmetic_Name, gen_iec61131_operators_Multiply_Symbol_Multiply_Operator, gen_iec61131_operators_Divide_Name_operators_Divide_Operator, gen_iec61131_operators_Greater_Name_operators_Greater_Operator, gen_iec61131_operators_Greater_Name_operators_Comparison_Name, gen_iec61131_operators_Greater_Symbol_Greater_Operator, gen_iec61131_operators_GreaterEqual_Name_operators_GreaterEqual_Operator, gen_iec61131_operators_GreaterEqual_Name_operators_Comparison_Name, gen_iec61131_operators_GreaterEqual_Symbol_GreaterEqual_Operator, gen_iec61131_operators_Substraction_Name_operators_Substraction_Operator, gen_iec61131_operators_Substraction_Name_operators_Arithmetic_Name, gen_iec61131_operators_Substraction_Symbol_operators_Substraction_Operator, gen_iec61131_operators_Substraction_Symbol_operators_Unary_Operator, gen_iec61131_operators_Substraction_Symbol_operators_Add_Operator, gen_iec61131_operators_EquUequ_Operator_Operator, gen_iec61131_operators_Comparison_Name_Il_Expr_Operator, gen_iec61131_operators_Equal_Symbol_Equal_Operator, gen_iec61131_operators_Unequal_Name_operators_Unequal_Operator, gen_iec61131_operators_Unequal_Name_operators_Comparison_Name, gen_iec61131_operators_Unequal_Symbol_Unequal_Operator, gen_iec61131_operators_Less_Name_operators_Less_Operator, gen_iec61131_operators_Less_Name_operators_Comparison_Name, gen_iec61131_operators_Less_Symbol_Less_Operator, gen_iec61131_operators_LessEqual_Name_operators_LessEqual_Operator, gen_iec61131_operators_LessEqual_Name_operators_Comparison_Name, gen_iec61131_operators_LessEqual_Symbol_LessEqual_Operator, gen_iec61131_interfaces_Var_Init_Decl_Input_Declaration, gen_iec61131_interfaces_Var1_Init_Decl_Var_Init_Decl, gen_iec61131_interfaces_Edge_Declaration_Input_Declaration, gen_iec61131_operators_Arithmetic_Name_Il_Expr_Operator, gen_iec61131_interfaces_Io_Var_Declaration_interfaces_Interface, gen_iec61131_interfaces_Io_Var_Declaration_pous_Function_Block_Vars, gen_iec61131_interfaces_Io_Var_Declaration_pous_Program_Vars, gen_iec61131_interfaces_Io_Var_Declaration_pous_Function_Vars, gen_iec61131_interfaces_Input_Declarations_Io_Var_Declaration, gen_iec61131_interfaces_Subrange_Spec_Init_interfaces_Var1_Specification, gen_iec61131_interfaces_Subrange_Spec_Init_interfaces_Located_Var_Spec_Init, gen_iec61131_interfaces_Subrange_Spec_Init_pous_Structure_Elements, gen_iec61131_interfaces_Subrange_Spec_Init_interfaces_Var1_Specification_Func, gen_iec61131_interfaces_Enumerated_Spec_Init_interfaces_Var1_Specification, gen_iec61131_interfaces_Enumerated_Spec_Init_interfaces_Located_Var_Spec_Init, gen_iec61131_interfaces_Enumerated_Spec_Init_pous_Structure_Elements, gen_iec61131_interfaces_Enumerated_Spec_Init_interfaces_Var1_Specification_Func, gen_iec61131_interfaces_Simple_Spec_Init_interfaces_Var1_Specification, gen_iec61131_interfaces_Simple_Spec_Init_interfaces_Located_Var_Spec_Init, gen_iec61131_interfaces_Simple_Spec_Init_pous_Structure_Elements, gen_iec61131_interfaces_Fb_Name_Decl_Temp_Var_Declaration, gen_iec61131_interfaces_String_Var_Declaration_interfaces_Temp_Var_Decl, gen_iec61131_interfaces_String_Var_Declaration_interfaces_Var2_Init_Decl, gen_iec61131_interfaces_Output_Declarations_Io_Var_Declaration, gen_iec61131_interfaces_Array_Var_Init_Decl_Var2_Init_Decl, gen_iec61131_interfaces_Structured_Var_Init_Decl_Var2_Init_Decl, gen_iec61131_interfaces_Initialized_Structure_interfaces_Located_Var_Spec_Init, gen_iec61131_interfaces_Initialized_Structure_pous_Structure_Specification, gen_iec61131_interfaces_Initialized_Structure_pous_Structure_Elements, gen_iec61131_interfaces_Input_Output_Declarations_Io_Var_Declaration, gen_iec61131_interfaces_Array_Spec_Init_interfaces_Located_Var_Spec_Init, gen_iec61131_interfaces_Array_Spec_Init_pous_Structure_Elements, gen_iec61131_interfaces_Enumerated_Value_st_Case_List_Element, gen_iec61131_interfaces_Enumerated_Value_configurations_Prog_Data_Source, gen_iec61131_interfaces_Enumerated_Value_il_Il_Operand, gen_iec61131_interfaces_Temp_Var_Decl_Var_Declaration, gen_iec61131_interfaces_Array_Var_Declaration_Temp_Var_Declaration, gen_iec61131_interfaces_Structured_Var_Declaration_Temp_Var_Declaration, gen_iec61131_interfaces_Subrange_Specification_interfaces_Specification, gen_iec61131_interfaces_Subrange_Specification_interfaces_External_Specification, gen_iec61131_interfaces_Var1_Declaration_Temp_Var_Declaration, gen_iec61131_interfaces_Double_Byte_String_Spec_Located_Var_Spec_Init, gen_iec61131_interfaces_Subrange_Specification_interfaces_Var_Spec, gen_iec61131_interfaces_Enumerated_Specification_interfaces_Specification, gen_iec61131_interfaces_Enumerated_Specification_interfaces_External_Specification, gen_iec61131_interfaces_Enumerated_Specification_interfaces_Var_Spec, gen_iec61131_interfaces_Single_Byte_String_Var_Declaration_String_Var_Declaration, gen_iec61131_interfaces_Array_Specification_interfaces_External_Specification, gen_iec61131_interfaces_Array_Specification_interfaces_Var_Spec, gen_iec61131_interfaces_Double_Byte_String_Var_Declaration_String_Var_Declaration, gen_iec61131_interfaces_Subrange_Case_List_Element, gen_iec61131_interfaces_Single_Byte_String_Spec_Located_Var_Spec_Init, gen_iec61131_interfaces_Interface_Commentable, gen_iec61131_interfaces_Other_Var_Declaration_interfaces_Interface, gen_iec61131_interfaces_Other_Var_Declaration_pous_Function_Block_Vars, gen_iec61131_interfaces_Other_Var_Declaration_pous_Program_Vars, gen_iec61131_interfaces_External_Var_Declarations_Other_Var_Declaration, gen_iec61131_interfaces_Retentive_Var_Declarations_RNV_Declarations, gen_iec61131_interfaces_Non_Retentive_Var_Declarations_RNV_Declarations, gen_iec61131_interfaces_Global_Var_Name_Library_Element_Name, gen_iec61131_interfaces_Global_Var_Name_Commentable, gen_iec61131_interfaces_Global_Var_List_Global_Var_Spec, gen_iec61131_interfaces_Temp_Var_Decls_Other_Var_Declaration, gen_iec61131_interfaces_Var_Declarations_RNV_Declarations, gen_iec61131_interfaces_Incompl_Located_Var_Declarations_Other_Var_Declaration, gen_iec61131_interfaces_RNV_Declarations_Other_Var_Declaration, gen_iec61131_interfaces_Located_Var_Declarations_Program_Vars, gen_iec61131_interfaces_Global_Var_Declarations_Library_Element_Declaration, gen_iec61131_interfaces_Global_Var_Decl_Commentable, gen_iec61131_interfaces_Global_Var_Location_Global_Var_Spec, gen_iec61131_interfaces_Subrange_Specification2_Subrange_Specification, gen_iec61131_interfaces_Byte_String_Var_Spec, gen_iec61131_interfaces_Single_BString_Byte_String, gen_iec61131_interfaces_Double_BString_Byte_String, gen_iec61131_interfaces_Subrange_Specification1_Subrange_Specification, gen_iec61131_interfaces_Array_Initial_Elements1_Array_Initial_Elements, gen_iec61131_interfaces_Enumerated_Specification1_Enumerated_Specification, gen_iec61131_interfaces_Enumerated_Specification2_Enumerated_Specification, gen_iec61131_interfaces_Array_Specification1_Array_Specification, gen_iec61131_interfaces_Array_Specification2_Array_Specification, gen_iec61131_interfaces_Array_Initial_Elements2_Array_Initial_Elements, gen_iec61131_interfaces_InitElement_Constant_Initial_Element, gen_iec61131_interfaces_InitElement_EnumValue_Initial_Element, gen_iec61131_interfaces_InitElement_Structure_Initial_Element, gen_iec61131_interfaces_InitElement_Array_Initial_Element, gen_iec61131_interfaces_Var2_Init_Decl_Var_Init_Decl, gen_iec61131_interfaces_Function_Var_Decl_pous_Function_Vars, gen_iec61131_interfaces_Function_Var_Decl_interfaces_Interface, gen_iec61131_interfaces_Var1_Specification_Func_Var1_Specification, gen_iec61131_interfaces_Var_Name_Decl_Simple_Spec_Init, gen_iec61131_interfaces_Var_Init_Decl_Func_Var2_Init_Decl, gen_iec61131_interfaces_Simple_Spec_Init_Func_Var1_Specification_Func, gen_iec61131_pous_Derived_Function_Block_Name_pous_Function_Block_Type_Name, gen_iec61131_pous_Derived_Function_Block_Name_Blocks, gen_iec61131_pous_Function_Block_Declaration_Library_Element_Declaration, gen_iec61131_interfaces_Temp_Var_Declaration_Temp_Var_Decl, gen_iec61131_pous_Program_Declaration_Library_Element_Declaration, gen_iec61131_pous_Program_Type_Name_Library_Element_Name, gen_iec61131_pous_Program_Type_Name_Blocks, gen_iec61131_pous_Function_Block_Type_Name_Library_Element_Name, gen_iec61131_pous_Function_Block_Type_Name_interfaces_External_Specification, gen_iec61131_pous_Function_Block_Type_Name_Commentable, gen_iec61131_pous_Function_Block_Type_Name_types_Simple_Specification, gen_iec61131_pous_Function_Declaration_Library_Element_Declaration, gen_iec61131_pous_Derived_Function_Name_pous_Function_Name, gen_iec61131_pous_Derived_Function_Name_Blocks, gen_iec61131_pous_Other_Language_pous_Function_Body, gen_iec61131_pous_Other_Language_pous_Function_Block_Body, gen_iec61131_pous_Function_Name_Library_Element_Name, gen_iec61131_pous_Data_Type_Declaration_Library_Element_Declaration, gen_iec61131_pous_Single_Element_Type_Declaration_Type_Declaration, gen_iec61131_pous_Array_Type_Declaration_Type_Declaration, gen_iec61131_pous_Structure_Type_Declaration_Type_Declaration, gen_iec61131_pous_String_Type_Declaration_Type_Declaration, gen_iec61131_pous_Simple_Type_Declaration_Single_Element_Type_Declaration, gen_iec61131_pous_Subrange_Type_Declaration_Single_Element_Type_Declaration, gen_iec61131_pous_Enumerated_Type_Declaration_Single_Element_Type_Declaration, gen_iec61131_pous_Structure_Declaration_Structure_Specification, gen_iec61131_pous_Program_Access_Decls_Program_Vars, gen_iec61131_configurations_Configuration_Name_Library_Element_Name, gen_iec61131_configurations_Resource_Type_Name_Library_Element_Name, gen_iec61131_configurations_Configuration_Declaration_Library_Element_Declaration, gen_iec61131_configurations_Resource_Declaration_Library_Element_Declaration, gen_iec61131_configurations_Program_Configuration_Commentable, gen_iec61131_configurations_Global_Var_Reference_configurations_Data_Source, gen_iec61131_configurations_Global_Var_Reference_configurations_Data_Sink, gen_iec61131_configurations_Global_Var_Reference_configurations_Prog_Data_Source, gen_iec61131_configurations_Program_Output_Reference_Data_Source, gen_iec61131_configurations_Prog_Cnxn_Prog_Conf_Element, gen_iec61131_configurations_Direct_Path_Access_Path, gen_iec61131_configurations_Symbolic_Path_Access_Path, gen_iec61131_configurations_Fb_Task_Prog_Conf_Element, gen_iec61131_configurations_Prog_Sink_Prog_Cnxn, gen_iec61131_configurations_Prog_Source_Prog_Cnxn, gen_iec61131_configurations_Instance_Spec1_Instance_Specific_Init, gen_iec61131_configurations_Instance_Spec2_Instance_Specific_Init, gen_iec61131_st_Subprogram_Control_Statement_Statement, gen_iec61131_st_Selection_Statement_Statement, gen_iec61131_configurations_Single_Task_Initialization, gen_iec61131_configurations_Interval_Task_Initialization, gen_iec61131_configurations_Priority_Task_Initialization, gen_iec61131_st_Statement_List_pous_Function_Body, gen_iec61131_st_Statement_List_pous_Function_Block_Body, gen_iec61131_st_Expression_Expression_Types, gen_iec61131_st_Statement_Commentable, gen_iec61131_st_Assignment_Statement_Statement, gen_iec61131_st_Case_Statement_Selection_Statement, gen_iec61131_st_Iteration_Statement_Statement, gen_iec61131_st_Return_Statement_Subprogram_Control_Statement, gen_iec61131_st_Fb_Invocation_Subprogram_Control_Statement, gen_iec61131_st_Param_Assignment_Commentable, gen_iec61131_st_Param_Type1_Param_Assignment, gen_iec61131_st_Param_Type2_Param_Assignment, gen_iec61131_st_If_Statement_Selection_Statement, gen_iec61131_st_For_Statement_Iteration_Statement, gen_iec61131_st_While_Statement_Iteration_Statement, gen_iec61131_st_Repeat_Statement_Iteration_Statement, gen_iec61131_st_Exit_Statement_Iteration_Statement, gen_iec61131_st_Xor_Expression_Expression_Types, gen_iec61131_st_And_Expression_Expression_Types, gen_iec61131_st_Comparison_Expression_Types, gen_iec61131_st_Equ_Expression_Expression_Types, gen_iec61131_st_Add_Expression_Expression_Types, gen_iec61131_st_Term_Expression_Expression_Types, gen_iec61131_st_Power_Expression_Expression_Types, gen_iec61131_st_Unary_Expression_Expression_Types, gen_iec61131_il_Instruction_List_pous_Function_Body, gen_iec61131_il_Instruction_List_pous_Function_Block_Body, gen_iec61131_st_Primary_Expression_Expression_Types, gen_iec61131_st_Bracket_Expression_Primary_Expression, gen_iec61131_st_Call_Expression_Primary_Expression, gen_iec61131_st_Expression_Types_Commentable, gen_iec61131_st_Expression_Variable_Commentable, gen_iec61131_st_Expression_Constant_Primary_Expression, gen_iec61131_st_Expression_EnumValue_Primary_Expression, gen_iec61131_st_Expression_Variable_Type_Primary_Expression, gen_iec61131_il_Il_Formal_Funct_Call_il_Il_Operations, gen_iec61131_il_Il_Formal_Funct_Call_il_Simple_Instr, gen_iec61131_il_Il_Simple_Operation_il_Il_Operations, gen_iec61131_il_Il_Simple_Operation_il_Simple_Instr, gen_iec61131_il_Il_Expression_il_Il_Operations, gen_iec61131_il_Il_Expression_il_Simple_Instr, gen_iec61131_il_Il_Jump_Operation_Il_Operations, gen_iec61131_il_Il_Fb_Call_Il_Operations, gen_iec61131_il_Operand2_Operands, gen_iec61131_il_Il_Return_Operator_Il_Operations, gen_iec61131_il_Il_Operand_Param_Assignment, gen_iec61131_il_Simple_Operation1_Il_Simple_Operation, gen_iec61131_il_Simple_Operation2_Il_Simple_Operation, gen_iec61131_il_Il_Expr_Operator_Il_Simple_Operator, gen_iec61131_il_Operand1_Operands, gen_iec61131_il_Il_Param_Instruction_Param_Instruction, gen_iec61131_il_Il_Param_Last_Instruction_Param_Instruction, gen_iec61131_il_Il_Param_Assignment_Param_Assignments, gen_iec61131_il_Il_Param_Out_Assignment_Param_Assignments, gen_iec61131_il_Param_Assignment2_Param_Assignment, gen_iec61131_sfc_Sequential_Function_Chart_Function_Block_Body, gen_iec61131_sfc_Initial_Step_Step_Types, gen_iec61131_sfc_Step_sfc_Sfc_Elements, gen_iec61131_sfc_Step_sfc_Step_Types, gen_iec61131_sfc_Transition_Sfc_Elements, gen_iec61131_sfc_Action_Sfc_Elements, gen_iec61131_sfc_Step_Name_NamedElement, gen_iec61131_sfc_Transition_Cond2_Transition_Condition, gen_iec61131_sfc_Steps1_Steps, gen_iec61131_sfc_Steps2_Steps, gen_iec61131_sfc_Transition_Cond1_Transition_Condition, gen_iec61131_sfc_Transition_Cond3_Transition_Condition, gen_iec61131_sfc_ActionTime2_Action_Time, gen_iec61131_variables_Symbolic_Variable_Variable, gen_iec61131_variables_Multi_Element_Variable_Symbolic_Variable, gen_iec61131_variables_Array_Variable_Multi_Element_Variable, gen_iec61131_variables_Structured_Variable_Multi_Element_Variable, gen_iec61131_types_Date_Type_Name_Elementary_Type_Name, gen_iec61131_types_Bit_String_Type_Name_Elementary_Type_Name, gen_iec61131_variables_Direct_Variable_variables_Variable, gen_iec61131_variables_Direct_Variable_configurations_Data_Source, gen_iec61131_variables_Direct_Variable_configurations_Data_Sink, gen_iec61131_variables_Direct_Variable_configurations_Prog_Data_Source, gen_iec61131_variables_Variable_il_Il_Operand, gen_iec61131_variables_Variable_Commentable, gen_iec61131_variables_Variable_Name_variables_Symbolic_Variable, gen_iec61131_variables_Variable_Name_NamedElement, gen_iec61131_variables_Variable_Name_Output_Reference, gen_iec61131_variables_Variable_Name_Input_Reference, gen_iec61131_ld_Ladder_Diagram_pous_Function_Body, gen_iec61131_ld_Ladder_Diagram_pous_Function_Block_Body, gen_iec61131_ld_Rung_Cond2_Condition, gen_iec61131_fbd_Function_Block_Diagram_pous_Function_Body, gen_iec61131_fbd_Function_Block_Diagram_pous_Function_Block_Body, gen_iec61131_fbd_Fbd_Network_Cond2_Condition, gen_iec61131_types_Numeric_Type_Name_Elementary_Type_Name, gen_iec61131_types_Integer_Type_Name_Numeric_Type_Name, gen_iec61131_types_Real_Type_Name_Numeric_Type_Name, gen_iec61131_types_Signed_Integer_Type_Name_Integer_Type_Name, gen_iec61131_types_Unsigned_Integer_Type_Name_Integer_Type_Name, gen_iec61131_types_Elementary_Type_Name_types_Non_Generic_Type_Name, gen_iec61131_types_Elementary_Type_Name_types_Simple_Specification, gen_iec61131_types_Elementary_Type_Name_interfaces_Simple_Specification_Func, gen_iec61131_types_Non_Generic_Type_Name_types_Data_Type_Name, gen_iec61131_types_Non_Generic_Type_Name_pous_Function_Return_Value, gen_iec61131_types_Derived_Type_Name_Non_Generic_Type_Name, gen_iec61131_types_Generic_Type_Name_types_Data_Type_Name, gen_iec61131_types_Generic_Type_Name_pous_Function_Return_Value, gen_iec61131_types_Generic_Type_Name_types_Simple_Specification, gen_iec61131_types_Data_Type_Name_Library_Element_Name, gen_iec61131_types_Bool_Type_Name_Bit_String_Type_Name, gen_iec61131_types_DT_Type_Name_Date_Type_Name, gen_iec61131_types_TOD_Type_Name_Date_Type_Name, gen_iec61131_types_Duration_Type_Name_Elementary_Type_Name, gen_iec61131_types_Single_Element_Type_Name_Derived_Type_Name, gen_iec61131_types_Array_Type_Name_Derived_Type_Name, gen_iec61131_types_Structure_Type_Name_types_Derived_Type_Name, gen_iec61131_types_Structure_Type_Name_interfaces_External_Specification, gen_iec61131_types_Structure_Type_Name_interfaces_Var_Spec, gen_iec61131_types_String_Type_Name_Derived_Type_Name, gen_iec61131_types_Simple_Type_Name_types_Single_Element_Type_Name, gen_iec61131_types_Simple_Type_Name_types_Simple_Specification, gen_iec61131_types_Simple_Type_Name_interfaces_Simple_Specification_Func, gen_iec61131_types_Subrange_Type_Name_Single_Element_Type_Name, gen_iec61131_types_Enumerated_Type_Name_Single_Element_Type_Name, gen_iec61131_types_Single_Byte_String_Type_Name_Byte_String_Type_Name, gen_iec61131_types_Double_Byte_String_Type_Name_Byte_String_Type_Name, gen_iec61131_types_Byte_String_Type_Name_Elementary_Type_Name, gen_iec61131_types_Simple_Specification_Data_Type_Name},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)