





import java.util.List;
import java.util.ArrayList;

public class expressions_UnaryExpression extends Expression {

    private String type;





    private expressions_Expression expressions_expression;


    public expressions_UnaryExpression(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public expressions_Expression getExpressions_expression() {
        return expressions_expression;
    }

    public void setExpressions_expression(expressions_Expression expressions_expression) {
        this.expressions_expression = expressions_expression;
    }

}