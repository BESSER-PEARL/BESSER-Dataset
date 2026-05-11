





import java.util.List;
import java.util.ArrayList;

public class frontend_patterns_PAttribute extends PFeature {






    private Variable variable;




    private Expression expression;


    public frontend_patterns_PAttribute(
    ) {
        super(
        );
    }



    public Variable getVariable() {
        return variable;
    }

    public void setVariable(Variable variable) {
        this.variable = variable;
    }
    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}