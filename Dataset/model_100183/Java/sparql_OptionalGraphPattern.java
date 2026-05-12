





import java.util.List;
import java.util.ArrayList;

public class sparql_OptionalGraphPattern extends GraphPattern {






    private List<sparql_GroupGraphPattern> sparql_groupgraphpatterns;


    public sparql_OptionalGraphPattern(
    ) {
        super(
        );
        this.sparql_groupgraphpatterns = new ArrayList<>();
    }

    public sparql_OptionalGraphPattern(
        ArrayList<sparql_GroupGraphPattern> sparql_groupgraphpatterns    ) {
        this.sparql_groupgraphpatterns = sparql_groupgraphpatterns;
    }


    public List<sparql_GroupGraphPattern> getSparql_groupgraphpatterns() {
        return sparql_groupgraphpatterns;
    }

    public void addSparql_groupgraphpattern(Sparql_groupgraphpattern sparql_groupgraphpattern) {
        this.sparql_groupgraphpatterns.add(sparql_groupgraphpattern);
    }

}