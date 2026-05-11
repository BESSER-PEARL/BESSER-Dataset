





import java.util.List;
import java.util.ArrayList;

public class eol_expression_PropertyCallExpression extends FeatureCallExpression {

    private boolean extended;





    private eol_expression_NameExpression eol_expression_nameexpression;


    public eol_expression_PropertyCallExpression(
        boolean extended    ) {
        super(
        );
        this.extended = extended;
    }


    public boolean getExtended() {
        return extended;
    }

    public void setExtended(boolean extended) {
        this.extended = extended;
    }

    public eol_expression_NameExpression getEol_expression_nameexpression() {
        return eol_expression_nameexpression;
    }

    public void setEol_expression_nameexpression(eol_expression_NameExpression eol_expression_nameexpression) {
        this.eol_expression_nameexpression = eol_expression_nameexpression;
    }

}