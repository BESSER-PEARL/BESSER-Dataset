





import java.util.List;
import java.util.ArrayList;

public class ImperativeOCL_ComputeExp extends ImperativeExpression {






    private OclExpression oclexpression;




    private Variable variable;


    public ImperativeOCL_ComputeExp(
    ) {
        super(
        );
    }



    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }
    public Variable getVariable() {
        return variable;
    }

    public void setVariable(Variable variable) {
        this.variable = variable;
    }

}