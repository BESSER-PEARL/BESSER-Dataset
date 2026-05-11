





import java.util.List;
import java.util.ArrayList;

public class gaml_Function extends Expression {






    private gaml_Expression gaml_expression;




    private gaml_ExpressionList gaml_expressionlist;


    public gaml_Function(
    ) {
        super(
        );
    }



    public gaml_Expression getGaml_expression() {
        return gaml_expression;
    }

    public void setGaml_expression(gaml_Expression gaml_expression) {
        this.gaml_expression = gaml_expression;
    }
    public gaml_ExpressionList getGaml_expressionlist() {
        return gaml_expressionlist;
    }

    public void setGaml_expressionlist(gaml_ExpressionList gaml_expressionlist) {
        this.gaml_expressionlist = gaml_expressionlist;
    }

}