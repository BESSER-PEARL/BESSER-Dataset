





import java.util.List;
import java.util.ArrayList;

public class essentialocl_LoopExp extends CallExp, OclExpression {






    private List<Variable> variables;


    public essentialocl_LoopExp(
    ) {
        super(
        );
        this.variables = new ArrayList<>();
    }

    public essentialocl_LoopExp(
        ArrayList<Variable> variables    ) {
        this.variables = variables;
    }


    public List<Variable> getVariables() {
        return variables;
    }

    public void addVariable(Variable variable) {
        this.variables.add(variable);
    }

}