





import java.util.List;
import java.util.ArrayList;

public class webapp_Check  {

    private String expr;





    private webapp_Constraint webapp_constraint;


    public webapp_Check(
        String expr    ) {
        this.expr = expr;
    }


    public String getExpr() {
        return expr;
    }

    public void setExpr(String expr) {
        this.expr = expr;
    }

    public webapp_Constraint getWebapp_constraint() {
        return webapp_constraint;
    }

    public void setWebapp_constraint(webapp_Constraint webapp_constraint) {
        this.webapp_constraint = webapp_constraint;
    }

}