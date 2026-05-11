





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_ComparisonExpression extends Expression {

    private String operator;





    private MOFScriptModel_ValueExpression mofscriptmodel_valueexpression;




    private MOFScriptModel_ValueExpression mofscriptmodel_valueexpression;


    public MOFScriptModel_ComparisonExpression(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public MOFScriptModel_ValueExpression getMofscriptmodel_valueexpression() {
        return mofscriptmodel_valueexpression;
    }

    public void setMofscriptmodel_valueexpression(MOFScriptModel_ValueExpression mofscriptmodel_valueexpression) {
        this.mofscriptmodel_valueexpression = mofscriptmodel_valueexpression;
    }
    public MOFScriptModel_ValueExpression getMofscriptmodel_valueexpression() {
        return mofscriptmodel_valueexpression;
    }

    public void setMofscriptmodel_valueexpression(MOFScriptModel_ValueExpression mofscriptmodel_valueexpression) {
        this.mofscriptmodel_valueexpression = mofscriptmodel_valueexpression;
    }

}