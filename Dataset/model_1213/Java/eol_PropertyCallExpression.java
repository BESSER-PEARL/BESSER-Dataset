





import java.util.List;
import java.util.ArrayList;

public class eol_PropertyCallExpression extends FeatureCallExpression {

    private boolean extended;





    private eol_NameExpression eol_nameexpression;


    public eol_PropertyCallExpression(
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

    public eol_NameExpression getEol_nameexpression() {
        return eol_nameexpression;
    }

    public void setEol_nameexpression(eol_NameExpression eol_nameexpression) {
        this.eol_nameexpression = eol_nameexpression;
    }

}