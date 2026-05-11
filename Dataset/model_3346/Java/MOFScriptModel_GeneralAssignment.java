





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_GeneralAssignment extends MOFScriptStatement {

    private String name;
    private String operator;





    private MOFScriptModel_Expression mofscriptmodel_expression;


    public MOFScriptModel_GeneralAssignment(
        String name,        String operator    ) {
        super(
        );
        this.name = name;
        this.operator = operator;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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

}