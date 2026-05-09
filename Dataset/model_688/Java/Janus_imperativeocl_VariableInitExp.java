





import java.util.List;
import java.util.ArrayList;

public class Janus_imperativeocl_VariableInitExp extends ImperativeExpression {

    private boolean withResult;





    private Variable variable;


    public Janus_imperativeocl_VariableInitExp(
        boolean withResult    ) {
        super(
        );
        this.withResult = withResult;
    }


    public boolean getWithresult() {
        return withResult;
    }

    public void setWithresult(boolean withResult) {
        this.withResult = withResult;
    }

    public Variable getVariable() {
        return variable;
    }

    public void setVariable(Variable variable) {
        this.variable = variable;
    }

}