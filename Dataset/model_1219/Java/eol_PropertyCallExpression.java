





import java.util.List;
import java.util.ArrayList;

public class eol_PropertyCallExpression extends FeatureCallExpression {






    private eol_NameExpression eol_nameexpression;




    private eol_BooleanExpression eol_booleanexpression;


    public eol_PropertyCallExpression(
    ) {
        super(
        );
    }



    public eol_NameExpression getEol_nameexpression() {
        return eol_nameexpression;
    }

    public void setEol_nameexpression(eol_NameExpression eol_nameexpression) {
        this.eol_nameexpression = eol_nameexpression;
    }
    public eol_BooleanExpression getEol_booleanexpression() {
        return eol_booleanexpression;
    }

    public void setEol_booleanexpression(eol_BooleanExpression eol_booleanexpression) {
        this.eol_booleanexpression = eol_booleanexpression;
    }

}