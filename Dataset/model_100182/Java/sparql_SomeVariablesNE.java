





import java.util.List;
import java.util.ArrayList;

public class sparql_SomeVariablesNE extends VariablesNE {






    private List<sparql_Var> sparql_vars;


    public sparql_SomeVariablesNE(
    ) {
        super(
        );
        this.sparql_vars = new ArrayList<>();
    }

    public sparql_SomeVariablesNE(
        ArrayList<sparql_Var> sparql_vars    ) {
        this.sparql_vars = sparql_vars;
    }


    public List<sparql_Var> getSparql_vars() {
        return sparql_vars;
    }

    public void addSparql_var(Sparql_var sparql_var) {
        this.sparql_vars.add(sparql_var);
    }

}