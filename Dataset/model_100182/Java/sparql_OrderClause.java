





import java.util.List;
import java.util.ArrayList;

public class sparql_OrderClause extends LocatedElement {






    private sparql_SolutionModifier sparql_solutionmodifier;




    private List<sparql_OrderCondition> sparql_orderconditions;


    public sparql_OrderClause(
    ) {
        super(
        );
        this.sparql_orderconditions = new ArrayList<>();
    }

    public sparql_OrderClause(
        ArrayList<sparql_OrderCondition> sparql_orderconditions    ) {
        this.sparql_orderconditions = sparql_orderconditions;
    }


    public sparql_SolutionModifier getSparql_solutionmodifier() {
        return sparql_solutionmodifier;
    }

    public void setSparql_solutionmodifier(sparql_SolutionModifier sparql_solutionmodifier) {
        this.sparql_solutionmodifier = sparql_solutionmodifier;
    }
    public List<sparql_OrderCondition> getSparql_orderconditions() {
        return sparql_orderconditions;
    }

    public void addSparql_ordercondition(Sparql_ordercondition sparql_ordercondition) {
        this.sparql_orderconditions.add(sparql_ordercondition);
    }

}