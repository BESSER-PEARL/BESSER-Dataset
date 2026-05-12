





import java.util.List;
import java.util.ArrayList;

public class sparql_TriplesSameSubject extends GraphPattern {






    private sparql_GraphNode sparql_graphnode;




    private List<sparql_PropertyList> sparql_propertylists;


    public sparql_TriplesSameSubject(
    ) {
        super(
        );
        this.sparql_propertylists = new ArrayList<>();
    }

    public sparql_TriplesSameSubject(
        ArrayList<sparql_PropertyList> sparql_propertylists    ) {
        this.sparql_propertylists = sparql_propertylists;
    }


    public sparql_GraphNode getSparql_graphnode() {
        return sparql_graphnode;
    }

    public void setSparql_graphnode(sparql_GraphNode sparql_graphnode) {
        this.sparql_graphnode = sparql_graphnode;
    }
    public List<sparql_PropertyList> getSparql_propertylists() {
        return sparql_propertylists;
    }

    public void addSparql_propertylist(Sparql_propertylist sparql_propertylist) {
        this.sparql_propertylists.add(sparql_propertylist);
    }

}