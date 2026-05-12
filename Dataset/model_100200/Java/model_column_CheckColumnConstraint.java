





import java.util.List;
import java.util.ArrayList;

public class model_column_CheckColumnConstraint extends ColumnConstraint {






    private Expression expression;


    public model_column_CheckColumnConstraint(
    ) {
        super(
        );
    }



    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }

}