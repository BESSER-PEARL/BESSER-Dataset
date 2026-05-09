





import java.util.List;
import java.util.ArrayList;

public class QVTCore_CorePattern extends Pattern {






    private List<Variable> variables;


    public QVTCore_CorePattern(
    ) {
        super(
        );
        this.variables = new ArrayList<>();
    }

    public QVTCore_CorePattern(
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