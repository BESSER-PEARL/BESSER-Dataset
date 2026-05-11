





import java.util.List;
import java.util.ArrayList;

public class b_Assign extends Expr, Statement {






    private b_Variable b_variable;


    public b_Assign(
    ) {
        super(
        );
    }



    public b_Variable getB_variable() {
        return b_variable;
    }

    public void setB_variable(b_Variable b_variable) {
        this.b_variable = b_variable;
    }

}