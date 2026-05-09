





import java.util.List;
import java.util.ArrayList;

public class Janus_imperativeocl_UnpackExp extends ImperativeExpression {






    private List<Variable> variables;


    public Janus_imperativeocl_UnpackExp(
    ) {
        super(
        );
        this.variables = new ArrayList<>();
    }

    public Janus_imperativeocl_UnpackExp(
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