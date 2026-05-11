





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_SimpleExpression extends ValueExpression {






    private MOFScriptModel_SelectExpression mofscriptmodel_selectexpression;




    private MOFScriptModel_SimpleExpression mofscriptmodel_simpleexpression;




    private MOFScriptModel_IteratorStatement mofscriptmodel_iteratorstatement;


    public MOFScriptModel_SimpleExpression(
    ) {
        super(
        );
    }



    public MOFScriptModel_SelectExpression getMofscriptmodel_selectexpression() {
        return mofscriptmodel_selectexpression;
    }

    public void setMofscriptmodel_selectexpression(MOFScriptModel_SelectExpression mofscriptmodel_selectexpression) {
        this.mofscriptmodel_selectexpression = mofscriptmodel_selectexpression;
    }
    public MOFScriptModel_SimpleExpression getMofscriptmodel_simpleexpression() {
        return mofscriptmodel_simpleexpression;
    }

    public void setMofscriptmodel_simpleexpression(MOFScriptModel_SimpleExpression mofscriptmodel_simpleexpression) {
        this.mofscriptmodel_simpleexpression = mofscriptmodel_simpleexpression;
    }
    public MOFScriptModel_IteratorStatement getMofscriptmodel_iteratorstatement() {
        return mofscriptmodel_iteratorstatement;
    }

    public void setMofscriptmodel_iteratorstatement(MOFScriptModel_IteratorStatement mofscriptmodel_iteratorstatement) {
        this.mofscriptmodel_iteratorstatement = mofscriptmodel_iteratorstatement;
    }

}