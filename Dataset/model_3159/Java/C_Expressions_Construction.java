





import java.util.List;
import java.util.ArrayList;

public class C_Expressions_Construction extends Expression {






    private List<Expressions_Expression> expressions_expressions;


    public C_Expressions_Construction(
    ) {
        super(
        );
        this.expressions_expressions = new ArrayList<>();
    }

    public C_Expressions_Construction(
        ArrayList<Expressions_Expression> expressions_expressions    ) {
        this.expressions_expressions = expressions_expressions;
    }


    public List<Expressions_Expression> getExpressions_expressions() {
        return expressions_expressions;
    }

    public void addExpressions_expression(Expressions_expression expressions_expression) {
        this.expressions_expressions.add(expressions_expression);
    }

}