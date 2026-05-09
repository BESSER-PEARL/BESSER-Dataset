





import java.util.List;
import java.util.ArrayList;

public class statements_ForEachLoop extends StatementContainer, Statement {






    private Expression expression;


    public statements_ForEachLoop(
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