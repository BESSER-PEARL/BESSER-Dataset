





import java.util.List;
import java.util.ArrayList;

public class iec61131_st_Param_Type1 extends Param_Assignment {






    private Assignment_Symbol assignment_symbol;




    private Expression_Types expression_types;




    private Variable_Name variable_name;


    public iec61131_st_Param_Type1(
    ) {
        super(
        );
    }



    public Assignment_Symbol getAssignment_symbol() {
        return assignment_symbol;
    }

    public void setAssignment_symbol(Assignment_Symbol assignment_symbol) {
        this.assignment_symbol = assignment_symbol;
    }
    public Expression_Types getExpression_types() {
        return expression_types;
    }

    public void setExpression_types(Expression_Types expression_types) {
        this.expression_types = expression_types;
    }
    public Variable_Name getVariable_name() {
        return variable_name;
    }

    public void setVariable_name(Variable_Name variable_name) {
        this.variable_name = variable_name;
    }

}