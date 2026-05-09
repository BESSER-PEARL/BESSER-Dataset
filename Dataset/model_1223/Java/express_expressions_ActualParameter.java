





import java.util.List;
import java.util.ArrayList;

public class express_expressions_ActualParameter  {

    private String position;





    private VARExpression varexpression;




    private Expression expression;


    public express_expressions_ActualParameter(
        String position    ) {
        this.position = position;
    }


    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }

    public VARExpression getVarexpression() {
        return varexpression;
    }

    public void setVarexpression(VARExpression varexpression) {
        this.varexpression = varexpression;
    }
    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}