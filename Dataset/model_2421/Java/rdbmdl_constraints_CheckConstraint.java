





import java.util.List;
import java.util.ArrayList;

public class rdbmdl_constraints_CheckConstraint extends Constraint {

    private String expression;



    public rdbmdl_constraints_CheckConstraint(
        String expression    ) {
        super(
        );
        this.expression = expression;
    }


    public String getExpression() {
        return expression;
    }

    public void setExpression(String expression) {
        this.expression = expression;
    }


}