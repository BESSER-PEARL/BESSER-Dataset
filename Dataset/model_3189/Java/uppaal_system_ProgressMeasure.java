





import java.util.List;
import java.util.ArrayList;

public class uppaal_system_ProgressMeasure  {






    private List<Expression> expressions;


    public uppaal_system_ProgressMeasure(
    ) {
        this.expressions = new ArrayList<>();
    }

    public uppaal_system_ProgressMeasure(
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