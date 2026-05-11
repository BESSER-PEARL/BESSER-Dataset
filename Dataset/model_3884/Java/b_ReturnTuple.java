





import java.util.List;
import java.util.ArrayList;

public class b_ReturnTuple extends Return {






    private b_LogicalExpr b_logicalexpr;




    private List<b_Variable> b_variables;


    public b_ReturnTuple(
    ) {
        super(
        );
        this.b_variables = new ArrayList<>();
    }

    public b_ReturnTuple(
        ArrayList<b_Variable> b_variables    ) {
        this.b_variables = b_variables;
    }


    public b_LogicalExpr getB_logicalexpr() {
        return b_logicalexpr;
    }

    public void setB_logicalexpr(b_LogicalExpr b_logicalexpr) {
        this.b_logicalexpr = b_logicalexpr;
    }
    public List<b_Variable> getB_variables() {
        return b_variables;
    }

    public void addB_variable(B_variable b_variable) {
        this.b_variables.add(b_variable);
    }

}