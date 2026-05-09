





import java.util.List;
import java.util.ArrayList;

public class eol_FeatureCallExpression extends Expression {

    private boolean isArrow;





    private eol_Expression eol_expression;


    public eol_FeatureCallExpression(
        boolean isArrow    ) {
        super(
        );
        this.isArrow = isArrow;
    }


    public boolean getIsarrow() {
        return isArrow;
    }

    public void setIsarrow(boolean isArrow) {
        this.isArrow = isArrow;
    }

    public eol_Expression getEol_expression() {
        return eol_expression;
    }

    public void setEol_expression(eol_Expression eol_expression) {
        this.eol_expression = eol_expression;
    }

}