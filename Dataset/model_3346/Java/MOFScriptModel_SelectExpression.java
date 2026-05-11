





import java.util.List;
import java.util.ArrayList;

public class MOFScriptModel_SelectExpression extends ValueExpression {

    private String type;
    private String variable;





    private MOFScriptModel_Expression mofscriptmodel_expression;


    public MOFScriptModel_SelectExpression(
        String type,        String variable    ) {
        super(
        );
        this.type = type;
        this.variable = variable;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getVariable() {
        return variable;
    }

    public void setVariable(String variable) {
        this.variable = variable;
    }

    public MOFScriptModel_Expression getMofscriptmodel_expression() {
        return mofscriptmodel_expression;
    }

    public void setMofscriptmodel_expression(MOFScriptModel_Expression mofscriptmodel_expression) {
        this.mofscriptmodel_expression = mofscriptmodel_expression;
    }

}