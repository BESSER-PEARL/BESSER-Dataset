





import java.util.List;
import java.util.ArrayList;

public class b_TypeConstraint extends LogicalExpr {






    private b_Type b_type;




    private b_Variable b_variable;


    public b_TypeConstraint(
    ) {
        super(
        );
    }



    public b_Type getB_type() {
        return b_type;
    }

    public void setB_type(b_Type b_type) {
        this.b_type = b_type;
    }
    public b_Variable getB_variable() {
        return b_variable;
    }

    public void setB_variable(b_Variable b_variable) {
        this.b_variable = b_variable;
    }

}