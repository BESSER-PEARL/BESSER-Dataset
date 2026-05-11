





import java.util.List;
import java.util.ArrayList;

public class expressionDSL_VariableAssignment extends Statement {

    private String op;





    private expressionDSL_VariableDef expressiondsl_variabledef;


    public expressionDSL_VariableAssignment(
        String op    ) {
        super(
        );
        this.op = op;
    }


    public String getOp() {
        return op;
    }

    public void setOp(String op) {
        this.op = op;
    }

    public expressionDSL_VariableDef getExpressiondsl_variabledef() {
        return expressiondsl_variabledef;
    }

    public void setExpressiondsl_variabledef(expressionDSL_VariableDef expressiondsl_variabledef) {
        this.expressiondsl_variabledef = expressiondsl_variabledef;
    }

}