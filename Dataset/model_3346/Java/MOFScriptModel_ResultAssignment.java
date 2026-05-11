





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_ResultAssignment extends MOFScriptStatement {

    private String operator;
    private String resultPart;





    private MOFScriptModel_Expression mofscriptmodel_expression;


    public MOFScriptModel_ResultAssignment(
        String operator,        String resultPart    ) {
        super(
        );
        this.operator = operator;
        this.resultPart = resultPart;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }
    public String getResultpart() {
        return resultPart;
    }

    public void setResultpart(String resultPart) {
        this.resultPart = resultPart;
    }

    public MOFScriptModel_Expression getMofscriptmodel_expression() {
        return mofscriptmodel_expression;
    }

    public void setMofscriptmodel_expression(MOFScriptModel_Expression mofscriptmodel_expression) {
        this.mofscriptmodel_expression = mofscriptmodel_expression;
    }

}