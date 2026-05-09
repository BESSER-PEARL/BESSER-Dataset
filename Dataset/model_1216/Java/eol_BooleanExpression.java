





import java.util.List;
import java.util.ArrayList;

public class eol_BooleanExpression extends PrimitiveExpression {

    private boolean val;





    private eol_VariableDeclarationExpression eol_variabledeclarationexpression;




    private eol_FeatureCallExpression eol_featurecallexpression;




    private eol_NameExpression eol_nameexpression;




    private eol_PropertyCallExpression eol_propertycallexpression;


    public eol_BooleanExpression(
        boolean val    ) {
        super(
        );
        this.val = val;
    }


    public boolean getVal() {
        return val;
    }

    public void setVal(boolean val) {
        this.val = val;
    }

    public eol_VariableDeclarationExpression getEol_variabledeclarationexpression() {
        return eol_variabledeclarationexpression;
    }

    public void setEol_variabledeclarationexpression(eol_VariableDeclarationExpression eol_variabledeclarationexpression) {
        this.eol_variabledeclarationexpression = eol_variabledeclarationexpression;
    }
    public eol_FeatureCallExpression getEol_featurecallexpression() {
        return eol_featurecallexpression;
    }

    public void setEol_featurecallexpression(eol_FeatureCallExpression eol_featurecallexpression) {
        this.eol_featurecallexpression = eol_featurecallexpression;
    }
    public eol_NameExpression getEol_nameexpression() {
        return eol_nameexpression;
    }

    public void setEol_nameexpression(eol_NameExpression eol_nameexpression) {
        this.eol_nameexpression = eol_nameexpression;
    }
    public eol_PropertyCallExpression getEol_propertycallexpression() {
        return eol_propertycallexpression;
    }

    public void setEol_propertycallexpression(eol_PropertyCallExpression eol_propertycallexpression) {
        this.eol_propertycallexpression = eol_propertycallexpression;
    }

}