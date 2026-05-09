





import java.util.List;
import java.util.ArrayList;

public class statements_SynchronizedBlock extends StatementListContainer, Statement {






    private Expression expression;


    public statements_SynchronizedBlock(
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