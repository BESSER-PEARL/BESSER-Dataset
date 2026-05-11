





import java.util.List;
import java.util.ArrayList;

public class b_Call extends Expr, Statement {






    private List<b_Variable> b_variables;




    private List<b_Arg> b_args;


    public b_Call(
    ) {
        super(
        );
        this.b_variables = new ArrayList<>();
        this.b_args = new ArrayList<>();
    }

    public b_Call(
        ArrayList<b_Variable> b_variables,        ArrayList<b_Arg> b_args    ) {
        this.b_variables = b_variables;
        this.b_args = b_args;
    }


    public List<b_Variable> getB_variables() {
        return b_variables;
    }

    public void addB_variable(B_variable b_variable) {
        this.b_variables.add(b_variable);
    }
    public List<b_Arg> getB_args() {
        return b_args;
    }

    public void addB_arg(B_arg b_arg) {
        this.b_args.add(b_arg);
    }

}