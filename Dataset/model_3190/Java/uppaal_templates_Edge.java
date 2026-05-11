





import java.util.List;
import java.util.ArrayList;

public class uppaal_templates_Edge extends visuals_ColoredElement, core_CommentableElement, visuals_LinearElement {






    private List<Expression> expressions;




    private Location location;




    private Expression expression;




    private Location location;


    public uppaal_templates_Edge(
    ) {
        super(
        );
        this.expressions = new ArrayList<>();
    }

    public uppaal_templates_Edge(
        ArrayList<Expression> expressions    ) {
        this.expressions = expressions;
    }


    public List<Expression> getExpressions() {
        return expressions;
    }

    public void addExpression(Expression expression) {
        this.expressions.add(expression);
    }
    public Location getLocation() {
        return location;
    }

    public void setLocation(Location location) {
        this.location = location;
    }
    public Expression getExpression() {
        return expression;
    }

    public void setExpression(Expression expression) {
        this.expression = expression;
    }
    public Location getLocation() {
        return location;
    }

    public void setLocation(Location location) {
        this.location = location;
    }

}