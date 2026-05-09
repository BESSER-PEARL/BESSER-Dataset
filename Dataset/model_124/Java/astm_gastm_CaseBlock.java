





import java.util.List;
import java.util.ArrayList;

public class astm_gastm_CaseBlock extends SwitchCase {






    private List<Expression> expressions;


    public astm_gastm_CaseBlock(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
    }

    public astm_gastm_CaseBlock(
        ArrayList<Expression> expressions    ) {
        this.expressions = expressions;
    }


    public List<Expression> getExpressions() {
        return expressions;
    }

    public void addExpression(Expression expression) {
        this.expressions.add(expression);
    }

}