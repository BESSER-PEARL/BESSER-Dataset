





import java.util.List;
import java.util.ArrayList;

public class eol_expression_FeatureCallExpression extends Expression {

    private boolean arrow;





    private eol_expression_Expression eol_expression_expression;


    public eol_expression_FeatureCallExpression(
        boolean arrow    ) {
        super(
        );
        this.arrow = arrow;
    }


    public boolean getArrow() {
        return arrow;
    }

    public void setArrow(boolean arrow) {
        this.arrow = arrow;
    }

    public eol_expression_Expression getEol_expression_expression() {
        return eol_expression_expression;
    }

    public void setEol_expression_expression(eol_expression_Expression eol_expression_expression) {
        this.eol_expression_expression = eol_expression_expression;
    }

}