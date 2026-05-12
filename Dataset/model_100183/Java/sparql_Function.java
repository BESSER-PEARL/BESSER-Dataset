





import java.util.List;
import java.util.ArrayList;

public class sparql_Function extends FilterNode, Constraint, GroupCondition {

    private String name;





    private List<sparql_Variable> sparql_variables;


    public sparql_Function(
        String name    ) {
        super(
        );
        this.name = name;
        this.sparql_variables = new ArrayList<>();
    }

    public sparql_Function(
        String name        ArrayList<sparql_Variable> sparql_variables    ) {
        this.name = name;
        this.sparql_variables = sparql_variables;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<sparql_Variable> getSparql_variables() {
        return sparql_variables;
    }

    public void addSparql_variable(Sparql_variable sparql_variable) {
        this.sparql_variables.add(sparql_variable);
    }

}