





import java.util.List;
import java.util.ArrayList;

public class iec61131_sfc_Transition extends Sfc_Elements {






    private Transition_Condition transition_condition;




    private Assignment_Symbol assignment_symbol;




    private Unsigned_Integer unsigned_integer;


    public iec61131_sfc_Transition(
    ) {
        super(
        );
    }



    public Transition_Condition getTransition_condition() {
        return transition_condition;
    }

    public void setTransition_condition(Transition_Condition transition_condition) {
        this.transition_condition = transition_condition;
    }
    public Assignment_Symbol getAssignment_symbol() {
        return assignment_symbol;
    }

    public void setAssignment_symbol(Assignment_Symbol assignment_symbol) {
        this.assignment_symbol = assignment_symbol;
    }
    public Unsigned_Integer getUnsigned_integer() {
        return unsigned_integer;
    }

    public void setUnsigned_integer(Unsigned_Integer unsigned_integer) {
        this.unsigned_integer = unsigned_integer;
    }

}