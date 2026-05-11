





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_PointCutExpression  {

    private String operator;
    private String expressionString;
    private String combinationOperator;





    private MOFScriptModel_PointCutExpression mofscriptmodel_pointcutexpression;


    public MOFScriptModel_PointCutExpression(
        String operator,        String expressionString,        String combinationOperator    ) {
        this.operator = operator;
        this.expressionString = expressionString;
        this.combinationOperator = combinationOperator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }
    public String getExpressionstring() {
        return expressionString;
    }

    public void setExpressionstring(String expressionString) {
        this.expressionString = expressionString;
    }
    public String getCombinationoperator() {
        return combinationOperator;
    }

    public void setCombinationoperator(String combinationOperator) {
        this.combinationOperator = combinationOperator;
    }

    public MOFScriptModel_PointCutExpression getMofscriptmodel_pointcutexpression() {
        return mofscriptmodel_pointcutexpression;
    }

    public void setMofscriptmodel_pointcutexpression(MOFScriptModel_PointCutExpression mofscriptmodel_pointcutexpression) {
        this.mofscriptmodel_pointcutexpression = mofscriptmodel_pointcutexpression;
    }

}