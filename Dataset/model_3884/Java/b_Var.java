





import java.util.List;
import java.util.ArrayList;

public class b_Var extends Expr, Body, FinalExpr {






    private List<b_Variable> b_variables;




    private b_Seq b_seq;


    public b_Var(
    ) {
        super(
        );
        this.b_variables = new ArrayList<>();
    }

    public b_Var(
        ArrayList<b_Variable> b_variables    ) {
        this.b_variables = b_variables;
    }


    public List<b_Variable> getB_variables() {
        return b_variables;
    }

    public void addB_variable(B_variable b_variable) {
        this.b_variables.add(b_variable);
    }
    public b_Seq getB_seq() {
        return b_seq;
    }

    public void setB_seq(b_Seq b_seq) {
        this.b_seq = b_seq;
    }

}