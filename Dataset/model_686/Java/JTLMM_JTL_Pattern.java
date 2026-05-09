





import java.util.List;
import java.util.ArrayList;

public class JTLMM_JTL_Pattern extends Element {






    private List<Variable> variables;


    public JTLMM_JTL_Pattern(
    ) {
        super(
        );
        this.variables = new ArrayList<>();
    }

    public JTLMM_JTL_Pattern(
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