





import java.util.List;
import java.util.ArrayList;

public class eol_FeatureCallExpression extends Expression {

    private boolean arrow;





    private eol_Expression eol_expression;


    public eol_FeatureCallExpression(
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

    public eol_Expression getEol_expression() {
        return eol_expression;
    }

    public void setEol_expression(eol_Expression eol_expression) {
        this.eol_expression = eol_expression;
    }

}