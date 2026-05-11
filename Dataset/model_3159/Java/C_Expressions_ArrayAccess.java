





import java.util.List;
import java.util.ArrayList;

public class C_Expressions_ArrayAccess extends Access {






    private List<Expressions_Expression> expressions_expressions;




    private Expressions_Expression expressions_expression;


    public C_Expressions_ArrayAccess(
    ) {
        super(
        );
        this.expressions_expressions = new ArrayList<>();
    }

    public C_Expressions_ArrayAccess(
        ArrayList<Expressions_Expression> expressions_expressions    ) {
        this.expressions_expressions = expressions_expressions;
    }


    public List<Expressions_Expression> getExpressions_expressions() {
        return expressions_expressions;
    }

    public void addExpressions_expression(Expressions_expression expressions_expression) {
        this.expressions_expressions.add(expressions_expression);
    }
    public Expressions_Expression getExpressions_expression() {
        return expressions_expression;
    }

    public void setExpressions_expression(Expressions_Expression expressions_expression) {
        this.expressions_expression = expressions_expression;
    }

}