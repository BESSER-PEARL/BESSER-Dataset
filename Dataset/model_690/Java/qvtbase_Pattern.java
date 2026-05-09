





import java.util.List;
import java.util.ArrayList;

public class qvtbase_Pattern extends Element {






    private List<Variable> variables;


    public qvtbase_Pattern(
    ) {
        super(
        );
        this.variables = new ArrayList<>();
    }

    public qvtbase_Pattern(
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