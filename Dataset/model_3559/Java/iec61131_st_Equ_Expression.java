





import java.util.List;
import java.util.ArrayList;

public class iec61131_st_Equ_Expression extends Expression_Types {






    private Comparison_Operator comparison_operator;


    public iec61131_st_Equ_Expression(
    ) {
        super(
        );
    }



    public Comparison_Operator getComparison_operator() {
        return comparison_operator;
    }

    public void setComparison_operator(Comparison_Operator comparison_operator) {
        this.comparison_operator = comparison_operator;
    }

}