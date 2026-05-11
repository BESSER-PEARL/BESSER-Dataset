import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    iec61131::sfc::Action::Qualifier,
    iec61131::sfc::Action::Name,
    Step::Name,
    Action::Association,
    iec61131::sfc::Step::Types,
    Action::Qualifier,
    iec61131::sfc::Action::Association,
    iec61131::sfc::Sfc::Elements,
    Action::Name,
    Transition::Condition,
    iec61131::sfc::Sfc::Network,
    Sfc::Network,
    iec61131::il::Il::Assign::Out::Operator,
    iec61131::il::Param::Assignment,
    Assignment::Name,
    iec61131::il::Il::Assign::Operator,
    iec61131::il::Param::Instruction,
    iec61131::il::Param::Assignments,
    Il::Assign::Out::Operator,
    iec61131::il::Il::Operand::List,
    iec61131::il::Il::Simple::Operator,
    iec61131::il::Il::Operations,
    Il::Param::List,
    Il::Assign::Operator,
    Param::Assignments,
    iec61131::il::Il::Param::Out::Assignment,
    iec61131::il::Il::Param::Assignment,
    Param::Instruction,
    iec61131::il::Il::Param::Last::Instruction,
    iec61131::il::Il::Param::Instruction,
    iec61131::il::Simple::Instr,
    Simple::Instr,
    iec61131::il::Il::Simple::Instruction,
    iec61131::il::Operands,
    Il::Param::Last::Instruction,
    Il::Param::Instruction,
    iec61131::il::Il::Param::List,
    iec61131::il::Il::Call::Operator,
    iec61131::il::Il::Jump::Operator,
    Il::Operand::List,
    Il::Simple::Operator,
    iec61131::il::Il::Expr::Operator,
    Il::Simple::Operation,
    iec61131::il::Simple::Operation2,
    iec61131::il::Simple::Operation1,
    Il::Instruction,
    Operands,
    iec61131::il::Operand2,
    iec61131::il::Operand1,
    Il::Call::Operator,
    Il::Jump::Operator,
    Simple::Instr::List,
    Il::Operand,
    il::Simple::Instr,
    il::Il::Operations,
    iec61131::il::Il::Expression,
    iec61131::il::Il::Formal::Funct::Call,
    iec61131::il::Il::Simple::Operation,
    iec61131::il::Label,
    Il::Operations,
    iec61131::il::Il::Return::Operator,
    iec61131::il::Il::Jump::Operation,
    iec61131::il::Il::Fb::Call,
    Label,
    iec61131::il::Il::Instruction,
    Il::Simple::Instruction,
    iec61131::il::Simple::Instr::List,
    Unary::Operator,
    Power::Symbol,
    Structured::Variable,
    Array::Variable,
    Function::Name,
    Primary::Expression,
    iec61131::st::Expression::Variable::Type,
    iec61131::st::Expression::EnumValue,
    iec61131::st::Call::Expression,
    iec61131::st::Expression::Constant,
    iec61131::st::Bracket::Expression,
    Add::Operator,
    Xor::Operator,
    iec61131::st::For::List,
    iec61131::st::Control::Variable,
    Statement::List,
    Selection::Statement,
    iec61131::st::If::Statement,
    Not::Operator,
    Variable,
    For::List,
    Control::Variable,
    Iteration::Statement,
    iec61131::st::Exit::Statement,
    iec61131::st::While::Statement,
    iec61131::st::Repeat::Statement,
    iec61131::st::For::Statement,
    iec61131::st::Case::List::Element,
    iec61131::st::Case::List,
    Case::List,
    iec61131::st::Case::Element,
    iec61131::st::Else::Statement,
    Single::Element::Type::Name,
    iec61131::types::Enumerated::Type::Name,
    iec61131::types::Subrange::Type::Name,
    types::Single::Element::Type::Name,
    types::Derived::Type::Name,
    Derived::Type::Name,
    iec61131::types::Array::Type::Name,
    iec61131::types::String::Type::Name,
    iec61131::types::Single::Element::Type::Name,
    iec61131::variables::Subscript::List,
    Input::Reference,
    Output::Reference,
    variables::Symbolic::Variable,
    pous::Function::Return::Value,
    types::Data::Type::Name,
    iec61131::types::Non::Generic::Type::Name,
    interfaces::Simple::Specification::Func,
    types::Non::Generic::Type::Name,
    Numeric::Type::Name,
    iec61131::types::Real::Type::Name,
    iec61131::types::Integer::Type::Name,
    Elementary::Type::Name,
    iec61131::types::Bit::String::Type::Name,
    iec61131::types::Date::Type::Name,
    iec61131::types::Duration::Type::Name,
    iec61131::types::Byte::String::Type::Name,
    iec61131::types::Numeric::Type::Name,
    Data::Type::Name,
    iec61131::types::Simple::Specification,
    iec61131::types::TypeLib,
    Fbd::Network,
    iec61131::sfc::Transition::Cond2,
    iec61131::sfc::Transition::Condition,
    iec61131::sfc::Steps,
    iec61131::sfc::Transition::Name,
    iec61131::sfc::Action::Time,
    variables::Variable,
    Subscript::List,
    Multi::Element::Variable,
    iec61131::variables::Structured::Variable,
    iec61131::variables::Array::Variable,
    iec61131::variables::Symbolic::Variable,
    iec61131::sfc::Cond2::Condition,
    iec61131::sfc::Transition::Cond3,
    iec61131::sfc::Transition::Cond1,
    Cond2::Condition,
    iec61131::fbd::Fbd::Network,
    iec61131::ld::Rung,
    Steps,
    iec61131::sfc::Steps1,
    iec61131::sfc::Steps2,
    Transition::Name,
    sfc::Step::Types,
    sfc::Sfc::Elements,
    iec61131::sfc::Step,
    Step::Types,
    iec61131::sfc::Initial::Step,
    Sfc::Elements,
    iec61131::sfc::Transition,
    iec61131::sfc::Action,
    Initial::Step,
    iec61131::sfc::Timed::Qualifier,
    Action::Time,
    iec61131::sfc::ActionTime2,
    Timed::Qualifier,
    Variable::Name,
    Location,
    iec61131::interfaces::Located::Var::Decl,
    Direct::Variable,
    iec61131::interfaces::Location,
    iec61131::interfaces::Located::Var::Spec::Init,
    iec61131::interfaces::External::Specification,
    iec61131::interfaces::Var::Spec,
    iec61131::interfaces::Incompl::Location,
    Var::Spec,
    Incompl::Location,
    iec61131::interfaces::Incompl::Located::Var::Decl,
    Incompl::Located::Var::Decl,
    Temp::Var::Decl,
    Global::Var::Spec,
    iec61131::interfaces::Global::Var::List,
    Library::Element::Name,
    iec61131::types::Data::Type::Name,
    iec61131::interfaces::Specification,
    Specification,
    Array::Initial::Elements,
    iec61131::interfaces::Array::Initialization,
    iec61131::interfaces::Var1::List,
    Double::BString,
    Double::Byte::Character::String,
    Single::BString,
    Single::Byte::Character::String,
    Located::Var::Spec::Init,
    iec61131::interfaces::Double::Byte::String::Spec,
    iec61131::interfaces::Single::Byte::String::Spec,
    Double::Byte::String::Spec,
    Single::Byte::String::Spec,
    String::Var::Declaration,
    iec61131::interfaces::Double::Byte::String::Var::Declaration,
    iec61131::interfaces::Single::Byte::String::Var::Declaration,
    Range,
    Case::List::Element,
    iec61131::interfaces::Subrange,
    iec61131::interfaces::Array::Initial::Elements,
    interfaces::Var::Spec,
    interfaces::External::Specification,
    iec61131::interfaces::Array::Specification,
    iec61131::types::Structure::Type::Name,
    interfaces::Specification,
    iec61131::interfaces::Enumerated::Specification,
    iec61131::interfaces::Subrange::Specification,
    interfaces::Var2::Init::Decl,
    interfaces::Temp::Var::Decl,
    iec61131::interfaces::String::Var::Declaration,
    Function::Block::Type::Name,
    Structure::Initialization,
    Temp::Var::Declaration,
    iec61131::interfaces::Array::Var::Declaration,
    iec61131::interfaces::Structured::Var::Declaration,
    iec61131::interfaces::Var1::Declaration,
    iec61131::interfaces::Fb::Name::Decl,
    Enumerated::Type::Name,
    iec61131::interfaces::Structure::Element::Name,
    Initial::Element,
    Structure::Element::Name,
    iec61131::interfaces::Structure::Element::Initialization,
    Structure::Element::Initialization,
    iec61131::interfaces::Structure::Initialization,
    iec61131::interfaces::Var::Declaration,
    Structure::Type::Name,
    pous::Structure::Specification,
    Array::Specification,
    Array::Initialization,
    Var::Declaration,
    iec61131::interfaces::Temp::Var::Decl,
    Var1::Specification,
    Var::Init::Decl,
    iec61131::interfaces::Var1::Init::Decl,
    Var1::List,
    Input::Declaration,
    iec61131::interfaces::Var::Init::Decl,
    Io::Var::Declaration,
    iec61131::interfaces::Output::Declarations,
    iec61131::interfaces::Input::Output::Declarations,
    iec61131::interfaces::Input::Declarations,
    pous::Function::Vars,
    pous::Program::Vars,
    pous::Function::Block::Vars,
    interfaces::Interface,
    iec61131::interfaces::Other::Var::Declaration,
    iec61131::interfaces::Io::Var::Declaration,
    Initialized::Structure,
    Array::Spec::Init,
    Var2::Init::Decl,
    iec61131::interfaces::Structured::Var::Init::Decl,
    iec61131::interfaces::Array::Var::Init::Decl,
    Enumerated::Value,
    Enumerated::Specification,
    Signed::Integer,
    Subrange::Specification,
    interfaces::Var1::Specification::Func,
    Simple::Specification,
    pous::Structure::Elements,
    interfaces::Located::Var::Spec::Init,
    iec61131::interfaces::Initialized::Structure,
    iec61131::interfaces::Array::Spec::Init,
    interfaces::Var1::Specification,
    iec61131::interfaces::Enumerated::Spec::Init,
    iec61131::interfaces::Subrange::Spec::Init,
    iec61131::interfaces::Simple::Spec::Init,
    Assignment::Symbol,
    iec61131::interfaces::Var1::Specification,
    Bool::Type::Name,
    iec61131::interfaces::Edge::Declaration,
    operators::Divide::Operator,
    Multiply::Operator,
    iec61131::operators::Multiply::Symbol,
    iec61131::st::Else::If::Statement,
    Case::Element,
    iec61131::st::Case::Statement,
    Else::Statement,
    Else::If::Statement,
    Statement,
    Param::Assignment,
    iec61131::il::Il::Operand,
    iec61131::st::Param::Type1,
    iec61131::st::Param::Type2,
    iec61131::il::Param::Assignment2,
    Subprogram::Control::Statement,
    iec61131::st::Fb::Invocation,
    iec61131::st::Return::Statement,
    iec61131::st::Iteration::Statement,
    iec61131::st::Selection::Statement,
    iec61131::st::Subprogram::Control::Statement,
    Expression::Variable,
    iec61131::st::Assignment::Statement,
    Or::Operator,
    Expression::Types,
    iec61131::st::Power::Expression,
    iec61131::st::Comparison,
    iec61131::st::Equ::Expression,
    iec61131::st::And::Expression,
    iec61131::st::Xor::Expression,
    iec61131::st::Term::Expression,
    iec61131::st::Primary::Expression,
    iec61131::st::Add::Expression,
    iec61131::st::Unary::Expression,
    iec61131::st::Expression,
    iec61131::configurations::Prog::Data::Source,
    iec61131::configurations::Prog::Conf::Element,
    Prog::Conf::Element,
    iec61131::configurations::Prog::Cnxn,
    iec61131::configurations::Fb::Task,
    iec61131::configurations::Prog::Conf::Elements,
    Task::Initialization,
    iec61131::configurations::Priority,
    iec61131::configurations::Interval,
    iec61131::configurations::Single,
    iec61131::configurations::Instance::Specific::Init,
    iec61131::configurations::Data::Sink,
    Prog::Data::Source,
    Data::Sink,
    Prog::Cnxn,
    iec61131::configurations::Prog::Source,
    iec61131::configurations::Prog::Sink,
    Data::Source,
    iec61131::configurations::Program::Output::Reference,
    configurations::Data::Sink,
    iec61131::configurations::Data::Source,
    Instance::Specific::Init,
    iec61131::configurations::Instance::Spec2,
    iec61131::configurations::Instance::Spec1,
    iec61131::configurations::Instance::Specific::Initializations,
    iec61131::configurations::Task::Initialization,
    iec61131::configurations::Task::Name,
    iec61131::configurations::Program::Name,
    iec61131::configurations::Access::Path,
    iec61131::configurations::Access::Name,
    Access::Path,
    iec61131::configurations::Symbolic::Path,
    iec61131::configurations::Direct::Path,
    iec61131::configurations::Access::Declaration,
    Access::Declaration,
    iec61131::configurations::Access::Declarations,
    Resource::Declaration,
    Access::Declarations,
    Instance::Specific::Initializations,
    Global::Var::Declarations,
    Single::Resource::Declaration,
    Configuration::Name,
    iec61131::configurations::Resource::Type::Name,
    Prog::Conf::Elements,
    Program::Name,
    Single,
    Priority,
    Task::Name,
    iec61131::configurations::Task::Configuration,
    Program::Configuration,
    Task::Configuration,
    iec61131::configurations::Single::Resource::Declaration,
    Resource::Type::Name,
    Resource::Name,
    iec61131::configurations::Resource::Name,
    Simple::Type::Name,
    Single::Element::Type::Declaration,
    iec61131::pous::Subrange::Type::Declaration,
    iec61131::pous::Simple::Type::Declaration,
    iec61131::configurations::Configuration::Name,
    Function::Block::Declaration,
    Function::Declaration,
    Program::Declaration,
    iec61131::pous::Library,
    Program::Access::Decl,
    iec61131::pous::Function::Block::Vars,
    iec61131::pous::Function::Vars,
    iec61131::pous::Program::Vars,
    iec61131::pous::Structure::Elements,
    Structure::Elements,
    iec61131::pous::Structure::Element::Declaration,
    Structure::Element::Declaration,
    iec61131::pous::Structure::Specification,
    Enumerated::Spec::Init,
    iec61131::pous::Enumerated::Type::Declaration,
    Subrange::Spec::Init,
    pous::Function::Block::Body,
    pous::Function::Body,
    iec61131::ld::Ladder::Diagram,
    iec61131::st::Statement::List,
    iec61131::il::Instruction::List,
    iec61131::fbd::Function::Block::Diagram,
    iec61131::pous::Other::Language,
    iec61131::pous::Function::Body,
    iec61131::pous::Function::Return::Value,
    pous::Function::Name,
    Function::Body,
    Function::Vars,
    Byte::String::Type::Name,
    iec61131::types::Single::Byte::String::Type::Name,
    iec61131::types::Double::Byte::String::Type::Name,
    String::Type::Name,
    Structure::Specification,
    iec61131::pous::Structure::Declaration,
    iec61131::pous::Type::Declaration,
    Type::Declaration,
    iec61131::pous::Structure::Type::Declaration,
    iec61131::pous::Array::Type::Declaration,
    iec61131::pous::Single::Element::Type::Declaration,
    iec61131::pous::String::Type::Declaration,
    iec61131::pous::Function::Name,
    iec61131::pous::Access::Name,
    Symbolic::Variable,
    iec61131::variables::Multi::Element::Variable,
    Access::Name,
    iec61131::pous::Program::Access::Decl,
    iec61131::pous::Function::Block::Body,
    Program::Type::Name,
    Function::Return::Value,
    Derived::Function::Name,
    Function::Block::Vars,
    Derived::Function::Block::Name,
    pous::Function::Block::Type::Name,
    types::Simple::Specification,
    iec61131::types::Elementary::Type::Name,
    iec61131::types::Simple::Type::Name,
    iec61131::types::Generic::Type::Name,
    Blocks,
    iec61131::pous::Derived::Function::Block::Name,
    iec61131::pous::Derived::Function::Name,
    iec61131::pous::Program::Type::Name,
    Function::Block::Body,
    iec61131::sfc::Sequential::Function::Chart,
    iec61131::interfaces::InitElement::Array,
    iec61131::interfaces::Temp::Var::Declaration,
    iec61131::interfaces::InitElement::Structure,
    iec61131::interfaces::Var1::Specification::Func,
    iec61131::interfaces::Simple::Specification::Func,
    Simple::Specification::Func,
    Var1::Specification::Func,
    iec61131::interfaces::Simple::Spec::Init::Func,
    iec61131::interfaces::Var::Init::Decl::Func,
    Simple::Spec::Init,
    iec61131::interfaces::Var::Name::Decl,
    iec61131::interfaces::Function::Var::Decl,
    iec61131::interfaces::Var2::Init::Decl,
    Array::Type::Name,
    iec61131::interfaces::Array::Specification1,
    iec61131::interfaces::InitElement::EnumValue,
    iec61131::interfaces::InitElement::Constant,
    iec61131::interfaces::Initial::Element,
    iec61131::interfaces::Array::Initial::Elements2,
    iec61131::interfaces::Array::Initial::Elements1,
    Non::Generic::Type::Name,
    iec61131::types::Derived::Type::Name,
    iec61131::interfaces::Array::Specification2,
    Global::Var::Decl,
    Library::Element::Declaration,
    iec61131::configurations::Configuration::Declaration,
    iec61131::pous::Function::Declaration,
    iec61131::pous::Function::Block::Declaration,
    iec61131::configurations::Resource::Declaration,
    iec61131::pous::Data::Type::Declaration,
    iec61131::pous::Program::Declaration,
    iec61131::interfaces::Global::Var::Declarations,
    Located::Var::Decl,
    Program::Vars,
    iec61131::pous::Program::Access::Decls,
    iec61131::interfaces::Located::Var::Declarations,
    iec61131::interfaces::Enumerated::Specification2,
    iec61131::interfaces::Enumerated::Specification1,
    Subrange::Type::Name,
    iec61131::interfaces::Subrange::Specification2,
    Subrange,
    iec61131::interfaces::Subrange::Specification1,
    Double::Byte::String::Type::Name,
    Single::Byte::String::Type::Name,
    Byte::String,
    iec61131::interfaces::Double::BString,
    iec61131::interfaces::Single::BString,
    iec61131::interfaces::Byte::String,
    iec61131::interfaces::Range,
    iec61131::interfaces::Input::Declaration,
    iec61131::interfaces::Global::Var::Location,
    iec61131::interfaces::Global::Var::Spec,
    External::Specification,
    Global::Var::Name,
    iec61131::interfaces::External::Declaration,
    RNV::Declarations,
    iec61131::interfaces::Var::Declarations,
    iec61131::interfaces::Non::Retentive::Var::Declarations,
    iec61131::interfaces::Retentive::Var::Declarations,
    External::Declaration,
    Other::Var::Declaration,
    iec61131::interfaces::RNV::Declarations,
    iec61131::interfaces::Temp::Var::Decls,
    iec61131::interfaces::External::Var::Declarations,
    iec61131::interfaces::Incompl::Located::Var::Declarations,
    operators::Multiply::Operator,
    operators::Add::Operator,
    operators::Arithmetic::Name,
    iec61131::operators::Divide::Name,
    iec61131::operators::Multiply::Name,
    operators::Addition::Operator,
    iec61131::operators::Addition::Symbol,
    iec61131::operators::Addition::Name,
    Comparison::Operator,
    iec61131::operators::LessEqual::Operator,
    iec61131::operators::GreaterEqual::Operator,
    iec61131::operators::Greater::Operator,
    iec61131::operators::Less::Operator,
    Il::Expr::Operator,
    iec61131::operators::Arithmetic::Name,
    iec61131::operators::Comparison::Name,
    operators::Substraction::Operator,
    iec61131::operators::Substraction::Name,
    GreaterEqual::Operator,
    iec61131::operators::GreaterEqual::Symbol,
    operators::GreaterEqual::Operator,
    Greater::Operator,
    iec61131::operators::Greater::Symbol,
    operators::Greater::Operator,
    LessEqual::Operator,
    iec61131::operators::LessEqual::Symbol,
    operators::LessEqual::Operator,
    Less::Operator,
    iec61131::operators::Less::Symbol,
    operators::Less::Operator,
    Unequal::Operator,
    iec61131::operators::Unequal::Symbol,
    operators::Unequal::Operator,
    Equal::Operator,
    iec61131::operators::Equal::Symbol,
    operators::Comparison::Name,
    iec61131::operators::Unequal::Name,
    iec61131::operators::GreaterEqual::Name,
    iec61131::operators::Greater::Name,
    iec61131::operators::LessEqual::Name,
    iec61131::operators::Less::Name,
    operators::Equal::Operator,
    iec61131::operators::Equal::Name,
    And::Operator,
    iec61131::operators::And::Name,
    iec61131::operators::And::Symbol,
    Assignment::Operator,
    iec61131::operators::Assignment::Name,
    iec61131::operators::Assignment::Symbol,
    Power::Operator,
    iec61131::operators::Power::Name,
    iec61131::operators::Power::Symbol,
    Divide::Operator,
    iec61131::operators::Divide::Symbol,
    iec61131::literals::Integer,
    iec61131::literals::BSInteger,
    iec61131::literals::Date::Literal,
    iec61131::literals::Daytime,
    iec61131::literals::Fixed::Point::Literal,
    Double::Byte::Character::Representation,
    operators::Dot::Operator,
    il::Il::Simple::Operator,
    operators::Unary::Operator,
    iec61131::operators::Substraction::Symbol,
    iec61131::operators::Not::Operator,
    il::Il::Expr::Operator,
    iec61131::operators::Modulo::Operator,
    operators::Operator,
    iec61131::operators::Xor::Operator,
    iec61131::operators::Or::Operator,
    iec61131::operators::And::Operator,
    EquUequ::Operator,
    iec61131::operators::Unequal::Operator,
    iec61131::operators::Equal::Operator,
    Dot::Operator,
    iec61131::operators::Divide::Operator,
    iec61131::operators::Multiply::Operator,
    iec61131::operators::Substraction::Operator,
    iec61131::operators::Addition::Operator,
    Operator,
    iec61131::operators::Dot::Operator,
    iec61131::operators::EquUequ::Operator,
    iec61131::operators::Unary::Operator,
    iec61131::operators::Comparison::Operator,
    iec61131::operators::Assignment::Operator,
    iec61131::operators::Power::Operator,
    iec61131::operators::Add::Operator,
    iec61131::operators::Operator,
    iec61131::literals::Double::Byte::Character::Representation,
    Common::Character::Representation,
    iec61131::literals::Single::Byte::Character::Representation,
    iec61131::literals::Common::Character::Representation,
    DT::Type::Name,
    Date::Literal,
    Date::Type::Name,
    iec61131::types::DT::Type::Name,
    iec61131::types::TOD::Type::Name,
    Single::Byte::Character::Representation,
    Character::String,
    iec61131::literals::Double::Byte::Character::String,
    iec61131::literals::Single::Byte::Character::String,
    Milliseconds,
    Seconds,
    Minutes,
    Hours,
    Unsigned::Integer,
    Fixed::Point::Literal,
    iec61131::literals::Fixed::Point,
    iec61131::literals::Interval,
    literals::Fixed::Point::Literal,
    Integer,
    Numeric::Literal,
    iec61131::literals::Integer::Literal,
    Bit::String::Type::Name,
    iec61131::types::Bool::Type::Name,
    BSInteger,
    Constant,
    iec61131::literals::Bit::String::Literal,
    iec61131::literals::Character::String,
    iec61131::literals::Time::Literal,
    iec61131::literals::Numeric::Literal,
    TOD::Type::Name,
    Daytime,
    Time::Literal,
    iec61131::literals::Date::And::Time,
    iec61131::literals::Date,
    iec61131::literals::Time::Of::Day,
    Substraction::Operator,
    Duration::Type::Name,
    Interval,
    iec61131::literals::Days,
    iec61131::literals::Milliseconds,
    iec61131::literals::Seconds,
    iec61131::literals::Minutes,
    iec61131::literals::Hours,
    sfc::Action::Time,
    literals::Time::Literal,
    iec61131::literals::Duration,
    literals::BSInteger,
    interfaces::Range,
    st::Case::List::Element,
    literals::Integer,
    iec61131::literals::Binary::Integer,
    iec61131::literals::Octal::Integer,
    iec61131::literals::Hex::Integer,
    iec61131::literals::Unsigned::Integer,
    iec61131::literals::Signed::Integer,
    il::Il::Operand,
    configurations::Prog::Data::Source,
    iec61131::interfaces::Enumerated::Value,
    configurations::Data::Source,
    iec61131::configurations::Global::Var::Reference,
    iec61131::variables::Direct::Variable,
    iec61131::literals::Constant,
    iec61131::literals::Boolean::Literal,
    Fixed::Point,
    Real::Type::Name,
    iec61131::literals::Real::Literal,
    Integer::Type::Name,
    iec61131::types::Signed::Integer::Type::Name,
    iec61131::types::Unsigned::Integer::Type::Name,
    iec61131::NamedElement,
    iec61131::Commentable,
    NamedElement,
    iec61131::variables::Variable::Name,
    iec61131::sfc::Step::Name,
    Commentable,
    iec61131::st::Param::Assignment,
    iec61131::st::Statement,
    iec61131::configurations::Program::Configuration,
    iec61131::interfaces::Interface,
    iec61131::st::Expression::Variable,
    iec61131::interfaces::Global::Var::Name,
    iec61131::variables::Variable,
    iec61131::st::Expression::Types,
    iec61131::pous::Function::Block::Type::Name,
    iec61131::interfaces::Global::Var::Decl,
    iec61131::Library::Element::Name,
    iec61131::Library::Element::Declaration,
    iec61131::IEC61131,
    Edge,
    Direction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_iec61131::sfc::action::qualifier_is_not_abstract():
    assert not inspect.isabstract(iec61131::sfc::Action::Qualifier)


def test_iec61131::sfc::action::qualifier_constructor_exists():
    assert callable(iec61131::sfc::Action::Qualifier.__init__)


def test_iec61131::sfc::action::qualifier_constructor_args():
    sig = inspect.signature(iec61131::sfc::Action::Qualifier.__init__)
    params = list(sig.parameters.keys())
    assert "qualifier" in params, "Missing parameter 'qualifier'"

def test_iec61131::sfc::action::qualifier_has_qualifier():
    assert hasattr(iec61131::sfc::Action::Qualifier, "qualifier")
    descriptor = None
    for klass in iec61131::sfc::Action::Qualifier.__mro__:
        if "qualifier" in klass.__dict__:
            descriptor = klass.__dict__["qualifier"]
            break
    assert isinstance(descriptor, property)



def test_iec61131::sfc::action::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::sfc::Action::Name)


def test_iec61131::sfc::action::name_constructor_exists():
    assert callable(iec61131::sfc::Action::Name.__init__)


def test_iec61131::sfc::action::name_constructor_args():
    sig = inspect.signature(iec61131::sfc::Action::Name.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iec61131::sfc::action::name_has_name():
    assert hasattr(iec61131::sfc::Action::Name, "name")
    descriptor = None
    for klass in iec61131::sfc::Action::Name.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_step::name_is_not_abstract():
    assert not inspect.isabstract(Step::Name)


def test_step::name_constructor_exists():
    assert callable(Step::Name.__init__)


def test_step::name_constructor_args():
    sig = inspect.signature(Step::Name.__init__)
    params = list(sig.parameters.keys())



def test_action::association_is_not_abstract():
    assert not inspect.isabstract(Action::Association)


def test_action::association_constructor_exists():
    assert callable(Action::Association.__init__)


def test_action::association_constructor_args():
    sig = inspect.signature(Action::Association.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::sfc::step::types_is_not_abstract():
    assert not inspect.isabstract(iec61131::sfc::Step::Types)


def test_iec61131::sfc::step::types_constructor_exists():
    assert callable(iec61131::sfc::Step::Types.__init__)


def test_iec61131::sfc::step::types_constructor_args():
    sig = inspect.signature(iec61131::sfc::Step::Types.__init__)
    params = list(sig.parameters.keys())



def test_action::qualifier_is_not_abstract():
    assert not inspect.isabstract(Action::Qualifier)


def test_action::qualifier_constructor_exists():
    assert callable(Action::Qualifier.__init__)


def test_action::qualifier_constructor_args():
    sig = inspect.signature(Action::Qualifier.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::sfc::action::association_is_not_abstract():
    assert not inspect.isabstract(iec61131::sfc::Action::Association)


def test_iec61131::sfc::action::association_constructor_exists():
    assert callable(iec61131::sfc::Action::Association.__init__)


def test_iec61131::sfc::action::association_constructor_args():
    sig = inspect.signature(iec61131::sfc::Action::Association.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::sfc::sfc::elements_is_not_abstract():
    assert not inspect.isabstract(iec61131::sfc::Sfc::Elements)


def test_iec61131::sfc::sfc::elements_constructor_exists():
    assert callable(iec61131::sfc::Sfc::Elements.__init__)


def test_iec61131::sfc::sfc::elements_constructor_args():
    sig = inspect.signature(iec61131::sfc::Sfc::Elements.__init__)
    params = list(sig.parameters.keys())



def test_action::name_is_not_abstract():
    assert not inspect.isabstract(Action::Name)


def test_action::name_constructor_exists():
    assert callable(Action::Name.__init__)


def test_action::name_constructor_args():
    sig = inspect.signature(Action::Name.__init__)
    params = list(sig.parameters.keys())



def test_transition::condition_is_not_abstract():
    assert not inspect.isabstract(Transition::Condition)


def test_transition::condition_constructor_exists():
    assert callable(Transition::Condition.__init__)


def test_transition::condition_constructor_args():
    sig = inspect.signature(Transition::Condition.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::sfc::sfc::network_is_not_abstract():
    assert not inspect.isabstract(iec61131::sfc::Sfc::Network)


def test_iec61131::sfc::sfc::network_constructor_exists():
    assert callable(iec61131::sfc::Sfc::Network.__init__)


def test_iec61131::sfc::sfc::network_constructor_args():
    sig = inspect.signature(iec61131::sfc::Sfc::Network.__init__)
    params = list(sig.parameters.keys())



def test_sfc::network_is_not_abstract():
    assert not inspect.isabstract(Sfc::Network)


def test_sfc::network_constructor_exists():
    assert callable(Sfc::Network.__init__)


def test_sfc::network_constructor_args():
    sig = inspect.signature(Sfc::Network.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::il::assign::out::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Il::Assign::Out::Operator)


def test_iec61131::il::il::assign::out::operator_constructor_exists():
    assert callable(iec61131::il::Il::Assign::Out::Operator.__init__)


def test_iec61131::il::il::assign::out::operator_constructor_args():
    sig = inspect.signature(iec61131::il::Il::Assign::Out::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::param::assignment_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Param::Assignment)


def test_iec61131::il::param::assignment_constructor_exists():
    assert callable(iec61131::il::Param::Assignment.__init__)


def test_iec61131::il::param::assignment_constructor_args():
    sig = inspect.signature(iec61131::il::Param::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_assignment::name_is_not_abstract():
    assert not inspect.isabstract(Assignment::Name)


def test_assignment::name_constructor_exists():
    assert callable(Assignment::Name.__init__)


def test_assignment::name_constructor_args():
    sig = inspect.signature(Assignment::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::il::assign::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Il::Assign::Operator)


def test_iec61131::il::il::assign::operator_constructor_exists():
    assert callable(iec61131::il::Il::Assign::Operator.__init__)


def test_iec61131::il::il::assign::operator_constructor_args():
    sig = inspect.signature(iec61131::il::Il::Assign::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::param::instruction_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Param::Instruction)


def test_iec61131::il::param::instruction_constructor_exists():
    assert callable(iec61131::il::Param::Instruction.__init__)


def test_iec61131::il::param::instruction_constructor_args():
    sig = inspect.signature(iec61131::il::Param::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::param::assignments_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Param::Assignments)


def test_iec61131::il::param::assignments_constructor_exists():
    assert callable(iec61131::il::Param::Assignments.__init__)


def test_iec61131::il::param::assignments_constructor_args():
    sig = inspect.signature(iec61131::il::Param::Assignments.__init__)
    params = list(sig.parameters.keys())



def test_il::assign::out::operator_is_not_abstract():
    assert not inspect.isabstract(Il::Assign::Out::Operator)


def test_il::assign::out::operator_constructor_exists():
    assert callable(Il::Assign::Out::Operator.__init__)


def test_il::assign::out::operator_constructor_args():
    sig = inspect.signature(Il::Assign::Out::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::il::operand::list_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Il::Operand::List)


def test_iec61131::il::il::operand::list_constructor_exists():
    assert callable(iec61131::il::Il::Operand::List.__init__)


def test_iec61131::il::il::operand::list_constructor_args():
    sig = inspect.signature(iec61131::il::Il::Operand::List.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::il::simple::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Il::Simple::Operator)


def test_iec61131::il::il::simple::operator_constructor_exists():
    assert callable(iec61131::il::Il::Simple::Operator.__init__)


def test_iec61131::il::il::simple::operator_constructor_args():
    sig = inspect.signature(iec61131::il::Il::Simple::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::il::operations_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Il::Operations)


def test_iec61131::il::il::operations_constructor_exists():
    assert callable(iec61131::il::Il::Operations.__init__)


def test_iec61131::il::il::operations_constructor_args():
    sig = inspect.signature(iec61131::il::Il::Operations.__init__)
    params = list(sig.parameters.keys())



def test_il::param::list_is_not_abstract():
    assert not inspect.isabstract(Il::Param::List)


def test_il::param::list_constructor_exists():
    assert callable(Il::Param::List.__init__)


def test_il::param::list_constructor_args():
    sig = inspect.signature(Il::Param::List.__init__)
    params = list(sig.parameters.keys())



def test_il::assign::operator_is_not_abstract():
    assert not inspect.isabstract(Il::Assign::Operator)


def test_il::assign::operator_constructor_exists():
    assert callable(Il::Assign::Operator.__init__)


def test_il::assign::operator_constructor_args():
    sig = inspect.signature(Il::Assign::Operator.__init__)
    params = list(sig.parameters.keys())



def test_param::assignments_is_not_abstract():
    assert not inspect.isabstract(Param::Assignments)


def test_param::assignments_constructor_exists():
    assert callable(Param::Assignments.__init__)


def test_param::assignments_constructor_args():
    sig = inspect.signature(Param::Assignments.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::il::param::out::assignment_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Il::Param::Out::Assignment)


def test_iec61131::il::il::param::out::assignment_constructor_exists():
    assert callable(iec61131::il::Il::Param::Out::Assignment.__init__)


def test_iec61131::il::il::param::out::assignment_constructor_args():
    sig = inspect.signature(iec61131::il::Il::Param::Out::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::il::param::assignment_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Il::Param::Assignment)


def test_iec61131::il::il::param::assignment_constructor_exists():
    assert callable(iec61131::il::Il::Param::Assignment.__init__)


def test_iec61131::il::il::param::assignment_constructor_args():
    sig = inspect.signature(iec61131::il::Il::Param::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_param::instruction_is_not_abstract():
    assert not inspect.isabstract(Param::Instruction)


def test_param::instruction_constructor_exists():
    assert callable(Param::Instruction.__init__)


def test_param::instruction_constructor_args():
    sig = inspect.signature(Param::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::il::param::last::instruction_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Il::Param::Last::Instruction)


def test_iec61131::il::il::param::last::instruction_constructor_exists():
    assert callable(iec61131::il::Il::Param::Last::Instruction.__init__)


def test_iec61131::il::il::param::last::instruction_constructor_args():
    sig = inspect.signature(iec61131::il::Il::Param::Last::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::il::param::instruction_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Il::Param::Instruction)


def test_iec61131::il::il::param::instruction_constructor_exists():
    assert callable(iec61131::il::Il::Param::Instruction.__init__)


def test_iec61131::il::il::param::instruction_constructor_args():
    sig = inspect.signature(iec61131::il::Il::Param::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::simple::instr_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Simple::Instr)


def test_iec61131::il::simple::instr_constructor_exists():
    assert callable(iec61131::il::Simple::Instr.__init__)


def test_iec61131::il::simple::instr_constructor_args():
    sig = inspect.signature(iec61131::il::Simple::Instr.__init__)
    params = list(sig.parameters.keys())



def test_simple::instr_is_not_abstract():
    assert not inspect.isabstract(Simple::Instr)


def test_simple::instr_constructor_exists():
    assert callable(Simple::Instr.__init__)


def test_simple::instr_constructor_args():
    sig = inspect.signature(Simple::Instr.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::il::simple::instruction_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Il::Simple::Instruction)


def test_iec61131::il::il::simple::instruction_constructor_exists():
    assert callable(iec61131::il::Il::Simple::Instruction.__init__)


def test_iec61131::il::il::simple::instruction_constructor_args():
    sig = inspect.signature(iec61131::il::Il::Simple::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::operands_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Operands)


def test_iec61131::il::operands_constructor_exists():
    assert callable(iec61131::il::Operands.__init__)


def test_iec61131::il::operands_constructor_args():
    sig = inspect.signature(iec61131::il::Operands.__init__)
    params = list(sig.parameters.keys())



def test_il::param::last::instruction_is_not_abstract():
    assert not inspect.isabstract(Il::Param::Last::Instruction)


def test_il::param::last::instruction_constructor_exists():
    assert callable(Il::Param::Last::Instruction.__init__)


def test_il::param::last::instruction_constructor_args():
    sig = inspect.signature(Il::Param::Last::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_il::param::instruction_is_not_abstract():
    assert not inspect.isabstract(Il::Param::Instruction)


def test_il::param::instruction_constructor_exists():
    assert callable(Il::Param::Instruction.__init__)


def test_il::param::instruction_constructor_args():
    sig = inspect.signature(Il::Param::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::il::param::list_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Il::Param::List)


def test_iec61131::il::il::param::list_constructor_exists():
    assert callable(iec61131::il::Il::Param::List.__init__)


def test_iec61131::il::il::param::list_constructor_args():
    sig = inspect.signature(iec61131::il::Il::Param::List.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::il::call::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Il::Call::Operator)


def test_iec61131::il::il::call::operator_constructor_exists():
    assert callable(iec61131::il::Il::Call::Operator.__init__)


def test_iec61131::il::il::call::operator_constructor_args():
    sig = inspect.signature(iec61131::il::Il::Call::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::il::jump::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Il::Jump::Operator)


def test_iec61131::il::il::jump::operator_constructor_exists():
    assert callable(iec61131::il::Il::Jump::Operator.__init__)


def test_iec61131::il::il::jump::operator_constructor_args():
    sig = inspect.signature(iec61131::il::Il::Jump::Operator.__init__)
    params = list(sig.parameters.keys())



def test_il::operand::list_is_not_abstract():
    assert not inspect.isabstract(Il::Operand::List)


def test_il::operand::list_constructor_exists():
    assert callable(Il::Operand::List.__init__)


def test_il::operand::list_constructor_args():
    sig = inspect.signature(Il::Operand::List.__init__)
    params = list(sig.parameters.keys())



def test_il::simple::operator_is_not_abstract():
    assert not inspect.isabstract(Il::Simple::Operator)


def test_il::simple::operator_constructor_exists():
    assert callable(Il::Simple::Operator.__init__)


def test_il::simple::operator_constructor_args():
    sig = inspect.signature(Il::Simple::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::il::expr::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Il::Expr::Operator)


def test_iec61131::il::il::expr::operator_constructor_exists():
    assert callable(iec61131::il::Il::Expr::Operator.__init__)


def test_iec61131::il::il::expr::operator_constructor_args():
    sig = inspect.signature(iec61131::il::Il::Expr::Operator.__init__)
    params = list(sig.parameters.keys())



def test_il::simple::operation_is_not_abstract():
    assert not inspect.isabstract(Il::Simple::Operation)


def test_il::simple::operation_constructor_exists():
    assert callable(Il::Simple::Operation.__init__)


def test_il::simple::operation_constructor_args():
    sig = inspect.signature(Il::Simple::Operation.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::simple::operation2_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Simple::Operation2)


def test_iec61131::il::simple::operation2_constructor_exists():
    assert callable(iec61131::il::Simple::Operation2.__init__)


def test_iec61131::il::simple::operation2_constructor_args():
    sig = inspect.signature(iec61131::il::Simple::Operation2.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::simple::operation1_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Simple::Operation1)


def test_iec61131::il::simple::operation1_constructor_exists():
    assert callable(iec61131::il::Simple::Operation1.__init__)


def test_iec61131::il::simple::operation1_constructor_args():
    sig = inspect.signature(iec61131::il::Simple::Operation1.__init__)
    params = list(sig.parameters.keys())



def test_il::instruction_is_not_abstract():
    assert not inspect.isabstract(Il::Instruction)


def test_il::instruction_constructor_exists():
    assert callable(Il::Instruction.__init__)


def test_il::instruction_constructor_args():
    sig = inspect.signature(Il::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_operands_is_not_abstract():
    assert not inspect.isabstract(Operands)


def test_operands_constructor_exists():
    assert callable(Operands.__init__)


def test_operands_constructor_args():
    sig = inspect.signature(Operands.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::operand2_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Operand2)


def test_iec61131::il::operand2_constructor_exists():
    assert callable(iec61131::il::Operand2.__init__)


def test_iec61131::il::operand2_constructor_args():
    sig = inspect.signature(iec61131::il::Operand2.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::operand1_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Operand1)


def test_iec61131::il::operand1_constructor_exists():
    assert callable(iec61131::il::Operand1.__init__)


def test_iec61131::il::operand1_constructor_args():
    sig = inspect.signature(iec61131::il::Operand1.__init__)
    params = list(sig.parameters.keys())



def test_il::call::operator_is_not_abstract():
    assert not inspect.isabstract(Il::Call::Operator)


def test_il::call::operator_constructor_exists():
    assert callable(Il::Call::Operator.__init__)


def test_il::call::operator_constructor_args():
    sig = inspect.signature(Il::Call::Operator.__init__)
    params = list(sig.parameters.keys())



def test_il::jump::operator_is_not_abstract():
    assert not inspect.isabstract(Il::Jump::Operator)


def test_il::jump::operator_constructor_exists():
    assert callable(Il::Jump::Operator.__init__)


def test_il::jump::operator_constructor_args():
    sig = inspect.signature(Il::Jump::Operator.__init__)
    params = list(sig.parameters.keys())



def test_simple::instr::list_is_not_abstract():
    assert not inspect.isabstract(Simple::Instr::List)


def test_simple::instr::list_constructor_exists():
    assert callable(Simple::Instr::List.__init__)


def test_simple::instr::list_constructor_args():
    sig = inspect.signature(Simple::Instr::List.__init__)
    params = list(sig.parameters.keys())



def test_il::operand_is_not_abstract():
    assert not inspect.isabstract(Il::Operand)


def test_il::operand_constructor_exists():
    assert callable(Il::Operand.__init__)


def test_il::operand_constructor_args():
    sig = inspect.signature(Il::Operand.__init__)
    params = list(sig.parameters.keys())



def test_il::simple::instr_is_not_abstract():
    assert not inspect.isabstract(il::Simple::Instr)


def test_il::simple::instr_constructor_exists():
    assert callable(il::Simple::Instr.__init__)


def test_il::simple::instr_constructor_args():
    sig = inspect.signature(il::Simple::Instr.__init__)
    params = list(sig.parameters.keys())



def test_il::il::operations_is_not_abstract():
    assert not inspect.isabstract(il::Il::Operations)


def test_il::il::operations_constructor_exists():
    assert callable(il::Il::Operations.__init__)


def test_il::il::operations_constructor_args():
    sig = inspect.signature(il::Il::Operations.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::il::expression_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Il::Expression)


def test_iec61131::il::il::expression_constructor_exists():
    assert callable(iec61131::il::Il::Expression.__init__)


def test_iec61131::il::il::expression_constructor_args():
    sig = inspect.signature(iec61131::il::Il::Expression.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::il::formal::funct::call_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Il::Formal::Funct::Call)


def test_iec61131::il::il::formal::funct::call_constructor_exists():
    assert callable(iec61131::il::Il::Formal::Funct::Call.__init__)


def test_iec61131::il::il::formal::funct::call_constructor_args():
    sig = inspect.signature(iec61131::il::Il::Formal::Funct::Call.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::il::simple::operation_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Il::Simple::Operation)


def test_iec61131::il::il::simple::operation_constructor_exists():
    assert callable(iec61131::il::Il::Simple::Operation.__init__)


def test_iec61131::il::il::simple::operation_constructor_args():
    sig = inspect.signature(iec61131::il::Il::Simple::Operation.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::label_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Label)


def test_iec61131::il::label_constructor_exists():
    assert callable(iec61131::il::Label.__init__)


def test_iec61131::il::label_constructor_args():
    sig = inspect.signature(iec61131::il::Label.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"

def test_iec61131::il::label_has_label():
    assert hasattr(iec61131::il::Label, "label")
    descriptor = None
    for klass in iec61131::il::Label.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)



def test_il::operations_is_not_abstract():
    assert not inspect.isabstract(Il::Operations)


def test_il::operations_constructor_exists():
    assert callable(Il::Operations.__init__)


def test_il::operations_constructor_args():
    sig = inspect.signature(Il::Operations.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::il::return::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Il::Return::Operator)


def test_iec61131::il::il::return::operator_constructor_exists():
    assert callable(iec61131::il::Il::Return::Operator.__init__)


def test_iec61131::il::il::return::operator_constructor_args():
    sig = inspect.signature(iec61131::il::Il::Return::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::il::jump::operation_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Il::Jump::Operation)


def test_iec61131::il::il::jump::operation_constructor_exists():
    assert callable(iec61131::il::Il::Jump::Operation.__init__)


def test_iec61131::il::il::jump::operation_constructor_args():
    sig = inspect.signature(iec61131::il::Il::Jump::Operation.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::il::fb::call_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Il::Fb::Call)


def test_iec61131::il::il::fb::call_constructor_exists():
    assert callable(iec61131::il::Il::Fb::Call.__init__)


def test_iec61131::il::il::fb::call_constructor_args():
    sig = inspect.signature(iec61131::il::Il::Fb::Call.__init__)
    params = list(sig.parameters.keys())



def test_label_is_not_abstract():
    assert not inspect.isabstract(Label)


def test_label_constructor_exists():
    assert callable(Label.__init__)


def test_label_constructor_args():
    sig = inspect.signature(Label.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::il::instruction_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Il::Instruction)


def test_iec61131::il::il::instruction_constructor_exists():
    assert callable(iec61131::il::Il::Instruction.__init__)


def test_iec61131::il::il::instruction_constructor_args():
    sig = inspect.signature(iec61131::il::Il::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_il::simple::instruction_is_not_abstract():
    assert not inspect.isabstract(Il::Simple::Instruction)


def test_il::simple::instruction_constructor_exists():
    assert callable(Il::Simple::Instruction.__init__)


def test_il::simple::instruction_constructor_args():
    sig = inspect.signature(Il::Simple::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::simple::instr::list_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Simple::Instr::List)


def test_iec61131::il::simple::instr::list_constructor_exists():
    assert callable(iec61131::il::Simple::Instr::List.__init__)


def test_iec61131::il::simple::instr::list_constructor_args():
    sig = inspect.signature(iec61131::il::Simple::Instr::List.__init__)
    params = list(sig.parameters.keys())



def test_unary::operator_is_not_abstract():
    assert not inspect.isabstract(Unary::Operator)


def test_unary::operator_constructor_exists():
    assert callable(Unary::Operator.__init__)


def test_unary::operator_constructor_args():
    sig = inspect.signature(Unary::Operator.__init__)
    params = list(sig.parameters.keys())



def test_power::symbol_is_not_abstract():
    assert not inspect.isabstract(Power::Symbol)


def test_power::symbol_constructor_exists():
    assert callable(Power::Symbol.__init__)


def test_power::symbol_constructor_args():
    sig = inspect.signature(Power::Symbol.__init__)
    params = list(sig.parameters.keys())



def test_structured::variable_is_not_abstract():
    assert not inspect.isabstract(Structured::Variable)


def test_structured::variable_constructor_exists():
    assert callable(Structured::Variable.__init__)


def test_structured::variable_constructor_args():
    sig = inspect.signature(Structured::Variable.__init__)
    params = list(sig.parameters.keys())



def test_array::variable_is_not_abstract():
    assert not inspect.isabstract(Array::Variable)


def test_array::variable_constructor_exists():
    assert callable(Array::Variable.__init__)


def test_array::variable_constructor_args():
    sig = inspect.signature(Array::Variable.__init__)
    params = list(sig.parameters.keys())



def test_function::name_is_not_abstract():
    assert not inspect.isabstract(Function::Name)


def test_function::name_constructor_exists():
    assert callable(Function::Name.__init__)


def test_function::name_constructor_args():
    sig = inspect.signature(Function::Name.__init__)
    params = list(sig.parameters.keys())



def test_primary::expression_is_not_abstract():
    assert not inspect.isabstract(Primary::Expression)


def test_primary::expression_constructor_exists():
    assert callable(Primary::Expression.__init__)


def test_primary::expression_constructor_args():
    sig = inspect.signature(Primary::Expression.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::expression::variable::type_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Expression::Variable::Type)


def test_iec61131::st::expression::variable::type_constructor_exists():
    assert callable(iec61131::st::Expression::Variable::Type.__init__)


def test_iec61131::st::expression::variable::type_constructor_args():
    sig = inspect.signature(iec61131::st::Expression::Variable::Type.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::expression::enumvalue_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Expression::EnumValue)


def test_iec61131::st::expression::enumvalue_constructor_exists():
    assert callable(iec61131::st::Expression::EnumValue.__init__)


def test_iec61131::st::expression::enumvalue_constructor_args():
    sig = inspect.signature(iec61131::st::Expression::EnumValue.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::call::expression_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Call::Expression)


def test_iec61131::st::call::expression_constructor_exists():
    assert callable(iec61131::st::Call::Expression.__init__)


def test_iec61131::st::call::expression_constructor_args():
    sig = inspect.signature(iec61131::st::Call::Expression.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::expression::constant_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Expression::Constant)


def test_iec61131::st::expression::constant_constructor_exists():
    assert callable(iec61131::st::Expression::Constant.__init__)


def test_iec61131::st::expression::constant_constructor_args():
    sig = inspect.signature(iec61131::st::Expression::Constant.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::bracket::expression_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Bracket::Expression)


def test_iec61131::st::bracket::expression_constructor_exists():
    assert callable(iec61131::st::Bracket::Expression.__init__)


def test_iec61131::st::bracket::expression_constructor_args():
    sig = inspect.signature(iec61131::st::Bracket::Expression.__init__)
    params = list(sig.parameters.keys())



def test_add::operator_is_not_abstract():
    assert not inspect.isabstract(Add::Operator)


def test_add::operator_constructor_exists():
    assert callable(Add::Operator.__init__)


def test_add::operator_constructor_args():
    sig = inspect.signature(Add::Operator.__init__)
    params = list(sig.parameters.keys())



def test_xor::operator_is_not_abstract():
    assert not inspect.isabstract(Xor::Operator)


def test_xor::operator_constructor_exists():
    assert callable(Xor::Operator.__init__)


def test_xor::operator_constructor_args():
    sig = inspect.signature(Xor::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::for::list_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::For::List)


def test_iec61131::st::for::list_constructor_exists():
    assert callable(iec61131::st::For::List.__init__)


def test_iec61131::st::for::list_constructor_args():
    sig = inspect.signature(iec61131::st::For::List.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::control::variable_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Control::Variable)


def test_iec61131::st::control::variable_constructor_exists():
    assert callable(iec61131::st::Control::Variable.__init__)


def test_iec61131::st::control::variable_constructor_args():
    sig = inspect.signature(iec61131::st::Control::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iec61131::st::control::variable_has_name():
    assert hasattr(iec61131::st::Control::Variable, "name")
    descriptor = None
    for klass in iec61131::st::Control::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statement::list_is_not_abstract():
    assert not inspect.isabstract(Statement::List)


def test_statement::list_constructor_exists():
    assert callable(Statement::List.__init__)


def test_statement::list_constructor_args():
    sig = inspect.signature(Statement::List.__init__)
    params = list(sig.parameters.keys())



def test_selection::statement_is_not_abstract():
    assert not inspect.isabstract(Selection::Statement)


def test_selection::statement_constructor_exists():
    assert callable(Selection::Statement.__init__)


def test_selection::statement_constructor_args():
    sig = inspect.signature(Selection::Statement.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::if::statement_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::If::Statement)


def test_iec61131::st::if::statement_constructor_exists():
    assert callable(iec61131::st::If::Statement.__init__)


def test_iec61131::st::if::statement_constructor_args():
    sig = inspect.signature(iec61131::st::If::Statement.__init__)
    params = list(sig.parameters.keys())



def test_not::operator_is_not_abstract():
    assert not inspect.isabstract(Not::Operator)


def test_not::operator_constructor_exists():
    assert callable(Not::Operator.__init__)


def test_not::operator_constructor_args():
    sig = inspect.signature(Not::Operator.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_for::list_is_not_abstract():
    assert not inspect.isabstract(For::List)


def test_for::list_constructor_exists():
    assert callable(For::List.__init__)


def test_for::list_constructor_args():
    sig = inspect.signature(For::List.__init__)
    params = list(sig.parameters.keys())



def test_control::variable_is_not_abstract():
    assert not inspect.isabstract(Control::Variable)


def test_control::variable_constructor_exists():
    assert callable(Control::Variable.__init__)


def test_control::variable_constructor_args():
    sig = inspect.signature(Control::Variable.__init__)
    params = list(sig.parameters.keys())



def test_iteration::statement_is_not_abstract():
    assert not inspect.isabstract(Iteration::Statement)


def test_iteration::statement_constructor_exists():
    assert callable(Iteration::Statement.__init__)


def test_iteration::statement_constructor_args():
    sig = inspect.signature(Iteration::Statement.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::exit::statement_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Exit::Statement)


def test_iec61131::st::exit::statement_constructor_exists():
    assert callable(iec61131::st::Exit::Statement.__init__)


def test_iec61131::st::exit::statement_constructor_args():
    sig = inspect.signature(iec61131::st::Exit::Statement.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::while::statement_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::While::Statement)


def test_iec61131::st::while::statement_constructor_exists():
    assert callable(iec61131::st::While::Statement.__init__)


def test_iec61131::st::while::statement_constructor_args():
    sig = inspect.signature(iec61131::st::While::Statement.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::repeat::statement_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Repeat::Statement)


def test_iec61131::st::repeat::statement_constructor_exists():
    assert callable(iec61131::st::Repeat::Statement.__init__)


def test_iec61131::st::repeat::statement_constructor_args():
    sig = inspect.signature(iec61131::st::Repeat::Statement.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::for::statement_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::For::Statement)


def test_iec61131::st::for::statement_constructor_exists():
    assert callable(iec61131::st::For::Statement.__init__)


def test_iec61131::st::for::statement_constructor_args():
    sig = inspect.signature(iec61131::st::For::Statement.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::case::list::element_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Case::List::Element)


def test_iec61131::st::case::list::element_constructor_exists():
    assert callable(iec61131::st::Case::List::Element.__init__)


def test_iec61131::st::case::list::element_constructor_args():
    sig = inspect.signature(iec61131::st::Case::List::Element.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::case::list_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Case::List)


def test_iec61131::st::case::list_constructor_exists():
    assert callable(iec61131::st::Case::List.__init__)


def test_iec61131::st::case::list_constructor_args():
    sig = inspect.signature(iec61131::st::Case::List.__init__)
    params = list(sig.parameters.keys())



def test_case::list_is_not_abstract():
    assert not inspect.isabstract(Case::List)


def test_case::list_constructor_exists():
    assert callable(Case::List.__init__)


def test_case::list_constructor_args():
    sig = inspect.signature(Case::List.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::case::element_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Case::Element)


def test_iec61131::st::case::element_constructor_exists():
    assert callable(iec61131::st::Case::Element.__init__)


def test_iec61131::st::case::element_constructor_args():
    sig = inspect.signature(iec61131::st::Case::Element.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::else::statement_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Else::Statement)


def test_iec61131::st::else::statement_constructor_exists():
    assert callable(iec61131::st::Else::Statement.__init__)


def test_iec61131::st::else::statement_constructor_args():
    sig = inspect.signature(iec61131::st::Else::Statement.__init__)
    params = list(sig.parameters.keys())



def test_single::element::type::name_is_not_abstract():
    assert not inspect.isabstract(Single::Element::Type::Name)


def test_single::element::type::name_constructor_exists():
    assert callable(Single::Element::Type::Name.__init__)


def test_single::element::type::name_constructor_args():
    sig = inspect.signature(Single::Element::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::enumerated::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::Enumerated::Type::Name)


def test_iec61131::types::enumerated::type::name_constructor_exists():
    assert callable(iec61131::types::Enumerated::Type::Name.__init__)


def test_iec61131::types::enumerated::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::Enumerated::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::subrange::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::Subrange::Type::Name)


def test_iec61131::types::subrange::type::name_constructor_exists():
    assert callable(iec61131::types::Subrange::Type::Name.__init__)


def test_iec61131::types::subrange::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::Subrange::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_types::single::element::type::name_is_not_abstract():
    assert not inspect.isabstract(types::Single::Element::Type::Name)


def test_types::single::element::type::name_constructor_exists():
    assert callable(types::Single::Element::Type::Name.__init__)


def test_types::single::element::type::name_constructor_args():
    sig = inspect.signature(types::Single::Element::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_types::derived::type::name_is_not_abstract():
    assert not inspect.isabstract(types::Derived::Type::Name)


def test_types::derived::type::name_constructor_exists():
    assert callable(types::Derived::Type::Name.__init__)


def test_types::derived::type::name_constructor_args():
    sig = inspect.signature(types::Derived::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_derived::type::name_is_not_abstract():
    assert not inspect.isabstract(Derived::Type::Name)


def test_derived::type::name_constructor_exists():
    assert callable(Derived::Type::Name.__init__)


def test_derived::type::name_constructor_args():
    sig = inspect.signature(Derived::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::array::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::Array::Type::Name)


def test_iec61131::types::array::type::name_constructor_exists():
    assert callable(iec61131::types::Array::Type::Name.__init__)


def test_iec61131::types::array::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::Array::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::string::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::String::Type::Name)


def test_iec61131::types::string::type::name_constructor_exists():
    assert callable(iec61131::types::String::Type::Name.__init__)


def test_iec61131::types::string::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::String::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::single::element::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::Single::Element::Type::Name)


def test_iec61131::types::single::element::type::name_constructor_exists():
    assert callable(iec61131::types::Single::Element::Type::Name.__init__)


def test_iec61131::types::single::element::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::Single::Element::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::variables::subscript::list_is_not_abstract():
    assert not inspect.isabstract(iec61131::variables::Subscript::List)


def test_iec61131::variables::subscript::list_constructor_exists():
    assert callable(iec61131::variables::Subscript::List.__init__)


def test_iec61131::variables::subscript::list_constructor_args():
    sig = inspect.signature(iec61131::variables::Subscript::List.__init__)
    params = list(sig.parameters.keys())



def test_input::reference_is_not_abstract():
    assert not inspect.isabstract(Input::Reference)


def test_input::reference_constructor_exists():
    assert callable(Input::Reference.__init__)


def test_input::reference_constructor_args():
    sig = inspect.signature(Input::Reference.__init__)
    params = list(sig.parameters.keys())



def test_output::reference_is_not_abstract():
    assert not inspect.isabstract(Output::Reference)


def test_output::reference_constructor_exists():
    assert callable(Output::Reference.__init__)


def test_output::reference_constructor_args():
    sig = inspect.signature(Output::Reference.__init__)
    params = list(sig.parameters.keys())



def test_variables::symbolic::variable_is_not_abstract():
    assert not inspect.isabstract(variables::Symbolic::Variable)


def test_variables::symbolic::variable_constructor_exists():
    assert callable(variables::Symbolic::Variable.__init__)


def test_variables::symbolic::variable_constructor_args():
    sig = inspect.signature(variables::Symbolic::Variable.__init__)
    params = list(sig.parameters.keys())



def test_pous::function::return::value_is_not_abstract():
    assert not inspect.isabstract(pous::Function::Return::Value)


def test_pous::function::return::value_constructor_exists():
    assert callable(pous::Function::Return::Value.__init__)


def test_pous::function::return::value_constructor_args():
    sig = inspect.signature(pous::Function::Return::Value.__init__)
    params = list(sig.parameters.keys())



def test_types::data::type::name_is_not_abstract():
    assert not inspect.isabstract(types::Data::Type::Name)


def test_types::data::type::name_constructor_exists():
    assert callable(types::Data::Type::Name.__init__)


def test_types::data::type::name_constructor_args():
    sig = inspect.signature(types::Data::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::non::generic::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::Non::Generic::Type::Name)


def test_iec61131::types::non::generic::type::name_constructor_exists():
    assert callable(iec61131::types::Non::Generic::Type::Name.__init__)


def test_iec61131::types::non::generic::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::Non::Generic::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_interfaces::simple::specification::func_is_not_abstract():
    assert not inspect.isabstract(interfaces::Simple::Specification::Func)


def test_interfaces::simple::specification::func_constructor_exists():
    assert callable(interfaces::Simple::Specification::Func.__init__)


def test_interfaces::simple::specification::func_constructor_args():
    sig = inspect.signature(interfaces::Simple::Specification::Func.__init__)
    params = list(sig.parameters.keys())



def test_types::non::generic::type::name_is_not_abstract():
    assert not inspect.isabstract(types::Non::Generic::Type::Name)


def test_types::non::generic::type::name_constructor_exists():
    assert callable(types::Non::Generic::Type::Name.__init__)


def test_types::non::generic::type::name_constructor_args():
    sig = inspect.signature(types::Non::Generic::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_numeric::type::name_is_not_abstract():
    assert not inspect.isabstract(Numeric::Type::Name)


def test_numeric::type::name_constructor_exists():
    assert callable(Numeric::Type::Name.__init__)


def test_numeric::type::name_constructor_args():
    sig = inspect.signature(Numeric::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::real::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::Real::Type::Name)


def test_iec61131::types::real::type::name_constructor_exists():
    assert callable(iec61131::types::Real::Type::Name.__init__)


def test_iec61131::types::real::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::Real::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::integer::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::Integer::Type::Name)


def test_iec61131::types::integer::type::name_constructor_exists():
    assert callable(iec61131::types::Integer::Type::Name.__init__)


def test_iec61131::types::integer::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::Integer::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_elementary::type::name_is_not_abstract():
    assert not inspect.isabstract(Elementary::Type::Name)


def test_elementary::type::name_constructor_exists():
    assert callable(Elementary::Type::Name.__init__)


def test_elementary::type::name_constructor_args():
    sig = inspect.signature(Elementary::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::bit::string::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::Bit::String::Type::Name)


def test_iec61131::types::bit::string::type::name_constructor_exists():
    assert callable(iec61131::types::Bit::String::Type::Name.__init__)


def test_iec61131::types::bit::string::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::Bit::String::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::date::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::Date::Type::Name)


def test_iec61131::types::date::type::name_constructor_exists():
    assert callable(iec61131::types::Date::Type::Name.__init__)


def test_iec61131::types::date::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::Date::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::duration::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::Duration::Type::Name)


def test_iec61131::types::duration::type::name_constructor_exists():
    assert callable(iec61131::types::Duration::Type::Name.__init__)


def test_iec61131::types::duration::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::Duration::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::byte::string::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::Byte::String::Type::Name)


def test_iec61131::types::byte::string::type::name_constructor_exists():
    assert callable(iec61131::types::Byte::String::Type::Name.__init__)


def test_iec61131::types::byte::string::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::Byte::String::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::numeric::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::Numeric::Type::Name)


def test_iec61131::types::numeric::type::name_constructor_exists():
    assert callable(iec61131::types::Numeric::Type::Name.__init__)


def test_iec61131::types::numeric::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::Numeric::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_data::type::name_is_not_abstract():
    assert not inspect.isabstract(Data::Type::Name)


def test_data::type::name_constructor_exists():
    assert callable(Data::Type::Name.__init__)


def test_data::type::name_constructor_args():
    sig = inspect.signature(Data::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::simple::specification_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::Simple::Specification)


def test_iec61131::types::simple::specification_constructor_exists():
    assert callable(iec61131::types::Simple::Specification.__init__)


def test_iec61131::types::simple::specification_constructor_args():
    sig = inspect.signature(iec61131::types::Simple::Specification.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::typelib_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::TypeLib)


def test_iec61131::types::typelib_constructor_exists():
    assert callable(iec61131::types::TypeLib.__init__)


def test_iec61131::types::typelib_constructor_args():
    sig = inspect.signature(iec61131::types::TypeLib.__init__)
    params = list(sig.parameters.keys())



def test_fbd::network_is_not_abstract():
    assert not inspect.isabstract(Fbd::Network)


def test_fbd::network_constructor_exists():
    assert callable(Fbd::Network.__init__)


def test_fbd::network_constructor_args():
    sig = inspect.signature(Fbd::Network.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::sfc::transition::cond2_is_not_abstract():
    assert not inspect.isabstract(iec61131::sfc::Transition::Cond2)


def test_iec61131::sfc::transition::cond2_constructor_exists():
    assert callable(iec61131::sfc::Transition::Cond2.__init__)


def test_iec61131::sfc::transition::cond2_constructor_args():
    sig = inspect.signature(iec61131::sfc::Transition::Cond2.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::sfc::transition::condition_is_not_abstract():
    assert not inspect.isabstract(iec61131::sfc::Transition::Condition)


def test_iec61131::sfc::transition::condition_constructor_exists():
    assert callable(iec61131::sfc::Transition::Condition.__init__)


def test_iec61131::sfc::transition::condition_constructor_args():
    sig = inspect.signature(iec61131::sfc::Transition::Condition.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::sfc::steps_is_not_abstract():
    assert not inspect.isabstract(iec61131::sfc::Steps)


def test_iec61131::sfc::steps_constructor_exists():
    assert callable(iec61131::sfc::Steps.__init__)


def test_iec61131::sfc::steps_constructor_args():
    sig = inspect.signature(iec61131::sfc::Steps.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::sfc::transition::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::sfc::Transition::Name)


def test_iec61131::sfc::transition::name_constructor_exists():
    assert callable(iec61131::sfc::Transition::Name.__init__)


def test_iec61131::sfc::transition::name_constructor_args():
    sig = inspect.signature(iec61131::sfc::Transition::Name.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iec61131::sfc::transition::name_has_name():
    assert hasattr(iec61131::sfc::Transition::Name, "name")
    descriptor = None
    for klass in iec61131::sfc::Transition::Name.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iec61131::sfc::action::time_is_not_abstract():
    assert not inspect.isabstract(iec61131::sfc::Action::Time)


def test_iec61131::sfc::action::time_constructor_exists():
    assert callable(iec61131::sfc::Action::Time.__init__)


def test_iec61131::sfc::action::time_constructor_args():
    sig = inspect.signature(iec61131::sfc::Action::Time.__init__)
    params = list(sig.parameters.keys())



def test_variables::variable_is_not_abstract():
    assert not inspect.isabstract(variables::Variable)


def test_variables::variable_constructor_exists():
    assert callable(variables::Variable.__init__)


def test_variables::variable_constructor_args():
    sig = inspect.signature(variables::Variable.__init__)
    params = list(sig.parameters.keys())



def test_subscript::list_is_not_abstract():
    assert not inspect.isabstract(Subscript::List)


def test_subscript::list_constructor_exists():
    assert callable(Subscript::List.__init__)


def test_subscript::list_constructor_args():
    sig = inspect.signature(Subscript::List.__init__)
    params = list(sig.parameters.keys())



def test_multi::element::variable_is_not_abstract():
    assert not inspect.isabstract(Multi::Element::Variable)


def test_multi::element::variable_constructor_exists():
    assert callable(Multi::Element::Variable.__init__)


def test_multi::element::variable_constructor_args():
    sig = inspect.signature(Multi::Element::Variable.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::variables::structured::variable_is_not_abstract():
    assert not inspect.isabstract(iec61131::variables::Structured::Variable)


def test_iec61131::variables::structured::variable_constructor_exists():
    assert callable(iec61131::variables::Structured::Variable.__init__)


def test_iec61131::variables::structured::variable_constructor_args():
    sig = inspect.signature(iec61131::variables::Structured::Variable.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::variables::array::variable_is_not_abstract():
    assert not inspect.isabstract(iec61131::variables::Array::Variable)


def test_iec61131::variables::array::variable_constructor_exists():
    assert callable(iec61131::variables::Array::Variable.__init__)


def test_iec61131::variables::array::variable_constructor_args():
    sig = inspect.signature(iec61131::variables::Array::Variable.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::variables::symbolic::variable_is_not_abstract():
    assert not inspect.isabstract(iec61131::variables::Symbolic::Variable)


def test_iec61131::variables::symbolic::variable_constructor_exists():
    assert callable(iec61131::variables::Symbolic::Variable.__init__)


def test_iec61131::variables::symbolic::variable_constructor_args():
    sig = inspect.signature(iec61131::variables::Symbolic::Variable.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::sfc::cond2::condition_is_not_abstract():
    assert not inspect.isabstract(iec61131::sfc::Cond2::Condition)


def test_iec61131::sfc::cond2::condition_constructor_exists():
    assert callable(iec61131::sfc::Cond2::Condition.__init__)


def test_iec61131::sfc::cond2::condition_constructor_args():
    sig = inspect.signature(iec61131::sfc::Cond2::Condition.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::sfc::transition::cond3_is_not_abstract():
    assert not inspect.isabstract(iec61131::sfc::Transition::Cond3)


def test_iec61131::sfc::transition::cond3_constructor_exists():
    assert callable(iec61131::sfc::Transition::Cond3.__init__)


def test_iec61131::sfc::transition::cond3_constructor_args():
    sig = inspect.signature(iec61131::sfc::Transition::Cond3.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::sfc::transition::cond1_is_not_abstract():
    assert not inspect.isabstract(iec61131::sfc::Transition::Cond1)


def test_iec61131::sfc::transition::cond1_constructor_exists():
    assert callable(iec61131::sfc::Transition::Cond1.__init__)


def test_iec61131::sfc::transition::cond1_constructor_args():
    sig = inspect.signature(iec61131::sfc::Transition::Cond1.__init__)
    params = list(sig.parameters.keys())



def test_cond2::condition_is_not_abstract():
    assert not inspect.isabstract(Cond2::Condition)


def test_cond2::condition_constructor_exists():
    assert callable(Cond2::Condition.__init__)


def test_cond2::condition_constructor_args():
    sig = inspect.signature(Cond2::Condition.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::fbd::fbd::network_is_not_abstract():
    assert not inspect.isabstract(iec61131::fbd::Fbd::Network)


def test_iec61131::fbd::fbd::network_constructor_exists():
    assert callable(iec61131::fbd::Fbd::Network.__init__)


def test_iec61131::fbd::fbd::network_constructor_args():
    sig = inspect.signature(iec61131::fbd::Fbd::Network.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::ld::rung_is_not_abstract():
    assert not inspect.isabstract(iec61131::ld::Rung)


def test_iec61131::ld::rung_constructor_exists():
    assert callable(iec61131::ld::Rung.__init__)


def test_iec61131::ld::rung_constructor_args():
    sig = inspect.signature(iec61131::ld::Rung.__init__)
    params = list(sig.parameters.keys())



def test_steps_is_not_abstract():
    assert not inspect.isabstract(Steps)


def test_steps_constructor_exists():
    assert callable(Steps.__init__)


def test_steps_constructor_args():
    sig = inspect.signature(Steps.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::sfc::steps1_is_not_abstract():
    assert not inspect.isabstract(iec61131::sfc::Steps1)


def test_iec61131::sfc::steps1_constructor_exists():
    assert callable(iec61131::sfc::Steps1.__init__)


def test_iec61131::sfc::steps1_constructor_args():
    sig = inspect.signature(iec61131::sfc::Steps1.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::sfc::steps2_is_not_abstract():
    assert not inspect.isabstract(iec61131::sfc::Steps2)


def test_iec61131::sfc::steps2_constructor_exists():
    assert callable(iec61131::sfc::Steps2.__init__)


def test_iec61131::sfc::steps2_constructor_args():
    sig = inspect.signature(iec61131::sfc::Steps2.__init__)
    params = list(sig.parameters.keys())



def test_transition::name_is_not_abstract():
    assert not inspect.isabstract(Transition::Name)


def test_transition::name_constructor_exists():
    assert callable(Transition::Name.__init__)


def test_transition::name_constructor_args():
    sig = inspect.signature(Transition::Name.__init__)
    params = list(sig.parameters.keys())



def test_sfc::step::types_is_not_abstract():
    assert not inspect.isabstract(sfc::Step::Types)


def test_sfc::step::types_constructor_exists():
    assert callable(sfc::Step::Types.__init__)


def test_sfc::step::types_constructor_args():
    sig = inspect.signature(sfc::Step::Types.__init__)
    params = list(sig.parameters.keys())



def test_sfc::sfc::elements_is_not_abstract():
    assert not inspect.isabstract(sfc::Sfc::Elements)


def test_sfc::sfc::elements_constructor_exists():
    assert callable(sfc::Sfc::Elements.__init__)


def test_sfc::sfc::elements_constructor_args():
    sig = inspect.signature(sfc::Sfc::Elements.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::sfc::step_is_not_abstract():
    assert not inspect.isabstract(iec61131::sfc::Step)


def test_iec61131::sfc::step_constructor_exists():
    assert callable(iec61131::sfc::Step.__init__)


def test_iec61131::sfc::step_constructor_args():
    sig = inspect.signature(iec61131::sfc::Step.__init__)
    params = list(sig.parameters.keys())



def test_step::types_is_not_abstract():
    assert not inspect.isabstract(Step::Types)


def test_step::types_constructor_exists():
    assert callable(Step::Types.__init__)


def test_step::types_constructor_args():
    sig = inspect.signature(Step::Types.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::sfc::initial::step_is_not_abstract():
    assert not inspect.isabstract(iec61131::sfc::Initial::Step)


def test_iec61131::sfc::initial::step_constructor_exists():
    assert callable(iec61131::sfc::Initial::Step.__init__)


def test_iec61131::sfc::initial::step_constructor_args():
    sig = inspect.signature(iec61131::sfc::Initial::Step.__init__)
    params = list(sig.parameters.keys())



def test_sfc::elements_is_not_abstract():
    assert not inspect.isabstract(Sfc::Elements)


def test_sfc::elements_constructor_exists():
    assert callable(Sfc::Elements.__init__)


def test_sfc::elements_constructor_args():
    sig = inspect.signature(Sfc::Elements.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::sfc::transition_is_not_abstract():
    assert not inspect.isabstract(iec61131::sfc::Transition)


def test_iec61131::sfc::transition_constructor_exists():
    assert callable(iec61131::sfc::Transition.__init__)


def test_iec61131::sfc::transition_constructor_args():
    sig = inspect.signature(iec61131::sfc::Transition.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::sfc::action_is_not_abstract():
    assert not inspect.isabstract(iec61131::sfc::Action)


def test_iec61131::sfc::action_constructor_exists():
    assert callable(iec61131::sfc::Action.__init__)


def test_iec61131::sfc::action_constructor_args():
    sig = inspect.signature(iec61131::sfc::Action.__init__)
    params = list(sig.parameters.keys())



def test_initial::step_is_not_abstract():
    assert not inspect.isabstract(Initial::Step)


def test_initial::step_constructor_exists():
    assert callable(Initial::Step.__init__)


def test_initial::step_constructor_args():
    sig = inspect.signature(Initial::Step.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::sfc::timed::qualifier_is_not_abstract():
    assert not inspect.isabstract(iec61131::sfc::Timed::Qualifier)


def test_iec61131::sfc::timed::qualifier_constructor_exists():
    assert callable(iec61131::sfc::Timed::Qualifier.__init__)


def test_iec61131::sfc::timed::qualifier_constructor_args():
    sig = inspect.signature(iec61131::sfc::Timed::Qualifier.__init__)
    params = list(sig.parameters.keys())
    assert "qualifier" in params, "Missing parameter 'qualifier'"

def test_iec61131::sfc::timed::qualifier_has_qualifier():
    assert hasattr(iec61131::sfc::Timed::Qualifier, "qualifier")
    descriptor = None
    for klass in iec61131::sfc::Timed::Qualifier.__mro__:
        if "qualifier" in klass.__dict__:
            descriptor = klass.__dict__["qualifier"]
            break
    assert isinstance(descriptor, property)



def test_action::time_is_not_abstract():
    assert not inspect.isabstract(Action::Time)


def test_action::time_constructor_exists():
    assert callable(Action::Time.__init__)


def test_action::time_constructor_args():
    sig = inspect.signature(Action::Time.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::sfc::actiontime2_is_not_abstract():
    assert not inspect.isabstract(iec61131::sfc::ActionTime2)


def test_iec61131::sfc::actiontime2_constructor_exists():
    assert callable(iec61131::sfc::ActionTime2.__init__)


def test_iec61131::sfc::actiontime2_constructor_args():
    sig = inspect.signature(iec61131::sfc::ActionTime2.__init__)
    params = list(sig.parameters.keys())



def test_timed::qualifier_is_not_abstract():
    assert not inspect.isabstract(Timed::Qualifier)


def test_timed::qualifier_constructor_exists():
    assert callable(Timed::Qualifier.__init__)


def test_timed::qualifier_constructor_args():
    sig = inspect.signature(Timed::Qualifier.__init__)
    params = list(sig.parameters.keys())



def test_variable::name_is_not_abstract():
    assert not inspect.isabstract(Variable::Name)


def test_variable::name_constructor_exists():
    assert callable(Variable::Name.__init__)


def test_variable::name_constructor_args():
    sig = inspect.signature(Variable::Name.__init__)
    params = list(sig.parameters.keys())



def test_location_is_not_abstract():
    assert not inspect.isabstract(Location)


def test_location_constructor_exists():
    assert callable(Location.__init__)


def test_location_constructor_args():
    sig = inspect.signature(Location.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::located::var::decl_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Located::Var::Decl)


def test_iec61131::interfaces::located::var::decl_constructor_exists():
    assert callable(iec61131::interfaces::Located::Var::Decl.__init__)


def test_iec61131::interfaces::located::var::decl_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Located::Var::Decl.__init__)
    params = list(sig.parameters.keys())



def test_direct::variable_is_not_abstract():
    assert not inspect.isabstract(Direct::Variable)


def test_direct::variable_constructor_exists():
    assert callable(Direct::Variable.__init__)


def test_direct::variable_constructor_args():
    sig = inspect.signature(Direct::Variable.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::location_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Location)


def test_iec61131::interfaces::location_constructor_exists():
    assert callable(iec61131::interfaces::Location.__init__)


def test_iec61131::interfaces::location_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Location.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::located::var::spec::init_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Located::Var::Spec::Init)


def test_iec61131::interfaces::located::var::spec::init_constructor_exists():
    assert callable(iec61131::interfaces::Located::Var::Spec::Init.__init__)


def test_iec61131::interfaces::located::var::spec::init_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Located::Var::Spec::Init.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::external::specification_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::External::Specification)


def test_iec61131::interfaces::external::specification_constructor_exists():
    assert callable(iec61131::interfaces::External::Specification.__init__)


def test_iec61131::interfaces::external::specification_constructor_args():
    sig = inspect.signature(iec61131::interfaces::External::Specification.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::var::spec_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Var::Spec)


def test_iec61131::interfaces::var::spec_constructor_exists():
    assert callable(iec61131::interfaces::Var::Spec.__init__)


def test_iec61131::interfaces::var::spec_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Var::Spec.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::incompl::location_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Incompl::Location)


def test_iec61131::interfaces::incompl::location_constructor_exists():
    assert callable(iec61131::interfaces::Incompl::Location.__init__)


def test_iec61131::interfaces::incompl::location_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Incompl::Location.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_iec61131::interfaces::incompl::location_has_location():
    assert hasattr(iec61131::interfaces::Incompl::Location, "location")
    descriptor = None
    for klass in iec61131::interfaces::Incompl::Location.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_var::spec_is_not_abstract():
    assert not inspect.isabstract(Var::Spec)


def test_var::spec_constructor_exists():
    assert callable(Var::Spec.__init__)


def test_var::spec_constructor_args():
    sig = inspect.signature(Var::Spec.__init__)
    params = list(sig.parameters.keys())



def test_incompl::location_is_not_abstract():
    assert not inspect.isabstract(Incompl::Location)


def test_incompl::location_constructor_exists():
    assert callable(Incompl::Location.__init__)


def test_incompl::location_constructor_args():
    sig = inspect.signature(Incompl::Location.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::incompl::located::var::decl_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Incompl::Located::Var::Decl)


def test_iec61131::interfaces::incompl::located::var::decl_constructor_exists():
    assert callable(iec61131::interfaces::Incompl::Located::Var::Decl.__init__)


def test_iec61131::interfaces::incompl::located::var::decl_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Incompl::Located::Var::Decl.__init__)
    params = list(sig.parameters.keys())



def test_incompl::located::var::decl_is_not_abstract():
    assert not inspect.isabstract(Incompl::Located::Var::Decl)


def test_incompl::located::var::decl_constructor_exists():
    assert callable(Incompl::Located::Var::Decl.__init__)


def test_incompl::located::var::decl_constructor_args():
    sig = inspect.signature(Incompl::Located::Var::Decl.__init__)
    params = list(sig.parameters.keys())



def test_temp::var::decl_is_not_abstract():
    assert not inspect.isabstract(Temp::Var::Decl)


def test_temp::var::decl_constructor_exists():
    assert callable(Temp::Var::Decl.__init__)


def test_temp::var::decl_constructor_args():
    sig = inspect.signature(Temp::Var::Decl.__init__)
    params = list(sig.parameters.keys())



def test_global::var::spec_is_not_abstract():
    assert not inspect.isabstract(Global::Var::Spec)


def test_global::var::spec_constructor_exists():
    assert callable(Global::Var::Spec.__init__)


def test_global::var::spec_constructor_args():
    sig = inspect.signature(Global::Var::Spec.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::global::var::list_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Global::Var::List)


def test_iec61131::interfaces::global::var::list_constructor_exists():
    assert callable(iec61131::interfaces::Global::Var::List.__init__)


def test_iec61131::interfaces::global::var::list_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Global::Var::List.__init__)
    params = list(sig.parameters.keys())



def test_library::element::name_is_not_abstract():
    assert not inspect.isabstract(Library::Element::Name)


def test_library::element::name_constructor_exists():
    assert callable(Library::Element::Name.__init__)


def test_library::element::name_constructor_args():
    sig = inspect.signature(Library::Element::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::data::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::Data::Type::Name)


def test_iec61131::types::data::type::name_constructor_exists():
    assert callable(iec61131::types::Data::Type::Name.__init__)


def test_iec61131::types::data::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::Data::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::specification_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Specification)


def test_iec61131::interfaces::specification_constructor_exists():
    assert callable(iec61131::interfaces::Specification.__init__)


def test_iec61131::interfaces::specification_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Specification.__init__)
    params = list(sig.parameters.keys())



def test_specification_is_not_abstract():
    assert not inspect.isabstract(Specification)


def test_specification_constructor_exists():
    assert callable(Specification.__init__)


def test_specification_constructor_args():
    sig = inspect.signature(Specification.__init__)
    params = list(sig.parameters.keys())



def test_array::initial::elements_is_not_abstract():
    assert not inspect.isabstract(Array::Initial::Elements)


def test_array::initial::elements_constructor_exists():
    assert callable(Array::Initial::Elements.__init__)


def test_array::initial::elements_constructor_args():
    sig = inspect.signature(Array::Initial::Elements.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::array::initialization_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Array::Initialization)


def test_iec61131::interfaces::array::initialization_constructor_exists():
    assert callable(iec61131::interfaces::Array::Initialization.__init__)


def test_iec61131::interfaces::array::initialization_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Array::Initialization.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::var1::list_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Var1::List)


def test_iec61131::interfaces::var1::list_constructor_exists():
    assert callable(iec61131::interfaces::Var1::List.__init__)


def test_iec61131::interfaces::var1::list_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Var1::List.__init__)
    params = list(sig.parameters.keys())



def test_double::bstring_is_not_abstract():
    assert not inspect.isabstract(Double::BString)


def test_double::bstring_constructor_exists():
    assert callable(Double::BString.__init__)


def test_double::bstring_constructor_args():
    sig = inspect.signature(Double::BString.__init__)
    params = list(sig.parameters.keys())



def test_double::byte::character::string_is_not_abstract():
    assert not inspect.isabstract(Double::Byte::Character::String)


def test_double::byte::character::string_constructor_exists():
    assert callable(Double::Byte::Character::String.__init__)


def test_double::byte::character::string_constructor_args():
    sig = inspect.signature(Double::Byte::Character::String.__init__)
    params = list(sig.parameters.keys())



def test_single::bstring_is_not_abstract():
    assert not inspect.isabstract(Single::BString)


def test_single::bstring_constructor_exists():
    assert callable(Single::BString.__init__)


def test_single::bstring_constructor_args():
    sig = inspect.signature(Single::BString.__init__)
    params = list(sig.parameters.keys())



def test_single::byte::character::string_is_not_abstract():
    assert not inspect.isabstract(Single::Byte::Character::String)


def test_single::byte::character::string_constructor_exists():
    assert callable(Single::Byte::Character::String.__init__)


def test_single::byte::character::string_constructor_args():
    sig = inspect.signature(Single::Byte::Character::String.__init__)
    params = list(sig.parameters.keys())



def test_located::var::spec::init_is_not_abstract():
    assert not inspect.isabstract(Located::Var::Spec::Init)


def test_located::var::spec::init_constructor_exists():
    assert callable(Located::Var::Spec::Init.__init__)


def test_located::var::spec::init_constructor_args():
    sig = inspect.signature(Located::Var::Spec::Init.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::double::byte::string::spec_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Double::Byte::String::Spec)


def test_iec61131::interfaces::double::byte::string::spec_constructor_exists():
    assert callable(iec61131::interfaces::Double::Byte::String::Spec.__init__)


def test_iec61131::interfaces::double::byte::string::spec_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Double::Byte::String::Spec.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::single::byte::string::spec_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Single::Byte::String::Spec)


def test_iec61131::interfaces::single::byte::string::spec_constructor_exists():
    assert callable(iec61131::interfaces::Single::Byte::String::Spec.__init__)


def test_iec61131::interfaces::single::byte::string::spec_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Single::Byte::String::Spec.__init__)
    params = list(sig.parameters.keys())



def test_double::byte::string::spec_is_not_abstract():
    assert not inspect.isabstract(Double::Byte::String::Spec)


def test_double::byte::string::spec_constructor_exists():
    assert callable(Double::Byte::String::Spec.__init__)


def test_double::byte::string::spec_constructor_args():
    sig = inspect.signature(Double::Byte::String::Spec.__init__)
    params = list(sig.parameters.keys())



def test_single::byte::string::spec_is_not_abstract():
    assert not inspect.isabstract(Single::Byte::String::Spec)


def test_single::byte::string::spec_constructor_exists():
    assert callable(Single::Byte::String::Spec.__init__)


def test_single::byte::string::spec_constructor_args():
    sig = inspect.signature(Single::Byte::String::Spec.__init__)
    params = list(sig.parameters.keys())



def test_string::var::declaration_is_not_abstract():
    assert not inspect.isabstract(String::Var::Declaration)


def test_string::var::declaration_constructor_exists():
    assert callable(String::Var::Declaration.__init__)


def test_string::var::declaration_constructor_args():
    sig = inspect.signature(String::Var::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::double::byte::string::var::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Double::Byte::String::Var::Declaration)


def test_iec61131::interfaces::double::byte::string::var::declaration_constructor_exists():
    assert callable(iec61131::interfaces::Double::Byte::String::Var::Declaration.__init__)


def test_iec61131::interfaces::double::byte::string::var::declaration_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Double::Byte::String::Var::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::single::byte::string::var::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Single::Byte::String::Var::Declaration)


def test_iec61131::interfaces::single::byte::string::var::declaration_constructor_exists():
    assert callable(iec61131::interfaces::Single::Byte::String::Var::Declaration.__init__)


def test_iec61131::interfaces::single::byte::string::var::declaration_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Single::Byte::String::Var::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_range_is_not_abstract():
    assert not inspect.isabstract(Range)


def test_range_constructor_exists():
    assert callable(Range.__init__)


def test_range_constructor_args():
    sig = inspect.signature(Range.__init__)
    params = list(sig.parameters.keys())



def test_case::list::element_is_not_abstract():
    assert not inspect.isabstract(Case::List::Element)


def test_case::list::element_constructor_exists():
    assert callable(Case::List::Element.__init__)


def test_case::list::element_constructor_args():
    sig = inspect.signature(Case::List::Element.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::subrange_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Subrange)


def test_iec61131::interfaces::subrange_constructor_exists():
    assert callable(iec61131::interfaces::Subrange.__init__)


def test_iec61131::interfaces::subrange_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Subrange.__init__)
    params = list(sig.parameters.keys())
    assert "delimiter" in params, "Missing parameter 'delimiter'"

def test_iec61131::interfaces::subrange_has_delimiter():
    assert hasattr(iec61131::interfaces::Subrange, "delimiter")
    descriptor = None
    for klass in iec61131::interfaces::Subrange.__mro__:
        if "delimiter" in klass.__dict__:
            descriptor = klass.__dict__["delimiter"]
            break
    assert isinstance(descriptor, property)



def test_iec61131::interfaces::array::initial::elements_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Array::Initial::Elements)


def test_iec61131::interfaces::array::initial::elements_constructor_exists():
    assert callable(iec61131::interfaces::Array::Initial::Elements.__init__)


def test_iec61131::interfaces::array::initial::elements_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Array::Initial::Elements.__init__)
    params = list(sig.parameters.keys())



def test_interfaces::var::spec_is_not_abstract():
    assert not inspect.isabstract(interfaces::Var::Spec)


def test_interfaces::var::spec_constructor_exists():
    assert callable(interfaces::Var::Spec.__init__)


def test_interfaces::var::spec_constructor_args():
    sig = inspect.signature(interfaces::Var::Spec.__init__)
    params = list(sig.parameters.keys())



def test_interfaces::external::specification_is_not_abstract():
    assert not inspect.isabstract(interfaces::External::Specification)


def test_interfaces::external::specification_constructor_exists():
    assert callable(interfaces::External::Specification.__init__)


def test_interfaces::external::specification_constructor_args():
    sig = inspect.signature(interfaces::External::Specification.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::array::specification_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Array::Specification)


def test_iec61131::interfaces::array::specification_constructor_exists():
    assert callable(iec61131::interfaces::Array::Specification.__init__)


def test_iec61131::interfaces::array::specification_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Array::Specification.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::structure::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::Structure::Type::Name)


def test_iec61131::types::structure::type::name_constructor_exists():
    assert callable(iec61131::types::Structure::Type::Name.__init__)


def test_iec61131::types::structure::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::Structure::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_interfaces::specification_is_not_abstract():
    assert not inspect.isabstract(interfaces::Specification)


def test_interfaces::specification_constructor_exists():
    assert callable(interfaces::Specification.__init__)


def test_interfaces::specification_constructor_args():
    sig = inspect.signature(interfaces::Specification.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::enumerated::specification_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Enumerated::Specification)


def test_iec61131::interfaces::enumerated::specification_constructor_exists():
    assert callable(iec61131::interfaces::Enumerated::Specification.__init__)


def test_iec61131::interfaces::enumerated::specification_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Enumerated::Specification.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::subrange::specification_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Subrange::Specification)


def test_iec61131::interfaces::subrange::specification_constructor_exists():
    assert callable(iec61131::interfaces::Subrange::Specification.__init__)


def test_iec61131::interfaces::subrange::specification_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Subrange::Specification.__init__)
    params = list(sig.parameters.keys())



def test_interfaces::var2::init::decl_is_not_abstract():
    assert not inspect.isabstract(interfaces::Var2::Init::Decl)


def test_interfaces::var2::init::decl_constructor_exists():
    assert callable(interfaces::Var2::Init::Decl.__init__)


def test_interfaces::var2::init::decl_constructor_args():
    sig = inspect.signature(interfaces::Var2::Init::Decl.__init__)
    params = list(sig.parameters.keys())



def test_interfaces::temp::var::decl_is_not_abstract():
    assert not inspect.isabstract(interfaces::Temp::Var::Decl)


def test_interfaces::temp::var::decl_constructor_exists():
    assert callable(interfaces::Temp::Var::Decl.__init__)


def test_interfaces::temp::var::decl_constructor_args():
    sig = inspect.signature(interfaces::Temp::Var::Decl.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::string::var::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::String::Var::Declaration)


def test_iec61131::interfaces::string::var::declaration_constructor_exists():
    assert callable(iec61131::interfaces::String::Var::Declaration.__init__)


def test_iec61131::interfaces::string::var::declaration_constructor_args():
    sig = inspect.signature(iec61131::interfaces::String::Var::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_function::block::type::name_is_not_abstract():
    assert not inspect.isabstract(Function::Block::Type::Name)


def test_function::block::type::name_constructor_exists():
    assert callable(Function::Block::Type::Name.__init__)


def test_function::block::type::name_constructor_args():
    sig = inspect.signature(Function::Block::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_structure::initialization_is_not_abstract():
    assert not inspect.isabstract(Structure::Initialization)


def test_structure::initialization_constructor_exists():
    assert callable(Structure::Initialization.__init__)


def test_structure::initialization_constructor_args():
    sig = inspect.signature(Structure::Initialization.__init__)
    params = list(sig.parameters.keys())



def test_temp::var::declaration_is_not_abstract():
    assert not inspect.isabstract(Temp::Var::Declaration)


def test_temp::var::declaration_constructor_exists():
    assert callable(Temp::Var::Declaration.__init__)


def test_temp::var::declaration_constructor_args():
    sig = inspect.signature(Temp::Var::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::array::var::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Array::Var::Declaration)


def test_iec61131::interfaces::array::var::declaration_constructor_exists():
    assert callable(iec61131::interfaces::Array::Var::Declaration.__init__)


def test_iec61131::interfaces::array::var::declaration_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Array::Var::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::structured::var::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Structured::Var::Declaration)


def test_iec61131::interfaces::structured::var::declaration_constructor_exists():
    assert callable(iec61131::interfaces::Structured::Var::Declaration.__init__)


def test_iec61131::interfaces::structured::var::declaration_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Structured::Var::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::var1::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Var1::Declaration)


def test_iec61131::interfaces::var1::declaration_constructor_exists():
    assert callable(iec61131::interfaces::Var1::Declaration.__init__)


def test_iec61131::interfaces::var1::declaration_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Var1::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::fb::name::decl_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Fb::Name::Decl)


def test_iec61131::interfaces::fb::name::decl_constructor_exists():
    assert callable(iec61131::interfaces::Fb::Name::Decl.__init__)


def test_iec61131::interfaces::fb::name::decl_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Fb::Name::Decl.__init__)
    params = list(sig.parameters.keys())



def test_enumerated::type::name_is_not_abstract():
    assert not inspect.isabstract(Enumerated::Type::Name)


def test_enumerated::type::name_constructor_exists():
    assert callable(Enumerated::Type::Name.__init__)


def test_enumerated::type::name_constructor_args():
    sig = inspect.signature(Enumerated::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::structure::element::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Structure::Element::Name)


def test_iec61131::interfaces::structure::element::name_constructor_exists():
    assert callable(iec61131::interfaces::Structure::Element::Name.__init__)


def test_iec61131::interfaces::structure::element::name_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Structure::Element::Name.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iec61131::interfaces::structure::element::name_has_name():
    assert hasattr(iec61131::interfaces::Structure::Element::Name, "name")
    descriptor = None
    for klass in iec61131::interfaces::Structure::Element::Name.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_initial::element_is_not_abstract():
    assert not inspect.isabstract(Initial::Element)


def test_initial::element_constructor_exists():
    assert callable(Initial::Element.__init__)


def test_initial::element_constructor_args():
    sig = inspect.signature(Initial::Element.__init__)
    params = list(sig.parameters.keys())



def test_structure::element::name_is_not_abstract():
    assert not inspect.isabstract(Structure::Element::Name)


def test_structure::element::name_constructor_exists():
    assert callable(Structure::Element::Name.__init__)


def test_structure::element::name_constructor_args():
    sig = inspect.signature(Structure::Element::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::structure::element::initialization_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Structure::Element::Initialization)


def test_iec61131::interfaces::structure::element::initialization_constructor_exists():
    assert callable(iec61131::interfaces::Structure::Element::Initialization.__init__)


def test_iec61131::interfaces::structure::element::initialization_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Structure::Element::Initialization.__init__)
    params = list(sig.parameters.keys())



def test_structure::element::initialization_is_not_abstract():
    assert not inspect.isabstract(Structure::Element::Initialization)


def test_structure::element::initialization_constructor_exists():
    assert callable(Structure::Element::Initialization.__init__)


def test_structure::element::initialization_constructor_args():
    sig = inspect.signature(Structure::Element::Initialization.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::structure::initialization_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Structure::Initialization)


def test_iec61131::interfaces::structure::initialization_constructor_exists():
    assert callable(iec61131::interfaces::Structure::Initialization.__init__)


def test_iec61131::interfaces::structure::initialization_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Structure::Initialization.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::var::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Var::Declaration)


def test_iec61131::interfaces::var::declaration_constructor_exists():
    assert callable(iec61131::interfaces::Var::Declaration.__init__)


def test_iec61131::interfaces::var::declaration_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Var::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_structure::type::name_is_not_abstract():
    assert not inspect.isabstract(Structure::Type::Name)


def test_structure::type::name_constructor_exists():
    assert callable(Structure::Type::Name.__init__)


def test_structure::type::name_constructor_args():
    sig = inspect.signature(Structure::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_pous::structure::specification_is_not_abstract():
    assert not inspect.isabstract(pous::Structure::Specification)


def test_pous::structure::specification_constructor_exists():
    assert callable(pous::Structure::Specification.__init__)


def test_pous::structure::specification_constructor_args():
    sig = inspect.signature(pous::Structure::Specification.__init__)
    params = list(sig.parameters.keys())



def test_array::specification_is_not_abstract():
    assert not inspect.isabstract(Array::Specification)


def test_array::specification_constructor_exists():
    assert callable(Array::Specification.__init__)


def test_array::specification_constructor_args():
    sig = inspect.signature(Array::Specification.__init__)
    params = list(sig.parameters.keys())



def test_array::initialization_is_not_abstract():
    assert not inspect.isabstract(Array::Initialization)


def test_array::initialization_constructor_exists():
    assert callable(Array::Initialization.__init__)


def test_array::initialization_constructor_args():
    sig = inspect.signature(Array::Initialization.__init__)
    params = list(sig.parameters.keys())



def test_var::declaration_is_not_abstract():
    assert not inspect.isabstract(Var::Declaration)


def test_var::declaration_constructor_exists():
    assert callable(Var::Declaration.__init__)


def test_var::declaration_constructor_args():
    sig = inspect.signature(Var::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::temp::var::decl_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Temp::Var::Decl)


def test_iec61131::interfaces::temp::var::decl_constructor_exists():
    assert callable(iec61131::interfaces::Temp::Var::Decl.__init__)


def test_iec61131::interfaces::temp::var::decl_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Temp::Var::Decl.__init__)
    params = list(sig.parameters.keys())



def test_var1::specification_is_not_abstract():
    assert not inspect.isabstract(Var1::Specification)


def test_var1::specification_constructor_exists():
    assert callable(Var1::Specification.__init__)


def test_var1::specification_constructor_args():
    sig = inspect.signature(Var1::Specification.__init__)
    params = list(sig.parameters.keys())



def test_var::init::decl_is_not_abstract():
    assert not inspect.isabstract(Var::Init::Decl)


def test_var::init::decl_constructor_exists():
    assert callable(Var::Init::Decl.__init__)


def test_var::init::decl_constructor_args():
    sig = inspect.signature(Var::Init::Decl.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::var1::init::decl_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Var1::Init::Decl)


def test_iec61131::interfaces::var1::init::decl_constructor_exists():
    assert callable(iec61131::interfaces::Var1::Init::Decl.__init__)


def test_iec61131::interfaces::var1::init::decl_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Var1::Init::Decl.__init__)
    params = list(sig.parameters.keys())



def test_var1::list_is_not_abstract():
    assert not inspect.isabstract(Var1::List)


def test_var1::list_constructor_exists():
    assert callable(Var1::List.__init__)


def test_var1::list_constructor_args():
    sig = inspect.signature(Var1::List.__init__)
    params = list(sig.parameters.keys())



def test_input::declaration_is_not_abstract():
    assert not inspect.isabstract(Input::Declaration)


def test_input::declaration_constructor_exists():
    assert callable(Input::Declaration.__init__)


def test_input::declaration_constructor_args():
    sig = inspect.signature(Input::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::var::init::decl_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Var::Init::Decl)


def test_iec61131::interfaces::var::init::decl_constructor_exists():
    assert callable(iec61131::interfaces::Var::Init::Decl.__init__)


def test_iec61131::interfaces::var::init::decl_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Var::Init::Decl.__init__)
    params = list(sig.parameters.keys())



def test_io::var::declaration_is_not_abstract():
    assert not inspect.isabstract(Io::Var::Declaration)


def test_io::var::declaration_constructor_exists():
    assert callable(Io::Var::Declaration.__init__)


def test_io::var::declaration_constructor_args():
    sig = inspect.signature(Io::Var::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::output::declarations_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Output::Declarations)


def test_iec61131::interfaces::output::declarations_constructor_exists():
    assert callable(iec61131::interfaces::Output::Declarations.__init__)


def test_iec61131::interfaces::output::declarations_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Output::Declarations.__init__)
    params = list(sig.parameters.keys())
    assert "retain" in params, "Missing parameter 'retain'"

def test_iec61131::interfaces::output::declarations_has_retain():
    assert hasattr(iec61131::interfaces::Output::Declarations, "retain")
    descriptor = None
    for klass in iec61131::interfaces::Output::Declarations.__mro__:
        if "retain" in klass.__dict__:
            descriptor = klass.__dict__["retain"]
            break
    assert isinstance(descriptor, property)



def test_iec61131::interfaces::input::output::declarations_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Input::Output::Declarations)


def test_iec61131::interfaces::input::output::declarations_constructor_exists():
    assert callable(iec61131::interfaces::Input::Output::Declarations.__init__)


def test_iec61131::interfaces::input::output::declarations_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Input::Output::Declarations.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::input::declarations_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Input::Declarations)


def test_iec61131::interfaces::input::declarations_constructor_exists():
    assert callable(iec61131::interfaces::Input::Declarations.__init__)


def test_iec61131::interfaces::input::declarations_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Input::Declarations.__init__)
    params = list(sig.parameters.keys())
    assert "retain" in params, "Missing parameter 'retain'"

def test_iec61131::interfaces::input::declarations_has_retain():
    assert hasattr(iec61131::interfaces::Input::Declarations, "retain")
    descriptor = None
    for klass in iec61131::interfaces::Input::Declarations.__mro__:
        if "retain" in klass.__dict__:
            descriptor = klass.__dict__["retain"]
            break
    assert isinstance(descriptor, property)



def test_pous::function::vars_is_not_abstract():
    assert not inspect.isabstract(pous::Function::Vars)


def test_pous::function::vars_constructor_exists():
    assert callable(pous::Function::Vars.__init__)


def test_pous::function::vars_constructor_args():
    sig = inspect.signature(pous::Function::Vars.__init__)
    params = list(sig.parameters.keys())



def test_pous::program::vars_is_not_abstract():
    assert not inspect.isabstract(pous::Program::Vars)


def test_pous::program::vars_constructor_exists():
    assert callable(pous::Program::Vars.__init__)


def test_pous::program::vars_constructor_args():
    sig = inspect.signature(pous::Program::Vars.__init__)
    params = list(sig.parameters.keys())



def test_pous::function::block::vars_is_not_abstract():
    assert not inspect.isabstract(pous::Function::Block::Vars)


def test_pous::function::block::vars_constructor_exists():
    assert callable(pous::Function::Block::Vars.__init__)


def test_pous::function::block::vars_constructor_args():
    sig = inspect.signature(pous::Function::Block::Vars.__init__)
    params = list(sig.parameters.keys())



def test_interfaces::interface_is_not_abstract():
    assert not inspect.isabstract(interfaces::Interface)


def test_interfaces::interface_constructor_exists():
    assert callable(interfaces::Interface.__init__)


def test_interfaces::interface_constructor_args():
    sig = inspect.signature(interfaces::Interface.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::other::var::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Other::Var::Declaration)


def test_iec61131::interfaces::other::var::declaration_constructor_exists():
    assert callable(iec61131::interfaces::Other::Var::Declaration.__init__)


def test_iec61131::interfaces::other::var::declaration_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Other::Var::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::io::var::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Io::Var::Declaration)


def test_iec61131::interfaces::io::var::declaration_constructor_exists():
    assert callable(iec61131::interfaces::Io::Var::Declaration.__init__)


def test_iec61131::interfaces::io::var::declaration_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Io::Var::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_initialized::structure_is_not_abstract():
    assert not inspect.isabstract(Initialized::Structure)


def test_initialized::structure_constructor_exists():
    assert callable(Initialized::Structure.__init__)


def test_initialized::structure_constructor_args():
    sig = inspect.signature(Initialized::Structure.__init__)
    params = list(sig.parameters.keys())



def test_array::spec::init_is_not_abstract():
    assert not inspect.isabstract(Array::Spec::Init)


def test_array::spec::init_constructor_exists():
    assert callable(Array::Spec::Init.__init__)


def test_array::spec::init_constructor_args():
    sig = inspect.signature(Array::Spec::Init.__init__)
    params = list(sig.parameters.keys())



def test_var2::init::decl_is_not_abstract():
    assert not inspect.isabstract(Var2::Init::Decl)


def test_var2::init::decl_constructor_exists():
    assert callable(Var2::Init::Decl.__init__)


def test_var2::init::decl_constructor_args():
    sig = inspect.signature(Var2::Init::Decl.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::structured::var::init::decl_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Structured::Var::Init::Decl)


def test_iec61131::interfaces::structured::var::init::decl_constructor_exists():
    assert callable(iec61131::interfaces::Structured::Var::Init::Decl.__init__)


def test_iec61131::interfaces::structured::var::init::decl_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Structured::Var::Init::Decl.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::array::var::init::decl_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Array::Var::Init::Decl)


def test_iec61131::interfaces::array::var::init::decl_constructor_exists():
    assert callable(iec61131::interfaces::Array::Var::Init::Decl.__init__)


def test_iec61131::interfaces::array::var::init::decl_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Array::Var::Init::Decl.__init__)
    params = list(sig.parameters.keys())



def test_enumerated::value_is_not_abstract():
    assert not inspect.isabstract(Enumerated::Value)


def test_enumerated::value_constructor_exists():
    assert callable(Enumerated::Value.__init__)


def test_enumerated::value_constructor_args():
    sig = inspect.signature(Enumerated::Value.__init__)
    params = list(sig.parameters.keys())



def test_enumerated::specification_is_not_abstract():
    assert not inspect.isabstract(Enumerated::Specification)


def test_enumerated::specification_constructor_exists():
    assert callable(Enumerated::Specification.__init__)


def test_enumerated::specification_constructor_args():
    sig = inspect.signature(Enumerated::Specification.__init__)
    params = list(sig.parameters.keys())



def test_signed::integer_is_not_abstract():
    assert not inspect.isabstract(Signed::Integer)


def test_signed::integer_constructor_exists():
    assert callable(Signed::Integer.__init__)


def test_signed::integer_constructor_args():
    sig = inspect.signature(Signed::Integer.__init__)
    params = list(sig.parameters.keys())



def test_subrange::specification_is_not_abstract():
    assert not inspect.isabstract(Subrange::Specification)


def test_subrange::specification_constructor_exists():
    assert callable(Subrange::Specification.__init__)


def test_subrange::specification_constructor_args():
    sig = inspect.signature(Subrange::Specification.__init__)
    params = list(sig.parameters.keys())



def test_interfaces::var1::specification::func_is_not_abstract():
    assert not inspect.isabstract(interfaces::Var1::Specification::Func)


def test_interfaces::var1::specification::func_constructor_exists():
    assert callable(interfaces::Var1::Specification::Func.__init__)


def test_interfaces::var1::specification::func_constructor_args():
    sig = inspect.signature(interfaces::Var1::Specification::Func.__init__)
    params = list(sig.parameters.keys())



def test_simple::specification_is_not_abstract():
    assert not inspect.isabstract(Simple::Specification)


def test_simple::specification_constructor_exists():
    assert callable(Simple::Specification.__init__)


def test_simple::specification_constructor_args():
    sig = inspect.signature(Simple::Specification.__init__)
    params = list(sig.parameters.keys())



def test_pous::structure::elements_is_not_abstract():
    assert not inspect.isabstract(pous::Structure::Elements)


def test_pous::structure::elements_constructor_exists():
    assert callable(pous::Structure::Elements.__init__)


def test_pous::structure::elements_constructor_args():
    sig = inspect.signature(pous::Structure::Elements.__init__)
    params = list(sig.parameters.keys())



def test_interfaces::located::var::spec::init_is_not_abstract():
    assert not inspect.isabstract(interfaces::Located::Var::Spec::Init)


def test_interfaces::located::var::spec::init_constructor_exists():
    assert callable(interfaces::Located::Var::Spec::Init.__init__)


def test_interfaces::located::var::spec::init_constructor_args():
    sig = inspect.signature(interfaces::Located::Var::Spec::Init.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::initialized::structure_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Initialized::Structure)


def test_iec61131::interfaces::initialized::structure_constructor_exists():
    assert callable(iec61131::interfaces::Initialized::Structure.__init__)


def test_iec61131::interfaces::initialized::structure_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Initialized::Structure.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::array::spec::init_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Array::Spec::Init)


def test_iec61131::interfaces::array::spec::init_constructor_exists():
    assert callable(iec61131::interfaces::Array::Spec::Init.__init__)


def test_iec61131::interfaces::array::spec::init_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Array::Spec::Init.__init__)
    params = list(sig.parameters.keys())



def test_interfaces::var1::specification_is_not_abstract():
    assert not inspect.isabstract(interfaces::Var1::Specification)


def test_interfaces::var1::specification_constructor_exists():
    assert callable(interfaces::Var1::Specification.__init__)


def test_interfaces::var1::specification_constructor_args():
    sig = inspect.signature(interfaces::Var1::Specification.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::enumerated::spec::init_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Enumerated::Spec::Init)


def test_iec61131::interfaces::enumerated::spec::init_constructor_exists():
    assert callable(iec61131::interfaces::Enumerated::Spec::Init.__init__)


def test_iec61131::interfaces::enumerated::spec::init_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Enumerated::Spec::Init.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::subrange::spec::init_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Subrange::Spec::Init)


def test_iec61131::interfaces::subrange::spec::init_constructor_exists():
    assert callable(iec61131::interfaces::Subrange::Spec::Init.__init__)


def test_iec61131::interfaces::subrange::spec::init_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Subrange::Spec::Init.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::simple::spec::init_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Simple::Spec::Init)


def test_iec61131::interfaces::simple::spec::init_constructor_exists():
    assert callable(iec61131::interfaces::Simple::Spec::Init.__init__)


def test_iec61131::interfaces::simple::spec::init_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Simple::Spec::Init.__init__)
    params = list(sig.parameters.keys())



def test_assignment::symbol_is_not_abstract():
    assert not inspect.isabstract(Assignment::Symbol)


def test_assignment::symbol_constructor_exists():
    assert callable(Assignment::Symbol.__init__)


def test_assignment::symbol_constructor_args():
    sig = inspect.signature(Assignment::Symbol.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::var1::specification_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Var1::Specification)


def test_iec61131::interfaces::var1::specification_constructor_exists():
    assert callable(iec61131::interfaces::Var1::Specification.__init__)


def test_iec61131::interfaces::var1::specification_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Var1::Specification.__init__)
    params = list(sig.parameters.keys())



def test_bool::type::name_is_not_abstract():
    assert not inspect.isabstract(Bool::Type::Name)


def test_bool::type::name_constructor_exists():
    assert callable(Bool::Type::Name.__init__)


def test_bool::type::name_constructor_args():
    sig = inspect.signature(Bool::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::edge::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Edge::Declaration)


def test_iec61131::interfaces::edge::declaration_constructor_exists():
    assert callable(iec61131::interfaces::Edge::Declaration.__init__)


def test_iec61131::interfaces::edge::declaration_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Edge::Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "edge" in params, "Missing parameter 'edge'"

def test_iec61131::interfaces::edge::declaration_has_edge():
    assert hasattr(iec61131::interfaces::Edge::Declaration, "edge")
    descriptor = None
    for klass in iec61131::interfaces::Edge::Declaration.__mro__:
        if "edge" in klass.__dict__:
            descriptor = klass.__dict__["edge"]
            break
    assert isinstance(descriptor, property)



def test_operators::divide::operator_is_not_abstract():
    assert not inspect.isabstract(operators::Divide::Operator)


def test_operators::divide::operator_constructor_exists():
    assert callable(operators::Divide::Operator.__init__)


def test_operators::divide::operator_constructor_args():
    sig = inspect.signature(operators::Divide::Operator.__init__)
    params = list(sig.parameters.keys())



def test_multiply::operator_is_not_abstract():
    assert not inspect.isabstract(Multiply::Operator)


def test_multiply::operator_constructor_exists():
    assert callable(Multiply::Operator.__init__)


def test_multiply::operator_constructor_args():
    sig = inspect.signature(Multiply::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::multiply::symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Multiply::Symbol)


def test_iec61131::operators::multiply::symbol_constructor_exists():
    assert callable(iec61131::operators::Multiply::Symbol.__init__)


def test_iec61131::operators::multiply::symbol_constructor_args():
    sig = inspect.signature(iec61131::operators::Multiply::Symbol.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::else::if::statement_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Else::If::Statement)


def test_iec61131::st::else::if::statement_constructor_exists():
    assert callable(iec61131::st::Else::If::Statement.__init__)


def test_iec61131::st::else::if::statement_constructor_args():
    sig = inspect.signature(iec61131::st::Else::If::Statement.__init__)
    params = list(sig.parameters.keys())



def test_case::element_is_not_abstract():
    assert not inspect.isabstract(Case::Element)


def test_case::element_constructor_exists():
    assert callable(Case::Element.__init__)


def test_case::element_constructor_args():
    sig = inspect.signature(Case::Element.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::case::statement_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Case::Statement)


def test_iec61131::st::case::statement_constructor_exists():
    assert callable(iec61131::st::Case::Statement.__init__)


def test_iec61131::st::case::statement_constructor_args():
    sig = inspect.signature(iec61131::st::Case::Statement.__init__)
    params = list(sig.parameters.keys())



def test_else::statement_is_not_abstract():
    assert not inspect.isabstract(Else::Statement)


def test_else::statement_constructor_exists():
    assert callable(Else::Statement.__init__)


def test_else::statement_constructor_args():
    sig = inspect.signature(Else::Statement.__init__)
    params = list(sig.parameters.keys())



def test_else::if::statement_is_not_abstract():
    assert not inspect.isabstract(Else::If::Statement)


def test_else::if::statement_constructor_exists():
    assert callable(Else::If::Statement.__init__)


def test_else::if::statement_constructor_args():
    sig = inspect.signature(Else::If::Statement.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_param::assignment_is_not_abstract():
    assert not inspect.isabstract(Param::Assignment)


def test_param::assignment_constructor_exists():
    assert callable(Param::Assignment.__init__)


def test_param::assignment_constructor_args():
    sig = inspect.signature(Param::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::il::operand_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Il::Operand)


def test_iec61131::il::il::operand_constructor_exists():
    assert callable(iec61131::il::Il::Operand.__init__)


def test_iec61131::il::il::operand_constructor_args():
    sig = inspect.signature(iec61131::il::Il::Operand.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::param::type1_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Param::Type1)


def test_iec61131::st::param::type1_constructor_exists():
    assert callable(iec61131::st::Param::Type1.__init__)


def test_iec61131::st::param::type1_constructor_args():
    sig = inspect.signature(iec61131::st::Param::Type1.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::param::type2_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Param::Type2)


def test_iec61131::st::param::type2_constructor_exists():
    assert callable(iec61131::st::Param::Type2.__init__)


def test_iec61131::st::param::type2_constructor_args():
    sig = inspect.signature(iec61131::st::Param::Type2.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::param::assignment2_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Param::Assignment2)


def test_iec61131::il::param::assignment2_constructor_exists():
    assert callable(iec61131::il::Param::Assignment2.__init__)


def test_iec61131::il::param::assignment2_constructor_args():
    sig = inspect.signature(iec61131::il::Param::Assignment2.__init__)
    params = list(sig.parameters.keys())



def test_subprogram::control::statement_is_not_abstract():
    assert not inspect.isabstract(Subprogram::Control::Statement)


def test_subprogram::control::statement_constructor_exists():
    assert callable(Subprogram::Control::Statement.__init__)


def test_subprogram::control::statement_constructor_args():
    sig = inspect.signature(Subprogram::Control::Statement.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::fb::invocation_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Fb::Invocation)


def test_iec61131::st::fb::invocation_constructor_exists():
    assert callable(iec61131::st::Fb::Invocation.__init__)


def test_iec61131::st::fb::invocation_constructor_args():
    sig = inspect.signature(iec61131::st::Fb::Invocation.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::return::statement_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Return::Statement)


def test_iec61131::st::return::statement_constructor_exists():
    assert callable(iec61131::st::Return::Statement.__init__)


def test_iec61131::st::return::statement_constructor_args():
    sig = inspect.signature(iec61131::st::Return::Statement.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::iteration::statement_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Iteration::Statement)


def test_iec61131::st::iteration::statement_constructor_exists():
    assert callable(iec61131::st::Iteration::Statement.__init__)


def test_iec61131::st::iteration::statement_constructor_args():
    sig = inspect.signature(iec61131::st::Iteration::Statement.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::selection::statement_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Selection::Statement)


def test_iec61131::st::selection::statement_constructor_exists():
    assert callable(iec61131::st::Selection::Statement.__init__)


def test_iec61131::st::selection::statement_constructor_args():
    sig = inspect.signature(iec61131::st::Selection::Statement.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::subprogram::control::statement_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Subprogram::Control::Statement)


def test_iec61131::st::subprogram::control::statement_constructor_exists():
    assert callable(iec61131::st::Subprogram::Control::Statement.__init__)


def test_iec61131::st::subprogram::control::statement_constructor_args():
    sig = inspect.signature(iec61131::st::Subprogram::Control::Statement.__init__)
    params = list(sig.parameters.keys())



def test_expression::variable_is_not_abstract():
    assert not inspect.isabstract(Expression::Variable)


def test_expression::variable_constructor_exists():
    assert callable(Expression::Variable.__init__)


def test_expression::variable_constructor_args():
    sig = inspect.signature(Expression::Variable.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::assignment::statement_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Assignment::Statement)


def test_iec61131::st::assignment::statement_constructor_exists():
    assert callable(iec61131::st::Assignment::Statement.__init__)


def test_iec61131::st::assignment::statement_constructor_args():
    sig = inspect.signature(iec61131::st::Assignment::Statement.__init__)
    params = list(sig.parameters.keys())



def test_or::operator_is_not_abstract():
    assert not inspect.isabstract(Or::Operator)


def test_or::operator_constructor_exists():
    assert callable(Or::Operator.__init__)


def test_or::operator_constructor_args():
    sig = inspect.signature(Or::Operator.__init__)
    params = list(sig.parameters.keys())



def test_expression::types_is_not_abstract():
    assert not inspect.isabstract(Expression::Types)


def test_expression::types_constructor_exists():
    assert callable(Expression::Types.__init__)


def test_expression::types_constructor_args():
    sig = inspect.signature(Expression::Types.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::power::expression_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Power::Expression)


def test_iec61131::st::power::expression_constructor_exists():
    assert callable(iec61131::st::Power::Expression.__init__)


def test_iec61131::st::power::expression_constructor_args():
    sig = inspect.signature(iec61131::st::Power::Expression.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::comparison_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Comparison)


def test_iec61131::st::comparison_constructor_exists():
    assert callable(iec61131::st::Comparison.__init__)


def test_iec61131::st::comparison_constructor_args():
    sig = inspect.signature(iec61131::st::Comparison.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::equ::expression_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Equ::Expression)


def test_iec61131::st::equ::expression_constructor_exists():
    assert callable(iec61131::st::Equ::Expression.__init__)


def test_iec61131::st::equ::expression_constructor_args():
    sig = inspect.signature(iec61131::st::Equ::Expression.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::and::expression_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::And::Expression)


def test_iec61131::st::and::expression_constructor_exists():
    assert callable(iec61131::st::And::Expression.__init__)


def test_iec61131::st::and::expression_constructor_args():
    sig = inspect.signature(iec61131::st::And::Expression.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::xor::expression_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Xor::Expression)


def test_iec61131::st::xor::expression_constructor_exists():
    assert callable(iec61131::st::Xor::Expression.__init__)


def test_iec61131::st::xor::expression_constructor_args():
    sig = inspect.signature(iec61131::st::Xor::Expression.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::term::expression_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Term::Expression)


def test_iec61131::st::term::expression_constructor_exists():
    assert callable(iec61131::st::Term::Expression.__init__)


def test_iec61131::st::term::expression_constructor_args():
    sig = inspect.signature(iec61131::st::Term::Expression.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::primary::expression_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Primary::Expression)


def test_iec61131::st::primary::expression_constructor_exists():
    assert callable(iec61131::st::Primary::Expression.__init__)


def test_iec61131::st::primary::expression_constructor_args():
    sig = inspect.signature(iec61131::st::Primary::Expression.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::add::expression_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Add::Expression)


def test_iec61131::st::add::expression_constructor_exists():
    assert callable(iec61131::st::Add::Expression.__init__)


def test_iec61131::st::add::expression_constructor_args():
    sig = inspect.signature(iec61131::st::Add::Expression.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::unary::expression_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Unary::Expression)


def test_iec61131::st::unary::expression_constructor_exists():
    assert callable(iec61131::st::Unary::Expression.__init__)


def test_iec61131::st::unary::expression_constructor_args():
    sig = inspect.signature(iec61131::st::Unary::Expression.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::expression_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Expression)


def test_iec61131::st::expression_constructor_exists():
    assert callable(iec61131::st::Expression.__init__)


def test_iec61131::st::expression_constructor_args():
    sig = inspect.signature(iec61131::st::Expression.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::prog::data::source_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Prog::Data::Source)


def test_iec61131::configurations::prog::data::source_constructor_exists():
    assert callable(iec61131::configurations::Prog::Data::Source.__init__)


def test_iec61131::configurations::prog::data::source_constructor_args():
    sig = inspect.signature(iec61131::configurations::Prog::Data::Source.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::prog::conf::element_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Prog::Conf::Element)


def test_iec61131::configurations::prog::conf::element_constructor_exists():
    assert callable(iec61131::configurations::Prog::Conf::Element.__init__)


def test_iec61131::configurations::prog::conf::element_constructor_args():
    sig = inspect.signature(iec61131::configurations::Prog::Conf::Element.__init__)
    params = list(sig.parameters.keys())



def test_prog::conf::element_is_not_abstract():
    assert not inspect.isabstract(Prog::Conf::Element)


def test_prog::conf::element_constructor_exists():
    assert callable(Prog::Conf::Element.__init__)


def test_prog::conf::element_constructor_args():
    sig = inspect.signature(Prog::Conf::Element.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::prog::cnxn_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Prog::Cnxn)


def test_iec61131::configurations::prog::cnxn_constructor_exists():
    assert callable(iec61131::configurations::Prog::Cnxn.__init__)


def test_iec61131::configurations::prog::cnxn_constructor_args():
    sig = inspect.signature(iec61131::configurations::Prog::Cnxn.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::fb::task_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Fb::Task)


def test_iec61131::configurations::fb::task_constructor_exists():
    assert callable(iec61131::configurations::Fb::Task.__init__)


def test_iec61131::configurations::fb::task_constructor_args():
    sig = inspect.signature(iec61131::configurations::Fb::Task.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::prog::conf::elements_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Prog::Conf::Elements)


def test_iec61131::configurations::prog::conf::elements_constructor_exists():
    assert callable(iec61131::configurations::Prog::Conf::Elements.__init__)


def test_iec61131::configurations::prog::conf::elements_constructor_args():
    sig = inspect.signature(iec61131::configurations::Prog::Conf::Elements.__init__)
    params = list(sig.parameters.keys())



def test_task::initialization_is_not_abstract():
    assert not inspect.isabstract(Task::Initialization)


def test_task::initialization_constructor_exists():
    assert callable(Task::Initialization.__init__)


def test_task::initialization_constructor_args():
    sig = inspect.signature(Task::Initialization.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::priority_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Priority)


def test_iec61131::configurations::priority_constructor_exists():
    assert callable(iec61131::configurations::Priority.__init__)


def test_iec61131::configurations::priority_constructor_args():
    sig = inspect.signature(iec61131::configurations::Priority.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::interval_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Interval)


def test_iec61131::configurations::interval_constructor_exists():
    assert callable(iec61131::configurations::Interval.__init__)


def test_iec61131::configurations::interval_constructor_args():
    sig = inspect.signature(iec61131::configurations::Interval.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::single_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Single)


def test_iec61131::configurations::single_constructor_exists():
    assert callable(iec61131::configurations::Single.__init__)


def test_iec61131::configurations::single_constructor_args():
    sig = inspect.signature(iec61131::configurations::Single.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::instance::specific::init_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Instance::Specific::Init)


def test_iec61131::configurations::instance::specific::init_constructor_exists():
    assert callable(iec61131::configurations::Instance::Specific::Init.__init__)


def test_iec61131::configurations::instance::specific::init_constructor_args():
    sig = inspect.signature(iec61131::configurations::Instance::Specific::Init.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::data::sink_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Data::Sink)


def test_iec61131::configurations::data::sink_constructor_exists():
    assert callable(iec61131::configurations::Data::Sink.__init__)


def test_iec61131::configurations::data::sink_constructor_args():
    sig = inspect.signature(iec61131::configurations::Data::Sink.__init__)
    params = list(sig.parameters.keys())



def test_prog::data::source_is_not_abstract():
    assert not inspect.isabstract(Prog::Data::Source)


def test_prog::data::source_constructor_exists():
    assert callable(Prog::Data::Source.__init__)


def test_prog::data::source_constructor_args():
    sig = inspect.signature(Prog::Data::Source.__init__)
    params = list(sig.parameters.keys())



def test_data::sink_is_not_abstract():
    assert not inspect.isabstract(Data::Sink)


def test_data::sink_constructor_exists():
    assert callable(Data::Sink.__init__)


def test_data::sink_constructor_args():
    sig = inspect.signature(Data::Sink.__init__)
    params = list(sig.parameters.keys())



def test_prog::cnxn_is_not_abstract():
    assert not inspect.isabstract(Prog::Cnxn)


def test_prog::cnxn_constructor_exists():
    assert callable(Prog::Cnxn.__init__)


def test_prog::cnxn_constructor_args():
    sig = inspect.signature(Prog::Cnxn.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::prog::source_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Prog::Source)


def test_iec61131::configurations::prog::source_constructor_exists():
    assert callable(iec61131::configurations::Prog::Source.__init__)


def test_iec61131::configurations::prog::source_constructor_args():
    sig = inspect.signature(iec61131::configurations::Prog::Source.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::prog::sink_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Prog::Sink)


def test_iec61131::configurations::prog::sink_constructor_exists():
    assert callable(iec61131::configurations::Prog::Sink.__init__)


def test_iec61131::configurations::prog::sink_constructor_args():
    sig = inspect.signature(iec61131::configurations::Prog::Sink.__init__)
    params = list(sig.parameters.keys())



def test_data::source_is_not_abstract():
    assert not inspect.isabstract(Data::Source)


def test_data::source_constructor_exists():
    assert callable(Data::Source.__init__)


def test_data::source_constructor_args():
    sig = inspect.signature(Data::Source.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::program::output::reference_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Program::Output::Reference)


def test_iec61131::configurations::program::output::reference_constructor_exists():
    assert callable(iec61131::configurations::Program::Output::Reference.__init__)


def test_iec61131::configurations::program::output::reference_constructor_args():
    sig = inspect.signature(iec61131::configurations::Program::Output::Reference.__init__)
    params = list(sig.parameters.keys())



def test_configurations::data::sink_is_not_abstract():
    assert not inspect.isabstract(configurations::Data::Sink)


def test_configurations::data::sink_constructor_exists():
    assert callable(configurations::Data::Sink.__init__)


def test_configurations::data::sink_constructor_args():
    sig = inspect.signature(configurations::Data::Sink.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::data::source_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Data::Source)


def test_iec61131::configurations::data::source_constructor_exists():
    assert callable(iec61131::configurations::Data::Source.__init__)


def test_iec61131::configurations::data::source_constructor_args():
    sig = inspect.signature(iec61131::configurations::Data::Source.__init__)
    params = list(sig.parameters.keys())



def test_instance::specific::init_is_not_abstract():
    assert not inspect.isabstract(Instance::Specific::Init)


def test_instance::specific::init_constructor_exists():
    assert callable(Instance::Specific::Init.__init__)


def test_instance::specific::init_constructor_args():
    sig = inspect.signature(Instance::Specific::Init.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::instance::spec2_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Instance::Spec2)


def test_iec61131::configurations::instance::spec2_constructor_exists():
    assert callable(iec61131::configurations::Instance::Spec2.__init__)


def test_iec61131::configurations::instance::spec2_constructor_args():
    sig = inspect.signature(iec61131::configurations::Instance::Spec2.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::instance::spec1_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Instance::Spec1)


def test_iec61131::configurations::instance::spec1_constructor_exists():
    assert callable(iec61131::configurations::Instance::Spec1.__init__)


def test_iec61131::configurations::instance::spec1_constructor_args():
    sig = inspect.signature(iec61131::configurations::Instance::Spec1.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::instance::specific::initializations_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Instance::Specific::Initializations)


def test_iec61131::configurations::instance::specific::initializations_constructor_exists():
    assert callable(iec61131::configurations::Instance::Specific::Initializations.__init__)


def test_iec61131::configurations::instance::specific::initializations_constructor_args():
    sig = inspect.signature(iec61131::configurations::Instance::Specific::Initializations.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::task::initialization_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Task::Initialization)


def test_iec61131::configurations::task::initialization_constructor_exists():
    assert callable(iec61131::configurations::Task::Initialization.__init__)


def test_iec61131::configurations::task::initialization_constructor_args():
    sig = inspect.signature(iec61131::configurations::Task::Initialization.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::task::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Task::Name)


def test_iec61131::configurations::task::name_constructor_exists():
    assert callable(iec61131::configurations::Task::Name.__init__)


def test_iec61131::configurations::task::name_constructor_args():
    sig = inspect.signature(iec61131::configurations::Task::Name.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iec61131::configurations::task::name_has_name():
    assert hasattr(iec61131::configurations::Task::Name, "name")
    descriptor = None
    for klass in iec61131::configurations::Task::Name.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iec61131::configurations::program::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Program::Name)


def test_iec61131::configurations::program::name_constructor_exists():
    assert callable(iec61131::configurations::Program::Name.__init__)


def test_iec61131::configurations::program::name_constructor_args():
    sig = inspect.signature(iec61131::configurations::Program::Name.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iec61131::configurations::program::name_has_name():
    assert hasattr(iec61131::configurations::Program::Name, "name")
    descriptor = None
    for klass in iec61131::configurations::Program::Name.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iec61131::configurations::access::path_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Access::Path)


def test_iec61131::configurations::access::path_constructor_exists():
    assert callable(iec61131::configurations::Access::Path.__init__)


def test_iec61131::configurations::access::path_constructor_args():
    sig = inspect.signature(iec61131::configurations::Access::Path.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::access::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Access::Name)


def test_iec61131::configurations::access::name_constructor_exists():
    assert callable(iec61131::configurations::Access::Name.__init__)


def test_iec61131::configurations::access::name_constructor_args():
    sig = inspect.signature(iec61131::configurations::Access::Name.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iec61131::configurations::access::name_has_name():
    assert hasattr(iec61131::configurations::Access::Name, "name")
    descriptor = None
    for klass in iec61131::configurations::Access::Name.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_access::path_is_not_abstract():
    assert not inspect.isabstract(Access::Path)


def test_access::path_constructor_exists():
    assert callable(Access::Path.__init__)


def test_access::path_constructor_args():
    sig = inspect.signature(Access::Path.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::symbolic::path_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Symbolic::Path)


def test_iec61131::configurations::symbolic::path_constructor_exists():
    assert callable(iec61131::configurations::Symbolic::Path.__init__)


def test_iec61131::configurations::symbolic::path_constructor_args():
    sig = inspect.signature(iec61131::configurations::Symbolic::Path.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::direct::path_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Direct::Path)


def test_iec61131::configurations::direct::path_constructor_exists():
    assert callable(iec61131::configurations::Direct::Path.__init__)


def test_iec61131::configurations::direct::path_constructor_args():
    sig = inspect.signature(iec61131::configurations::Direct::Path.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::access::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Access::Declaration)


def test_iec61131::configurations::access::declaration_constructor_exists():
    assert callable(iec61131::configurations::Access::Declaration.__init__)


def test_iec61131::configurations::access::declaration_constructor_args():
    sig = inspect.signature(iec61131::configurations::Access::Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_iec61131::configurations::access::declaration_has_direction():
    assert hasattr(iec61131::configurations::Access::Declaration, "direction")
    descriptor = None
    for klass in iec61131::configurations::Access::Declaration.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_access::declaration_is_not_abstract():
    assert not inspect.isabstract(Access::Declaration)


def test_access::declaration_constructor_exists():
    assert callable(Access::Declaration.__init__)


def test_access::declaration_constructor_args():
    sig = inspect.signature(Access::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::access::declarations_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Access::Declarations)


def test_iec61131::configurations::access::declarations_constructor_exists():
    assert callable(iec61131::configurations::Access::Declarations.__init__)


def test_iec61131::configurations::access::declarations_constructor_args():
    sig = inspect.signature(iec61131::configurations::Access::Declarations.__init__)
    params = list(sig.parameters.keys())



def test_resource::declaration_is_not_abstract():
    assert not inspect.isabstract(Resource::Declaration)


def test_resource::declaration_constructor_exists():
    assert callable(Resource::Declaration.__init__)


def test_resource::declaration_constructor_args():
    sig = inspect.signature(Resource::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_access::declarations_is_not_abstract():
    assert not inspect.isabstract(Access::Declarations)


def test_access::declarations_constructor_exists():
    assert callable(Access::Declarations.__init__)


def test_access::declarations_constructor_args():
    sig = inspect.signature(Access::Declarations.__init__)
    params = list(sig.parameters.keys())



def test_instance::specific::initializations_is_not_abstract():
    assert not inspect.isabstract(Instance::Specific::Initializations)


def test_instance::specific::initializations_constructor_exists():
    assert callable(Instance::Specific::Initializations.__init__)


def test_instance::specific::initializations_constructor_args():
    sig = inspect.signature(Instance::Specific::Initializations.__init__)
    params = list(sig.parameters.keys())



def test_global::var::declarations_is_not_abstract():
    assert not inspect.isabstract(Global::Var::Declarations)


def test_global::var::declarations_constructor_exists():
    assert callable(Global::Var::Declarations.__init__)


def test_global::var::declarations_constructor_args():
    sig = inspect.signature(Global::Var::Declarations.__init__)
    params = list(sig.parameters.keys())



def test_single::resource::declaration_is_not_abstract():
    assert not inspect.isabstract(Single::Resource::Declaration)


def test_single::resource::declaration_constructor_exists():
    assert callable(Single::Resource::Declaration.__init__)


def test_single::resource::declaration_constructor_args():
    sig = inspect.signature(Single::Resource::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_configuration::name_is_not_abstract():
    assert not inspect.isabstract(Configuration::Name)


def test_configuration::name_constructor_exists():
    assert callable(Configuration::Name.__init__)


def test_configuration::name_constructor_args():
    sig = inspect.signature(Configuration::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::resource::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Resource::Type::Name)


def test_iec61131::configurations::resource::type::name_constructor_exists():
    assert callable(iec61131::configurations::Resource::Type::Name.__init__)


def test_iec61131::configurations::resource::type::name_constructor_args():
    sig = inspect.signature(iec61131::configurations::Resource::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_prog::conf::elements_is_not_abstract():
    assert not inspect.isabstract(Prog::Conf::Elements)


def test_prog::conf::elements_constructor_exists():
    assert callable(Prog::Conf::Elements.__init__)


def test_prog::conf::elements_constructor_args():
    sig = inspect.signature(Prog::Conf::Elements.__init__)
    params = list(sig.parameters.keys())



def test_program::name_is_not_abstract():
    assert not inspect.isabstract(Program::Name)


def test_program::name_constructor_exists():
    assert callable(Program::Name.__init__)


def test_program::name_constructor_args():
    sig = inspect.signature(Program::Name.__init__)
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



def test_task::name_is_not_abstract():
    assert not inspect.isabstract(Task::Name)


def test_task::name_constructor_exists():
    assert callable(Task::Name.__init__)


def test_task::name_constructor_args():
    sig = inspect.signature(Task::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::task::configuration_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Task::Configuration)


def test_iec61131::configurations::task::configuration_constructor_exists():
    assert callable(iec61131::configurations::Task::Configuration.__init__)


def test_iec61131::configurations::task::configuration_constructor_args():
    sig = inspect.signature(iec61131::configurations::Task::Configuration.__init__)
    params = list(sig.parameters.keys())



def test_program::configuration_is_not_abstract():
    assert not inspect.isabstract(Program::Configuration)


def test_program::configuration_constructor_exists():
    assert callable(Program::Configuration.__init__)


def test_program::configuration_constructor_args():
    sig = inspect.signature(Program::Configuration.__init__)
    params = list(sig.parameters.keys())



def test_task::configuration_is_not_abstract():
    assert not inspect.isabstract(Task::Configuration)


def test_task::configuration_constructor_exists():
    assert callable(Task::Configuration.__init__)


def test_task::configuration_constructor_args():
    sig = inspect.signature(Task::Configuration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::single::resource::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Single::Resource::Declaration)


def test_iec61131::configurations::single::resource::declaration_constructor_exists():
    assert callable(iec61131::configurations::Single::Resource::Declaration.__init__)


def test_iec61131::configurations::single::resource::declaration_constructor_args():
    sig = inspect.signature(iec61131::configurations::Single::Resource::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_resource::type::name_is_not_abstract():
    assert not inspect.isabstract(Resource::Type::Name)


def test_resource::type::name_constructor_exists():
    assert callable(Resource::Type::Name.__init__)


def test_resource::type::name_constructor_args():
    sig = inspect.signature(Resource::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_resource::name_is_not_abstract():
    assert not inspect.isabstract(Resource::Name)


def test_resource::name_constructor_exists():
    assert callable(Resource::Name.__init__)


def test_resource::name_constructor_args():
    sig = inspect.signature(Resource::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::resource::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Resource::Name)


def test_iec61131::configurations::resource::name_constructor_exists():
    assert callable(iec61131::configurations::Resource::Name.__init__)


def test_iec61131::configurations::resource::name_constructor_args():
    sig = inspect.signature(iec61131::configurations::Resource::Name.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iec61131::configurations::resource::name_has_name():
    assert hasattr(iec61131::configurations::Resource::Name, "name")
    descriptor = None
    for klass in iec61131::configurations::Resource::Name.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_simple::type::name_is_not_abstract():
    assert not inspect.isabstract(Simple::Type::Name)


def test_simple::type::name_constructor_exists():
    assert callable(Simple::Type::Name.__init__)


def test_simple::type::name_constructor_args():
    sig = inspect.signature(Simple::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_single::element::type::declaration_is_not_abstract():
    assert not inspect.isabstract(Single::Element::Type::Declaration)


def test_single::element::type::declaration_constructor_exists():
    assert callable(Single::Element::Type::Declaration.__init__)


def test_single::element::type::declaration_constructor_args():
    sig = inspect.signature(Single::Element::Type::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::subrange::type::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Subrange::Type::Declaration)


def test_iec61131::pous::subrange::type::declaration_constructor_exists():
    assert callable(iec61131::pous::Subrange::Type::Declaration.__init__)


def test_iec61131::pous::subrange::type::declaration_constructor_args():
    sig = inspect.signature(iec61131::pous::Subrange::Type::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::simple::type::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Simple::Type::Declaration)


def test_iec61131::pous::simple::type::declaration_constructor_exists():
    assert callable(iec61131::pous::Simple::Type::Declaration.__init__)


def test_iec61131::pous::simple::type::declaration_constructor_args():
    sig = inspect.signature(iec61131::pous::Simple::Type::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::configuration::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Configuration::Name)


def test_iec61131::configurations::configuration::name_constructor_exists():
    assert callable(iec61131::configurations::Configuration::Name.__init__)


def test_iec61131::configurations::configuration::name_constructor_args():
    sig = inspect.signature(iec61131::configurations::Configuration::Name.__init__)
    params = list(sig.parameters.keys())



def test_function::block::declaration_is_not_abstract():
    assert not inspect.isabstract(Function::Block::Declaration)


def test_function::block::declaration_constructor_exists():
    assert callable(Function::Block::Declaration.__init__)


def test_function::block::declaration_constructor_args():
    sig = inspect.signature(Function::Block::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_function::declaration_is_not_abstract():
    assert not inspect.isabstract(Function::Declaration)


def test_function::declaration_constructor_exists():
    assert callable(Function::Declaration.__init__)


def test_function::declaration_constructor_args():
    sig = inspect.signature(Function::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_program::declaration_is_not_abstract():
    assert not inspect.isabstract(Program::Declaration)


def test_program::declaration_constructor_exists():
    assert callable(Program::Declaration.__init__)


def test_program::declaration_constructor_args():
    sig = inspect.signature(Program::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::library_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Library)


def test_iec61131::pous::library_constructor_exists():
    assert callable(iec61131::pous::Library.__init__)


def test_iec61131::pous::library_constructor_args():
    sig = inspect.signature(iec61131::pous::Library.__init__)
    params = list(sig.parameters.keys())



def test_program::access::decl_is_not_abstract():
    assert not inspect.isabstract(Program::Access::Decl)


def test_program::access::decl_constructor_exists():
    assert callable(Program::Access::Decl.__init__)


def test_program::access::decl_constructor_args():
    sig = inspect.signature(Program::Access::Decl.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::function::block::vars_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Function::Block::Vars)


def test_iec61131::pous::function::block::vars_constructor_exists():
    assert callable(iec61131::pous::Function::Block::Vars.__init__)


def test_iec61131::pous::function::block::vars_constructor_args():
    sig = inspect.signature(iec61131::pous::Function::Block::Vars.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::function::vars_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Function::Vars)


def test_iec61131::pous::function::vars_constructor_exists():
    assert callable(iec61131::pous::Function::Vars.__init__)


def test_iec61131::pous::function::vars_constructor_args():
    sig = inspect.signature(iec61131::pous::Function::Vars.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::program::vars_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Program::Vars)


def test_iec61131::pous::program::vars_constructor_exists():
    assert callable(iec61131::pous::Program::Vars.__init__)


def test_iec61131::pous::program::vars_constructor_args():
    sig = inspect.signature(iec61131::pous::Program::Vars.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::structure::elements_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Structure::Elements)


def test_iec61131::pous::structure::elements_constructor_exists():
    assert callable(iec61131::pous::Structure::Elements.__init__)


def test_iec61131::pous::structure::elements_constructor_args():
    sig = inspect.signature(iec61131::pous::Structure::Elements.__init__)
    params = list(sig.parameters.keys())



def test_structure::elements_is_not_abstract():
    assert not inspect.isabstract(Structure::Elements)


def test_structure::elements_constructor_exists():
    assert callable(Structure::Elements.__init__)


def test_structure::elements_constructor_args():
    sig = inspect.signature(Structure::Elements.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::structure::element::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Structure::Element::Declaration)


def test_iec61131::pous::structure::element::declaration_constructor_exists():
    assert callable(iec61131::pous::Structure::Element::Declaration.__init__)


def test_iec61131::pous::structure::element::declaration_constructor_args():
    sig = inspect.signature(iec61131::pous::Structure::Element::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_structure::element::declaration_is_not_abstract():
    assert not inspect.isabstract(Structure::Element::Declaration)


def test_structure::element::declaration_constructor_exists():
    assert callable(Structure::Element::Declaration.__init__)


def test_structure::element::declaration_constructor_args():
    sig = inspect.signature(Structure::Element::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::structure::specification_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Structure::Specification)


def test_iec61131::pous::structure::specification_constructor_exists():
    assert callable(iec61131::pous::Structure::Specification.__init__)


def test_iec61131::pous::structure::specification_constructor_args():
    sig = inspect.signature(iec61131::pous::Structure::Specification.__init__)
    params = list(sig.parameters.keys())



def test_enumerated::spec::init_is_not_abstract():
    assert not inspect.isabstract(Enumerated::Spec::Init)


def test_enumerated::spec::init_constructor_exists():
    assert callable(Enumerated::Spec::Init.__init__)


def test_enumerated::spec::init_constructor_args():
    sig = inspect.signature(Enumerated::Spec::Init.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::enumerated::type::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Enumerated::Type::Declaration)


def test_iec61131::pous::enumerated::type::declaration_constructor_exists():
    assert callable(iec61131::pous::Enumerated::Type::Declaration.__init__)


def test_iec61131::pous::enumerated::type::declaration_constructor_args():
    sig = inspect.signature(iec61131::pous::Enumerated::Type::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_subrange::spec::init_is_not_abstract():
    assert not inspect.isabstract(Subrange::Spec::Init)


def test_subrange::spec::init_constructor_exists():
    assert callable(Subrange::Spec::Init.__init__)


def test_subrange::spec::init_constructor_args():
    sig = inspect.signature(Subrange::Spec::Init.__init__)
    params = list(sig.parameters.keys())



def test_pous::function::block::body_is_not_abstract():
    assert not inspect.isabstract(pous::Function::Block::Body)


def test_pous::function::block::body_constructor_exists():
    assert callable(pous::Function::Block::Body.__init__)


def test_pous::function::block::body_constructor_args():
    sig = inspect.signature(pous::Function::Block::Body.__init__)
    params = list(sig.parameters.keys())



def test_pous::function::body_is_not_abstract():
    assert not inspect.isabstract(pous::Function::Body)


def test_pous::function::body_constructor_exists():
    assert callable(pous::Function::Body.__init__)


def test_pous::function::body_constructor_args():
    sig = inspect.signature(pous::Function::Body.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::ld::ladder::diagram_is_not_abstract():
    assert not inspect.isabstract(iec61131::ld::Ladder::Diagram)


def test_iec61131::ld::ladder::diagram_constructor_exists():
    assert callable(iec61131::ld::Ladder::Diagram.__init__)


def test_iec61131::ld::ladder::diagram_constructor_args():
    sig = inspect.signature(iec61131::ld::Ladder::Diagram.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::statement::list_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Statement::List)


def test_iec61131::st::statement::list_constructor_exists():
    assert callable(iec61131::st::Statement::List.__init__)


def test_iec61131::st::statement::list_constructor_args():
    sig = inspect.signature(iec61131::st::Statement::List.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::il::instruction::list_is_not_abstract():
    assert not inspect.isabstract(iec61131::il::Instruction::List)


def test_iec61131::il::instruction::list_constructor_exists():
    assert callable(iec61131::il::Instruction::List.__init__)


def test_iec61131::il::instruction::list_constructor_args():
    sig = inspect.signature(iec61131::il::Instruction::List.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::fbd::function::block::diagram_is_not_abstract():
    assert not inspect.isabstract(iec61131::fbd::Function::Block::Diagram)


def test_iec61131::fbd::function::block::diagram_constructor_exists():
    assert callable(iec61131::fbd::Function::Block::Diagram.__init__)


def test_iec61131::fbd::function::block::diagram_constructor_args():
    sig = inspect.signature(iec61131::fbd::Function::Block::Diagram.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::other::language_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Other::Language)


def test_iec61131::pous::other::language_constructor_exists():
    assert callable(iec61131::pous::Other::Language.__init__)


def test_iec61131::pous::other::language_constructor_args():
    sig = inspect.signature(iec61131::pous::Other::Language.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_iec61131::pous::other::language_has_text():
    assert hasattr(iec61131::pous::Other::Language, "text")
    descriptor = None
    for klass in iec61131::pous::Other::Language.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_iec61131::pous::function::body_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Function::Body)


def test_iec61131::pous::function::body_constructor_exists():
    assert callable(iec61131::pous::Function::Body.__init__)


def test_iec61131::pous::function::body_constructor_args():
    sig = inspect.signature(iec61131::pous::Function::Body.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::function::return::value_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Function::Return::Value)


def test_iec61131::pous::function::return::value_constructor_exists():
    assert callable(iec61131::pous::Function::Return::Value.__init__)


def test_iec61131::pous::function::return::value_constructor_args():
    sig = inspect.signature(iec61131::pous::Function::Return::Value.__init__)
    params = list(sig.parameters.keys())



def test_pous::function::name_is_not_abstract():
    assert not inspect.isabstract(pous::Function::Name)


def test_pous::function::name_constructor_exists():
    assert callable(pous::Function::Name.__init__)


def test_pous::function::name_constructor_args():
    sig = inspect.signature(pous::Function::Name.__init__)
    params = list(sig.parameters.keys())



def test_function::body_is_not_abstract():
    assert not inspect.isabstract(Function::Body)


def test_function::body_constructor_exists():
    assert callable(Function::Body.__init__)


def test_function::body_constructor_args():
    sig = inspect.signature(Function::Body.__init__)
    params = list(sig.parameters.keys())



def test_function::vars_is_not_abstract():
    assert not inspect.isabstract(Function::Vars)


def test_function::vars_constructor_exists():
    assert callable(Function::Vars.__init__)


def test_function::vars_constructor_args():
    sig = inspect.signature(Function::Vars.__init__)
    params = list(sig.parameters.keys())



def test_byte::string::type::name_is_not_abstract():
    assert not inspect.isabstract(Byte::String::Type::Name)


def test_byte::string::type::name_constructor_exists():
    assert callable(Byte::String::Type::Name.__init__)


def test_byte::string::type::name_constructor_args():
    sig = inspect.signature(Byte::String::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::single::byte::string::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::Single::Byte::String::Type::Name)


def test_iec61131::types::single::byte::string::type::name_constructor_exists():
    assert callable(iec61131::types::Single::Byte::String::Type::Name.__init__)


def test_iec61131::types::single::byte::string::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::Single::Byte::String::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::double::byte::string::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::Double::Byte::String::Type::Name)


def test_iec61131::types::double::byte::string::type::name_constructor_exists():
    assert callable(iec61131::types::Double::Byte::String::Type::Name.__init__)


def test_iec61131::types::double::byte::string::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::Double::Byte::String::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_string::type::name_is_not_abstract():
    assert not inspect.isabstract(String::Type::Name)


def test_string::type::name_constructor_exists():
    assert callable(String::Type::Name.__init__)


def test_string::type::name_constructor_args():
    sig = inspect.signature(String::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_structure::specification_is_not_abstract():
    assert not inspect.isabstract(Structure::Specification)


def test_structure::specification_constructor_exists():
    assert callable(Structure::Specification.__init__)


def test_structure::specification_constructor_args():
    sig = inspect.signature(Structure::Specification.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::structure::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Structure::Declaration)


def test_iec61131::pous::structure::declaration_constructor_exists():
    assert callable(iec61131::pous::Structure::Declaration.__init__)


def test_iec61131::pous::structure::declaration_constructor_args():
    sig = inspect.signature(iec61131::pous::Structure::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::type::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Type::Declaration)


def test_iec61131::pous::type::declaration_constructor_exists():
    assert callable(iec61131::pous::Type::Declaration.__init__)


def test_iec61131::pous::type::declaration_constructor_args():
    sig = inspect.signature(iec61131::pous::Type::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_type::declaration_is_not_abstract():
    assert not inspect.isabstract(Type::Declaration)


def test_type::declaration_constructor_exists():
    assert callable(Type::Declaration.__init__)


def test_type::declaration_constructor_args():
    sig = inspect.signature(Type::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::structure::type::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Structure::Type::Declaration)


def test_iec61131::pous::structure::type::declaration_constructor_exists():
    assert callable(iec61131::pous::Structure::Type::Declaration.__init__)


def test_iec61131::pous::structure::type::declaration_constructor_args():
    sig = inspect.signature(iec61131::pous::Structure::Type::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::array::type::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Array::Type::Declaration)


def test_iec61131::pous::array::type::declaration_constructor_exists():
    assert callable(iec61131::pous::Array::Type::Declaration.__init__)


def test_iec61131::pous::array::type::declaration_constructor_args():
    sig = inspect.signature(iec61131::pous::Array::Type::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::single::element::type::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Single::Element::Type::Declaration)


def test_iec61131::pous::single::element::type::declaration_constructor_exists():
    assert callable(iec61131::pous::Single::Element::Type::Declaration.__init__)


def test_iec61131::pous::single::element::type::declaration_constructor_args():
    sig = inspect.signature(iec61131::pous::Single::Element::Type::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::string::type::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::String::Type::Declaration)


def test_iec61131::pous::string::type::declaration_constructor_exists():
    assert callable(iec61131::pous::String::Type::Declaration.__init__)


def test_iec61131::pous::string::type::declaration_constructor_args():
    sig = inspect.signature(iec61131::pous::String::Type::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::function::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Function::Name)


def test_iec61131::pous::function::name_constructor_exists():
    assert callable(iec61131::pous::Function::Name.__init__)


def test_iec61131::pous::function::name_constructor_args():
    sig = inspect.signature(iec61131::pous::Function::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::access::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Access::Name)


def test_iec61131::pous::access::name_constructor_exists():
    assert callable(iec61131::pous::Access::Name.__init__)


def test_iec61131::pous::access::name_constructor_args():
    sig = inspect.signature(iec61131::pous::Access::Name.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iec61131::pous::access::name_has_name():
    assert hasattr(iec61131::pous::Access::Name, "name")
    descriptor = None
    for klass in iec61131::pous::Access::Name.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_symbolic::variable_is_not_abstract():
    assert not inspect.isabstract(Symbolic::Variable)


def test_symbolic::variable_constructor_exists():
    assert callable(Symbolic::Variable.__init__)


def test_symbolic::variable_constructor_args():
    sig = inspect.signature(Symbolic::Variable.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::variables::multi::element::variable_is_not_abstract():
    assert not inspect.isabstract(iec61131::variables::Multi::Element::Variable)


def test_iec61131::variables::multi::element::variable_constructor_exists():
    assert callable(iec61131::variables::Multi::Element::Variable.__init__)


def test_iec61131::variables::multi::element::variable_constructor_args():
    sig = inspect.signature(iec61131::variables::Multi::Element::Variable.__init__)
    params = list(sig.parameters.keys())



def test_access::name_is_not_abstract():
    assert not inspect.isabstract(Access::Name)


def test_access::name_constructor_exists():
    assert callable(Access::Name.__init__)


def test_access::name_constructor_args():
    sig = inspect.signature(Access::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::program::access::decl_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Program::Access::Decl)


def test_iec61131::pous::program::access::decl_constructor_exists():
    assert callable(iec61131::pous::Program::Access::Decl.__init__)


def test_iec61131::pous::program::access::decl_constructor_args():
    sig = inspect.signature(iec61131::pous::Program::Access::Decl.__init__)
    params = list(sig.parameters.keys())
    assert "direction" in params, "Missing parameter 'direction'"

def test_iec61131::pous::program::access::decl_has_direction():
    assert hasattr(iec61131::pous::Program::Access::Decl, "direction")
    descriptor = None
    for klass in iec61131::pous::Program::Access::Decl.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_iec61131::pous::function::block::body_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Function::Block::Body)


def test_iec61131::pous::function::block::body_constructor_exists():
    assert callable(iec61131::pous::Function::Block::Body.__init__)


def test_iec61131::pous::function::block::body_constructor_args():
    sig = inspect.signature(iec61131::pous::Function::Block::Body.__init__)
    params = list(sig.parameters.keys())



def test_program::type::name_is_not_abstract():
    assert not inspect.isabstract(Program::Type::Name)


def test_program::type::name_constructor_exists():
    assert callable(Program::Type::Name.__init__)


def test_program::type::name_constructor_args():
    sig = inspect.signature(Program::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_function::return::value_is_not_abstract():
    assert not inspect.isabstract(Function::Return::Value)


def test_function::return::value_constructor_exists():
    assert callable(Function::Return::Value.__init__)


def test_function::return::value_constructor_args():
    sig = inspect.signature(Function::Return::Value.__init__)
    params = list(sig.parameters.keys())



def test_derived::function::name_is_not_abstract():
    assert not inspect.isabstract(Derived::Function::Name)


def test_derived::function::name_constructor_exists():
    assert callable(Derived::Function::Name.__init__)


def test_derived::function::name_constructor_args():
    sig = inspect.signature(Derived::Function::Name.__init__)
    params = list(sig.parameters.keys())



def test_function::block::vars_is_not_abstract():
    assert not inspect.isabstract(Function::Block::Vars)


def test_function::block::vars_constructor_exists():
    assert callable(Function::Block::Vars.__init__)


def test_function::block::vars_constructor_args():
    sig = inspect.signature(Function::Block::Vars.__init__)
    params = list(sig.parameters.keys())



def test_derived::function::block::name_is_not_abstract():
    assert not inspect.isabstract(Derived::Function::Block::Name)


def test_derived::function::block::name_constructor_exists():
    assert callable(Derived::Function::Block::Name.__init__)


def test_derived::function::block::name_constructor_args():
    sig = inspect.signature(Derived::Function::Block::Name.__init__)
    params = list(sig.parameters.keys())



def test_pous::function::block::type::name_is_not_abstract():
    assert not inspect.isabstract(pous::Function::Block::Type::Name)


def test_pous::function::block::type::name_constructor_exists():
    assert callable(pous::Function::Block::Type::Name.__init__)


def test_pous::function::block::type::name_constructor_args():
    sig = inspect.signature(pous::Function::Block::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_types::simple::specification_is_not_abstract():
    assert not inspect.isabstract(types::Simple::Specification)


def test_types::simple::specification_constructor_exists():
    assert callable(types::Simple::Specification.__init__)


def test_types::simple::specification_constructor_args():
    sig = inspect.signature(types::Simple::Specification.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::elementary::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::Elementary::Type::Name)


def test_iec61131::types::elementary::type::name_constructor_exists():
    assert callable(iec61131::types::Elementary::Type::Name.__init__)


def test_iec61131::types::elementary::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::Elementary::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::simple::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::Simple::Type::Name)


def test_iec61131::types::simple::type::name_constructor_exists():
    assert callable(iec61131::types::Simple::Type::Name.__init__)


def test_iec61131::types::simple::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::Simple::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::generic::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::Generic::Type::Name)


def test_iec61131::types::generic::type::name_constructor_exists():
    assert callable(iec61131::types::Generic::Type::Name.__init__)


def test_iec61131::types::generic::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::Generic::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_blocks_is_not_abstract():
    assert not inspect.isabstract(Blocks)


def test_blocks_constructor_exists():
    assert callable(Blocks.__init__)


def test_blocks_constructor_args():
    sig = inspect.signature(Blocks.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::derived::function::block::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Derived::Function::Block::Name)


def test_iec61131::pous::derived::function::block::name_constructor_exists():
    assert callable(iec61131::pous::Derived::Function::Block::Name.__init__)


def test_iec61131::pous::derived::function::block::name_constructor_args():
    sig = inspect.signature(iec61131::pous::Derived::Function::Block::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::derived::function::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Derived::Function::Name)


def test_iec61131::pous::derived::function::name_constructor_exists():
    assert callable(iec61131::pous::Derived::Function::Name.__init__)


def test_iec61131::pous::derived::function::name_constructor_args():
    sig = inspect.signature(iec61131::pous::Derived::Function::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::program::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Program::Type::Name)


def test_iec61131::pous::program::type::name_constructor_exists():
    assert callable(iec61131::pous::Program::Type::Name.__init__)


def test_iec61131::pous::program::type::name_constructor_args():
    sig = inspect.signature(iec61131::pous::Program::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_function::block::body_is_not_abstract():
    assert not inspect.isabstract(Function::Block::Body)


def test_function::block::body_constructor_exists():
    assert callable(Function::Block::Body.__init__)


def test_function::block::body_constructor_args():
    sig = inspect.signature(Function::Block::Body.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::sfc::sequential::function::chart_is_not_abstract():
    assert not inspect.isabstract(iec61131::sfc::Sequential::Function::Chart)


def test_iec61131::sfc::sequential::function::chart_constructor_exists():
    assert callable(iec61131::sfc::Sequential::Function::Chart.__init__)


def test_iec61131::sfc::sequential::function::chart_constructor_args():
    sig = inspect.signature(iec61131::sfc::Sequential::Function::Chart.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::initelement::array_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::InitElement::Array)


def test_iec61131::interfaces::initelement::array_constructor_exists():
    assert callable(iec61131::interfaces::InitElement::Array.__init__)


def test_iec61131::interfaces::initelement::array_constructor_args():
    sig = inspect.signature(iec61131::interfaces::InitElement::Array.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::temp::var::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Temp::Var::Declaration)


def test_iec61131::interfaces::temp::var::declaration_constructor_exists():
    assert callable(iec61131::interfaces::Temp::Var::Declaration.__init__)


def test_iec61131::interfaces::temp::var::declaration_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Temp::Var::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::initelement::structure_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::InitElement::Structure)


def test_iec61131::interfaces::initelement::structure_constructor_exists():
    assert callable(iec61131::interfaces::InitElement::Structure.__init__)


def test_iec61131::interfaces::initelement::structure_constructor_args():
    sig = inspect.signature(iec61131::interfaces::InitElement::Structure.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::var1::specification::func_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Var1::Specification::Func)


def test_iec61131::interfaces::var1::specification::func_constructor_exists():
    assert callable(iec61131::interfaces::Var1::Specification::Func.__init__)


def test_iec61131::interfaces::var1::specification::func_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Var1::Specification::Func.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::simple::specification::func_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Simple::Specification::Func)


def test_iec61131::interfaces::simple::specification::func_constructor_exists():
    assert callable(iec61131::interfaces::Simple::Specification::Func.__init__)


def test_iec61131::interfaces::simple::specification::func_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Simple::Specification::Func.__init__)
    params = list(sig.parameters.keys())



def test_simple::specification::func_is_not_abstract():
    assert not inspect.isabstract(Simple::Specification::Func)


def test_simple::specification::func_constructor_exists():
    assert callable(Simple::Specification::Func.__init__)


def test_simple::specification::func_constructor_args():
    sig = inspect.signature(Simple::Specification::Func.__init__)
    params = list(sig.parameters.keys())



def test_var1::specification::func_is_not_abstract():
    assert not inspect.isabstract(Var1::Specification::Func)


def test_var1::specification::func_constructor_exists():
    assert callable(Var1::Specification::Func.__init__)


def test_var1::specification::func_constructor_args():
    sig = inspect.signature(Var1::Specification::Func.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::simple::spec::init::func_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Simple::Spec::Init::Func)


def test_iec61131::interfaces::simple::spec::init::func_constructor_exists():
    assert callable(iec61131::interfaces::Simple::Spec::Init::Func.__init__)


def test_iec61131::interfaces::simple::spec::init::func_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Simple::Spec::Init::Func.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::var::init::decl::func_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Var::Init::Decl::Func)


def test_iec61131::interfaces::var::init::decl::func_constructor_exists():
    assert callable(iec61131::interfaces::Var::Init::Decl::Func.__init__)


def test_iec61131::interfaces::var::init::decl::func_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Var::Init::Decl::Func.__init__)
    params = list(sig.parameters.keys())



def test_simple::spec::init_is_not_abstract():
    assert not inspect.isabstract(Simple::Spec::Init)


def test_simple::spec::init_constructor_exists():
    assert callable(Simple::Spec::Init.__init__)


def test_simple::spec::init_constructor_args():
    sig = inspect.signature(Simple::Spec::Init.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::var::name::decl_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Var::Name::Decl)


def test_iec61131::interfaces::var::name::decl_constructor_exists():
    assert callable(iec61131::interfaces::Var::Name::Decl.__init__)


def test_iec61131::interfaces::var::name::decl_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Var::Name::Decl.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::function::var::decl_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Function::Var::Decl)


def test_iec61131::interfaces::function::var::decl_constructor_exists():
    assert callable(iec61131::interfaces::Function::Var::Decl.__init__)


def test_iec61131::interfaces::function::var::decl_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Function::Var::Decl.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"

def test_iec61131::interfaces::function::var::decl_has_constant():
    assert hasattr(iec61131::interfaces::Function::Var::Decl, "constant")
    descriptor = None
    for klass in iec61131::interfaces::Function::Var::Decl.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_iec61131::interfaces::var2::init::decl_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Var2::Init::Decl)


def test_iec61131::interfaces::var2::init::decl_constructor_exists():
    assert callable(iec61131::interfaces::Var2::Init::Decl.__init__)


def test_iec61131::interfaces::var2::init::decl_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Var2::Init::Decl.__init__)
    params = list(sig.parameters.keys())



def test_array::type::name_is_not_abstract():
    assert not inspect.isabstract(Array::Type::Name)


def test_array::type::name_constructor_exists():
    assert callable(Array::Type::Name.__init__)


def test_array::type::name_constructor_args():
    sig = inspect.signature(Array::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::array::specification1_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Array::Specification1)


def test_iec61131::interfaces::array::specification1_constructor_exists():
    assert callable(iec61131::interfaces::Array::Specification1.__init__)


def test_iec61131::interfaces::array::specification1_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Array::Specification1.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::initelement::enumvalue_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::InitElement::EnumValue)


def test_iec61131::interfaces::initelement::enumvalue_constructor_exists():
    assert callable(iec61131::interfaces::InitElement::EnumValue.__init__)


def test_iec61131::interfaces::initelement::enumvalue_constructor_args():
    sig = inspect.signature(iec61131::interfaces::InitElement::EnumValue.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::initelement::constant_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::InitElement::Constant)


def test_iec61131::interfaces::initelement::constant_constructor_exists():
    assert callable(iec61131::interfaces::InitElement::Constant.__init__)


def test_iec61131::interfaces::initelement::constant_constructor_args():
    sig = inspect.signature(iec61131::interfaces::InitElement::Constant.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::initial::element_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Initial::Element)


def test_iec61131::interfaces::initial::element_constructor_exists():
    assert callable(iec61131::interfaces::Initial::Element.__init__)


def test_iec61131::interfaces::initial::element_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Initial::Element.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::array::initial::elements2_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Array::Initial::Elements2)


def test_iec61131::interfaces::array::initial::elements2_constructor_exists():
    assert callable(iec61131::interfaces::Array::Initial::Elements2.__init__)


def test_iec61131::interfaces::array::initial::elements2_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Array::Initial::Elements2.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::array::initial::elements1_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Array::Initial::Elements1)


def test_iec61131::interfaces::array::initial::elements1_constructor_exists():
    assert callable(iec61131::interfaces::Array::Initial::Elements1.__init__)


def test_iec61131::interfaces::array::initial::elements1_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Array::Initial::Elements1.__init__)
    params = list(sig.parameters.keys())



def test_non::generic::type::name_is_not_abstract():
    assert not inspect.isabstract(Non::Generic::Type::Name)


def test_non::generic::type::name_constructor_exists():
    assert callable(Non::Generic::Type::Name.__init__)


def test_non::generic::type::name_constructor_args():
    sig = inspect.signature(Non::Generic::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::derived::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::Derived::Type::Name)


def test_iec61131::types::derived::type::name_constructor_exists():
    assert callable(iec61131::types::Derived::Type::Name.__init__)


def test_iec61131::types::derived::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::Derived::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::array::specification2_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Array::Specification2)


def test_iec61131::interfaces::array::specification2_constructor_exists():
    assert callable(iec61131::interfaces::Array::Specification2.__init__)


def test_iec61131::interfaces::array::specification2_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Array::Specification2.__init__)
    params = list(sig.parameters.keys())



def test_global::var::decl_is_not_abstract():
    assert not inspect.isabstract(Global::Var::Decl)


def test_global::var::decl_constructor_exists():
    assert callable(Global::Var::Decl.__init__)


def test_global::var::decl_constructor_args():
    sig = inspect.signature(Global::Var::Decl.__init__)
    params = list(sig.parameters.keys())



def test_library::element::declaration_is_not_abstract():
    assert not inspect.isabstract(Library::Element::Declaration)


def test_library::element::declaration_constructor_exists():
    assert callable(Library::Element::Declaration.__init__)


def test_library::element::declaration_constructor_args():
    sig = inspect.signature(Library::Element::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::configuration::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Configuration::Declaration)


def test_iec61131::configurations::configuration::declaration_constructor_exists():
    assert callable(iec61131::configurations::Configuration::Declaration.__init__)


def test_iec61131::configurations::configuration::declaration_constructor_args():
    sig = inspect.signature(iec61131::configurations::Configuration::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::function::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Function::Declaration)


def test_iec61131::pous::function::declaration_constructor_exists():
    assert callable(iec61131::pous::Function::Declaration.__init__)


def test_iec61131::pous::function::declaration_constructor_args():
    sig = inspect.signature(iec61131::pous::Function::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::function::block::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Function::Block::Declaration)


def test_iec61131::pous::function::block::declaration_constructor_exists():
    assert callable(iec61131::pous::Function::Block::Declaration.__init__)


def test_iec61131::pous::function::block::declaration_constructor_args():
    sig = inspect.signature(iec61131::pous::Function::Block::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::resource::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Resource::Declaration)


def test_iec61131::configurations::resource::declaration_constructor_exists():
    assert callable(iec61131::configurations::Resource::Declaration.__init__)


def test_iec61131::configurations::resource::declaration_constructor_args():
    sig = inspect.signature(iec61131::configurations::Resource::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::data::type::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Data::Type::Declaration)


def test_iec61131::pous::data::type::declaration_constructor_exists():
    assert callable(iec61131::pous::Data::Type::Declaration.__init__)


def test_iec61131::pous::data::type::declaration_constructor_args():
    sig = inspect.signature(iec61131::pous::Data::Type::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::program::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Program::Declaration)


def test_iec61131::pous::program::declaration_constructor_exists():
    assert callable(iec61131::pous::Program::Declaration.__init__)


def test_iec61131::pous::program::declaration_constructor_args():
    sig = inspect.signature(iec61131::pous::Program::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::global::var::declarations_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Global::Var::Declarations)


def test_iec61131::interfaces::global::var::declarations_constructor_exists():
    assert callable(iec61131::interfaces::Global::Var::Declarations.__init__)


def test_iec61131::interfaces::global::var::declarations_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Global::Var::Declarations.__init__)
    params = list(sig.parameters.keys())
    assert "retain" in params, "Missing parameter 'retain'"
    assert "constant" in params, "Missing parameter 'constant'"

def test_iec61131::interfaces::global::var::declarations_has_retain():
    assert hasattr(iec61131::interfaces::Global::Var::Declarations, "retain")
    descriptor = None
    for klass in iec61131::interfaces::Global::Var::Declarations.__mro__:
        if "retain" in klass.__dict__:
            descriptor = klass.__dict__["retain"]
            break
    assert isinstance(descriptor, property)

def test_iec61131::interfaces::global::var::declarations_has_constant():
    assert hasattr(iec61131::interfaces::Global::Var::Declarations, "constant")
    descriptor = None
    for klass in iec61131::interfaces::Global::Var::Declarations.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_located::var::decl_is_not_abstract():
    assert not inspect.isabstract(Located::Var::Decl)


def test_located::var::decl_constructor_exists():
    assert callable(Located::Var::Decl.__init__)


def test_located::var::decl_constructor_args():
    sig = inspect.signature(Located::Var::Decl.__init__)
    params = list(sig.parameters.keys())



def test_program::vars_is_not_abstract():
    assert not inspect.isabstract(Program::Vars)


def test_program::vars_constructor_exists():
    assert callable(Program::Vars.__init__)


def test_program::vars_constructor_args():
    sig = inspect.signature(Program::Vars.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::program::access::decls_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Program::Access::Decls)


def test_iec61131::pous::program::access::decls_constructor_exists():
    assert callable(iec61131::pous::Program::Access::Decls.__init__)


def test_iec61131::pous::program::access::decls_constructor_args():
    sig = inspect.signature(iec61131::pous::Program::Access::Decls.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::located::var::declarations_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Located::Var::Declarations)


def test_iec61131::interfaces::located::var::declarations_constructor_exists():
    assert callable(iec61131::interfaces::Located::Var::Declarations.__init__)


def test_iec61131::interfaces::located::var::declarations_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Located::Var::Declarations.__init__)
    params = list(sig.parameters.keys())
    assert "retain" in params, "Missing parameter 'retain'"
    assert "constant" in params, "Missing parameter 'constant'"

def test_iec61131::interfaces::located::var::declarations_has_retain():
    assert hasattr(iec61131::interfaces::Located::Var::Declarations, "retain")
    descriptor = None
    for klass in iec61131::interfaces::Located::Var::Declarations.__mro__:
        if "retain" in klass.__dict__:
            descriptor = klass.__dict__["retain"]
            break
    assert isinstance(descriptor, property)

def test_iec61131::interfaces::located::var::declarations_has_constant():
    assert hasattr(iec61131::interfaces::Located::Var::Declarations, "constant")
    descriptor = None
    for klass in iec61131::interfaces::Located::Var::Declarations.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_iec61131::interfaces::enumerated::specification2_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Enumerated::Specification2)


def test_iec61131::interfaces::enumerated::specification2_constructor_exists():
    assert callable(iec61131::interfaces::Enumerated::Specification2.__init__)


def test_iec61131::interfaces::enumerated::specification2_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Enumerated::Specification2.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::enumerated::specification1_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Enumerated::Specification1)


def test_iec61131::interfaces::enumerated::specification1_constructor_exists():
    assert callable(iec61131::interfaces::Enumerated::Specification1.__init__)


def test_iec61131::interfaces::enumerated::specification1_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Enumerated::Specification1.__init__)
    params = list(sig.parameters.keys())



def test_subrange::type::name_is_not_abstract():
    assert not inspect.isabstract(Subrange::Type::Name)


def test_subrange::type::name_constructor_exists():
    assert callable(Subrange::Type::Name.__init__)


def test_subrange::type::name_constructor_args():
    sig = inspect.signature(Subrange::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::subrange::specification2_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Subrange::Specification2)


def test_iec61131::interfaces::subrange::specification2_constructor_exists():
    assert callable(iec61131::interfaces::Subrange::Specification2.__init__)


def test_iec61131::interfaces::subrange::specification2_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Subrange::Specification2.__init__)
    params = list(sig.parameters.keys())



def test_subrange_is_not_abstract():
    assert not inspect.isabstract(Subrange)


def test_subrange_constructor_exists():
    assert callable(Subrange.__init__)


def test_subrange_constructor_args():
    sig = inspect.signature(Subrange.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::subrange::specification1_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Subrange::Specification1)


def test_iec61131::interfaces::subrange::specification1_constructor_exists():
    assert callable(iec61131::interfaces::Subrange::Specification1.__init__)


def test_iec61131::interfaces::subrange::specification1_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Subrange::Specification1.__init__)
    params = list(sig.parameters.keys())



def test_double::byte::string::type::name_is_not_abstract():
    assert not inspect.isabstract(Double::Byte::String::Type::Name)


def test_double::byte::string::type::name_constructor_exists():
    assert callable(Double::Byte::String::Type::Name.__init__)


def test_double::byte::string::type::name_constructor_args():
    sig = inspect.signature(Double::Byte::String::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_single::byte::string::type::name_is_not_abstract():
    assert not inspect.isabstract(Single::Byte::String::Type::Name)


def test_single::byte::string::type::name_constructor_exists():
    assert callable(Single::Byte::String::Type::Name.__init__)


def test_single::byte::string::type::name_constructor_args():
    sig = inspect.signature(Single::Byte::String::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_byte::string_is_not_abstract():
    assert not inspect.isabstract(Byte::String)


def test_byte::string_constructor_exists():
    assert callable(Byte::String.__init__)


def test_byte::string_constructor_args():
    sig = inspect.signature(Byte::String.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::double::bstring_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Double::BString)


def test_iec61131::interfaces::double::bstring_constructor_exists():
    assert callable(iec61131::interfaces::Double::BString.__init__)


def test_iec61131::interfaces::double::bstring_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Double::BString.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::single::bstring_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Single::BString)


def test_iec61131::interfaces::single::bstring_constructor_exists():
    assert callable(iec61131::interfaces::Single::BString.__init__)


def test_iec61131::interfaces::single::bstring_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Single::BString.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::byte::string_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Byte::String)


def test_iec61131::interfaces::byte::string_constructor_exists():
    assert callable(iec61131::interfaces::Byte::String.__init__)


def test_iec61131::interfaces::byte::string_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Byte::String.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::range_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Range)


def test_iec61131::interfaces::range_constructor_exists():
    assert callable(iec61131::interfaces::Range.__init__)


def test_iec61131::interfaces::range_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Range.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::input::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Input::Declaration)


def test_iec61131::interfaces::input::declaration_constructor_exists():
    assert callable(iec61131::interfaces::Input::Declaration.__init__)


def test_iec61131::interfaces::input::declaration_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Input::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::global::var::location_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Global::Var::Location)


def test_iec61131::interfaces::global::var::location_constructor_exists():
    assert callable(iec61131::interfaces::Global::Var::Location.__init__)


def test_iec61131::interfaces::global::var::location_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Global::Var::Location.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::global::var::spec_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Global::Var::Spec)


def test_iec61131::interfaces::global::var::spec_constructor_exists():
    assert callable(iec61131::interfaces::Global::Var::Spec.__init__)


def test_iec61131::interfaces::global::var::spec_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Global::Var::Spec.__init__)
    params = list(sig.parameters.keys())



def test_external::specification_is_not_abstract():
    assert not inspect.isabstract(External::Specification)


def test_external::specification_constructor_exists():
    assert callable(External::Specification.__init__)


def test_external::specification_constructor_args():
    sig = inspect.signature(External::Specification.__init__)
    params = list(sig.parameters.keys())



def test_global::var::name_is_not_abstract():
    assert not inspect.isabstract(Global::Var::Name)


def test_global::var::name_constructor_exists():
    assert callable(Global::Var::Name.__init__)


def test_global::var::name_constructor_args():
    sig = inspect.signature(Global::Var::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::external::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::External::Declaration)


def test_iec61131::interfaces::external::declaration_constructor_exists():
    assert callable(iec61131::interfaces::External::Declaration.__init__)


def test_iec61131::interfaces::external::declaration_constructor_args():
    sig = inspect.signature(iec61131::interfaces::External::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_rnv::declarations_is_not_abstract():
    assert not inspect.isabstract(RNV::Declarations)


def test_rnv::declarations_constructor_exists():
    assert callable(RNV::Declarations.__init__)


def test_rnv::declarations_constructor_args():
    sig = inspect.signature(RNV::Declarations.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::var::declarations_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Var::Declarations)


def test_iec61131::interfaces::var::declarations_constructor_exists():
    assert callable(iec61131::interfaces::Var::Declarations.__init__)


def test_iec61131::interfaces::var::declarations_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Var::Declarations.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"

def test_iec61131::interfaces::var::declarations_has_constant():
    assert hasattr(iec61131::interfaces::Var::Declarations, "constant")
    descriptor = None
    for klass in iec61131::interfaces::Var::Declarations.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_iec61131::interfaces::non::retentive::var::declarations_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Non::Retentive::Var::Declarations)


def test_iec61131::interfaces::non::retentive::var::declarations_constructor_exists():
    assert callable(iec61131::interfaces::Non::Retentive::Var::Declarations.__init__)


def test_iec61131::interfaces::non::retentive::var::declarations_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Non::Retentive::Var::Declarations.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::retentive::var::declarations_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Retentive::Var::Declarations)


def test_iec61131::interfaces::retentive::var::declarations_constructor_exists():
    assert callable(iec61131::interfaces::Retentive::Var::Declarations.__init__)


def test_iec61131::interfaces::retentive::var::declarations_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Retentive::Var::Declarations.__init__)
    params = list(sig.parameters.keys())



def test_external::declaration_is_not_abstract():
    assert not inspect.isabstract(External::Declaration)


def test_external::declaration_constructor_exists():
    assert callable(External::Declaration.__init__)


def test_external::declaration_constructor_args():
    sig = inspect.signature(External::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_other::var::declaration_is_not_abstract():
    assert not inspect.isabstract(Other::Var::Declaration)


def test_other::var::declaration_constructor_exists():
    assert callable(Other::Var::Declaration.__init__)


def test_other::var::declaration_constructor_args():
    sig = inspect.signature(Other::Var::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::rnv::declarations_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::RNV::Declarations)


def test_iec61131::interfaces::rnv::declarations_constructor_exists():
    assert callable(iec61131::interfaces::RNV::Declarations.__init__)


def test_iec61131::interfaces::rnv::declarations_constructor_args():
    sig = inspect.signature(iec61131::interfaces::RNV::Declarations.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::temp::var::decls_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Temp::Var::Decls)


def test_iec61131::interfaces::temp::var::decls_constructor_exists():
    assert callable(iec61131::interfaces::Temp::Var::Decls.__init__)


def test_iec61131::interfaces::temp::var::decls_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Temp::Var::Decls.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::external::var::declarations_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::External::Var::Declarations)


def test_iec61131::interfaces::external::var::declarations_constructor_exists():
    assert callable(iec61131::interfaces::External::Var::Declarations.__init__)


def test_iec61131::interfaces::external::var::declarations_constructor_args():
    sig = inspect.signature(iec61131::interfaces::External::Var::Declarations.__init__)
    params = list(sig.parameters.keys())
    assert "constant" in params, "Missing parameter 'constant'"

def test_iec61131::interfaces::external::var::declarations_has_constant():
    assert hasattr(iec61131::interfaces::External::Var::Declarations, "constant")
    descriptor = None
    for klass in iec61131::interfaces::External::Var::Declarations.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_iec61131::interfaces::incompl::located::var::declarations_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Incompl::Located::Var::Declarations)


def test_iec61131::interfaces::incompl::located::var::declarations_constructor_exists():
    assert callable(iec61131::interfaces::Incompl::Located::Var::Declarations.__init__)


def test_iec61131::interfaces::incompl::located::var::declarations_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Incompl::Located::Var::Declarations.__init__)
    params = list(sig.parameters.keys())
    assert "retain" in params, "Missing parameter 'retain'"

def test_iec61131::interfaces::incompl::located::var::declarations_has_retain():
    assert hasattr(iec61131::interfaces::Incompl::Located::Var::Declarations, "retain")
    descriptor = None
    for klass in iec61131::interfaces::Incompl::Located::Var::Declarations.__mro__:
        if "retain" in klass.__dict__:
            descriptor = klass.__dict__["retain"]
            break
    assert isinstance(descriptor, property)



def test_operators::multiply::operator_is_not_abstract():
    assert not inspect.isabstract(operators::Multiply::Operator)


def test_operators::multiply::operator_constructor_exists():
    assert callable(operators::Multiply::Operator.__init__)


def test_operators::multiply::operator_constructor_args():
    sig = inspect.signature(operators::Multiply::Operator.__init__)
    params = list(sig.parameters.keys())



def test_operators::add::operator_is_not_abstract():
    assert not inspect.isabstract(operators::Add::Operator)


def test_operators::add::operator_constructor_exists():
    assert callable(operators::Add::Operator.__init__)


def test_operators::add::operator_constructor_args():
    sig = inspect.signature(operators::Add::Operator.__init__)
    params = list(sig.parameters.keys())



def test_operators::arithmetic::name_is_not_abstract():
    assert not inspect.isabstract(operators::Arithmetic::Name)


def test_operators::arithmetic::name_constructor_exists():
    assert callable(operators::Arithmetic::Name.__init__)


def test_operators::arithmetic::name_constructor_args():
    sig = inspect.signature(operators::Arithmetic::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::divide::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Divide::Name)


def test_iec61131::operators::divide::name_constructor_exists():
    assert callable(iec61131::operators::Divide::Name.__init__)


def test_iec61131::operators::divide::name_constructor_args():
    sig = inspect.signature(iec61131::operators::Divide::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::multiply::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Multiply::Name)


def test_iec61131::operators::multiply::name_constructor_exists():
    assert callable(iec61131::operators::Multiply::Name.__init__)


def test_iec61131::operators::multiply::name_constructor_args():
    sig = inspect.signature(iec61131::operators::Multiply::Name.__init__)
    params = list(sig.parameters.keys())



def test_operators::addition::operator_is_not_abstract():
    assert not inspect.isabstract(operators::Addition::Operator)


def test_operators::addition::operator_constructor_exists():
    assert callable(operators::Addition::Operator.__init__)


def test_operators::addition::operator_constructor_args():
    sig = inspect.signature(operators::Addition::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::addition::symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Addition::Symbol)


def test_iec61131::operators::addition::symbol_constructor_exists():
    assert callable(iec61131::operators::Addition::Symbol.__init__)


def test_iec61131::operators::addition::symbol_constructor_args():
    sig = inspect.signature(iec61131::operators::Addition::Symbol.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::addition::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Addition::Name)


def test_iec61131::operators::addition::name_constructor_exists():
    assert callable(iec61131::operators::Addition::Name.__init__)


def test_iec61131::operators::addition::name_constructor_args():
    sig = inspect.signature(iec61131::operators::Addition::Name.__init__)
    params = list(sig.parameters.keys())



def test_comparison::operator_is_not_abstract():
    assert not inspect.isabstract(Comparison::Operator)


def test_comparison::operator_constructor_exists():
    assert callable(Comparison::Operator.__init__)


def test_comparison::operator_constructor_args():
    sig = inspect.signature(Comparison::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::lessequal::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::LessEqual::Operator)


def test_iec61131::operators::lessequal::operator_constructor_exists():
    assert callable(iec61131::operators::LessEqual::Operator.__init__)


def test_iec61131::operators::lessequal::operator_constructor_args():
    sig = inspect.signature(iec61131::operators::LessEqual::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::greaterequal::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::GreaterEqual::Operator)


def test_iec61131::operators::greaterequal::operator_constructor_exists():
    assert callable(iec61131::operators::GreaterEqual::Operator.__init__)


def test_iec61131::operators::greaterequal::operator_constructor_args():
    sig = inspect.signature(iec61131::operators::GreaterEqual::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::greater::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Greater::Operator)


def test_iec61131::operators::greater::operator_constructor_exists():
    assert callable(iec61131::operators::Greater::Operator.__init__)


def test_iec61131::operators::greater::operator_constructor_args():
    sig = inspect.signature(iec61131::operators::Greater::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::less::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Less::Operator)


def test_iec61131::operators::less::operator_constructor_exists():
    assert callable(iec61131::operators::Less::Operator.__init__)


def test_iec61131::operators::less::operator_constructor_args():
    sig = inspect.signature(iec61131::operators::Less::Operator.__init__)
    params = list(sig.parameters.keys())



def test_il::expr::operator_is_not_abstract():
    assert not inspect.isabstract(Il::Expr::Operator)


def test_il::expr::operator_constructor_exists():
    assert callable(Il::Expr::Operator.__init__)


def test_il::expr::operator_constructor_args():
    sig = inspect.signature(Il::Expr::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::arithmetic::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Arithmetic::Name)


def test_iec61131::operators::arithmetic::name_constructor_exists():
    assert callable(iec61131::operators::Arithmetic::Name.__init__)


def test_iec61131::operators::arithmetic::name_constructor_args():
    sig = inspect.signature(iec61131::operators::Arithmetic::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::comparison::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Comparison::Name)


def test_iec61131::operators::comparison::name_constructor_exists():
    assert callable(iec61131::operators::Comparison::Name.__init__)


def test_iec61131::operators::comparison::name_constructor_args():
    sig = inspect.signature(iec61131::operators::Comparison::Name.__init__)
    params = list(sig.parameters.keys())



def test_operators::substraction::operator_is_not_abstract():
    assert not inspect.isabstract(operators::Substraction::Operator)


def test_operators::substraction::operator_constructor_exists():
    assert callable(operators::Substraction::Operator.__init__)


def test_operators::substraction::operator_constructor_args():
    sig = inspect.signature(operators::Substraction::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::substraction::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Substraction::Name)


def test_iec61131::operators::substraction::name_constructor_exists():
    assert callable(iec61131::operators::Substraction::Name.__init__)


def test_iec61131::operators::substraction::name_constructor_args():
    sig = inspect.signature(iec61131::operators::Substraction::Name.__init__)
    params = list(sig.parameters.keys())



def test_greaterequal::operator_is_not_abstract():
    assert not inspect.isabstract(GreaterEqual::Operator)


def test_greaterequal::operator_constructor_exists():
    assert callable(GreaterEqual::Operator.__init__)


def test_greaterequal::operator_constructor_args():
    sig = inspect.signature(GreaterEqual::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::greaterequal::symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::GreaterEqual::Symbol)


def test_iec61131::operators::greaterequal::symbol_constructor_exists():
    assert callable(iec61131::operators::GreaterEqual::Symbol.__init__)


def test_iec61131::operators::greaterequal::symbol_constructor_args():
    sig = inspect.signature(iec61131::operators::GreaterEqual::Symbol.__init__)
    params = list(sig.parameters.keys())



def test_operators::greaterequal::operator_is_not_abstract():
    assert not inspect.isabstract(operators::GreaterEqual::Operator)


def test_operators::greaterequal::operator_constructor_exists():
    assert callable(operators::GreaterEqual::Operator.__init__)


def test_operators::greaterequal::operator_constructor_args():
    sig = inspect.signature(operators::GreaterEqual::Operator.__init__)
    params = list(sig.parameters.keys())



def test_greater::operator_is_not_abstract():
    assert not inspect.isabstract(Greater::Operator)


def test_greater::operator_constructor_exists():
    assert callable(Greater::Operator.__init__)


def test_greater::operator_constructor_args():
    sig = inspect.signature(Greater::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::greater::symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Greater::Symbol)


def test_iec61131::operators::greater::symbol_constructor_exists():
    assert callable(iec61131::operators::Greater::Symbol.__init__)


def test_iec61131::operators::greater::symbol_constructor_args():
    sig = inspect.signature(iec61131::operators::Greater::Symbol.__init__)
    params = list(sig.parameters.keys())



def test_operators::greater::operator_is_not_abstract():
    assert not inspect.isabstract(operators::Greater::Operator)


def test_operators::greater::operator_constructor_exists():
    assert callable(operators::Greater::Operator.__init__)


def test_operators::greater::operator_constructor_args():
    sig = inspect.signature(operators::Greater::Operator.__init__)
    params = list(sig.parameters.keys())



def test_lessequal::operator_is_not_abstract():
    assert not inspect.isabstract(LessEqual::Operator)


def test_lessequal::operator_constructor_exists():
    assert callable(LessEqual::Operator.__init__)


def test_lessequal::operator_constructor_args():
    sig = inspect.signature(LessEqual::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::lessequal::symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::LessEqual::Symbol)


def test_iec61131::operators::lessequal::symbol_constructor_exists():
    assert callable(iec61131::operators::LessEqual::Symbol.__init__)


def test_iec61131::operators::lessequal::symbol_constructor_args():
    sig = inspect.signature(iec61131::operators::LessEqual::Symbol.__init__)
    params = list(sig.parameters.keys())



def test_operators::lessequal::operator_is_not_abstract():
    assert not inspect.isabstract(operators::LessEqual::Operator)


def test_operators::lessequal::operator_constructor_exists():
    assert callable(operators::LessEqual::Operator.__init__)


def test_operators::lessequal::operator_constructor_args():
    sig = inspect.signature(operators::LessEqual::Operator.__init__)
    params = list(sig.parameters.keys())



def test_less::operator_is_not_abstract():
    assert not inspect.isabstract(Less::Operator)


def test_less::operator_constructor_exists():
    assert callable(Less::Operator.__init__)


def test_less::operator_constructor_args():
    sig = inspect.signature(Less::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::less::symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Less::Symbol)


def test_iec61131::operators::less::symbol_constructor_exists():
    assert callable(iec61131::operators::Less::Symbol.__init__)


def test_iec61131::operators::less::symbol_constructor_args():
    sig = inspect.signature(iec61131::operators::Less::Symbol.__init__)
    params = list(sig.parameters.keys())



def test_operators::less::operator_is_not_abstract():
    assert not inspect.isabstract(operators::Less::Operator)


def test_operators::less::operator_constructor_exists():
    assert callable(operators::Less::Operator.__init__)


def test_operators::less::operator_constructor_args():
    sig = inspect.signature(operators::Less::Operator.__init__)
    params = list(sig.parameters.keys())



def test_unequal::operator_is_not_abstract():
    assert not inspect.isabstract(Unequal::Operator)


def test_unequal::operator_constructor_exists():
    assert callable(Unequal::Operator.__init__)


def test_unequal::operator_constructor_args():
    sig = inspect.signature(Unequal::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::unequal::symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Unequal::Symbol)


def test_iec61131::operators::unequal::symbol_constructor_exists():
    assert callable(iec61131::operators::Unequal::Symbol.__init__)


def test_iec61131::operators::unequal::symbol_constructor_args():
    sig = inspect.signature(iec61131::operators::Unequal::Symbol.__init__)
    params = list(sig.parameters.keys())



def test_operators::unequal::operator_is_not_abstract():
    assert not inspect.isabstract(operators::Unequal::Operator)


def test_operators::unequal::operator_constructor_exists():
    assert callable(operators::Unequal::Operator.__init__)


def test_operators::unequal::operator_constructor_args():
    sig = inspect.signature(operators::Unequal::Operator.__init__)
    params = list(sig.parameters.keys())



def test_equal::operator_is_not_abstract():
    assert not inspect.isabstract(Equal::Operator)


def test_equal::operator_constructor_exists():
    assert callable(Equal::Operator.__init__)


def test_equal::operator_constructor_args():
    sig = inspect.signature(Equal::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::equal::symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Equal::Symbol)


def test_iec61131::operators::equal::symbol_constructor_exists():
    assert callable(iec61131::operators::Equal::Symbol.__init__)


def test_iec61131::operators::equal::symbol_constructor_args():
    sig = inspect.signature(iec61131::operators::Equal::Symbol.__init__)
    params = list(sig.parameters.keys())



def test_operators::comparison::name_is_not_abstract():
    assert not inspect.isabstract(operators::Comparison::Name)


def test_operators::comparison::name_constructor_exists():
    assert callable(operators::Comparison::Name.__init__)


def test_operators::comparison::name_constructor_args():
    sig = inspect.signature(operators::Comparison::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::unequal::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Unequal::Name)


def test_iec61131::operators::unequal::name_constructor_exists():
    assert callable(iec61131::operators::Unequal::Name.__init__)


def test_iec61131::operators::unequal::name_constructor_args():
    sig = inspect.signature(iec61131::operators::Unequal::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::greaterequal::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::GreaterEqual::Name)


def test_iec61131::operators::greaterequal::name_constructor_exists():
    assert callable(iec61131::operators::GreaterEqual::Name.__init__)


def test_iec61131::operators::greaterequal::name_constructor_args():
    sig = inspect.signature(iec61131::operators::GreaterEqual::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::greater::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Greater::Name)


def test_iec61131::operators::greater::name_constructor_exists():
    assert callable(iec61131::operators::Greater::Name.__init__)


def test_iec61131::operators::greater::name_constructor_args():
    sig = inspect.signature(iec61131::operators::Greater::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::lessequal::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::LessEqual::Name)


def test_iec61131::operators::lessequal::name_constructor_exists():
    assert callable(iec61131::operators::LessEqual::Name.__init__)


def test_iec61131::operators::lessequal::name_constructor_args():
    sig = inspect.signature(iec61131::operators::LessEqual::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::less::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Less::Name)


def test_iec61131::operators::less::name_constructor_exists():
    assert callable(iec61131::operators::Less::Name.__init__)


def test_iec61131::operators::less::name_constructor_args():
    sig = inspect.signature(iec61131::operators::Less::Name.__init__)
    params = list(sig.parameters.keys())



def test_operators::equal::operator_is_not_abstract():
    assert not inspect.isabstract(operators::Equal::Operator)


def test_operators::equal::operator_constructor_exists():
    assert callable(operators::Equal::Operator.__init__)


def test_operators::equal::operator_constructor_args():
    sig = inspect.signature(operators::Equal::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::equal::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Equal::Name)


def test_iec61131::operators::equal::name_constructor_exists():
    assert callable(iec61131::operators::Equal::Name.__init__)


def test_iec61131::operators::equal::name_constructor_args():
    sig = inspect.signature(iec61131::operators::Equal::Name.__init__)
    params = list(sig.parameters.keys())



def test_and::operator_is_not_abstract():
    assert not inspect.isabstract(And::Operator)


def test_and::operator_constructor_exists():
    assert callable(And::Operator.__init__)


def test_and::operator_constructor_args():
    sig = inspect.signature(And::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::and::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::And::Name)


def test_iec61131::operators::and::name_constructor_exists():
    assert callable(iec61131::operators::And::Name.__init__)


def test_iec61131::operators::and::name_constructor_args():
    sig = inspect.signature(iec61131::operators::And::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::and::symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::And::Symbol)


def test_iec61131::operators::and::symbol_constructor_exists():
    assert callable(iec61131::operators::And::Symbol.__init__)


def test_iec61131::operators::and::symbol_constructor_args():
    sig = inspect.signature(iec61131::operators::And::Symbol.__init__)
    params = list(sig.parameters.keys())



def test_assignment::operator_is_not_abstract():
    assert not inspect.isabstract(Assignment::Operator)


def test_assignment::operator_constructor_exists():
    assert callable(Assignment::Operator.__init__)


def test_assignment::operator_constructor_args():
    sig = inspect.signature(Assignment::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::assignment::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Assignment::Name)


def test_iec61131::operators::assignment::name_constructor_exists():
    assert callable(iec61131::operators::Assignment::Name.__init__)


def test_iec61131::operators::assignment::name_constructor_args():
    sig = inspect.signature(iec61131::operators::Assignment::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::assignment::symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Assignment::Symbol)


def test_iec61131::operators::assignment::symbol_constructor_exists():
    assert callable(iec61131::operators::Assignment::Symbol.__init__)


def test_iec61131::operators::assignment::symbol_constructor_args():
    sig = inspect.signature(iec61131::operators::Assignment::Symbol.__init__)
    params = list(sig.parameters.keys())



def test_power::operator_is_not_abstract():
    assert not inspect.isabstract(Power::Operator)


def test_power::operator_constructor_exists():
    assert callable(Power::Operator.__init__)


def test_power::operator_constructor_args():
    sig = inspect.signature(Power::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::power::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Power::Name)


def test_iec61131::operators::power::name_constructor_exists():
    assert callable(iec61131::operators::Power::Name.__init__)


def test_iec61131::operators::power::name_constructor_args():
    sig = inspect.signature(iec61131::operators::Power::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::power::symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Power::Symbol)


def test_iec61131::operators::power::symbol_constructor_exists():
    assert callable(iec61131::operators::Power::Symbol.__init__)


def test_iec61131::operators::power::symbol_constructor_args():
    sig = inspect.signature(iec61131::operators::Power::Symbol.__init__)
    params = list(sig.parameters.keys())



def test_divide::operator_is_not_abstract():
    assert not inspect.isabstract(Divide::Operator)


def test_divide::operator_constructor_exists():
    assert callable(Divide::Operator.__init__)


def test_divide::operator_constructor_args():
    sig = inspect.signature(Divide::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::divide::symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Divide::Symbol)


def test_iec61131::operators::divide::symbol_constructor_exists():
    assert callable(iec61131::operators::Divide::Symbol.__init__)


def test_iec61131::operators::divide::symbol_constructor_args():
    sig = inspect.signature(iec61131::operators::Divide::Symbol.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::integer_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Integer)


def test_iec61131::literals::integer_constructor_exists():
    assert callable(iec61131::literals::Integer.__init__)


def test_iec61131::literals::integer_constructor_args():
    sig = inspect.signature(iec61131::literals::Integer.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iec61131::literals::integer_has_value():
    assert hasattr(iec61131::literals::Integer, "value")
    descriptor = None
    for klass in iec61131::literals::Integer.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iec61131::literals::bsinteger_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::BSInteger)


def test_iec61131::literals::bsinteger_constructor_exists():
    assert callable(iec61131::literals::BSInteger.__init__)


def test_iec61131::literals::bsinteger_constructor_args():
    sig = inspect.signature(iec61131::literals::BSInteger.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::date::literal_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Date::Literal)


def test_iec61131::literals::date::literal_constructor_exists():
    assert callable(iec61131::literals::Date::Literal.__init__)


def test_iec61131::literals::date::literal_constructor_args():
    sig = inspect.signature(iec61131::literals::Date::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "month" in params, "Missing parameter 'month'"
    assert "day" in params, "Missing parameter 'day'"
    assert "year" in params, "Missing parameter 'year'"

def test_iec61131::literals::date::literal_has_month():
    assert hasattr(iec61131::literals::Date::Literal, "month")
    descriptor = None
    for klass in iec61131::literals::Date::Literal.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_iec61131::literals::date::literal_has_day():
    assert hasattr(iec61131::literals::Date::Literal, "day")
    descriptor = None
    for klass in iec61131::literals::Date::Literal.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_iec61131::literals::date::literal_has_year():
    assert hasattr(iec61131::literals::Date::Literal, "year")
    descriptor = None
    for klass in iec61131::literals::Date::Literal.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_iec61131::literals::daytime_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Daytime)


def test_iec61131::literals::daytime_constructor_exists():
    assert callable(iec61131::literals::Daytime.__init__)


def test_iec61131::literals::daytime_constructor_args():
    sig = inspect.signature(iec61131::literals::Daytime.__init__)
    params = list(sig.parameters.keys())
    assert "hour" in params, "Missing parameter 'hour'"
    assert "minute" in params, "Missing parameter 'minute'"

def test_iec61131::literals::daytime_has_hour():
    assert hasattr(iec61131::literals::Daytime, "hour")
    descriptor = None
    for klass in iec61131::literals::Daytime.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)

def test_iec61131::literals::daytime_has_minute():
    assert hasattr(iec61131::literals::Daytime, "minute")
    descriptor = None
    for klass in iec61131::literals::Daytime.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)



def test_iec61131::literals::fixed::point::literal_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Fixed::Point::Literal)


def test_iec61131::literals::fixed::point::literal_constructor_exists():
    assert callable(iec61131::literals::Fixed::Point::Literal.__init__)


def test_iec61131::literals::fixed::point::literal_constructor_args():
    sig = inspect.signature(iec61131::literals::Fixed::Point::Literal.__init__)
    params = list(sig.parameters.keys())



def test_double::byte::character::representation_is_not_abstract():
    assert not inspect.isabstract(Double::Byte::Character::Representation)


def test_double::byte::character::representation_constructor_exists():
    assert callable(Double::Byte::Character::Representation.__init__)


def test_double::byte::character::representation_constructor_args():
    sig = inspect.signature(Double::Byte::Character::Representation.__init__)
    params = list(sig.parameters.keys())



def test_operators::dot::operator_is_not_abstract():
    assert not inspect.isabstract(operators::Dot::Operator)


def test_operators::dot::operator_constructor_exists():
    assert callable(operators::Dot::Operator.__init__)


def test_operators::dot::operator_constructor_args():
    sig = inspect.signature(operators::Dot::Operator.__init__)
    params = list(sig.parameters.keys())



def test_il::il::simple::operator_is_not_abstract():
    assert not inspect.isabstract(il::Il::Simple::Operator)


def test_il::il::simple::operator_constructor_exists():
    assert callable(il::Il::Simple::Operator.__init__)


def test_il::il::simple::operator_constructor_args():
    sig = inspect.signature(il::Il::Simple::Operator.__init__)
    params = list(sig.parameters.keys())



def test_operators::unary::operator_is_not_abstract():
    assert not inspect.isabstract(operators::Unary::Operator)


def test_operators::unary::operator_constructor_exists():
    assert callable(operators::Unary::Operator.__init__)


def test_operators::unary::operator_constructor_args():
    sig = inspect.signature(operators::Unary::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::substraction::symbol_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Substraction::Symbol)


def test_iec61131::operators::substraction::symbol_constructor_exists():
    assert callable(iec61131::operators::Substraction::Symbol.__init__)


def test_iec61131::operators::substraction::symbol_constructor_args():
    sig = inspect.signature(iec61131::operators::Substraction::Symbol.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::not::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Not::Operator)


def test_iec61131::operators::not::operator_constructor_exists():
    assert callable(iec61131::operators::Not::Operator.__init__)


def test_iec61131::operators::not::operator_constructor_args():
    sig = inspect.signature(iec61131::operators::Not::Operator.__init__)
    params = list(sig.parameters.keys())



def test_il::il::expr::operator_is_not_abstract():
    assert not inspect.isabstract(il::Il::Expr::Operator)


def test_il::il::expr::operator_constructor_exists():
    assert callable(il::Il::Expr::Operator.__init__)


def test_il::il::expr::operator_constructor_args():
    sig = inspect.signature(il::Il::Expr::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::modulo::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Modulo::Operator)


def test_iec61131::operators::modulo::operator_constructor_exists():
    assert callable(iec61131::operators::Modulo::Operator.__init__)


def test_iec61131::operators::modulo::operator_constructor_args():
    sig = inspect.signature(iec61131::operators::Modulo::Operator.__init__)
    params = list(sig.parameters.keys())



def test_operators::operator_is_not_abstract():
    assert not inspect.isabstract(operators::Operator)


def test_operators::operator_constructor_exists():
    assert callable(operators::Operator.__init__)


def test_operators::operator_constructor_args():
    sig = inspect.signature(operators::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::xor::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Xor::Operator)


def test_iec61131::operators::xor::operator_constructor_exists():
    assert callable(iec61131::operators::Xor::Operator.__init__)


def test_iec61131::operators::xor::operator_constructor_args():
    sig = inspect.signature(iec61131::operators::Xor::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::or::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Or::Operator)


def test_iec61131::operators::or::operator_constructor_exists():
    assert callable(iec61131::operators::Or::Operator.__init__)


def test_iec61131::operators::or::operator_constructor_args():
    sig = inspect.signature(iec61131::operators::Or::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::and::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::And::Operator)


def test_iec61131::operators::and::operator_constructor_exists():
    assert callable(iec61131::operators::And::Operator.__init__)


def test_iec61131::operators::and::operator_constructor_args():
    sig = inspect.signature(iec61131::operators::And::Operator.__init__)
    params = list(sig.parameters.keys())



def test_equuequ::operator_is_not_abstract():
    assert not inspect.isabstract(EquUequ::Operator)


def test_equuequ::operator_constructor_exists():
    assert callable(EquUequ::Operator.__init__)


def test_equuequ::operator_constructor_args():
    sig = inspect.signature(EquUequ::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::unequal::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Unequal::Operator)


def test_iec61131::operators::unequal::operator_constructor_exists():
    assert callable(iec61131::operators::Unequal::Operator.__init__)


def test_iec61131::operators::unequal::operator_constructor_args():
    sig = inspect.signature(iec61131::operators::Unequal::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::equal::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Equal::Operator)


def test_iec61131::operators::equal::operator_constructor_exists():
    assert callable(iec61131::operators::Equal::Operator.__init__)


def test_iec61131::operators::equal::operator_constructor_args():
    sig = inspect.signature(iec61131::operators::Equal::Operator.__init__)
    params = list(sig.parameters.keys())



def test_dot::operator_is_not_abstract():
    assert not inspect.isabstract(Dot::Operator)


def test_dot::operator_constructor_exists():
    assert callable(Dot::Operator.__init__)


def test_dot::operator_constructor_args():
    sig = inspect.signature(Dot::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::divide::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Divide::Operator)


def test_iec61131::operators::divide::operator_constructor_exists():
    assert callable(iec61131::operators::Divide::Operator.__init__)


def test_iec61131::operators::divide::operator_constructor_args():
    sig = inspect.signature(iec61131::operators::Divide::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::multiply::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Multiply::Operator)


def test_iec61131::operators::multiply::operator_constructor_exists():
    assert callable(iec61131::operators::Multiply::Operator.__init__)


def test_iec61131::operators::multiply::operator_constructor_args():
    sig = inspect.signature(iec61131::operators::Multiply::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::substraction::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Substraction::Operator)


def test_iec61131::operators::substraction::operator_constructor_exists():
    assert callable(iec61131::operators::Substraction::Operator.__init__)


def test_iec61131::operators::substraction::operator_constructor_args():
    sig = inspect.signature(iec61131::operators::Substraction::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::addition::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Addition::Operator)


def test_iec61131::operators::addition::operator_constructor_exists():
    assert callable(iec61131::operators::Addition::Operator.__init__)


def test_iec61131::operators::addition::operator_constructor_args():
    sig = inspect.signature(iec61131::operators::Addition::Operator.__init__)
    params = list(sig.parameters.keys())



def test_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::dot::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Dot::Operator)


def test_iec61131::operators::dot::operator_constructor_exists():
    assert callable(iec61131::operators::Dot::Operator.__init__)


def test_iec61131::operators::dot::operator_constructor_args():
    sig = inspect.signature(iec61131::operators::Dot::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::equuequ::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::EquUequ::Operator)


def test_iec61131::operators::equuequ::operator_constructor_exists():
    assert callable(iec61131::operators::EquUequ::Operator.__init__)


def test_iec61131::operators::equuequ::operator_constructor_args():
    sig = inspect.signature(iec61131::operators::EquUequ::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::unary::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Unary::Operator)


def test_iec61131::operators::unary::operator_constructor_exists():
    assert callable(iec61131::operators::Unary::Operator.__init__)


def test_iec61131::operators::unary::operator_constructor_args():
    sig = inspect.signature(iec61131::operators::Unary::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::comparison::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Comparison::Operator)


def test_iec61131::operators::comparison::operator_constructor_exists():
    assert callable(iec61131::operators::Comparison::Operator.__init__)


def test_iec61131::operators::comparison::operator_constructor_args():
    sig = inspect.signature(iec61131::operators::Comparison::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::assignment::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Assignment::Operator)


def test_iec61131::operators::assignment::operator_constructor_exists():
    assert callable(iec61131::operators::Assignment::Operator.__init__)


def test_iec61131::operators::assignment::operator_constructor_args():
    sig = inspect.signature(iec61131::operators::Assignment::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::power::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Power::Operator)


def test_iec61131::operators::power::operator_constructor_exists():
    assert callable(iec61131::operators::Power::Operator.__init__)


def test_iec61131::operators::power::operator_constructor_args():
    sig = inspect.signature(iec61131::operators::Power::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::add::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Add::Operator)


def test_iec61131::operators::add::operator_constructor_exists():
    assert callable(iec61131::operators::Add::Operator.__init__)


def test_iec61131::operators::add::operator_constructor_args():
    sig = inspect.signature(iec61131::operators::Add::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::operators::operator_is_not_abstract():
    assert not inspect.isabstract(iec61131::operators::Operator)


def test_iec61131::operators::operator_constructor_exists():
    assert callable(iec61131::operators::Operator.__init__)


def test_iec61131::operators::operator_constructor_args():
    sig = inspect.signature(iec61131::operators::Operator.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::double::byte::character::representation_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Double::Byte::Character::Representation)


def test_iec61131::literals::double::byte::character::representation_constructor_exists():
    assert callable(iec61131::literals::Double::Byte::Character::Representation.__init__)


def test_iec61131::literals::double::byte::character::representation_constructor_args():
    sig = inspect.signature(iec61131::literals::Double::Byte::Character::Representation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iec61131::literals::double::byte::character::representation_has_value():
    assert hasattr(iec61131::literals::Double::Byte::Character::Representation, "value")
    descriptor = None
    for klass in iec61131::literals::Double::Byte::Character::Representation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_common::character::representation_is_not_abstract():
    assert not inspect.isabstract(Common::Character::Representation)


def test_common::character::representation_constructor_exists():
    assert callable(Common::Character::Representation.__init__)


def test_common::character::representation_constructor_args():
    sig = inspect.signature(Common::Character::Representation.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::single::byte::character::representation_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Single::Byte::Character::Representation)


def test_iec61131::literals::single::byte::character::representation_constructor_exists():
    assert callable(iec61131::literals::Single::Byte::Character::Representation.__init__)


def test_iec61131::literals::single::byte::character::representation_constructor_args():
    sig = inspect.signature(iec61131::literals::Single::Byte::Character::Representation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iec61131::literals::single::byte::character::representation_has_value():
    assert hasattr(iec61131::literals::Single::Byte::Character::Representation, "value")
    descriptor = None
    for klass in iec61131::literals::Single::Byte::Character::Representation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iec61131::literals::common::character::representation_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Common::Character::Representation)


def test_iec61131::literals::common::character::representation_constructor_exists():
    assert callable(iec61131::literals::Common::Character::Representation.__init__)


def test_iec61131::literals::common::character::representation_constructor_args():
    sig = inspect.signature(iec61131::literals::Common::Character::Representation.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iec61131::literals::common::character::representation_has_value():
    assert hasattr(iec61131::literals::Common::Character::Representation, "value")
    descriptor = None
    for klass in iec61131::literals::Common::Character::Representation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_dt::type::name_is_not_abstract():
    assert not inspect.isabstract(DT::Type::Name)


def test_dt::type::name_constructor_exists():
    assert callable(DT::Type::Name.__init__)


def test_dt::type::name_constructor_args():
    sig = inspect.signature(DT::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_date::literal_is_not_abstract():
    assert not inspect.isabstract(Date::Literal)


def test_date::literal_constructor_exists():
    assert callable(Date::Literal.__init__)


def test_date::literal_constructor_args():
    sig = inspect.signature(Date::Literal.__init__)
    params = list(sig.parameters.keys())



def test_date::type::name_is_not_abstract():
    assert not inspect.isabstract(Date::Type::Name)


def test_date::type::name_constructor_exists():
    assert callable(Date::Type::Name.__init__)


def test_date::type::name_constructor_args():
    sig = inspect.signature(Date::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::dt::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::DT::Type::Name)


def test_iec61131::types::dt::type::name_constructor_exists():
    assert callable(iec61131::types::DT::Type::Name.__init__)


def test_iec61131::types::dt::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::DT::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::tod::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::TOD::Type::Name)


def test_iec61131::types::tod::type::name_constructor_exists():
    assert callable(iec61131::types::TOD::Type::Name.__init__)


def test_iec61131::types::tod::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::TOD::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_single::byte::character::representation_is_not_abstract():
    assert not inspect.isabstract(Single::Byte::Character::Representation)


def test_single::byte::character::representation_constructor_exists():
    assert callable(Single::Byte::Character::Representation.__init__)


def test_single::byte::character::representation_constructor_args():
    sig = inspect.signature(Single::Byte::Character::Representation.__init__)
    params = list(sig.parameters.keys())



def test_character::string_is_not_abstract():
    assert not inspect.isabstract(Character::String)


def test_character::string_constructor_exists():
    assert callable(Character::String.__init__)


def test_character::string_constructor_args():
    sig = inspect.signature(Character::String.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::double::byte::character::string_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Double::Byte::Character::String)


def test_iec61131::literals::double::byte::character::string_constructor_exists():
    assert callable(iec61131::literals::Double::Byte::Character::String.__init__)


def test_iec61131::literals::double::byte::character::string_constructor_args():
    sig = inspect.signature(iec61131::literals::Double::Byte::Character::String.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::single::byte::character::string_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Single::Byte::Character::String)


def test_iec61131::literals::single::byte::character::string_constructor_exists():
    assert callable(iec61131::literals::Single::Byte::Character::String.__init__)


def test_iec61131::literals::single::byte::character::string_constructor_args():
    sig = inspect.signature(iec61131::literals::Single::Byte::Character::String.__init__)
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



def test_unsigned::integer_is_not_abstract():
    assert not inspect.isabstract(Unsigned::Integer)


def test_unsigned::integer_constructor_exists():
    assert callable(Unsigned::Integer.__init__)


def test_unsigned::integer_constructor_args():
    sig = inspect.signature(Unsigned::Integer.__init__)
    params = list(sig.parameters.keys())



def test_fixed::point::literal_is_not_abstract():
    assert not inspect.isabstract(Fixed::Point::Literal)


def test_fixed::point::literal_constructor_exists():
    assert callable(Fixed::Point::Literal.__init__)


def test_fixed::point::literal_constructor_args():
    sig = inspect.signature(Fixed::Point::Literal.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::fixed::point_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Fixed::Point)


def test_iec61131::literals::fixed::point_constructor_exists():
    assert callable(iec61131::literals::Fixed::Point.__init__)


def test_iec61131::literals::fixed::point_constructor_args():
    sig = inspect.signature(iec61131::literals::Fixed::Point.__init__)
    params = list(sig.parameters.keys())
    assert "valuePre" in params, "Missing parameter 'valuePre'"
    assert "valuePost" in params, "Missing parameter 'valuePost'"

def test_iec61131::literals::fixed::point_has_valuePre():
    assert hasattr(iec61131::literals::Fixed::Point, "valuePre")
    descriptor = None
    for klass in iec61131::literals::Fixed::Point.__mro__:
        if "valuePre" in klass.__dict__:
            descriptor = klass.__dict__["valuePre"]
            break
    assert isinstance(descriptor, property)

def test_iec61131::literals::fixed::point_has_valuePost():
    assert hasattr(iec61131::literals::Fixed::Point, "valuePost")
    descriptor = None
    for klass in iec61131::literals::Fixed::Point.__mro__:
        if "valuePost" in klass.__dict__:
            descriptor = klass.__dict__["valuePost"]
            break
    assert isinstance(descriptor, property)



def test_iec61131::literals::interval_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Interval)


def test_iec61131::literals::interval_constructor_exists():
    assert callable(iec61131::literals::Interval.__init__)


def test_iec61131::literals::interval_constructor_args():
    sig = inspect.signature(iec61131::literals::Interval.__init__)
    params = list(sig.parameters.keys())



def test_literals::fixed::point::literal_is_not_abstract():
    assert not inspect.isabstract(literals::Fixed::Point::Literal)


def test_literals::fixed::point::literal_constructor_exists():
    assert callable(literals::Fixed::Point::Literal.__init__)


def test_literals::fixed::point::literal_constructor_args():
    sig = inspect.signature(literals::Fixed::Point::Literal.__init__)
    params = list(sig.parameters.keys())



def test_integer_is_not_abstract():
    assert not inspect.isabstract(Integer)


def test_integer_constructor_exists():
    assert callable(Integer.__init__)


def test_integer_constructor_args():
    sig = inspect.signature(Integer.__init__)
    params = list(sig.parameters.keys())



def test_numeric::literal_is_not_abstract():
    assert not inspect.isabstract(Numeric::Literal)


def test_numeric::literal_constructor_exists():
    assert callable(Numeric::Literal.__init__)


def test_numeric::literal_constructor_args():
    sig = inspect.signature(Numeric::Literal.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::integer::literal_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Integer::Literal)


def test_iec61131::literals::integer::literal_constructor_exists():
    assert callable(iec61131::literals::Integer::Literal.__init__)


def test_iec61131::literals::integer::literal_constructor_args():
    sig = inspect.signature(iec61131::literals::Integer::Literal.__init__)
    params = list(sig.parameters.keys())



def test_bit::string::type::name_is_not_abstract():
    assert not inspect.isabstract(Bit::String::Type::Name)


def test_bit::string::type::name_constructor_exists():
    assert callable(Bit::String::Type::Name.__init__)


def test_bit::string::type::name_constructor_args():
    sig = inspect.signature(Bit::String::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::bool::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::Bool::Type::Name)


def test_iec61131::types::bool::type::name_constructor_exists():
    assert callable(iec61131::types::Bool::Type::Name.__init__)


def test_iec61131::types::bool::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::Bool::Type::Name.__init__)
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



def test_iec61131::literals::bit::string::literal_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Bit::String::Literal)


def test_iec61131::literals::bit::string::literal_constructor_exists():
    assert callable(iec61131::literals::Bit::String::Literal.__init__)


def test_iec61131::literals::bit::string::literal_constructor_args():
    sig = inspect.signature(iec61131::literals::Bit::String::Literal.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::character::string_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Character::String)


def test_iec61131::literals::character::string_constructor_exists():
    assert callable(iec61131::literals::Character::String.__init__)


def test_iec61131::literals::character::string_constructor_args():
    sig = inspect.signature(iec61131::literals::Character::String.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::time::literal_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Time::Literal)


def test_iec61131::literals::time::literal_constructor_exists():
    assert callable(iec61131::literals::Time::Literal.__init__)


def test_iec61131::literals::time::literal_constructor_args():
    sig = inspect.signature(iec61131::literals::Time::Literal.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::numeric::literal_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Numeric::Literal)


def test_iec61131::literals::numeric::literal_constructor_exists():
    assert callable(iec61131::literals::Numeric::Literal.__init__)


def test_iec61131::literals::numeric::literal_constructor_args():
    sig = inspect.signature(iec61131::literals::Numeric::Literal.__init__)
    params = list(sig.parameters.keys())



def test_tod::type::name_is_not_abstract():
    assert not inspect.isabstract(TOD::Type::Name)


def test_tod::type::name_constructor_exists():
    assert callable(TOD::Type::Name.__init__)


def test_tod::type::name_constructor_args():
    sig = inspect.signature(TOD::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_daytime_is_not_abstract():
    assert not inspect.isabstract(Daytime)


def test_daytime_constructor_exists():
    assert callable(Daytime.__init__)


def test_daytime_constructor_args():
    sig = inspect.signature(Daytime.__init__)
    params = list(sig.parameters.keys())



def test_time::literal_is_not_abstract():
    assert not inspect.isabstract(Time::Literal)


def test_time::literal_constructor_exists():
    assert callable(Time::Literal.__init__)


def test_time::literal_constructor_args():
    sig = inspect.signature(Time::Literal.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::date::and::time_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Date::And::Time)


def test_iec61131::literals::date::and::time_constructor_exists():
    assert callable(iec61131::literals::Date::And::Time.__init__)


def test_iec61131::literals::date::and::time_constructor_args():
    sig = inspect.signature(iec61131::literals::Date::And::Time.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::date_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Date)


def test_iec61131::literals::date_constructor_exists():
    assert callable(iec61131::literals::Date.__init__)


def test_iec61131::literals::date_constructor_args():
    sig = inspect.signature(iec61131::literals::Date.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::time::of::day_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Time::Of::Day)


def test_iec61131::literals::time::of::day_constructor_exists():
    assert callable(iec61131::literals::Time::Of::Day.__init__)


def test_iec61131::literals::time::of::day_constructor_args():
    sig = inspect.signature(iec61131::literals::Time::Of::Day.__init__)
    params = list(sig.parameters.keys())



def test_substraction::operator_is_not_abstract():
    assert not inspect.isabstract(Substraction::Operator)


def test_substraction::operator_constructor_exists():
    assert callable(Substraction::Operator.__init__)


def test_substraction::operator_constructor_args():
    sig = inspect.signature(Substraction::Operator.__init__)
    params = list(sig.parameters.keys())



def test_duration::type::name_is_not_abstract():
    assert not inspect.isabstract(Duration::Type::Name)


def test_duration::type::name_constructor_exists():
    assert callable(Duration::Type::Name.__init__)


def test_duration::type::name_constructor_args():
    sig = inspect.signature(Duration::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_interval_is_not_abstract():
    assert not inspect.isabstract(Interval)


def test_interval_constructor_exists():
    assert callable(Interval.__init__)


def test_interval_constructor_args():
    sig = inspect.signature(Interval.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::days_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Days)


def test_iec61131::literals::days_constructor_exists():
    assert callable(iec61131::literals::Days.__init__)


def test_iec61131::literals::days_constructor_args():
    sig = inspect.signature(iec61131::literals::Days.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::milliseconds_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Milliseconds)


def test_iec61131::literals::milliseconds_constructor_exists():
    assert callable(iec61131::literals::Milliseconds.__init__)


def test_iec61131::literals::milliseconds_constructor_args():
    sig = inspect.signature(iec61131::literals::Milliseconds.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::seconds_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Seconds)


def test_iec61131::literals::seconds_constructor_exists():
    assert callable(iec61131::literals::Seconds.__init__)


def test_iec61131::literals::seconds_constructor_args():
    sig = inspect.signature(iec61131::literals::Seconds.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::minutes_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Minutes)


def test_iec61131::literals::minutes_constructor_exists():
    assert callable(iec61131::literals::Minutes.__init__)


def test_iec61131::literals::minutes_constructor_args():
    sig = inspect.signature(iec61131::literals::Minutes.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::hours_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Hours)


def test_iec61131::literals::hours_constructor_exists():
    assert callable(iec61131::literals::Hours.__init__)


def test_iec61131::literals::hours_constructor_args():
    sig = inspect.signature(iec61131::literals::Hours.__init__)
    params = list(sig.parameters.keys())



def test_sfc::action::time_is_not_abstract():
    assert not inspect.isabstract(sfc::Action::Time)


def test_sfc::action::time_constructor_exists():
    assert callable(sfc::Action::Time.__init__)


def test_sfc::action::time_constructor_args():
    sig = inspect.signature(sfc::Action::Time.__init__)
    params = list(sig.parameters.keys())



def test_literals::time::literal_is_not_abstract():
    assert not inspect.isabstract(literals::Time::Literal)


def test_literals::time::literal_constructor_exists():
    assert callable(literals::Time::Literal.__init__)


def test_literals::time::literal_constructor_args():
    sig = inspect.signature(literals::Time::Literal.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::duration_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Duration)


def test_iec61131::literals::duration_constructor_exists():
    assert callable(iec61131::literals::Duration.__init__)


def test_iec61131::literals::duration_constructor_args():
    sig = inspect.signature(iec61131::literals::Duration.__init__)
    params = list(sig.parameters.keys())



def test_literals::bsinteger_is_not_abstract():
    assert not inspect.isabstract(literals::BSInteger)


def test_literals::bsinteger_constructor_exists():
    assert callable(literals::BSInteger.__init__)


def test_literals::bsinteger_constructor_args():
    sig = inspect.signature(literals::BSInteger.__init__)
    params = list(sig.parameters.keys())



def test_interfaces::range_is_not_abstract():
    assert not inspect.isabstract(interfaces::Range)


def test_interfaces::range_constructor_exists():
    assert callable(interfaces::Range.__init__)


def test_interfaces::range_constructor_args():
    sig = inspect.signature(interfaces::Range.__init__)
    params = list(sig.parameters.keys())



def test_st::case::list::element_is_not_abstract():
    assert not inspect.isabstract(st::Case::List::Element)


def test_st::case::list::element_constructor_exists():
    assert callable(st::Case::List::Element.__init__)


def test_st::case::list::element_constructor_args():
    sig = inspect.signature(st::Case::List::Element.__init__)
    params = list(sig.parameters.keys())



def test_literals::integer_is_not_abstract():
    assert not inspect.isabstract(literals::Integer)


def test_literals::integer_constructor_exists():
    assert callable(literals::Integer.__init__)


def test_literals::integer_constructor_args():
    sig = inspect.signature(literals::Integer.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::binary::integer_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Binary::Integer)


def test_iec61131::literals::binary::integer_constructor_exists():
    assert callable(iec61131::literals::Binary::Integer.__init__)


def test_iec61131::literals::binary::integer_constructor_args():
    sig = inspect.signature(iec61131::literals::Binary::Integer.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::octal::integer_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Octal::Integer)


def test_iec61131::literals::octal::integer_constructor_exists():
    assert callable(iec61131::literals::Octal::Integer.__init__)


def test_iec61131::literals::octal::integer_constructor_args():
    sig = inspect.signature(iec61131::literals::Octal::Integer.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::hex::integer_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Hex::Integer)


def test_iec61131::literals::hex::integer_constructor_exists():
    assert callable(iec61131::literals::Hex::Integer.__init__)


def test_iec61131::literals::hex::integer_constructor_args():
    sig = inspect.signature(iec61131::literals::Hex::Integer.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::unsigned::integer_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Unsigned::Integer)


def test_iec61131::literals::unsigned::integer_constructor_exists():
    assert callable(iec61131::literals::Unsigned::Integer.__init__)


def test_iec61131::literals::unsigned::integer_constructor_args():
    sig = inspect.signature(iec61131::literals::Unsigned::Integer.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::signed::integer_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Signed::Integer)


def test_iec61131::literals::signed::integer_constructor_exists():
    assert callable(iec61131::literals::Signed::Integer.__init__)


def test_iec61131::literals::signed::integer_constructor_args():
    sig = inspect.signature(iec61131::literals::Signed::Integer.__init__)
    params = list(sig.parameters.keys())
    assert "negative" in params, "Missing parameter 'negative'"

def test_iec61131::literals::signed::integer_has_negative():
    assert hasattr(iec61131::literals::Signed::Integer, "negative")
    descriptor = None
    for klass in iec61131::literals::Signed::Integer.__mro__:
        if "negative" in klass.__dict__:
            descriptor = klass.__dict__["negative"]
            break
    assert isinstance(descriptor, property)



def test_il::il::operand_is_not_abstract():
    assert not inspect.isabstract(il::Il::Operand)


def test_il::il::operand_constructor_exists():
    assert callable(il::Il::Operand.__init__)


def test_il::il::operand_constructor_args():
    sig = inspect.signature(il::Il::Operand.__init__)
    params = list(sig.parameters.keys())



def test_configurations::prog::data::source_is_not_abstract():
    assert not inspect.isabstract(configurations::Prog::Data::Source)


def test_configurations::prog::data::source_constructor_exists():
    assert callable(configurations::Prog::Data::Source.__init__)


def test_configurations::prog::data::source_constructor_args():
    sig = inspect.signature(configurations::Prog::Data::Source.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::enumerated::value_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Enumerated::Value)


def test_iec61131::interfaces::enumerated::value_constructor_exists():
    assert callable(iec61131::interfaces::Enumerated::Value.__init__)


def test_iec61131::interfaces::enumerated::value_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Enumerated::Value.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iec61131::interfaces::enumerated::value_has_name():
    assert hasattr(iec61131::interfaces::Enumerated::Value, "name")
    descriptor = None
    for klass in iec61131::interfaces::Enumerated::Value.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_configurations::data::source_is_not_abstract():
    assert not inspect.isabstract(configurations::Data::Source)


def test_configurations::data::source_constructor_exists():
    assert callable(configurations::Data::Source.__init__)


def test_configurations::data::source_constructor_args():
    sig = inspect.signature(configurations::Data::Source.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::global::var::reference_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Global::Var::Reference)


def test_iec61131::configurations::global::var::reference_constructor_exists():
    assert callable(iec61131::configurations::Global::Var::Reference.__init__)


def test_iec61131::configurations::global::var::reference_constructor_args():
    sig = inspect.signature(iec61131::configurations::Global::Var::Reference.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::variables::direct::variable_is_not_abstract():
    assert not inspect.isabstract(iec61131::variables::Direct::Variable)


def test_iec61131::variables::direct::variable_constructor_exists():
    assert callable(iec61131::variables::Direct::Variable.__init__)


def test_iec61131::variables::direct::variable_constructor_args():
    sig = inspect.signature(iec61131::variables::Direct::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iec61131::variables::direct::variable_has_value():
    assert hasattr(iec61131::variables::Direct::Variable, "value")
    descriptor = None
    for klass in iec61131::variables::Direct::Variable.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iec61131::literals::constant_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Constant)


def test_iec61131::literals::constant_constructor_exists():
    assert callable(iec61131::literals::Constant.__init__)


def test_iec61131::literals::constant_constructor_args():
    sig = inspect.signature(iec61131::literals::Constant.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::boolean::literal_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Boolean::Literal)


def test_iec61131::literals::boolean::literal_constructor_exists():
    assert callable(iec61131::literals::Boolean::Literal.__init__)


def test_iec61131::literals::boolean::literal_constructor_args():
    sig = inspect.signature(iec61131::literals::Boolean::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iec61131::literals::boolean::literal_has_value():
    assert hasattr(iec61131::literals::Boolean::Literal, "value")
    descriptor = None
    for klass in iec61131::literals::Boolean::Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_fixed::point_is_not_abstract():
    assert not inspect.isabstract(Fixed::Point)


def test_fixed::point_constructor_exists():
    assert callable(Fixed::Point.__init__)


def test_fixed::point_constructor_args():
    sig = inspect.signature(Fixed::Point.__init__)
    params = list(sig.parameters.keys())



def test_real::type::name_is_not_abstract():
    assert not inspect.isabstract(Real::Type::Name)


def test_real::type::name_constructor_exists():
    assert callable(Real::Type::Name.__init__)


def test_real::type::name_constructor_args():
    sig = inspect.signature(Real::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::literals::real::literal_is_not_abstract():
    assert not inspect.isabstract(iec61131::literals::Real::Literal)


def test_iec61131::literals::real::literal_constructor_exists():
    assert callable(iec61131::literals::Real::Literal.__init__)


def test_iec61131::literals::real::literal_constructor_args():
    sig = inspect.signature(iec61131::literals::Real::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "negative" in params, "Missing parameter 'negative'"
    assert "exponent" in params, "Missing parameter 'exponent'"

def test_iec61131::literals::real::literal_has_negative():
    assert hasattr(iec61131::literals::Real::Literal, "negative")
    descriptor = None
    for klass in iec61131::literals::Real::Literal.__mro__:
        if "negative" in klass.__dict__:
            descriptor = klass.__dict__["negative"]
            break
    assert isinstance(descriptor, property)

def test_iec61131::literals::real::literal_has_exponent():
    assert hasattr(iec61131::literals::Real::Literal, "exponent")
    descriptor = None
    for klass in iec61131::literals::Real::Literal.__mro__:
        if "exponent" in klass.__dict__:
            descriptor = klass.__dict__["exponent"]
            break
    assert isinstance(descriptor, property)



def test_integer::type::name_is_not_abstract():
    assert not inspect.isabstract(Integer::Type::Name)


def test_integer::type::name_constructor_exists():
    assert callable(Integer::Type::Name.__init__)


def test_integer::type::name_constructor_args():
    sig = inspect.signature(Integer::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::signed::integer::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::Signed::Integer::Type::Name)


def test_iec61131::types::signed::integer::type::name_constructor_exists():
    assert callable(iec61131::types::Signed::Integer::Type::Name.__init__)


def test_iec61131::types::signed::integer::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::Signed::Integer::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::types::unsigned::integer::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::types::Unsigned::Integer::Type::Name)


def test_iec61131::types::unsigned::integer::type::name_constructor_exists():
    assert callable(iec61131::types::Unsigned::Integer::Type::Name.__init__)


def test_iec61131::types::unsigned::integer::type::name_constructor_args():
    sig = inspect.signature(iec61131::types::Unsigned::Integer::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::namedelement_is_not_abstract():
    assert not inspect.isabstract(iec61131::NamedElement)


def test_iec61131::namedelement_constructor_exists():
    assert callable(iec61131::NamedElement.__init__)


def test_iec61131::namedelement_constructor_args():
    sig = inspect.signature(iec61131::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iec61131::namedelement_has_name():
    assert hasattr(iec61131::NamedElement, "name")
    descriptor = None
    for klass in iec61131::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iec61131::commentable_is_not_abstract():
    assert not inspect.isabstract(iec61131::Commentable)


def test_iec61131::commentable_constructor_exists():
    assert callable(iec61131::Commentable.__init__)


def test_iec61131::commentable_constructor_args():
    sig = inspect.signature(iec61131::Commentable.__init__)
    params = list(sig.parameters.keys())
    assert "comments" in params, "Missing parameter 'comments'"

def test_iec61131::commentable_has_comments():
    assert hasattr(iec61131::Commentable, "comments")
    descriptor = None
    for klass in iec61131::Commentable.__mro__:
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



def test_iec61131::variables::variable::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::variables::Variable::Name)


def test_iec61131::variables::variable::name_constructor_exists():
    assert callable(iec61131::variables::Variable::Name.__init__)


def test_iec61131::variables::variable::name_constructor_args():
    sig = inspect.signature(iec61131::variables::Variable::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::sfc::step::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::sfc::Step::Name)


def test_iec61131::sfc::step::name_constructor_exists():
    assert callable(iec61131::sfc::Step::Name.__init__)


def test_iec61131::sfc::step::name_constructor_args():
    sig = inspect.signature(iec61131::sfc::Step::Name.__init__)
    params = list(sig.parameters.keys())



def test_commentable_is_not_abstract():
    assert not inspect.isabstract(Commentable)


def test_commentable_constructor_exists():
    assert callable(Commentable.__init__)


def test_commentable_constructor_args():
    sig = inspect.signature(Commentable.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::param::assignment_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Param::Assignment)


def test_iec61131::st::param::assignment_constructor_exists():
    assert callable(iec61131::st::Param::Assignment.__init__)


def test_iec61131::st::param::assignment_constructor_args():
    sig = inspect.signature(iec61131::st::Param::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::statement_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Statement)


def test_iec61131::st::statement_constructor_exists():
    assert callable(iec61131::st::Statement.__init__)


def test_iec61131::st::statement_constructor_args():
    sig = inspect.signature(iec61131::st::Statement.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::configurations::program::configuration_is_not_abstract():
    assert not inspect.isabstract(iec61131::configurations::Program::Configuration)


def test_iec61131::configurations::program::configuration_constructor_exists():
    assert callable(iec61131::configurations::Program::Configuration.__init__)


def test_iec61131::configurations::program::configuration_constructor_args():
    sig = inspect.signature(iec61131::configurations::Program::Configuration.__init__)
    params = list(sig.parameters.keys())
    assert "retain" in params, "Missing parameter 'retain'"

def test_iec61131::configurations::program::configuration_has_retain():
    assert hasattr(iec61131::configurations::Program::Configuration, "retain")
    descriptor = None
    for klass in iec61131::configurations::Program::Configuration.__mro__:
        if "retain" in klass.__dict__:
            descriptor = klass.__dict__["retain"]
            break
    assert isinstance(descriptor, property)



def test_iec61131::interfaces::interface_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Interface)


def test_iec61131::interfaces::interface_constructor_exists():
    assert callable(iec61131::interfaces::Interface.__init__)


def test_iec61131::interfaces::interface_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Interface.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::expression::variable_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Expression::Variable)


def test_iec61131::st::expression::variable_constructor_exists():
    assert callable(iec61131::st::Expression::Variable.__init__)


def test_iec61131::st::expression::variable_constructor_args():
    sig = inspect.signature(iec61131::st::Expression::Variable.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::global::var::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Global::Var::Name)


def test_iec61131::interfaces::global::var::name_constructor_exists():
    assert callable(iec61131::interfaces::Global::Var::Name.__init__)


def test_iec61131::interfaces::global::var::name_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Global::Var::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::variables::variable_is_not_abstract():
    assert not inspect.isabstract(iec61131::variables::Variable)


def test_iec61131::variables::variable_constructor_exists():
    assert callable(iec61131::variables::Variable.__init__)


def test_iec61131::variables::variable_constructor_args():
    sig = inspect.signature(iec61131::variables::Variable.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::st::expression::types_is_not_abstract():
    assert not inspect.isabstract(iec61131::st::Expression::Types)


def test_iec61131::st::expression::types_constructor_exists():
    assert callable(iec61131::st::Expression::Types.__init__)


def test_iec61131::st::expression::types_constructor_args():
    sig = inspect.signature(iec61131::st::Expression::Types.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::pous::function::block::type::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::pous::Function::Block::Type::Name)


def test_iec61131::pous::function::block::type::name_constructor_exists():
    assert callable(iec61131::pous::Function::Block::Type::Name.__init__)


def test_iec61131::pous::function::block::type::name_constructor_args():
    sig = inspect.signature(iec61131::pous::Function::Block::Type::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::interfaces::global::var::decl_is_not_abstract():
    assert not inspect.isabstract(iec61131::interfaces::Global::Var::Decl)


def test_iec61131::interfaces::global::var::decl_constructor_exists():
    assert callable(iec61131::interfaces::Global::Var::Decl.__init__)


def test_iec61131::interfaces::global::var::decl_constructor_args():
    sig = inspect.signature(iec61131::interfaces::Global::Var::Decl.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::library::element::name_is_not_abstract():
    assert not inspect.isabstract(iec61131::Library::Element::Name)


def test_iec61131::library::element::name_constructor_exists():
    assert callable(iec61131::Library::Element::Name.__init__)


def test_iec61131::library::element::name_constructor_args():
    sig = inspect.signature(iec61131::Library::Element::Name.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::library::element::declaration_is_not_abstract():
    assert not inspect.isabstract(iec61131::Library::Element::Declaration)


def test_iec61131::library::element::declaration_constructor_exists():
    assert callable(iec61131::Library::Element::Declaration.__init__)


def test_iec61131::library::element::declaration_constructor_args():
    sig = inspect.signature(iec61131::Library::Element::Declaration.__init__)
    params = list(sig.parameters.keys())



def test_iec61131::iec61131_is_not_abstract():
    assert not inspect.isabstract(iec61131::IEC61131)


def test_iec61131::iec61131_constructor_exists():
    assert callable(iec61131::IEC61131.__init__)


def test_iec61131::iec61131_constructor_args():
    sig = inspect.signature(iec61131::IEC61131.__init__)
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
        "READ_ONLY",
        "READ_WRITE",
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
iec61131::sfc::Action::Qualifier_strategy = st.builds(
    iec61131::sfc::Action::Qualifier,
    qualifier=
        safe_text
)
iec61131::sfc::Action::Name_strategy = st.builds(
    iec61131::sfc::Action::Name,
    name=
        safe_text
)
Step::Name_strategy = st.builds(
    Step::Name,
)
Action::Association_strategy = st.builds(
    Action::Association,
)
iec61131::sfc::Step::Types_strategy = st.builds(
    iec61131::sfc::Step::Types,
)
Action::Qualifier_strategy = st.builds(
    Action::Qualifier,
)
iec61131::sfc::Action::Association_strategy = st.builds(
    iec61131::sfc::Action::Association,
)
iec61131::sfc::Sfc::Elements_strategy = st.builds(
    iec61131::sfc::Sfc::Elements,
)
Action::Name_strategy = st.builds(
    Action::Name,
)
Transition::Condition_strategy = st.builds(
    Transition::Condition,
)
iec61131::sfc::Sfc::Network_strategy = st.builds(
    iec61131::sfc::Sfc::Network,
)
Sfc::Network_strategy = st.builds(
    Sfc::Network,
)
iec61131::il::Il::Assign::Out::Operator_strategy = st.builds(
    iec61131::il::Il::Assign::Out::Operator,
)
iec61131::il::Param::Assignment_strategy = st.builds(
    iec61131::il::Param::Assignment,
)
Assignment::Name_strategy = st.builds(
    Assignment::Name,
)
iec61131::il::Il::Assign::Operator_strategy = st.builds(
    iec61131::il::Il::Assign::Operator,
)
iec61131::il::Param::Instruction_strategy = st.builds(
    iec61131::il::Param::Instruction,
)
iec61131::il::Param::Assignments_strategy = st.builds(
    iec61131::il::Param::Assignments,
)
Il::Assign::Out::Operator_strategy = st.builds(
    Il::Assign::Out::Operator,
)
iec61131::il::Il::Operand::List_strategy = st.builds(
    iec61131::il::Il::Operand::List,
)
iec61131::il::Il::Simple::Operator_strategy = st.builds(
    iec61131::il::Il::Simple::Operator,
)
iec61131::il::Il::Operations_strategy = st.builds(
    iec61131::il::Il::Operations,
)
Il::Param::List_strategy = st.builds(
    Il::Param::List,
)
Il::Assign::Operator_strategy = st.builds(
    Il::Assign::Operator,
)
Param::Assignments_strategy = st.builds(
    Param::Assignments,
)
iec61131::il::Il::Param::Out::Assignment_strategy = st.builds(
    iec61131::il::Il::Param::Out::Assignment,
)
iec61131::il::Il::Param::Assignment_strategy = st.builds(
    iec61131::il::Il::Param::Assignment,
)
Param::Instruction_strategy = st.builds(
    Param::Instruction,
)
iec61131::il::Il::Param::Last::Instruction_strategy = st.builds(
    iec61131::il::Il::Param::Last::Instruction,
)
iec61131::il::Il::Param::Instruction_strategy = st.builds(
    iec61131::il::Il::Param::Instruction,
)
iec61131::il::Simple::Instr_strategy = st.builds(
    iec61131::il::Simple::Instr,
)
Simple::Instr_strategy = st.builds(
    Simple::Instr,
)
iec61131::il::Il::Simple::Instruction_strategy = st.builds(
    iec61131::il::Il::Simple::Instruction,
)
iec61131::il::Operands_strategy = st.builds(
    iec61131::il::Operands,
)
Il::Param::Last::Instruction_strategy = st.builds(
    Il::Param::Last::Instruction,
)
Il::Param::Instruction_strategy = st.builds(
    Il::Param::Instruction,
)
iec61131::il::Il::Param::List_strategy = st.builds(
    iec61131::il::Il::Param::List,
)
iec61131::il::Il::Call::Operator_strategy = st.builds(
    iec61131::il::Il::Call::Operator,
)
iec61131::il::Il::Jump::Operator_strategy = st.builds(
    iec61131::il::Il::Jump::Operator,
)
Il::Operand::List_strategy = st.builds(
    Il::Operand::List,
)
Il::Simple::Operator_strategy = st.builds(
    Il::Simple::Operator,
)
iec61131::il::Il::Expr::Operator_strategy = st.builds(
    iec61131::il::Il::Expr::Operator,
)
Il::Simple::Operation_strategy = st.builds(
    Il::Simple::Operation,
)
iec61131::il::Simple::Operation2_strategy = st.builds(
    iec61131::il::Simple::Operation2,
)
iec61131::il::Simple::Operation1_strategy = st.builds(
    iec61131::il::Simple::Operation1,
)
Il::Instruction_strategy = st.builds(
    Il::Instruction,
)
Operands_strategy = st.builds(
    Operands,
)
iec61131::il::Operand2_strategy = st.builds(
    iec61131::il::Operand2,
)
iec61131::il::Operand1_strategy = st.builds(
    iec61131::il::Operand1,
)
Il::Call::Operator_strategy = st.builds(
    Il::Call::Operator,
)
Il::Jump::Operator_strategy = st.builds(
    Il::Jump::Operator,
)
Simple::Instr::List_strategy = st.builds(
    Simple::Instr::List,
)
Il::Operand_strategy = st.builds(
    Il::Operand,
)
il::Simple::Instr_strategy = st.builds(
    il::Simple::Instr,
)
il::Il::Operations_strategy = st.builds(
    il::Il::Operations,
)
iec61131::il::Il::Expression_strategy = st.builds(
    iec61131::il::Il::Expression,
)
iec61131::il::Il::Formal::Funct::Call_strategy = st.builds(
    iec61131::il::Il::Formal::Funct::Call,
)
iec61131::il::Il::Simple::Operation_strategy = st.builds(
    iec61131::il::Il::Simple::Operation,
)
iec61131::il::Label_strategy = st.builds(
    iec61131::il::Label,
    label=
        safe_text
)
Il::Operations_strategy = st.builds(
    Il::Operations,
)
iec61131::il::Il::Return::Operator_strategy = st.builds(
    iec61131::il::Il::Return::Operator,
)
iec61131::il::Il::Jump::Operation_strategy = st.builds(
    iec61131::il::Il::Jump::Operation,
)
iec61131::il::Il::Fb::Call_strategy = st.builds(
    iec61131::il::Il::Fb::Call,
)
Label_strategy = st.builds(
    Label,
)
iec61131::il::Il::Instruction_strategy = st.builds(
    iec61131::il::Il::Instruction,
)
Il::Simple::Instruction_strategy = st.builds(
    Il::Simple::Instruction,
)
iec61131::il::Simple::Instr::List_strategy = st.builds(
    iec61131::il::Simple::Instr::List,
)
Unary::Operator_strategy = st.builds(
    Unary::Operator,
)
Power::Symbol_strategy = st.builds(
    Power::Symbol,
)
Structured::Variable_strategy = st.builds(
    Structured::Variable,
)
Array::Variable_strategy = st.builds(
    Array::Variable,
)
Function::Name_strategy = st.builds(
    Function::Name,
)
Primary::Expression_strategy = st.builds(
    Primary::Expression,
)
iec61131::st::Expression::Variable::Type_strategy = st.builds(
    iec61131::st::Expression::Variable::Type,
)
iec61131::st::Expression::EnumValue_strategy = st.builds(
    iec61131::st::Expression::EnumValue,
)
iec61131::st::Call::Expression_strategy = st.builds(
    iec61131::st::Call::Expression,
)
iec61131::st::Expression::Constant_strategy = st.builds(
    iec61131::st::Expression::Constant,
)
iec61131::st::Bracket::Expression_strategy = st.builds(
    iec61131::st::Bracket::Expression,
)
Add::Operator_strategy = st.builds(
    Add::Operator,
)
Xor::Operator_strategy = st.builds(
    Xor::Operator,
)
iec61131::st::For::List_strategy = st.builds(
    iec61131::st::For::List,
)
iec61131::st::Control::Variable_strategy = st.builds(
    iec61131::st::Control::Variable,
    name=
        safe_text
)
Statement::List_strategy = st.builds(
    Statement::List,
)
Selection::Statement_strategy = st.builds(
    Selection::Statement,
)
iec61131::st::If::Statement_strategy = st.builds(
    iec61131::st::If::Statement,
)
Not::Operator_strategy = st.builds(
    Not::Operator,
)
Variable_strategy = st.builds(
    Variable,
)
For::List_strategy = st.builds(
    For::List,
)
Control::Variable_strategy = st.builds(
    Control::Variable,
)
Iteration::Statement_strategy = st.builds(
    Iteration::Statement,
)
iec61131::st::Exit::Statement_strategy = st.builds(
    iec61131::st::Exit::Statement,
)
iec61131::st::While::Statement_strategy = st.builds(
    iec61131::st::While::Statement,
)
iec61131::st::Repeat::Statement_strategy = st.builds(
    iec61131::st::Repeat::Statement,
)
iec61131::st::For::Statement_strategy = st.builds(
    iec61131::st::For::Statement,
)
iec61131::st::Case::List::Element_strategy = st.builds(
    iec61131::st::Case::List::Element,
)
iec61131::st::Case::List_strategy = st.builds(
    iec61131::st::Case::List,
)
Case::List_strategy = st.builds(
    Case::List,
)
iec61131::st::Case::Element_strategy = st.builds(
    iec61131::st::Case::Element,
)
iec61131::st::Else::Statement_strategy = st.builds(
    iec61131::st::Else::Statement,
)
Single::Element::Type::Name_strategy = st.builds(
    Single::Element::Type::Name,
)
iec61131::types::Enumerated::Type::Name_strategy = st.builds(
    iec61131::types::Enumerated::Type::Name,
)
iec61131::types::Subrange::Type::Name_strategy = st.builds(
    iec61131::types::Subrange::Type::Name,
)
types::Single::Element::Type::Name_strategy = st.builds(
    types::Single::Element::Type::Name,
)
types::Derived::Type::Name_strategy = st.builds(
    types::Derived::Type::Name,
)
Derived::Type::Name_strategy = st.builds(
    Derived::Type::Name,
)
iec61131::types::Array::Type::Name_strategy = st.builds(
    iec61131::types::Array::Type::Name,
)
iec61131::types::String::Type::Name_strategy = st.builds(
    iec61131::types::String::Type::Name,
)
iec61131::types::Single::Element::Type::Name_strategy = st.builds(
    iec61131::types::Single::Element::Type::Name,
)
iec61131::variables::Subscript::List_strategy = st.builds(
    iec61131::variables::Subscript::List,
)
Input::Reference_strategy = st.builds(
    Input::Reference,
)
Output::Reference_strategy = st.builds(
    Output::Reference,
)
variables::Symbolic::Variable_strategy = st.builds(
    variables::Symbolic::Variable,
)
pous::Function::Return::Value_strategy = st.builds(
    pous::Function::Return::Value,
)
types::Data::Type::Name_strategy = st.builds(
    types::Data::Type::Name,
)
iec61131::types::Non::Generic::Type::Name_strategy = st.builds(
    iec61131::types::Non::Generic::Type::Name,
)
interfaces::Simple::Specification::Func_strategy = st.builds(
    interfaces::Simple::Specification::Func,
)
types::Non::Generic::Type::Name_strategy = st.builds(
    types::Non::Generic::Type::Name,
)
Numeric::Type::Name_strategy = st.builds(
    Numeric::Type::Name,
)
iec61131::types::Real::Type::Name_strategy = st.builds(
    iec61131::types::Real::Type::Name,
)
iec61131::types::Integer::Type::Name_strategy = st.builds(
    iec61131::types::Integer::Type::Name,
)
Elementary::Type::Name_strategy = st.builds(
    Elementary::Type::Name,
)
iec61131::types::Bit::String::Type::Name_strategy = st.builds(
    iec61131::types::Bit::String::Type::Name,
)
iec61131::types::Date::Type::Name_strategy = st.builds(
    iec61131::types::Date::Type::Name,
)
iec61131::types::Duration::Type::Name_strategy = st.builds(
    iec61131::types::Duration::Type::Name,
)
iec61131::types::Byte::String::Type::Name_strategy = st.builds(
    iec61131::types::Byte::String::Type::Name,
)
iec61131::types::Numeric::Type::Name_strategy = st.builds(
    iec61131::types::Numeric::Type::Name,
)
Data::Type::Name_strategy = st.builds(
    Data::Type::Name,
)
iec61131::types::Simple::Specification_strategy = st.builds(
    iec61131::types::Simple::Specification,
)
iec61131::types::TypeLib_strategy = st.builds(
    iec61131::types::TypeLib,
)
Fbd::Network_strategy = st.builds(
    Fbd::Network,
)
iec61131::sfc::Transition::Cond2_strategy = st.builds(
    iec61131::sfc::Transition::Cond2,
)
iec61131::sfc::Transition::Condition_strategy = st.builds(
    iec61131::sfc::Transition::Condition,
)
iec61131::sfc::Steps_strategy = st.builds(
    iec61131::sfc::Steps,
)
iec61131::sfc::Transition::Name_strategy = st.builds(
    iec61131::sfc::Transition::Name,
    name=
        safe_text
)
iec61131::sfc::Action::Time_strategy = st.builds(
    iec61131::sfc::Action::Time,
)
variables::Variable_strategy = st.builds(
    variables::Variable,
)
Subscript::List_strategy = st.builds(
    Subscript::List,
)
Multi::Element::Variable_strategy = st.builds(
    Multi::Element::Variable,
)
iec61131::variables::Structured::Variable_strategy = st.builds(
    iec61131::variables::Structured::Variable,
)
iec61131::variables::Array::Variable_strategy = st.builds(
    iec61131::variables::Array::Variable,
)
iec61131::variables::Symbolic::Variable_strategy = st.builds(
    iec61131::variables::Symbolic::Variable,
)
iec61131::sfc::Cond2::Condition_strategy = st.builds(
    iec61131::sfc::Cond2::Condition,
)
iec61131::sfc::Transition::Cond3_strategy = st.builds(
    iec61131::sfc::Transition::Cond3,
)
iec61131::sfc::Transition::Cond1_strategy = st.builds(
    iec61131::sfc::Transition::Cond1,
)
Cond2::Condition_strategy = st.builds(
    Cond2::Condition,
)
iec61131::fbd::Fbd::Network_strategy = st.builds(
    iec61131::fbd::Fbd::Network,
)
iec61131::ld::Rung_strategy = st.builds(
    iec61131::ld::Rung,
)
Steps_strategy = st.builds(
    Steps,
)
iec61131::sfc::Steps1_strategy = st.builds(
    iec61131::sfc::Steps1,
)
iec61131::sfc::Steps2_strategy = st.builds(
    iec61131::sfc::Steps2,
)
Transition::Name_strategy = st.builds(
    Transition::Name,
)
sfc::Step::Types_strategy = st.builds(
    sfc::Step::Types,
)
sfc::Sfc::Elements_strategy = st.builds(
    sfc::Sfc::Elements,
)
iec61131::sfc::Step_strategy = st.builds(
    iec61131::sfc::Step,
)
Step::Types_strategy = st.builds(
    Step::Types,
)
iec61131::sfc::Initial::Step_strategy = st.builds(
    iec61131::sfc::Initial::Step,
)
Sfc::Elements_strategy = st.builds(
    Sfc::Elements,
)
iec61131::sfc::Transition_strategy = st.builds(
    iec61131::sfc::Transition,
)
iec61131::sfc::Action_strategy = st.builds(
    iec61131::sfc::Action,
)
Initial::Step_strategy = st.builds(
    Initial::Step,
)
iec61131::sfc::Timed::Qualifier_strategy = st.builds(
    iec61131::sfc::Timed::Qualifier,
    qualifier=
        safe_text
)
Action::Time_strategy = st.builds(
    Action::Time,
)
iec61131::sfc::ActionTime2_strategy = st.builds(
    iec61131::sfc::ActionTime2,
)
Timed::Qualifier_strategy = st.builds(
    Timed::Qualifier,
)
Variable::Name_strategy = st.builds(
    Variable::Name,
)
Location_strategy = st.builds(
    Location,
)
iec61131::interfaces::Located::Var::Decl_strategy = st.builds(
    iec61131::interfaces::Located::Var::Decl,
)
Direct::Variable_strategy = st.builds(
    Direct::Variable,
)
iec61131::interfaces::Location_strategy = st.builds(
    iec61131::interfaces::Location,
)
iec61131::interfaces::Located::Var::Spec::Init_strategy = st.builds(
    iec61131::interfaces::Located::Var::Spec::Init,
)
iec61131::interfaces::External::Specification_strategy = st.builds(
    iec61131::interfaces::External::Specification,
)
iec61131::interfaces::Var::Spec_strategy = st.builds(
    iec61131::interfaces::Var::Spec,
)
iec61131::interfaces::Incompl::Location_strategy = st.builds(
    iec61131::interfaces::Incompl::Location,
    location=
        safe_text
)
Var::Spec_strategy = st.builds(
    Var::Spec,
)
Incompl::Location_strategy = st.builds(
    Incompl::Location,
)
iec61131::interfaces::Incompl::Located::Var::Decl_strategy = st.builds(
    iec61131::interfaces::Incompl::Located::Var::Decl,
)
Incompl::Located::Var::Decl_strategy = st.builds(
    Incompl::Located::Var::Decl,
)
Temp::Var::Decl_strategy = st.builds(
    Temp::Var::Decl,
)
Global::Var::Spec_strategy = st.builds(
    Global::Var::Spec,
)
iec61131::interfaces::Global::Var::List_strategy = st.builds(
    iec61131::interfaces::Global::Var::List,
)
Library::Element::Name_strategy = st.builds(
    Library::Element::Name,
)
iec61131::types::Data::Type::Name_strategy = st.builds(
    iec61131::types::Data::Type::Name,
)
iec61131::interfaces::Specification_strategy = st.builds(
    iec61131::interfaces::Specification,
)
Specification_strategy = st.builds(
    Specification,
)
Array::Initial::Elements_strategy = st.builds(
    Array::Initial::Elements,
)
iec61131::interfaces::Array::Initialization_strategy = st.builds(
    iec61131::interfaces::Array::Initialization,
)
iec61131::interfaces::Var1::List_strategy = st.builds(
    iec61131::interfaces::Var1::List,
)
Double::BString_strategy = st.builds(
    Double::BString,
)
Double::Byte::Character::String_strategy = st.builds(
    Double::Byte::Character::String,
)
Single::BString_strategy = st.builds(
    Single::BString,
)
Single::Byte::Character::String_strategy = st.builds(
    Single::Byte::Character::String,
)
Located::Var::Spec::Init_strategy = st.builds(
    Located::Var::Spec::Init,
)
iec61131::interfaces::Double::Byte::String::Spec_strategy = st.builds(
    iec61131::interfaces::Double::Byte::String::Spec,
)
iec61131::interfaces::Single::Byte::String::Spec_strategy = st.builds(
    iec61131::interfaces::Single::Byte::String::Spec,
)
Double::Byte::String::Spec_strategy = st.builds(
    Double::Byte::String::Spec,
)
Single::Byte::String::Spec_strategy = st.builds(
    Single::Byte::String::Spec,
)
String::Var::Declaration_strategy = st.builds(
    String::Var::Declaration,
)
iec61131::interfaces::Double::Byte::String::Var::Declaration_strategy = st.builds(
    iec61131::interfaces::Double::Byte::String::Var::Declaration,
)
iec61131::interfaces::Single::Byte::String::Var::Declaration_strategy = st.builds(
    iec61131::interfaces::Single::Byte::String::Var::Declaration,
)
Range_strategy = st.builds(
    Range,
)
Case::List::Element_strategy = st.builds(
    Case::List::Element,
)
iec61131::interfaces::Subrange_strategy = st.builds(
    iec61131::interfaces::Subrange,
    delimiter=
        safe_text
)
iec61131::interfaces::Array::Initial::Elements_strategy = st.builds(
    iec61131::interfaces::Array::Initial::Elements,
)
interfaces::Var::Spec_strategy = st.builds(
    interfaces::Var::Spec,
)
interfaces::External::Specification_strategy = st.builds(
    interfaces::External::Specification,
)
iec61131::interfaces::Array::Specification_strategy = st.builds(
    iec61131::interfaces::Array::Specification,
)
iec61131::types::Structure::Type::Name_strategy = st.builds(
    iec61131::types::Structure::Type::Name,
)
interfaces::Specification_strategy = st.builds(
    interfaces::Specification,
)
iec61131::interfaces::Enumerated::Specification_strategy = st.builds(
    iec61131::interfaces::Enumerated::Specification,
)
iec61131::interfaces::Subrange::Specification_strategy = st.builds(
    iec61131::interfaces::Subrange::Specification,
)
interfaces::Var2::Init::Decl_strategy = st.builds(
    interfaces::Var2::Init::Decl,
)
interfaces::Temp::Var::Decl_strategy = st.builds(
    interfaces::Temp::Var::Decl,
)
iec61131::interfaces::String::Var::Declaration_strategy = st.builds(
    iec61131::interfaces::String::Var::Declaration,
)
Function::Block::Type::Name_strategy = st.builds(
    Function::Block::Type::Name,
)
Structure::Initialization_strategy = st.builds(
    Structure::Initialization,
)
Temp::Var::Declaration_strategy = st.builds(
    Temp::Var::Declaration,
)
iec61131::interfaces::Array::Var::Declaration_strategy = st.builds(
    iec61131::interfaces::Array::Var::Declaration,
)
iec61131::interfaces::Structured::Var::Declaration_strategy = st.builds(
    iec61131::interfaces::Structured::Var::Declaration,
)
iec61131::interfaces::Var1::Declaration_strategy = st.builds(
    iec61131::interfaces::Var1::Declaration,
)
iec61131::interfaces::Fb::Name::Decl_strategy = st.builds(
    iec61131::interfaces::Fb::Name::Decl,
)
Enumerated::Type::Name_strategy = st.builds(
    Enumerated::Type::Name,
)
iec61131::interfaces::Structure::Element::Name_strategy = st.builds(
    iec61131::interfaces::Structure::Element::Name,
    name=
        safe_text
)
Initial::Element_strategy = st.builds(
    Initial::Element,
)
Structure::Element::Name_strategy = st.builds(
    Structure::Element::Name,
)
iec61131::interfaces::Structure::Element::Initialization_strategy = st.builds(
    iec61131::interfaces::Structure::Element::Initialization,
)
Structure::Element::Initialization_strategy = st.builds(
    Structure::Element::Initialization,
)
iec61131::interfaces::Structure::Initialization_strategy = st.builds(
    iec61131::interfaces::Structure::Initialization,
)
iec61131::interfaces::Var::Declaration_strategy = st.builds(
    iec61131::interfaces::Var::Declaration,
)
Structure::Type::Name_strategy = st.builds(
    Structure::Type::Name,
)
pous::Structure::Specification_strategy = st.builds(
    pous::Structure::Specification,
)
Array::Specification_strategy = st.builds(
    Array::Specification,
)
Array::Initialization_strategy = st.builds(
    Array::Initialization,
)
Var::Declaration_strategy = st.builds(
    Var::Declaration,
)
iec61131::interfaces::Temp::Var::Decl_strategy = st.builds(
    iec61131::interfaces::Temp::Var::Decl,
)
Var1::Specification_strategy = st.builds(
    Var1::Specification,
)
Var::Init::Decl_strategy = st.builds(
    Var::Init::Decl,
)
iec61131::interfaces::Var1::Init::Decl_strategy = st.builds(
    iec61131::interfaces::Var1::Init::Decl,
)
Var1::List_strategy = st.builds(
    Var1::List,
)
Input::Declaration_strategy = st.builds(
    Input::Declaration,
)
iec61131::interfaces::Var::Init::Decl_strategy = st.builds(
    iec61131::interfaces::Var::Init::Decl,
)
Io::Var::Declaration_strategy = st.builds(
    Io::Var::Declaration,
)
iec61131::interfaces::Output::Declarations_strategy = st.builds(
    iec61131::interfaces::Output::Declarations,
    retain=
        st.booleans()
)
iec61131::interfaces::Input::Output::Declarations_strategy = st.builds(
    iec61131::interfaces::Input::Output::Declarations,
)
iec61131::interfaces::Input::Declarations_strategy = st.builds(
    iec61131::interfaces::Input::Declarations,
    retain=
        st.booleans()
)
pous::Function::Vars_strategy = st.builds(
    pous::Function::Vars,
)
pous::Program::Vars_strategy = st.builds(
    pous::Program::Vars,
)
pous::Function::Block::Vars_strategy = st.builds(
    pous::Function::Block::Vars,
)
interfaces::Interface_strategy = st.builds(
    interfaces::Interface,
)
iec61131::interfaces::Other::Var::Declaration_strategy = st.builds(
    iec61131::interfaces::Other::Var::Declaration,
)
iec61131::interfaces::Io::Var::Declaration_strategy = st.builds(
    iec61131::interfaces::Io::Var::Declaration,
)
Initialized::Structure_strategy = st.builds(
    Initialized::Structure,
)
Array::Spec::Init_strategy = st.builds(
    Array::Spec::Init,
)
Var2::Init::Decl_strategy = st.builds(
    Var2::Init::Decl,
)
iec61131::interfaces::Structured::Var::Init::Decl_strategy = st.builds(
    iec61131::interfaces::Structured::Var::Init::Decl,
)
iec61131::interfaces::Array::Var::Init::Decl_strategy = st.builds(
    iec61131::interfaces::Array::Var::Init::Decl,
)
Enumerated::Value_strategy = st.builds(
    Enumerated::Value,
)
Enumerated::Specification_strategy = st.builds(
    Enumerated::Specification,
)
Signed::Integer_strategy = st.builds(
    Signed::Integer,
)
Subrange::Specification_strategy = st.builds(
    Subrange::Specification,
)
interfaces::Var1::Specification::Func_strategy = st.builds(
    interfaces::Var1::Specification::Func,
)
Simple::Specification_strategy = st.builds(
    Simple::Specification,
)
pous::Structure::Elements_strategy = st.builds(
    pous::Structure::Elements,
)
interfaces::Located::Var::Spec::Init_strategy = st.builds(
    interfaces::Located::Var::Spec::Init,
)
iec61131::interfaces::Initialized::Structure_strategy = st.builds(
    iec61131::interfaces::Initialized::Structure,
)
iec61131::interfaces::Array::Spec::Init_strategy = st.builds(
    iec61131::interfaces::Array::Spec::Init,
)
interfaces::Var1::Specification_strategy = st.builds(
    interfaces::Var1::Specification,
)
iec61131::interfaces::Enumerated::Spec::Init_strategy = st.builds(
    iec61131::interfaces::Enumerated::Spec::Init,
)
iec61131::interfaces::Subrange::Spec::Init_strategy = st.builds(
    iec61131::interfaces::Subrange::Spec::Init,
)
iec61131::interfaces::Simple::Spec::Init_strategy = st.builds(
    iec61131::interfaces::Simple::Spec::Init,
)
Assignment::Symbol_strategy = st.builds(
    Assignment::Symbol,
)
iec61131::interfaces::Var1::Specification_strategy = st.builds(
    iec61131::interfaces::Var1::Specification,
)
Bool::Type::Name_strategy = st.builds(
    Bool::Type::Name,
)
iec61131::interfaces::Edge::Declaration_strategy = st.builds(
    iec61131::interfaces::Edge::Declaration,
    edge=
        safe_text
)
operators::Divide::Operator_strategy = st.builds(
    operators::Divide::Operator,
)
Multiply::Operator_strategy = st.builds(
    Multiply::Operator,
)
iec61131::operators::Multiply::Symbol_strategy = st.builds(
    iec61131::operators::Multiply::Symbol,
)
iec61131::st::Else::If::Statement_strategy = st.builds(
    iec61131::st::Else::If::Statement,
)
Case::Element_strategy = st.builds(
    Case::Element,
)
iec61131::st::Case::Statement_strategy = st.builds(
    iec61131::st::Case::Statement,
)
Else::Statement_strategy = st.builds(
    Else::Statement,
)
Else::If::Statement_strategy = st.builds(
    Else::If::Statement,
)
Statement_strategy = st.builds(
    Statement,
)
Param::Assignment_strategy = st.builds(
    Param::Assignment,
)
iec61131::il::Il::Operand_strategy = st.builds(
    iec61131::il::Il::Operand,
)
iec61131::st::Param::Type1_strategy = st.builds(
    iec61131::st::Param::Type1,
)
iec61131::st::Param::Type2_strategy = st.builds(
    iec61131::st::Param::Type2,
)
iec61131::il::Param::Assignment2_strategy = st.builds(
    iec61131::il::Param::Assignment2,
)
Subprogram::Control::Statement_strategy = st.builds(
    Subprogram::Control::Statement,
)
iec61131::st::Fb::Invocation_strategy = st.builds(
    iec61131::st::Fb::Invocation,
)
iec61131::st::Return::Statement_strategy = st.builds(
    iec61131::st::Return::Statement,
)
iec61131::st::Iteration::Statement_strategy = st.builds(
    iec61131::st::Iteration::Statement,
)
iec61131::st::Selection::Statement_strategy = st.builds(
    iec61131::st::Selection::Statement,
)
iec61131::st::Subprogram::Control::Statement_strategy = st.builds(
    iec61131::st::Subprogram::Control::Statement,
)
Expression::Variable_strategy = st.builds(
    Expression::Variable,
)
iec61131::st::Assignment::Statement_strategy = st.builds(
    iec61131::st::Assignment::Statement,
)
Or::Operator_strategy = st.builds(
    Or::Operator,
)
Expression::Types_strategy = st.builds(
    Expression::Types,
)
iec61131::st::Power::Expression_strategy = st.builds(
    iec61131::st::Power::Expression,
)
iec61131::st::Comparison_strategy = st.builds(
    iec61131::st::Comparison,
)
iec61131::st::Equ::Expression_strategy = st.builds(
    iec61131::st::Equ::Expression,
)
iec61131::st::And::Expression_strategy = st.builds(
    iec61131::st::And::Expression,
)
iec61131::st::Xor::Expression_strategy = st.builds(
    iec61131::st::Xor::Expression,
)
iec61131::st::Term::Expression_strategy = st.builds(
    iec61131::st::Term::Expression,
)
iec61131::st::Primary::Expression_strategy = st.builds(
    iec61131::st::Primary::Expression,
)
iec61131::st::Add::Expression_strategy = st.builds(
    iec61131::st::Add::Expression,
)
iec61131::st::Unary::Expression_strategy = st.builds(
    iec61131::st::Unary::Expression,
)
iec61131::st::Expression_strategy = st.builds(
    iec61131::st::Expression,
)
iec61131::configurations::Prog::Data::Source_strategy = st.builds(
    iec61131::configurations::Prog::Data::Source,
)
iec61131::configurations::Prog::Conf::Element_strategy = st.builds(
    iec61131::configurations::Prog::Conf::Element,
)
Prog::Conf::Element_strategy = st.builds(
    Prog::Conf::Element,
)
iec61131::configurations::Prog::Cnxn_strategy = st.builds(
    iec61131::configurations::Prog::Cnxn,
)
iec61131::configurations::Fb::Task_strategy = st.builds(
    iec61131::configurations::Fb::Task,
)
iec61131::configurations::Prog::Conf::Elements_strategy = st.builds(
    iec61131::configurations::Prog::Conf::Elements,
)
Task::Initialization_strategy = st.builds(
    Task::Initialization,
)
iec61131::configurations::Priority_strategy = st.builds(
    iec61131::configurations::Priority,
)
iec61131::configurations::Interval_strategy = st.builds(
    iec61131::configurations::Interval,
)
iec61131::configurations::Single_strategy = st.builds(
    iec61131::configurations::Single,
)
iec61131::configurations::Instance::Specific::Init_strategy = st.builds(
    iec61131::configurations::Instance::Specific::Init,
)
iec61131::configurations::Data::Sink_strategy = st.builds(
    iec61131::configurations::Data::Sink,
)
Prog::Data::Source_strategy = st.builds(
    Prog::Data::Source,
)
Data::Sink_strategy = st.builds(
    Data::Sink,
)
Prog::Cnxn_strategy = st.builds(
    Prog::Cnxn,
)
iec61131::configurations::Prog::Source_strategy = st.builds(
    iec61131::configurations::Prog::Source,
)
iec61131::configurations::Prog::Sink_strategy = st.builds(
    iec61131::configurations::Prog::Sink,
)
Data::Source_strategy = st.builds(
    Data::Source,
)
iec61131::configurations::Program::Output::Reference_strategy = st.builds(
    iec61131::configurations::Program::Output::Reference,
)
configurations::Data::Sink_strategy = st.builds(
    configurations::Data::Sink,
)
iec61131::configurations::Data::Source_strategy = st.builds(
    iec61131::configurations::Data::Source,
)
Instance::Specific::Init_strategy = st.builds(
    Instance::Specific::Init,
)
iec61131::configurations::Instance::Spec2_strategy = st.builds(
    iec61131::configurations::Instance::Spec2,
)
iec61131::configurations::Instance::Spec1_strategy = st.builds(
    iec61131::configurations::Instance::Spec1,
)
iec61131::configurations::Instance::Specific::Initializations_strategy = st.builds(
    iec61131::configurations::Instance::Specific::Initializations,
)
iec61131::configurations::Task::Initialization_strategy = st.builds(
    iec61131::configurations::Task::Initialization,
)
iec61131::configurations::Task::Name_strategy = st.builds(
    iec61131::configurations::Task::Name,
    name=
        safe_text
)
iec61131::configurations::Program::Name_strategy = st.builds(
    iec61131::configurations::Program::Name,
    name=
        safe_text
)
iec61131::configurations::Access::Path_strategy = st.builds(
    iec61131::configurations::Access::Path,
)
iec61131::configurations::Access::Name_strategy = st.builds(
    iec61131::configurations::Access::Name,
    name=
        safe_text
)
Access::Path_strategy = st.builds(
    Access::Path,
)
iec61131::configurations::Symbolic::Path_strategy = st.builds(
    iec61131::configurations::Symbolic::Path,
)
iec61131::configurations::Direct::Path_strategy = st.builds(
    iec61131::configurations::Direct::Path,
)
iec61131::configurations::Access::Declaration_strategy = st.builds(
    iec61131::configurations::Access::Declaration,
    direction=
        safe_text
)
Access::Declaration_strategy = st.builds(
    Access::Declaration,
)
iec61131::configurations::Access::Declarations_strategy = st.builds(
    iec61131::configurations::Access::Declarations,
)
Resource::Declaration_strategy = st.builds(
    Resource::Declaration,
)
Access::Declarations_strategy = st.builds(
    Access::Declarations,
)
Instance::Specific::Initializations_strategy = st.builds(
    Instance::Specific::Initializations,
)
Global::Var::Declarations_strategy = st.builds(
    Global::Var::Declarations,
)
Single::Resource::Declaration_strategy = st.builds(
    Single::Resource::Declaration,
)
Configuration::Name_strategy = st.builds(
    Configuration::Name,
)
iec61131::configurations::Resource::Type::Name_strategy = st.builds(
    iec61131::configurations::Resource::Type::Name,
)
Prog::Conf::Elements_strategy = st.builds(
    Prog::Conf::Elements,
)
Program::Name_strategy = st.builds(
    Program::Name,
)
Single_strategy = st.builds(
    Single,
)
Priority_strategy = st.builds(
    Priority,
)
Task::Name_strategy = st.builds(
    Task::Name,
)
iec61131::configurations::Task::Configuration_strategy = st.builds(
    iec61131::configurations::Task::Configuration,
)
Program::Configuration_strategy = st.builds(
    Program::Configuration,
)
Task::Configuration_strategy = st.builds(
    Task::Configuration,
)
iec61131::configurations::Single::Resource::Declaration_strategy = st.builds(
    iec61131::configurations::Single::Resource::Declaration,
)
Resource::Type::Name_strategy = st.builds(
    Resource::Type::Name,
)
Resource::Name_strategy = st.builds(
    Resource::Name,
)
iec61131::configurations::Resource::Name_strategy = st.builds(
    iec61131::configurations::Resource::Name,
    name=
        safe_text
)
Simple::Type::Name_strategy = st.builds(
    Simple::Type::Name,
)
Single::Element::Type::Declaration_strategy = st.builds(
    Single::Element::Type::Declaration,
)
iec61131::pous::Subrange::Type::Declaration_strategy = st.builds(
    iec61131::pous::Subrange::Type::Declaration,
)
iec61131::pous::Simple::Type::Declaration_strategy = st.builds(
    iec61131::pous::Simple::Type::Declaration,
)
iec61131::configurations::Configuration::Name_strategy = st.builds(
    iec61131::configurations::Configuration::Name,
)
Function::Block::Declaration_strategy = st.builds(
    Function::Block::Declaration,
)
Function::Declaration_strategy = st.builds(
    Function::Declaration,
)
Program::Declaration_strategy = st.builds(
    Program::Declaration,
)
iec61131::pous::Library_strategy = st.builds(
    iec61131::pous::Library,
)
Program::Access::Decl_strategy = st.builds(
    Program::Access::Decl,
)
iec61131::pous::Function::Block::Vars_strategy = st.builds(
    iec61131::pous::Function::Block::Vars,
)
iec61131::pous::Function::Vars_strategy = st.builds(
    iec61131::pous::Function::Vars,
)
iec61131::pous::Program::Vars_strategy = st.builds(
    iec61131::pous::Program::Vars,
)
iec61131::pous::Structure::Elements_strategy = st.builds(
    iec61131::pous::Structure::Elements,
)
Structure::Elements_strategy = st.builds(
    Structure::Elements,
)
iec61131::pous::Structure::Element::Declaration_strategy = st.builds(
    iec61131::pous::Structure::Element::Declaration,
)
Structure::Element::Declaration_strategy = st.builds(
    Structure::Element::Declaration,
)
iec61131::pous::Structure::Specification_strategy = st.builds(
    iec61131::pous::Structure::Specification,
)
Enumerated::Spec::Init_strategy = st.builds(
    Enumerated::Spec::Init,
)
iec61131::pous::Enumerated::Type::Declaration_strategy = st.builds(
    iec61131::pous::Enumerated::Type::Declaration,
)
Subrange::Spec::Init_strategy = st.builds(
    Subrange::Spec::Init,
)
pous::Function::Block::Body_strategy = st.builds(
    pous::Function::Block::Body,
)
pous::Function::Body_strategy = st.builds(
    pous::Function::Body,
)
iec61131::ld::Ladder::Diagram_strategy = st.builds(
    iec61131::ld::Ladder::Diagram,
)
iec61131::st::Statement::List_strategy = st.builds(
    iec61131::st::Statement::List,
)
iec61131::il::Instruction::List_strategy = st.builds(
    iec61131::il::Instruction::List,
)
iec61131::fbd::Function::Block::Diagram_strategy = st.builds(
    iec61131::fbd::Function::Block::Diagram,
)
iec61131::pous::Other::Language_strategy = st.builds(
    iec61131::pous::Other::Language,
    text=
        safe_text
)
iec61131::pous::Function::Body_strategy = st.builds(
    iec61131::pous::Function::Body,
)
iec61131::pous::Function::Return::Value_strategy = st.builds(
    iec61131::pous::Function::Return::Value,
)
pous::Function::Name_strategy = st.builds(
    pous::Function::Name,
)
Function::Body_strategy = st.builds(
    Function::Body,
)
Function::Vars_strategy = st.builds(
    Function::Vars,
)
Byte::String::Type::Name_strategy = st.builds(
    Byte::String::Type::Name,
)
iec61131::types::Single::Byte::String::Type::Name_strategy = st.builds(
    iec61131::types::Single::Byte::String::Type::Name,
)
iec61131::types::Double::Byte::String::Type::Name_strategy = st.builds(
    iec61131::types::Double::Byte::String::Type::Name,
)
String::Type::Name_strategy = st.builds(
    String::Type::Name,
)
Structure::Specification_strategy = st.builds(
    Structure::Specification,
)
iec61131::pous::Structure::Declaration_strategy = st.builds(
    iec61131::pous::Structure::Declaration,
)
iec61131::pous::Type::Declaration_strategy = st.builds(
    iec61131::pous::Type::Declaration,
)
Type::Declaration_strategy = st.builds(
    Type::Declaration,
)
iec61131::pous::Structure::Type::Declaration_strategy = st.builds(
    iec61131::pous::Structure::Type::Declaration,
)
iec61131::pous::Array::Type::Declaration_strategy = st.builds(
    iec61131::pous::Array::Type::Declaration,
)
iec61131::pous::Single::Element::Type::Declaration_strategy = st.builds(
    iec61131::pous::Single::Element::Type::Declaration,
)
iec61131::pous::String::Type::Declaration_strategy = st.builds(
    iec61131::pous::String::Type::Declaration,
)
iec61131::pous::Function::Name_strategy = st.builds(
    iec61131::pous::Function::Name,
)
iec61131::pous::Access::Name_strategy = st.builds(
    iec61131::pous::Access::Name,
    name=
        safe_text
)
Symbolic::Variable_strategy = st.builds(
    Symbolic::Variable,
)
iec61131::variables::Multi::Element::Variable_strategy = st.builds(
    iec61131::variables::Multi::Element::Variable,
)
Access::Name_strategy = st.builds(
    Access::Name,
)
iec61131::pous::Program::Access::Decl_strategy = st.builds(
    iec61131::pous::Program::Access::Decl,
    direction=
        safe_text
)
iec61131::pous::Function::Block::Body_strategy = st.builds(
    iec61131::pous::Function::Block::Body,
)
Program::Type::Name_strategy = st.builds(
    Program::Type::Name,
)
Function::Return::Value_strategy = st.builds(
    Function::Return::Value,
)
Derived::Function::Name_strategy = st.builds(
    Derived::Function::Name,
)
Function::Block::Vars_strategy = st.builds(
    Function::Block::Vars,
)
Derived::Function::Block::Name_strategy = st.builds(
    Derived::Function::Block::Name,
)
pous::Function::Block::Type::Name_strategy = st.builds(
    pous::Function::Block::Type::Name,
)
types::Simple::Specification_strategy = st.builds(
    types::Simple::Specification,
)
iec61131::types::Elementary::Type::Name_strategy = st.builds(
    iec61131::types::Elementary::Type::Name,
)
iec61131::types::Simple::Type::Name_strategy = st.builds(
    iec61131::types::Simple::Type::Name,
)
iec61131::types::Generic::Type::Name_strategy = st.builds(
    iec61131::types::Generic::Type::Name,
)
Blocks_strategy = st.builds(
    Blocks,
)
iec61131::pous::Derived::Function::Block::Name_strategy = st.builds(
    iec61131::pous::Derived::Function::Block::Name,
)
iec61131::pous::Derived::Function::Name_strategy = st.builds(
    iec61131::pous::Derived::Function::Name,
)
iec61131::pous::Program::Type::Name_strategy = st.builds(
    iec61131::pous::Program::Type::Name,
)
Function::Block::Body_strategy = st.builds(
    Function::Block::Body,
)
iec61131::sfc::Sequential::Function::Chart_strategy = st.builds(
    iec61131::sfc::Sequential::Function::Chart,
)
iec61131::interfaces::InitElement::Array_strategy = st.builds(
    iec61131::interfaces::InitElement::Array,
)
iec61131::interfaces::Temp::Var::Declaration_strategy = st.builds(
    iec61131::interfaces::Temp::Var::Declaration,
)
iec61131::interfaces::InitElement::Structure_strategy = st.builds(
    iec61131::interfaces::InitElement::Structure,
)
iec61131::interfaces::Var1::Specification::Func_strategy = st.builds(
    iec61131::interfaces::Var1::Specification::Func,
)
iec61131::interfaces::Simple::Specification::Func_strategy = st.builds(
    iec61131::interfaces::Simple::Specification::Func,
)
Simple::Specification::Func_strategy = st.builds(
    Simple::Specification::Func,
)
Var1::Specification::Func_strategy = st.builds(
    Var1::Specification::Func,
)
iec61131::interfaces::Simple::Spec::Init::Func_strategy = st.builds(
    iec61131::interfaces::Simple::Spec::Init::Func,
)
iec61131::interfaces::Var::Init::Decl::Func_strategy = st.builds(
    iec61131::interfaces::Var::Init::Decl::Func,
)
Simple::Spec::Init_strategy = st.builds(
    Simple::Spec::Init,
)
iec61131::interfaces::Var::Name::Decl_strategy = st.builds(
    iec61131::interfaces::Var::Name::Decl,
)
iec61131::interfaces::Function::Var::Decl_strategy = st.builds(
    iec61131::interfaces::Function::Var::Decl,
    constant=
        st.booleans()
)
iec61131::interfaces::Var2::Init::Decl_strategy = st.builds(
    iec61131::interfaces::Var2::Init::Decl,
)
Array::Type::Name_strategy = st.builds(
    Array::Type::Name,
)
iec61131::interfaces::Array::Specification1_strategy = st.builds(
    iec61131::interfaces::Array::Specification1,
)
iec61131::interfaces::InitElement::EnumValue_strategy = st.builds(
    iec61131::interfaces::InitElement::EnumValue,
)
iec61131::interfaces::InitElement::Constant_strategy = st.builds(
    iec61131::interfaces::InitElement::Constant,
)
iec61131::interfaces::Initial::Element_strategy = st.builds(
    iec61131::interfaces::Initial::Element,
)
iec61131::interfaces::Array::Initial::Elements2_strategy = st.builds(
    iec61131::interfaces::Array::Initial::Elements2,
)
iec61131::interfaces::Array::Initial::Elements1_strategy = st.builds(
    iec61131::interfaces::Array::Initial::Elements1,
)
Non::Generic::Type::Name_strategy = st.builds(
    Non::Generic::Type::Name,
)
iec61131::types::Derived::Type::Name_strategy = st.builds(
    iec61131::types::Derived::Type::Name,
)
iec61131::interfaces::Array::Specification2_strategy = st.builds(
    iec61131::interfaces::Array::Specification2,
)
Global::Var::Decl_strategy = st.builds(
    Global::Var::Decl,
)
Library::Element::Declaration_strategy = st.builds(
    Library::Element::Declaration,
)
iec61131::configurations::Configuration::Declaration_strategy = st.builds(
    iec61131::configurations::Configuration::Declaration,
)
iec61131::pous::Function::Declaration_strategy = st.builds(
    iec61131::pous::Function::Declaration,
)
iec61131::pous::Function::Block::Declaration_strategy = st.builds(
    iec61131::pous::Function::Block::Declaration,
)
iec61131::configurations::Resource::Declaration_strategy = st.builds(
    iec61131::configurations::Resource::Declaration,
)
iec61131::pous::Data::Type::Declaration_strategy = st.builds(
    iec61131::pous::Data::Type::Declaration,
)
iec61131::pous::Program::Declaration_strategy = st.builds(
    iec61131::pous::Program::Declaration,
)
iec61131::interfaces::Global::Var::Declarations_strategy = st.builds(
    iec61131::interfaces::Global::Var::Declarations,
    retain=
        st.booleans(),
    constant=
        st.booleans()
)
Located::Var::Decl_strategy = st.builds(
    Located::Var::Decl,
)
Program::Vars_strategy = st.builds(
    Program::Vars,
)
iec61131::pous::Program::Access::Decls_strategy = st.builds(
    iec61131::pous::Program::Access::Decls,
)
iec61131::interfaces::Located::Var::Declarations_strategy = st.builds(
    iec61131::interfaces::Located::Var::Declarations,
    retain=
        st.booleans(),
    constant=
        st.booleans()
)
iec61131::interfaces::Enumerated::Specification2_strategy = st.builds(
    iec61131::interfaces::Enumerated::Specification2,
)
iec61131::interfaces::Enumerated::Specification1_strategy = st.builds(
    iec61131::interfaces::Enumerated::Specification1,
)
Subrange::Type::Name_strategy = st.builds(
    Subrange::Type::Name,
)
iec61131::interfaces::Subrange::Specification2_strategy = st.builds(
    iec61131::interfaces::Subrange::Specification2,
)
Subrange_strategy = st.builds(
    Subrange,
)
iec61131::interfaces::Subrange::Specification1_strategy = st.builds(
    iec61131::interfaces::Subrange::Specification1,
)
Double::Byte::String::Type::Name_strategy = st.builds(
    Double::Byte::String::Type::Name,
)
Single::Byte::String::Type::Name_strategy = st.builds(
    Single::Byte::String::Type::Name,
)
Byte::String_strategy = st.builds(
    Byte::String,
)
iec61131::interfaces::Double::BString_strategy = st.builds(
    iec61131::interfaces::Double::BString,
)
iec61131::interfaces::Single::BString_strategy = st.builds(
    iec61131::interfaces::Single::BString,
)
iec61131::interfaces::Byte::String_strategy = st.builds(
    iec61131::interfaces::Byte::String,
)
iec61131::interfaces::Range_strategy = st.builds(
    iec61131::interfaces::Range,
)
iec61131::interfaces::Input::Declaration_strategy = st.builds(
    iec61131::interfaces::Input::Declaration,
)
iec61131::interfaces::Global::Var::Location_strategy = st.builds(
    iec61131::interfaces::Global::Var::Location,
)
iec61131::interfaces::Global::Var::Spec_strategy = st.builds(
    iec61131::interfaces::Global::Var::Spec,
)
External::Specification_strategy = st.builds(
    External::Specification,
)
Global::Var::Name_strategy = st.builds(
    Global::Var::Name,
)
iec61131::interfaces::External::Declaration_strategy = st.builds(
    iec61131::interfaces::External::Declaration,
)
RNV::Declarations_strategy = st.builds(
    RNV::Declarations,
)
iec61131::interfaces::Var::Declarations_strategy = st.builds(
    iec61131::interfaces::Var::Declarations,
    constant=
        st.booleans()
)
iec61131::interfaces::Non::Retentive::Var::Declarations_strategy = st.builds(
    iec61131::interfaces::Non::Retentive::Var::Declarations,
)
iec61131::interfaces::Retentive::Var::Declarations_strategy = st.builds(
    iec61131::interfaces::Retentive::Var::Declarations,
)
External::Declaration_strategy = st.builds(
    External::Declaration,
)
Other::Var::Declaration_strategy = st.builds(
    Other::Var::Declaration,
)
iec61131::interfaces::RNV::Declarations_strategy = st.builds(
    iec61131::interfaces::RNV::Declarations,
)
iec61131::interfaces::Temp::Var::Decls_strategy = st.builds(
    iec61131::interfaces::Temp::Var::Decls,
)
iec61131::interfaces::External::Var::Declarations_strategy = st.builds(
    iec61131::interfaces::External::Var::Declarations,
    constant=
        st.booleans()
)
iec61131::interfaces::Incompl::Located::Var::Declarations_strategy = st.builds(
    iec61131::interfaces::Incompl::Located::Var::Declarations,
    retain=
        st.booleans()
)
operators::Multiply::Operator_strategy = st.builds(
    operators::Multiply::Operator,
)
operators::Add::Operator_strategy = st.builds(
    operators::Add::Operator,
)
operators::Arithmetic::Name_strategy = st.builds(
    operators::Arithmetic::Name,
)
iec61131::operators::Divide::Name_strategy = st.builds(
    iec61131::operators::Divide::Name,
)
iec61131::operators::Multiply::Name_strategy = st.builds(
    iec61131::operators::Multiply::Name,
)
operators::Addition::Operator_strategy = st.builds(
    operators::Addition::Operator,
)
iec61131::operators::Addition::Symbol_strategy = st.builds(
    iec61131::operators::Addition::Symbol,
)
iec61131::operators::Addition::Name_strategy = st.builds(
    iec61131::operators::Addition::Name,
)
Comparison::Operator_strategy = st.builds(
    Comparison::Operator,
)
iec61131::operators::LessEqual::Operator_strategy = st.builds(
    iec61131::operators::LessEqual::Operator,
)
iec61131::operators::GreaterEqual::Operator_strategy = st.builds(
    iec61131::operators::GreaterEqual::Operator,
)
iec61131::operators::Greater::Operator_strategy = st.builds(
    iec61131::operators::Greater::Operator,
)
iec61131::operators::Less::Operator_strategy = st.builds(
    iec61131::operators::Less::Operator,
)
Il::Expr::Operator_strategy = st.builds(
    Il::Expr::Operator,
)
iec61131::operators::Arithmetic::Name_strategy = st.builds(
    iec61131::operators::Arithmetic::Name,
)
iec61131::operators::Comparison::Name_strategy = st.builds(
    iec61131::operators::Comparison::Name,
)
operators::Substraction::Operator_strategy = st.builds(
    operators::Substraction::Operator,
)
iec61131::operators::Substraction::Name_strategy = st.builds(
    iec61131::operators::Substraction::Name,
)
GreaterEqual::Operator_strategy = st.builds(
    GreaterEqual::Operator,
)
iec61131::operators::GreaterEqual::Symbol_strategy = st.builds(
    iec61131::operators::GreaterEqual::Symbol,
)
operators::GreaterEqual::Operator_strategy = st.builds(
    operators::GreaterEqual::Operator,
)
Greater::Operator_strategy = st.builds(
    Greater::Operator,
)
iec61131::operators::Greater::Symbol_strategy = st.builds(
    iec61131::operators::Greater::Symbol,
)
operators::Greater::Operator_strategy = st.builds(
    operators::Greater::Operator,
)
LessEqual::Operator_strategy = st.builds(
    LessEqual::Operator,
)
iec61131::operators::LessEqual::Symbol_strategy = st.builds(
    iec61131::operators::LessEqual::Symbol,
)
operators::LessEqual::Operator_strategy = st.builds(
    operators::LessEqual::Operator,
)
Less::Operator_strategy = st.builds(
    Less::Operator,
)
iec61131::operators::Less::Symbol_strategy = st.builds(
    iec61131::operators::Less::Symbol,
)
operators::Less::Operator_strategy = st.builds(
    operators::Less::Operator,
)
Unequal::Operator_strategy = st.builds(
    Unequal::Operator,
)
iec61131::operators::Unequal::Symbol_strategy = st.builds(
    iec61131::operators::Unequal::Symbol,
)
operators::Unequal::Operator_strategy = st.builds(
    operators::Unequal::Operator,
)
Equal::Operator_strategy = st.builds(
    Equal::Operator,
)
iec61131::operators::Equal::Symbol_strategy = st.builds(
    iec61131::operators::Equal::Symbol,
)
operators::Comparison::Name_strategy = st.builds(
    operators::Comparison::Name,
)
iec61131::operators::Unequal::Name_strategy = st.builds(
    iec61131::operators::Unequal::Name,
)
iec61131::operators::GreaterEqual::Name_strategy = st.builds(
    iec61131::operators::GreaterEqual::Name,
)
iec61131::operators::Greater::Name_strategy = st.builds(
    iec61131::operators::Greater::Name,
)
iec61131::operators::LessEqual::Name_strategy = st.builds(
    iec61131::operators::LessEqual::Name,
)
iec61131::operators::Less::Name_strategy = st.builds(
    iec61131::operators::Less::Name,
)
operators::Equal::Operator_strategy = st.builds(
    operators::Equal::Operator,
)
iec61131::operators::Equal::Name_strategy = st.builds(
    iec61131::operators::Equal::Name,
)
And::Operator_strategy = st.builds(
    And::Operator,
)
iec61131::operators::And::Name_strategy = st.builds(
    iec61131::operators::And::Name,
)
iec61131::operators::And::Symbol_strategy = st.builds(
    iec61131::operators::And::Symbol,
)
Assignment::Operator_strategy = st.builds(
    Assignment::Operator,
)
iec61131::operators::Assignment::Name_strategy = st.builds(
    iec61131::operators::Assignment::Name,
)
iec61131::operators::Assignment::Symbol_strategy = st.builds(
    iec61131::operators::Assignment::Symbol,
)
Power::Operator_strategy = st.builds(
    Power::Operator,
)
iec61131::operators::Power::Name_strategy = st.builds(
    iec61131::operators::Power::Name,
)
iec61131::operators::Power::Symbol_strategy = st.builds(
    iec61131::operators::Power::Symbol,
)
Divide::Operator_strategy = st.builds(
    Divide::Operator,
)
iec61131::operators::Divide::Symbol_strategy = st.builds(
    iec61131::operators::Divide::Symbol,
)
iec61131::literals::Integer_strategy = st.builds(
    iec61131::literals::Integer,
    value=
        safe_text
)
iec61131::literals::BSInteger_strategy = st.builds(
    iec61131::literals::BSInteger,
)
iec61131::literals::Date::Literal_strategy = st.builds(
    iec61131::literals::Date::Literal,
    month=
        safe_text,
    day=
        safe_text,
    year=
        safe_text
)
iec61131::literals::Daytime_strategy = st.builds(
    iec61131::literals::Daytime,
    hour=
        safe_text,
    minute=
        safe_text
)
iec61131::literals::Fixed::Point::Literal_strategy = st.builds(
    iec61131::literals::Fixed::Point::Literal,
)
Double::Byte::Character::Representation_strategy = st.builds(
    Double::Byte::Character::Representation,
)
operators::Dot::Operator_strategy = st.builds(
    operators::Dot::Operator,
)
il::Il::Simple::Operator_strategy = st.builds(
    il::Il::Simple::Operator,
)
operators::Unary::Operator_strategy = st.builds(
    operators::Unary::Operator,
)
iec61131::operators::Substraction::Symbol_strategy = st.builds(
    iec61131::operators::Substraction::Symbol,
)
iec61131::operators::Not::Operator_strategy = st.builds(
    iec61131::operators::Not::Operator,
)
il::Il::Expr::Operator_strategy = st.builds(
    il::Il::Expr::Operator,
)
iec61131::operators::Modulo::Operator_strategy = st.builds(
    iec61131::operators::Modulo::Operator,
)
operators::Operator_strategy = st.builds(
    operators::Operator,
)
iec61131::operators::Xor::Operator_strategy = st.builds(
    iec61131::operators::Xor::Operator,
)
iec61131::operators::Or::Operator_strategy = st.builds(
    iec61131::operators::Or::Operator,
)
iec61131::operators::And::Operator_strategy = st.builds(
    iec61131::operators::And::Operator,
)
EquUequ::Operator_strategy = st.builds(
    EquUequ::Operator,
)
iec61131::operators::Unequal::Operator_strategy = st.builds(
    iec61131::operators::Unequal::Operator,
)
iec61131::operators::Equal::Operator_strategy = st.builds(
    iec61131::operators::Equal::Operator,
)
Dot::Operator_strategy = st.builds(
    Dot::Operator,
)
iec61131::operators::Divide::Operator_strategy = st.builds(
    iec61131::operators::Divide::Operator,
)
iec61131::operators::Multiply::Operator_strategy = st.builds(
    iec61131::operators::Multiply::Operator,
)
iec61131::operators::Substraction::Operator_strategy = st.builds(
    iec61131::operators::Substraction::Operator,
)
iec61131::operators::Addition::Operator_strategy = st.builds(
    iec61131::operators::Addition::Operator,
)
Operator_strategy = st.builds(
    Operator,
)
iec61131::operators::Dot::Operator_strategy = st.builds(
    iec61131::operators::Dot::Operator,
)
iec61131::operators::EquUequ::Operator_strategy = st.builds(
    iec61131::operators::EquUequ::Operator,
)
iec61131::operators::Unary::Operator_strategy = st.builds(
    iec61131::operators::Unary::Operator,
)
iec61131::operators::Comparison::Operator_strategy = st.builds(
    iec61131::operators::Comparison::Operator,
)
iec61131::operators::Assignment::Operator_strategy = st.builds(
    iec61131::operators::Assignment::Operator,
)
iec61131::operators::Power::Operator_strategy = st.builds(
    iec61131::operators::Power::Operator,
)
iec61131::operators::Add::Operator_strategy = st.builds(
    iec61131::operators::Add::Operator,
)
iec61131::operators::Operator_strategy = st.builds(
    iec61131::operators::Operator,
)
iec61131::literals::Double::Byte::Character::Representation_strategy = st.builds(
    iec61131::literals::Double::Byte::Character::Representation,
    value=
        safe_text
)
Common::Character::Representation_strategy = st.builds(
    Common::Character::Representation,
)
iec61131::literals::Single::Byte::Character::Representation_strategy = st.builds(
    iec61131::literals::Single::Byte::Character::Representation,
    value=
        safe_text
)
iec61131::literals::Common::Character::Representation_strategy = st.builds(
    iec61131::literals::Common::Character::Representation,
    value=
        safe_text
)
DT::Type::Name_strategy = st.builds(
    DT::Type::Name,
)
Date::Literal_strategy = st.builds(
    Date::Literal,
)
Date::Type::Name_strategy = st.builds(
    Date::Type::Name,
)
iec61131::types::DT::Type::Name_strategy = st.builds(
    iec61131::types::DT::Type::Name,
)
iec61131::types::TOD::Type::Name_strategy = st.builds(
    iec61131::types::TOD::Type::Name,
)
Single::Byte::Character::Representation_strategy = st.builds(
    Single::Byte::Character::Representation,
)
Character::String_strategy = st.builds(
    Character::String,
)
iec61131::literals::Double::Byte::Character::String_strategy = st.builds(
    iec61131::literals::Double::Byte::Character::String,
)
iec61131::literals::Single::Byte::Character::String_strategy = st.builds(
    iec61131::literals::Single::Byte::Character::String,
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
Unsigned::Integer_strategy = st.builds(
    Unsigned::Integer,
)
Fixed::Point::Literal_strategy = st.builds(
    Fixed::Point::Literal,
)
iec61131::literals::Fixed::Point_strategy = st.builds(
    iec61131::literals::Fixed::Point,
    valuePre=
        safe_text,
    valuePost=
        safe_text
)
iec61131::literals::Interval_strategy = st.builds(
    iec61131::literals::Interval,
)
literals::Fixed::Point::Literal_strategy = st.builds(
    literals::Fixed::Point::Literal,
)
Integer_strategy = st.builds(
    Integer,
)
Numeric::Literal_strategy = st.builds(
    Numeric::Literal,
)
iec61131::literals::Integer::Literal_strategy = st.builds(
    iec61131::literals::Integer::Literal,
)
Bit::String::Type::Name_strategy = st.builds(
    Bit::String::Type::Name,
)
iec61131::types::Bool::Type::Name_strategy = st.builds(
    iec61131::types::Bool::Type::Name,
)
BSInteger_strategy = st.builds(
    BSInteger,
)
Constant_strategy = st.builds(
    Constant,
)
iec61131::literals::Bit::String::Literal_strategy = st.builds(
    iec61131::literals::Bit::String::Literal,
)
iec61131::literals::Character::String_strategy = st.builds(
    iec61131::literals::Character::String,
)
iec61131::literals::Time::Literal_strategy = st.builds(
    iec61131::literals::Time::Literal,
)
iec61131::literals::Numeric::Literal_strategy = st.builds(
    iec61131::literals::Numeric::Literal,
)
TOD::Type::Name_strategy = st.builds(
    TOD::Type::Name,
)
Daytime_strategy = st.builds(
    Daytime,
)
Time::Literal_strategy = st.builds(
    Time::Literal,
)
iec61131::literals::Date::And::Time_strategy = st.builds(
    iec61131::literals::Date::And::Time,
)
iec61131::literals::Date_strategy = st.builds(
    iec61131::literals::Date,
)
iec61131::literals::Time::Of::Day_strategy = st.builds(
    iec61131::literals::Time::Of::Day,
)
Substraction::Operator_strategy = st.builds(
    Substraction::Operator,
)
Duration::Type::Name_strategy = st.builds(
    Duration::Type::Name,
)
Interval_strategy = st.builds(
    Interval,
)
iec61131::literals::Days_strategy = st.builds(
    iec61131::literals::Days,
)
iec61131::literals::Milliseconds_strategy = st.builds(
    iec61131::literals::Milliseconds,
)
iec61131::literals::Seconds_strategy = st.builds(
    iec61131::literals::Seconds,
)
iec61131::literals::Minutes_strategy = st.builds(
    iec61131::literals::Minutes,
)
iec61131::literals::Hours_strategy = st.builds(
    iec61131::literals::Hours,
)
sfc::Action::Time_strategy = st.builds(
    sfc::Action::Time,
)
literals::Time::Literal_strategy = st.builds(
    literals::Time::Literal,
)
iec61131::literals::Duration_strategy = st.builds(
    iec61131::literals::Duration,
)
literals::BSInteger_strategy = st.builds(
    literals::BSInteger,
)
interfaces::Range_strategy = st.builds(
    interfaces::Range,
)
st::Case::List::Element_strategy = st.builds(
    st::Case::List::Element,
)
literals::Integer_strategy = st.builds(
    literals::Integer,
)
iec61131::literals::Binary::Integer_strategy = st.builds(
    iec61131::literals::Binary::Integer,
)
iec61131::literals::Octal::Integer_strategy = st.builds(
    iec61131::literals::Octal::Integer,
)
iec61131::literals::Hex::Integer_strategy = st.builds(
    iec61131::literals::Hex::Integer,
)
iec61131::literals::Unsigned::Integer_strategy = st.builds(
    iec61131::literals::Unsigned::Integer,
)
iec61131::literals::Signed::Integer_strategy = st.builds(
    iec61131::literals::Signed::Integer,
    negative=
        st.booleans()
)
il::Il::Operand_strategy = st.builds(
    il::Il::Operand,
)
configurations::Prog::Data::Source_strategy = st.builds(
    configurations::Prog::Data::Source,
)
iec61131::interfaces::Enumerated::Value_strategy = st.builds(
    iec61131::interfaces::Enumerated::Value,
    name=
        safe_text
)
configurations::Data::Source_strategy = st.builds(
    configurations::Data::Source,
)
iec61131::configurations::Global::Var::Reference_strategy = st.builds(
    iec61131::configurations::Global::Var::Reference,
)
iec61131::variables::Direct::Variable_strategy = st.builds(
    iec61131::variables::Direct::Variable,
    value=
        safe_text
)
iec61131::literals::Constant_strategy = st.builds(
    iec61131::literals::Constant,
)
iec61131::literals::Boolean::Literal_strategy = st.builds(
    iec61131::literals::Boolean::Literal,
    value=
        safe_text
)
Fixed::Point_strategy = st.builds(
    Fixed::Point,
)
Real::Type::Name_strategy = st.builds(
    Real::Type::Name,
)
iec61131::literals::Real::Literal_strategy = st.builds(
    iec61131::literals::Real::Literal,
    negative=
        st.booleans(),
    exponent=
        safe_text
)
Integer::Type::Name_strategy = st.builds(
    Integer::Type::Name,
)
iec61131::types::Signed::Integer::Type::Name_strategy = st.builds(
    iec61131::types::Signed::Integer::Type::Name,
)
iec61131::types::Unsigned::Integer::Type::Name_strategy = st.builds(
    iec61131::types::Unsigned::Integer::Type::Name,
)
iec61131::NamedElement_strategy = st.builds(
    iec61131::NamedElement,
    name=
        safe_text
)
iec61131::Commentable_strategy = st.builds(
    iec61131::Commentable,
    comments=
        safe_text
)
NamedElement_strategy = st.builds(
    NamedElement,
)
iec61131::variables::Variable::Name_strategy = st.builds(
    iec61131::variables::Variable::Name,
)
iec61131::sfc::Step::Name_strategy = st.builds(
    iec61131::sfc::Step::Name,
)
Commentable_strategy = st.builds(
    Commentable,
)
iec61131::st::Param::Assignment_strategy = st.builds(
    iec61131::st::Param::Assignment,
)
iec61131::st::Statement_strategy = st.builds(
    iec61131::st::Statement,
)
iec61131::configurations::Program::Configuration_strategy = st.builds(
    iec61131::configurations::Program::Configuration,
    retain=
        st.booleans()
)
iec61131::interfaces::Interface_strategy = st.builds(
    iec61131::interfaces::Interface,
)
iec61131::st::Expression::Variable_strategy = st.builds(
    iec61131::st::Expression::Variable,
)
iec61131::interfaces::Global::Var::Name_strategy = st.builds(
    iec61131::interfaces::Global::Var::Name,
)
iec61131::variables::Variable_strategy = st.builds(
    iec61131::variables::Variable,
)
iec61131::st::Expression::Types_strategy = st.builds(
    iec61131::st::Expression::Types,
)
iec61131::pous::Function::Block::Type::Name_strategy = st.builds(
    iec61131::pous::Function::Block::Type::Name,
)
iec61131::interfaces::Global::Var::Decl_strategy = st.builds(
    iec61131::interfaces::Global::Var::Decl,
)
iec61131::Library::Element::Name_strategy = st.builds(
    iec61131::Library::Element::Name,
)
iec61131::Library::Element::Declaration_strategy = st.builds(
    iec61131::Library::Element::Declaration,
)
iec61131::IEC61131_strategy = st.builds(
    iec61131::IEC61131,
)

@given(instance=iec61131::sfc::Action::Qualifier_strategy)
@settings(max_examples=50)
def test_iec61131::sfc::action::qualifier_instantiation(instance):
    assert isinstance(instance, iec61131::sfc::Action::Qualifier)

@given(instance=iec61131::sfc::Action::Qualifier_strategy)
def test_iec61131::sfc::action::qualifier_qualifier_type(instance):
    assert isinstance(instance.qualifier, str)


@given(instance=iec61131::sfc::Action::Qualifier_strategy)
def test_iec61131::sfc::action::qualifier_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original

@given(instance=iec61131::sfc::Action::Name_strategy)
@settings(max_examples=50)
def test_iec61131::sfc::action::name_instantiation(instance):
    assert isinstance(instance, iec61131::sfc::Action::Name)

@given(instance=iec61131::sfc::Action::Name_strategy)
def test_iec61131::sfc::action::name_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iec61131::sfc::Action::Name_strategy)
def test_iec61131::sfc::action::name_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Step::Name_strategy)
@settings(max_examples=50)
def test_step::name_instantiation(instance):
    assert isinstance(instance, Step::Name)

@given(instance=Action::Association_strategy)
@settings(max_examples=50)
def test_action::association_instantiation(instance):
    assert isinstance(instance, Action::Association)

@given(instance=iec61131::sfc::Step::Types_strategy)
@settings(max_examples=50)
def test_iec61131::sfc::step::types_instantiation(instance):
    assert isinstance(instance, iec61131::sfc::Step::Types)

@given(instance=Action::Qualifier_strategy)
@settings(max_examples=50)
def test_action::qualifier_instantiation(instance):
    assert isinstance(instance, Action::Qualifier)

@given(instance=iec61131::sfc::Action::Association_strategy)
@settings(max_examples=50)
def test_iec61131::sfc::action::association_instantiation(instance):
    assert isinstance(instance, iec61131::sfc::Action::Association)

@given(instance=iec61131::sfc::Sfc::Elements_strategy)
@settings(max_examples=50)
def test_iec61131::sfc::sfc::elements_instantiation(instance):
    assert isinstance(instance, iec61131::sfc::Sfc::Elements)

@given(instance=Action::Name_strategy)
@settings(max_examples=50)
def test_action::name_instantiation(instance):
    assert isinstance(instance, Action::Name)

@given(instance=Transition::Condition_strategy)
@settings(max_examples=50)
def test_transition::condition_instantiation(instance):
    assert isinstance(instance, Transition::Condition)

@given(instance=iec61131::sfc::Sfc::Network_strategy)
@settings(max_examples=50)
def test_iec61131::sfc::sfc::network_instantiation(instance):
    assert isinstance(instance, iec61131::sfc::Sfc::Network)

@given(instance=Sfc::Network_strategy)
@settings(max_examples=50)
def test_sfc::network_instantiation(instance):
    assert isinstance(instance, Sfc::Network)

@given(instance=iec61131::il::Il::Assign::Out::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::il::il::assign::out::operator_instantiation(instance):
    assert isinstance(instance, iec61131::il::Il::Assign::Out::Operator)

@given(instance=iec61131::il::Param::Assignment_strategy)
@settings(max_examples=50)
def test_iec61131::il::param::assignment_instantiation(instance):
    assert isinstance(instance, iec61131::il::Param::Assignment)

@given(instance=Assignment::Name_strategy)
@settings(max_examples=50)
def test_assignment::name_instantiation(instance):
    assert isinstance(instance, Assignment::Name)

@given(instance=iec61131::il::Il::Assign::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::il::il::assign::operator_instantiation(instance):
    assert isinstance(instance, iec61131::il::Il::Assign::Operator)

@given(instance=iec61131::il::Param::Instruction_strategy)
@settings(max_examples=50)
def test_iec61131::il::param::instruction_instantiation(instance):
    assert isinstance(instance, iec61131::il::Param::Instruction)

@given(instance=iec61131::il::Param::Assignments_strategy)
@settings(max_examples=50)
def test_iec61131::il::param::assignments_instantiation(instance):
    assert isinstance(instance, iec61131::il::Param::Assignments)

@given(instance=Il::Assign::Out::Operator_strategy)
@settings(max_examples=50)
def test_il::assign::out::operator_instantiation(instance):
    assert isinstance(instance, Il::Assign::Out::Operator)

@given(instance=iec61131::il::Il::Operand::List_strategy)
@settings(max_examples=50)
def test_iec61131::il::il::operand::list_instantiation(instance):
    assert isinstance(instance, iec61131::il::Il::Operand::List)

@given(instance=iec61131::il::Il::Simple::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::il::il::simple::operator_instantiation(instance):
    assert isinstance(instance, iec61131::il::Il::Simple::Operator)

@given(instance=iec61131::il::Il::Operations_strategy)
@settings(max_examples=50)
def test_iec61131::il::il::operations_instantiation(instance):
    assert isinstance(instance, iec61131::il::Il::Operations)

@given(instance=Il::Param::List_strategy)
@settings(max_examples=50)
def test_il::param::list_instantiation(instance):
    assert isinstance(instance, Il::Param::List)

@given(instance=Il::Assign::Operator_strategy)
@settings(max_examples=50)
def test_il::assign::operator_instantiation(instance):
    assert isinstance(instance, Il::Assign::Operator)

@given(instance=Param::Assignments_strategy)
@settings(max_examples=50)
def test_param::assignments_instantiation(instance):
    assert isinstance(instance, Param::Assignments)

@given(instance=iec61131::il::Il::Param::Out::Assignment_strategy)
@settings(max_examples=50)
def test_iec61131::il::il::param::out::assignment_instantiation(instance):
    assert isinstance(instance, iec61131::il::Il::Param::Out::Assignment)

@given(instance=iec61131::il::Il::Param::Assignment_strategy)
@settings(max_examples=50)
def test_iec61131::il::il::param::assignment_instantiation(instance):
    assert isinstance(instance, iec61131::il::Il::Param::Assignment)

@given(instance=Param::Instruction_strategy)
@settings(max_examples=50)
def test_param::instruction_instantiation(instance):
    assert isinstance(instance, Param::Instruction)

@given(instance=iec61131::il::Il::Param::Last::Instruction_strategy)
@settings(max_examples=50)
def test_iec61131::il::il::param::last::instruction_instantiation(instance):
    assert isinstance(instance, iec61131::il::Il::Param::Last::Instruction)

@given(instance=iec61131::il::Il::Param::Instruction_strategy)
@settings(max_examples=50)
def test_iec61131::il::il::param::instruction_instantiation(instance):
    assert isinstance(instance, iec61131::il::Il::Param::Instruction)

@given(instance=iec61131::il::Simple::Instr_strategy)
@settings(max_examples=50)
def test_iec61131::il::simple::instr_instantiation(instance):
    assert isinstance(instance, iec61131::il::Simple::Instr)

@given(instance=Simple::Instr_strategy)
@settings(max_examples=50)
def test_simple::instr_instantiation(instance):
    assert isinstance(instance, Simple::Instr)

@given(instance=iec61131::il::Il::Simple::Instruction_strategy)
@settings(max_examples=50)
def test_iec61131::il::il::simple::instruction_instantiation(instance):
    assert isinstance(instance, iec61131::il::Il::Simple::Instruction)

@given(instance=iec61131::il::Operands_strategy)
@settings(max_examples=50)
def test_iec61131::il::operands_instantiation(instance):
    assert isinstance(instance, iec61131::il::Operands)

@given(instance=Il::Param::Last::Instruction_strategy)
@settings(max_examples=50)
def test_il::param::last::instruction_instantiation(instance):
    assert isinstance(instance, Il::Param::Last::Instruction)

@given(instance=Il::Param::Instruction_strategy)
@settings(max_examples=50)
def test_il::param::instruction_instantiation(instance):
    assert isinstance(instance, Il::Param::Instruction)

@given(instance=iec61131::il::Il::Param::List_strategy)
@settings(max_examples=50)
def test_iec61131::il::il::param::list_instantiation(instance):
    assert isinstance(instance, iec61131::il::Il::Param::List)

@given(instance=iec61131::il::Il::Call::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::il::il::call::operator_instantiation(instance):
    assert isinstance(instance, iec61131::il::Il::Call::Operator)

@given(instance=iec61131::il::Il::Jump::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::il::il::jump::operator_instantiation(instance):
    assert isinstance(instance, iec61131::il::Il::Jump::Operator)

@given(instance=Il::Operand::List_strategy)
@settings(max_examples=50)
def test_il::operand::list_instantiation(instance):
    assert isinstance(instance, Il::Operand::List)

@given(instance=Il::Simple::Operator_strategy)
@settings(max_examples=50)
def test_il::simple::operator_instantiation(instance):
    assert isinstance(instance, Il::Simple::Operator)

@given(instance=iec61131::il::Il::Expr::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::il::il::expr::operator_instantiation(instance):
    assert isinstance(instance, iec61131::il::Il::Expr::Operator)

@given(instance=Il::Simple::Operation_strategy)
@settings(max_examples=50)
def test_il::simple::operation_instantiation(instance):
    assert isinstance(instance, Il::Simple::Operation)

@given(instance=iec61131::il::Simple::Operation2_strategy)
@settings(max_examples=50)
def test_iec61131::il::simple::operation2_instantiation(instance):
    assert isinstance(instance, iec61131::il::Simple::Operation2)

@given(instance=iec61131::il::Simple::Operation1_strategy)
@settings(max_examples=50)
def test_iec61131::il::simple::operation1_instantiation(instance):
    assert isinstance(instance, iec61131::il::Simple::Operation1)

@given(instance=Il::Instruction_strategy)
@settings(max_examples=50)
def test_il::instruction_instantiation(instance):
    assert isinstance(instance, Il::Instruction)

@given(instance=Operands_strategy)
@settings(max_examples=50)
def test_operands_instantiation(instance):
    assert isinstance(instance, Operands)

@given(instance=iec61131::il::Operand2_strategy)
@settings(max_examples=50)
def test_iec61131::il::operand2_instantiation(instance):
    assert isinstance(instance, iec61131::il::Operand2)

@given(instance=iec61131::il::Operand1_strategy)
@settings(max_examples=50)
def test_iec61131::il::operand1_instantiation(instance):
    assert isinstance(instance, iec61131::il::Operand1)

@given(instance=Il::Call::Operator_strategy)
@settings(max_examples=50)
def test_il::call::operator_instantiation(instance):
    assert isinstance(instance, Il::Call::Operator)

@given(instance=Il::Jump::Operator_strategy)
@settings(max_examples=50)
def test_il::jump::operator_instantiation(instance):
    assert isinstance(instance, Il::Jump::Operator)

@given(instance=Simple::Instr::List_strategy)
@settings(max_examples=50)
def test_simple::instr::list_instantiation(instance):
    assert isinstance(instance, Simple::Instr::List)

@given(instance=Il::Operand_strategy)
@settings(max_examples=50)
def test_il::operand_instantiation(instance):
    assert isinstance(instance, Il::Operand)

@given(instance=il::Simple::Instr_strategy)
@settings(max_examples=50)
def test_il::simple::instr_instantiation(instance):
    assert isinstance(instance, il::Simple::Instr)

@given(instance=il::Il::Operations_strategy)
@settings(max_examples=50)
def test_il::il::operations_instantiation(instance):
    assert isinstance(instance, il::Il::Operations)

@given(instance=iec61131::il::Il::Expression_strategy)
@settings(max_examples=50)
def test_iec61131::il::il::expression_instantiation(instance):
    assert isinstance(instance, iec61131::il::Il::Expression)

@given(instance=iec61131::il::Il::Formal::Funct::Call_strategy)
@settings(max_examples=50)
def test_iec61131::il::il::formal::funct::call_instantiation(instance):
    assert isinstance(instance, iec61131::il::Il::Formal::Funct::Call)

@given(instance=iec61131::il::Il::Simple::Operation_strategy)
@settings(max_examples=50)
def test_iec61131::il::il::simple::operation_instantiation(instance):
    assert isinstance(instance, iec61131::il::Il::Simple::Operation)

@given(instance=iec61131::il::Label_strategy)
@settings(max_examples=50)
def test_iec61131::il::label_instantiation(instance):
    assert isinstance(instance, iec61131::il::Label)

@given(instance=iec61131::il::Label_strategy)
def test_iec61131::il::label_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=iec61131::il::Label_strategy)
def test_iec61131::il::label_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=Il::Operations_strategy)
@settings(max_examples=50)
def test_il::operations_instantiation(instance):
    assert isinstance(instance, Il::Operations)

@given(instance=iec61131::il::Il::Return::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::il::il::return::operator_instantiation(instance):
    assert isinstance(instance, iec61131::il::Il::Return::Operator)

@given(instance=iec61131::il::Il::Jump::Operation_strategy)
@settings(max_examples=50)
def test_iec61131::il::il::jump::operation_instantiation(instance):
    assert isinstance(instance, iec61131::il::Il::Jump::Operation)

@given(instance=iec61131::il::Il::Fb::Call_strategy)
@settings(max_examples=50)
def test_iec61131::il::il::fb::call_instantiation(instance):
    assert isinstance(instance, iec61131::il::Il::Fb::Call)

@given(instance=Label_strategy)
@settings(max_examples=50)
def test_label_instantiation(instance):
    assert isinstance(instance, Label)

@given(instance=iec61131::il::Il::Instruction_strategy)
@settings(max_examples=50)
def test_iec61131::il::il::instruction_instantiation(instance):
    assert isinstance(instance, iec61131::il::Il::Instruction)

@given(instance=Il::Simple::Instruction_strategy)
@settings(max_examples=50)
def test_il::simple::instruction_instantiation(instance):
    assert isinstance(instance, Il::Simple::Instruction)

@given(instance=iec61131::il::Simple::Instr::List_strategy)
@settings(max_examples=50)
def test_iec61131::il::simple::instr::list_instantiation(instance):
    assert isinstance(instance, iec61131::il::Simple::Instr::List)

@given(instance=Unary::Operator_strategy)
@settings(max_examples=50)
def test_unary::operator_instantiation(instance):
    assert isinstance(instance, Unary::Operator)

@given(instance=Power::Symbol_strategy)
@settings(max_examples=50)
def test_power::symbol_instantiation(instance):
    assert isinstance(instance, Power::Symbol)

@given(instance=Structured::Variable_strategy)
@settings(max_examples=50)
def test_structured::variable_instantiation(instance):
    assert isinstance(instance, Structured::Variable)

@given(instance=Array::Variable_strategy)
@settings(max_examples=50)
def test_array::variable_instantiation(instance):
    assert isinstance(instance, Array::Variable)

@given(instance=Function::Name_strategy)
@settings(max_examples=50)
def test_function::name_instantiation(instance):
    assert isinstance(instance, Function::Name)

@given(instance=Primary::Expression_strategy)
@settings(max_examples=50)
def test_primary::expression_instantiation(instance):
    assert isinstance(instance, Primary::Expression)

@given(instance=iec61131::st::Expression::Variable::Type_strategy)
@settings(max_examples=50)
def test_iec61131::st::expression::variable::type_instantiation(instance):
    assert isinstance(instance, iec61131::st::Expression::Variable::Type)

@given(instance=iec61131::st::Expression::EnumValue_strategy)
@settings(max_examples=50)
def test_iec61131::st::expression::enumvalue_instantiation(instance):
    assert isinstance(instance, iec61131::st::Expression::EnumValue)

@given(instance=iec61131::st::Call::Expression_strategy)
@settings(max_examples=50)
def test_iec61131::st::call::expression_instantiation(instance):
    assert isinstance(instance, iec61131::st::Call::Expression)

@given(instance=iec61131::st::Expression::Constant_strategy)
@settings(max_examples=50)
def test_iec61131::st::expression::constant_instantiation(instance):
    assert isinstance(instance, iec61131::st::Expression::Constant)

@given(instance=iec61131::st::Bracket::Expression_strategy)
@settings(max_examples=50)
def test_iec61131::st::bracket::expression_instantiation(instance):
    assert isinstance(instance, iec61131::st::Bracket::Expression)

@given(instance=Add::Operator_strategy)
@settings(max_examples=50)
def test_add::operator_instantiation(instance):
    assert isinstance(instance, Add::Operator)

@given(instance=Xor::Operator_strategy)
@settings(max_examples=50)
def test_xor::operator_instantiation(instance):
    assert isinstance(instance, Xor::Operator)

@given(instance=iec61131::st::For::List_strategy)
@settings(max_examples=50)
def test_iec61131::st::for::list_instantiation(instance):
    assert isinstance(instance, iec61131::st::For::List)

@given(instance=iec61131::st::Control::Variable_strategy)
@settings(max_examples=50)
def test_iec61131::st::control::variable_instantiation(instance):
    assert isinstance(instance, iec61131::st::Control::Variable)

@given(instance=iec61131::st::Control::Variable_strategy)
def test_iec61131::st::control::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iec61131::st::Control::Variable_strategy)
def test_iec61131::st::control::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Statement::List_strategy)
@settings(max_examples=50)
def test_statement::list_instantiation(instance):
    assert isinstance(instance, Statement::List)

@given(instance=Selection::Statement_strategy)
@settings(max_examples=50)
def test_selection::statement_instantiation(instance):
    assert isinstance(instance, Selection::Statement)

@given(instance=iec61131::st::If::Statement_strategy)
@settings(max_examples=50)
def test_iec61131::st::if::statement_instantiation(instance):
    assert isinstance(instance, iec61131::st::If::Statement)

@given(instance=Not::Operator_strategy)
@settings(max_examples=50)
def test_not::operator_instantiation(instance):
    assert isinstance(instance, Not::Operator)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=For::List_strategy)
@settings(max_examples=50)
def test_for::list_instantiation(instance):
    assert isinstance(instance, For::List)

@given(instance=Control::Variable_strategy)
@settings(max_examples=50)
def test_control::variable_instantiation(instance):
    assert isinstance(instance, Control::Variable)

@given(instance=Iteration::Statement_strategy)
@settings(max_examples=50)
def test_iteration::statement_instantiation(instance):
    assert isinstance(instance, Iteration::Statement)

@given(instance=iec61131::st::Exit::Statement_strategy)
@settings(max_examples=50)
def test_iec61131::st::exit::statement_instantiation(instance):
    assert isinstance(instance, iec61131::st::Exit::Statement)

@given(instance=iec61131::st::While::Statement_strategy)
@settings(max_examples=50)
def test_iec61131::st::while::statement_instantiation(instance):
    assert isinstance(instance, iec61131::st::While::Statement)

@given(instance=iec61131::st::Repeat::Statement_strategy)
@settings(max_examples=50)
def test_iec61131::st::repeat::statement_instantiation(instance):
    assert isinstance(instance, iec61131::st::Repeat::Statement)

@given(instance=iec61131::st::For::Statement_strategy)
@settings(max_examples=50)
def test_iec61131::st::for::statement_instantiation(instance):
    assert isinstance(instance, iec61131::st::For::Statement)

@given(instance=iec61131::st::Case::List::Element_strategy)
@settings(max_examples=50)
def test_iec61131::st::case::list::element_instantiation(instance):
    assert isinstance(instance, iec61131::st::Case::List::Element)

@given(instance=iec61131::st::Case::List_strategy)
@settings(max_examples=50)
def test_iec61131::st::case::list_instantiation(instance):
    assert isinstance(instance, iec61131::st::Case::List)

@given(instance=Case::List_strategy)
@settings(max_examples=50)
def test_case::list_instantiation(instance):
    assert isinstance(instance, Case::List)

@given(instance=iec61131::st::Case::Element_strategy)
@settings(max_examples=50)
def test_iec61131::st::case::element_instantiation(instance):
    assert isinstance(instance, iec61131::st::Case::Element)

@given(instance=iec61131::st::Else::Statement_strategy)
@settings(max_examples=50)
def test_iec61131::st::else::statement_instantiation(instance):
    assert isinstance(instance, iec61131::st::Else::Statement)

@given(instance=Single::Element::Type::Name_strategy)
@settings(max_examples=50)
def test_single::element::type::name_instantiation(instance):
    assert isinstance(instance, Single::Element::Type::Name)

@given(instance=iec61131::types::Enumerated::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::enumerated::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::Enumerated::Type::Name)

@given(instance=iec61131::types::Subrange::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::subrange::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::Subrange::Type::Name)

@given(instance=types::Single::Element::Type::Name_strategy)
@settings(max_examples=50)
def test_types::single::element::type::name_instantiation(instance):
    assert isinstance(instance, types::Single::Element::Type::Name)

@given(instance=types::Derived::Type::Name_strategy)
@settings(max_examples=50)
def test_types::derived::type::name_instantiation(instance):
    assert isinstance(instance, types::Derived::Type::Name)

@given(instance=Derived::Type::Name_strategy)
@settings(max_examples=50)
def test_derived::type::name_instantiation(instance):
    assert isinstance(instance, Derived::Type::Name)

@given(instance=iec61131::types::Array::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::array::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::Array::Type::Name)

@given(instance=iec61131::types::String::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::string::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::String::Type::Name)

@given(instance=iec61131::types::Single::Element::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::single::element::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::Single::Element::Type::Name)

@given(instance=iec61131::variables::Subscript::List_strategy)
@settings(max_examples=50)
def test_iec61131::variables::subscript::list_instantiation(instance):
    assert isinstance(instance, iec61131::variables::Subscript::List)

@given(instance=Input::Reference_strategy)
@settings(max_examples=50)
def test_input::reference_instantiation(instance):
    assert isinstance(instance, Input::Reference)

@given(instance=Output::Reference_strategy)
@settings(max_examples=50)
def test_output::reference_instantiation(instance):
    assert isinstance(instance, Output::Reference)

@given(instance=variables::Symbolic::Variable_strategy)
@settings(max_examples=50)
def test_variables::symbolic::variable_instantiation(instance):
    assert isinstance(instance, variables::Symbolic::Variable)

@given(instance=pous::Function::Return::Value_strategy)
@settings(max_examples=50)
def test_pous::function::return::value_instantiation(instance):
    assert isinstance(instance, pous::Function::Return::Value)

@given(instance=types::Data::Type::Name_strategy)
@settings(max_examples=50)
def test_types::data::type::name_instantiation(instance):
    assert isinstance(instance, types::Data::Type::Name)

@given(instance=iec61131::types::Non::Generic::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::non::generic::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::Non::Generic::Type::Name)

@given(instance=interfaces::Simple::Specification::Func_strategy)
@settings(max_examples=50)
def test_interfaces::simple::specification::func_instantiation(instance):
    assert isinstance(instance, interfaces::Simple::Specification::Func)

@given(instance=types::Non::Generic::Type::Name_strategy)
@settings(max_examples=50)
def test_types::non::generic::type::name_instantiation(instance):
    assert isinstance(instance, types::Non::Generic::Type::Name)

@given(instance=Numeric::Type::Name_strategy)
@settings(max_examples=50)
def test_numeric::type::name_instantiation(instance):
    assert isinstance(instance, Numeric::Type::Name)

@given(instance=iec61131::types::Real::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::real::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::Real::Type::Name)

@given(instance=iec61131::types::Integer::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::integer::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::Integer::Type::Name)

@given(instance=Elementary::Type::Name_strategy)
@settings(max_examples=50)
def test_elementary::type::name_instantiation(instance):
    assert isinstance(instance, Elementary::Type::Name)

@given(instance=iec61131::types::Bit::String::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::bit::string::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::Bit::String::Type::Name)

@given(instance=iec61131::types::Date::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::date::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::Date::Type::Name)

@given(instance=iec61131::types::Duration::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::duration::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::Duration::Type::Name)

@given(instance=iec61131::types::Byte::String::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::byte::string::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::Byte::String::Type::Name)

@given(instance=iec61131::types::Numeric::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::numeric::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::Numeric::Type::Name)

@given(instance=Data::Type::Name_strategy)
@settings(max_examples=50)
def test_data::type::name_instantiation(instance):
    assert isinstance(instance, Data::Type::Name)

@given(instance=iec61131::types::Simple::Specification_strategy)
@settings(max_examples=50)
def test_iec61131::types::simple::specification_instantiation(instance):
    assert isinstance(instance, iec61131::types::Simple::Specification)

@given(instance=iec61131::types::TypeLib_strategy)
@settings(max_examples=50)
def test_iec61131::types::typelib_instantiation(instance):
    assert isinstance(instance, iec61131::types::TypeLib)

@given(instance=Fbd::Network_strategy)
@settings(max_examples=50)
def test_fbd::network_instantiation(instance):
    assert isinstance(instance, Fbd::Network)

@given(instance=iec61131::sfc::Transition::Cond2_strategy)
@settings(max_examples=50)
def test_iec61131::sfc::transition::cond2_instantiation(instance):
    assert isinstance(instance, iec61131::sfc::Transition::Cond2)

@given(instance=iec61131::sfc::Transition::Condition_strategy)
@settings(max_examples=50)
def test_iec61131::sfc::transition::condition_instantiation(instance):
    assert isinstance(instance, iec61131::sfc::Transition::Condition)

@given(instance=iec61131::sfc::Steps_strategy)
@settings(max_examples=50)
def test_iec61131::sfc::steps_instantiation(instance):
    assert isinstance(instance, iec61131::sfc::Steps)

@given(instance=iec61131::sfc::Transition::Name_strategy)
@settings(max_examples=50)
def test_iec61131::sfc::transition::name_instantiation(instance):
    assert isinstance(instance, iec61131::sfc::Transition::Name)

@given(instance=iec61131::sfc::Transition::Name_strategy)
def test_iec61131::sfc::transition::name_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iec61131::sfc::Transition::Name_strategy)
def test_iec61131::sfc::transition::name_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iec61131::sfc::Action::Time_strategy)
@settings(max_examples=50)
def test_iec61131::sfc::action::time_instantiation(instance):
    assert isinstance(instance, iec61131::sfc::Action::Time)

@given(instance=variables::Variable_strategy)
@settings(max_examples=50)
def test_variables::variable_instantiation(instance):
    assert isinstance(instance, variables::Variable)

@given(instance=Subscript::List_strategy)
@settings(max_examples=50)
def test_subscript::list_instantiation(instance):
    assert isinstance(instance, Subscript::List)

@given(instance=Multi::Element::Variable_strategy)
@settings(max_examples=50)
def test_multi::element::variable_instantiation(instance):
    assert isinstance(instance, Multi::Element::Variable)

@given(instance=iec61131::variables::Structured::Variable_strategy)
@settings(max_examples=50)
def test_iec61131::variables::structured::variable_instantiation(instance):
    assert isinstance(instance, iec61131::variables::Structured::Variable)

@given(instance=iec61131::variables::Array::Variable_strategy)
@settings(max_examples=50)
def test_iec61131::variables::array::variable_instantiation(instance):
    assert isinstance(instance, iec61131::variables::Array::Variable)

@given(instance=iec61131::variables::Symbolic::Variable_strategy)
@settings(max_examples=50)
def test_iec61131::variables::symbolic::variable_instantiation(instance):
    assert isinstance(instance, iec61131::variables::Symbolic::Variable)

@given(instance=iec61131::sfc::Cond2::Condition_strategy)
@settings(max_examples=50)
def test_iec61131::sfc::cond2::condition_instantiation(instance):
    assert isinstance(instance, iec61131::sfc::Cond2::Condition)

@given(instance=iec61131::sfc::Transition::Cond3_strategy)
@settings(max_examples=50)
def test_iec61131::sfc::transition::cond3_instantiation(instance):
    assert isinstance(instance, iec61131::sfc::Transition::Cond3)

@given(instance=iec61131::sfc::Transition::Cond1_strategy)
@settings(max_examples=50)
def test_iec61131::sfc::transition::cond1_instantiation(instance):
    assert isinstance(instance, iec61131::sfc::Transition::Cond1)

@given(instance=Cond2::Condition_strategy)
@settings(max_examples=50)
def test_cond2::condition_instantiation(instance):
    assert isinstance(instance, Cond2::Condition)

@given(instance=iec61131::fbd::Fbd::Network_strategy)
@settings(max_examples=50)
def test_iec61131::fbd::fbd::network_instantiation(instance):
    assert isinstance(instance, iec61131::fbd::Fbd::Network)

@given(instance=iec61131::ld::Rung_strategy)
@settings(max_examples=50)
def test_iec61131::ld::rung_instantiation(instance):
    assert isinstance(instance, iec61131::ld::Rung)

@given(instance=Steps_strategy)
@settings(max_examples=50)
def test_steps_instantiation(instance):
    assert isinstance(instance, Steps)

@given(instance=iec61131::sfc::Steps1_strategy)
@settings(max_examples=50)
def test_iec61131::sfc::steps1_instantiation(instance):
    assert isinstance(instance, iec61131::sfc::Steps1)

@given(instance=iec61131::sfc::Steps2_strategy)
@settings(max_examples=50)
def test_iec61131::sfc::steps2_instantiation(instance):
    assert isinstance(instance, iec61131::sfc::Steps2)

@given(instance=Transition::Name_strategy)
@settings(max_examples=50)
def test_transition::name_instantiation(instance):
    assert isinstance(instance, Transition::Name)

@given(instance=sfc::Step::Types_strategy)
@settings(max_examples=50)
def test_sfc::step::types_instantiation(instance):
    assert isinstance(instance, sfc::Step::Types)

@given(instance=sfc::Sfc::Elements_strategy)
@settings(max_examples=50)
def test_sfc::sfc::elements_instantiation(instance):
    assert isinstance(instance, sfc::Sfc::Elements)

@given(instance=iec61131::sfc::Step_strategy)
@settings(max_examples=50)
def test_iec61131::sfc::step_instantiation(instance):
    assert isinstance(instance, iec61131::sfc::Step)

@given(instance=Step::Types_strategy)
@settings(max_examples=50)
def test_step::types_instantiation(instance):
    assert isinstance(instance, Step::Types)

@given(instance=iec61131::sfc::Initial::Step_strategy)
@settings(max_examples=50)
def test_iec61131::sfc::initial::step_instantiation(instance):
    assert isinstance(instance, iec61131::sfc::Initial::Step)

@given(instance=Sfc::Elements_strategy)
@settings(max_examples=50)
def test_sfc::elements_instantiation(instance):
    assert isinstance(instance, Sfc::Elements)

@given(instance=iec61131::sfc::Transition_strategy)
@settings(max_examples=50)
def test_iec61131::sfc::transition_instantiation(instance):
    assert isinstance(instance, iec61131::sfc::Transition)

@given(instance=iec61131::sfc::Action_strategy)
@settings(max_examples=50)
def test_iec61131::sfc::action_instantiation(instance):
    assert isinstance(instance, iec61131::sfc::Action)

@given(instance=Initial::Step_strategy)
@settings(max_examples=50)
def test_initial::step_instantiation(instance):
    assert isinstance(instance, Initial::Step)

@given(instance=iec61131::sfc::Timed::Qualifier_strategy)
@settings(max_examples=50)
def test_iec61131::sfc::timed::qualifier_instantiation(instance):
    assert isinstance(instance, iec61131::sfc::Timed::Qualifier)

@given(instance=iec61131::sfc::Timed::Qualifier_strategy)
def test_iec61131::sfc::timed::qualifier_qualifier_type(instance):
    assert isinstance(instance.qualifier, str)


@given(instance=iec61131::sfc::Timed::Qualifier_strategy)
def test_iec61131::sfc::timed::qualifier_qualifier_setter(instance):
    original = instance.qualifier
    instance.qualifier = original
    assert instance.qualifier == original

@given(instance=Action::Time_strategy)
@settings(max_examples=50)
def test_action::time_instantiation(instance):
    assert isinstance(instance, Action::Time)

@given(instance=iec61131::sfc::ActionTime2_strategy)
@settings(max_examples=50)
def test_iec61131::sfc::actiontime2_instantiation(instance):
    assert isinstance(instance, iec61131::sfc::ActionTime2)

@given(instance=Timed::Qualifier_strategy)
@settings(max_examples=50)
def test_timed::qualifier_instantiation(instance):
    assert isinstance(instance, Timed::Qualifier)

@given(instance=Variable::Name_strategy)
@settings(max_examples=50)
def test_variable::name_instantiation(instance):
    assert isinstance(instance, Variable::Name)

@given(instance=Location_strategy)
@settings(max_examples=50)
def test_location_instantiation(instance):
    assert isinstance(instance, Location)

@given(instance=iec61131::interfaces::Located::Var::Decl_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::located::var::decl_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Located::Var::Decl)

@given(instance=Direct::Variable_strategy)
@settings(max_examples=50)
def test_direct::variable_instantiation(instance):
    assert isinstance(instance, Direct::Variable)

@given(instance=iec61131::interfaces::Location_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::location_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Location)

@given(instance=iec61131::interfaces::Located::Var::Spec::Init_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::located::var::spec::init_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Located::Var::Spec::Init)

@given(instance=iec61131::interfaces::External::Specification_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::external::specification_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::External::Specification)

@given(instance=iec61131::interfaces::Var::Spec_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::var::spec_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Var::Spec)

@given(instance=iec61131::interfaces::Incompl::Location_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::incompl::location_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Incompl::Location)

@given(instance=iec61131::interfaces::Incompl::Location_strategy)
def test_iec61131::interfaces::incompl::location_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=iec61131::interfaces::Incompl::Location_strategy)
def test_iec61131::interfaces::incompl::location_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=Var::Spec_strategy)
@settings(max_examples=50)
def test_var::spec_instantiation(instance):
    assert isinstance(instance, Var::Spec)

@given(instance=Incompl::Location_strategy)
@settings(max_examples=50)
def test_incompl::location_instantiation(instance):
    assert isinstance(instance, Incompl::Location)

@given(instance=iec61131::interfaces::Incompl::Located::Var::Decl_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::incompl::located::var::decl_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Incompl::Located::Var::Decl)

@given(instance=Incompl::Located::Var::Decl_strategy)
@settings(max_examples=50)
def test_incompl::located::var::decl_instantiation(instance):
    assert isinstance(instance, Incompl::Located::Var::Decl)

@given(instance=Temp::Var::Decl_strategy)
@settings(max_examples=50)
def test_temp::var::decl_instantiation(instance):
    assert isinstance(instance, Temp::Var::Decl)

@given(instance=Global::Var::Spec_strategy)
@settings(max_examples=50)
def test_global::var::spec_instantiation(instance):
    assert isinstance(instance, Global::Var::Spec)

@given(instance=iec61131::interfaces::Global::Var::List_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::global::var::list_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Global::Var::List)

@given(instance=Library::Element::Name_strategy)
@settings(max_examples=50)
def test_library::element::name_instantiation(instance):
    assert isinstance(instance, Library::Element::Name)

@given(instance=iec61131::types::Data::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::data::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::Data::Type::Name)

@given(instance=iec61131::interfaces::Specification_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::specification_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Specification)

@given(instance=Specification_strategy)
@settings(max_examples=50)
def test_specification_instantiation(instance):
    assert isinstance(instance, Specification)

@given(instance=Array::Initial::Elements_strategy)
@settings(max_examples=50)
def test_array::initial::elements_instantiation(instance):
    assert isinstance(instance, Array::Initial::Elements)

@given(instance=iec61131::interfaces::Array::Initialization_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::array::initialization_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Array::Initialization)

@given(instance=iec61131::interfaces::Var1::List_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::var1::list_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Var1::List)

@given(instance=Double::BString_strategy)
@settings(max_examples=50)
def test_double::bstring_instantiation(instance):
    assert isinstance(instance, Double::BString)

@given(instance=Double::Byte::Character::String_strategy)
@settings(max_examples=50)
def test_double::byte::character::string_instantiation(instance):
    assert isinstance(instance, Double::Byte::Character::String)

@given(instance=Single::BString_strategy)
@settings(max_examples=50)
def test_single::bstring_instantiation(instance):
    assert isinstance(instance, Single::BString)

@given(instance=Single::Byte::Character::String_strategy)
@settings(max_examples=50)
def test_single::byte::character::string_instantiation(instance):
    assert isinstance(instance, Single::Byte::Character::String)

@given(instance=Located::Var::Spec::Init_strategy)
@settings(max_examples=50)
def test_located::var::spec::init_instantiation(instance):
    assert isinstance(instance, Located::Var::Spec::Init)

@given(instance=iec61131::interfaces::Double::Byte::String::Spec_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::double::byte::string::spec_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Double::Byte::String::Spec)

@given(instance=iec61131::interfaces::Single::Byte::String::Spec_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::single::byte::string::spec_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Single::Byte::String::Spec)

@given(instance=Double::Byte::String::Spec_strategy)
@settings(max_examples=50)
def test_double::byte::string::spec_instantiation(instance):
    assert isinstance(instance, Double::Byte::String::Spec)

@given(instance=Single::Byte::String::Spec_strategy)
@settings(max_examples=50)
def test_single::byte::string::spec_instantiation(instance):
    assert isinstance(instance, Single::Byte::String::Spec)

@given(instance=String::Var::Declaration_strategy)
@settings(max_examples=50)
def test_string::var::declaration_instantiation(instance):
    assert isinstance(instance, String::Var::Declaration)

@given(instance=iec61131::interfaces::Double::Byte::String::Var::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::double::byte::string::var::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Double::Byte::String::Var::Declaration)

@given(instance=iec61131::interfaces::Single::Byte::String::Var::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::single::byte::string::var::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Single::Byte::String::Var::Declaration)

@given(instance=Range_strategy)
@settings(max_examples=50)
def test_range_instantiation(instance):
    assert isinstance(instance, Range)

@given(instance=Case::List::Element_strategy)
@settings(max_examples=50)
def test_case::list::element_instantiation(instance):
    assert isinstance(instance, Case::List::Element)

@given(instance=iec61131::interfaces::Subrange_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::subrange_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Subrange)

@given(instance=iec61131::interfaces::Subrange_strategy)
def test_iec61131::interfaces::subrange_delimiter_type(instance):
    assert isinstance(instance.delimiter, str)


@given(instance=iec61131::interfaces::Subrange_strategy)
def test_iec61131::interfaces::subrange_delimiter_setter(instance):
    original = instance.delimiter
    instance.delimiter = original
    assert instance.delimiter == original

@given(instance=iec61131::interfaces::Array::Initial::Elements_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::array::initial::elements_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Array::Initial::Elements)

@given(instance=interfaces::Var::Spec_strategy)
@settings(max_examples=50)
def test_interfaces::var::spec_instantiation(instance):
    assert isinstance(instance, interfaces::Var::Spec)

@given(instance=interfaces::External::Specification_strategy)
@settings(max_examples=50)
def test_interfaces::external::specification_instantiation(instance):
    assert isinstance(instance, interfaces::External::Specification)

@given(instance=iec61131::interfaces::Array::Specification_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::array::specification_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Array::Specification)

@given(instance=iec61131::types::Structure::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::structure::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::Structure::Type::Name)

@given(instance=interfaces::Specification_strategy)
@settings(max_examples=50)
def test_interfaces::specification_instantiation(instance):
    assert isinstance(instance, interfaces::Specification)

@given(instance=iec61131::interfaces::Enumerated::Specification_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::enumerated::specification_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Enumerated::Specification)

@given(instance=iec61131::interfaces::Subrange::Specification_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::subrange::specification_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Subrange::Specification)

@given(instance=interfaces::Var2::Init::Decl_strategy)
@settings(max_examples=50)
def test_interfaces::var2::init::decl_instantiation(instance):
    assert isinstance(instance, interfaces::Var2::Init::Decl)

@given(instance=interfaces::Temp::Var::Decl_strategy)
@settings(max_examples=50)
def test_interfaces::temp::var::decl_instantiation(instance):
    assert isinstance(instance, interfaces::Temp::Var::Decl)

@given(instance=iec61131::interfaces::String::Var::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::string::var::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::String::Var::Declaration)

@given(instance=Function::Block::Type::Name_strategy)
@settings(max_examples=50)
def test_function::block::type::name_instantiation(instance):
    assert isinstance(instance, Function::Block::Type::Name)

@given(instance=Structure::Initialization_strategy)
@settings(max_examples=50)
def test_structure::initialization_instantiation(instance):
    assert isinstance(instance, Structure::Initialization)

@given(instance=Temp::Var::Declaration_strategy)
@settings(max_examples=50)
def test_temp::var::declaration_instantiation(instance):
    assert isinstance(instance, Temp::Var::Declaration)

@given(instance=iec61131::interfaces::Array::Var::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::array::var::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Array::Var::Declaration)

@given(instance=iec61131::interfaces::Structured::Var::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::structured::var::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Structured::Var::Declaration)

@given(instance=iec61131::interfaces::Var1::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::var1::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Var1::Declaration)

@given(instance=iec61131::interfaces::Fb::Name::Decl_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::fb::name::decl_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Fb::Name::Decl)

@given(instance=Enumerated::Type::Name_strategy)
@settings(max_examples=50)
def test_enumerated::type::name_instantiation(instance):
    assert isinstance(instance, Enumerated::Type::Name)

@given(instance=iec61131::interfaces::Structure::Element::Name_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::structure::element::name_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Structure::Element::Name)

@given(instance=iec61131::interfaces::Structure::Element::Name_strategy)
def test_iec61131::interfaces::structure::element::name_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iec61131::interfaces::Structure::Element::Name_strategy)
def test_iec61131::interfaces::structure::element::name_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Initial::Element_strategy)
@settings(max_examples=50)
def test_initial::element_instantiation(instance):
    assert isinstance(instance, Initial::Element)

@given(instance=Structure::Element::Name_strategy)
@settings(max_examples=50)
def test_structure::element::name_instantiation(instance):
    assert isinstance(instance, Structure::Element::Name)

@given(instance=iec61131::interfaces::Structure::Element::Initialization_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::structure::element::initialization_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Structure::Element::Initialization)

@given(instance=Structure::Element::Initialization_strategy)
@settings(max_examples=50)
def test_structure::element::initialization_instantiation(instance):
    assert isinstance(instance, Structure::Element::Initialization)

@given(instance=iec61131::interfaces::Structure::Initialization_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::structure::initialization_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Structure::Initialization)

@given(instance=iec61131::interfaces::Var::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::var::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Var::Declaration)

@given(instance=Structure::Type::Name_strategy)
@settings(max_examples=50)
def test_structure::type::name_instantiation(instance):
    assert isinstance(instance, Structure::Type::Name)

@given(instance=pous::Structure::Specification_strategy)
@settings(max_examples=50)
def test_pous::structure::specification_instantiation(instance):
    assert isinstance(instance, pous::Structure::Specification)

@given(instance=Array::Specification_strategy)
@settings(max_examples=50)
def test_array::specification_instantiation(instance):
    assert isinstance(instance, Array::Specification)

@given(instance=Array::Initialization_strategy)
@settings(max_examples=50)
def test_array::initialization_instantiation(instance):
    assert isinstance(instance, Array::Initialization)

@given(instance=Var::Declaration_strategy)
@settings(max_examples=50)
def test_var::declaration_instantiation(instance):
    assert isinstance(instance, Var::Declaration)

@given(instance=iec61131::interfaces::Temp::Var::Decl_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::temp::var::decl_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Temp::Var::Decl)

@given(instance=Var1::Specification_strategy)
@settings(max_examples=50)
def test_var1::specification_instantiation(instance):
    assert isinstance(instance, Var1::Specification)

@given(instance=Var::Init::Decl_strategy)
@settings(max_examples=50)
def test_var::init::decl_instantiation(instance):
    assert isinstance(instance, Var::Init::Decl)

@given(instance=iec61131::interfaces::Var1::Init::Decl_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::var1::init::decl_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Var1::Init::Decl)

@given(instance=Var1::List_strategy)
@settings(max_examples=50)
def test_var1::list_instantiation(instance):
    assert isinstance(instance, Var1::List)

@given(instance=Input::Declaration_strategy)
@settings(max_examples=50)
def test_input::declaration_instantiation(instance):
    assert isinstance(instance, Input::Declaration)

@given(instance=iec61131::interfaces::Var::Init::Decl_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::var::init::decl_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Var::Init::Decl)

@given(instance=Io::Var::Declaration_strategy)
@settings(max_examples=50)
def test_io::var::declaration_instantiation(instance):
    assert isinstance(instance, Io::Var::Declaration)

@given(instance=iec61131::interfaces::Output::Declarations_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::output::declarations_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Output::Declarations)

@given(instance=iec61131::interfaces::Output::Declarations_strategy)
def test_iec61131::interfaces::output::declarations_retain_type(instance):
    assert isinstance(instance.retain, bool)


@given(instance=iec61131::interfaces::Output::Declarations_strategy)
def test_iec61131::interfaces::output::declarations_retain_setter(instance):
    original = instance.retain
    instance.retain = original
    assert instance.retain == original

@given(instance=iec61131::interfaces::Input::Output::Declarations_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::input::output::declarations_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Input::Output::Declarations)

@given(instance=iec61131::interfaces::Input::Declarations_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::input::declarations_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Input::Declarations)

@given(instance=iec61131::interfaces::Input::Declarations_strategy)
def test_iec61131::interfaces::input::declarations_retain_type(instance):
    assert isinstance(instance.retain, bool)


@given(instance=iec61131::interfaces::Input::Declarations_strategy)
def test_iec61131::interfaces::input::declarations_retain_setter(instance):
    original = instance.retain
    instance.retain = original
    assert instance.retain == original

@given(instance=pous::Function::Vars_strategy)
@settings(max_examples=50)
def test_pous::function::vars_instantiation(instance):
    assert isinstance(instance, pous::Function::Vars)

@given(instance=pous::Program::Vars_strategy)
@settings(max_examples=50)
def test_pous::program::vars_instantiation(instance):
    assert isinstance(instance, pous::Program::Vars)

@given(instance=pous::Function::Block::Vars_strategy)
@settings(max_examples=50)
def test_pous::function::block::vars_instantiation(instance):
    assert isinstance(instance, pous::Function::Block::Vars)

@given(instance=interfaces::Interface_strategy)
@settings(max_examples=50)
def test_interfaces::interface_instantiation(instance):
    assert isinstance(instance, interfaces::Interface)

@given(instance=iec61131::interfaces::Other::Var::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::other::var::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Other::Var::Declaration)

@given(instance=iec61131::interfaces::Io::Var::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::io::var::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Io::Var::Declaration)

@given(instance=Initialized::Structure_strategy)
@settings(max_examples=50)
def test_initialized::structure_instantiation(instance):
    assert isinstance(instance, Initialized::Structure)

@given(instance=Array::Spec::Init_strategy)
@settings(max_examples=50)
def test_array::spec::init_instantiation(instance):
    assert isinstance(instance, Array::Spec::Init)

@given(instance=Var2::Init::Decl_strategy)
@settings(max_examples=50)
def test_var2::init::decl_instantiation(instance):
    assert isinstance(instance, Var2::Init::Decl)

@given(instance=iec61131::interfaces::Structured::Var::Init::Decl_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::structured::var::init::decl_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Structured::Var::Init::Decl)

@given(instance=iec61131::interfaces::Array::Var::Init::Decl_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::array::var::init::decl_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Array::Var::Init::Decl)

@given(instance=Enumerated::Value_strategy)
@settings(max_examples=50)
def test_enumerated::value_instantiation(instance):
    assert isinstance(instance, Enumerated::Value)

@given(instance=Enumerated::Specification_strategy)
@settings(max_examples=50)
def test_enumerated::specification_instantiation(instance):
    assert isinstance(instance, Enumerated::Specification)

@given(instance=Signed::Integer_strategy)
@settings(max_examples=50)
def test_signed::integer_instantiation(instance):
    assert isinstance(instance, Signed::Integer)

@given(instance=Subrange::Specification_strategy)
@settings(max_examples=50)
def test_subrange::specification_instantiation(instance):
    assert isinstance(instance, Subrange::Specification)

@given(instance=interfaces::Var1::Specification::Func_strategy)
@settings(max_examples=50)
def test_interfaces::var1::specification::func_instantiation(instance):
    assert isinstance(instance, interfaces::Var1::Specification::Func)

@given(instance=Simple::Specification_strategy)
@settings(max_examples=50)
def test_simple::specification_instantiation(instance):
    assert isinstance(instance, Simple::Specification)

@given(instance=pous::Structure::Elements_strategy)
@settings(max_examples=50)
def test_pous::structure::elements_instantiation(instance):
    assert isinstance(instance, pous::Structure::Elements)

@given(instance=interfaces::Located::Var::Spec::Init_strategy)
@settings(max_examples=50)
def test_interfaces::located::var::spec::init_instantiation(instance):
    assert isinstance(instance, interfaces::Located::Var::Spec::Init)

@given(instance=iec61131::interfaces::Initialized::Structure_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::initialized::structure_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Initialized::Structure)

@given(instance=iec61131::interfaces::Array::Spec::Init_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::array::spec::init_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Array::Spec::Init)

@given(instance=interfaces::Var1::Specification_strategy)
@settings(max_examples=50)
def test_interfaces::var1::specification_instantiation(instance):
    assert isinstance(instance, interfaces::Var1::Specification)

@given(instance=iec61131::interfaces::Enumerated::Spec::Init_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::enumerated::spec::init_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Enumerated::Spec::Init)

@given(instance=iec61131::interfaces::Subrange::Spec::Init_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::subrange::spec::init_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Subrange::Spec::Init)

@given(instance=iec61131::interfaces::Simple::Spec::Init_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::simple::spec::init_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Simple::Spec::Init)

@given(instance=Assignment::Symbol_strategy)
@settings(max_examples=50)
def test_assignment::symbol_instantiation(instance):
    assert isinstance(instance, Assignment::Symbol)

@given(instance=iec61131::interfaces::Var1::Specification_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::var1::specification_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Var1::Specification)

@given(instance=Bool::Type::Name_strategy)
@settings(max_examples=50)
def test_bool::type::name_instantiation(instance):
    assert isinstance(instance, Bool::Type::Name)

@given(instance=iec61131::interfaces::Edge::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::edge::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Edge::Declaration)

@given(instance=iec61131::interfaces::Edge::Declaration_strategy)
def test_iec61131::interfaces::edge::declaration_edge_type(instance):
    assert isinstance(instance.edge, str)


@given(instance=iec61131::interfaces::Edge::Declaration_strategy)
def test_iec61131::interfaces::edge::declaration_edge_setter(instance):
    original = instance.edge
    instance.edge = original
    assert instance.edge == original

@given(instance=operators::Divide::Operator_strategy)
@settings(max_examples=50)
def test_operators::divide::operator_instantiation(instance):
    assert isinstance(instance, operators::Divide::Operator)

@given(instance=Multiply::Operator_strategy)
@settings(max_examples=50)
def test_multiply::operator_instantiation(instance):
    assert isinstance(instance, Multiply::Operator)

@given(instance=iec61131::operators::Multiply::Symbol_strategy)
@settings(max_examples=50)
def test_iec61131::operators::multiply::symbol_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Multiply::Symbol)

@given(instance=iec61131::st::Else::If::Statement_strategy)
@settings(max_examples=50)
def test_iec61131::st::else::if::statement_instantiation(instance):
    assert isinstance(instance, iec61131::st::Else::If::Statement)

@given(instance=Case::Element_strategy)
@settings(max_examples=50)
def test_case::element_instantiation(instance):
    assert isinstance(instance, Case::Element)

@given(instance=iec61131::st::Case::Statement_strategy)
@settings(max_examples=50)
def test_iec61131::st::case::statement_instantiation(instance):
    assert isinstance(instance, iec61131::st::Case::Statement)

@given(instance=Else::Statement_strategy)
@settings(max_examples=50)
def test_else::statement_instantiation(instance):
    assert isinstance(instance, Else::Statement)

@given(instance=Else::If::Statement_strategy)
@settings(max_examples=50)
def test_else::if::statement_instantiation(instance):
    assert isinstance(instance, Else::If::Statement)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=Param::Assignment_strategy)
@settings(max_examples=50)
def test_param::assignment_instantiation(instance):
    assert isinstance(instance, Param::Assignment)

@given(instance=iec61131::il::Il::Operand_strategy)
@settings(max_examples=50)
def test_iec61131::il::il::operand_instantiation(instance):
    assert isinstance(instance, iec61131::il::Il::Operand)

@given(instance=iec61131::st::Param::Type1_strategy)
@settings(max_examples=50)
def test_iec61131::st::param::type1_instantiation(instance):
    assert isinstance(instance, iec61131::st::Param::Type1)

@given(instance=iec61131::st::Param::Type2_strategy)
@settings(max_examples=50)
def test_iec61131::st::param::type2_instantiation(instance):
    assert isinstance(instance, iec61131::st::Param::Type2)

@given(instance=iec61131::il::Param::Assignment2_strategy)
@settings(max_examples=50)
def test_iec61131::il::param::assignment2_instantiation(instance):
    assert isinstance(instance, iec61131::il::Param::Assignment2)

@given(instance=Subprogram::Control::Statement_strategy)
@settings(max_examples=50)
def test_subprogram::control::statement_instantiation(instance):
    assert isinstance(instance, Subprogram::Control::Statement)

@given(instance=iec61131::st::Fb::Invocation_strategy)
@settings(max_examples=50)
def test_iec61131::st::fb::invocation_instantiation(instance):
    assert isinstance(instance, iec61131::st::Fb::Invocation)

@given(instance=iec61131::st::Return::Statement_strategy)
@settings(max_examples=50)
def test_iec61131::st::return::statement_instantiation(instance):
    assert isinstance(instance, iec61131::st::Return::Statement)

@given(instance=iec61131::st::Iteration::Statement_strategy)
@settings(max_examples=50)
def test_iec61131::st::iteration::statement_instantiation(instance):
    assert isinstance(instance, iec61131::st::Iteration::Statement)

@given(instance=iec61131::st::Selection::Statement_strategy)
@settings(max_examples=50)
def test_iec61131::st::selection::statement_instantiation(instance):
    assert isinstance(instance, iec61131::st::Selection::Statement)

@given(instance=iec61131::st::Subprogram::Control::Statement_strategy)
@settings(max_examples=50)
def test_iec61131::st::subprogram::control::statement_instantiation(instance):
    assert isinstance(instance, iec61131::st::Subprogram::Control::Statement)

@given(instance=Expression::Variable_strategy)
@settings(max_examples=50)
def test_expression::variable_instantiation(instance):
    assert isinstance(instance, Expression::Variable)

@given(instance=iec61131::st::Assignment::Statement_strategy)
@settings(max_examples=50)
def test_iec61131::st::assignment::statement_instantiation(instance):
    assert isinstance(instance, iec61131::st::Assignment::Statement)

@given(instance=Or::Operator_strategy)
@settings(max_examples=50)
def test_or::operator_instantiation(instance):
    assert isinstance(instance, Or::Operator)

@given(instance=Expression::Types_strategy)
@settings(max_examples=50)
def test_expression::types_instantiation(instance):
    assert isinstance(instance, Expression::Types)

@given(instance=iec61131::st::Power::Expression_strategy)
@settings(max_examples=50)
def test_iec61131::st::power::expression_instantiation(instance):
    assert isinstance(instance, iec61131::st::Power::Expression)

@given(instance=iec61131::st::Comparison_strategy)
@settings(max_examples=50)
def test_iec61131::st::comparison_instantiation(instance):
    assert isinstance(instance, iec61131::st::Comparison)

@given(instance=iec61131::st::Equ::Expression_strategy)
@settings(max_examples=50)
def test_iec61131::st::equ::expression_instantiation(instance):
    assert isinstance(instance, iec61131::st::Equ::Expression)

@given(instance=iec61131::st::And::Expression_strategy)
@settings(max_examples=50)
def test_iec61131::st::and::expression_instantiation(instance):
    assert isinstance(instance, iec61131::st::And::Expression)

@given(instance=iec61131::st::Xor::Expression_strategy)
@settings(max_examples=50)
def test_iec61131::st::xor::expression_instantiation(instance):
    assert isinstance(instance, iec61131::st::Xor::Expression)

@given(instance=iec61131::st::Term::Expression_strategy)
@settings(max_examples=50)
def test_iec61131::st::term::expression_instantiation(instance):
    assert isinstance(instance, iec61131::st::Term::Expression)

@given(instance=iec61131::st::Primary::Expression_strategy)
@settings(max_examples=50)
def test_iec61131::st::primary::expression_instantiation(instance):
    assert isinstance(instance, iec61131::st::Primary::Expression)

@given(instance=iec61131::st::Add::Expression_strategy)
@settings(max_examples=50)
def test_iec61131::st::add::expression_instantiation(instance):
    assert isinstance(instance, iec61131::st::Add::Expression)

@given(instance=iec61131::st::Unary::Expression_strategy)
@settings(max_examples=50)
def test_iec61131::st::unary::expression_instantiation(instance):
    assert isinstance(instance, iec61131::st::Unary::Expression)

@given(instance=iec61131::st::Expression_strategy)
@settings(max_examples=50)
def test_iec61131::st::expression_instantiation(instance):
    assert isinstance(instance, iec61131::st::Expression)

@given(instance=iec61131::configurations::Prog::Data::Source_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::prog::data::source_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Prog::Data::Source)

@given(instance=iec61131::configurations::Prog::Conf::Element_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::prog::conf::element_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Prog::Conf::Element)

@given(instance=Prog::Conf::Element_strategy)
@settings(max_examples=50)
def test_prog::conf::element_instantiation(instance):
    assert isinstance(instance, Prog::Conf::Element)

@given(instance=iec61131::configurations::Prog::Cnxn_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::prog::cnxn_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Prog::Cnxn)

@given(instance=iec61131::configurations::Fb::Task_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::fb::task_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Fb::Task)

@given(instance=iec61131::configurations::Prog::Conf::Elements_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::prog::conf::elements_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Prog::Conf::Elements)

@given(instance=Task::Initialization_strategy)
@settings(max_examples=50)
def test_task::initialization_instantiation(instance):
    assert isinstance(instance, Task::Initialization)

@given(instance=iec61131::configurations::Priority_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::priority_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Priority)

@given(instance=iec61131::configurations::Interval_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::interval_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Interval)

@given(instance=iec61131::configurations::Single_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::single_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Single)

@given(instance=iec61131::configurations::Instance::Specific::Init_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::instance::specific::init_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Instance::Specific::Init)

@given(instance=iec61131::configurations::Data::Sink_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::data::sink_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Data::Sink)

@given(instance=Prog::Data::Source_strategy)
@settings(max_examples=50)
def test_prog::data::source_instantiation(instance):
    assert isinstance(instance, Prog::Data::Source)

@given(instance=Data::Sink_strategy)
@settings(max_examples=50)
def test_data::sink_instantiation(instance):
    assert isinstance(instance, Data::Sink)

@given(instance=Prog::Cnxn_strategy)
@settings(max_examples=50)
def test_prog::cnxn_instantiation(instance):
    assert isinstance(instance, Prog::Cnxn)

@given(instance=iec61131::configurations::Prog::Source_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::prog::source_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Prog::Source)

@given(instance=iec61131::configurations::Prog::Sink_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::prog::sink_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Prog::Sink)

@given(instance=Data::Source_strategy)
@settings(max_examples=50)
def test_data::source_instantiation(instance):
    assert isinstance(instance, Data::Source)

@given(instance=iec61131::configurations::Program::Output::Reference_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::program::output::reference_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Program::Output::Reference)

@given(instance=configurations::Data::Sink_strategy)
@settings(max_examples=50)
def test_configurations::data::sink_instantiation(instance):
    assert isinstance(instance, configurations::Data::Sink)

@given(instance=iec61131::configurations::Data::Source_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::data::source_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Data::Source)

@given(instance=Instance::Specific::Init_strategy)
@settings(max_examples=50)
def test_instance::specific::init_instantiation(instance):
    assert isinstance(instance, Instance::Specific::Init)

@given(instance=iec61131::configurations::Instance::Spec2_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::instance::spec2_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Instance::Spec2)

@given(instance=iec61131::configurations::Instance::Spec1_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::instance::spec1_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Instance::Spec1)

@given(instance=iec61131::configurations::Instance::Specific::Initializations_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::instance::specific::initializations_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Instance::Specific::Initializations)

@given(instance=iec61131::configurations::Task::Initialization_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::task::initialization_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Task::Initialization)

@given(instance=iec61131::configurations::Task::Name_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::task::name_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Task::Name)

@given(instance=iec61131::configurations::Task::Name_strategy)
def test_iec61131::configurations::task::name_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iec61131::configurations::Task::Name_strategy)
def test_iec61131::configurations::task::name_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iec61131::configurations::Program::Name_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::program::name_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Program::Name)

@given(instance=iec61131::configurations::Program::Name_strategy)
def test_iec61131::configurations::program::name_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iec61131::configurations::Program::Name_strategy)
def test_iec61131::configurations::program::name_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iec61131::configurations::Access::Path_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::access::path_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Access::Path)

@given(instance=iec61131::configurations::Access::Name_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::access::name_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Access::Name)

@given(instance=iec61131::configurations::Access::Name_strategy)
def test_iec61131::configurations::access::name_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iec61131::configurations::Access::Name_strategy)
def test_iec61131::configurations::access::name_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Access::Path_strategy)
@settings(max_examples=50)
def test_access::path_instantiation(instance):
    assert isinstance(instance, Access::Path)

@given(instance=iec61131::configurations::Symbolic::Path_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::symbolic::path_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Symbolic::Path)

@given(instance=iec61131::configurations::Direct::Path_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::direct::path_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Direct::Path)

@given(instance=iec61131::configurations::Access::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::access::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Access::Declaration)

@given(instance=iec61131::configurations::Access::Declaration_strategy)
def test_iec61131::configurations::access::declaration_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=iec61131::configurations::Access::Declaration_strategy)
def test_iec61131::configurations::access::declaration_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=Access::Declaration_strategy)
@settings(max_examples=50)
def test_access::declaration_instantiation(instance):
    assert isinstance(instance, Access::Declaration)

@given(instance=iec61131::configurations::Access::Declarations_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::access::declarations_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Access::Declarations)

@given(instance=Resource::Declaration_strategy)
@settings(max_examples=50)
def test_resource::declaration_instantiation(instance):
    assert isinstance(instance, Resource::Declaration)

@given(instance=Access::Declarations_strategy)
@settings(max_examples=50)
def test_access::declarations_instantiation(instance):
    assert isinstance(instance, Access::Declarations)

@given(instance=Instance::Specific::Initializations_strategy)
@settings(max_examples=50)
def test_instance::specific::initializations_instantiation(instance):
    assert isinstance(instance, Instance::Specific::Initializations)

@given(instance=Global::Var::Declarations_strategy)
@settings(max_examples=50)
def test_global::var::declarations_instantiation(instance):
    assert isinstance(instance, Global::Var::Declarations)

@given(instance=Single::Resource::Declaration_strategy)
@settings(max_examples=50)
def test_single::resource::declaration_instantiation(instance):
    assert isinstance(instance, Single::Resource::Declaration)

@given(instance=Configuration::Name_strategy)
@settings(max_examples=50)
def test_configuration::name_instantiation(instance):
    assert isinstance(instance, Configuration::Name)

@given(instance=iec61131::configurations::Resource::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::resource::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Resource::Type::Name)

@given(instance=Prog::Conf::Elements_strategy)
@settings(max_examples=50)
def test_prog::conf::elements_instantiation(instance):
    assert isinstance(instance, Prog::Conf::Elements)

@given(instance=Program::Name_strategy)
@settings(max_examples=50)
def test_program::name_instantiation(instance):
    assert isinstance(instance, Program::Name)

@given(instance=Single_strategy)
@settings(max_examples=50)
def test_single_instantiation(instance):
    assert isinstance(instance, Single)

@given(instance=Priority_strategy)
@settings(max_examples=50)
def test_priority_instantiation(instance):
    assert isinstance(instance, Priority)

@given(instance=Task::Name_strategy)
@settings(max_examples=50)
def test_task::name_instantiation(instance):
    assert isinstance(instance, Task::Name)

@given(instance=iec61131::configurations::Task::Configuration_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::task::configuration_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Task::Configuration)

@given(instance=Program::Configuration_strategy)
@settings(max_examples=50)
def test_program::configuration_instantiation(instance):
    assert isinstance(instance, Program::Configuration)

@given(instance=Task::Configuration_strategy)
@settings(max_examples=50)
def test_task::configuration_instantiation(instance):
    assert isinstance(instance, Task::Configuration)

@given(instance=iec61131::configurations::Single::Resource::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::single::resource::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Single::Resource::Declaration)

@given(instance=Resource::Type::Name_strategy)
@settings(max_examples=50)
def test_resource::type::name_instantiation(instance):
    assert isinstance(instance, Resource::Type::Name)

@given(instance=Resource::Name_strategy)
@settings(max_examples=50)
def test_resource::name_instantiation(instance):
    assert isinstance(instance, Resource::Name)

@given(instance=iec61131::configurations::Resource::Name_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::resource::name_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Resource::Name)

@given(instance=iec61131::configurations::Resource::Name_strategy)
def test_iec61131::configurations::resource::name_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iec61131::configurations::Resource::Name_strategy)
def test_iec61131::configurations::resource::name_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Simple::Type::Name_strategy)
@settings(max_examples=50)
def test_simple::type::name_instantiation(instance):
    assert isinstance(instance, Simple::Type::Name)

@given(instance=Single::Element::Type::Declaration_strategy)
@settings(max_examples=50)
def test_single::element::type::declaration_instantiation(instance):
    assert isinstance(instance, Single::Element::Type::Declaration)

@given(instance=iec61131::pous::Subrange::Type::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::pous::subrange::type::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Subrange::Type::Declaration)

@given(instance=iec61131::pous::Simple::Type::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::pous::simple::type::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Simple::Type::Declaration)

@given(instance=iec61131::configurations::Configuration::Name_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::configuration::name_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Configuration::Name)

@given(instance=Function::Block::Declaration_strategy)
@settings(max_examples=50)
def test_function::block::declaration_instantiation(instance):
    assert isinstance(instance, Function::Block::Declaration)

@given(instance=Function::Declaration_strategy)
@settings(max_examples=50)
def test_function::declaration_instantiation(instance):
    assert isinstance(instance, Function::Declaration)

@given(instance=Program::Declaration_strategy)
@settings(max_examples=50)
def test_program::declaration_instantiation(instance):
    assert isinstance(instance, Program::Declaration)

@given(instance=iec61131::pous::Library_strategy)
@settings(max_examples=50)
def test_iec61131::pous::library_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Library)

@given(instance=Program::Access::Decl_strategy)
@settings(max_examples=50)
def test_program::access::decl_instantiation(instance):
    assert isinstance(instance, Program::Access::Decl)

@given(instance=iec61131::pous::Function::Block::Vars_strategy)
@settings(max_examples=50)
def test_iec61131::pous::function::block::vars_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Function::Block::Vars)

@given(instance=iec61131::pous::Function::Vars_strategy)
@settings(max_examples=50)
def test_iec61131::pous::function::vars_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Function::Vars)

@given(instance=iec61131::pous::Program::Vars_strategy)
@settings(max_examples=50)
def test_iec61131::pous::program::vars_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Program::Vars)

@given(instance=iec61131::pous::Structure::Elements_strategy)
@settings(max_examples=50)
def test_iec61131::pous::structure::elements_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Structure::Elements)

@given(instance=Structure::Elements_strategy)
@settings(max_examples=50)
def test_structure::elements_instantiation(instance):
    assert isinstance(instance, Structure::Elements)

@given(instance=iec61131::pous::Structure::Element::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::pous::structure::element::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Structure::Element::Declaration)

@given(instance=Structure::Element::Declaration_strategy)
@settings(max_examples=50)
def test_structure::element::declaration_instantiation(instance):
    assert isinstance(instance, Structure::Element::Declaration)

@given(instance=iec61131::pous::Structure::Specification_strategy)
@settings(max_examples=50)
def test_iec61131::pous::structure::specification_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Structure::Specification)

@given(instance=Enumerated::Spec::Init_strategy)
@settings(max_examples=50)
def test_enumerated::spec::init_instantiation(instance):
    assert isinstance(instance, Enumerated::Spec::Init)

@given(instance=iec61131::pous::Enumerated::Type::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::pous::enumerated::type::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Enumerated::Type::Declaration)

@given(instance=Subrange::Spec::Init_strategy)
@settings(max_examples=50)
def test_subrange::spec::init_instantiation(instance):
    assert isinstance(instance, Subrange::Spec::Init)

@given(instance=pous::Function::Block::Body_strategy)
@settings(max_examples=50)
def test_pous::function::block::body_instantiation(instance):
    assert isinstance(instance, pous::Function::Block::Body)

@given(instance=pous::Function::Body_strategy)
@settings(max_examples=50)
def test_pous::function::body_instantiation(instance):
    assert isinstance(instance, pous::Function::Body)

@given(instance=iec61131::ld::Ladder::Diagram_strategy)
@settings(max_examples=50)
def test_iec61131::ld::ladder::diagram_instantiation(instance):
    assert isinstance(instance, iec61131::ld::Ladder::Diagram)

@given(instance=iec61131::st::Statement::List_strategy)
@settings(max_examples=50)
def test_iec61131::st::statement::list_instantiation(instance):
    assert isinstance(instance, iec61131::st::Statement::List)

@given(instance=iec61131::il::Instruction::List_strategy)
@settings(max_examples=50)
def test_iec61131::il::instruction::list_instantiation(instance):
    assert isinstance(instance, iec61131::il::Instruction::List)

@given(instance=iec61131::fbd::Function::Block::Diagram_strategy)
@settings(max_examples=50)
def test_iec61131::fbd::function::block::diagram_instantiation(instance):
    assert isinstance(instance, iec61131::fbd::Function::Block::Diagram)

@given(instance=iec61131::pous::Other::Language_strategy)
@settings(max_examples=50)
def test_iec61131::pous::other::language_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Other::Language)

@given(instance=iec61131::pous::Other::Language_strategy)
def test_iec61131::pous::other::language_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=iec61131::pous::Other::Language_strategy)
def test_iec61131::pous::other::language_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=iec61131::pous::Function::Body_strategy)
@settings(max_examples=50)
def test_iec61131::pous::function::body_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Function::Body)

@given(instance=iec61131::pous::Function::Return::Value_strategy)
@settings(max_examples=50)
def test_iec61131::pous::function::return::value_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Function::Return::Value)

@given(instance=pous::Function::Name_strategy)
@settings(max_examples=50)
def test_pous::function::name_instantiation(instance):
    assert isinstance(instance, pous::Function::Name)

@given(instance=Function::Body_strategy)
@settings(max_examples=50)
def test_function::body_instantiation(instance):
    assert isinstance(instance, Function::Body)

@given(instance=Function::Vars_strategy)
@settings(max_examples=50)
def test_function::vars_instantiation(instance):
    assert isinstance(instance, Function::Vars)

@given(instance=Byte::String::Type::Name_strategy)
@settings(max_examples=50)
def test_byte::string::type::name_instantiation(instance):
    assert isinstance(instance, Byte::String::Type::Name)

@given(instance=iec61131::types::Single::Byte::String::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::single::byte::string::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::Single::Byte::String::Type::Name)

@given(instance=iec61131::types::Double::Byte::String::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::double::byte::string::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::Double::Byte::String::Type::Name)

@given(instance=String::Type::Name_strategy)
@settings(max_examples=50)
def test_string::type::name_instantiation(instance):
    assert isinstance(instance, String::Type::Name)

@given(instance=Structure::Specification_strategy)
@settings(max_examples=50)
def test_structure::specification_instantiation(instance):
    assert isinstance(instance, Structure::Specification)

@given(instance=iec61131::pous::Structure::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::pous::structure::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Structure::Declaration)

@given(instance=iec61131::pous::Type::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::pous::type::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Type::Declaration)

@given(instance=Type::Declaration_strategy)
@settings(max_examples=50)
def test_type::declaration_instantiation(instance):
    assert isinstance(instance, Type::Declaration)

@given(instance=iec61131::pous::Structure::Type::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::pous::structure::type::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Structure::Type::Declaration)

@given(instance=iec61131::pous::Array::Type::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::pous::array::type::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Array::Type::Declaration)

@given(instance=iec61131::pous::Single::Element::Type::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::pous::single::element::type::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Single::Element::Type::Declaration)

@given(instance=iec61131::pous::String::Type::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::pous::string::type::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::pous::String::Type::Declaration)

@given(instance=iec61131::pous::Function::Name_strategy)
@settings(max_examples=50)
def test_iec61131::pous::function::name_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Function::Name)

@given(instance=iec61131::pous::Access::Name_strategy)
@settings(max_examples=50)
def test_iec61131::pous::access::name_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Access::Name)

@given(instance=iec61131::pous::Access::Name_strategy)
def test_iec61131::pous::access::name_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iec61131::pous::Access::Name_strategy)
def test_iec61131::pous::access::name_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Symbolic::Variable_strategy)
@settings(max_examples=50)
def test_symbolic::variable_instantiation(instance):
    assert isinstance(instance, Symbolic::Variable)

@given(instance=iec61131::variables::Multi::Element::Variable_strategy)
@settings(max_examples=50)
def test_iec61131::variables::multi::element::variable_instantiation(instance):
    assert isinstance(instance, iec61131::variables::Multi::Element::Variable)

@given(instance=Access::Name_strategy)
@settings(max_examples=50)
def test_access::name_instantiation(instance):
    assert isinstance(instance, Access::Name)

@given(instance=iec61131::pous::Program::Access::Decl_strategy)
@settings(max_examples=50)
def test_iec61131::pous::program::access::decl_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Program::Access::Decl)

@given(instance=iec61131::pous::Program::Access::Decl_strategy)
def test_iec61131::pous::program::access::decl_direction_type(instance):
    assert isinstance(instance.direction, str)


@given(instance=iec61131::pous::Program::Access::Decl_strategy)
def test_iec61131::pous::program::access::decl_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=iec61131::pous::Function::Block::Body_strategy)
@settings(max_examples=50)
def test_iec61131::pous::function::block::body_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Function::Block::Body)

@given(instance=Program::Type::Name_strategy)
@settings(max_examples=50)
def test_program::type::name_instantiation(instance):
    assert isinstance(instance, Program::Type::Name)

@given(instance=Function::Return::Value_strategy)
@settings(max_examples=50)
def test_function::return::value_instantiation(instance):
    assert isinstance(instance, Function::Return::Value)

@given(instance=Derived::Function::Name_strategy)
@settings(max_examples=50)
def test_derived::function::name_instantiation(instance):
    assert isinstance(instance, Derived::Function::Name)

@given(instance=Function::Block::Vars_strategy)
@settings(max_examples=50)
def test_function::block::vars_instantiation(instance):
    assert isinstance(instance, Function::Block::Vars)

@given(instance=Derived::Function::Block::Name_strategy)
@settings(max_examples=50)
def test_derived::function::block::name_instantiation(instance):
    assert isinstance(instance, Derived::Function::Block::Name)

@given(instance=pous::Function::Block::Type::Name_strategy)
@settings(max_examples=50)
def test_pous::function::block::type::name_instantiation(instance):
    assert isinstance(instance, pous::Function::Block::Type::Name)

@given(instance=types::Simple::Specification_strategy)
@settings(max_examples=50)
def test_types::simple::specification_instantiation(instance):
    assert isinstance(instance, types::Simple::Specification)

@given(instance=iec61131::types::Elementary::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::elementary::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::Elementary::Type::Name)

@given(instance=iec61131::types::Simple::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::simple::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::Simple::Type::Name)

@given(instance=iec61131::types::Generic::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::generic::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::Generic::Type::Name)

@given(instance=Blocks_strategy)
@settings(max_examples=50)
def test_blocks_instantiation(instance):
    assert isinstance(instance, Blocks)

@given(instance=iec61131::pous::Derived::Function::Block::Name_strategy)
@settings(max_examples=50)
def test_iec61131::pous::derived::function::block::name_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Derived::Function::Block::Name)

@given(instance=iec61131::pous::Derived::Function::Name_strategy)
@settings(max_examples=50)
def test_iec61131::pous::derived::function::name_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Derived::Function::Name)

@given(instance=iec61131::pous::Program::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::pous::program::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Program::Type::Name)

@given(instance=Function::Block::Body_strategy)
@settings(max_examples=50)
def test_function::block::body_instantiation(instance):
    assert isinstance(instance, Function::Block::Body)

@given(instance=iec61131::sfc::Sequential::Function::Chart_strategy)
@settings(max_examples=50)
def test_iec61131::sfc::sequential::function::chart_instantiation(instance):
    assert isinstance(instance, iec61131::sfc::Sequential::Function::Chart)

@given(instance=iec61131::interfaces::InitElement::Array_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::initelement::array_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::InitElement::Array)

@given(instance=iec61131::interfaces::Temp::Var::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::temp::var::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Temp::Var::Declaration)

@given(instance=iec61131::interfaces::InitElement::Structure_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::initelement::structure_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::InitElement::Structure)

@given(instance=iec61131::interfaces::Var1::Specification::Func_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::var1::specification::func_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Var1::Specification::Func)

@given(instance=iec61131::interfaces::Simple::Specification::Func_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::simple::specification::func_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Simple::Specification::Func)

@given(instance=Simple::Specification::Func_strategy)
@settings(max_examples=50)
def test_simple::specification::func_instantiation(instance):
    assert isinstance(instance, Simple::Specification::Func)

@given(instance=Var1::Specification::Func_strategy)
@settings(max_examples=50)
def test_var1::specification::func_instantiation(instance):
    assert isinstance(instance, Var1::Specification::Func)

@given(instance=iec61131::interfaces::Simple::Spec::Init::Func_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::simple::spec::init::func_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Simple::Spec::Init::Func)

@given(instance=iec61131::interfaces::Var::Init::Decl::Func_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::var::init::decl::func_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Var::Init::Decl::Func)

@given(instance=Simple::Spec::Init_strategy)
@settings(max_examples=50)
def test_simple::spec::init_instantiation(instance):
    assert isinstance(instance, Simple::Spec::Init)

@given(instance=iec61131::interfaces::Var::Name::Decl_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::var::name::decl_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Var::Name::Decl)

@given(instance=iec61131::interfaces::Function::Var::Decl_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::function::var::decl_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Function::Var::Decl)

@given(instance=iec61131::interfaces::Function::Var::Decl_strategy)
def test_iec61131::interfaces::function::var::decl_constant_type(instance):
    assert isinstance(instance.constant, bool)


@given(instance=iec61131::interfaces::Function::Var::Decl_strategy)
def test_iec61131::interfaces::function::var::decl_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=iec61131::interfaces::Var2::Init::Decl_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::var2::init::decl_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Var2::Init::Decl)

@given(instance=Array::Type::Name_strategy)
@settings(max_examples=50)
def test_array::type::name_instantiation(instance):
    assert isinstance(instance, Array::Type::Name)

@given(instance=iec61131::interfaces::Array::Specification1_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::array::specification1_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Array::Specification1)

@given(instance=iec61131::interfaces::InitElement::EnumValue_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::initelement::enumvalue_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::InitElement::EnumValue)

@given(instance=iec61131::interfaces::InitElement::Constant_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::initelement::constant_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::InitElement::Constant)

@given(instance=iec61131::interfaces::Initial::Element_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::initial::element_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Initial::Element)

@given(instance=iec61131::interfaces::Array::Initial::Elements2_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::array::initial::elements2_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Array::Initial::Elements2)

@given(instance=iec61131::interfaces::Array::Initial::Elements1_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::array::initial::elements1_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Array::Initial::Elements1)

@given(instance=Non::Generic::Type::Name_strategy)
@settings(max_examples=50)
def test_non::generic::type::name_instantiation(instance):
    assert isinstance(instance, Non::Generic::Type::Name)

@given(instance=iec61131::types::Derived::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::derived::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::Derived::Type::Name)

@given(instance=iec61131::interfaces::Array::Specification2_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::array::specification2_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Array::Specification2)

@given(instance=Global::Var::Decl_strategy)
@settings(max_examples=50)
def test_global::var::decl_instantiation(instance):
    assert isinstance(instance, Global::Var::Decl)

@given(instance=Library::Element::Declaration_strategy)
@settings(max_examples=50)
def test_library::element::declaration_instantiation(instance):
    assert isinstance(instance, Library::Element::Declaration)

@given(instance=iec61131::configurations::Configuration::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::configuration::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Configuration::Declaration)

@given(instance=iec61131::pous::Function::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::pous::function::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Function::Declaration)

@given(instance=iec61131::pous::Function::Block::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::pous::function::block::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Function::Block::Declaration)

@given(instance=iec61131::configurations::Resource::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::resource::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Resource::Declaration)

@given(instance=iec61131::pous::Data::Type::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::pous::data::type::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Data::Type::Declaration)

@given(instance=iec61131::pous::Program::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::pous::program::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Program::Declaration)

@given(instance=iec61131::interfaces::Global::Var::Declarations_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::global::var::declarations_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Global::Var::Declarations)

@given(instance=iec61131::interfaces::Global::Var::Declarations_strategy)
def test_iec61131::interfaces::global::var::declarations_retain_type(instance):
    assert isinstance(instance.retain, bool)


@given(instance=iec61131::interfaces::Global::Var::Declarations_strategy)
def test_iec61131::interfaces::global::var::declarations_retain_setter(instance):
    original = instance.retain
    instance.retain = original
    assert instance.retain == original

@given(instance=iec61131::interfaces::Global::Var::Declarations_strategy)
def test_iec61131::interfaces::global::var::declarations_constant_type(instance):
    assert isinstance(instance.constant, bool)


@given(instance=iec61131::interfaces::Global::Var::Declarations_strategy)
def test_iec61131::interfaces::global::var::declarations_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=Located::Var::Decl_strategy)
@settings(max_examples=50)
def test_located::var::decl_instantiation(instance):
    assert isinstance(instance, Located::Var::Decl)

@given(instance=Program::Vars_strategy)
@settings(max_examples=50)
def test_program::vars_instantiation(instance):
    assert isinstance(instance, Program::Vars)

@given(instance=iec61131::pous::Program::Access::Decls_strategy)
@settings(max_examples=50)
def test_iec61131::pous::program::access::decls_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Program::Access::Decls)

@given(instance=iec61131::interfaces::Located::Var::Declarations_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::located::var::declarations_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Located::Var::Declarations)

@given(instance=iec61131::interfaces::Located::Var::Declarations_strategy)
def test_iec61131::interfaces::located::var::declarations_retain_type(instance):
    assert isinstance(instance.retain, bool)


@given(instance=iec61131::interfaces::Located::Var::Declarations_strategy)
def test_iec61131::interfaces::located::var::declarations_retain_setter(instance):
    original = instance.retain
    instance.retain = original
    assert instance.retain == original

@given(instance=iec61131::interfaces::Located::Var::Declarations_strategy)
def test_iec61131::interfaces::located::var::declarations_constant_type(instance):
    assert isinstance(instance.constant, bool)


@given(instance=iec61131::interfaces::Located::Var::Declarations_strategy)
def test_iec61131::interfaces::located::var::declarations_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=iec61131::interfaces::Enumerated::Specification2_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::enumerated::specification2_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Enumerated::Specification2)

@given(instance=iec61131::interfaces::Enumerated::Specification1_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::enumerated::specification1_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Enumerated::Specification1)

@given(instance=Subrange::Type::Name_strategy)
@settings(max_examples=50)
def test_subrange::type::name_instantiation(instance):
    assert isinstance(instance, Subrange::Type::Name)

@given(instance=iec61131::interfaces::Subrange::Specification2_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::subrange::specification2_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Subrange::Specification2)

@given(instance=Subrange_strategy)
@settings(max_examples=50)
def test_subrange_instantiation(instance):
    assert isinstance(instance, Subrange)

@given(instance=iec61131::interfaces::Subrange::Specification1_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::subrange::specification1_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Subrange::Specification1)

@given(instance=Double::Byte::String::Type::Name_strategy)
@settings(max_examples=50)
def test_double::byte::string::type::name_instantiation(instance):
    assert isinstance(instance, Double::Byte::String::Type::Name)

@given(instance=Single::Byte::String::Type::Name_strategy)
@settings(max_examples=50)
def test_single::byte::string::type::name_instantiation(instance):
    assert isinstance(instance, Single::Byte::String::Type::Name)

@given(instance=Byte::String_strategy)
@settings(max_examples=50)
def test_byte::string_instantiation(instance):
    assert isinstance(instance, Byte::String)

@given(instance=iec61131::interfaces::Double::BString_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::double::bstring_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Double::BString)

@given(instance=iec61131::interfaces::Single::BString_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::single::bstring_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Single::BString)

@given(instance=iec61131::interfaces::Byte::String_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::byte::string_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Byte::String)

@given(instance=iec61131::interfaces::Range_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::range_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Range)

@given(instance=iec61131::interfaces::Input::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::input::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Input::Declaration)

@given(instance=iec61131::interfaces::Global::Var::Location_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::global::var::location_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Global::Var::Location)

@given(instance=iec61131::interfaces::Global::Var::Spec_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::global::var::spec_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Global::Var::Spec)

@given(instance=External::Specification_strategy)
@settings(max_examples=50)
def test_external::specification_instantiation(instance):
    assert isinstance(instance, External::Specification)

@given(instance=Global::Var::Name_strategy)
@settings(max_examples=50)
def test_global::var::name_instantiation(instance):
    assert isinstance(instance, Global::Var::Name)

@given(instance=iec61131::interfaces::External::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::external::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::External::Declaration)

@given(instance=RNV::Declarations_strategy)
@settings(max_examples=50)
def test_rnv::declarations_instantiation(instance):
    assert isinstance(instance, RNV::Declarations)

@given(instance=iec61131::interfaces::Var::Declarations_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::var::declarations_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Var::Declarations)

@given(instance=iec61131::interfaces::Var::Declarations_strategy)
def test_iec61131::interfaces::var::declarations_constant_type(instance):
    assert isinstance(instance.constant, bool)


@given(instance=iec61131::interfaces::Var::Declarations_strategy)
def test_iec61131::interfaces::var::declarations_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=iec61131::interfaces::Non::Retentive::Var::Declarations_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::non::retentive::var::declarations_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Non::Retentive::Var::Declarations)

@given(instance=iec61131::interfaces::Retentive::Var::Declarations_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::retentive::var::declarations_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Retentive::Var::Declarations)

@given(instance=External::Declaration_strategy)
@settings(max_examples=50)
def test_external::declaration_instantiation(instance):
    assert isinstance(instance, External::Declaration)

@given(instance=Other::Var::Declaration_strategy)
@settings(max_examples=50)
def test_other::var::declaration_instantiation(instance):
    assert isinstance(instance, Other::Var::Declaration)

@given(instance=iec61131::interfaces::RNV::Declarations_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::rnv::declarations_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::RNV::Declarations)

@given(instance=iec61131::interfaces::Temp::Var::Decls_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::temp::var::decls_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Temp::Var::Decls)

@given(instance=iec61131::interfaces::External::Var::Declarations_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::external::var::declarations_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::External::Var::Declarations)

@given(instance=iec61131::interfaces::External::Var::Declarations_strategy)
def test_iec61131::interfaces::external::var::declarations_constant_type(instance):
    assert isinstance(instance.constant, bool)


@given(instance=iec61131::interfaces::External::Var::Declarations_strategy)
def test_iec61131::interfaces::external::var::declarations_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=iec61131::interfaces::Incompl::Located::Var::Declarations_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::incompl::located::var::declarations_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Incompl::Located::Var::Declarations)

@given(instance=iec61131::interfaces::Incompl::Located::Var::Declarations_strategy)
def test_iec61131::interfaces::incompl::located::var::declarations_retain_type(instance):
    assert isinstance(instance.retain, bool)


@given(instance=iec61131::interfaces::Incompl::Located::Var::Declarations_strategy)
def test_iec61131::interfaces::incompl::located::var::declarations_retain_setter(instance):
    original = instance.retain
    instance.retain = original
    assert instance.retain == original

@given(instance=operators::Multiply::Operator_strategy)
@settings(max_examples=50)
def test_operators::multiply::operator_instantiation(instance):
    assert isinstance(instance, operators::Multiply::Operator)

@given(instance=operators::Add::Operator_strategy)
@settings(max_examples=50)
def test_operators::add::operator_instantiation(instance):
    assert isinstance(instance, operators::Add::Operator)

@given(instance=operators::Arithmetic::Name_strategy)
@settings(max_examples=50)
def test_operators::arithmetic::name_instantiation(instance):
    assert isinstance(instance, operators::Arithmetic::Name)

@given(instance=iec61131::operators::Divide::Name_strategy)
@settings(max_examples=50)
def test_iec61131::operators::divide::name_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Divide::Name)

@given(instance=iec61131::operators::Multiply::Name_strategy)
@settings(max_examples=50)
def test_iec61131::operators::multiply::name_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Multiply::Name)

@given(instance=operators::Addition::Operator_strategy)
@settings(max_examples=50)
def test_operators::addition::operator_instantiation(instance):
    assert isinstance(instance, operators::Addition::Operator)

@given(instance=iec61131::operators::Addition::Symbol_strategy)
@settings(max_examples=50)
def test_iec61131::operators::addition::symbol_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Addition::Symbol)

@given(instance=iec61131::operators::Addition::Name_strategy)
@settings(max_examples=50)
def test_iec61131::operators::addition::name_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Addition::Name)

@given(instance=Comparison::Operator_strategy)
@settings(max_examples=50)
def test_comparison::operator_instantiation(instance):
    assert isinstance(instance, Comparison::Operator)

@given(instance=iec61131::operators::LessEqual::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::operators::lessequal::operator_instantiation(instance):
    assert isinstance(instance, iec61131::operators::LessEqual::Operator)

@given(instance=iec61131::operators::GreaterEqual::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::operators::greaterequal::operator_instantiation(instance):
    assert isinstance(instance, iec61131::operators::GreaterEqual::Operator)

@given(instance=iec61131::operators::Greater::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::operators::greater::operator_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Greater::Operator)

@given(instance=iec61131::operators::Less::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::operators::less::operator_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Less::Operator)

@given(instance=Il::Expr::Operator_strategy)
@settings(max_examples=50)
def test_il::expr::operator_instantiation(instance):
    assert isinstance(instance, Il::Expr::Operator)

@given(instance=iec61131::operators::Arithmetic::Name_strategy)
@settings(max_examples=50)
def test_iec61131::operators::arithmetic::name_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Arithmetic::Name)

@given(instance=iec61131::operators::Comparison::Name_strategy)
@settings(max_examples=50)
def test_iec61131::operators::comparison::name_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Comparison::Name)

@given(instance=operators::Substraction::Operator_strategy)
@settings(max_examples=50)
def test_operators::substraction::operator_instantiation(instance):
    assert isinstance(instance, operators::Substraction::Operator)

@given(instance=iec61131::operators::Substraction::Name_strategy)
@settings(max_examples=50)
def test_iec61131::operators::substraction::name_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Substraction::Name)

@given(instance=GreaterEqual::Operator_strategy)
@settings(max_examples=50)
def test_greaterequal::operator_instantiation(instance):
    assert isinstance(instance, GreaterEqual::Operator)

@given(instance=iec61131::operators::GreaterEqual::Symbol_strategy)
@settings(max_examples=50)
def test_iec61131::operators::greaterequal::symbol_instantiation(instance):
    assert isinstance(instance, iec61131::operators::GreaterEqual::Symbol)

@given(instance=operators::GreaterEqual::Operator_strategy)
@settings(max_examples=50)
def test_operators::greaterequal::operator_instantiation(instance):
    assert isinstance(instance, operators::GreaterEqual::Operator)

@given(instance=Greater::Operator_strategy)
@settings(max_examples=50)
def test_greater::operator_instantiation(instance):
    assert isinstance(instance, Greater::Operator)

@given(instance=iec61131::operators::Greater::Symbol_strategy)
@settings(max_examples=50)
def test_iec61131::operators::greater::symbol_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Greater::Symbol)

@given(instance=operators::Greater::Operator_strategy)
@settings(max_examples=50)
def test_operators::greater::operator_instantiation(instance):
    assert isinstance(instance, operators::Greater::Operator)

@given(instance=LessEqual::Operator_strategy)
@settings(max_examples=50)
def test_lessequal::operator_instantiation(instance):
    assert isinstance(instance, LessEqual::Operator)

@given(instance=iec61131::operators::LessEqual::Symbol_strategy)
@settings(max_examples=50)
def test_iec61131::operators::lessequal::symbol_instantiation(instance):
    assert isinstance(instance, iec61131::operators::LessEqual::Symbol)

@given(instance=operators::LessEqual::Operator_strategy)
@settings(max_examples=50)
def test_operators::lessequal::operator_instantiation(instance):
    assert isinstance(instance, operators::LessEqual::Operator)

@given(instance=Less::Operator_strategy)
@settings(max_examples=50)
def test_less::operator_instantiation(instance):
    assert isinstance(instance, Less::Operator)

@given(instance=iec61131::operators::Less::Symbol_strategy)
@settings(max_examples=50)
def test_iec61131::operators::less::symbol_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Less::Symbol)

@given(instance=operators::Less::Operator_strategy)
@settings(max_examples=50)
def test_operators::less::operator_instantiation(instance):
    assert isinstance(instance, operators::Less::Operator)

@given(instance=Unequal::Operator_strategy)
@settings(max_examples=50)
def test_unequal::operator_instantiation(instance):
    assert isinstance(instance, Unequal::Operator)

@given(instance=iec61131::operators::Unequal::Symbol_strategy)
@settings(max_examples=50)
def test_iec61131::operators::unequal::symbol_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Unequal::Symbol)

@given(instance=operators::Unequal::Operator_strategy)
@settings(max_examples=50)
def test_operators::unequal::operator_instantiation(instance):
    assert isinstance(instance, operators::Unequal::Operator)

@given(instance=Equal::Operator_strategy)
@settings(max_examples=50)
def test_equal::operator_instantiation(instance):
    assert isinstance(instance, Equal::Operator)

@given(instance=iec61131::operators::Equal::Symbol_strategy)
@settings(max_examples=50)
def test_iec61131::operators::equal::symbol_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Equal::Symbol)

@given(instance=operators::Comparison::Name_strategy)
@settings(max_examples=50)
def test_operators::comparison::name_instantiation(instance):
    assert isinstance(instance, operators::Comparison::Name)

@given(instance=iec61131::operators::Unequal::Name_strategy)
@settings(max_examples=50)
def test_iec61131::operators::unequal::name_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Unequal::Name)

@given(instance=iec61131::operators::GreaterEqual::Name_strategy)
@settings(max_examples=50)
def test_iec61131::operators::greaterequal::name_instantiation(instance):
    assert isinstance(instance, iec61131::operators::GreaterEqual::Name)

@given(instance=iec61131::operators::Greater::Name_strategy)
@settings(max_examples=50)
def test_iec61131::operators::greater::name_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Greater::Name)

@given(instance=iec61131::operators::LessEqual::Name_strategy)
@settings(max_examples=50)
def test_iec61131::operators::lessequal::name_instantiation(instance):
    assert isinstance(instance, iec61131::operators::LessEqual::Name)

@given(instance=iec61131::operators::Less::Name_strategy)
@settings(max_examples=50)
def test_iec61131::operators::less::name_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Less::Name)

@given(instance=operators::Equal::Operator_strategy)
@settings(max_examples=50)
def test_operators::equal::operator_instantiation(instance):
    assert isinstance(instance, operators::Equal::Operator)

@given(instance=iec61131::operators::Equal::Name_strategy)
@settings(max_examples=50)
def test_iec61131::operators::equal::name_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Equal::Name)

@given(instance=And::Operator_strategy)
@settings(max_examples=50)
def test_and::operator_instantiation(instance):
    assert isinstance(instance, And::Operator)

@given(instance=iec61131::operators::And::Name_strategy)
@settings(max_examples=50)
def test_iec61131::operators::and::name_instantiation(instance):
    assert isinstance(instance, iec61131::operators::And::Name)

@given(instance=iec61131::operators::And::Symbol_strategy)
@settings(max_examples=50)
def test_iec61131::operators::and::symbol_instantiation(instance):
    assert isinstance(instance, iec61131::operators::And::Symbol)

@given(instance=Assignment::Operator_strategy)
@settings(max_examples=50)
def test_assignment::operator_instantiation(instance):
    assert isinstance(instance, Assignment::Operator)

@given(instance=iec61131::operators::Assignment::Name_strategy)
@settings(max_examples=50)
def test_iec61131::operators::assignment::name_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Assignment::Name)

@given(instance=iec61131::operators::Assignment::Symbol_strategy)
@settings(max_examples=50)
def test_iec61131::operators::assignment::symbol_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Assignment::Symbol)

@given(instance=Power::Operator_strategy)
@settings(max_examples=50)
def test_power::operator_instantiation(instance):
    assert isinstance(instance, Power::Operator)

@given(instance=iec61131::operators::Power::Name_strategy)
@settings(max_examples=50)
def test_iec61131::operators::power::name_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Power::Name)

@given(instance=iec61131::operators::Power::Symbol_strategy)
@settings(max_examples=50)
def test_iec61131::operators::power::symbol_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Power::Symbol)

@given(instance=Divide::Operator_strategy)
@settings(max_examples=50)
def test_divide::operator_instantiation(instance):
    assert isinstance(instance, Divide::Operator)

@given(instance=iec61131::operators::Divide::Symbol_strategy)
@settings(max_examples=50)
def test_iec61131::operators::divide::symbol_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Divide::Symbol)

@given(instance=iec61131::literals::Integer_strategy)
@settings(max_examples=50)
def test_iec61131::literals::integer_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Integer)

@given(instance=iec61131::literals::Integer_strategy)
def test_iec61131::literals::integer_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=iec61131::literals::Integer_strategy)
def test_iec61131::literals::integer_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=iec61131::literals::BSInteger_strategy)
@settings(max_examples=50)
def test_iec61131::literals::bsinteger_instantiation(instance):
    assert isinstance(instance, iec61131::literals::BSInteger)

@given(instance=iec61131::literals::Date::Literal_strategy)
@settings(max_examples=50)
def test_iec61131::literals::date::literal_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Date::Literal)

@given(instance=iec61131::literals::Date::Literal_strategy)
def test_iec61131::literals::date::literal_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=iec61131::literals::Date::Literal_strategy)
def test_iec61131::literals::date::literal_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=iec61131::literals::Date::Literal_strategy)
def test_iec61131::literals::date::literal_day_type(instance):
    assert isinstance(instance.day, str)


@given(instance=iec61131::literals::Date::Literal_strategy)
def test_iec61131::literals::date::literal_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original

@given(instance=iec61131::literals::Date::Literal_strategy)
def test_iec61131::literals::date::literal_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=iec61131::literals::Date::Literal_strategy)
def test_iec61131::literals::date::literal_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=iec61131::literals::Daytime_strategy)
@settings(max_examples=50)
def test_iec61131::literals::daytime_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Daytime)

@given(instance=iec61131::literals::Daytime_strategy)
def test_iec61131::literals::daytime_hour_type(instance):
    assert isinstance(instance.hour, str)


@given(instance=iec61131::literals::Daytime_strategy)
def test_iec61131::literals::daytime_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original

@given(instance=iec61131::literals::Daytime_strategy)
def test_iec61131::literals::daytime_minute_type(instance):
    assert isinstance(instance.minute, str)


@given(instance=iec61131::literals::Daytime_strategy)
def test_iec61131::literals::daytime_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original

@given(instance=iec61131::literals::Fixed::Point::Literal_strategy)
@settings(max_examples=50)
def test_iec61131::literals::fixed::point::literal_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Fixed::Point::Literal)

@given(instance=Double::Byte::Character::Representation_strategy)
@settings(max_examples=50)
def test_double::byte::character::representation_instantiation(instance):
    assert isinstance(instance, Double::Byte::Character::Representation)

@given(instance=operators::Dot::Operator_strategy)
@settings(max_examples=50)
def test_operators::dot::operator_instantiation(instance):
    assert isinstance(instance, operators::Dot::Operator)

@given(instance=il::Il::Simple::Operator_strategy)
@settings(max_examples=50)
def test_il::il::simple::operator_instantiation(instance):
    assert isinstance(instance, il::Il::Simple::Operator)

@given(instance=operators::Unary::Operator_strategy)
@settings(max_examples=50)
def test_operators::unary::operator_instantiation(instance):
    assert isinstance(instance, operators::Unary::Operator)

@given(instance=iec61131::operators::Substraction::Symbol_strategy)
@settings(max_examples=50)
def test_iec61131::operators::substraction::symbol_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Substraction::Symbol)

@given(instance=iec61131::operators::Not::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::operators::not::operator_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Not::Operator)

@given(instance=il::Il::Expr::Operator_strategy)
@settings(max_examples=50)
def test_il::il::expr::operator_instantiation(instance):
    assert isinstance(instance, il::Il::Expr::Operator)

@given(instance=iec61131::operators::Modulo::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::operators::modulo::operator_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Modulo::Operator)

@given(instance=operators::Operator_strategy)
@settings(max_examples=50)
def test_operators::operator_instantiation(instance):
    assert isinstance(instance, operators::Operator)

@given(instance=iec61131::operators::Xor::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::operators::xor::operator_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Xor::Operator)

@given(instance=iec61131::operators::Or::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::operators::or::operator_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Or::Operator)

@given(instance=iec61131::operators::And::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::operators::and::operator_instantiation(instance):
    assert isinstance(instance, iec61131::operators::And::Operator)

@given(instance=EquUequ::Operator_strategy)
@settings(max_examples=50)
def test_equuequ::operator_instantiation(instance):
    assert isinstance(instance, EquUequ::Operator)

@given(instance=iec61131::operators::Unequal::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::operators::unequal::operator_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Unequal::Operator)

@given(instance=iec61131::operators::Equal::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::operators::equal::operator_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Equal::Operator)

@given(instance=Dot::Operator_strategy)
@settings(max_examples=50)
def test_dot::operator_instantiation(instance):
    assert isinstance(instance, Dot::Operator)

@given(instance=iec61131::operators::Divide::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::operators::divide::operator_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Divide::Operator)

@given(instance=iec61131::operators::Multiply::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::operators::multiply::operator_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Multiply::Operator)

@given(instance=iec61131::operators::Substraction::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::operators::substraction::operator_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Substraction::Operator)

@given(instance=iec61131::operators::Addition::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::operators::addition::operator_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Addition::Operator)

@given(instance=Operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, Operator)

@given(instance=iec61131::operators::Dot::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::operators::dot::operator_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Dot::Operator)

@given(instance=iec61131::operators::EquUequ::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::operators::equuequ::operator_instantiation(instance):
    assert isinstance(instance, iec61131::operators::EquUequ::Operator)

@given(instance=iec61131::operators::Unary::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::operators::unary::operator_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Unary::Operator)

@given(instance=iec61131::operators::Comparison::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::operators::comparison::operator_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Comparison::Operator)

@given(instance=iec61131::operators::Assignment::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::operators::assignment::operator_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Assignment::Operator)

@given(instance=iec61131::operators::Power::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::operators::power::operator_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Power::Operator)

@given(instance=iec61131::operators::Add::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::operators::add::operator_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Add::Operator)

@given(instance=iec61131::operators::Operator_strategy)
@settings(max_examples=50)
def test_iec61131::operators::operator_instantiation(instance):
    assert isinstance(instance, iec61131::operators::Operator)

@given(instance=iec61131::literals::Double::Byte::Character::Representation_strategy)
@settings(max_examples=50)
def test_iec61131::literals::double::byte::character::representation_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Double::Byte::Character::Representation)

@given(instance=iec61131::literals::Double::Byte::Character::Representation_strategy)
def test_iec61131::literals::double::byte::character::representation_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=iec61131::literals::Double::Byte::Character::Representation_strategy)
def test_iec61131::literals::double::byte::character::representation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Common::Character::Representation_strategy)
@settings(max_examples=50)
def test_common::character::representation_instantiation(instance):
    assert isinstance(instance, Common::Character::Representation)

@given(instance=iec61131::literals::Single::Byte::Character::Representation_strategy)
@settings(max_examples=50)
def test_iec61131::literals::single::byte::character::representation_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Single::Byte::Character::Representation)

@given(instance=iec61131::literals::Single::Byte::Character::Representation_strategy)
def test_iec61131::literals::single::byte::character::representation_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=iec61131::literals::Single::Byte::Character::Representation_strategy)
def test_iec61131::literals::single::byte::character::representation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=iec61131::literals::Common::Character::Representation_strategy)
@settings(max_examples=50)
def test_iec61131::literals::common::character::representation_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Common::Character::Representation)

@given(instance=iec61131::literals::Common::Character::Representation_strategy)
def test_iec61131::literals::common::character::representation_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=iec61131::literals::Common::Character::Representation_strategy)
def test_iec61131::literals::common::character::representation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=DT::Type::Name_strategy)
@settings(max_examples=50)
def test_dt::type::name_instantiation(instance):
    assert isinstance(instance, DT::Type::Name)

@given(instance=Date::Literal_strategy)
@settings(max_examples=50)
def test_date::literal_instantiation(instance):
    assert isinstance(instance, Date::Literal)

@given(instance=Date::Type::Name_strategy)
@settings(max_examples=50)
def test_date::type::name_instantiation(instance):
    assert isinstance(instance, Date::Type::Name)

@given(instance=iec61131::types::DT::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::dt::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::DT::Type::Name)

@given(instance=iec61131::types::TOD::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::tod::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::TOD::Type::Name)

@given(instance=Single::Byte::Character::Representation_strategy)
@settings(max_examples=50)
def test_single::byte::character::representation_instantiation(instance):
    assert isinstance(instance, Single::Byte::Character::Representation)

@given(instance=Character::String_strategy)
@settings(max_examples=50)
def test_character::string_instantiation(instance):
    assert isinstance(instance, Character::String)

@given(instance=iec61131::literals::Double::Byte::Character::String_strategy)
@settings(max_examples=50)
def test_iec61131::literals::double::byte::character::string_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Double::Byte::Character::String)

@given(instance=iec61131::literals::Single::Byte::Character::String_strategy)
@settings(max_examples=50)
def test_iec61131::literals::single::byte::character::string_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Single::Byte::Character::String)

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

@given(instance=Unsigned::Integer_strategy)
@settings(max_examples=50)
def test_unsigned::integer_instantiation(instance):
    assert isinstance(instance, Unsigned::Integer)

@given(instance=Fixed::Point::Literal_strategy)
@settings(max_examples=50)
def test_fixed::point::literal_instantiation(instance):
    assert isinstance(instance, Fixed::Point::Literal)

@given(instance=iec61131::literals::Fixed::Point_strategy)
@settings(max_examples=50)
def test_iec61131::literals::fixed::point_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Fixed::Point)

@given(instance=iec61131::literals::Fixed::Point_strategy)
def test_iec61131::literals::fixed::point_valuePre_type(instance):
    assert isinstance(instance.valuePre, str)


@given(instance=iec61131::literals::Fixed::Point_strategy)
def test_iec61131::literals::fixed::point_valuePre_setter(instance):
    original = instance.valuePre
    instance.valuePre = original
    assert instance.valuePre == original

@given(instance=iec61131::literals::Fixed::Point_strategy)
def test_iec61131::literals::fixed::point_valuePost_type(instance):
    assert isinstance(instance.valuePost, str)


@given(instance=iec61131::literals::Fixed::Point_strategy)
def test_iec61131::literals::fixed::point_valuePost_setter(instance):
    original = instance.valuePost
    instance.valuePost = original
    assert instance.valuePost == original

@given(instance=iec61131::literals::Interval_strategy)
@settings(max_examples=50)
def test_iec61131::literals::interval_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Interval)

@given(instance=literals::Fixed::Point::Literal_strategy)
@settings(max_examples=50)
def test_literals::fixed::point::literal_instantiation(instance):
    assert isinstance(instance, literals::Fixed::Point::Literal)

@given(instance=Integer_strategy)
@settings(max_examples=50)
def test_integer_instantiation(instance):
    assert isinstance(instance, Integer)

@given(instance=Numeric::Literal_strategy)
@settings(max_examples=50)
def test_numeric::literal_instantiation(instance):
    assert isinstance(instance, Numeric::Literal)

@given(instance=iec61131::literals::Integer::Literal_strategy)
@settings(max_examples=50)
def test_iec61131::literals::integer::literal_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Integer::Literal)

@given(instance=Bit::String::Type::Name_strategy)
@settings(max_examples=50)
def test_bit::string::type::name_instantiation(instance):
    assert isinstance(instance, Bit::String::Type::Name)

@given(instance=iec61131::types::Bool::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::bool::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::Bool::Type::Name)

@given(instance=BSInteger_strategy)
@settings(max_examples=50)
def test_bsinteger_instantiation(instance):
    assert isinstance(instance, BSInteger)

@given(instance=Constant_strategy)
@settings(max_examples=50)
def test_constant_instantiation(instance):
    assert isinstance(instance, Constant)

@given(instance=iec61131::literals::Bit::String::Literal_strategy)
@settings(max_examples=50)
def test_iec61131::literals::bit::string::literal_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Bit::String::Literal)

@given(instance=iec61131::literals::Character::String_strategy)
@settings(max_examples=50)
def test_iec61131::literals::character::string_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Character::String)

@given(instance=iec61131::literals::Time::Literal_strategy)
@settings(max_examples=50)
def test_iec61131::literals::time::literal_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Time::Literal)

@given(instance=iec61131::literals::Numeric::Literal_strategy)
@settings(max_examples=50)
def test_iec61131::literals::numeric::literal_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Numeric::Literal)

@given(instance=TOD::Type::Name_strategy)
@settings(max_examples=50)
def test_tod::type::name_instantiation(instance):
    assert isinstance(instance, TOD::Type::Name)

@given(instance=Daytime_strategy)
@settings(max_examples=50)
def test_daytime_instantiation(instance):
    assert isinstance(instance, Daytime)

@given(instance=Time::Literal_strategy)
@settings(max_examples=50)
def test_time::literal_instantiation(instance):
    assert isinstance(instance, Time::Literal)

@given(instance=iec61131::literals::Date::And::Time_strategy)
@settings(max_examples=50)
def test_iec61131::literals::date::and::time_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Date::And::Time)

@given(instance=iec61131::literals::Date_strategy)
@settings(max_examples=50)
def test_iec61131::literals::date_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Date)

@given(instance=iec61131::literals::Time::Of::Day_strategy)
@settings(max_examples=50)
def test_iec61131::literals::time::of::day_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Time::Of::Day)

@given(instance=Substraction::Operator_strategy)
@settings(max_examples=50)
def test_substraction::operator_instantiation(instance):
    assert isinstance(instance, Substraction::Operator)

@given(instance=Duration::Type::Name_strategy)
@settings(max_examples=50)
def test_duration::type::name_instantiation(instance):
    assert isinstance(instance, Duration::Type::Name)

@given(instance=Interval_strategy)
@settings(max_examples=50)
def test_interval_instantiation(instance):
    assert isinstance(instance, Interval)

@given(instance=iec61131::literals::Days_strategy)
@settings(max_examples=50)
def test_iec61131::literals::days_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Days)

@given(instance=iec61131::literals::Milliseconds_strategy)
@settings(max_examples=50)
def test_iec61131::literals::milliseconds_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Milliseconds)

@given(instance=iec61131::literals::Seconds_strategy)
@settings(max_examples=50)
def test_iec61131::literals::seconds_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Seconds)

@given(instance=iec61131::literals::Minutes_strategy)
@settings(max_examples=50)
def test_iec61131::literals::minutes_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Minutes)

@given(instance=iec61131::literals::Hours_strategy)
@settings(max_examples=50)
def test_iec61131::literals::hours_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Hours)

@given(instance=sfc::Action::Time_strategy)
@settings(max_examples=50)
def test_sfc::action::time_instantiation(instance):
    assert isinstance(instance, sfc::Action::Time)

@given(instance=literals::Time::Literal_strategy)
@settings(max_examples=50)
def test_literals::time::literal_instantiation(instance):
    assert isinstance(instance, literals::Time::Literal)

@given(instance=iec61131::literals::Duration_strategy)
@settings(max_examples=50)
def test_iec61131::literals::duration_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Duration)

@given(instance=literals::BSInteger_strategy)
@settings(max_examples=50)
def test_literals::bsinteger_instantiation(instance):
    assert isinstance(instance, literals::BSInteger)

@given(instance=interfaces::Range_strategy)
@settings(max_examples=50)
def test_interfaces::range_instantiation(instance):
    assert isinstance(instance, interfaces::Range)

@given(instance=st::Case::List::Element_strategy)
@settings(max_examples=50)
def test_st::case::list::element_instantiation(instance):
    assert isinstance(instance, st::Case::List::Element)

@given(instance=literals::Integer_strategy)
@settings(max_examples=50)
def test_literals::integer_instantiation(instance):
    assert isinstance(instance, literals::Integer)

@given(instance=iec61131::literals::Binary::Integer_strategy)
@settings(max_examples=50)
def test_iec61131::literals::binary::integer_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Binary::Integer)

@given(instance=iec61131::literals::Octal::Integer_strategy)
@settings(max_examples=50)
def test_iec61131::literals::octal::integer_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Octal::Integer)

@given(instance=iec61131::literals::Hex::Integer_strategy)
@settings(max_examples=50)
def test_iec61131::literals::hex::integer_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Hex::Integer)

@given(instance=iec61131::literals::Unsigned::Integer_strategy)
@settings(max_examples=50)
def test_iec61131::literals::unsigned::integer_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Unsigned::Integer)

@given(instance=iec61131::literals::Signed::Integer_strategy)
@settings(max_examples=50)
def test_iec61131::literals::signed::integer_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Signed::Integer)

@given(instance=iec61131::literals::Signed::Integer_strategy)
def test_iec61131::literals::signed::integer_negative_type(instance):
    assert isinstance(instance.negative, bool)


@given(instance=iec61131::literals::Signed::Integer_strategy)
def test_iec61131::literals::signed::integer_negative_setter(instance):
    original = instance.negative
    instance.negative = original
    assert instance.negative == original

@given(instance=il::Il::Operand_strategy)
@settings(max_examples=50)
def test_il::il::operand_instantiation(instance):
    assert isinstance(instance, il::Il::Operand)

@given(instance=configurations::Prog::Data::Source_strategy)
@settings(max_examples=50)
def test_configurations::prog::data::source_instantiation(instance):
    assert isinstance(instance, configurations::Prog::Data::Source)

@given(instance=iec61131::interfaces::Enumerated::Value_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::enumerated::value_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Enumerated::Value)

@given(instance=iec61131::interfaces::Enumerated::Value_strategy)
def test_iec61131::interfaces::enumerated::value_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iec61131::interfaces::Enumerated::Value_strategy)
def test_iec61131::interfaces::enumerated::value_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=configurations::Data::Source_strategy)
@settings(max_examples=50)
def test_configurations::data::source_instantiation(instance):
    assert isinstance(instance, configurations::Data::Source)

@given(instance=iec61131::configurations::Global::Var::Reference_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::global::var::reference_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Global::Var::Reference)

@given(instance=iec61131::variables::Direct::Variable_strategy)
@settings(max_examples=50)
def test_iec61131::variables::direct::variable_instantiation(instance):
    assert isinstance(instance, iec61131::variables::Direct::Variable)

@given(instance=iec61131::variables::Direct::Variable_strategy)
def test_iec61131::variables::direct::variable_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=iec61131::variables::Direct::Variable_strategy)
def test_iec61131::variables::direct::variable_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=iec61131::literals::Constant_strategy)
@settings(max_examples=50)
def test_iec61131::literals::constant_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Constant)

@given(instance=iec61131::literals::Boolean::Literal_strategy)
@settings(max_examples=50)
def test_iec61131::literals::boolean::literal_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Boolean::Literal)

@given(instance=iec61131::literals::Boolean::Literal_strategy)
def test_iec61131::literals::boolean::literal_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=iec61131::literals::Boolean::Literal_strategy)
def test_iec61131::literals::boolean::literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Fixed::Point_strategy)
@settings(max_examples=50)
def test_fixed::point_instantiation(instance):
    assert isinstance(instance, Fixed::Point)

@given(instance=Real::Type::Name_strategy)
@settings(max_examples=50)
def test_real::type::name_instantiation(instance):
    assert isinstance(instance, Real::Type::Name)

@given(instance=iec61131::literals::Real::Literal_strategy)
@settings(max_examples=50)
def test_iec61131::literals::real::literal_instantiation(instance):
    assert isinstance(instance, iec61131::literals::Real::Literal)

@given(instance=iec61131::literals::Real::Literal_strategy)
def test_iec61131::literals::real::literal_negative_type(instance):
    assert isinstance(instance.negative, bool)


@given(instance=iec61131::literals::Real::Literal_strategy)
def test_iec61131::literals::real::literal_negative_setter(instance):
    original = instance.negative
    instance.negative = original
    assert instance.negative == original

@given(instance=iec61131::literals::Real::Literal_strategy)
def test_iec61131::literals::real::literal_exponent_type(instance):
    assert isinstance(instance.exponent, str)


@given(instance=iec61131::literals::Real::Literal_strategy)
def test_iec61131::literals::real::literal_exponent_setter(instance):
    original = instance.exponent
    instance.exponent = original
    assert instance.exponent == original

@given(instance=Integer::Type::Name_strategy)
@settings(max_examples=50)
def test_integer::type::name_instantiation(instance):
    assert isinstance(instance, Integer::Type::Name)

@given(instance=iec61131::types::Signed::Integer::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::signed::integer::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::Signed::Integer::Type::Name)

@given(instance=iec61131::types::Unsigned::Integer::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::types::unsigned::integer::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::types::Unsigned::Integer::Type::Name)

@given(instance=iec61131::NamedElement_strategy)
@settings(max_examples=50)
def test_iec61131::namedelement_instantiation(instance):
    assert isinstance(instance, iec61131::NamedElement)

@given(instance=iec61131::NamedElement_strategy)
def test_iec61131::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iec61131::NamedElement_strategy)
def test_iec61131::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iec61131::Commentable_strategy)
@settings(max_examples=50)
def test_iec61131::commentable_instantiation(instance):
    assert isinstance(instance, iec61131::Commentable)

@given(instance=iec61131::Commentable_strategy)
def test_iec61131::commentable_comments_type(instance):
    assert isinstance(instance.comments, str)


@given(instance=iec61131::Commentable_strategy)
def test_iec61131::commentable_comments_setter(instance):
    original = instance.comments
    instance.comments = original
    assert instance.comments == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=iec61131::variables::Variable::Name_strategy)
@settings(max_examples=50)
def test_iec61131::variables::variable::name_instantiation(instance):
    assert isinstance(instance, iec61131::variables::Variable::Name)

@given(instance=iec61131::sfc::Step::Name_strategy)
@settings(max_examples=50)
def test_iec61131::sfc::step::name_instantiation(instance):
    assert isinstance(instance, iec61131::sfc::Step::Name)

@given(instance=Commentable_strategy)
@settings(max_examples=50)
def test_commentable_instantiation(instance):
    assert isinstance(instance, Commentable)

@given(instance=iec61131::st::Param::Assignment_strategy)
@settings(max_examples=50)
def test_iec61131::st::param::assignment_instantiation(instance):
    assert isinstance(instance, iec61131::st::Param::Assignment)

@given(instance=iec61131::st::Statement_strategy)
@settings(max_examples=50)
def test_iec61131::st::statement_instantiation(instance):
    assert isinstance(instance, iec61131::st::Statement)

@given(instance=iec61131::configurations::Program::Configuration_strategy)
@settings(max_examples=50)
def test_iec61131::configurations::program::configuration_instantiation(instance):
    assert isinstance(instance, iec61131::configurations::Program::Configuration)

@given(instance=iec61131::configurations::Program::Configuration_strategy)
def test_iec61131::configurations::program::configuration_retain_type(instance):
    assert isinstance(instance.retain, bool)


@given(instance=iec61131::configurations::Program::Configuration_strategy)
def test_iec61131::configurations::program::configuration_retain_setter(instance):
    original = instance.retain
    instance.retain = original
    assert instance.retain == original

@given(instance=iec61131::interfaces::Interface_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::interface_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Interface)

@given(instance=iec61131::st::Expression::Variable_strategy)
@settings(max_examples=50)
def test_iec61131::st::expression::variable_instantiation(instance):
    assert isinstance(instance, iec61131::st::Expression::Variable)

@given(instance=iec61131::interfaces::Global::Var::Name_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::global::var::name_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Global::Var::Name)

@given(instance=iec61131::variables::Variable_strategy)
@settings(max_examples=50)
def test_iec61131::variables::variable_instantiation(instance):
    assert isinstance(instance, iec61131::variables::Variable)

@given(instance=iec61131::st::Expression::Types_strategy)
@settings(max_examples=50)
def test_iec61131::st::expression::types_instantiation(instance):
    assert isinstance(instance, iec61131::st::Expression::Types)

@given(instance=iec61131::pous::Function::Block::Type::Name_strategy)
@settings(max_examples=50)
def test_iec61131::pous::function::block::type::name_instantiation(instance):
    assert isinstance(instance, iec61131::pous::Function::Block::Type::Name)

@given(instance=iec61131::interfaces::Global::Var::Decl_strategy)
@settings(max_examples=50)
def test_iec61131::interfaces::global::var::decl_instantiation(instance):
    assert isinstance(instance, iec61131::interfaces::Global::Var::Decl)

@given(instance=iec61131::Library::Element::Name_strategy)
@settings(max_examples=50)
def test_iec61131::library::element::name_instantiation(instance):
    assert isinstance(instance, iec61131::Library::Element::Name)

@given(instance=iec61131::Library::Element::Declaration_strategy)
@settings(max_examples=50)
def test_iec61131::library::element::declaration_instantiation(instance):
    assert isinstance(instance, iec61131::Library::Element::Declaration)

@given(instance=iec61131::IEC61131_strategy)
@settings(max_examples=50)
def test_iec61131::iec61131_instantiation(instance):
    assert isinstance(instance, iec61131::IEC61131)
