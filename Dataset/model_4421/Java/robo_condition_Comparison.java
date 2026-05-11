





import java.util.List;
import java.util.ArrayList;

public class robo_condition_Comparison extends Condition {

    private String operator;





    private Expr expr;




    private Expr expr;


    public robo_condition_Comparison(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public Expr getExpr() {
        return expr;
    }

    public void setExpr(Expr expr) {
        this.expr = expr;
    }
    public Expr getExpr() {
        return expr;
    }

    public void setExpr(Expr expr) {
        this.expr = expr;
    }

}