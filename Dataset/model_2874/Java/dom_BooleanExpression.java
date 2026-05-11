





import java.util.List;
import java.util.ArrayList;

public class dom_BooleanExpression extends PrimitiveExpression {

    private boolean val;





    private dom_FeatureCallExpression dom_featurecallexpression;




    private dom_PropertyCallExpression dom_propertycallexpression;




    private dom_VariableDeclarationExpression dom_variabledeclarationexpression;


    public dom_BooleanExpression(
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

    public dom_FeatureCallExpression getDom_featurecallexpression() {
        return dom_featurecallexpression;
    }

    public void setDom_featurecallexpression(dom_FeatureCallExpression dom_featurecallexpression) {
        this.dom_featurecallexpression = dom_featurecallexpression;
    }
    public dom_PropertyCallExpression getDom_propertycallexpression() {
        return dom_propertycallexpression;
    }

    public void setDom_propertycallexpression(dom_PropertyCallExpression dom_propertycallexpression) {
        this.dom_propertycallexpression = dom_propertycallexpression;
    }
    public dom_VariableDeclarationExpression getDom_variabledeclarationexpression() {
        return dom_variabledeclarationexpression;
    }

    public void setDom_variabledeclarationexpression(dom_VariableDeclarationExpression dom_variabledeclarationexpression) {
        this.dom_variabledeclarationexpression = dom_variabledeclarationexpression;
    }

}