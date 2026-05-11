





import java.util.List;
import java.util.ArrayList;

public class xs_Assign extends Expression {






    private xs_Var xs_var;




    private xs_Expression xs_expression;


    public xs_Assign(
    ) {
        super(
        );
    }



    public xs_Var getXs_var() {
        return xs_var;
    }

    public void setXs_var(xs_Var xs_var) {
        this.xs_var = xs_var;
    }
    public xs_Expression getXs_expression() {
        return xs_expression;
    }

    public void setXs_expression(xs_Expression xs_expression) {
        this.xs_expression = xs_expression;
    }

}