





import java.util.List;
import java.util.ArrayList;

public class noop_Method extends Member {






    private List<noop_Variable> noop_variables;


    public noop_Method(
    ) {
        super(
        );
        this.noop_variables = new ArrayList<>();
    }

    public noop_Method(
        ArrayList<noop_Variable> noop_variables    ) {
        this.noop_variables = noop_variables;
    }


    public List<noop_Variable> getNoop_variables() {
        return noop_variables;
    }

    public void addNoop_variable(Noop_variable noop_variable) {
        this.noop_variables.add(noop_variable);
    }

}