





import java.util.List;
import java.util.ArrayList;

public class sparql_Collection extends TriplesNode {






    private List<sparql_GraphNode> sparql_graphnodes;


    public sparql_Collection(
    ) {
        super(
        );
        this.sparql_graphnodes = new ArrayList<>();
    }

    public sparql_Collection(
        ArrayList<sparql_GraphNode> sparql_graphnodes    ) {
        this.sparql_graphnodes = sparql_graphnodes;
    }


    public List<sparql_GraphNode> getSparql_graphnodes() {
        return sparql_graphnodes;
    }

    public void addSparql_graphnode(Sparql_graphnode sparql_graphnode) {
        this.sparql_graphnodes.add(sparql_graphnode);
    }

}