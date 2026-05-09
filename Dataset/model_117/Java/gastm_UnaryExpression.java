





import java.util.List;
import java.util.ArrayList;

public class gastm_UnaryExpression extends Expression {






    private gastm_UnaryOperator gastm_unaryoperator;




    private gastm_Expression gastm_expression;


    public gastm_UnaryExpression(
    ) {
        super(
        );
    }



    public gastm_UnaryOperator getGastm_unaryoperator() {
        return gastm_unaryoperator;
    }

    public void setGastm_unaryoperator(gastm_UnaryOperator gastm_unaryoperator) {
        this.gastm_unaryoperator = gastm_unaryoperator;
    }
    public gastm_Expression getGastm_expression() {
        return gastm_expression;
    }

    public void setGastm_expression(gastm_Expression gastm_expression) {
        this.gastm_expression = gastm_expression;
    }

}