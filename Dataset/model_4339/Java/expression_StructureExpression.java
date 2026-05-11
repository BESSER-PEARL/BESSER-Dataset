





import java.util.List;
import java.util.ArrayList;

public class expression_StructureExpression extends Expression {






    private List<expression_Expression> expression_expressions;




    private expression_KeyValuePair expression_keyvaluepair;


    public expression_StructureExpression(
    ) {
        super(
        );
        this.expression_expressions = new ArrayList<>();
    }

    public expression_StructureExpression(
        ArrayList<expression_Expression> expression_expressions    ) {
        this.expression_expressions = expression_expressions;
    }


    public List<expression_Expression> getExpression_expressions() {
        return expression_expressions;
    }

    public void addExpression_expression(Expression_expression expression_expression) {
        this.expression_expressions.add(expression_expression);
    }
    public expression_KeyValuePair getExpression_keyvaluepair() {
        return expression_keyvaluepair;
    }

    public void setExpression_keyvaluepair(expression_KeyValuePair expression_keyvaluepair) {
        this.expression_keyvaluepair = expression_keyvaluepair;
    }

}