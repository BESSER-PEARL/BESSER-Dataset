





import java.util.List;
import java.util.ArrayList;

public class expression_FeatureCall extends Expression {

    private String name;





    private expression_Expression expression_expression;




    private expression_Identifier expression_identifier;


    public expression_FeatureCall(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public expression_Expression getExpression_expression() {
        return expression_expression;
    }

    public void setExpression_expression(expression_Expression expression_expression) {
        this.expression_expression = expression_expression;
    }
    public expression_Identifier getExpression_identifier() {
        return expression_identifier;
    }

    public void setExpression_identifier(expression_Identifier expression_identifier) {
        this.expression_identifier = expression_identifier;
    }

}