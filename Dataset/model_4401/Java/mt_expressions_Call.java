





import java.util.List;
import java.util.ArrayList;

public class mt_expressions_Call extends ASTNode {

    private String name;
    private String prefix;





    private Expression expression;




    private List<Expression> expressions;


    public mt_expressions_Call(
        String name,        String prefix    ) {
        super(
        );
        this.name = name;
        this.prefix = prefix;
        this.expressions = new ArrayList<>();
    }

    public mt_expressions_Call(
        String name,        String prefix        ArrayList<Expression> expressions    ) {
        this.name = name;
        this.prefix = prefix;
        this.expressions = expressions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPrefix() {
        return prefix;
    }

    public void setPrefix(String prefix) {
        this.prefix = prefix;
    }

    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }
    public List<Expression> getExpressions() {
        return expressions;
    }

    public void addExpression(Expression expression) {
        this.expressions.add(expression);
    }

}