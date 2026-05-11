





import java.util.List;
import java.util.ArrayList;

public class iec61131_sfc_Transition_Cond3 extends Transition_Condition {






    private Expression_Types expression_types;




    private Assignment_Symbol assignment_symbol;


    public iec61131_sfc_Transition_Cond3(
    ) {
        super(
        );
    }



    public Expression_Types getExpression_types() {
        return expression_types;
    }

    public void setExpression_types(Expression_Types expression_types) {
        this.expression_types = expression_types;
    }
    public Assignment_Symbol getAssignment_symbol() {
        return assignment_symbol;
    }

    public void setAssignment_symbol(Assignment_Symbol assignment_symbol) {
        this.assignment_symbol = assignment_symbol;
    }

}