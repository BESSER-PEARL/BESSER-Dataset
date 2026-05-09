





import java.util.List;
import java.util.ArrayList;

public class essentialocl_expressions_LoopExp extends CallExp {






    private List<Variable> variables;




    private OclExpression oclexpression;


    public essentialocl_expressions_LoopExp(
    ) {
        super(
        );
        this.variables = new ArrayList<>();
    }

    public essentialocl_expressions_LoopExp(
        ArrayList<Variable> variables    ) {
        this.variables = variables;
    }


    public List<Variable> getVariables() {
        return variables;
    }

    public void addVariable(Variable variable) {
        this.variables.add(variable);
    }
    public OclExpression getOclexpression() {
        return oclexpression;
    }

    public void setOclexpression(OclExpression oclexpression) {
        this.oclexpression = oclexpression;
    }

}