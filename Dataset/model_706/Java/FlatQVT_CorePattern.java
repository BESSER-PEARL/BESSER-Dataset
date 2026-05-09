





import java.util.List;
import java.util.ArrayList;

public class FlatQVT_CorePattern extends Pattern {






    private List<Variable> variables;


    public FlatQVT_CorePattern(
    ) {
        super(
        );
        this.variables = new ArrayList<>();
    }

    public FlatQVT_CorePattern(
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