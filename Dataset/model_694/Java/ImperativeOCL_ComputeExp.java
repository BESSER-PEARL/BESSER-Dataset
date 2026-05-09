





import java.util.List;
import java.util.ArrayList;

public class ImperativeOCL_ComputeExp extends ImperativeExpression {






    private Variable variable;




    private OclExpression oclexpression;


    public ImperativeOCL_ComputeExp(
    ) {
        super(
        );
    }



    public Variable getVariable() {
        return variable;
    }

    public void setVariable(Variable variable) {
        this.variable = variable;
    }
    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}