





import java.util.List;
import java.util.ArrayList;

public class ImperativeOCL_UnpackExp extends ImperativeExpression {






    private OclExpression oclexpression;




    private List<Variable> variables;


    public ImperativeOCL_UnpackExp(
    ) {
        super(
        );
        this.variables = new ArrayList<>();
    }

    public ImperativeOCL_UnpackExp(
        ArrayList<Variable> variables    ) {
        this.variables = variables;
    }


    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }
    public List<Variable> getVariables() {
        return variables;
    }

    public void addVariable(Variable variable) {
        this.variables.add(variable);
    }

}