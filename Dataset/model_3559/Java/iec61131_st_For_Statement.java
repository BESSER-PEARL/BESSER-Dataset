





import java.util.List;
import java.util.ArrayList;

public class iec61131_st_For_Statement extends Iteration_Statement {






    private Assignment_Symbol assignment_symbol;


    public iec61131_st_For_Statement(
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

}