





import java.util.List;
import java.util.ArrayList;

public class ImperativeOCL_VariableInitExp extends ImperativeExpression {

    private String withResult;





    private Variable variable;


    public ImperativeOCL_VariableInitExp(
        String withResult    ) {
        super(
        );
        this.withResult = withResult;
    }


    public String getWithresult() {
        return withResult;
    }

    public void setWithresult(String withResult) {
        this.withResult = withResult;
    }

    public Variable getVariable() {
        return variable;
    }

    public void setVariable(Variable variable) {
        this.variable = variable;
    }

}