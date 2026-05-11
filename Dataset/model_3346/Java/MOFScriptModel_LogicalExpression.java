





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_LogicalExpression extends Expression {

    private String operator;





    private MOFScriptModel_Expression mofscriptmodel_expression;




    private MOFScriptModel_Expression mofscriptmodel_expression;


    public MOFScriptModel_LogicalExpression(
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

    public MOFScriptModel_Expression getMofscriptmodel_expression() {
        return mofscriptmodel_expression;
    }

    public void setMofscriptmodel_expression(MOFScriptModel_Expression mofscriptmodel_expression) {
        this.mofscriptmodel_expression = mofscriptmodel_expression;
    }
    public MOFScriptModel_Expression getMofscriptmodel_expression() {
        return mofscriptmodel_expression;
    }

    public void setMofscriptmodel_expression(MOFScriptModel_Expression mofscriptmodel_expression) {
        this.mofscriptmodel_expression = mofscriptmodel_expression;
    }

}